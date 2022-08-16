# Generated by Django 4.1 on 2022-08-15 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=78)),
                ('author', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=288)),
                ('url', models.CharField(max_length=500, null=True)),
                ('urlToImage', models.CharField(max_length=500, null=True)),
                ('publishedAt', models.DateField()),
                ('added', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ('-publishedAt',),
            },
        ),
        migrations.CreateModel(
            name='SubscribersEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('created', models.DateField(auto_now_add=True)),
                ('sent', models.IntegerField()),
            ],
        ),
    ]