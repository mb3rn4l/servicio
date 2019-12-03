from django.conf.urls import url

from .api_views import ListCreatePerson, RetrieveDestroyPerson, Geocoder
from .views import ProcessFile

urlpatterns = (
    url(r'^v1/person/$', ListCreatePerson.as_view(), name='ListCreatePerson'),
    url(r'^v1/person/(?P<pk>[0-9]+)$', RetrieveDestroyPerson.as_view(), name='RetrieveDestroyPerson'),
    url(r'^v1/geocodificar_base$', Geocoder.as_view(), name='Geocoder'),
    url(r'^file/$', ProcessFile.as_view(), name='ProcessFile')
)
