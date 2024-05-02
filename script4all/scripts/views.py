from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import ScriptRequest, GeneratedScript
from .serializers import ScriptRequestSerializer, GeneratedScriptSerializer
from ai_logic.script_generator import generate_code
# from ai_logic.execute_script import execute_code

class ScriptRequestCreateView(generics.CreateAPIView):
    queryset = ScriptRequest.objects.all()
    serializer_class = ScriptRequestSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        script_request = self.perform_create(serializer)

        generated_code = generate_code(script_request)
        generated_script = GeneratedScript.objects.create(
            script_request=script_request,
            code=generated_code,
            language="python",
            user=self.request.user,
        )

        generated_script_serializer = GeneratedScriptSerializer(generated_script)
        response_data = {
            'script_request': serializer.data,
            'generated_script': generated_script_serializer.data,
        }
        headers = self.get_success_headers(serializer.data)
        return Response(response_data, status=201, headers=headers)

    def perform_create(self, serializer):
        script_request = serializer.save(user=self.request.user)
        return script_request
    
class ScriptRequestDeleteView(generics.DestroyAPIView):
    queryset = ScriptRequest.objects.all()
    serializer_class = ScriptRequestSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user

        # Verify user owns the script request
        if instance.user != user:
            return Response({'detail': 'You do not have permission to delete this script request.'},
                            status=403)

        # Since deletion of ScriptRequest cascades to GeneratedScript, no need for additional delete calls
        self.perform_destroy(instance)
        return Response({'detail': 'Script request and associated generated script deleted'},
                        status=204)

class ScriptRequestDetailView(generics.RetrieveUpdateAPIView):
    queryset = ScriptRequest.objects.all()
    serializer_class = ScriptRequestSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **pk):
        script_request = self.get_object()
        generated_script = GeneratedScript.objects.filter(script_request=script_request).first()

        script_request_serializer = ScriptRequestSerializer(script_request)
        generated_script_serializer = GeneratedScriptSerializer(generated_script) if generated_script else None

        response_data = {
            'script_request': script_request_serializer.data,
            'generated_script': generated_script_serializer.data if generated_script_serializer else {}
        }

        return Response(response_data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # After updating the script request, regenerate the code
        generated_script = GeneratedScript.objects.filter(script_request=instance).first()
        if generated_script:
            # You might want to pass new parameters or modify how generate_code is called based on updated script request
            new_code = generate_code(instance)
            print(new_code)
            generated_script.code = new_code
            generated_script.save()

            generated_script_serializer = GeneratedScriptSerializer(generated_script)
            response_data = {
                'script_request': serializer.data,
                'generated_script': generated_script_serializer.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            # Handle case where there is no generated script
            return Response({'detail': 'Generated script not found'}, status=status.HTTP_404_NOT_FOUND)
