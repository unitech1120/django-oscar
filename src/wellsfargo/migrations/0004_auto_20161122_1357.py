# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-22 13:57
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('order', '0004_auto_20160111_1108'),
        ('wellsfargo', '0003_financingplan_is_default_plan'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountOwner',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='accountmetadata',
            name='billing_address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='order.BillingAddress', verbose_name='Billing Address'),
        ),
    ]
