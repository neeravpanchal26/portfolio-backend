# Generated by Django 4.0.4 on 2022-07-13 17:05

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('eventNameTwo', models.CharField(max_length=250, null=True)),
                ('eventFrom', models.CharField(max_length=10, null=True)),
                ('eventTo', models.CharField(max_length=10, null=True)),
                ('eventType', models.CharField(max_length=20, null=True)),
                ('eventDescription', wagtail.fields.RichTextField(blank=True, null=True)),
                ('eventIcon', models.CharField(max_length=50, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
