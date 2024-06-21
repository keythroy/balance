from django.db import models

class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    repeat_password = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.name}[{self.email}]'
    
    class Meta:
        verbose_name = 'Register'
        verbose_name_plural = 'Registers'
        ordering = ['name']
