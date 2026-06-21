from django.urls import path
from . import views

urlpatterns = [

    path(
        'create/',
        views.complaint_create,
        name='create_complaint'
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
]