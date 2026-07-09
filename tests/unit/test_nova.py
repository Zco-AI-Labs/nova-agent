from unittest.mock import MagicMock, patch
import pytest
from app.scripts.capture_space_snapshot import capture_space_snapshot
from app.scripts.delete_space_snapshot import delete_space_snapshot
from app.scripts.analyze_space_snapshot import analyze_space_snapshot
from app.scripts.register_platform_event import register_platform_event
from app.scripts.set_platform_wallpaper import set_platform_wallpaper

@pytest.fixture
def mock_context():
    with patch("app.core.hubscape_adk.get_context") as mock_get_context:
        ctx = MagicMock()
        mock_get_context.return_value = ctx
        yield ctx

def test_capture_space_snapshot_success(mock_context):
    # Mock GCS response
    mock_context.save_file.return_value = {
        "storage_path": "agents/nova_agent/user/test_user/orion.jpg",
        "download_url": "https://download.url/orion.jpg"
    }
    
    with patch("app.scripts.capture_space_snapshot.generate_space_image") as mock_gen:
        mock_gen.return_value = b"mocked_image_bytes"
        
        res = capture_space_snapshot("Orion")
        
        assert res["status"] == "success"
        assert res["image_url"] == "https://download.url/orion.jpg"
        mock_gen.assert_called_once_with("A beautiful high-quality photographic space telescope image of the celestial object: Orion.")
        mock_context.save_file.assert_called_once_with(
            scope="user",
            filename="orion.jpg",
            content=b"mocked_image_bytes",
            content_type="image/jpeg"
        )
        mock_context.show_widget.assert_called_once_with(
            "snapshot_detail_card",
            {"target": "Orion", "image_url": "https://download.url/orion.jpg"}
        )

def test_delete_space_snapshot_success(mock_context):
    res = delete_space_snapshot("Orion")
    assert res["status"] == "success"
    mock_context.delete_file.assert_called_once_with(scope="user", filename="orion.jpg")

def test_analyze_space_snapshot_success(mock_context):
    mock_context.get_file.return_value = b"mocked_image_bytes_length_18"
    
    res = analyze_space_snapshot("Orion")
    assert res["status"] == "success"
    assert "Detected 88 stellar sources" in res["analysis"]
    mock_context.get_file.assert_called_once_with(scope="user", filename="orion.jpg")
    mock_context.show_widget.assert_called_once_with(
        "analysis_results_card",
        {
            "target": "Orion",
            "file_size_kb": 0.03, # 28 / 1024
            "analysis": res["analysis"]
        }
    )

def test_register_platform_event_success(mock_context):
    mock_context.save.return_value = {"status": "saved"}
    
    res = register_platform_event("Perseid Meteor Shower", "August 12th")
    assert res["status"] == "success"
    assert len(res["event_id"]) == 8
    
    mock_context.save.assert_called_once()
    mock_context.show_widget.assert_called_once_with(
        "event_calendar_card",
        {
            "event_id": res["event_id"],
            "event_name": "Perseid Meteor Shower",
            "event_date": "August 12th"
        }
    )

def test_set_platform_wallpaper_success(mock_context):
    mock_context.save_file.return_value = {
        "storage_path": "agents/nova_agent/platform/wallpapers/deep_space.jpg",
        "download_url": "https://download.url/deep_space.jpg"
    }
    
    with patch("app.scripts.set_platform_wallpaper.generate_space_image") as mock_gen:
        mock_gen.return_value = b"mocked_wallpaper_bytes"
        
        res = set_platform_wallpaper("deep_space")
        assert res["status"] == "success"
        assert res["wallpaper_url"] == "https://download.url/deep_space.jpg"
        mock_gen.assert_called_once_with("A beautiful high-resolution astronomical wallpaper themed around: deep_space.")
        
        mock_context.save_file.assert_called_once_with(
            scope="platform",
            filename="wallpapers/deep_space.jpg",
            content=b"mocked_wallpaper_bytes",
            content_type="image/jpeg"
        )
        mock_context.show_widget.assert_called_once_with(
            "wallpaper_preview_card",
            {"wallpaper_name": "deep_space", "wallpaper_url": "https://download.url/deep_space.jpg"}
        )
