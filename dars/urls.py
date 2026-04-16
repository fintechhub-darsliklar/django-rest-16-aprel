from django.urls import path
from .views import TelefonListCreateApiView,TelefonDetailApiView, NoutbookDetailApiView, NoutbookListCreateApiView, \
    TVListCreatApiViews, TVDetailApiView



urlpatterns = [
    path('telefon/', TelefonListCreateApiView.as_view()),
    path('telefon/<int:pk>/', TelefonDetailApiView.as_view()),
    path('noutbook/', NoutbookListCreateApiView.as_view()),
    path('noutbook/<int:pk>/',NoutbookDetailApiView.as_view()),
    path('tv/', TVListCreatApiViews.as_view()),
    path('tv/<int:pk>/',TVDetailApiView.as_view())

]