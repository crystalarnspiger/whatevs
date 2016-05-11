from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.models_practice, name='models_practice'),
]