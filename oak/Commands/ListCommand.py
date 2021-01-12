from oak.Support import Runable


class ListCommand(Runable):

    signature = ["list"]

    arguments = {
        'name': {
            'description': 'Any commands/options that start with the given characters will be listed',
            'default': None
        }
    }

    def run(self, args=None):
        self.printCommands()
        self.printOptions()
        self.application.exit(0)

    def printCommands(self):

        print('\nCommands:')

        for signature, handler in self.application.commands.items():

            if hasattr(handler, "hidden") and handler.hidden:

                continue

            print('> ', signature)

    def printOptions(self):

        print("\nOptions:")

        for signature, handler in self.application.options.items():

            if hasattr(handler, "hidden") and handler.hidden:

                continue

            print('> ', signature)
