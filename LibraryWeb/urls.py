from django.conf import settings
from django.conf.urls.static import static
import django.contrib.auth.urls as djangoAuth
import  django.contrib.auth.views as auth



from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url = 'catalog/', permanent = True)), #Redirecting to catalog route
    #Django urls for authentication
    # path('accounts/', include(djangoAuth)),
    path('login/', auth.LoginView.as_view(template_name="auth/login.html"), name='login'),
    path('logout/', auth.LogoutView.as_view(template_name="auth/logout.html"), name='logout'),
    path('reset-password/', auth.PasswordResetView.as_view(template_name="auth/password/password-reset.html"), name="password_reset"),
    path('reset-password-done/', auth.PasswordResetDoneView.as_view(template_name="auth/password/password-reset-done.html"), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', auth.PasswordResetConfirmView.as_view(template_name = 'auth/password/password_reset_confirm.html'), name="password_reset_confirm"),
    path('password-reset-complete/', auth.PasswordResetCompleteView.as_view(template_name='auth/password/password-reset-complete.html'), name='password_reset_complete'),
    

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
