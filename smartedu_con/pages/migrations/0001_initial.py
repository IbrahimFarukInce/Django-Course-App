# Generated by Django 4.1.1 on 2022-12-15 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='İsim Soyisim')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='E Posta')),
                ('phone', models.CharField(max_length=254, verbose_name='Telefon')),
                ('message', models.TextField(blank=True, verbose_name='Açıklama')),
                ('isRead', models.BooleanField(default=False, verbose_name='Okundu mu?')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
            ],
            options={
                'verbose_name': 'İletişim Formu',
                'verbose_name_plural': 'İletişim Formu',
                'managed': True,
            },
        ),
    ]