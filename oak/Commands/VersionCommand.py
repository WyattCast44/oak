from oak.Support import Runable


class VersionCommand(Runable):

    signature = ["version"]

    def run(self, args=None):

        print(f"\n{self.application.config.get('version')}")
