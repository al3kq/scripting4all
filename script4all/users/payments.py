import stripe
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from django.shortcuts import redirect
from django.views import View
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import User

stripe.api_key = settings.STRIPE_SECRET_KEY

@method_decorator(csrf_exempt, name='dispatch')
class SubscribeView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        print("USER:", user)
        # user_stripe_id = User.objects.get(stripe_customer_id=customer_id)

        if not user.stripe_customer_id:
            try:
                customer = stripe.Customer.create(name=user.username, email=user.email)
                user.stripe_customer_id = customer.id
                user.save()
            except Exception as e:
                print(e)
                return JsonResponse({'error': str(e)}, status=400)

        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price': 'price_1PBrchETTXwHh2RA2RPp0uzT',  # You should replace this with your actual price ID
                    'quantity': 1,
                }],
                mode='subscription',
                success_url='http://localhost:3000/success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url='http://localhost:3000/cancel',
                customer=user.stripe_customer_id,
            )
            print(checkout_session.id)
            return JsonResponse({'sessionId': checkout_session.id})
        except Exception as e:
            print(e)
            return JsonResponse({'error': str(e)}, status=400)
        

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        customer_id = session['customer']
        subscription_id = session['subscription']
        print(customer_id)
        print(session)

        user = User.objects.get(stripe_customer_id=customer_id)
        user.stripe_subscription_id = subscription_id
        user.stripe_subscription_status = 'active'
        print("here!")
        user.save()

    if event['type'] == 'customer.subscription.deleted':
        subscription_id = event['data']['object']['id']
        user = User.objects.get(stripe_subscription_id=subscription_id)
        user.stripe_subscription_status = 'inactive'
        user.save()

    return HttpResponse(status=200)

@csrf_exempt
def create_checkout_session(request):
    # payment_link_url = 'https://buy.stripe.com/test_7sI3ey9W5enG556144'
    # return HttpResponseRedirect(payment_link_url)
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': 'price_1PBrchETTXwHh2RA2RPp0uzT',  # You should replace this with your actual price ID
                'quantity': 1,
            }],
            mode='subscription',
            success_url='http://localhost:3000/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url='http://localhost:3000/cancel',
        )
        return JsonResponse({'sessionId': checkout_session.id})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)