class Runable(object):

    signature = None

    arguments = {}

    options = {}

    def __init__(self, application):

        self.application = application

    @classmethod
    def getSignature(cls):

        return cls.signature

    @classmethod
    def _hasAliases(cls):

        if type(cls.getSignature()) == list:

            return True

        return False

    @classmethod
    def _hasArguments(cls):

        if type(cls.arguments) == dict and not len(cls.arguments) == 0:

            return True

        return False

    @classmethod
    def _hasOptions(cls):

        if type(cls.options) == dict and not len(cls.options) == 0:

            return True

        return False

    # @classmethod
    # def getRegisterableSignature(self, signature=None):

    #     if signature == None:
    #         return self.getSignature().strip().split(" ")[0]
    #     else:
    #         return signature.strip().split(" ")[0]

    @classmethod
    def _hasArgsOrOptions(cls):

        if cls._hasArguments() or cls._hasOptions():

            return True

        return False
