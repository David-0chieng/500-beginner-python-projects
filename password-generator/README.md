# Password Generator

A simple command-line password generator that creates a random password using a customizable mix of lowercase letters, uppercase letters, digits, and special characters.


## Table of Contents
- [Features Overview](#features-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Next Steps](#next-steps)
- [Author](#author)


## Features Overview

- **Custom length** — choose exactly how many characters your password will have
- **Uppercase letters** — optionally include A–Z characters
- **Digits** — optionally include 0–9
- **Special characters** — optionally include punctuation symbols (e.g. `!@#$%`)
- **Guaranteed inclusion** — if you enable a character type, at least one of that type is guaranteed to appear in the output
- **Shuffled output** — the final password is shuffled so guaranteed characters don't appear in a predictable position
- **Input validation** — raises an error if the requested password length is too short to fit all the enabled character types


## Installation
To install this program, use the commands below:
```bash
git clone https://github.com/fmax-dev/PASSWORD-GENERATOR.git
cd PASSWORD-GENERATOR
```

No external dependencies are required — the program uses only Python's standard library (`random` and `string`).


## Usage
To start using this program:

1. Clone this repo using the commands above
2. Run the program:
    - Windows: `python password_generator.py`
    - Mac/Linux: `python3 password_generator.py`
3. Answer the prompts:
    - Enter your desired password length
    - Choose whether to include uppercase letters (`y`/`n`)
    - Choose whether to include digits (`y`/`n`)
    - Choose whether to include special characters (`y`/`n`)
4. Your generated password is displayed — store it somewhere safe!

**Example session:**
```
====================== WELCOME TO PASSWORD GENERATOR ==========================

How many characters would you like your password to have: 16
Would you like your password to have uppercase characters? (y/n): y
Would you like your password to have digits? (y/n): y
Would you like your password to have special characters? (y/n): y

Here's your password: aT3#mKz9!rLqW2@v
Please keep it somewhere safe!
```


## Next Steps

Looking to expand the project? Here are a few potential improvements for future versions:

- **Multiple passwords** — generate a batch of N passwords in one run
- **Copy to clipboard** — automatically copy the result so it's ready to paste
- **Password strength indicator** — rate the generated password's entropy
- **Save to file** — optionally append generated passwords to a local file
- **GUI / web interface** — a browser or desktop UI for non-technical users
- **Exclude ambiguous characters** — option to omit characters like `0`, `O`, `l`, `1` that are easy to confuse


## Author

[fmax-dev](https://github.com/fmax-dev)