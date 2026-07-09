import os
import urllib.request
import json
import logging
from app.core import hubscape_adk

logger = logging.getLogger(__name__)

@hubscape_adk.require_tool_privilege
def set_platform_wallpaper(wallpaper_name: str) -> dict:
    """
    Uploads a new default background wallpaper visible to all users of the platform.

    Args:
        wallpaper_name: The name of the wallpaper to set.
    """
    try:
        ctx = hubscape_adk.get_context()
        
        # 1. Fetch space image from NASA or fallback
        api_key = os.environ.get("NASA_API_KEY") or "DEMO_KEY"
        apod_url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
        
        image_url = None
        
        try:
            req = urllib.request.Request(apod_url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=5) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode())
                    if data.get("media_type") == "image":
                        image_url = data.get("url") or data.get("hdurl")
        except Exception as e:
            logger.warning(f"Failed to query NASA APOD API: {e}. Falling back to static image.")
            
        # 2. Fallback to a high-quality static wallpaper space image if APOD fails or returns non-image
        if not image_url:
            image_url = "https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_Hubble_Space_Telescope%27s_hubble_extreme_deep_field.jpg"
            
        # 3. Retrieve raw image bytes
        image_bytes = None
        try:
            req = urllib.request.Request(image_url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=5) as response:
                if response.status == 200:
                    image_bytes = response.read()
        except Exception as e:
            logger.error(f"Failed to download image from {image_url}: {e}")
            raise RuntimeError(f"Failed to fetch wallpaper image bytes: {e}")
            
        if not image_bytes:
            raise RuntimeError("Fetched wallpaper image content was empty.")
            
        filename = f"wallpapers/{wallpaper_name.lower().replace(' ', '_')}.jpg"
        
        # 4. Save to Platform GCS Scope
        res = ctx.save_file(
            scope="platform", 
            filename=filename, 
            content=image_bytes, 
            content_type="image/jpeg"
        )
        
        # 5. Load and display the widget
        try:
            ctx.show_widget("wallpaper_preview_card", {
                "wallpaper_name": wallpaper_name,
                "wallpaper_url": res["download_url"]
            })
        except Exception as widget_err:
            logger.warning(f"Could not load/queue wallpaper_preview_card: {widget_err}")
            
        return {
            "status": "success",
            "wallpaper_url": res["download_url"]
        }
    except Exception as e:
        logger.error(f"Error in set_platform_wallpaper: {e}", exc_info=True)
        return {
            "status": "error",
            "message": f"Failed to set platform wallpaper: {str(e)}"
        }
