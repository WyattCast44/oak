from oak.Support import Runable


class RunCommand(Runable):

    signature = ["run"]

    def run(self, args=None):

        index = 0
        optionsStack = {}
        commandsStack = {}

        for signature, handler in self.application.commands.items():

            commandsStack[index] = signature

            index = index + 1

        for signature, handler in self.application.options.items():

            optionsStack[index] = signature

            index = index + 1

        print('\nCommands:')

        for index, signature in commandsStack.items():

            print(f"[{index}] {signature}")

        print('\nOptions:')

        for index, signature in optionsStack.items():

            print(f"[{index}] {signature}")

        print('')
        selected = int(input('> Enter the number to run, or -1 to exit: '))

        if selected == -1:

            self.application.exit(0)

        elif selected in commandsStack:

            print(f"\nRunning command: {commandsStack[selected]}")

            handler = self.application.commands[commandsStack[selected]]

            self.application._runRunnable(handler)

        elif selected in optionsStack:

            print(f"\nRunning option: {optionsStack[selected]}")

            handler = self.application.options[optionsStack[selected]]

            self.application._runRunnable(handler)

        else:

            print('\nIndex not found, please try again.')
            self.application.exit(1)

        self.application.exit(0)
