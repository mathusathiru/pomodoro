import pomodoro


def test_package_imports():
    assert pomodoro.__name__ == "pomodoro"


def test_package_has_version():
    assert isinstance(pomodoro.__version__, str)
    assert pomodoro.__version__ != ""