# cmd_utils
[![Build Status](https://travis-ci.org/CBSkarmory/cmd_utils.png)](https://travis-ci.org/CBSkarmory/cmd_utils)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## How To Use
 - be using unix
 - get this repo with `git clone https://github.com/CBSkarmory/cmd_utils.git` or 
 `git clone git@github.com:CBSkarmory/cmd_utils.git` (for https and ssh respectively)
 - add it to your PATH. (You can add `export PATH=$PATH:<directory name here>` to 
 your `~/.profile` file and use `source ~/.profile` to set it up immediately.) 
 Make sure to add a blank line at the end of `~/.profile`.
 - compile the files you want. Generally, use `<compiler> <file name>`: `javac` for Java, and `gcc` for C. 
 - alternatively, use `make`.
 - set up aliases to run programs faster. For example, you can alias `avg` to `java Average`.
 - use `chmod u+x <PROGRAM_NAME>` for python scripts to run directly

## Tool Usage
|Prorgam|usage                       |
|-------|:---------------------------|
|average calculator|`java Average`|
|password generator|`python3 pwdgen.py`|
