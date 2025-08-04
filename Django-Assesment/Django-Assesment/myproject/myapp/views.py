from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .forms import UserRegistrationForm, LoginForm
from .models import CustomUser, Member, Watchman, Notice
from .utils import send_confirmation_email
import json

# MVT: View
def login_view(request):
    """Handles user login."""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    """Handles user logout."""
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')

def register_view(request):
    """
    Handles user registration with a standard form submission.
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            
            # Create a corresponding profile object based on user type
            if user.user_type == "Member":
                Member.objects.create(user=user)
            elif user.user_type == "Watchman":
                Watchman.objects.create(user=user)
            
            # You can send an email here if you want
            # subject = 'Welcome to Digital Society!'
            # message = f'Hi {user.username},\n\nThank you for registering. Your account is pending approval by the admin.'
            # send_confirmation_email(user.email, subject, message)
            
            messages.success(request, 'Registration successful! Your account is pending admin approval.')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})
def forgot_password_view(request):
    """
    Handles the forgot password flow.
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = CustomUser.objects.get(email=email)
            subject = 'Password Reset Request'
            message = 'A password reset link has been requested. Please contact the administrator.'
            send_confirmation_email(email, subject, message)
            messages.success(request, 'Password reset instructions have been sent to your email.')
        except CustomUser.DoesNotExist:
            messages.error(request, 'No user found with that email address.')
        return redirect('forgot_password')
    return render(request, 'forgot_password.html')

@login_required
def dashboard_view(request):
    """Displays the main dashboard for logged-in users."""
    total_members = Member.objects.count()
    total_watchmen = Watchman.objects.count()
    latest_notices = Notice.objects.all().order_by('-created_at')[:5]
    
    context = {
        'total_members': total_members,
        'total_watchmen': total_watchmen,
        'latest_notices': latest_notices,
    }
    return render(request, 'dashboard.html', context)

@login_required
def profile_view(request):
    """Displays the user's profile."""
    if request.user.user_type == "Member":
        profile = get_object_or_404(Member, user=request.user)
    elif request.user.user_type == "Watchman":
        profile = get_object_or_404(Watchman, user=request.user)
    else:
        profile = request.user 

    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)

@login_required
def delete_notice_view(request, notice_id):
    """Allows superusers to delete a notice."""
    if not request.user.is_superuser:
        messages.error(request, "You do not have permission to perform this action.")
        return redirect('dashboard')
        
    notice = get_object_or_404(Notice, pk=notice_id)
    
    if request.method == 'POST':
        confirmation = request.POST.get('confirmation')
        if confirmation and confirmation.lower() == 'y':
            notice.delete()
            messages.success(request, "Notice deleted successfully.")
            return redirect('dashboard')
        else:
            messages.info(request, "Deletion cancelled.")
            return redirect('dashboard')
    
    return render(request, 'delete_notice_confirm.html', {'notice': notice})