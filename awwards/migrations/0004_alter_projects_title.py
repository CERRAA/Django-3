# Generated by Django 4.0.3 on 2022-06-16 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0003_alter_rating_content_alter_rating_design_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]