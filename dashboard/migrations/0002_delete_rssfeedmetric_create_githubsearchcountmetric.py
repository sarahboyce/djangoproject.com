# Generated by Django 2.2.24 on 2021-10-27 01:33
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GitHubSearchCountMetric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('slug', models.SlugField()),
                ('position', models.PositiveSmallIntegerField(default=1)),
                ('show_on_dashboard', models.BooleanField(default=True)),
                ('show_sparkline', models.BooleanField(default=True)),
                ('period', models.CharField(choices=[('instant', 'Instant'), ('daily', 'Daily'), ('weekly', 'Weekly')], default='instant', max_length=15)),
                ('unit', models.CharField(max_length=100)),
                ('unit_plural', models.CharField(max_length=100)),
                ('api_url', models.URLField(max_length=1000)),
                ('link_url', models.URLField(max_length=1000)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='RSSFeedMetric',
        ),
    ]