from rest_framework import viewsets

from credit.models import Credit
from credit.serializers import CreditSerializer


class CreditViewSet(viewsets.ModelViewSet):
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer

    # filtrar por nombre y created_at 
    def get_queryset(self):
        queryset = Credit.objects.all()
        nombre = self.request.query_params.get('nombre', None)
        created_at = self.request.query_params.get('created_at', None)
        if nombre is not None:
            queryset = queryset.filter(nombre__startswith=nombre)
        if created_at is not None:
            queryset = queryset.filter(created_at=created_at)
        return queryset