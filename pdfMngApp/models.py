from django.db import models

# Create your models here.

class uploadfile(models.Model):
    f_name = models.CharField(max_length=255)
    files = models.FileField(upload_to="")

    # def __str__(self) -> str:
    #     return super().__str__()