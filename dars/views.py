from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .seralizers import TelefonSeralizer, NoutbookSeralizer, TVSeralizer
from .models import Telefon, Noutbook, TV


# Create your views here.


class TelefonListCreateApiView(ListCreateAPIView):
    queryset = Telefon.objects.all()
    serializer_class = TelefonSeralizer

class TelefonDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Telefon.objects.all()
    serializer_class = TelefonSeralizer


class NoutbookListCreateApiView(ListCreateAPIView):
    queryset = Noutbook.objects.all()
    serializer_class = NoutbookSeralizer

class NoutbookDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Noutbook.objects.all()
    serializer_class = NoutbookSeralizer


class TVListCreatApiViews(ListCreateAPIView):
    queryset = TV.objects.all()
    serializer_class = TVSeralizer

class TVDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = TV.objects.all()
    serializer_class = TVSeralizer