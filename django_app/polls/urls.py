from django.conf.urls import url

from . import views

# from . ~ 은 from polls import views와 같은 의미

urlpatterns = [
    url(r'^$', views.index, name='index')
]
