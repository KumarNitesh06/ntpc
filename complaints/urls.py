from django.urls import path
from . import views

urlpatterns = [

    path(
        'create/',
        views.complaint_create,
        name='create_complaint'
    ),
    path(
        'my/',
        views.my_complaints,
        name='my_complaints'
    ),

    path(
        'admin/',
        views.complaint_list,
        name='complaint_list'
    ),

    path(
        'update/<int:complaint_id>/',
        views.update_status,
        name='update_status'
    ),
    path(
    'export/',
    views.export_complaints_excel,
    name='export_complaints_excel'
),
]