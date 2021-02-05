from oak import Application
from oak.Options import HelpOption, SilentOption
from oak.Commands import RunCommand, HelpCommand, VersionCommand
from oak import ListCommand

a = Application({
    'name': 'Python CLI',
    'version': '0.1.0',
}).registerCommands([
    RunCommand,
    HelpCommand,
    ListCommand,
    VersionCommand
]).registerOptions([
    HelpOption,
    SilentOption,
]).registerOptions({
    '--version': VersionCommand
})

a.setDefaultRunnable(
    runnable=ListCommand,
    args=None
)

a.run()
