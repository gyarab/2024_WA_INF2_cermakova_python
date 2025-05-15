
from django.contrib import admin
from django.urls import path
import content.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', content.views.homepage),
    path('book/<int:id>/', content.views.book),
    path('author/<int:id>/', content.views.author),
    path('genre/<int:id>/', content.views.genre),
]
