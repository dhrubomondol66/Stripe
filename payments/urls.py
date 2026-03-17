from django.urls import path
from .views import CreatePaymentView
from .webhook import stripe_webhook

urlpatterns = [
    path("create-payment/",CreatePaymentView.as_view()),
    path("webhook/",stripe_webhook)
]