from django.conf.urls import url
from django.contrib import admin

from app_mail.views import index

urlpatterns = [
    url(r'^index/', index),
    url(r'^$', index),
    url(r'^admin/', admin.site.urls),
]
