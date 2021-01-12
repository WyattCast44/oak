# Oak

Oak is a python command line application framework.

## Notable Features

- Ability to register commands
- Ability to register options
- Several pre-built commands and options you can use

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