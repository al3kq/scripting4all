from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLogoutView, UserProfileView, UserDashboardView
from .payments import SubscribeView, stripe_webhook, create_checkout_session

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
    path('stripe-webhook/', stripe_webhook, name='stripe_webhook'),
    path('create-checkout-session/', create_checkout_session, name='create-checkout-session'),
    path('dashboard/', UserDashboardView.as_view(), name='user-dashboard'),
]