import pytest

from render import exposure as mod

CASES = [
    ('ev_scale', [0], 1.0, True),
    ('ev_scale', [2], 4.0, True),
    ('luminance', [[1, 1, 1]], 1.0, True),
    ('luminance', [[0, 1, 0]], 0.7152, True),
    ('percentile', [[1, 1, 1, 1], 0.5], 1, False),
    ('percentile', [[], 0.5], 0, False),
    ('center_weight', [1, 1, 2, 2], 1.0, True),
    ('center_weight', [0, 0, 2, 2], 0.0, True),
    ('ev_scale', [-1], 0.5, True),
    ('luminance', [[1, 0, 0]], 0.2126, True),
    ('percentile', [[0, 1], 0.0], 0, False),
    ('percentile', [[0, 0], 0.5], 0, False),
    ('center_weight', [0, 0, 0, 0], 0.0, True),
    ('adapt', [1, 2, 0], 1, False),
    ('center_weight', [1, 1, 4, 4], 0.2928932188134524, True),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_exposure_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
