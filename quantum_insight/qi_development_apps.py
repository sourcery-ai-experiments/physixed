from typing import Any, Dict

development_apps: Dict[str, Any] = {
    "qi_main": {
        "mount_point": "qi/main/",
        "log_files": ["views"],
    },
    "qi_infinite": {
        "mount_point": "qi/infinite/",
        "log_files": ["views"],
    },
}
