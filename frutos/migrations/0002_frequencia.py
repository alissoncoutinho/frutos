# Generated by Django 3.2.4 on 2021-06-22 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frutos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Frequencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frutos.pessoa')),
                ('reuniao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frutos.reuniao')),
            ],
        ),
    ]
