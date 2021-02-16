from oak import Runnable


class ListCommand(Runnable):

    signature = "list"

    def run(self, args=None):
        self.printCommands()
        self.printOptions()

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
