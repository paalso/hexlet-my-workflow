from src.module import half


def test_half():
    assert half(0) == 0.0
    assert half(2) == 1.0
    assert half(-2) == -1.0
