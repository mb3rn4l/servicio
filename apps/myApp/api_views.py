import os
import requests

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django_filters import rest_framework as filters

from .models import Person
from .serializers import PersonSerializer
from .filters import PersonFilter


class ListCreatePerson(generics.ListCreateAPIView):
    """
    POST = Permite la creacion de personas
    GET = Lista todas las personas.
    """

    def get_queryset(self):
        return Person.objects.all().order_by('-id')

    serializer_class = PersonSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = PersonFilter


class RetrieveDestroyPerson(generics.RetrieveDestroyAPIView):
    """
    GET = Obtiene el detalle de una persona de acuerdo a su id
    DELETE = Elimina una persona de acuerdo a su id
    """
    def get_queryset(self):
        return Person.objects.all().order_by('-id')

    serializer_class = PersonSerializer
    permission_classes = [AllowAny]


class Geocoder(APIView):
    """
    GET = Realiza la geolocalizacion de las direcciones de los usuarios que no las tengan.
    """
    STATUS_OK = 'OK'

    def get(self, request):
        people = Person.objects.filter(latitud=None, longitud=None)
        counter = 0
        for person in people:
            try:
                api_key_google = os.environ.get('API_KEY_GOOGLE')
                url = os.environ.get('API_URL_GOOGLE')
                url = "{}?key={}&address={}".format(url, api_key_google, person.address)
                response = requests.get(url=url)

                if response.status_code in [200, 201]:
                    data_response = response.json()
                    if data_response['status'] == self.STATUS_OK:
                        person.latitud = data_response['results'][0]['geometry']['location']['lat']
                        person.longitud = data_response['results'][0]['geometry']['location']['lat']
                        person.estate_geo = 'A'
                        person.save()
                        counter = counter + 1
            except Exception as e:
                print('Ocurrio un problema {}'.format(str(e)))
                person.latitud = 0
                person.longitud = 0
                person.save()

        return Response({'message': 'actualizados {} de {} usuarios'.format(counter, people.count())},
                        status=status.HTTP_200_OK)

    permission_classes = [AllowAny]
