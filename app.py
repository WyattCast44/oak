import abc
from oak.Support import CommandRegistrar
from oak import Application, ContainerTwo
from oak.Options import HelpOption, SilentOption
from oak.Commands import RunCommand, HelpCommand, ListCommand, VersionCommand


class MailInterface:

    pass


class ZeroConfig:

    def __init__(self):
        pass


class SMTPMailer:

    def __init__(self, message):

        print(message)


class SMTPMailerProvider:

    def __init__(self):
        super().__init__()

    def __new__(cls):
        return SMTPMailer("Tada")


c = ContainerTwo()

# # we can provide the container instructions on how to init a class
# c.bind(SMTPMailer, SMTPMailerProvider)
# m = c.make(SMTPMailer)
# print(isinstance(m, SMTPMailer))
# quit()

# # we can use a string as a abstract key
# c.bind('mailer', SMTPMailerProvider)
# m = c.make('mailer')
# print(isinstance(m, SMTPMailer))
# quit()

# # We can bind an interface to a implmentation
# c.bind(MailInterface, SMTPMailerProvider)
# m = c.make(MailInterface)
# print(isinstance(m, SMTPMailer))
# quit()

# # We can bind a class directly without providing instructions on how to init
# c.bind('direct', SMTPMailer)
# m = c.make('direct')
# print(m, isinstance(m, SMTPMailer))
# quit()

# # We can do zero config resolution
# m = c.make(ZeroConfig)
# print(m)
# quit()

# # We can recusively resolve
# Weh we ask for a mail interface, we want an instance of SMTP mailer
c.bind(MailInterface, SMTPMailer)
# When we need an SMTPMailer, the SMTPMailerProvider must help us build it
c.bind(SMTPMailer, SMTPMailerProvider)
# So when we ask for the mailerinterface, we expect a smtpmailer, that the provider helped build
m = c.make(MailInterface)
print(isinstance(m, SMTPMailer))
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
