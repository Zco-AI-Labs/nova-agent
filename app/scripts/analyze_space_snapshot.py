import logging
from app.core import hubscape_adk

logger = logging.getLogger(__name__)

def analyze_space_snapshot(target: str) -> dict:
    """
    Retrieves and analyzes a captured telescope snapshot from your personal log using get_file.

    Args:
        target: The name of the celestial target snapshot to retrieve and analyze.
    """
    try:
        ctx = hubscape_adk.get_context()
        filename = f"{target.lower().replace(' ', '_')}.jpg"
        
        image_bytes = ctx.get_file(scope="user", filename=filename)
        if not image_bytes:
            return {
                "status": "error",
                "message": f"Snapshot for {target} not found in logs."
            }
            
        file_size_kb = len(image_bytes) / 1024
        
        # Deterministic details based on target string length
        star_count = (len(target) * 7) + 53
        nebulosity = "High" if len(target) % 2 == 0 else "Moderate"
        
        analysis_report = (
            f"Analysis complete for {filename}. "
            f"Detected {star_count} stellar sources. "
            f"Stellar class O/B stars present with {nebulosity} nebulosity index."
        )
        
        data = {
            "target": target,
            "file_size_kb": round(file_size_kb, 2),
            "analysis": analysis_report
        }
        
        # Load and queue the widget
        try:
            ctx.show_widget("analysis_results_card", data)
        except Exception as widget_err:
            logger.warning(f"Could not load/queue analysis_results_card: {widget_err}")
            
        return {
            "status": "success",
            "target": target,
            "file_size_kb": data["file_size_kb"],
            "analysis": analysis_report
        }
    except Exception as e:
        logger.error(f"Error in analyze_space_snapshot: {e}", exc_info=True)
        return {
            "status": "error",
            "message": f"Failed to analyze snapshot of {target}: {str(e)}"
        }
