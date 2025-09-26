---
title: Managing Multiple Python Versions With pyenv
link: https://realpython.com/intro-to-pyenv/
summary: 'pyenv is a package manager for managing multiple Python versions on Linux systems. It allows you to switch between different versions of Python without affecting other projects or system-wide packages. To use pyenv, follow these steps:

1. Install pyenv by running `sudo apt-get install python3.8` (for Ubuntu-based systems) or `sudo apt-get install python3.8` (for Debian-based systems).

2. Create a new environment for each project you want to work on.

3. Activate the desired environment using `pyenv activate <environment_name>`.

4. Install any necessary dependencies in the activated environment.

5. Use Python commands like `python -m venv <venv_name>` and `pip install -e .` to switch between different versions of Python.

6. To keep your projects compatible with each other, you can use a tool like `pyenv-virtualenv` or `pyenv-rebase`.

7. To avoid conflicts when switching between multiple versions of Python, make sure to update the `PATH` variable in your shell configuration file (e.g., `.bashrc`, `.zshrc`) after installing new versions.

8. Keep in mind that pyenv is not a replacement for pip or conda, but it can be used as an alternative when you need to switch between different Python versions without affecting other projects or system-wide packages.

By using pyenv, you can manage multiple Python versions on your Linux system, prevent conflicts, and keep your projects compatible and development smooth.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: f11e73830e1fbba6afbd3b46b4ecb7b51de25db647d04c38eb8c5c24d4c18c1e
feed_title: Real Python
feed_url: https://realpython.com/atom.xml
date_processed: '2025-09-22T17:07:13.364526'
category: 24-computing
---

Learn how to use pyenv to manage multiple Python versions, prevent conflicts, and keep your projects compatible and development smooth.