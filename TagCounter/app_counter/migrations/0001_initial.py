# Generated by Django 3.2.7 on 2021-10-22 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TagCounter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=2048, verbose_name='URL')),
                ('status', models.CharField(choices=[('performed', 'Performed'), ('done', 'Done')], max_length=9, verbose_name='Parse status')),
                ('tags', models.JSONField(default=dict, verbose_name='URL Tags')),
            ],
            options={
                'verbose_name': 'Counter',
                'verbose_name_plural': 'Counters',
            },
        ),
    ]
