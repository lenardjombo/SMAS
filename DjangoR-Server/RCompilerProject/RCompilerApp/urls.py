from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView
from django.contrib.auth.views import LoginView, LogoutView
from RCompilerApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/accounts/login/')),  # Redirect root URL to login
    path('accounts/login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='/accounts/login/'), name='logout'),
    path('accounts/register/', views.register, name='register'),
    path('compile/', views.compile_code, name='compile_code'),  # Updated path to avoid conflicts
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


