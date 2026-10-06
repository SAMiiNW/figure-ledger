import os

_unlink = os.unlink

def safe_unlink(path, *args, **kwargs):
    try:
        return _unlink(path, *args, **kwargs)
    except PermissionError:
        return None

os.unlink = safe_unlink
CONTRACT = "contracts/contract.py"
SDK_VERSION = "v0.6.0-rc8"
