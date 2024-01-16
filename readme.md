
# Django
Django is a Python framework that makes it easier to create web sites using Python.Django takes care of the difficult stuff so that
you can concentrate on building your web applications.
## Key Features of Django:
Django is a back-end server side web framework.

Django is free, open source and written in Python.

Django makes it easier to build web pages using Python.

## Django Requires Python
To check if your system has Python installed, run this command in the command prompt:
```
python --version

```
## PIP
To install Django, you must use a package manager like PIP, which is included in Python from ``version 3.4``.
To check if your system has PIP installed, run this command in the command prompt:
```
pip --version

```

## Virtual Environment
It is suggested to have a dedicated virtual environment for each Django project, and one way to manage a virtual environment is ``venv``, which is included in Python.

The name of the virtual environment is your choice, for example ``virtual``.
Type the following in the command prompt, remember to navigate to where you want to create your project:
```
py -m venv virtual

```
This will set up a virtual environment, and create a folder named "virtual" with subfolders and files, like this:
```
virtual
  Include
  Lib
  Scripts
  pyvenv.cfg

```
Then you have to activate the environment, by typing this command:

```
virtual\Scripts\activate.bat

```
Once the environment is activated, you will see this result in the command prompt:

```
(virtual) C:\Users\Your Name>

```
## Install Django
Now, that we have created a virtual environment, we are ready to install Django.

**Note: Remember to install Django while you are in the `` virtual environment `` !**

Django is installed using pip, with this command:
```
(virtual) C:\Users\Your Name>py -m pip install Django
```
## We can create different virtual environments with different Python Versions ! 
Steps for this are : 
## Step1
- Create a directory for example Dj
- cd Dj or open in vs code
### If ``virtualenv`` is not present install it
```python 
pip install virtualenv
```
### To check it's version and for confirmation use
```python 
virtualenv --version
```
### Creating a Virtual Environment named "tutorial-env"
```python
python -m venv tutorial-env
```
### Checking Python's version in this environment
```python
python --version
```
### Activating our Virtual Environment
```python
C:\Users\DELL\Desktop\RoadMap\DJ\virtualenv.txt\Scripts\activate
```
### Deactivating this environment incase of having multiple environments to work with 
```python
deactivate
```
### By default if suppose python vesion 3.11 is installed on your C drive, it shows
```python
 Virtualenv 3.11 created.
```

## If you want to create different python versions on your virtual environment you need to install atleast any 2 diffferent versions of python,e.g  ``python 3.9`` and python ``3.11`` separately.

### For checking Python's files location on pc
 write in terminal ``where python``.
 Result:
```python
C:\Python\python.exe
```
```python
C:\Users\DELL\AppData\Local\Programs\Python\Python39\python.exe
```
```python
C:\Users\DELL\AppData\Local\Microsoft\WindowsApps\python.exe
```
### Creating another Virtual Environment with a different Python Version
```python
 python -m virtualenv2 -p C:\Users\DELL\AppData\Local\Programs\Python\Python39\python.exe python3.9
```
### Activating this Virtual Environment
```python
 C:\Users\DELL\Desktop\RoadMap\DJ\python3.9\Scripts\activate
```
### Checking the Python Version in this virtual environment
```python
 python --version
```
which will now show ``python 3.9``
##  Now we have 2 different virtual environments with different python versions

## After this we can 
- deactivate this environment and switch between the 2 environments that we have
- install python specific libraries version in the different environments
### installing a specific version of the requests library using the Python package manager 'pip'
```python
 python -m pip install requests==2.6.0
```
