from oak import Application
import oak.Options as OakOptions
import oak.Commands as OakCommands
from oak import Args

arg = Args()

print(arg)
quit()

a = Application({
    'name': 'Python CLI',
    'version': '0.1.0',
}).registerCommands(
    OakCommands
).registerCommands(
    OakCommands
).registerOptions(
    OakOptions
).setDefaultRunnable(
    runnable=OakCommands.RunCommand
).run()
