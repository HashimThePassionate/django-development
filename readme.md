{\rtf1}
Step1
1 . Create a directory for example Dj
2 . cd Dj or open in vs code
3 . pip install virtualenv
4.  virtualenv --version
5.  python -m venv tutorial-env
6.  python --version
7.  C:\Users\DELL\Desktop\RoadMap\DJ\virtualenv.txt\Scripts\activate
8.  deactivate
By deafult suppose python 3.11 is installed on your C drive
Virtualenv 3.11 created.

Step2:
if you want to create different python versions on your virtual environmeent you need to install python 3.9 and python 3.11 separately.
Step 2
1. where python
C:\Python\python.exe
C:\Users\DELL\AppData\Local\Programs\Python\Python39\python.exe
C:\Users\DELL\AppData\Local\Microsoft\WindowsApps\python.exe
2. python -m virtualenv -p C:\Users\DELL\AppData\Local\Programs\Python\Python39\python.exe python3.9
3. C:\Users\DELL\Desktop\RoadMap\DJ\python3.9\Scripts\activate
4. python --version
5. python -m pip install requests==2.6.0
install python specific libraries version
6. deactivate