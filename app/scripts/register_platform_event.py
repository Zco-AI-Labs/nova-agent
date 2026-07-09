import uuid
import logging
from app.core import hubscape_adk

logger = logging.getLogger(__name__)

@hubscape_adk.require_tool_privilege
def register_platform_event(event_name: str, event_date: str) -> dict:
    """
    Adds a shared space event (e.g. meteor shower) to the platform calendar.

    Args:
        event_name: The name of the astronomical event.
        event_date: The date of the event (e.g. 'August 12th').
    """
    try:
        ctx = hubscape_adk.get_context()
        event_id = str(uuid.uuid4())[:8]
        
        data = {
            "name": event_name,
            "date": event_date,
            "type": "astronomy_alert"
        }
        
        # Save to Platform Firestore Scope
        res = ctx.save(scope="platform", collection_name="events", doc_id=event_id, data=data)
        
        # Queue/show the widget event_calendar_card
        try:
            ctx.show_widget("event_calendar_card", {
                "event_id": event_id,
                "event_name": event_name,
                "event_date": event_date
            })
        except Exception as widget_err:
            logger.warning(f"Could not load/queue event_calendar_card: {widget_err}")
            
        return {
            "status": "success",
            "event_id": event_id,
            "data": res
        }
    except Exception as e:
        logger.error(f"Error in register_platform_event: {e}", exc_info=True)
        return {
            "status": "error",
            "message": f"Failed to register platform event: {str(e)}"
        }
