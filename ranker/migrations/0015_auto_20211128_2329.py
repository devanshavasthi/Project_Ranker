# Generated by Django 3.2.8 on 2021-11-28 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ranker', '0014_auto_20211128_1844'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FrequentPaper',
        ),
        migrations.AlterModelOptions(
            name='fetchinfo',
            options={'ordering': ['rank']},
        ),
    ]
