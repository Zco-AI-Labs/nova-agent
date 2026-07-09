## 🎨 7. User Interface & Widgets Specification

This section outlines the UI templates used by the Nova Agent to render telescope captures and event registrations in the Chat UI.

### Widget 1: `snapshot_detail_card`
*   **Type:** Detail Card
*   **Theme Token Default:** `indigo`
*   **Layout JSON Structure:**
```json
// app/ui/widgets/snapshot_detail_card.json
{
  "type": "container",
  "props": {
    "direction": "vertical",
    "gap": "md",
    "padding": "md"
  },
  "children": [
    {
      "type": "text",
      "props": {
        "text": "Deep-Space Observation Captured",
        "size": "lg",
        "weight": "bold",
        "color": "indigo"
      }
    },
    {
      "type": "image",
      "props": {
        "url": "{{data.image_url}}",
        "alt": "Telescope capture of {{data.target}}",
        "aspectRatio": "16:9",
        "borderRadius": "md"
      }
    },
    {
      "type": "text",
      "props": {
        "text": "Target: {{data.target}}",
        "size": "md",
        "weight": "medium"
      }
    },
    {
      "type": "button",
      "props": {
        "label": "Delete Snapshot",
        "actionUrl": "agent://delete_space_snapshot?target={{data.target}}",
        "styling": {
          "colorTheme": "red"
        }
      }
    }
  ]
}
```

---

### Widget 2: `event_calendar_card`
*   **Type:** Calendar Card
*   **Theme Token Default:** `amber`
*   **Layout JSON Structure:**
```json
// app/ui/widgets/event_calendar_card.json
{
  "type": "container",
  "props": {
    "direction": "vertical",
    "gap": "sm",
    "padding": "md"
  },
  "children": [
    {
      "type": "text",
      "props": {
        "text": "Platform Astronomy Alert",
        "size": "lg",
        "weight": "bold",
        "color": "amber"
      }
    },
    {
      "type": "container",
      "props": {
        "direction": "horizontal",
        "gap": "sm",
        "align": "center"
      },
      "children": [
        {
          "type": "text",
          "props": {
            "text": "📅 Date: {{data.event_date}}",
            "size": "sm",
            "weight": "medium"
          }
        },
        {
          "type": "text",
          "props": {
            "text": "📌 ID: {{data.event_id}}",
            "size": "sm",
            "color": "secondary"
          }
        }
      ]
    },
    {
      "type": "text",
      "props": {
        "text": "Event: {{data.event_name}}",
        "size": "md"
      }
    }
  ]
}
```

---

### Widget 3: `wallpaper_preview_card`
*   **Type:** Wallpaper Card
*   **Theme Token Default:** `violet`
*   **Layout JSON Structure:**
```json
// app/ui/widgets/wallpaper_preview_card.json
{
  "type": "container",
  "props": {
    "direction": "vertical",
    "gap": "md",
    "padding": "md"
  },
  "children": [
    {
      "type": "text",
      "props": {
        "text": "Platform Wallpaper Set",
        "size": "lg",
        "weight": "bold",
        "color": "violet"
      }
    },
    {
      "type": "image",
      "props": {
        "url": "{{data.wallpaper_url}}",
        "alt": "Platform Background Preview",
        "aspectRatio": "16:9",
        "borderRadius": "md"
      }
    },
    {
      "type": "text",
      "props": {
        "text": "Successfully uploaded background: {{data.wallpaper_name}}",
        "size": "sm"
      }
    }
  ]
}

---

### Widget 4: `analysis_results_card`
*   **Type:** Detail Card
*   **Theme Token Default:** `emerald`
*   **Layout JSON Structure:**
```json
// app/ui/widgets/analysis_results_card.json
{
  "type": "container",
  "props": {
    "direction": "vertical",
    "gap": "sm",
    "padding": "md"
  },
  "children": [
    {
      "type": "text",
      "props": {
        "text": "Astrophotography Analysis Report",
        "size": "lg",
        "weight": "bold",
        "color": "emerald"
      }
    },
    {
      "type": "container",
      "props": {
        "direction": "horizontal",
        "gap": "sm"
      },
      "children": [
        {
          "type": "text",
          "props": {
            "text": "Target Object: {{data.target}}",
            "size": "md",
            "weight": "medium"
          }
        },
        {
          "type": "text",
          "props": {
            "text": "File Size: {{data.file_size_kb}} KB",
            "size": "sm",
            "color": "secondary"
          }
        }
      ]
    },
    {
      "type": "text",
      "props": {
        "text": "{{data.analysis}}",
        "size": "sm"
      }
    }
  ]
}
```

