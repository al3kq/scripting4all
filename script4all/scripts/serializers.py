from rest_framework import serializers
from .models import ScriptRequest, GeneratedScript

class ScriptRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScriptRequest
        fields = ('id', 'user', 'title', 'description', 'status', 'created_at', 'updated_at')
        read_only_fields = ('user', 'status', 'created_at', 'updated_at')

class GeneratedScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneratedScript
        fields = ('id', 'script_request', 'code', 'language', 'created_at')
        read_only_fields = ('created_at',)