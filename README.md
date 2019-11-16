# Setting up testframework in Python

## Setup 

### Folder structure

1. create new folder for your project (e.g. tdd_test_project)
2. create two new folders within this folder
    - my_greetings (for your source code)
    - tests (for your test files)
3.  Inside my_greetings, create an empty file called \_\_init\_\_.py. Creating the \_\_init\_\_.py file means that the my_greetings folder can be imported as a module from the parent directory.

    tdd_test_project/  
    │  
    ├── my_greetings/  
    │&emsp;&emsp;└──\_\_init\_\_.py  
    │&emsp;&emsp;└── greetings.py  
    |  
    ├── tests/  
    &emsp;&emsp;└── test_greetings.py  

    
insert a first dummy test into the test_greetings.py

```python
import pytest

def test_greet():
pass
```


### Installs
- install pytest


        conda install pytest


### Testenvironment

#### using VSCode Extension
- install VSCode Extensions ("Python")
- use "Test" Menu item in left sidebar to discover tests:
    - select "pytest" as framework
    - select "tests" as test folder
- run test

#### using comand line
run:

        python -m pytest

or even shorter:


        py.test

## Writing tests

### Process

- write a test that fails (bc no code has been written yet)
- watch it fail!
- implement enough code to make it pass
- run test and watch it pass

### Assert

anything that evaluates to "True" or "False" can be used as assertion

e.g. 
```python
assert 1+2 == 3 # successful assertion
assert "Hello" == "Hello" # successful assertion
assert "Hello" == "Hi" # assertion fails
assert "Hello" != "Hi" # successful assertion
assert isinstance("Hello", str) # successful assertion
```


### Task

1. We want to create a function, that greets our CorrelAid members. Therefore, write a function that returns a greeting in English.
2. As CorrelAid becomes more international, we want to extend the greet function, so we can greet in all languages, where CorrelAid is represented (German, English, Dutch, French). The greet function should therefore take the language as input and return the proper greeting. If no language is specified, greet in English.
3. To personalize the greeting even more, we also want to include the name of the person to be greeted. I no name is specified, greet without a name.

