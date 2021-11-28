# Generated by Django 3.2.8 on 2021-11-28 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranker', '0013_mkeyword_frequency'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fetchinfo',
            options={'ordering': ['rank', 'papername']},
        ),
        migrations.AddField(
            model_name='newpaper',
            name='url',
            field=models.URLField(default='https://www.semanticscholar.org/', null=True),
        ),
    ]
