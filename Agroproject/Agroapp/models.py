from django.db import models
from django.contrib import admin
CATEGORY=(
  ("1", "Crop production"),
  ("2", "Animal Production"),
  ("3", "Processing"),
)
class Client(models.Model):
  name = models.CharField(max_length=200)
  cat = models.CharField(max_length=200, choices=CATEGORY, default=True)
  doe = models.DateField("Date of Establishment")
admin.site.register(Client)
