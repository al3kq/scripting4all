# scripts/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

def user_directory_path(instance, filename):
    return f'script4all/temp_input/{instance.user.id}/{filename}'

class ScriptRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='script_requests', null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    description_file = models.FileField(upload_to=user_directory_path, default='', blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class GeneratedScript(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='generate_script', null=True)
    script_request = models.OneToOneField(ScriptRequest, on_delete=models.CASCADE, related_name='generated_script')
    code = models.TextField()
    language = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Generated Script for {self.script_request.title}"