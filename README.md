
# Quick Start

1. **Clone this repo**

```
$ git clone git@github.com:jondot/langchain-llm-katas.git
```

2. **Install [`poetry`](https://github.com/python-poetry/poetry)**

Universal installer:

```
$ curl -sSL https://install.python-poetry.org | python3 -
```

Or with `pipx`:

```
$ pipx install poetry
```


3. (optional) **Install [`devstart`](https://github.com/jondot/devstart)**

`devstart` can help you run common commands as shortcuts.

With `brew`:

```
brew tap jondot/tap && brew install devstart
```

Or grab a [binary from releases](https://github.com/jondot/devstart/releases/tag/v0.7.0)

## Starting up

You will be practicing using _LLMs_, `langchain`, and other tools through completing tests that run with `pytest`.

**The rules are simple: make all tests pass.**

Using `devstart`, you can set up your repo for action

* `ds i` to install deps
* `ds s` to start

> `ds s` will run a pytest watcher, which will re-run test as you make modification. The first run may take longer than additional one.


If you did not install `devstart`, you can use these commands:

* `poetry install` to install deps
* `poetry run ptw . --now --disable-warnings` to start

## Best way to learn

The best way to learn is **by fighting it out the hard way**. Every test has a `TODO` that hints at what's wrong and a possible first direction.

1. Experiment, print stuff out, look at the sources
2. Read the docs: [langchain](https://langchain-langchain.vercel.app/docs/get_started/introduction.html), try different things and experiment
3. When all else fails, you can run hints:

```
$ poetry run hints
```

And search for a test name.

