from oak import Application
from oak.Options import HelpOption, SilentOption
from oak.Commands import RunCommand, HelpCommand, ListCommand, VersionCommand
from oak.Support import CommandRegistrar

a = Application({
    'name': 'Python CLI',
    'version': '0.1.0',
})

# c = CommandRegistrar(a)
# c['key'] = 'value'
# print(c)
# quit()

a.registerCommands([
    RunCommand,
    HelpCommand,
    ListCommand,
    VersionCommand
]).registerOptions([
    HelpOption,
    SilentOption,
]).registerOptions({
    '--version': VersionCommand
}).setDefaultRunnable(
    runnable=ListCommand,
    args=None
).run()
