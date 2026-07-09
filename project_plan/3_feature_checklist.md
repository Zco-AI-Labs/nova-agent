## 📂 3. Feature Checklist & Interaction Modes

### Feature 1: Capture Space Snapshot
*   **Description:** Generates/acquires telescope imagery of a specified celestial body and uploads it to the user's personal storage (User Scope GCS).
*   **Visual Interaction Mode:**
    *   *Trigger:* "Take a snapshot of the Orion Nebula and save it."
    *   *UI Rendered:* A custom image detail card showcasing the newly captured astrophotography image and the generated public download URL.
    *   *Form Actions:* Button to delete the snapshot, button to download.
*   **Non-Visual Interaction Mode (SMS/Voice Fallback):**
    *   *SMS Transcript Flow:*
        *   User: `Capture Orion Nebula`
        *   Agent: `Successfully captured Orion Nebula! The image has been saved to your personal log.`
    *   *Voice/Phone Flow:*
        *   User: `Take a snapshot of Orion Nebula`
        *   Agent: `Successfully captured Orion Nebula. I have saved it to your log.`
    *   *Natural Language Parameters Extracted:* `target` (string)
*   **Acceptance Criteria (Given-When-Then):**
    *   *Scenario A (Happy Path):*
        *   **GIVEN** the user asks to capture a valid celestial target.
        *   **WHEN** the capture tool is triggered.
        *   **THEN** the telescope mocks the image bytes, saves it to the user GCS path, and returns the GCS download URL.
    *   *Scenario B (Fallback/Error Path):*
        *   **GIVEN** the telescope simulator fails to resolve the requested object.
        *   **WHEN** the capture tool is triggered.
        *   **THEN** the agent returns a descriptive error message and prompts the user to select another target object.

---

### Feature 2: Delete Space Snapshot
*   **Description:** Deletes a previously captured space snapshot from the user's personal log (User Scope GCS).
*   **Visual Interaction Mode:**
    *   *Trigger:* "Delete my snapshot of Orion."
    *   *UI Rendered:* A text notification or status badge confirming successful removal.
    *   *Form Actions:* None.
*   **Non-Visual Interaction Mode (SMS/Voice Fallback):**
    *   *SMS Transcript Flow:*
        *   User: `Delete Orion snapshot`
        *   Agent: `Deleted Orion from logs.`
    *   *Voice/Phone Flow:*
        *   User: `Delete my Orion snapshot`
        *   Agent: `Deleted Orion from your logs.`
    *   *Natural Language Parameters Extracted:* `target` (string)
*   **Acceptance Criteria (Given-When-Then):**
    *   *Scenario A (Happy Path):*
        *   **GIVEN** a file named `orion.jpg` exists in the user's scope storage.
        *   **WHEN** the user requests to delete it.
        *   **THEN** the deletion call succeeds, and the file is removed from storage.
    *   *Scenario B (Fallback/Error Path):*
        *   **GIVEN** no file named `orion.jpg` exists in the user's scope storage.
        *   **WHEN** the user requests to delete it.
        *   **THEN** the agent notifies the user that the snapshot was not found in their logs.

---

### Feature 3: Register Platform Astronomy Event
*   **Description:** Registers an upcoming astronomical event in the shared platform-wide event database (Platform Scope Firestore).
*   **Visual Interaction Mode:**
    *   *Trigger:* "Add a platform-wide event for the Perseid Meteor Shower happening on August 12th."
    *   *UI Rendered:* An updated calendar widget or event list displaying the new event details.
    *   *Form Actions:* None.
*   **Non-Visual Interaction Mode (SMS/Voice Fallback):**
    *   *SMS Transcript Flow:*
        *   User: `Register event Perseid Meteor Shower on August 12th`
        *   Agent: `Event 'Perseid Meteor Shower' registered successfully under ID a1b2c3d4.`
    *   *Voice/Phone Flow:*
        *   User: `Register the Perseid Meteor Shower for August twelfth`
        *   Agent: `Registered the Perseid Meteor Shower for August twelfth. The event ID is a1b2c3d4.`
    *   *Natural Language Parameters Extracted:* `event_name` (string), `event_date` (string)
