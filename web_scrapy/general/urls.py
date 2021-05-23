from django.conf.urls import include, url
from rest_framework import routers
from general.views import ScrapyView, FileView, earthquakes_view
from rest_framework.routers import DefaultRouter
# from importlib.resources import path
from django.urls import path

# router = DefaultRouter()
# router.register(r'search', ScrapyView, basename='search')
# urlpatterns = router.urls

urlpatterns = [
    path('search/', ScrapyView.as_view()),
    path('file/', FileView.as_view()),
    path('details', earthquakes_view ),
    
]
