# Generated by Django 4.2 on 2023-04-18 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_created_post_pub_date_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='iamges'),
        ),
    ]
