from django.conf.urls import url

from . import views

app_name = 'models_practice'
urlpatterns = [
    url(r'^$', views.models_practice, name='practice'),
    url(r'^new$', views.new_person, name='new_person'),
    url(r'^update$', views.update_person, name='update_person'),

]