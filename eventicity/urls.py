from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('category/', include('categories.urls')),
    path('participant/', include('participants.urls'))
] + debug_toolbar_urls()
