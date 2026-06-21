from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import ComplaintForm
from .models import Complaint
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required

from .models import Complaint
from .forms import ComplaintForm, ComplaintStatusForm


@login_required
def complaint_create(request):

    if request.method == 'POST':
        form = ComplaintForm(request.POST, request.FILES)

        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user
            complaint.save()

            return redirect('my_complaints')

    else:
        form = ComplaintForm()

    return render(
        request,
        'complaints/create.html',
        {'form': form}
    )


@login_required
def my_complaints(request):

    complaints = Complaint.objects.filter(
        user=request.user
    )

    return render(
        request,
        'complaints/list.html',
        {'complaints': complaints}
    )
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_complaints(request):

    complaints = Complaint.objects.all().order_by(
        '-created_at'
    )

    return render(
        request,
        'complaints/admin_list.html',
        {
            'complaints': complaints
        }
    )

@staff_member_required
def complaint_list(request):

    complaints = Complaint.objects.all().order_by('-created_at')

    return render(
        request,
        'complaints/admin_list.html',
        {
            'complaints': complaints
        }
    )


@staff_member_required
def update_status(request, complaint_id):

    complaint = get_object_or_404(
        Complaint,
        id=complaint_id
    )

    if request.method == 'POST':

        form = ComplaintStatusForm(
            request.POST,
            instance=complaint
        )

        if form.is_valid():

            form.save()

            return redirect(
                'complaint_list'
            )

    else:

        form = ComplaintStatusForm(
            instance=complaint
        )

    return render(
        request,
        'complaints/update_status.html',
        {
            'form': form,
            'complaint': complaint
        }
    )