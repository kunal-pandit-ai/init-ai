# Init AI

> Create production-ready AI project structures with a single CLI command.

![Python](https://img.shields.io/badge/Python-3.12+-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

# What is Init AI?

Init AI is a command-line tool that helps developers bootstrap AI and Python projects instantly.

Instead of manually creating folders, files, configuration, and project structure every time, Init AI generates a clean, production-ready project in seconds.

Whether you're building an AI application, FastAPI backend, CLI tool, or Python package, Init AI saves time by automating repetitive project setup.

---

# Problem It Solves

Creating a new project usually requires manually creating files like:

- .venv/
- .gitignore
- README.md
- LICENSE
- pyproject.toml
- src/
- tests/
- configuration files

Doing this repeatedly is slow and error-prone.

Init AI automates the entire setup process with one command.

---

# Features

- 🚀 Create projects in seconds
- 📁 Generate production-ready folder structures
- ⚙️ Configuration management
- 🛠️ Built with Typer
- 📦 Modern Python packaging
- 💻 Cross-platform
- ❤️ Open Source

---

# Contributing

Contributions are welcome.

Please read

CONTRIBUTING.md

before submitting a Pull Request.

---

# Installation

```bash
git clone https://github.com/kunal-pandit-ai/InitAI.git

cd init_ai

uv venv

source .venv/bin/activate

uv pip install -e .

# QUICK START 

init-ai hello

init-ai version

init-ai create project my-ai-app

# More commands are documented inside /docs.