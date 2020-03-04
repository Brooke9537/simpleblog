# Generated by Django 2.2.10 on 2020-02-29 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20200229_0904'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aritcle',
            options={'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.AlterField(
            model_name='aritcle',
            name='article_content',
            field=models.TextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='aritcle',
            name='article_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='文章ID'),
        ),
        migrations.AlterField(
            model_name='aritcle',
            name='article_title',
            field=models.CharField(max_length=200, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='aritcle',
            name='like_count',
            field=models.IntegerField(default=0, verbose_name='点赞数'),
        ),
        migrations.AlterField(
            model_name='aritcle',
            name='show_article',
            field=models.BooleanField(default=1, verbose_name='是否展示'),
        ),
    ]