### Learn langchain & LLMs through code  Katas

Welcome to **langchain & llm katas**! This is a an open-source project designed to help you improve your skills with AI engineering using LLMs and the `langchain` library. 

By completing tests using `pytest`, you'll gain hands-on experience and have a lot of fun in the process!

#### Quick Start

1. **Clone this repository**

   ```
   $ git clone git://github.com/jondot/langchain-llm-katas.git
   ```

2. **Install [`poetry`](https://github.com/python-poetry/poetry)**

   You can use the universal installer:

   ```
   $ curl -sSL https://install.python-poetry.org | python3 -
   ```

   Or, if you prefer `pipx`:

   ```
   $ pipx install poetry
   ```

3. (optional) **Install [`devstart`](https://github.com/jondot/devstart)**

   `devstart` provides handy shortcuts for common commands.

   Using `brew`:

   ```
   brew tap jondot/tap && brew install devstart
   ```

   Alternatively, you can download a binary from [releases](https://github.com/jondot/devstart/releases/tag/v0.7.0).

#### Getting Started

To begin your journey, you'll need to solve various tests and make all the tests pass successfully. It will help you learn how to use LLMs and the `langchain` library effectively.

With `devstart`:

- Use `ds i` to install dependencies.
- Use `ds s` to start.

> `ds s` runs a pytest watcher, which re-runs tests automatically as you make modifications. The first run may take longer than subsequent ones.

If you prefer not to install `devstart`, use these commands instead:

- Run `poetry install` to install dependencies.
- Start tests with `poetry run ptw . --now --disable-warnings`.

#### Best Way to Learn

Learning is an adventure! Embrace the challenges and discover the best solutions by:

1. **Experimenting**: Print out code and observe the results, dive into the sources, and tinker with different approaches.
2. **Reading the Docs**: Explore the [langchain documentation](https://langchain-langchain.vercel.app/docs/get_started/introduction.html) and try out different concepts through experimentation.
3. **Seeking Hints**: If you're stuck, you can use:

   ```
   $ poetry run hints
   ```

   This will provide hints for solving the challenges. Search for the test name to find relevant tips.

#### Stay Updated

To stay updated with the latest developments, new features, and announcements, consider:

- **Watching**: Click the "Watch" button on GitHub to receive notifications about the project.
- **Starring**: Show your support by starring the repository on GitHub.
- **Social Media**: Follow our official social media channels for updates and community interactions.

#### Contributing

We welcome more contributions! Whether you're fixing bugs, adding new features, or improving documentation, your contributions are highly valued and appreciated.

To contribute to this repo, follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request to the `main` branch of the original repository.

We review and discuss pull requests promptly.

When adding new tests keep in mind:

* Try to be educative, tests should be narrow in focus and demonstrate just one principle, technique, or tool
* Try to be short, and give a helpful `TODO` message
* If possible, have fun. For example use example data or texts that are fun, heartwarming, classics (songs, books, TV), but not offensive

#### Code of Conduct

This project is committed to providing a friendly, inclusive, and harassment-free environment for all contributors and users. We follow the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/0/code_of_conduct/) and expect everyone involved with the project to adhere to these guidelines.

If you encounter any behavior that violates the code of conduct, please report it by contacting the project maintainers.
