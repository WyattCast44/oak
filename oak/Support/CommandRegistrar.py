import types
import inspect
from oak.Support import Repository


class CommandRegistrar(Repository):

    def __init__(self, application):

        super().__init__()

        self.application = application

    @classmethod
    def __raiseSignatureAccessibleError(cls, command):

        raise ValueError(
            f"Class based commands must have either a signature property, or a getSignature method. Given command: {command}")

    @classmethod
    def __raiseSignatureValidationError(cls, signature, command):

        raise ValueError(
            f"Command signatures must be a non zero length string and must not contain the '-' character. Given command: {command}, signature: {signature}. Read more at: https://github.com/wyattcast44/oak")

    @classmethod
    def __raiseInvalidCommandDataStructureError(cls, command):

        raise ValueError(
            f"Command must be a either be a user defined function, or a class. Given command: {command}, type: {type(command)}. Read more at: https://github.com/wyattcast44/oak")

    @classmethod
    def __validateCommandSignature(cls, signature, command):

        if type(signature) == list:

            if len(signature) == 0:

                cls.__raiseSignatureValidationError(signature, command)

            for sig in signature:

                if type(sig) != str:

                    cls.__raiseSignatureValidationError(sig, command)

                sig = sig.strip()

                if len(sig) == 0:

                    cls.__raiseSignatureValidationError(sig, command)

                if sig.startswith('-'):

                    cls.__raiseSignatureValidationError(sig, command)

        else:

            if type(signature) != str:

                cls.__raiseSignatureValidationError(signature, command)

            signature = signature.strip()

            if len(signature) == 0:

                cls.__raiseSignatureValidationError(signature, command)

            if signature.startswith('-'):

                cls.__raiseSignatureValidationError(signature, command)

    def registerFromList(self, commands: list):

        from oak.Support import Runnable

        for command in commands:

            if type(command) == types.BuiltinFunctionType:

                raise TypeError(
                    f"Command handler ({command}) cannot be of type: types.BuiltinFunctionType. Read more at: https://github.com/wyattcast44/oak")

            elif type(command) == types.FunctionType:

                raise TypeError(
                    f"Function based commands must be registed by passing in a dictionary, where the key is the signature of the command. Given command: {command}. Read more at: https://github.com/wyattcast44/oak")

            elif inspect.isclass(command):

                # Determine the signature
                if hasattr(command, "getSignature"):
                    signature = command.getSignature()
                elif hasattr(command, "signature"):
                    signature = command.signature
                else:
                    self.__raiseSignatureAccessibleError(command)

                # Validate the signature(s)
                self.__validateCommandSignature(signature, command)

                # Register the command with the application
                # if has aliases, register each
                if type(signature) == list:

                    for sig in signature:

                        self.store.update({
                            sig: command
                        })

                else:

                    self.store.update({
                        signature: command
                    })

            else:

                self.__raiseInvalidCommandDataStructureError(self, command)

    def registerFromDict(self, commands: dict):

        from oak.Support import Runnable

        for signature, command in commands.items():

            self.__validateCommandSignature(signature, command)

            if type(command) == types.BuiltinFunctionType:

                raise TypeError(
                    f"Command handler ({command}) cannot be of type: types.BuiltinFunctionType. Read more at: https://github.com/wyattcast44/oak")

            elif type(command) == types.FunctionType:

                self.store.update({
                    signature: command
                })

            elif inspect.isclass(command):

                self.store.update({
                    signature: command
                })

            else:

                self.__raiseInvalidCommandDataStructureError(self, command)
