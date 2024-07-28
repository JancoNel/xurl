# Xurl

xurl is a powerful tool designed to extract URLs from Python executables.

![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)

## Features

- Extracts URLs from Python executables.
- Easy to use with a simple command-line interface.
- Supports executables compiled with PyInstaller.

## Prerequisites

- Python environment
- [pyinstxtractor](https://github.com/extremecoders-re/pyinstxtractor)

## Installation

To install xurl, simply clone this repository and navigate to the project directory:

```bash
git clone https://github.com/JancoNel-dev/xurl.git
cd xurl
```

## Usage

1. **Make sure your executeable was made with Pyinstaller**

2. **Extract the executable using pyinstxtractor:**

    ```bash
    pyinstxtractor.py your_exe_file
    ```

3. **Locate the main .pyc file in the output folder.**

4. **Run xurl on the main .pyc file:**

    ```bash
    python xurl.py main.pyc
    ```

    xurl will print all the URLs it finds in the file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
