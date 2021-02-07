from oak import Application


class SimpleOutputInterface:

    def __init__(self, application: Application):

        self.application = application

    def info(self, message):

        raise NotImplementedError()

    def line(self, message):

        raise NotImplementedError()

    def newLine(self, times=1):

        raise NotImplementedError()

    def success(self, message):

        raise NotImplementedError()

    def error(self, message):

        raise NotImplementedError()
