from typing import Any

development_apps: dict[str, Any] = {
    "px_main": {
        "mount_point": "px/main/",
        "log_files": ["views"],
    },
    "px_quantum": {
        "mount_point": "px/infinite/",
        "log_files": ["views"],
    },
}
