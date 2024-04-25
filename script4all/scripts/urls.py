from django.urls import path
from .views import ScriptRequestCreateView

urlpatterns = [
    path('script-requests/', ScriptRequestCreateView.as_view(), name='script-request-create'),
    # Add other script-related URLs if needed
]