# Pandoctylus

A modern Python package for document processing.

## Installation

```bash
pip install pandoctylus
```

## Development

This project uses modern Python packaging with `pyproject.toml`. To set up the development environment:

1. Clone the repository:
```bash
git clone https://github.com/yourusername/pandoctylus.git
cd pandoctylus
```

2. Create a virtual environment and install development dependencies:
```bash
# Using uv (recommended)
uv venv  # Create virtual environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e ".[dev]"  # Install package in editable mode with dev dependencies

# Or using traditional pip
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e ".[dev]"
```

3. Run tests:
```bash
pytest
```

## Features

- Document processing with pypandoc
- Template-based document generation with python-docx-template

## License

MIT License 