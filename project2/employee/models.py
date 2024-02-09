from django.db import models

class Deparment(models.Model):
    name = models.CharField('部署名', max_lemgth=20)
    created_at = models.DateTimeField('日付', default=timezone.now)

    def__str(self):
        return self.name
    
class Employee(models.Model):
    first_name = models.CharField('名', max_lemgth=20)
    last_name = models.CharField('姓', max_lemgth=20)
    email = models.EmailField('メールアドレス', blank=True)
    Deparment, verbose_name(= '部署', on_delete=models.PRPJECT,)

    created_at = models.DateTimeField('日付', default=timezone.now)

    def__str(self):
        return '{0} {1} {2}'.format(self.last_name, self.first_name, self.deparment)