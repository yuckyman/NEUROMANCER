# Agent Guidelines

This document outlines the expected behavior and guidelines for agentic coding agents operating within this repository. Adherence to these guidelines ensures consistency, maintainability, and efficient collaboration.

## 1. Build, Lint, and Test Commands

- **General:** While specific commands vary by language and framework, common practices include:
    - **Python:** `python -m venv venv`, `source venv/bin/activate`, `pip install -r requirements.txt`, `ruff check .`, `pytest`
    - **JavaScript/TypeScript:** `npm install`, `npm run lint`, `npm test`
    - **Shell Scripts:** `bash script_name.sh`
- **Running a Single Test:**
    - **Python (pytest):** `pytest path/to/test_file.py::test_function_name`
    - **JavaScript (Jest):** `npm test -- -t 'test name'` (or similar, depending on Jest configuration)

## 2. Code Style Guidelines

- **Imports:**
    - Group imports logically (standard library, third-party, local).
    - Avoid wildcard imports (`from module import *`).
- **Formatting:**
    - Adhere to established style guides (e.g., PEP 8 for Python, Prettier for JS/TS).
    - Maintain consistent indentation (spaces preferred over tabs).
    - Use meaningful whitespace to improve readability.
- **Types:**
    - Utilize type hints (e.g., Python type annotations, TypeScript) where appropriate to enhance code clarity and enable static analysis.
- **Naming Conventions:**
    - **Variables & Functions:** Use camelCase for JavaScript/TypeScript, snake_case for Python.
    - **Classes:** Use PascalCase for all languages.
    - **Constants:** Use SCREAMING_SNAKE_CASE.
    - Names should be descriptive and clearly indicate the purpose of the entity.
- **Error Handling:**
    - Implement robust error handling using try-except blocks (Python) or try-catch blocks (JavaScript/TypeScript).
    - Provide clear and informative error messages.
    - Differentiate between recoverable errors and critical failures.
- **Modularity:**
    - Write small, focused functions and modules.
    - Aim for high cohesion and low coupling.
- **Comments:**
    - Add comments to explain the *why* behind complex logic, not the *what*.
    - Keep comments concise and up-to-date.

## 3. Cursor and Copilot Rules

- If `.cursor/rules/` or `.github/copilot-instructions.md` exist, consult these files for specific agent behavior and constraints. These files may override or supplement the general guidelines above.

## 4. Project Structure Philosophy

- Refer to `0_admin/00_index/00.01_structure_guide.md` for details on the project's directory structure and organizational philosophy (e.g., Johnny Decimal System).
