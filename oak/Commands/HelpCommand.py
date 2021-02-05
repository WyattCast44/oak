from oak import Runnable


class HelpCommand(Runnable):

    signature = ["help"]

    def run(self, args=None):

        print(f"\nHelp TODO")
