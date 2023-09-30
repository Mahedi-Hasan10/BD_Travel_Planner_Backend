from .models import Hotel
from .serializers import HotelSerializer
from rest_framework import viewsets

class HotelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
