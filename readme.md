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


```python
C:\Users\DELL\Desktop\RoadMap\DJ\virtualenv.txt\Scripts\activate
```
```python
deactivate
```
- By deafult suppose python 3.11 is installed on your C drive
```python
 Virtualenv 3.11 created.
```

## Step2:
- if you want to create different python versions on your virtual environmeent you need to install python 3.9 and python 3.11 separately.
### Step 2
- where python
```python
C:\Python\python.exe
```
```python
C:\Users\DELL\AppData\Local\Programs\Python\Python39\python.exe
```
```python
C:\Users\DELL\AppData\Local\Microsoft\WindowsApps\python.exe
```
```python
 python -m virtualenv -p C:\Users\DELL\AppData\Local\Programs\Python\Python39\python.exe python3.9
```
```python
 C:\Users\DELL\Desktop\RoadMap\DJ\python3.9\Scripts\activate
```
```python
 python --version
```
```python
 python -m pip install requests==2.6.0
```
- install python specific libraries version
### How to get Django ?
Get the latest official version
```python
The latest official version is 5.0.1. Read the 5.0.1 release notes, then install it with pip:
pip install Django==5.0.1
```
- deactivate
