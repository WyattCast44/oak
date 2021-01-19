from oak.Support import Runnable


class VersionCommand(Runnable):

    signature = ["version"]

    def run(self, args=None):

        print(f"\n{self.application.config.get('version')}")
