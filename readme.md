## Create a Django Project
- first entre the virtual by using following command
```python
cd virtual
```
- Then entre into lib  by using following comand
```python
 cd lib
```
- Then entre into side-packages by using following command
```python
  cd side-packages
```
### Command to check django installation folder
```python
pip show django
```
- Once Django is installed, you can create a Django project using the following command:
```python
django-admin startproject projectname
```
- if you want to come backword use following command
```python
 cd ../
```
### After Creating Project projectname we see these levels
```
projectname
    |____ projectname
    |        |___ __init__.py   
    |        |___ asgi.py
    |        |___ settings.py
    |        |___ urls.py
    |        |___ wsgi.py
    |____ manage.py
```
### init.py file
 This folder which contains init file is considered as python package.
 ### wsgi.py file
WSGI (Web Server Gateway Interface) is a specification that describes how a web server communicates with web applications. WSGI provies synchronous Python App.

### asgi.py file
ASGI (Asynchronous Server Gateway Interface) it provides both synchronous and Asynchronous Python App.

### Settings.py file
This files contains all the information or data about project settings
e.g. Database Configuration, Template install, Validation etc.

### urls.py file
This file contains information of url attached with application.

### manage.py file
manage.py atomatically created in each django project. It is a django commandline utility also sets DJANGO_SETTINGS_MODULE environment variable so that it can points to your django project's settings file.
## Now How to Create and Start Application
- A Django project contain one or more applications inside project. Steps to create applications
- Go to Project Folder
- Run the following command
```python
django-admin startapp admission
```
- creating multiple applications run the following commands
```python
django-admin  startapp admission
django-admin  startapp student
django-admin  startapp teacher
```
### Now Installing Application in our Project
- Open settings.py file and add apps name in ``` INSTALLLED_APPS ``` section
- ``` setting.py ``` file present in the project folder Not in application folder
```
INSTALLED_APPS [
    'django.contrib.admin',
    'course',
    'admission',
    'teacher',
]
```
### Write your first view
- open your app views.py file and paste the view as a function
```python
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h3>Hello This is our first App just for Practice </h3>")
```
### Urls Pattern in Project level urls.py
- Simple open your project level urls.py file and find urlpatterns list variable and mention your view in path variable, make sure to import views from your app
```python
from django.contrib import admin
from django.urls import path
from SimpleApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.index),
]
```
### now run your server with simple this code
```python
python manage.py runserver
```
- Now here is the point, when you run the server you will see error like
```
Page not found (404)
Request Method:	GET
Request URL:	http://127.0.0.1:8000/
Using the URLconf defined in Alfa.urls, Django tried these URL patterns, in this order:
admin/
home/
The empty path didn’t match any of these.
You’re seeing this error because you have DEBUG = True in your Django settings file. Change that to False, and Django will display a standard 404 page.
```
- This error tells that you url is not found to fix this paste this url
```python
http://127.0.0.1:8000/home/
```
3. Now when you look the url pattern you, will see i mention /home/ after the url bcz when i define the url i clearly mention 'home/' in  urlpatterns variable so to access this we must mention this url
http://127.0.0.1:8000/home/
4. Now we need to define a default url pattern than what we do, here is the example go to urls.py and paste this code
```
from django.contrib import admin
from django.urls import path
from SimpleApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
]
```
5. Now when you run the server you will see the url is working default.

### Urls Patterns inside  in Application  urls.py
1. Simply create view in views.py in app level
```
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h3>Hello This is our first App just for Practice </h3>")
```
2. now create urls.py in app level directory. To create a URLconf in the App directory, create a file called urls.py. Your app directory should now look like.
<pre>
App/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    urls.py
    views.py
</pre>
3. open urls.py and paste this code
4. This is the simplest view possible in Django. To call the view, we need to map it to a URL - and for this we need a URLconf.
### In the App/urls.py file include the following code
```
from django.urls import path
from SimpleApp import views
urlpatterns = [
    path("",views.index, name="home"),
]
```
### The next step is to point the root URLconf at the project.urls module
1. In project/urls.py, add an import for django.urls.include and insert an include() in the urlpatterns list, so you have:
```
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include('SimpleApp.urls')),
]
```
### Template 
1. A Template is a text file, it can generate any text-based format (HTML, CSV, XML etc)
2. A template contains variables, which get replaced with values when the template is evaluated, and tages, which control the logic of template.
3. Template is used by view function to represent the data to user.
4. User sends request to view then view contact template after that view get information from the template and then view gives response to user.