*   **Acceptance Criteria (Given-When-Then):**
    *   *Scenario A (Happy Path):*
        *   **GIVEN** the caller has permission to edit platform-level data.
        *   **WHEN** the user registers an event with a name and date.
        *   **THEN** the details are saved in Platform Firestore with a random 8-character ID, returning success.
    *   *Scenario B (Fallback/Error Path):*
        *   **GIVEN** the platform database connection is down.
        *   **WHEN** the registration is triggered.
        *   **THEN** the agent informs the user that database storage is temporarily unavailable.

---

### Feature 4: Set Platform Wallpaper
*   **Description:** Uploads a shared desktop/hub wallpaper visible to all users (Platform Scope GCS).
*   **Visual Interaction Mode:**
    *   *Trigger:* "Set the platform wallpaper to deep_space."
    *   *UI Rendered:* A confirmation preview showing the newly active wallpaper.
    *   *Form Actions:* Button to revert, button to download.
*   **Non-Visual Interaction Mode (SMS/Voice Fallback):**
    *   *SMS Transcript Flow:*
        *   User: `Set platform wallpaper deep_space`
        *   Agent: `Successfully uploaded deep_space as the new platform wallpaper.`
    *   *Voice/Phone Flow:*
        *   User: `Set the platform wallpaper to deep space`
        *   Agent: `Successfully uploaded deep space as the new platform wallpaper.`
    *   *Natural Language Parameters Extracted:* `wallpaper_name` (string)
*   **Acceptance Criteria (Given-When-Then):**
    *   *Scenario A (Happy Path):*
        *   **GIVEN** the caller has platform permissions.
        *   **WHEN** a wallpaper name is provided.
        *   **THEN** the mock wallpaper bytes are uploaded to Platform GCS and a success response with the image URL is returned.
    *   *Scenario B (Fallback/Error Path):*
        *   **GIVEN** the platform file storage is read-only or full.
        *   **WHEN** the upload is attempted.
        *   **THEN** the agent returns a permission or storage capacity error.

---

### Feature 5: Analyze Space Snapshot
*   **Description:** Retrieves a captured space snapshot from the user's log (User Scope GCS) and analyses its details (e.g. file size and astronomical data).
*   **Visual Interaction Mode:**
    *   *Trigger:* "Analyze my snapshot of Orion."
    *   *UI Rendered:* An analysis results panel showing detected stars, nebulosity levels, and image metadata.
    *   *Form Actions:* None.
*   **Non-Visual Interaction Mode (SMS/Voice Fallback):**
    *   *SMS Transcript Flow:*
        *   User: `Analyze Orion snapshot`
        *   Agent: `Analysis complete. Target: Orion. Size: 154 KB. Detected high nebulosity.`
    *   *Voice/Phone Flow:*
        *   User: `Analyze my Orion snapshot`
        *   Agent: `I have analyzed your Orion snapshot. The file is 154 kilobytes. It shows high nebulosity.`
    *   *Natural Language Parameters Extracted:* `target` (string)
*   **Acceptance Criteria (Given-When-Then):**
    *   *Scenario A (Happy Path):*
        *   **GIVEN** a file named `orion.jpg` exists in the user's scope storage.
        *   **WHEN** the analyze snapshot tool is triggered.
        *   **THEN** the agent retrieves the file content bytes via get_file, performs analysis, and returns success details.
    *   *Scenario B (Fallback/Error Path):*
        *   **GIVEN** no file named `orion.jpg` exists in the user's scope storage.
        *   **WHEN** the analyze snapshot tool is triggered.
        *   **THEN** the agent returns an error stating the snapshot was not found.

