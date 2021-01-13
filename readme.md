# Oak

🌲 Oak is a python command line application framework.

## Notable Features

- Ability to register commands
- Ability to register options
- Abilty to set a default command/option
- Several pre-built commands and options you can use

## Creating Applications

To create a new Oak application:
- import `Application` from `oak`
- Create an instance of `Application`
- Pass a dictionary with any [config](https://github.com/wyattcast44/oak) values to the constructor
- Call the `run` method on the `Application`

```python
from oak import Application

Application({
    'name': 'Oak CLI App',
    'version': '0.1.0',
}).run()
```

That's it! You've created your first `Oak` application 🎉! It doesn't do anything yet because we haven't added any commands or options, keep reading to start adding functionality to your app.

## Registering Commands

To add commands to your applications you should call the `registerCommands` method on the application instance.

```python
from oak import Application

Application({
    'name': 'Oak CLI App',
    'version': '0.1.0',
}).registerCommands().run()
```

You can either pass in a `list` of [class based](https://github.com/wyattcast44/oak) commands, or a `dictionary` of [function based](https://github.com/wyattcast44/oak) commands. 

Let's take a look at registering function based commands first:

```python
from oak import Application

def myCommand(application, args=None):

    print('My first command!')

Application({
    'name': 'Oak CLI App',
    'version': '0.1.0',
}).registerCommands({
    'my-command': myCommand
}).run()
```

In the example above, you can see we defined a function called `myCommand` and we passed it to the `registerCommands` method with the key `my-command`. This will register a command with your application, the signature will be the key and when a user calls this command, the `myCommand` function will be called. Read more about `function` based commands [here](https://github.com/wyattcast44/oak).

Alright, now let's take a look at registering class based commands:

```python
from oak import Application

class MyCommand:

    signature = "my-command"

    def __init__(self, application):

        self.application = application

    def run(self, args=None):

        print(f"\n{self.application.config.get('version', '0.1.0')}")

Application({
    'name': 'Oak CLI App',
    'version': '0.1.0',
}).registerCommands([
    MyCommand
]).run()
```

In the example above, you can see we defined a class called `MyCommand` and we passed it to the `registerCommands` method. This will register a command with your application, the signature will be taken from the signature property and when a user calls this command, the `run` method of the class will be called. Read more about `class` based commands [here](https://github.com/wyattcast44/oak).

## Registering Options

To add options to your applications you should call the `registerOptions` method on the application instance.

```python
from oak import Application

Application({
    'name': 'Oak CLI App',
    'version': '0.1.0',
}).registerOptions().run()
```

You can either pass in a `list` of [class based](https://github.com/wyattcast44/oak) options, or a `dictionary` of [function based](https://github.com/wyattcast44/oak) options. 

Let's take a look at registering function based options first:

```python
from oak import Application

def versionOption(application, args=None):

    print(f"\n{self.application.config.get('version', '0.1.0')}")

Application({
    'name': 'Oak CLI App',
    'version': '0.1.0',
}).registerOptions({
    '--version': versionOption
}).run()
```

In the example above, you can see we defined a function called `versionOption` and we passed it to the `registerCommands` method with the key `--version`. This will register a option with your application, the signature will be the key and when a user calls this command, the `versionOption` function will be called. Read more about `function` based options [here](https://github.com/wyattcast44/oak).

Alright, now let's take a look at registering class based options:

```python
from oak import Application

class VersionOption:

    signature = "--version"

    def __init__(self, application):

        self.application = application

    def run(self, args=None):
        
        print(f"\n{self.application.config.get('version')}")

Application({
    'name': 'Oak CLI App',
    'version': '0.1.0',
}).registerCommands([
    VersionOption
]).run()
```

In the example above, you can see we defined a class called `VersionOption` and we passed it to the `registerCommands` method. This will register a option with your application, the signature will be taken from the signature property and when a user calls this command, the `run` method of the class will be called. Read more about `class` based options [here](https://github.com/wyattcast44/oak).

## Function Based Commands

## Class Based Commands

## Pre-built Commands

### List Command

#### Description:

The `list` command simply lists all commands and options registered with your application.

#### Usage:

```bash
python app.py list
```

#### Output:

This is the output for the standard [example](https://github.com/wyattcast44/oak) `app.py` script.

```bash
Commands:
>  run
>  list
>  version

Options:
>  --version
>  --silent
```