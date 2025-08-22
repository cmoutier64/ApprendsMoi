from django.contrib import admin
from django.urls import path
from core import views
urlpatterns = [
 path('admin/', admin.site.urls),
 path('', views.index),
 path('pricing/', views.pricing),
 path('meeting/', views.meeting),
 path('calendar/', views.calendar_view),
 path('calendar/feed', views.calendar_feed),
]
