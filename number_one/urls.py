from django.conf.urls import url

from . import views

app_name = 'models_practice'
urlpatterns = [
    url(r'^$', views.models_practice, name='practice'),
    url(r'^new$', views.new_person, name='new_person'),
    url(r'^update_form(?P<id>\w+)/$', views.enter_update, name='enter_update'),
    url(r'^save_update$', views.save_update, name='save_update'),

]