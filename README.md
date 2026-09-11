# CimerbotPy

A Python automation experiment for interacting with the CİMER web flow through browser automation.

> **Important:** This is an unofficial community project and is not affiliated with CİMER, e-Devlet or any Turkish government institution. Website changes may break the automation. Use it responsibly and comply with applicable service rules.

## Requirements

- Python 3.x
- A supported browser/webdriver environment
- Dependencies listed by the project
- An account configured for the relevant official service

## Installation

```bash
git clone https://github.com/KayJss/CimerbotPy.git
cd CimerbotPy
python -m venv .venv
```

Activate the virtual environment, then install the project dependencies and run:

```bash
python main.py
```

## Configuration

The current version reads configuration from `classes.py`. Before running the project, review the configuration fields for the account, email, application text and character limits.

**Do not commit real credentials or personal identifiers.** A safer future version should load sensitive configuration from environment variables instead of source files.

## Security

- Never publish passwords, identity numbers or session information.
- Use a dedicated local environment and keep credentials out of Git history.
- Review [SECURITY.md](SECURITY.md) before reporting security issues.
- Do not use automation for spam, harassment or mass submissions.

## Project status

This repository is an experimental browser-automation project. Planned improvements include safer configuration, clearer error handling, testable modules and reduced coupling between browser logic and user settings.

## Contributing

Keep pull requests focused and never include real account credentials or personal data in examples, logs, screenshots or tests.

## License

See [LICENSE](LICENSE).
