from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from assets.models import Asset, Department, Building
from complaints.models import Complaint
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request, 'home.html')


def signup_view(request):

    if request.method == 'POST':

        employee_id = request.POST['employee_id']
        name = request.POST['name']
        password = request.POST['password']

        User.objects.create_user(
            username=employee_id,
            first_name=name,
            password=password
        )

        return redirect('login')

    return render(request, 'signup.html')


def login_view(request):

    if request.method == 'POST':

        username = request.POST['employee_id']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            if user.is_superuser:
                return redirect('admin_dashboard')

            return redirect('user_dashboard')

    return render(request, 'login.html')

@never_cache
@login_required(login_url='login')

def user_dashboard(request):
    return render(request, 'user/dashboard.html')

@never_cache
@login_required(login_url='login')
def admin_dashboard(request):

    total_assets = Asset.objects.count()
    total_departments = Department.objects.count()
    total_buildings = Building.objects.count()

    total_complaints = Complaint.objects.count()

    pending_complaints = Complaint.objects.filter(
        status='Pending'
    ).count()

    resolved_complaints = Complaint.objects.filter(
        status='Resolved'
    ).count()

    context = {

        'total_assets': total_assets,
        'total_departments': total_departments,
        'total_buildings': total_buildings,

        'total_complaints': total_complaints,

        'pending_complaints': pending_complaints,

        'resolved_complaints': resolved_complaints,
    }

    return render(
        request,
        'admin/dashboard.html',
        context
    )
@never_cache
def logout_view(request):

    logout(request)

    request.session.flush()

    response = redirect('login')

    response['Cache-Control'] = (
        'no-cache, no-store, must-revalidate'
    )
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'

    return response