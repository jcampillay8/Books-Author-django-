# Generated by Django 2.2.4 on 2021-04-30 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0002_auto_20210430_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='escritor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='libros', to='books_authors_app.Author'),
        ),
    ]
