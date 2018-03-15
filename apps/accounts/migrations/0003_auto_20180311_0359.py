# Generated by Django 2.0.3 on 2018-03-11 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180311_0358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clan',
            name='clan',
            field=models.CharField(choices=[('CATS', 'Cats'), ('DOGS', 'Dogs'), ('RATS', 'Rats'), ('RACCONS', 'Racoons'), ('BIRDS', 'Birds'), ('PIGEONS', 'Pigeons'), ('REPTILES', 'Reptiles'), ('SNAKES', 'Snakes')], max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='clan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Clan'),
        ),
        migrations.AlterField(
            model_name='profileimg',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profileImg', to='accounts.Clan'),
        ),
    ]