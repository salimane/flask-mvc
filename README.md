# Flask-mvc

![Build Status](https://github.com/salimane/flask-mvc/actions/workflows/main.yml/badge.svg)
[![Maintenance](https://img.shields.io/maintenance/yes/2023.svg)](https://github.com/salimane/flask-mvc/commits/master)


A simple boilerplate application following the MVC pattern using Flask micro python framework.
It basically here to be a base skeleton for new python web applications

It includes:

| environment | url |
| --- | --- |
| Demo | http://flask-mvc-salimane.herokuapp.com/ |

This repository is maintained by [Salimane Adjao Moustapha](https://github.com/salimane).
If you need to make changes to or have any ideas for improvement at this, please send a PR

## Prerequisites

* Git
* A working [Python](https://www.python.org/) 3.10 installation with [virtualenv](https://virtualenv.pypa.io/en/stable/) and [pip](https://pypi.python.org/pypi/pip).
    ** 
    ```shell
    # Mac OS X
    brew update
    brew install asdf pipx
    asdf plugin add python
    asdf install python 3.10.11
    pipx ensurepath
    pipx install virtualenv
    ```

## Setup

    ```Bash
    $ git clone git@github.com:salimane/flask-mvc.git
    $ cd flask-mvc
    $ asdf local python 3.10.11
    $ pipx install virtualenv
    $ Run ``make setup``
    ```

## Running

* Run in console with 
```
$ make run
```

## Contributing

It basically here to be a base skeleton for new python web applications, so we'd love your input! Got a question or an idea? Create an issue or a pull-request.

## Maintainers

* [Salimane Adjao Moustapha - @salimane](https://github.com/salimane)

## Copyright Notice

Copyright (C) 2023 Salimane Adjao Moustapha, authors, and contributors. Licensed under the [MIT License](/LICENSE).
