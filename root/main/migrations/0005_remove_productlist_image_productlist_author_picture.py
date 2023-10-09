# Generated by Django 4.2.5 on 2023-09-30 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_shoppingcart_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productlist',
            name='image',
        ),
        migrations.AddField(
            model_name='productlist',
            name='author',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pics')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.productlist')),
            ],
        ),
    ]
