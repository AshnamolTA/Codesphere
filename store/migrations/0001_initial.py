# Generated by Django 5.1.2 on 2024-10-23 19:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='store.basemodel')),
                ('title', models.CharField(max_length=200)),
            ],
            bases=('store.basemodel',),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='store.basemodel')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('preview_image', models.ImageField(blank=True, null=True, upload_to='previewimage')),
                ('price', models.PositiveIntegerField()),
                ('files', models.FileField(blank=True, null=True, upload_to='project')),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tag_objects', models.ManyToManyField(to='store.tag')),
            ],
            bases=('store.basemodel',),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='store.basemodel')),
                ('bio', models.CharField(max_length=200)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_picture')),
                ('phone', models.CharField(max_length=200)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('store.basemodel',),
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='store.basemodel')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='basket', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('store.basemodel',),
        ),
        migrations.CreateModel(
            name='WishListItem',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='store.basemodel')),
                ('is_order_placed', models.BooleanField(default=False)),
                ('project_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.project')),
                ('wishlist_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket_item', to='store.wishlist')),
            ],
            bases=('store.basemodel',),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='store.basemodel')),
                ('is_paid', models.BooleanField(default=False)),
                ('order_id', models.CharField(max_length=200, null=True)),
                ('wishlistitem_objects', models.ManyToManyField(to='store.wishlistitem')),
            ],
            bases=('store.basemodel',),
        ),
    ]
