from rest_framework import viewsets
from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
