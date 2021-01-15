from oak.Support import Runable


class HelpCommand(Runable):

    signature = ["help"]

    def run(self, args=None):

        print(f"\nHelp TODO")
