# Devin Onboarding

A Python library project template for onboarding purposes.

## Project Structure

- `src/`: Contains the source code for the project
- `tests/`: Contains pytest tests for the project
- `docs/`: Contains Sphinx documentation

## Documentation

The project documentation is automatically built and deployed to GitHub Pages:

[View Documentation](https://SeitaroShinagawa.github.io/devin-onboarding/)

To build the documentation locally:

```bash
cd docs
make html
```

Then open `docs/_build/html/index.html` in your browser.

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install the package in development mode:
   ```bash
   pip install -e .
   ```

## Testing

Run tests using pytest:
```bash
pytest
```
