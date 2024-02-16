from django.urls import path
from home.views import home, about, portfolio

urlpatterns = [
    path('', home),
    path('sobre/', about),
    path('portfolio/', portfolio),
]
