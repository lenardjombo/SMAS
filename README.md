<h1 id="title" align="center">SMAS</h1>

<p id="description">SMAS is a web-application created with django.The main purpose for its creation is to help students in the field of StatisticsMathematics and Actuarial science learn and code in R programming language without the need of personal computers. SMAS is mainly targeted for students who do not have access to personal computers and anyone wishing to code on their smartphone due to mobility and portability of smartphones.</p>

<h2>Project Screenshots:</h2>

<img src="https://github.com/user-attachments/assets/91b546a4-fff9-460a-92cb-977e1ac974b8" alt="Screen Shot 2024-07-19 at 18 44 53" width="900" height="700">


![Screen Shot 2024-07-19 at 18 44 40](https://github.com/user-attachments/assets/8142a624-8fd4-40fd-9695-ddab25f87f2a)

  
  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   Intuitive Code-editor
*   Responsiveness
*   Data Visualization
*   R-Documentation
*   Student-Registration
*   Admin-Site
*   Logging in and Authentication

<h2>🛠️ Installation Steps:</h2>

<p>1. Create and Configure Django Project If you haven’t already create a Django project:</p>

```
django-admin startproject RCompilerProject
```

<p>2. Navigate to your project directory:</p>

```
cd RCompilerProject
```

<p>3. Create Django App Create an app for handling your R compiler logic:</p>

```
python manage.py startapp RCompilerApp
```

<p>4. Add App to settings.py In RCompilerProject/settings.py add RCompilerApp to the INSTALLED_APPS list:</p>

```
INSTALLED_APPS = [     ...     'RCompilerApp' ]
```

<p>5. Configure R Compiler Install R on Server Ensure R is installed on the server where you will run the Django application. On Unix-based systems you can typically install R using a package manager:</p>

```
sudo apt-get install r-base
```

<p>6. Create a Script to Run R Code Write a script to execute R code and return the result. You can create a Python function in Django that uses subprocess to call R and return the output. Example script (r_script.py):</p>

```
import subprocess  def run_r_code(r_code):     try:         result = subprocess.run(['Rscript' '-e' r_code] capture_output=True text=True)         return result.stdout result.stderr     except Exception as e:         return str(e) ''
```

<p>7. Create Django Views and Forms Create a Form for R Code Submission In RCompilerApp/forms.py:</p>

```
from django import forms  class RCodeForm(forms.Form):     r_code = forms.CharField(widget=forms.Textarea label='Enter R Code')
```

<p>8. Create a View to Handle Form Submission In RCompilerApp/views.py:</p>

```
from django.shortcuts import render from .forms import RCodeForm from .r_script import run_r_code  def compile_r_code(request):     output = ''     error = ''     if request.method == 'POST':         form = RCodeForm(request.POST)         if form.is_valid():             r_code = form.cleaned_data['r_code']             output error = run_r_code(r_code)     else:         form = RCodeForm()          return render(request 'RCompilerApp/compiler.html' {'form': form 'output': output 'error': error})
```

<p>9. Create a Template for the Form In RCompilerApp/templates/RCompilerApp/compiler.html:</p>

```
      R Online Compiler              {% csrf_token %}         {{ form.as_p }}         Run Code          Output     {{ output }}     Error     {{ error }}  
```

<p>10. Set Up URL Routing Configure URLs in RCompilerApp/urls.py</p>

```
from django.urls import path from . import views  urlpatterns = [     path('' views.compile_r_code name='compile_r_code') ]
```

<p>11. Include App URLs in Project URLs In RCompilerProject/urls.py:</p>

```
from django.contrib import admin from django.urls import include path  urlpatterns = [     path('admin/' admin.site.urls)     path('compiler/' include('RCompilerApp.urls')) ]
```

<p>12. Deploy Your Django Application Prepare for Deployment</p>

```
Configure your settings.py for production (e.g. set DEBUG = False and configure allowed hosts). Set up a production-ready database and configure it in settings.py.
```

<p>13. Deploy to a Hosting Service</p>

```
Follow the deployment instructions for your chosen hosting service (Heroku Railway Render etc.). You will need to ensure that R is installed and accessible on the server.
```

<p>14. Test the Deployment</p>

```
Ensure your deployment environment is correctly configured to run both Django and R. Test your application thoroughly to confirm everything works as expected.
```

  
  
<h2>💻 Built with</h2>

Technologies used in the project:

*   Django
*   Python
*   sqlite
*   javascript
*   html5
*   css3
*   MDBootstrap

<h2>🛡️ License:</h2>

This project is licensed under the MIT
