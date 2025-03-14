# Python Code Checker

## Overview
Python Code Checker is a tool that analyzes Python scripts for syntax errors, styling issues, and best practices. It uses Python's `ast` module for syntax analysis and `flake8` for style checking.

## Features
- Detects syntax errors in Python code
- Identifies unused imports
- Flags the use of wildcard imports
- Detects unsafe functions like `eval()` and `exec()`
- Checks for code style violations using `flake8`

## Installation
Ensure you have Python installed. Then, install the required dependencies:
```sh
pip install flake8
```

## Usage
1. Place the Python script you want to check inside a text file (e.g., `code.txt`).
2. Run the script:
```sh
python syntax_checker.py
```
3. The tool will output any syntax errors, unused imports, wildcard imports, or style violations.

## Project Structure
```
Python Code Checker/
│── syntax_checker.py  # Main script for code analysis
│── code.txt           # Sample Python code to analyze
│── README.md          # Project documentation
```

## Contributing
Feel free to fork this repository and contribute improvements!

## License
This project is open-source under the MIT License.


