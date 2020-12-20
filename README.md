# study programming for python

## Preparation

### install application

- VsCode

https://code.visualstudio.com/download

- Github desktop

https://desktop.github.com/

- Chrome

https://www.google.com/intl/ja_jp/chrome/


### create github account

create github account from below url

https://github.com


### install homebrew

https://brew.sh/index_ja

### install python

```
brew install python
```

```
python3 -V
```

---------------

### install pipenv pyenv

```
brew install pipenv pyenv
```

### generate virtual environment (pipenv)

```
pipenv --python 3.9
```

#### activate virtual environment

```
pipenv shell
```

#### deactivate virtual environment

```
exit
```

#### install packages

```
pipenv install [package name]
```

example:

```
pipenv install pyyaml
```

#### show package list

```
pipenv graph
```

### already exist pipfile (restore packages)

```
pipenv install
```


---------------


### generate virtual environment (venv)

```
python3 -m venv .venv
```

#### activate virtual environment

```
source .venv/bin/activate
```

#### deactivate virtual environment

```
deactivate
```

### What's the Pipfile and Pipfile.lock

> The Pipfile file is intended to specify packages requirements for your Python application or library, both to development and execution.

> The Pipfile.lock is intended to specify, based on the packages present in Pipfile, which specific version of those should be used, avoiding the risks of automatically upgrading packages that depend upon each other and breaking your project dependency tree.

