from django.shortcuts import render, redirect
from .forms import MedicalRecordForm
from .models import MedicalRecord
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

@login_required
def upload_medical_record(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please log in to upload records.")
        print("User is not authenticated, redirecting to login page.")  # Debugging print
        return redirect('Login')  # Redirect to login page

    print("User is authenticated, rendering upload page.") 

    if request.method == "POST":
        form = MedicalRecordForm(request.POST, request.FILES)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user 
            record.save()
            return redirect('record_list')
    else:
        form = MedicalRecordForm()
 
    return render(request, 'upload_to.html', {'form': form})

@login_required
def record_list(request):
    records = MedicalRecord.objects.filter(user=request.user)  
    return render(request, 'display_data.html', {'records': records})
