import sys
import types
import inspect


class Application(object):

    __defaultConfig = {
        'env': 'dev',
        'silent': False
    }

    def __init__(self, config={}):

        from oak import Container

        # Bind the container
        self.container = Container()

        # Merge the default config and user config
        self.config = {**self.__defaultConfig, **config}

        # Register base bindings
        self.container.bind("application", self)

        # Grab the name of the script
        self.config.update({'script': sys.argv[0]})

        # Bind the commands container
        self.commands = {}

        # Bind the options container
        self.options = {}

        # Set the default command to None
        self.defaultCommand = None

        # Grab any args passed to the app
        self.args = sys.argv[1:]

        return

    def registerCommands(self, commands):

        from oak.Support import CommandRegistrar

        registrar = CommandRegistrar(self)

        if type(commands) == list:

            registrar.registerFromList(commands)

            from oak.Support import Runable

            # If we get a list, then we can assume
            # it is a list of class based commands
            # We just need to ensure the handler
            # has some type of signature

            for command in commands:

                if type(command) == types.BuiltinFunctionType:

                    raise TypeError(
                        f"Command handler ({command}) cannot be of type: types.BuiltinFunctionType. Read more at: https://github.com/wyattcast44/oak")

                elif type(command) == types.FunctionType:

                    raise TypeError(
                        f"Function based commands must be registed by passing in a dictionary, where the key is the signature of the command. Given command: {command}. Read more at: https://github.com/wyattcast44/oak")

                # Check if runnable instance
                elif issubclass(command, Runable):

                    if command._hasAliases():

                        if len(command.getSignature()) == 0:

                            raise ValueError(
                                f"Command signatures must be a non zero length string and must not contain the '-' character. Given command: {command}, signature: {command.getSignature()}. Read more at: https://github.com/wyattcast44/oak")

                        for signature in command.getSignature():

                            self.__validateCommandSignature(signature, command)

                            self.commands.update({
                                signature: command
                            })

                    else:

                        signature = command.getSignature()

                        self.__validateCommandSignature(signature, command)

                        self.commands.update({
                            signature: command
                        })

                    continue

                # Check if general class
                elif inspect.isclass(command):

                    if hasattr(command, "getSignature"):

                        signature = command.getSignature()

                        if type(signature) == list:

                            if len(signature) == 0:

                                raise ValueError(
                                    f"Command signatures must be a non zero length string and must not contain the '-' character. Given command: {command}, signature: {signature}. Read more at: https://github.com/wyattcast44/oak")

                            for sig in signature:

                                self.__validateCommandSignature(sig, command)

                                self.commands.update({
                                    sig: command
                                })

                        else:

                            self.__validateCommandSignature(signature, command)

                            self.commands.update({
                                signature: command
                            })

                    elif hasattr(command, "signature"):

                        if type(command.signature) == list:

                            if len(command.signature) == 0:

                                raise ValueError(
                                    f"Command signatures must be a non zero length string and must not contain the '-' character. Given command: {command}, signature: {signature}. Read more at: https://github.com/wyattcast44/oak")

                            for signature in command.signature:

                                self.__validateCommandSignature(
                                    signature, command)

                                self.commands.update({
                                    signature: command
                                })

                        else:

                            signature = command.signature

                            self.__validateCommandSignature(signature, command)

                            self.commands.update({
                                signature: command
                            })

                    else:

                        raise ValueError(
                            f"Class based commands must have either a signature property, or a getSignature method. Given command: {command}")

                    continue

        elif type(commands) == dict:

            # If we get a dict, then we can assume
            # it is a list of signatures and handlers

            for signature, handler in commands.items():

                self.commands.update({signature: handler})

        else:

            raise ValueError(
                "To register commands you must either pass in a list of class based commands, or a dictionary of signature: handler commands. Read more at https://github.com/wyattcast44/oak")

        return self

    def registerOptions(self, options):

        if type(options) == list:

            # If we get a list, then we can assume
            # it is a list of class based commands
            # in the future, I'd like to expand and
            # allow functions to be registered.
            # The problem is we need a some type
            # signature to assign

            for option in options:

                if option._hasAliases():

                    for signature in option.getSignature():

                        self.options.update({
                            signature: option
                        })

                else:

                    self.options.update({
                        option.getSignature(): option
                    })

        elif type(options) == dict:

            # If we get a dict, then we can assume
            # it is a list of signatures and handlers

            for signature, handler in options.items():

                self.options.update({signature: handler})

        return self

    def setDefaultRunable(self, runable, args=None):

        # Can set a default command
        # that will run if the user runs
        # the app w/o passing any args.

        self.defaultCommand = {
            'handler': runable,
            'args': args
        }

        return self

    def run(self):

        if len(self.args) == 0:

            # If no args, need to check if we have
            # a default arg, if so run it

            if not self.defaultCommand == None:

                # Need to check if default command has
                # default args to pass in

                if self.defaultCommand['args'] == None:
                    self.defaultCommand['handler'](self).run()
                else:
                    self.defaultCommand['handler'](self).run(
                        self.defaultCommand['args']
                    )

            self.exit(0)

        if len(self.args) == 1:

            if self.args[0] in self.commands:
                self._runRunnable(self.commands[self.args[0]])
            elif self.args[0] in self.options:
                self._runRunnable(self.options[self.args[0]])
            else:
                self.exit(127)  # command not found

            self.exit(0)

        # Alright we have more than one arg
        # We need to parse the arguments
        # how to do this...
        # we can seperate the command and options by searching for
        # -- in the args
        possibleOptions = []
        possibleCommandsAndArgs = []

        for arg in self.args:

            if "--" in arg:

                possibleOptions.append(arg)

            else:

                possibleCommandsAndArgs.append(arg)

        # We have seperated the possible commands
        # we can loop thru and determine if the first
        # one matches any known commands
        if possibleCommandsAndArgs[0] in self.commands:

            print('found...')

        # new strategy, first loop thru all args
        # and search for any known application options
        # rip these out and the rest can be considered
        # args and options for the given command

        print(possibleOptions, possibleCommandsAndArgs)
        quit()

        commandStack = []
        commandFound = False

        optionsStack = []
        optionFound = False

        for arg in self.args:

            # py script command c-option      g-option
            # py app.py version --format=json --silent

            if arg in self.commands:

                commandFound = True

                if hasattr(self.commands[arg], '_hasArgsOrOptions') and self.commands[arg]._hasArgsOrOptions():

                    # TODO need to determine which of the remaining (if any)
                    #  args belong to this command
                    remainingArgs = self.args[self.args.index(arg)+1:]

                    commandStack.append({
                        'signature': arg,
                        'args': None
                    })

                    # print(self.commands[arg].arguments,
                    #       self.commands[arg].options, len(self.commands[arg].arguments))

                else:

                    commandStack.append({
                        'signature': arg,
                        'args': None
                    })

            elif arg in self.options:

                optionFound = True
                optionsStack.append({
                    'option': arg,
                    'value': arg.split("=")[1] if "=" in arg else True
                })

    def _runRunnable(self, runable, args=None):

        from oak.Support import Runable

        if isinstance(runable, Runable):

            runable(self).run(args)

        elif inspect.isclass(runable):

            runable(self).run(args)

        elif type(runable) == types.BuiltinFunctionType:

            runable(self, args)

        elif type(runable) == types.FunctionType:

            runable(self, args)

        else:

            self.exit(1)

    def exit(self, code=0):

        return sys.exit(code)

    def __del__(self):

        # if "--" in arg:

        #         if "=" in arg:
        #             self.optionArgs.update({
        #                 arg.replace('--', '').split('=')[0]: arg.split('=')[1]
        #             })
        #         else:
        #             self.optionArgs.update({
        #                 arg.replace('--', ''): True
        #             })

        #     else:

        #         self.commandArgs.append(arg)

        return
