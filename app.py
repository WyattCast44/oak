from oak import Application
from oak.Options import SilentOption
from oak.Commands import RunCommand, ListCommand, VersionCommand

a = Application({
    'name': 'Python CLI',
    'version': '0.1.0',
}).registerCommands([
    RunCommand,
    ListCommand,
    VersionCommand,
]).registerOptions([
    SilentOption,
]).registerOptions({
    '--version': VersionCommand
}).setDefaultRunable(
    runable=ListCommand,
).run()
