# Generated by Django 3.1.6 on 2021-02-03 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('totalPrice', models.DecimalField(decimal_places=2, max_digits=20)),
                ('orderId', models.PositiveIntegerField()),
                ('ingedients', models.ManyToManyField(blank=True, to='pizzas.Ingredient')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzas.size')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzas.user')),
            ],
        ),
    ]
