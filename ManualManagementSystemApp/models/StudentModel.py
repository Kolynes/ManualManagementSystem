from django.db import models

class StudentModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=256)
    department = models.CharField(max_length=50)
    reg_no = models.CharField(max_length=16)
    manual_id = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    level = models.CharField(max_length=3)

    @property
    def dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "department": self.department,
            "reg_no": self.reg_no,
            "manual_id": self.manual_id,
            "created_at": self.created_at.timestamp() * 1000,
            "updated_at": self.updated_at.timestamp() * 1000,
            "level": self.level,
            "id": self.id
        }

    def save(self, *args, **kwargs):
        all = self.objects.all()
        self.manual_id = "M-%d" %self.objects.all().count()
        super().save(*args, **kwargs)