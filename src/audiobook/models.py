from django.db import models


class AudioBook(models.Model):
    file_field = models.FileField(upload_to='documents/')
