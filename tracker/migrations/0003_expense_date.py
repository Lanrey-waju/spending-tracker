# Generated by Django 4.1.6 on 2023-02-12 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tracker", "0002_expense"),
    ]

    operations = [
        migrations.AddField(
            model_name="expense",
            name="date",
            field=models.DateField(auto_now=True),
        ),
    ]