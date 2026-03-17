import stripe
from django.conf import settings
from .models import Payment

stripe.api_key = settings.STRIPE_SECRET_KEY


class PaymentService:

    @staticmethod
    def create_payment(user, amount):
        """
        Create a payment record in DB and a Stripe PaymentIntent.
        """
        # 1️⃣ Create payment record in DB
        payment = Payment.objects.create(
            user=user,
            amount=amount,
            status="pending"
        )

        # 2️⃣ Create Stripe PaymentIntent
        intent = stripe.PaymentIntent.create(
            amount=int(amount * 100),
            currency="usd",
            metadata={"payment_id": payment.id},
            automatic_payment_methods={"enabled": True},
        )

        # 3️⃣ Save Stripe PaymentIntent ID
        payment.stripe_payment_intent = intent["id"]
        payment.save()

        # 4️⃣ Return client_secret
        return intent.client_secret