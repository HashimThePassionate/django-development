from django.shortcuts import render
from datetime import datetime
# Create your views here.
def home(request):
    name : str = "Muhammad Ahmed"
    age  : int= 28
    d : dict = {'n':name,'a':age}
    return render(request,'index.html', d)


def ourHome(request):
    multiString ="""One
    two
    three
    four"""
    name = "muhammad Hashim"
    age = 20
    list1 = [1,2,3]
    list2 = [4,5,6]
    django = "I'm using django"
    dj = "Django"
    nick = "MUHAMMAD"
    D = datetime.now()
    value = 123456789
    f = 34.23234
    messages = 1
    welcome = "&quotWelcome&quot to &#x27;&ltDjango&gt;&#x27; Programming"
    list3 = [  {"name": "Zahid", "age": 19},{"name": "Ahmed", "age": 22},{"name": "Jamshed", "age": 31},]
    d = {'name':name, 'age':age, 'list1':list1, 'list2':list2, 'django':django, 'dj':dj, 'D':D,'list3':list3,'value':value, 'f':f, "m":multiString, 'nick':nick, 'messages': messages , 'w':welcome}
    return render(request,'home.html',d)