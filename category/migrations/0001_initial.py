# Generated by Django 4.2 on 2023-04-24 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('Draft', 'Draft'), ('Live', 'Live')], max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modify_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
