from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^myApp/api/', include('apps.myApp.urls', namespace="myApp", app_name="myApp")),
]
