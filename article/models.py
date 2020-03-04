
from django.db import models

class Aritcle(models.Model):
    def __str__(self):
        return "("+str(self.article_id)+")"+self.article_title
    article_id = models.AutoField("文章ID",primary_key=True)
    article_type = models.ForeignKey("category.Category",verbose_name='文章类型',on_delete=models.CASCADE)
    article_title = models.CharField("标题",max_length=200)
    article_content = models.TextField("内容")
    like_count = models.IntegerField("点赞数",default=0)
    show_article = models.BooleanField("是否展示",default=1)

    class Meta: 
        verbose_name = '文章'
        verbose_name_plural = '文章'

