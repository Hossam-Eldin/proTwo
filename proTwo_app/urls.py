from django.conf.urls import url
from proTwo_app import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
]
