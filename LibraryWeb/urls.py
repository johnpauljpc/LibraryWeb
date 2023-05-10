from django.conf import settings
from django.conf.urls.static import static



from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')),
    path('', RedirectView.as_view(url = 'catalog/', permanent = True)), #Redirecting to catalog route

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
