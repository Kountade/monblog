# Generated by Django 4.2.2 on 2023-06-30 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_coursphp_options_alter_coursphp_resultat_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coursphp",
            name="code",
            field=models.TextField(max_length=50000),
        ),
        migrations.AlterField(
            model_name="coursphp",
            name="title",
            field=models.CharField(max_length=500),
        ),
    ]
