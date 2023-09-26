# Generated by Django 4.1.1 on 2022-10-07 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_remove_user_watchlist_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='current_bid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='latest_bid', to='auctions.bid'),
        ),
        migrations.AddField(
            model_name='listings',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listings',
            name='bid',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='listings',
            name='description',
            field=models.CharField(blank=True, default='Regret', max_length=200),
        ),
        migrations.AlterField(
            model_name='listings',
            name='title',
            field=models.CharField(max_length=64),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=256)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_of_comment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('listing', models.ManyToManyField(blank=True, related_name='category_listings', to='auctions.listings')),
            ],
        ),
        migrations.AddField(
            model_name='listings',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='comments_of_item', to='auctions.comment'),
        ),
        migrations.AlterField(
            model_name='listings',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_of_item', to='auctions.category'),
        ),
    ]
