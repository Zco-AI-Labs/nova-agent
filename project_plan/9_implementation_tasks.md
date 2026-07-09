## 📋 9. Implementation Tasks

This checklist maps the precise, step-by-step changes required to implement the Nova Agent. Mark tasks as `[ ]` (unstarted), `[/]` (in progress), or `[x]` (completed) as you execute the implementation.

### Phase 1: Configuration & Metadata
- [ ] Initialize agent configuration in `app/agent.py` setting `name` to `"nova_agent"` and updating the description.
- [ ] Add the tools registration inside `app/agent.py`.

### Phase 2: Business Logic & Tool Implementation
- [ ] Write system prompt instructions inside the `app/SKILL.md` file using the defined system prompt template.
- [ ] Implement `app/scripts/capture_space_snapshot.py` with GCS User Scope saving logic.
- [ ] Implement `app/scripts/delete_space_snapshot.py` with GCS User Scope file deletion logic.
- [ ] Implement `app/scripts/register_platform_event.py` with Platform Scope Firestore saving logic.
- [ ] Implement `app/scripts/set_platform_wallpaper.py` with GCS Platform Scope saving logic.
- [ ] Implement `app/scripts/analyze_space_snapshot.py` using the GCS User Scope get_file retrieval logic.

### Phase 3: UI/Widgets Definition
- [ ] Create Lego block widget template `app/ui/widgets/snapshot_detail_card.json`.
- [ ] Create Lego block widget template `app/ui/widgets/event_calendar_card.json`.
- [ ] Create Lego block widget template `app/ui/widgets/wallpaper_preview_card.json`.
- [ ] Create Lego block widget template `app/ui/widgets/analysis_results_card.json`.

### Phase 4: Verification & Testing
- [ ] Create unit tests in `tests/unit/test_nova.py` or similar to verify capture, delete, register, set-wallpaper, and analyze tools with mock contexts.
- [ ] Run automated tests: `uv run pytest tests/`.
- [ ] Run local playground testing: `agents-cli playground`.
- [ ] Perform evaluations: `agents-cli eval generate` and `agents-cli eval grade`.
