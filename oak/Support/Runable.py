class Runable(object):

    signature = None

    arguments = {}

    options = {}

    def __init__(self, application):

        self.application = application

    @classmethod
    def getSignature(self):

        return self.signature

    @classmethod
    def _hasAliases(self):

        if type(self.getSignature()) == list:

            return True

        return False

    @classmethod
    def _hasArguments(self):

        if type(self.arguments) == dict and not len(self.arguments) == 0:

            return True

        return False

    @classmethod
    def _hasOptions(self):

        if type(self.options) == dict and not len(self.options) == 0:

            return True

        return False

    # @classmethod
    # def getRegisterableSignature(self, signature=None):

    #     if signature == None:
    #         return self.getSignature().strip().split(" ")[0]
    #     else:
    #         return signature.strip().split(" ")[0]

    @classmethod
    def _hasArgsOrOptions(self):

        if self._hasArguments() or self._hasOptions():

            return True

        return False
