# Django
Django is a Python framework that makes it easier to create web sites using Python.Django takes care of the difficult stuff so that
you can concentrate on building your web applications.
## Key Features of Django:
- Django is a back-end server side web framework.
- Django is free, open source and written in Python.
- Django makes it easier to build web pages using Python.

## Django Requires Python
To check if your system has Python installed, run this command in the command prompt:
```
python --version
```
## Pip python package manager like npm
To install Django, you must use a package manager like pip, which is included in Python when simply install python.
To check if your system has pip installed, run this command in the command prompt:
```
pip --version
```
## Virtual Environment
It is suggested to have a dedicated virtual environment for each Django project, and one way to manage a virtual environment is ``virtualenv``package, which is included in Python

## check virtualenv package is installed or not 
```python 
pip list
```
## if virtualenv is not installed that install this package
```python 
pip install virtualenv
```
## check version of virtualenv
```python 
virtualenv --version
```
## Now create a virtual environment
- Create a directory for example Django-development
- cd Django-development or open in vs code and type in cmd
```python
python -m virtualenv virtual
```
## Now see a folder virtual is created and inside this virtual you will folders structure like this
<pre>
virtual
    |____ lib
    |        |___site-packages   
    |            |___ .......
    |____ Scripts
    |           |____ ....... 
    |____ pyvenv.cfg  
</pre>
## Then you have to activate the environment, by typing this command:
- On Window
```
virtual\Scripts\activate

```
## Once the environment is activated, you will see this result in the command prompt:
```python
(virtual) C:\Users\aaaa\Desktop\Batches\Django_Development
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
