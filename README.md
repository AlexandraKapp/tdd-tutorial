# Slides
https://alexandrakapp.github.io/tdd-tutorial/presentation/presentation.slides.html 

# Setting up testframework in Python

## Setup 

### Folder structure

1. create new folder for your project (e.g. tdd_test_project)
2. create two new folders within this folder
    - my_greetings (for your source code)
    - tests (for your test files)
3.  Inside my_greetings and tests, create an empty file called \_\_init\_\_.py. Creating the \_\_init\_\_.py file means that the my_greetings folder can be imported as a module from the parent directory.

    tdd_test_project/  
    │  
    ├── my_greetings/  
    │&emsp;&emsp;└──\_\_init\_\_.py  
    │&emsp;&emsp;└── greetings.py  
    |  
    ├── tests/  
    &emsp;&emsp;└──\_\_init\_\_.py  
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

#### Mocking:

*Mock a class*

    A seperate "Person" class represents CorrelAid members. The class has instance the instance variables "nationality" and "firstname". 
3. Mock the class "Person" and use the mocked instance as input for your greet function. Return the language of the greeting according to the Persons nationality.
4. To personalize the greeting even more, we also want to include the name of the person to be greeted. If no name is specified, greet without a name.

*Mock a function*

5. Change the greeting according to the daytime. Pretend that you have a function "get_daytime", that returns the current datime for the proper greeting, by mocking the function.


#### Setup with fixture:
6. Extract the two mocks into "fixtures" so they can be reused for multiple tests.


## Code Coverage

How much of your code is covered with tests? With code coverage you get a percentage of lines of code that are run with your tests.


        conda install pytest-cov

get covered percentage:

        pytest --cov=my_greetings tests/

### See which lines in your code are not covered:


*Directly in source code*

- Install VSCode Plugin "Coverage Gutters"
- get annotations, with xml:

        pytest --cov=my_greetings tests/ --cov-report xml

- open source file and "Display Coverage"

*Alternative: seperate annotated file*

get annotations, which files are covered (for direct view in file):

        pytest --cov=my_greetings tests/ --cov-report annotate:cov_annotate

*Alternative: HTML in Browser*

get annotations, which files are covered (for html output to view in browser):

        pytest --cov=my_greetings tests/ --cov-report html


## Travis CI (Continous Integration)


## General

### Best Practices

- Use long, descriptive names. This often obviates the need for doctrines in test methods.
- Tests should be isolated. Don’t interact with a real database or network. Use a separate test database that gets torn down or uses mock objects.
- Focus on one tiny bit of functionality.
- Should be fast, but a slow test is better than no test.
- It often makes sense to have one test case class for a single class or model.