from django.urls import path
from . import views

urlpatterns = [
    path(
        'search/',
        views.asset_search,
        name='asset_search'
    ),
    path(
    'detail/<int:asset_id>/',
    views.asset_detail,
    name='asset_detail'
),
path(
    'admin-assets/',
    views.asset_list,
    name='asset_list'
),

path(
    'add/',
    views.add_asset,
    name='add_asset'
),
path(
    'edit/<int:asset_id>/',
    views.edit_asset,
    name='edit_asset'
),

path(
    'delete/<int:asset_id>/',
    views.delete_asset,
    name='delete_asset'
),
path(
    'detail/<int:asset_id>/',
    views.asset_detail,
    name='asset_detail'
),
path(
    'departments/',
    views.department_list,
    name='department_list'
),

path(
    'departments/add/',
    views.add_department,
    name='add_department'
),

path(
    'departments/delete/<int:department_id>/',
    views.delete_department,
    name='delete_department'
),
path(
    'buildings/',
    views.building_list,
    name='building_list'
),

path(
    'buildings/add/',
    views.add_building,
    name='add_building'
),

path(
    'buildings/delete/<int:building_id>/',
    views.delete_building,
    name='delete_building'
),
path(
    'export/',
    views.export_assets_excel,
    name='export_assets_excel'
),
]