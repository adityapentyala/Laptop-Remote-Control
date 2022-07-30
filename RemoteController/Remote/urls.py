from django.urls import path

from . import views

urlpatterns = [
    path('', views.remote),
    path('play_pause', views.play_pause),
    path('next_track', views.next_track),
    path('prev_track', views.prev_track),
    path('vol_up', views.vol_up),
    path('vol_down', views.vol_down),
    path('mute', views.mute),
    path('toggle_fullscreen', views.toggle_fullscreen),
    path('toggle_caption', views.toggle_caption),
    path('space', views.space),
    path('up', views.up),
    path('down', views.down),
    path('left', views.left),
    path('right', views.right),
]