### Create dynamic templates folder inside root directory
1. Simply create "templates" directory inside project folder 
<pre>
projectname/
├── projectname/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
|   |__ templates
|      |___ home.html
|      |___ about.html
|      |___ contact.html
|      |___ blog.html
├── manage.py
└── myapp/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations/
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py
</pre>

### Simply create home.html file inside templates directory 
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- <meta http-equiv="refresh" content="05"> -->
    <title>Div </title>
</head>
<body>
    <article>
        <h2>Google Chrome</h2>
        <p>Google Chrome is a web browser developed by Google, released in 2008. Chrome is the world's most popular web browser today!</p>
    </article>
    <details>
        <summary>Epcot Center</summary>
        <p>Hi,{{name}} How are you? Your age is {{age}}</p>
    </details>
    <p>I have a date on <time datetime="2008-02-14 20:00">Valentines day</time>.</p>
</body>
</html>
```
### Add "TEMPLATE_DIR" in settings.py 
```
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],//Add TEMPLATE_DIR here
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
### What is render() function 
1. When you call render(), it combines the provided template with a context dictionary (containing data to be inserted into the template) and generates an HTML response.
- render()- It combines a given template with a given context dictionary and returns an Httpresponse object with that rendered text.
<pre>
Syntax:
    render(request,template_name, context = dict_name, using = None)
Where,
request -- The object used to generate this response.
template_name -- The full name of a template to use or sequence of templates names, if a sequence is given, the first template thats exists will be used.
context -- A dictionary of values to add to the template context. By default, this is an empty dictionary. if a value in the dictionary is callable, the view will call just before rendering the template.
using -- The NAME of a template engine to use for  loading the template.
</pre>
### Define views to render html
```
def home(request):
    name = "Muhammad Hashim"
    age = 23
    d = {'name':name, 'age':age}
    return render(request, 'index.html', d)
```
### define urlpattern in app level urls.py
```
from django.urls import path
from SimpleApp import views
urlpatterns = [
    path("",views.home, name="home"),
]
```
### finally add url to root project urls.py
```
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include('SimpleApp.urls')),
]
```
### Now its time to render html
```
python manage.py runserver
```
- Here is how to access home page
<pre>
http://127.0.0.1:8000/home/
</pre>

### Create dynamic templates folder inside Application
1. Create templates directory inside application and inside templates create another directory with same application name and inside it create html files, the result should be link this.
<pre>
projectname/
├── projectname/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── myapp/
    |__ templates
    |  |___ home.html
    |  |___ about.html
    |  |___ contact.html
    |  |___ blog.html
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations/
    │   |__ __init__.py
    ├── models.py
    ├── tests.py
    └── views.py
</pre>

### Define views
```
from django.shortcuts import render
def home(request):
    name = "Muhammad Hashim"
    age = 23
    d = {'name':name, 'age':age}
    return render(request, 'SimpleApp/index.html', d)
```

### Define urls in Application level
```
from django.urls import path
from SimpleApp import views
urlpatterns = [
    path("",views.home),
]
```
### Define urls in Project level
```
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include('SimpleApp.urls')),
]
```
### Create html document inside application  templates / folder / index.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- <meta http-equiv="refresh" content="05"> -->
    <title>Div </title>
</head>
<body>
    <article>
        <h2>Google Chrome</h2>
        <p>Google Chrome is a web browser developed by Google, released in 2008. Chrome is the world's most popular web browser today!</p>
    </article>
    <details>
        <summary>Epcot Center</summary>
        <p>Hi,{{name}} How are you? Your age is {{age}}</p>
    </details>
    <p>This is just a simple paragraph</p>
</body>
</html>
```

### Lets explore Django built in filters
1. When we need to modify variable before displaying we can use filters. Pipe symbol | is used to apply filter.
<pre>
Syntax:
      {{variable | filter}}
Some filters takes arguments
Syntax:
      {{variable | filter : argument}}
</pre>

### filters Example
#### Filters list
- add
- addslashes
- capfirst
- date
- dictsort
- filesizeformat
- first
- floatformat
- length
- linenumbers
- escape

1. defines a view
```
from django.shortcuts import render
from django.http import HttpResponse 
from datetime import datetime
multiString ="""One
two
three
four"""
def home(request):
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
    return render(request, 'SimpleApp/index.html', d)
