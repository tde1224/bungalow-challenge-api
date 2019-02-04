from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status
from django_filters import rest_framework as filters

from .decorators import validate_request_data
from .models import Data
from .serializer import DataSerializer
from .filters import DataFilter

class DataList(generics.ListAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DataFilter

    @validate_request_data
    def post(self, request, *args, **kwargs):
        datum = Data.objects.create(
            address=request.data["address"],
            city=request.data["city"],
            state=request.data["state"],
            zipcode=request.data["zipcode"]
        )
        return Response(
            data=DataSerializer(datum).data,
            status=status.HTTP_201_CREATED
        )