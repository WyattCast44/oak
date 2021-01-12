# Oak

🌲 Oak is a python command line application framework.

## Notable Features

- Ability to register commands
- Ability to register options
- Several pre-built commands and options you can use

## Creating Applications

To create a new Oak application:
- import `Application` from `oak`
- Create an instance of `Application`
- Pass a [config](https://github.com/wyattcast44/oak) dictionary to the constructor

```python
from oak import Application

a = Application({
    'name': 'Python CLI',
    'env': os.getenv('APP_ENV'),
    'version': os.getenv('APP_VERSION'),
}).registerCommands([
    RunCommand,
    ListCommand,
    VersionCommand
]).registerOptions({
    '--version': VersionCommand
}).registerOptions([
    SilentOption,
]).setDefaultRunable(
    runable=ListCommand,
).run()
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