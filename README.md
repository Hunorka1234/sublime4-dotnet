# sublime4-dotnet

A Microsoft .NET integration for Sublime Text 4 on Unix-based systems, with special focus on MATE desktop environment.

## Features

- Quick .NET project creation with file explorer (Ctrl+Shift+D)
- Custom build system for running .NET projects in MATE Terminal
- Automatic project folder opening in new Sublime window
- Interactive terminal support for development

## Requirements

- Sublime Text 4
- MATE Desktop Environment
- .NET SDK
- Additional packages:
  ```bash
  sudo pacman -S dotnet-sdk mate-terminal zenity xdotool

README.md
Installation

    Clone this repository:

    cd ~/.config/sublime-text/Packages/
    git clone https://github.com/Hunorka1234/sublime4-dotnet User

    Restart Sublime Text

Usage
Creating New Projects

    Press Ctrl+Shift+D
    Select project location in file explorer
    Enter project name
    New project opens automatically in fresh Sublime window

Building/Running Projects

    Open any .cs file
    Press Ctrl+B or F7
    MATE Terminal opens in project directory
    Project starts running automatically

Configuration

Default project creation path: /home/nagyhunor/Documents/nerdstuff/programming (edit for your use case, its my programming folder)

    Edit this in dotnet_new_project.py

Testing & Feedback

Currently in testing phase. Your feedback is valuable!

    Email: hunoramester@gmail.com
    Issues: Create on GitHub

Compatibility

Tested on:

    Arch Linux with MATE Desktop
    Sublime Text 4
    .NET 7.0+

Planning to expand support for other Unix environments and terminal emulators.
Contributing

Feel free to:

    Test on different setups
    Report issues
    Submit pull requests
    Suggest improvements
