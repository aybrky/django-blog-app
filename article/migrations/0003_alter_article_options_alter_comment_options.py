# Generated by Django 4.1.7 on 2023-03-16 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_alter_article_article_image_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_date']},
        ),
    ]