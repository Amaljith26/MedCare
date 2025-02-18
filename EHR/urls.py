from django.urls import path
from . import views

urlpatterns = [
    path('Medical_Record/', views.upload_medical_record, name='upload_record'),
    path('records/', views.record_list, name='record_list'),
]

    
    
