from django.db import models

class Deparment(models.Model):
    name = models.CharField('部署名', max_lemgth=20)
    created_at = models.DateTimeField('日付', default=timezone.now)