import sys
import os
import types
from unittest.mock import MagicMock, patch

# Add workspace root to system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# 1. Mock external packages using types.ModuleType to satisfy importlib
class MockModule(types.ModuleType):
    def __init__(self, name, is_package=True):
        super().__init__(name)
        if is_package:
            self.__path__ = []
            
    def __getattr__(self, name):
        mock_obj = MagicMock()
        setattr(self, name, mock_obj)
        return mock_obj

# Register package namespaces
sys.modules['google'] = MockModule('google')
sys.modules['google.adk'] = MockModule('google.adk')
sys.modules['google.adk.models'] = MockModule('google.adk.models')
sys.modules['google.adk.utils'] = MockModule('google.adk.utils')
sys.modules['google.genai'] = MockModule('google.genai')
sys.modules['google.cloud'] = MockModule('google.cloud')

# Define real exception classes for jwt mock to allow try-except catching
class ExpiredSignatureError(Exception):
    pass

class InvalidTokenError(Exception):
    pass

jwt_mock = MockModule('jwt', is_package=False)
jwt_mock.ExpiredSignatureError = ExpiredSignatureError
jwt_mock.InvalidTokenError = InvalidTokenError

# Register other submodules
sys.modules['jwt'] = jwt_mock
for mod in [
    'google.auth', 'google.oauth2', 'google.oauth2.credentials',
    'google.cloud.firestore', 'google.adk.runners', 'google.adk.apps', 
    'google.adk.models.google_llm', 'google.adk.models.llm_response',
    'google.adk.models.llm_request', 'google.adk.utils.context_utils',
    'google.adk.utils.streaming_utils',
    'google.genai.types', 'cryptography', 'cryptography.fernet'
]:
    sys.modules[mod] = MockModule(mod, is_package=False)

# Mock pytest
class MockPytest:
    def fixture(self, *args, **kwargs):
        if len(args) == 1 and callable(args[0]):
            return args[0]
        def decorator(f):
            return f
        return decorator

sys.modules['pytest'] = MockPytest()

# 2. Import tests
from tests.unit.test_nova import (
    test_capture_space_snapshot_success,
    test_delete_space_snapshot_success,
    test_analyze_space_snapshot_success,
    test_register_platform_event_success,
    test_set_platform_wallpaper_success
)

def run():
    print("--------------------------------------------------")
    print("Running Nova Agent Unit Tests via Custom Runner")
    print("--------------------------------------------------")
    
    passed = 0
    failed = 0
    
    # Create the shared mock context and configure it to bypass JWT check
    ctx = MagicMock()
    ctx.raw_context = {}  # Empty dict ensures capability_token is None
    ctx.auth.get_user_id.return_value = "test_user"
    
    # 3. Patch app.core.hubscape_adk.get_context to return our mock context
    with patch("app.core.hubscape_adk.get_context", return_value=ctx):
        
        # 1. test_delete_space_snapshot_success
        print("1. test_delete_space_snapshot_success: ", end="")
        try:
            ctx.delete_file.reset_mock()
            test_delete_space_snapshot_success(ctx)
            print("PASSED")
            passed += 1
        except Exception as e:
            print("FAILED:", e)
            failed += 1
            
        # 2. test_analyze_space_snapshot_success
        print("2. test_analyze_space_snapshot_success: ", end="")
        try:
            ctx.get_file.reset_mock()
            ctx.show_widget.reset_mock()
            test_analyze_space_snapshot_success(ctx)
            print("PASSED")
            passed += 1
        except Exception as e:
            print("FAILED:", e)
            failed += 1
            
        # 3. test_register_platform_event_success
        print("3. test_register_platform_event_success: ", end="")
        try:
            ctx.save.reset_mock()
            ctx.show_widget.reset_mock()
            test_register_platform_event_success(ctx)
            print("PASSED")
            passed += 1
        except Exception as e:
            print("FAILED:", e)
            failed += 1
            
        # 4. test_capture_space_snapshot_success
        print("4. test_capture_space_snapshot_success: ", end="")
        try:
            ctx.save_file.reset_mock()
            ctx.show_widget.reset_mock()
            test_capture_space_snapshot_success(ctx)
            print("PASSED")
            passed += 1
        except Exception as e:
            import traceback
            print("FAILED:", e)
            traceback.print_exc()
            failed += 1
            
        # 5. test_set_platform_wallpaper_success
        print("5. test_set_platform_wallpaper_success: ", end="")
        try:
            ctx.save_file.reset_mock()
            ctx.show_widget.reset_mock()
            test_set_platform_wallpaper_success(ctx)
            print("PASSED")
            passed += 1
        except Exception as e:
            print("FAILED:", e)
            failed += 1

    print("--------------------------------------------------")
    print(f"Results: {passed} passed, {failed} failed")
    print("--------------------------------------------------")
    
    if failed > 0:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    run()
