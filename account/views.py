# account/views.py
from rest_framework import viewsets,status,filters
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from user_auth.models import CustomUser
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']

    def get_queryset(self):
        return CustomUser.objects.filter(is_active=True)

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

    def create(self, request, *args, **kwargs):
        return Response({"detail": "Method 'POST' not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)