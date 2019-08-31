from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from parsi_api import views
from parsi_api.models import Poets

try:
    admin.site.register(Poets)
except admin.sites.AlreadyRegistered:
    pass

urlpatterns = [
    url(r'^poets$', views.get_poets.as_view()),
    path(r'poem/<int:count>', views.get_poem.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'.*', views.github),
]
