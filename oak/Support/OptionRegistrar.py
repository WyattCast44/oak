import types
import inspect
from oak.Support import Repository


class OptionRegistrar(Repository):

    def __init__(self, application):

        super().__init__()

        self.application = application

    @classmethod
    def __raiseSignatureAccessibleError(cls, option):

        raise ValueError(
            f"Class based options must have either a signature property, or a getSignature method. Given option: {option}")

    @classmethod
    def __raiseSignatureValidationError(cls, signature, option):

        raise ValueError(
            f"Option signatures must be a non zero length string and must start with '--'. Given option: {option}, signature: {signature}. Read more at: https://github.com/wyattcast44/oak")

    @classmethod
    def __raiseInvalidoptionDataStructureError(cls, option):

        raise ValueError(
            f"Options must be a either be a user defined function, or a class. Given option: {option}, type: {type(option)}. Read more at: https://github.com/wyattcast44/oak")

    @classmethod
    def __validateOptionSignature(cls, signature, option):

        if type(signature) == list:

            if len(signature) == 0:

                cls.__raiseSignatureValidationError(signature, option)

            for sig in signature:

                if type(sig) != str:

                    cls.__raiseSignatureValidationError(sig, option)

                sig = sig.strip()

                if len(sig) == 0:

                    cls.__raiseSignatureValidationError(sig, option)

                if not sig.startswith('--'):

                    cls.__raiseSignatureValidationError(sig, option)

        else:

            if type(signature) != str:

                cls.__raiseSignatureValidationError(signature, option)

            signature = signature.strip()

            if len(signature) == 0:

                cls.__raiseSignatureValidationError(signature, option)

            if not signature.startswith('--'):

                cls.__raiseSignatureValidationError(signature, option)

    def registerFromList(self, options: list):

        from oak import Runnable

        for option in options:

            if type(option) == types.BuiltinFunctionType:

                raise TypeError(
                    f"Option handler ({option}) cannot be of type: types.BuiltinFunctionType. Read more at: https://github.com/wyattcast44/oak")

            elif type(option) == types.FunctionType:

                raise TypeError(
                    f"Function based options must be registed by passing in a dictionary, where the key is the signature of the option. Given option: {option}. Read more at: https://github.com/wyattcast44/oak")

            elif inspect.isclass(option):

                # Determine the signature
                if hasattr(option, "getSignature"):
                    signature = option.getSignature()
                elif hasattr(option, "signature"):
                    signature = option.signature
                else:
                    self.__raiseSignatureAccessibleError(option)

                # Validate the signature(s)
                self.__validateOptionSignature(signature, option)

                # Register the option with the application
                # if has aliases, register each
                if type(signature) == list:

                    for sig in signature:

                        self.store.update({
                            sig: option
                        })

                else:

                    self.store.update({
                        signature: option
                    })

            else:

                self.__raiseInvalidoptionDataStructureError(self, option)

    def registerFromDict(self, options: dict):

        from oak import Runnable

        for signature, option in options.items():

            self.__validateOptionSignature(signature, option)

            if type(option) == types.BuiltinFunctionType:

                raise TypeError(
                    f"Option handler ({option}) cannot be of type: types.BuiltinFunctionType. Read more at: https://github.com/wyattcast44/oak")

            elif type(option) == types.FunctionType:

                self.store.update({
                    signature: option
                })

            elif inspect.isclass(option):

                self.store.update({
                    signature: option
                })

            else:

                self.__raiseInvalidoptionDataStructureError(self, option)
