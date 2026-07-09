## 🧪 8. Verification & QA Plan

This plan details the verification strategy for testing Nova Agent's tools and conversational interfaces.

### Automated Tests
Run the unit and integration tests using the following command:
```bash
uv run pytest tests/unit tests/integration
```

To execute the evaluations on agent performance (traces and grading):
```bash
agents-cli eval generate
agents-cli eval grade
```

### Manual Verification Checklist
1.  `[ ]` **Personal Capture Flow:** Request the agent to snapshot a celestial body (e.g. Orion Nebula), verify the file is created in user scope GCS, and ensure the URL matches GCS format.
2.  `[ ]` **Personal Delete Flow:** Ask the agent to delete a captured snapshot, verify that the file is deleted from GCS, and ensure proper notification is returned.
3.  `[ ]` **Platform Event Registration:** Register an event via chat, check Firestore platform-scoped collection `/agents/nova-agent/agent_data/platform/events` to ensure the document exists with appropriate audit fields (`created_at`, `created_by`, `version`, etc.).
4.  `[ ]` **Platform Wallpaper Upload:** Request to upload a platform wallpaper, and verify the file is created under `/agents/nova-agent/platform/wallpapers/{wallpaper_name}.jpg`.
5.  `[ ]` **Personal Analyze Flow:** Run the analysis command for a captured snapshot, verify that the tool uses `get_file` to fetch the file content, and returns the mock size and nebulosity analysis.
6.  `[ ]` **SMS Modality Verification:** Text the agent with short commands and verify response contains plain text with no UI or markdown syntax.
7.  `[ ]` **Voice Modality Verification:** Use spoken prompts and verify the spoken responses are natural, short, and free of markdown syntax.

