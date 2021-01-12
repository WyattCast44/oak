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
    'env': 'dev',
    'version': '0.1.0',
}).run()
```

That's it! You've created your first `Oak` application 🎉! It doesn't do anything yet because we haven't added any commands or options, keep reading to start adding functionality to your app.

## Registering Commands

To add commands to your applications you should call the `registerCommands` method on the application instance.

```python
Application({
    'name': 'Oak CLI App',
    'env': 'dev',
    'version': '0.1.0',
}).registerCommands().run()
```

You can either pass in a `list` of [class based](https://github.com/wyattcast44/oak) commands, or a `dictionary` of `signatures` and `handlers`. Let's look at passing in a `dictionary` first.

```python

def myCommand(self, args=None):

    print('My first command!')

Application({
    'name': 'Oak CLI App',
    'env': 'dev',
    'version': '0.1.0',
}).registerCommands({
    'my-command': myCommand
}).run()
```

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