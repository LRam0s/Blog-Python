# Generated by Django 4.0.3 on 2022-04-01 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_blog_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]