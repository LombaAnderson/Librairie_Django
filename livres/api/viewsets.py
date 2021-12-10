from rest_framework import viewsets
from livres.api.serializers import LivresSerializers
from livres.models import Livres


class LivresViewSet(viewsets.ModelViewSet):
    serializer_class = LivresSerializers
    queryset = Livres.objects.all()
