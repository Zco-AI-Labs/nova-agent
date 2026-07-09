## 🛠️ 5. Architecture & Capabilities

### System Instructions (`app/SKILL.md`)
```markdown
---
name: nova-agent
description: "Observatory assistant that logs telescope snapshots and shares platform-wide space event notifications."
---
You are Nova, an AI space observatory assistant. You help users capture telescopic snapshots, manage their observation logs, and maintain the platform's public space event calendar.

Format your output using clean markdown. When showing space snapshots, display the inline GCS download URL as a markdown image link: `![Nebula](url)`.
```

### Tool Implementations (`app/scripts/`)

#### 1. Capture Space Snapshot
```python
# app/scripts/capture_space_snapshot.py
import app.core.hubscape_adk

@app.core.hubscape_adk.require_tool_privilege
def capture_space_snapshot(target: str) -> dict:
    """
    Captures a telescope image of a target celestial object (e.g., 'andromeda', 'orion')
    by fetching the NASA Astronomy Picture of the Day (APOD) image (or a public NASA image library url),
    downloading the raw bytes, and saving it to the user's personal GCS space.

    Args:
        target: The name of the celestial target to snapshot.
    """
    # Tool implementation logic:
    # 1. Fetch APOD metadata from NASA API (e.g., https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY).
    # 2. Extract image URL (and fallback to static NASA hubble image if APOD returns a video or fails).
    # 3. Retrieve raw image bytes using requests/urllib.
    # 4. Upload to user GCS scope via RemoteContext.save_file.
    # 5. Return success status and the GCS download URL.

```

#### 2. Delete Space Snapshot
```python
# app/scripts/delete_space_snapshot.py
import app.core.hubscape_adk

@app.core.hubscape_adk.require_tool_privilege
def delete_space_snapshot(target: str) -> dict:
    """
    Removes a captured telescope snapshot from your personal log.

    Args:
        target: The name of the celestial target snapshot to delete.
    """
    # Tool implementation logic...
```

#### 3. Register Platform Astronomy Event
```python
# app/scripts/register_platform_event.py
import app.core.hubscape_adk

@app.core.hubscape_adk.require_tool_privilege
def register_platform_event(event_name: str, event_date: str) -> dict:
    """
    Adds a shared space event (e.g. meteor shower) to the platform calendar.

    Args:
        event_name: The name of the astronomical event.
        event_date: The date of the event (e.g. 'August 12th').
    """
    # Tool implementation logic...
```

#### 4. Set Platform Wallpaper
```python
# app/scripts/set_platform_wallpaper.py
import app.core.hubscape_adk

@app.core.hubscape_adk.require_tool_privilege
def set_platform_wallpaper(wallpaper_name: str) -> dict:
    """
    Uploads a new default background wallpaper visible to all users of the platform.

    Args:
        wallpaper_name: The name of the wallpaper to set.
    """
    # Tool implementation logic...
```

#### 5. Analyze Space Snapshot
```python
# app/scripts/analyze_space_snapshot.py
import app.core.hubscape_adk

@app.core.hubscape_adk.require_tool_privilege
def analyze_space_snapshot(target: str) -> dict:
    """
    Retrieves and analyzes a captured telescope snapshot from your personal log using get_file.

    Args:
        target: The name of the celestial target snapshot to retrieve and analyze.
    """
    # Tool implementation logic...
```

### 🔑 Tool Privileges Matrix

| Privilege Name | Description of Granted Capabilities / Tools |
| :--- | :--- |
| `ADMIN` | Allows modifying platform resources (e.g., `register_platform_event`, `set_platform_wallpaper`). |
| `USER` | Allows capturing, deleting, and analyzing personal snapshots (e.g., `capture_space_snapshot`, `delete_space_snapshot`, `analyze_space_snapshot`). |

### Model Context Protocol (MCP) & Agent-to-Agent (A2A) Connections
This agent does not require any external MCP or A2A connections.

### Required Secrets (Agent Secrets Vault)
Define any external API keys or client secrets that must be configured and uploaded to the platform Secrets Vault.

| Secret Name | Description | Required? (True/False) |
| :--- | :--- | :--- |
| `NASA_API_KEY` | Key for querying NASA's Astronomy Picture of the Day (APOD) API. Defaults to 'DEMO_KEY' if not configured. | False |

