
from django.http import HttpResponse
from django.template import loader
from .models import Member
from .models import Employee
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from .serializers import MemberSerializer, EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#class MemberView(APIView):
#    def post(self, request):
#        # Verarbeitung der Daten
#        return Response({"message": "Member created"}, status=status.HTTP_201_CREATED)


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

def main_page(request):
    return render(request, "main.html")

def logout_view(request):
    logout(request)  # Django-Session beenden
    return redirect('login')  # Stelle sicher, dass 'login' eine URL in deiner urls.py ist


def login_page(request):
    return render(request, 'login.html')  # Stellt sicher, dass die Datei existiert

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_api(request):
    members = Member.objects.all()
    employees = Employee.objects.all()
    members_serializer = MemberSerializer(members, many=True)
    employees_serializer = EmployeeSerializer(employees, many=True)

    # Anzahl der Mitglieder
    member_count = members.count()

    # Umsatz-Berechnung: Preise für Abonnements (Beispielwerte, in Euro)
    prices = {
        'monthly': 30,      # z. B. 30€ pro Monat
        'quarterly': 80,    # z. B. 80€ pro Quartal
        'yearly': 300       # z. B. 300€ pro Jahr
    }
    revenue = sum(prices.get(member.abonement, 0) for member in members)

    data = {
        "user": request.user.username,
        "member_count": member_count,
        "revenue": revenue,
        "members": members_serializer.data,
        "employees": employees_serializer.data,
    }
    
    return Response(data)


#@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
    

def all_members(request):
   mymembers = Member.objects.all().values()
   template = loader.get_template('all_members.html')
   context = {
     'mymembers': mymembers,
   }
   return HttpResponse(template.render(context, request))

def members_details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('members_details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def all_employees(request):
   myemployees = Employee.objects.all().values()
   template = loader.get_template('all_employees.html')
   context = {
     'myemployees': myemployees,
   }
   return HttpResponse(template.render(context, request))

def employees_details(request, id):
  myemployee = Employee.objects.get(id=id)
  template = loader.get_template('employees_details.html')
  context = {
    'myemployee': myemployee,
  }
  return HttpResponse(template.render(context, request))

