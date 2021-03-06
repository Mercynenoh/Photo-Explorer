# Generated by Django 3.0 on 2022-05-29 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.ForeignKey(default=1, blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pictures.Location'),
        ),
    ]
