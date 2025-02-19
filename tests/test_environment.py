import sys
import platform
import pytest

def test_operating_system():
    """Test that the operating system is Linux"""
    assert platform.system().lower() == 'linux', \
        f"Operating system {platform.system()} is not Linux"

def test_python_version():
    """Test that Python version is either 3.10 or 3.11"""
    version = sys.version_info
    assert version.major == 3 and version.minor in [10, 11], \
        f"Python version {version.major}.{version.minor} not in [3.10, 3.11]"
