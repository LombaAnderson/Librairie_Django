from django.db.models import fields
from rest_framework import serializers
from livres.models import Livres


class LivresSerializers(serializers.ModelSerializer):
    class Meta:
        model = Livres
        fields = "__all__"
