# Generated by Django 4.2.13 on 2024-05-28 14:35

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("learning_logs", "0003_topic_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="entry",
            name="text",
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
