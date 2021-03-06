# Generated by Django 3.0.3 on 2020-02-09 01:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0003_client_active'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lots', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sales_price', models.FloatField()),
                ('approval', models.BooleanField(default=True)),
                ('total_comission', models.FloatField()),
                ('broker_comission', models.FloatField()),
                ('sale_date', models.DateField(default=datetime.datetime(2020, 2, 9, 1, 58, 2, 337233, tzinfo=utc))),
                ('active', models.BooleanField(default=True)),
                ('notes', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('broker_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='clients.Client')),
                ('lot_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lots.Lot')),
            ],
        ),
    ]
