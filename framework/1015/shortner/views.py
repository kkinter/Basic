from django.shortcuts import render
from shortner.models import User

# Create your views here.

def index(request):
    user = User.objects.filter(username="admin").first()
    email = user.email if user else "Anonymous User !"
    if not request.user.is_authenticated: 
        email = "Anonymous User !"

    context = {
        "welcome_msg": f"Hello {email}",

    }

    return render(request, "shortner/index.html", context)