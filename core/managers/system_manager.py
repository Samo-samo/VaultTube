import platform

class SystemManager:
    def __init__(self):
        self.operating_system = None
        self.python_version = None

    def initialize(self):
        return True
        print("Initializing System Manager...\n")

        self.operating_system = platform.system()
        self.python_version = platform.python_version()

        print(f"Operating System : {self.operating_system}")
        print(f"Python Version   : {self.python_version}")

        print("\nSystem Manager Ready.\n")

    def get_system_info(self):
        return {
            "operating_system": self.operating_system,
            "python_version": self.python_version,
        }