from django.urls import path, include
#from . import views

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import dashboard, login_page
from .views import logout_view
from .views import main_page, dashboard_api, all_members, members_details, all_employees, employees_details
from rest_framework.routers import DefaultRouter
from .views import MemberViewSet, EmployeeViewSet

# DRF Router für ViewSets
router = DefaultRouter()
router.register(r'member', MemberViewSet)  # Erstellt /api/members/
router.register(r'employee', EmployeeViewSet)  # Erstellt /api/employees/



urlpatterns = [
    path('members/', all_members, name='all_members'),
    path('members/<int:id>/', members_details, name='members_details'),
    path('employees/', all_employees, name='all_employees'),
    path('employees/<int:id>/', employees_details, name='employees_details'),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/dashboard/', dashboard, name='dashboard'),
    path('api/dashboard/', dashboard_api, name='dashboard_api'),
    path('login/', login_page, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', main_page, name='main'),
    path('api/', include(router.urls)),  # Füge den Router hinzu
]

