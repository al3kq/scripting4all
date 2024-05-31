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
        fields = ('id', 'user', 'title', 'description', 'description_file', 'status', 'created_at', 'updated_at', 'generated_script')
        read_only_fields = ('user', 'status', 'created_at', 'generated_script')
    def validate_description_file(self, value):
        if value.content_type not in ['application/pdf', 'image/jpeg']:
            raise serializers.ValidationError("Only PDF and JPEG files are allowed.")
        return value