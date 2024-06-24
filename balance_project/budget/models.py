from django.db import models

class Budget(models.Model):
    id_budget = models.AutoField(primary_key=True)
    id_user = models.IntegerField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return f'{self.name}[{self.description}]'
    
    class Meta:
        verbose_name = 'Budget'
        verbose_name_plural = 'Budgets'
        ordering = ['id_budget']

class Category(models.Model):

    id_category = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    id_user = models.IntegerField()
    type = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}[{self.description}]'
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id_category']


class Meta(models.Model):

    id_meta = models.AutoField(primary_key=True)
    id_user = models.IntegerField()
    id_budget = models.IntegerField()
    id_category = models.IntegerField()

    def __str__(self):
        return f'{self.name}[{self.description}]'
    
    class Meta:
        verbose_name = 'Meta'
        verbose_name_plural = 'Metas'
        ordering = ['name']