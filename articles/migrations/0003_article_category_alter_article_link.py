# Generated by Django 4.2.20 on 2025-07-03 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0002_alter_article_link"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="category",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="article",
            name="link",
            field=models.URLField(blank=True, null=True),
        ),
    ]
