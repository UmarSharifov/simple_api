from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index,
         name='index'),
    path('get_all_catalogs/', views.get_all_catalogs.as_view(),
         name='get_all_catalogs'),
    path('get_actual_catalogs/<str:actualDate>/', views.get_actual_catalogs.as_view(),
         name='get_actual_catalogs'),
    path('get_Elements_actual_catalog/<str:short_name>/', views.get_Elements_actual_catalog.as_view(),
         name='get_Elements_actual_catalog'),
    path('validation_Elements_actual_version_catalog/<str:short_name>/', views.validation_Elements_actual_version_catalog.as_view(),
         name='validation_Elements_actual_version_catalog'),
    path('get_Elements_of_current_version_catalog/<str:version>/',views.get_Elements_of_current_version_catalog.as_view(),
         name='get_Elements_of_current_version_catalog'),
    path('validation_Elements_current_version_version_catalog/<str:version>/',views.validation_Elements_current_version_version_catalog.as_view(),
         name='validation_Elements_current_version_version_catalog'),
  ]