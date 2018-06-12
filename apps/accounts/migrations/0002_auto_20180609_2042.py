# Generated by Django 2.0.6 on 2018-06-09 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileimg',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='clan',
        ),
        migrations.AlterField(
            model_name='profile',
            name='profileImg',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.DeleteModel(
            name='Clan',
        ),
        migrations.DeleteModel(
            name='ProfileImg',
        ),
    ]
