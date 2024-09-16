"""Hello unit test module."""

from pythonApp.hello import hello


def test_hello():
    """Test the hello function."""
    assert hello() == "Hello pythonApp"
