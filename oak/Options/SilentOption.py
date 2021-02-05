from oak import Runnable


class SilentOption(Runnable):

    signature = [
        "--silent"
    ]

    def run(self, args=None):

        self.application.config.update({
            'silent': True
        })
