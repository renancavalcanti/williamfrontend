from django.db import models

class Task(models.Model):
    created_by_uid = models.CharField(max_length=255)  
    created_by_name = models.CharField(max_length=255)
    assigned_to_uid = models.CharField(max_length=255)
    assigned_to_name = models.CharField(max_length=255)
    description = models.TextField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.description} - Assigned to {self.assigned_to_name}- Created_by_uid {self.created_by_uid}"
