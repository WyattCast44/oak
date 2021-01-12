import os
import types
import inspect
from oak import Application
from dotenv import load_dotenv
from oak.Options import SilentOption
from oak.Commands import RunCommand, ListCommand, VersionCommand

load_dotenv()


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

class MyCommand:

    def __init__(self, application):

        self.application = application

    def run(self, args=None):

        print(f"\n{self.application.config.get('version', '0.1.0')}")


a = Application({
    'name': 'Python CLI',
    'env': os.getenv('APP_ENV'),
    'version': os.getenv('APP_VERSION'),
}).registerCommands([
    RunCommand,
    ListCommand,
    VersionCommand
]).registerCommands({
    'my-command': MyCommand
}).registerOptions({
    '--version': VersionCommand
}).registerOptions([
    SilentOption,
]).setDefaultRunable(
    runable=ListCommand,
).run()
