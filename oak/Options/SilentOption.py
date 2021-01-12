from oak.Support import Runable


class SilentOption(Runable):

    signature = ["--silent"]

    def run(self, args=None):

        self.application.config.update({
            'silent': True
        })
