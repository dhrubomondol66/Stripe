# Django Stripe Payment Gateway

A Django REST API payment gateway integrated with Stripe for processing payments securely.

## Features

- ✅ User registration and authentication with JWT tokens
- ✅ Stripe payment integration
- ✅ Payment intent creation
- ✅ Webhook handling for payment status updates
- ✅ RESTful API with Swagger documentation
- ✅ Secure environment variable configuration

## Prerequisites

- Python 3.8+
- Django 4.2+
- Stripe account and API keys

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/dhrubomondol66/Stripe.git
cd Stripe/gateway
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

Create a `.env` file in the project root:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True

# Stripe API Keys
STRIPE_SECRET_KEY=sk_test_your-stripe-secret-key
STRIPE_PUBLISHABLE_KEY=pk_test_your-stripe-publishable-key
STRIPE_WEBHOOK_SECRET=whsec_your-webhook-secret
```

**Get your Stripe keys from the [Stripe Dashboard](https://dashboard.stripe.com/apikeys)**

### 5. Database Setup

```bash
# Apply migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000`

## API Endpoints

### Authentication

#### Register User
```http
POST /api/auth/register/
Content-Type: application/json

{
    "username": "testuser",
    "email": "test@example.com",
    "password": "yourpassword"
}
```

**Response:**
```json
{
    "user": {
        "id": 1,
        "username": "testuser",
        "email": "test@example.com"
    },
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

#### Login (Get Token)
```http
POST /api/auth/token/
Content-Type: application/json

{
    "email": "test@example.com",
    "password": "yourpassword"
}
```

### Payments

#### Create Payment Intent
```http
POST /api/payment/create-payment/
Authorization: Bearer <access-token>
Content-Type: application/json

{
    "amount": 10.50
}
```

**Response:**
```json
{
    "client_secret": "pi_1234567890_secret_abcdef..."
}
```

## Documentation

### Swagger UI
Visit `http://127.0.0.1:8000/docs/` for interactive API documentation

### ReDoc
Visit `http://127.0.0.1:8000/redoc/` for alternative API documentation

## Webhook Setup

### 1. Configure Stripe Webhook

1. Go to [Stripe Webhooks](https://dashboard.stripe.com/webhooks)
2. Add endpoint: `https://yourdomain.com/api/payment/webhook/`
3. Select events: `payment_intent.succeeded`, `payment_intent.payment_failed`
4. Copy the webhook signing secret to your `.env` file

### 2. Local Development with Webhooks

For local testing, use the Stripe CLI:

```bash
# Install Stripe CLI
# Then forward webhooks to your local server
stripe listen --forward-to localhost:8000/api/payment/webhook/
```

## Project Structure

```
gateway/
├── accounts/           # User authentication app
│   ├── models.py       # Custom User model
│   ├── serializers.py  # User serializers
│   ├── views.py        # Authentication views
│   └── urls.py         # Authentication URLs
├── payments/           # Payment processing app
│   ├── models.py       # Payment model
│   ├── services.py     # Stripe integration logic
│   ├── views.py        # Payment views
│   ├── webhook.py      # Stripe webhook handler
│   └── urls.py         # Payment URLs
├── gateway/           # Django project settings
│   ├── settings.py     # Project configuration
│   └── urls.py         # Main URL configuration
├── .env                # Environment variables (create this)
├── .gitignore          # Git ignore file
└── manage.py           # Django management script
```

## Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | `django-insecure-...` |
| `DEBUG` | Debug mode | `True/False` |
| `STRIPE_SECRET_KEY` | Stripe secret key | `sk_test_...` |
| `STRIPE_PUBLISHABLE_KEY` | Stripe publishable key | `pk_test_...` |
| `STRIPE_WEBHOOK_SECRET` | Stripe webhook secret | `whsec_...` |

## Security Notes

- ⚠️ **Never commit `.env` file to version control**
- 🔒 Use HTTPS in production
- 🛡️ Validate all user inputs
- 🔑 Keep Stripe keys secure
- 📝 Use environment variables for all sensitive data

## Production Deployment

1. Set `DEBUG=False` in production
2. Use environment variables for all configuration
3. Configure proper CORS settings
4. Set up SSL/TLS certificates
5. Use production Stripe keys (not test keys)
6. Configure proper logging and monitoring

## Troubleshooting

### Common Issues

1. **Stripe Authentication Error**
   - Verify your Stripe API keys in `.env`
   - Ensure keys are correctly formatted

2. **Migration Issues**
   - Run `python manage.py makemigrations`
   - Then run `python manage.py migrate`

3. **CORS Issues**
   - Add CORS middleware for frontend integration
   - Configure allowed origins properly

4. **Webhook Issues**
   - Verify webhook endpoint is accessible
   - Check webhook secret matches Stripe configuration

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For issues and questions:
- Create an issue on GitHub
- Email: admin@marketlink.com

---

**Built with ❤️ using Django and Stripe**
