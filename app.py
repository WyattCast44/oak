from oak import Application
from oak.Support import Runable
from oak.Options import SilentOption
from oak.Commands import RunCommand, ListCommand, VersionCommand


def version(app, args=None):

    print(f"\n{app.config['version']}")


class SomeCommand(Runable):

    def run(self, args=None):

        print("tada!")


a = Application({
    'name': 'Python CLI',
    'version': '0.1.0',
}).registerCommands([
    RunCommand,
    ListCommand,
    VersionCommand,
    SomeCommand
]).registerOptions([
    SilentOption,
]).registerOptions({
    '--version': VersionCommand
}).setDefaultRunable(
    runable=ListCommand,
).run()
