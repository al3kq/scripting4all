# Generated by Django 5.0.4 on 2024-05-01 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_stripe_customer_id_user_stripe_subscription_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='stripe_subscription_status',
            field=models.CharField(default='inactive', max_length=20),
        ),
    ]
