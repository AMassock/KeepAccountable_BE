from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from .serializers import UserSerializer, TokenSerializer
from .models import API_KEYS, User, FavoriteList
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
def api_keys(request):
    key = API_KEYS.objects.all()
    return JsonResponse(request, '', {'key': key})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', "")
        password = request.POST.get('password', "")
        print(request)

        if not username or not password:
            return JsonResponse({'error': 'Missing username or password'}, status=400)

        try:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return JsonResponse({'success': 'User registered and logged in'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            return JsonResponse({'error': 'Missing username or password'}, status=400)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'success': 'Logged in'})
        else:
            return JsonResponse({'error': 'Invalid username or password'}, status=401)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

