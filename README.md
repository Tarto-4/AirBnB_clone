# AirBnB_clone
Project completed for ALX.
![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/263/HBTN-hbnb-Final.png)

## Table of Contents
* [**Project Details**](#project-details)
	* [Description](#description)
	* [Project Requirements](#project-requirements)
	* [Project Objectives](#what-students-should-learn-from-this-project)
* [**Project Breakdown**](#project-breakdown)
* [**Getting Started**](#getting-started)
    * [Installation](#installation)
	* [Screenshots](#screenshots)
* [**Contributing**](#contributing)
* [**Team**](#team)
* [**Resources**](#resources)

---
## Project Details

### Description
![image](https://www.holbertonschool.com/assets/holberton-logo-1cc451260ca3cd297def53f2250a9794810667c7ca7b5fa5879a569a457bf16f.png)
Project for [ALX](https://github.com/holbertonschool/). First step: Write a command interpreter to manage your AirBnB objects.

This is the first step towards building a full web application: an AirBnB clone. This first step is very important because everything built during this project will be used in all following projects: HTML/CSS templating, database storage, API, front-end integration...

Each tasks are linked and will help you to: 
- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances 
- create a simple flow of serialization/deserialization: 
```Instance <-> Dictionary <-> JSON string <-> file ```
- create all classes used for AirBnB (User, State, City, Place...) that inherit from BaseModel 
- create the first abstracted storage engine of the project: File storage. 
- create all unittests to validate all our classes and storage engine

#### Environment 
Ubuntu 14.04 LTS

#### Python version
Python 3.4.3

#### Style
PEP 8 (v.1.7)

### Project Requirements
#### Requirements for Python scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `PEP 8` style
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)

#### Requirements for Python unit tests
For this project, you will create unit tests, not doctest:

- Allowed editors: `vi`, `vim`, `emacs`
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- You have to use the [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
- All your test files should be python files (extension: `.py`)
- All your test files and folders should start by `test_`
- Your file organization in the tests folder should be the same as your project: ex: for `models/base_model.py`, unit tests must be in: `tests/test_models/test_base_model.py`
- All your tests should be executed by using this command: `python3 -m unittest discover tests`
- You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base_model.py`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- We strongly encourage you to work together on test cases, so that you don't miss any edge case

### What students should learn from this project
- At the end of this project students are expected to be able to explain to anyone, without the help of Google:
- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

## Project Breakdown

## Getting Started

### Installation
To use this project:

1. Clone
```
https://github.com/yeungegs/AirBnB_clone.git
```

2. On your machine, navigate (`cd`) to the newly created directory
```
cd AirBnb_clone
```

3. Start the console in one of the modes outlined below!

### Screenshots
This console works in interactive mode:
```shell
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```


This console also works in non-interactive mode:
```shell
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

## Contributing
This project is a closed and contributions are not accepted at this time. 

## Team

 | [Thato Mongwe](https://github.com/tarto-4) <a target="_blank" href="https://x.com/THATOMongwe4"> <img src="https://github.com/account" height="20"></a>

## Resources
* Readme template from GitHub https://guides.github.com/features/wikis/
* Docker generate-authors script https://github.com/docker/docker/blob/master/hack/generate-authors.sh
