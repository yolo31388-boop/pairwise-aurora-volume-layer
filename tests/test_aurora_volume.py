import pytest
import graphics.aurora_volume as mod

CASES = [
    ("view_shell_thickness", (1,)),
    ("cloud_driven_intensity", (1,)),
    ("stable_sort_key", (1,)),
    ("pause_freeze_phase", (1,)),
    ("high_bitdepth_write", (1,)),
    ("shared_camera_state", (1,)),
    ("load_sky", (1,)),
    ("build_aurora", (1,)),
    ("shade_aurora", (1,)),
    ("present_sky", (1,)),
    ("validate_aurora", (1,)),
    ("metrics_aurora", (1,)),
    ("audit_aurora", (1,)),
    ("fallback_aurora", (1,)),
    ("determinism_aurora", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
