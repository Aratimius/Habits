# Generated by Django 5.1.3 on 2024-11-20 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_tg_chat_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="tg_chat_id",
            field=models.CharField(
                blank=True,
                help_text="укажите chat id из telegram для получения уведомлений",
                max_length=100,
                null=True,
                verbose_name="telegram-chat-id",
            ),
        ),
    ]