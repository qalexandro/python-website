from django.contrib import admin
from django.urls import path, include
from .views import HomeView, HelpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name = "main_home"),
    path('blog/', include('blog.urls', namespace = 'blog')),
    path('help/', HelpView.as_view(), name = "help"),
]
