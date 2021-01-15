from oak.Support import Runable


class HelpOption(Runable):

    signature = [
        "--help",
    ]

    def run(self, args=None):

        print(
            f"\nYou can get help with any command or option by running:\n\npython {self.application.config['script']} help [command/option]")
