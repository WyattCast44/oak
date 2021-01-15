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

        elif type(commands) == dict:

            registrar.registerFromDict(commands)

        else:

            raise ValueError(
                "To register commands you must either pass in a list of class based commands, or a dictionary of signatures and handlers. Read more at https://github.com/wyattcast44/oak")

        return self

    def registerOptions(self, options):

        from oak.Support import OptionRegistrar

        registrar = OptionRegistrar(self)

        if type(options) == list:

            registrar.registerFromList(options)

        elif type(options) == dict:

            registrar.registerFromDict(options)

        else:

            raise ValueError(
                "To register options you must either pass in a list of class based options, or a dictionary of signatures and handlers. Read more at https://github.com/wyattcast44/oak")

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
                    self._runRunnable(self.defaultCommand['handler'])
                else:
                    self._runRunnable(
                        self.defaultCommand['handler'], self.defaultCommand['args'])

            return self

        if len(self.args) == 1:

            if self.args[0] in self.commands:
                self._runRunnable(self.commands[self.args[0]])
            elif self.args[0] in self.options:
                self._runRunnable(self.options[self.args[0]])
            else:
                self.exit(127)  # command not found

            return self

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

        if inspect.isclass(runable):

            runable = runable(self)

            if hasattr(runable, "beforeRun"):

                runable.beforeRun()

            runable.run(args)

            if hasattr(runable, "afterRun"):

                runable.afterRun()

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
