from rest_framework import generics
from .models import ScriptRequest, GeneratedScript
from .serializers import ScriptRequestSerializer
from ai_logic.script_generator import generate_code
# from ai_logic.execute_script import execute_code

class ScriptRequestCreateView(generics.CreateAPIView):
    queryset = ScriptRequest.objects.all()
    serializer_class = ScriptRequestSerializer
    authentication_classes = []  # Disable authentication
    permission_classes = []      # Disable permission checks

    def create(self, request, *args, **kwargs):
        print(request.headers.get('Authorization'))
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        script_request = serializer.save(user=self.request.user if self.request.user.is_authenticated else None)
        
        generated_code = generate_code(script_request)
        
        # Create a GeneratedScript instance
        GeneratedScript.objects.create(
            script_request=script_request,
            code=generated_code,
            language="python",
        )
        
        # Optionally execute the generated code in a secure environment
        # output = execute_code(generated_code)
