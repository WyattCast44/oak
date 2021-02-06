from oak import Application
import oak.Commands as OakCommands
from oak.Options import HelpOption, SilentOption

a = Application({
    'name': 'Python CLI',
    'version': '0.1.0',
}).registerCommands(
    OakCommands
).registerOptions([
    HelpOption,
    SilentOption,
]).setDefaultRunnable(
    runnable=OakCommands.ListCommand
).run()
