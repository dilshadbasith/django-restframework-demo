from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from api.models import Todo
from api.serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by('-id')
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)