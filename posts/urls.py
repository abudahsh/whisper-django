from django.urls import path

from posts.views import HomePage

app_name='posts'

urlpatterns=[
    path('', HomePage.as_view(), name='home'),
]