from oak import Application, ContainerTwo
from oak.Options import HelpOption, SilentOption
from oak.Commands import RunCommand, HelpCommand, ListCommand, VersionCommand
from oak.Support import CommandRegistrar


class SMTPMailer:

    def __init__(self, message='default'):

        print(message)


class MailServiceProvider:

    def register(self):
        return SMTPMailer('provided via ioc')


c = ContainerTwo()
# c.bind(SMTPMailer, SMTPMailer)
# c.bind(SMTPMailer, MailServiceProvider, 'register')
m = c.make(SMTPMailer)

quit()

a = Application({
    'name': 'Python CLI',
    'version': '0.1.0',
})

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
