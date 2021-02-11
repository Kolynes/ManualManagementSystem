from django.forms import ModelForm
from ManualManagementSystemApp.models import StudentModel

class StudentModelForm(ModelForm):
    class Meta:
        model = StudentModel
        exclude = ["manual_id", "created_at", "updated_at"]
        