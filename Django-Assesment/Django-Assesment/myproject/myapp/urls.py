from django.urls import path
from . import views

urlpatterns = [
    # Authentication URLs
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    
    # Core Application URLs
    path('', views.dashboard_view, name='dashboard'),
    path('profile/', views.profile_view, name='profile'),

    # Admin-specific URLs
    path('delete_notice/<int:notice_id>/', views.delete_notice_view, name='delete_notice'),
    
    # Placeholder URLs for other pages (e.g., Members, Watchmen)
    path('members/', views.dashboard_view, name='members'),
    path('watchmen/', views.dashboard_view, name='watchmen'),
    path('notices/', views.dashboard_view, name='notices'),
    path('events/', views.dashboard_view, name='events'),
]