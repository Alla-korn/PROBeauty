from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from main_app.apps import MainAppConfig
from main_app.views import get_main_page

app_name = MainAppConfig.name
urlpatterns = [
                  path('', get_main_page, name='main_page'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
