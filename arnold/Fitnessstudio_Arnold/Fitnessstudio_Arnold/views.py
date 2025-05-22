from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#@api_view(['GET'])
#@permission_classes([IsAuthenticated])
#def dashboard(request):
   
#    return render(request, 'dashboard.html')  # Datei muss in templates/ existieren






def login_page(request):
    return render(request, 'login.html')  # Stellt sicher, dass die Datei existiert

