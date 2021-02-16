from oak import Application
import oak.Options as OakOptions
import oak.Commands as OakCommands
from oak.Providers import SimpleOutputProvider


def here():

    print('here')


a = Application({
    'name': 'Python CLI',
    'version': '0.1.0',
    'providers': [
        SimpleOutputProvider
    ]
}).registerCommands({
    'ppp': here
}).registerCommands(
    OakCommands
).registerOptions(
    OakOptions
)

a.run()
