from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import ScriptRequest
from .serializers import ScriptRequestSerializer

class ScriptRequestCreateView(generics.CreateAPIView):
    queryset = ScriptRequest.objects.all()
    serializer_class = ScriptRequestSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)