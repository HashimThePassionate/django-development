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
## if you learn about python please go to this repo step by step
**[Pythonforpassionate](https://github.com/HashimThePassionate/Python-For-Absolute-Beginners)**
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
## deactivate virtual environment simple type in cmd
```python
deactivate
```
## By default python version 3.11 installed in this virtual environment
- Because python 3.11 version installed globally on my machine
- to install different python version 
- go to [python.org](https://www.python.org/downloads/) and install different  version globally
- we are going to install python 3.12 separately
- so have a look to our environment variables when two different python versions is installed
<pre>
C:\Users\aaaa\AppData\Local\Programs\Python\Python311\Scripts\;
C:\Users\aaaa\AppData\Local\Programs\Python\Python311\;
C:\Users\aaaa\AppData\Local\Programs\Python\Python312\Scripts\;
C\Users\aaaa\AppData\Local\Programs\Python\Python312\;
</pre>

##  Now we want to install python 3.12 on our new virtual environment
first run command
```
where python
```
- expected output
<pre>
C:\Users\DELL\AppData\Local\Programs\Python\Python3.12\python.exe
C:\Users\DELL\AppData\Local\Programs\Python\Python3.11\python.exe
</pre>

## copy the path of python 3.12 version and create a new virtualenv
```
python -m virtualenv -p C:\Users\DELL\AppData\Local\Programs\Python\Python3.12\python.exe Virtual3.12
```
## Now again check python version
```
python --version
```
## Congratulations You have python 3.12 on new virtual environment

## Install Django
Now, that we have created a virtual environment, we are ready to install Django.
**Note: Remember to install Django while you are in the `` virtual environment `` !**
Django is installed using pip, with this command:
```
(virtual3.12) C:\Users\aaaa\Desktop\Batches\Django_Development>pip install Django==5.0.1
```
## to check django install or not run this cmd
```
(virtual3.12) C:\Users\aaaa\Desktop\Batches\Django_Development>django-admin --version
```
<pre>
    5.0.1
</pre>
## Deactivate virtualenv  
```
deactivate
```
## Now we deactivate virtual environment check django again 
```
django-admin --version
```
- Note we got error this error
<pre>
'django-admin' is not recognized as an internal or external command,
operable program or batch file.
</pre> 
-  Why we got this error please have a research thank you!!!!

#### Regards Muhammad Hashim
