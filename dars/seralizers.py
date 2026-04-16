
from rest_framework.serializers import ModelSerializer
from .models import Telefon, Noutbook, TV


class TelefonSeralizer(ModelSerializer):

    class Meta:
        model = Telefon
        fields = "__all__"

class NoutbookSeralizer(ModelSerializer):


    class Meta:
        model = Noutbook
        fields = "__all__"

class TVSeralizer(ModelSerializer):

    class Meta:
        model = TV
        fields = "__all__"