import jwt
import json
from datetime import datetime, timedelta, timezone
from django.conf import settings
from django.contrib.auth import authenticate
from django.http import JsonResponse
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

def generate_jwt(user):
    expiration = timedelta(hours=1)  # Access token expires in 1 hour
    payload = {
        'sub': user.id,
        'username': user.username,
        'exp': datetime.now(timezone.utc) + expiration
    }
    token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return token

@csrf_exempt
def login(request):
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>") 
    if request.method == 'POST':
            if request.content_type == 'application/json':
                data = json.loads(request.body)
                username = data.get('username')
                password = data.get('password')
            else:
                data = request.POST
                username = data.get('username')
                password = data.get('password')

            print(f"Attempting login with username: {username} and password: {password}")

            user = authenticate(username=username, password=password)
            if user:
                expiration = timedelta(hours=1)  # Access token expires in 1 hour
                payload = {
                    'sub': user.id,
                    'username': user.username,
                    'exp': datetime.now(timezone.utc) + expiration
                }
                token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
                print("##################", token)
                return JsonResponse({'token': token}, status=200)
            return JsonResponse({'message': 'Invalid credentials'}, status=401)

def login_page(request):
    return render(request, 'authentication/login.html')

def timer_page(request):
    return render(request, 'authentication/timer.html')