```
2. urls.py in application level
```
from django.urls import path
from SimpleApp import views
urlpatterns = [
    path("",views.home),
]
```
3. urls.py in project level
```
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('SimpleApp.urls')),
]
```
4. rendering document
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- <meta http-equiv="refresh" content="05"> -->
    <title>Built-in Filters</title>
</head>
<body>
<section>
<h2>Google Chrome</h2>
<p>Google Chrome is a web browser developed by Google, released in 2008. Chrome is the world's most popular web browser today!</p>
</section>
<p>Hi,{{name|capfirst}} How are you? Your age is {{age|add:"3"}}</p>
<pre>
First list :{{list1}}

Second list : {{list2}}

The Sum of two list is {{list1|add:list2}}
</pre>
<p>{{django|addslashes}}</p>
<p>"{{dj|center:"15"}}"</p>
<p>{{D|date:"j s l n M Y"}}</p>
<pre>
Without sorted List:
{{list3}} 

With sorted list:
{{list3|dictsort:"name"}}
</pre>
<p>This is just a simple paragraph</p>
<p>if value is {{value}} than the output will be {{value|filesizeformat}} </p>
<p>The {{list1}} list first item is {{list1|first}}</p>
<p>The value {{f}}</p>
<p>The value {{f|floatformat}}</p>
<p>The value {{f|floatformat:"3"}}</p>
<p>My name {{name|capfirst}} contains {{name|length}} letters</p>
<pre>
{{m}}

{{m|linenumbers}}
</pre>
<pre>
Name in Captial letter : {{nick}}

Name in lower letter : {{nick|lower}}
</pre>
<p>Rendered text date: "{{D|date:"l" }}"</p>
{% comment "Optional note" %}
    <p>Commented out text with {{ create_date|date:"c" }}</p>
{% endcomment %}
</pre>
<span style="font-size:30px;">Django Templates tags</span>
<pre>{% autoescape off %}
{{w}}
{{w|escape}}
{% endautoescape %}</pre>
</body>
</html>
```
- #### Note: if you want to  learn more about it please visit https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#built-in-filter-reference

### Built-in template tags
1.  comment
2.  if tag
- if tags with boolean operators
- - and, or, not
- - == operator
- - in operator
- - if tag with filter
3. lorem
<pre>
Displays random “lorem ipsum” Latin text. This is useful for providing sample data in templates.

Usage:
{% lorem [count] [method] [random] %}
The {% lorem %} tag can be used with zero, one, two or three arguments. The arguments are:
Argument	Description
count	A number (or variable) containing the number of paragraphs or words to generate (default is 1).
method	Either w for words, p for HTML paragraphs or b for plain-text paragraph blocks (default is b).
random	The word random, which if given, does not use the common paragraph (“Lorem ipsum dolor sit amet…”) when generating text.
Examples:
{% lorem %} will output the common “lorem ipsum” paragraph.
{% lorem 3 p %} will output the common “lorem ipsum” paragraph and two random paragraphs each wrapped in HTML <p> tags.
{% lorem 2 w random %} will output two random Latin words.
</pre>
4. now
```
It is {% now "jS F Y H:i" %}
```
- The {% if %} tag evaluates a variable, and if that variable is “true” (i.e. exists, is not empty, and is not a false boolean value) the contents of the block are output:
5. For tag
- Syntax
<pre>
{% for itemvariable in variable %}
{{itemvariable}}
{% endfor %}
Example:
<ul>
{% for itemvariable in variable %}
<li>{{itemvariable}}</li>
{% endfor %}
</ul>
</pre>
5. regroup
- regroup¶
Regroups a list of alike objects by a common attribute.
- This complex tag is best illustrated by way of an example: say that cities is a list of cities represented by dictionaries containing "name", "population", and "country" keys
<pre>
cities = [
    {"name": "Mumbai", "population": "19,000,000", "country": "India"},
    {"name": "Calcutta", "population": "15,000,000", "country": "India"},
    {"name": "New York", "population": "20,000,000", "country": "USA"},
    {"name": "Chicago", "population": "7,000,000", "country": "USA"},
    {"name": "Tokyo", "population": "33,000,000", "country": "Japan"},
]
and you’d like to display a hierarchical list that is ordered by country, like this:
. India
  . Mumbai: 19,000,000
  . Calcutta: 15,000,000
. USA
  . New York: 20,000,000
  . Chicago: 7,000,000
. Japan
  . Tokyo: 33,000,000
