from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .services import PaymentService


class CreatePaymentView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self,request):

        amount = request.data.get("amount")

        client_secret = PaymentService.create_payment(
            request.user,
            amount
        )

        return Response({
            "client_secret":client_secret
        })