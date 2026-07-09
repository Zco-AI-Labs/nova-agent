## 💬 4. Interaction Scripts & Conversational Flows

### Scenario 1: Capturing a Space Snapshot

#### Flow A: Visual Path (Chat UI with widgets)
*   **User:** "Nova, take a snapshot of the Orion Nebula and add it to my log."
*   **Agent (Behind the Scenes):** Calls tool `capture_space_snapshot` with argument `target="Orion Nebula"`.
*   **Agent UI Rendered:** Displays Widget `snapshot_detail_card` showcasing the image and details.
*   **Agent Message:** "I've pointed the telescope to the Orion Nebula and captured a snapshot. It has been successfully saved to your personal observation log: ![Orion Nebula](https://storage.googleapis.com/hubscape-user-bucket/user123/orion_nebula.jpg)"

#### Flow B: Non-Visual SMS Path (No-UI, Text Only)
*   **User (SMS):** "Capture Orion Nebula"
*   **Agent (Behind the Scenes):** Calls tool `capture_space_snapshot` with argument `target="Orion Nebula"`.
*   **Agent Text Reply:** "Successfully captured Orion Nebula. Saved to your personal log."

#### Flow C: Non-Visual Voice Path (No-UI, Spoken Phone Call)
*   **User (Voice):** "Please take a snapshot of the Orion Nebula."
*   **Agent (Behind the Scenes):** Calls tool `capture_space_snapshot` with argument `target="Orion Nebula"`.
*   **Agent Speech Reply:** "Successfully captured the Orion Nebula. I have saved it to your personal observation log."

---

### Scenario 2: Deleting a Space Snapshot

#### Flow A: Visual Path (Chat UI with widgets)
*   **User:** "Delete my snapshot of Orion."
*   **Agent (Behind the Scenes):** Calls tool `delete_space_snapshot` with argument `target="Orion"`.
*   **Agent UI Rendered:** Displays Widget `status_notification` showing success.
*   **Agent Message:** "I have deleted the Orion snapshot from your personal log."

#### Flow B: Non-Visual SMS Path (No-UI, Text Only)
*   **User (SMS):** "Delete Orion"
*   **Agent (Behind the Scenes):** Calls tool `delete_space_snapshot` with argument `target="Orion"`.
*   **Agent Text Reply:** "Deleted Orion from logs."

#### Flow C: Non-Visual Voice Path (No-UI, Spoken Phone Call)
*   **User (Voice):** "Delete my Orion snapshot."
*   **Agent (Behind the Scenes):** Calls tool `delete_space_snapshot` with argument `target="Orion"`.
*   **Agent Speech Reply:** "Deleted Orion from your logs."

---

### Scenario 3: Registering a Platform-wide Astronomy Event

#### Flow A: Visual Path (Chat UI with widgets)
*   **User:** "Add a platform-wide event for the Perseid Meteor Shower happening on August 12th."
*   **Agent (Behind the Scenes):** Calls tool `register_platform_event` with arguments `event_name="Perseid Meteor Shower"` and `event_date="August 12th"`.
*   **Agent UI Rendered:** Displays Widget `event_calendar_card` showcasing the newly registered event.
*   **Agent Message:** "I have registered the Perseid Meteor Shower happening on August 12th on the platform calendar. Event ID: 8a4c1f9b."

#### Flow B: Non-Visual SMS Path (No-UI, Text Only)
*   **User (SMS):** "Register event Perseid Meteor Shower August 12th"
*   **Agent (Behind the Scenes):** Calls tool `register_platform_event` with arguments `event_name="Perseid Meteor Shower"` and `event_date="August 12th"`.
*   **Agent Text Reply:** "Registered Perseid Meteor Shower on August 12th. Event ID is 8a4c1f9b."

#### Flow C: Non-Visual Voice Path (No-UI, Spoken Phone Call)
*   **User (Voice):** "Register the Perseid Meteor Shower happening on August twelfth."
*   **Agent (Behind the Scenes):** Calls tool `register_platform_event` with arguments `event_name="Perseid Meteor Shower"` and `event_date="August 12th"`.
*   **Agent Speech Reply:** "I have registered the Perseid Meteor Shower on August twelfth. The event ID is eight a four c one f nine b."

---

### Scenario 4: Setting a Platform-wide Wallpaper

#### Flow A: Visual Path (Chat UI with widgets)
*   **User:** "Set the platform wallpaper to deep_space."
*   **Agent (Behind the Scenes):** Calls tool `set_platform_wallpaper` with argument `wallpaper_name="deep_space"`.
*   **Agent UI Rendered:** Displays Widget `wallpaper_preview_card`.
*   **Agent Message:** "Successfully uploaded deep_space as the new platform wallpaper: ![deep_space](https://storage.googleapis.com/hubscape-platform-bucket/wallpapers/deep_space.jpg)"

#### Flow B: Non-Visual SMS Path (No-UI, Text Only)
*   **User (SMS):** "Set wallpaper deep_space"
*   **Agent (Behind the Scenes):** Calls tool `set_platform_wallpaper` with argument `wallpaper_name="deep_space"`.
*   **Agent Text Reply:** "Successfully uploaded deep_space as the new platform wallpaper."

#### Flow C: Non-Visual Voice Path (No-UI, Spoken Phone Call)
*   **User (Voice):** "Set the platform wallpaper to deep space."
*   **Agent (Behind the Scenes):** Calls tool `set_platform_wallpaper` with argument `wallpaper_name="deep_space"`.
*   **Agent Speech Reply:** "Successfully uploaded deep space as the new platform wallpaper."

---

### Scenario 5: Analyzing a Space Snapshot

#### Flow A: Visual Path (Chat UI with widgets)
*   **User:** "Analyze my snapshot of Orion."
*   **Agent (Behind the Scenes):** Calls tool `analyze_space_snapshot` with argument `target="Orion"`.
*   **Agent UI Rendered:** Displays Widget `analysis_results_card` with data.
*   **Agent Message:** "Analysis complete for your Orion snapshot. Detected 142 stellar sources, stellar class O/B stars present, and high nebulosity."

#### Flow B: Non-Visual SMS Path (No-UI, Text Only)
*   **User (SMS):** "Analyze Orion snapshot"
*   **Agent (Behind the Scenes):** Calls tool `analyze_space_snapshot` with argument `target="Orion"`.
*   **Agent Text Reply:** "Analysis complete. Target: Orion. Size: 154 KB. Detected high nebulosity."

#### Flow C: Non-Visual Voice Path (No-UI, Spoken Phone Call)
*   **User (Voice):** "Analyze my Orion snapshot."
*   **Agent (Behind the Scenes):** Calls tool `analyze_space_snapshot` with argument `target="Orion"`.
*   **Agent Speech Reply:** "I have completed the analysis for your Orion snapshot. It is one hundred fifty-four kilobytes and shows high nebulosity."