You can use the {% regroup %} tag to group the list of cities by country. The following snippet of template code would accomplish this:
</pre>
6. cycle
- Produces one of its arguments each time this tag is encountered. The first argument is produced on the first encounter, the second argument on the second encounter, and so forth. Once all arguments are exhausted, the tag cycles to the first argument and produces it again.


1. Views
```
from django.shortcuts import render
from django.http import HttpResponse 
from datetime import datetime
multiString ="""One
two
three
four"""
def home(request):
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
    list4 = ["Hashim","Juniad","Usman","Zahid"]
    cities = [
    {"name": "Mumbai", "population": "19,000,000", "country": "India"},
    {"name": "Calcutta", "population": "15,000,000", "country": "India"},
    {"name": "New York", "population": "20,000,000", "country": "USA"},
    {"name": "Chicago", "population": "7,000,000", "country": "USA"},
    {"name": "Tokyo", "population": "33,000,000", "country": "Japan"}]
    coach_list = [
        {
            'name': 'junaid',
            'athletes': [
                {'name': 'Hassan'},
                {'name': 'Hamza'},
                {'name': 'Zubair'},
            ]
        },
        {
            'name': 'Jamshed',
            'athletes': [
                {'name': 'Ehtisham'},
                {'name': 'Ahsan'},
                {'name': 'Zeeshan'},
            ]
        },
    ]
    d = {'name':name, 'age':age, 'list1':list1, 'list2':list2, 'django':django, 'dj':dj, 'D':D,'list3':list3,'value':value, 'f':f, "m":multiString, 'nick':nick, 'messages': messages , 'w':welcome, 'nl':list4, 'cities':cities,'c':coach_list}
    return render(request, 'SimpleApp/index.html', d))
```
2. urls.py in application level
```
from django.urls import path
from SimpleApp import views
urlpatterns = [
    path("",views.home),
]
```
3. urls.py in project level
```
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('SimpleApp.urls')),
]
```
4. rendering document
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- <meta http-equiv="refresh" content="05"> -->
    <title>Built-in Filters</title>
</head>
<body>
<p>Rendered text date: "{{D|date:"l" }}"</p>
{% comment "Optional note" %}
    <p>Commented out text with {{ create_date|date:"c" }}</p>
{% endcomment %}
</pre>
{% comment %} if Tag {% endcomment %}
<pre>{% if name %}
Number is: {{ name|capfirst }}
{% endif %}
</pre>
<pre>{% if n %}Number is: {{ name|capfirst }}
{% else %}no name available{% endif %}
</pre>
{% comment %} If tag with and operator {% endcomment %}
<pre>
{% if name and age  %}
Your Name is {{name}} and Age is {{age}}
{% else %}
No name and age available
{% endif %}
</pre>
{% comment %} if tag with == operator {% endcomment %}
<pre>
{% if age == 23 %}
Your age is  {{age}}
{% else %}
try again
{% endif %}
</pre>
{% comment %} if tag with == "string" {% endcomment %}
<pre>
{% if name == "muhammad Hashim" %}
Your name is : {{name}}
{% endif %}
</pre>
{% comment %} if tag with in operator {% endcomment %}
<pre>
{% if "Dj" in "Django" %}
true it is present
{% endif %}
</pre>
{% comment %} if tag with filter {% endcomment %}
<pre>
{% if name|length >= 14 %}
You have lots of messages today!
 {% endif %}
</pre>
{% comment %}  if tag with random text {% endcomment %}
<p>
{% lorem 50 w random %}
</p>
<p>
    It is {% now "jS F Y H:i" %}
</p>
{% comment %} for loop {% endcomment %}
{% for n in name %}
<li>{{n}}</li>
{% endfor %}
{% comment %} regroup tag {% endcomment %}
{% regroup cities by country as country_list %}
<ul>
{% for country in country_list %}
    <li>{{ country.grouper }}
    <ul>
        {% for city in country.list %}
          <li>{{ city.name }}: {{ city.population }}</li>
        {% endfor %}
    </ul>
    </li>
{% endfor %}
</ul>
{% comment %} cycle tag {% endcomment %}
{% for o in list1 %}
    <tr class="{% cycle 'row1' 'row2' %}">
        ...
    </tr>
{% endfor %}
{% comment %} resetcycle tag {% endcomment %}
{% for coach in c %}
    <h1>{{ coach.name }}</h1>
    {% for athlete in coach.athletes%}
        <p class="{% cycle 'odd' 'even' %}">{{ athlete.name }}</p>
    {% endfor %}
    {% resetcycle %}
{% endfor %}
</body>
</html>
```
=======

>>>>>>> main
