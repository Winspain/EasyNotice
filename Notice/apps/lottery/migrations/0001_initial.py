# Generated by Django 3.2.4 on 2022-04-11 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LotteryInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drawNum', models.CharField(max_length=50, unique=True, verbose_name='开奖期号')),
                ('drawResult', models.CharField(max_length=100, verbose_name='开奖结果')),
                ('drawTime', models.DateField(verbose_name='开奖日期')),
                ('state', models.CharField(max_length=100)),
                ('isDeleted', models.BooleanField()),
                ('createdBy', models.CharField(max_length=100)),
                ('updateBy', models.CharField(max_length=100)),
                ('createdTime', models.DateTimeField(auto_now_add=True)),
                ('updateTime', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'lottery_info',
            },
        ),
        migrations.CreateModel(
            name='MyLottery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selectNum', models.CharField(max_length=100, verbose_name='开奖结果')),
                ('state', models.CharField(max_length=100)),
                ('isDeleted', models.BooleanField()),
                ('createdBy', models.CharField(max_length=100)),
                ('updateBy', models.CharField(max_length=100)),
                ('createdTime', models.DateTimeField(auto_now_add=True)),
                ('updateTime', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'lottery_select',
            },
        ),
    ]
