# Generated by Django 2.2.10 on 2020-02-29 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aritcle',
            name='id',
        ),
        migrations.AddField(
            model_name='aritcle',
            name='article_content',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='aritcle',
            name='isshow_article',
            field=models.BooleanField(default=1),
        ),
        migrations.AddField(
            model_name='aritcle',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='aritcle',
            name='article_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]