from django.urls import path, include
from rest_framework import routers

from .views import ActorView, DirectorView, MovieView

router = routers.DefaultRouter()
router.register('actors', ActorView)
router.register('directors', DirectorView)
router.register('movies', MovieView)



urlpatterns = [
    path('', include(router.urls))
]