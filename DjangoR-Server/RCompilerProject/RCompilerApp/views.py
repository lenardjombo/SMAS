
import os
import subprocess
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('compile_code')  # Redirect to coding platform
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('compile_code')  # Redirect to coding platform
    else:
        form = CustomAuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('login')

@login_required
@csrf_exempt
def compile_code(request):
    output = ''
    error = ''
    code = ''
    plot_url = ''

    if request.method == 'POST':
        code = request.POST.get('code', '')

        # Validate code input
        if not code:
            error = 'No code provided.'
            return render(request, 'index.html', {'output': output, 'error': error, 'code': code, 'plot_url': plot_url})

        # Write code to a temporary file
        temp_code_path = 'temp_code.R'
        with open(temp_code_path, 'w') as file:
            file.write(code)

        # Define plot path
        plot_dir = os.path.join(settings.BASE_DIR, 'static', 'plots')
        os.makedirs(plot_dir, exist_ok=True)
        plot_path = os.path.join(plot_dir, 'plot.png')

        # Prepare R script
        r_script = f"""
        png('{plot_path}', width=700, height=500)
        {code}
        dev.off()
        """
        
        with open(temp_code_path, 'w') as file:
            file.write(r_script)

        # Execute R script
        try:
            result = subprocess.run(['Rscript', temp_code_path], capture_output=True, text=True, timeout=10)
            output = result.stdout
            error = result.stderr

            # Check if plot file was created
            if os.path.exists(plot_path):
                plot_url = 'plots/plot.png'
            else:
                plot_url = ''

        except subprocess.TimeoutExpired:
            error = "Code execution timed out."
        except Exception as e:
            error = f"An error occurred: {str(e)}"
        finally:
            # Clean up temporary files
            if os.path.exists(temp_code_path):
                os.remove(temp_code_path)

    return render(request, 'index.html', {'output': output, 'error': error, 'code': code, 'plot_url': plot_url})
