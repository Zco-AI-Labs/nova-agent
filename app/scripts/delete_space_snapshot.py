import logging
from app.core import hubscape_adk

logger = logging.getLogger(__name__)

@hubscape_adk.require_tool_privilege
def delete_space_snapshot(target: str) -> dict:
    """
    Removes a captured telescope snapshot from your personal log.

    Args:
        target: The name of the celestial target snapshot to delete.
    """
    try:
        ctx = hubscape_adk.get_context()
        filename = f"{target.lower().replace(' ', '_')}.jpg"
        
        ctx.delete_file(scope="user", filename=filename)
        return {"status": "success", "message": f"Deleted {target} from logs."}
    except Exception as e:
        logger.error(f"Error in delete_space_snapshot: {e}", exc_info=True)
        return {"status": "error", "message": f"Failed to delete {target}: {str(e)}"}
