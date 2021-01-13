import os
import types
import inspect
from oak import Application
from oak.Options import SilentOption
from oak.Commands import RunCommand, ListCommand, VersionCommand


def version(app, args=None):

    print(f"\n{app.config['version']}")

# signature
# print(len(inspect.signature(version).parameters))
# quit()


a = Application({
    'name': 'Python CLI',
    'version': '0.1.0',
}).registerCommands([
    RunCommand,
    ListCommand,
    VersionCommand,
]).registerCommands({
    'vers': version
}).registerOptions([
    SilentOption,
]).setDefaultRunable(
    runable=ListCommand,
).run()
