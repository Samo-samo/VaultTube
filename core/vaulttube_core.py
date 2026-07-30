"""
VaultTube Core

Project: VaultTube
Version: Alpha 0.0.1

Responsible only for:
- Core initialization
- Manager loading
- Service initialization
- Dependency checks
- Graceful shutdown
"""

from managers.system_manager import SystemManager
from managers.database_manager import DatabaseManager
from managers.settings_manager import SettingsManager
from managers.protocol_manager import ProtocolManager
from constants.app_constants import APP_VERSION

class VaultTubeCore:
    def __init__(self):
        self.version = "0.0.1"
        self.system_manager = SystemManager()
        self.database_manager = DatabaseManager()
        self.settings_manager = SettingsManager()
        self.protocol_manager = ProtocolManager()

    def initialize(self):
        print("\nInitializing VaultTube Core...\n")

        self.load_managers()

        print("\nVaultTube Core is ready.\n")

    def load_managers(self):
        print("Loading managers...\n")

        if self.system_manager.initialize(): print("[ OK ] System Manager")
        if self.database_manager.initialize(): print("[ OK ] Database Manager")
        if self.settings_manager.initialize(): print("[ OK ] Settings Manager")
        if self.protocol_manager.initialize(): print("[ OK ] Protocol Manager")

def print_banner():
    print("=" * 40)
    print(f"VaultTube Core v{APP_VERSION}".center(40))
    print("=" * 40)


def main():
    print_banner()

    core = VaultTubeCore()
    core.initialize()


if __name__ == "__main__":
    main()