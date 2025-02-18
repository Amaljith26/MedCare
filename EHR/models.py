from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    # Files will be uploaded to MEDIA_ROOT/medical_records/username/filename
    return f'medical_records/{instance.user.username}/{filename}'

class MedicalRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Links record to a user
    document = models.FileField(upload_to='medical_records/')  # Stores the file
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Timestamp of upload

    def __str__(self):
        return f"{self.user.username} - {self.document.name}"
