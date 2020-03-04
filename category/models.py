from django.db import models

class Category(models.Model):
    def __str__(self):
        return self.category_name
    category_id = models.AutoField("分类ID",primary_key=True,default=1)
    category_name = models.CharField(max_length=200)

    class Meta: 
        verbose_name = '分类'
        verbose_name_plural = '分类'

