from rest_framework import serializers
from .models import ScriptRequest, GeneratedScript

class GeneratedScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneratedScript
        fields = ('id', 'user', 'code', 'language', 'created_at')
        read_only_fields = ('id', 'user', 'created_at')

class ScriptRequestSerializer(serializers.ModelSerializer):
    generated_script = GeneratedScriptSerializer(read_only=True)

    class Meta:
        model = ScriptRequest
        fields = ('id', 'user', 'title', 'description', 'status', 'created_at', 'updated_at', 'generated_script')
        read_only_fields = ('user', 'status', 'created_at', 'updated_at', 'generated_script')