# Generated by Django 2.1 on 2018-08-19 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='board',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='forum.Board'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='forum.Thread'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.TextField(blank=True, default=''),
        ),
    ]
