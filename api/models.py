from django.db import models
from user_auth.models import CustomUser
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='todos',default=1) 
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    
    def __str__(self):
        return self.title
