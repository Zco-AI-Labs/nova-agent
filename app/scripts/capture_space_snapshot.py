import os
import urllib.request
import urllib.parse
import json
import logging
from app.core import hubscape_adk

logger = logging.getLogger(__name__)

@hubscape_adk.require_tool_privilege
def capture_space_snapshot(target: str) -> dict:
    """
    Captures a telescope image of a target celestial object (e.g., 'andromeda', 'orion')
    by fetching the NASA Astronomy Picture of the Day (APOD) image (or a public NASA image library url),
    downloading the raw bytes, and saving it to the user's personal GCS space.

    Args:
        target: The name of the celestial target to snapshot.
    """
    try:
        ctx = hubscape_adk.get_context()
        
        # 1. Fetch NASA APOD image or fallback
        api_key = os.environ.get("NASA_API_KEY") or "DEMO_KEY"
        apod_url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
        
        image_url = None
        
        try:
            req = urllib.request.Request(apod_url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=5) as response:
                if response.status == 200:
                    raw_bytes = response.read()
                    data = json.loads(raw_bytes.decode())
                    if data.get("media_type") == "image":
                        image_url = data.get("url") or data.get("hdurl")
        except Exception as e:
            logger.warning(f"Failed to query NASA APOD API: {e}. Falling back to static image.")
            
        # 2. Fallback to a high-quality static Hubble space image if APOD fails or returns non-image
        if not image_url:
            image_url = "https://upload.wikimedia.org/wikipedia/commons/c/c3/NGC_4414_%28NASA-ESA%29.jpg"
            
        # 3. Retrieve raw image bytes
        image_bytes = None
        try:
            req = urllib.request.Request(image_url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=5) as response:
                if response.status == 200:
                    image_bytes = response.read()
        except Exception as e:
            logger.error(f"Failed to download image from {image_url}: {e}")
            raise RuntimeError(f"Failed to fetch telescope image bytes: {e}")
            
        if not image_bytes:
            raise RuntimeError("Fetched telescope image content was empty.")
            
        filename = f"{target.lower().replace(' ', '_')}.jpg"
        
        # 4. Save to User GCS Scope
        res = ctx.save_file(
            scope="user", 
            filename=filename, 
            content=image_bytes, 
            content_type="image/jpeg"
        )
        
        # 5. Load and display the widget
        try:
            ctx.show_widget("snapshot_detail_card", {
                "target": target,
                "image_url": res["download_url"]
            })
        except Exception as widget_err:
            logger.warning(f"Could not load/queue snapshot_detail_card: {widget_err}")
            
        return {
            "status": "success",
            "message": f"Successfully captured {target}",
            "image_url": res["download_url"]
        }
    except Exception as e:
        logger.error(f"Error in capture_space_snapshot: {e}", exc_info=True)
        return {
            "status": "error",
            "message": f"Failed to capture snapshot of {target}: {str(e)}"
        }
