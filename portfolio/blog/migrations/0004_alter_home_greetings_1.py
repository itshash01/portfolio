# Generated by Django 4.1.5 on 2023-01-15 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_home_greetings_1_alter_home_greetings_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='greetings_1',
            field=models.CharField(max_length=200),
        ),
    ]
