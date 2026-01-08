from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.newspage),
    path('news/', include('news.urls')),
    path('accounts/', include('accounts.urls')),
    path('tracker/', include(('tracker.urls', 'tracker'), namespace='tracker')),  # <-- add namespace
    path('membership/', include('membership.urls')),
]
