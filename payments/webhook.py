import stripe
from django.conf import settings
from django.http import HttpResponse
from .models import Payment


stripe.api_key = settings.STRIPE_SECRET_KEY


def stripe_webhook(request):

    payload = request.body
    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]

    event = stripe.Webhook.construct_event(
        payload,
        sig_header,
        settings.STRIPE_WEBHOOK_SECRET
    )

    if event["type"] == "payment_intent.succeeded":

        intent = event["data"]["object"]
        payment_id = intent["metadata"]["payment_id"]

        payment = Payment.objects.get(id=payment_id)
        payment.status = "success"
        payment.save()

    return HttpResponse(status=200)