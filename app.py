import os
import types
import inspect
from oak import Application
from oak.Options import SilentOption
from oak.Commands import RunCommand, ListCommand, VersionCommand


def version(app, args=None):

    print(f"\n{app.config['version']}")

# Built-in
# print('\nprint:')
# print(type(print) == types.BuiltinFunctionType)
# print(type(print) == types.FunctionType)
# print(inspect.isclass(print))

# # User defined
# print('\nversion:')
# print(type(version) == types.BuiltinFunctionType)
# print(type(version) == types.FunctionType)

# # Class
# print('\nclass:')
# print(type(VersionCommand) == types.BuiltinFunctionType)
# print(type(VersionCommand) == types.FunctionType)
# print(inspect.isclass(VersionCommand))

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
