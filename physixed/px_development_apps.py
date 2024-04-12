from typing import Any, Dict

development_apps: Dict[str, Any] = {
    "px_main": {
        "mount_point": "qi/main/",
        "log_files": ["views"],
    },
    "px_quantum": {
        "mount_point": "qi/infinite/",
        "log_files": ["views"],
    },
}
