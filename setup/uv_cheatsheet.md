# UV Installation & Project Set up Cheatsheet

**Author** Claude Opus 4.5 based on prompting from and with edits by Jeremy Mikecz



## Why UV?

    10-100x faster than pip
    Single tool for everything
    Automatic virtual environment management
    Cross-platform consistency
    Deterministic builds with lockfile

```
# Install uv (Windows PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Install uv (macOS/Linux)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install Python via uv
uv python install 3.12

# Verify installations
uv --version
uv python list
uv run python --version
```

## Project Lifecycle Commands

```
# Create new project
uv init my-project
cd my-project

# Select Python Interpreter within VSC
# Select the Python Interpreter you want to use for this project by opening the "Show and Run Command Bars" (Windows: `CTRL + SHIFT + P`; Mac: `CMD + CTRL + SPACE`), select **Python: Select Interpreter**, and choose the version of Python installed to your local environment. I.e.: `Python 3.14.2 (name-of-project) .venv/Scripts/python.exe       Recommended"
"""

# Add dependencies
uv add requests              # Add package
uv add pytest --dev          # Add dev dependency
uv add "flask>=2.0,<3.0"     # Add with version constraints

# Remove dependencies
uv remove requests

# Run commands
uv run python main.py        # Run script
uv run pytest                # Run tests
uv run python                # Interactive Python

# Sync environment
uv sync                      # Install all dependencies from lockfile
uv sync --frozen             # Strict sync (fail if lockfile outdated)

# Update dependencies
uv lock --upgrade            # Update all packages
uv lock --upgrade-package requests  # Update specific package
```

## VS Code Setup Checklist

     ✅ Install VS Code
     ✅ Install Python extension (ms-python.python)
     ✅ Install Jupyter extension
     ✅ Open project folder
     ✅ Select interpreter: Ctrl+Shift+P → "Python: Select Interpreter" → .venv
     ✅ Configure terminal to use uv

Key Files in UV Projects
```
my-project/
├── .venv/              # Virtual environment (auto-created)
├── .python-version     # Python version pin
├── pyproject.toml      # Project config & dependencies
├── uv.lock            # Locked dependency versions
├── src/               # Source code (optional)
│   └── my_project/
└── README.md
```

