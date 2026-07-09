## 💾 6. Data Architecture & DB Schemas

This section documents the database collection structure and file storage scopes used by the Nova Agent.

### 🏢 Firestore Database Collections

#### Collection: `events`
*   **Scope:** `platform`
*   **Resolved Path:** `agents/{agent_id}/agent_data/platform/events`
*   **Document ID Format:** 8-character alphanumeric string (derived from uuid)

##### Fields Table
| Field Name | Type | Description | Mandatory / Optional |
| :--- | :--- | :--- | :--- |
| `id` | `String` | Unique 8-character ID of the platform event. | Mandatory |
| `name` | `String` | The display name of the space event (e.g., "Perseid Meteor Shower"). | Mandatory |
| `date` | `String` | The scheduled date of the event (e.g., "August 12th"). | Mandatory |
| `type` | `String` | Categorization type, set to `astronomy_alert`. | Mandatory |
| `created_at` | `Timestamp` | Injected automatically by context helpers. | Mandatory |
| `created_by` | `String` | Injected automatically by context helpers. | Mandatory |
| `updated_at` | `Timestamp` | Injected automatically by context helpers. | Mandatory |
| `updated_by` | `String` | Injected automatically by context helpers. | Mandatory |
| `version` | `Integer` | Injected automatically by context helpers. | Mandatory |

---

### 📁 Firebase / GCS Storage Scopes

File storage is partitioned by scopes under Firebase Storage:

#### 1. User Snapshot Storage
*   **Scope:** `user`
*   **Resolved GCS Path:** `agents/{agent_id}/user/{user_id}/{filename}`
*   **Example Filename:** `orion_nebula.jpg`
*   **Description:** Stores telescope captures private to individual users.

#### 2. Platform Wallpaper Storage
*   **Scope:** `platform`
*   **Resolved GCS Path:** `agents/{agent_id}/platform/{filename}`
*   **Example Filename:** `wallpapers/deep_space.jpg`
*   **Description:** Stores default background wallpapers available platform-wide.
