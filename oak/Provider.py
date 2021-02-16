from .Application import Application


class Provider:

    def __init__(self, application: Application):
        self.application = application

    def register(self):

        pass

    def boot(self):

        pass
