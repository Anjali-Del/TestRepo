# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('article_id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=1000000)),
                ('pub_date', models.DateTimeField(verbose_name=b'Last edited')),
            ],
        ),
        migrations.CreateModel(
            name='author_signup',
            fields=[
                ('aid', models.AutoField(serialize=False, primary_key=True)),
                ('author_name', models.CharField(max_length=200)),
                ('email', models.EmailField(unique=True, max_length=200)),
                ('pswd', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='uid',
            field=models.ForeignKey(to='wikipage.author_signup'),
        ),
    ]
