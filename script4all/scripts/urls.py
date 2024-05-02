from django.urls import path
from .views import ScriptRequestCreateView, ScriptRequestDeleteView, ScriptRequestDetailView

urlpatterns = [
    path('script-requests/', ScriptRequestCreateView.as_view(), name='script-request-create'),
    path('<int:pk>/', ScriptRequestDeleteView.as_view(), name='script-request-delete'),
    path('script-requests/<int:pk>/', ScriptRequestDetailView.as_view(), name='script-request-detail')
    # Add other script-related URLs if needed
]