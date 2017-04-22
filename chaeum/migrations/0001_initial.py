# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-06 05:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('board_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('contents', models.CharField(max_length=4000)),
                ('img_url', models.CharField(max_length=200)),
                ('inq_cnt', models.IntegerField()),
                ('like_cnt', models.IntegerField()),
                ('clip_cnt', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boards', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'TBBOARD',
            },
        ),
        migrations.CreateModel(
            name='Brnd',
            fields=[
                ('brnd_id', models.AutoField(primary_key=True, serialize=False)),
                ('brnd_nm', models.CharField(max_length=50)),
                ('like_cnt', models.IntegerField()),
            ],
            options={
                'db_table': 'TBBRND',
            },
        ),
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('clinic_id', models.AutoField(primary_key=True, serialize=False)),
                ('clinic_nm', models.CharField(max_length=200)),
                ('region', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=50)),
                ('inq_cnt', models.IntegerField()),
                ('clip_cnt', models.IntegerField()),
                ('like_cnt', models.IntegerField()),
                ('img_url', models.CharField(max_length=200)),
                ('reg_date', models.DateTimeField()),
                ('mod_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'TBCLINIC',
            },
        ),
        migrations.CreateModel(
            name='ClinicReview',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('score', models.IntegerField()),
                ('good_thing', models.CharField(max_length=500)),
                ('bad_thing', models.CharField(max_length=500)),
                ('tips', models.CharField(max_length=500)),
                ('inq_cnt', models.IntegerField()),
                ('clip_cnt', models.IntegerField()),
                ('like_cnt', models.IntegerField()),
                ('img_url', models.CharField(max_length=200)),
                ('reg_date', models.DateTimeField()),
                ('mod_date', models.DateTimeField(auto_now_add=True)),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clinicrv_clinic', to='chaeum.Clinic')),
                ('usr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clinicrv_usr', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'TBCLINICREVIEW',
            },
        ),
        migrations.CreateModel(
            name='ClinicSurgery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chaeum.Clinic')),
            ],
            options={
                'db_table': 'TBCLINICSURGERY',
            },
        ),
        migrations.CreateModel(
            name='Comp',
            fields=[
                ('comp_id', models.AutoField(primary_key=True, serialize=False)),
                ('comp_nm', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'TBCOMP',
            },
        ),
        migrations.CreateModel(
            name='HairPrd',
            fields=[
                ('hairprd_id', models.AutoField(primary_key=True, serialize=False)),
                ('hairprd_nm', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('cap', models.IntegerField()),
                ('inq_cnt', models.IntegerField()),
                ('clip_cnt', models.IntegerField()),
                ('like_cnt', models.IntegerField()),
                ('img_url', models.CharField(max_length=200)),
                ('brnd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hairprds', to='chaeum.Brnd')),
                ('comp', models.ManyToManyField(to='chaeum.Comp')),
            ],
            options={
                'db_table': 'TBHAIRPRD',
            },
        ),
        migrations.CreateModel(
            name='HairPrdReview',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('score', models.IntegerField()),
                ('good_thing', models.CharField(max_length=500)),
                ('bad_thing', models.CharField(max_length=500)),
                ('tips', models.CharField(max_length=500)),
                ('inq_cnt', models.IntegerField()),
                ('clip_cnt', models.IntegerField()),
                ('like_cnt', models.IntegerField()),
                ('img_url', models.CharField(max_length=200)),
                ('reg_date', models.DateTimeField()),
                ('mod_date', models.DateTimeField(auto_now_add=True)),
                ('hairprd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hairprdrv_hairprd', to='chaeum.HairPrd')),
                ('usr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hairprdrv_usr', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'TBHAIRPRDREVIEW',
            },
        ),
        migrations.CreateModel(
            name='HairPrg',
            fields=[
                ('hairprg_id', models.AutoField(primary_key=True, serialize=False)),
                ('hairprg_nm', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'TBHAIRPRG',
            },
        ),
        migrations.CreateModel(
            name='HairPrgSet',
            fields=[
                ('hairprgset_id', models.AutoField(primary_key=True, serialize=False)),
                ('hairprgset_nm', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'TBHAIRPRGSET',
            },
        ),
        migrations.CreateModel(
            name='HairShop',
            fields=[
                ('hairshop_id', models.AutoField(primary_key=True, serialize=False)),
                ('hairshop_nm', models.CharField(max_length=200)),
                ('region', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('inq_cnt', models.IntegerField()),
                ('clip_cnt', models.IntegerField()),
                ('like_cnt', models.IntegerField()),
                ('img_url', models.CharField(max_length=200)),
                ('reg_date', models.DateTimeField()),
                ('mod_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'TBHAIRSHOP',
            },
        ),
        migrations.CreateModel(
            name='HairShopReview',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('score', models.IntegerField()),
                ('good_thing', models.CharField(max_length=500)),
                ('bad_thing', models.CharField(max_length=500)),
                ('tips', models.CharField(max_length=500)),
                ('inq_cnt', models.IntegerField()),
                ('clip_cnt', models.IntegerField()),
                ('like_cnt', models.IntegerField()),
                ('img_url', models.CharField(max_length=200)),
                ('reg_date', models.DateTimeField()),
                ('mod_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'TBHAIRSHOPREVIEW',
            },
        ),
        migrations.CreateModel(
            name='NormMed',
            fields=[
                ('normmed_id', models.AutoField(primary_key=True, serialize=False)),
                ('normmed_nm', models.CharField(max_length=200)),
                ('inq_cnt', models.IntegerField()),
                ('clip_cnt', models.IntegerField()),
                ('like_cnt', models.IntegerField()),
                ('img_url', models.CharField(max_length=200)),
                ('insur_yn', models.CharField(max_length=1)),
                ('effect', models.CharField(max_length=500)),
                ('usg_cap', models.CharField(max_length=500)),
                ('forbid', models.CharField(max_length=500)),
                ('careful_med', models.CharField(max_length=500)),
                ('side_effect', models.CharField(max_length=500)),
                ('brnd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='normmeds', to='chaeum.Brnd')),
                ('comp', models.ManyToManyField(to='chaeum.Comp')),
            ],
            options={
                'db_table': 'TBNORMMED',
            },
        ),
        migrations.CreateModel(
            name='NormMedReview',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('score', models.IntegerField()),
                ('good_thing', models.CharField(max_length=500)),
                ('bad_thing', models.CharField(max_length=500)),
                ('tips', models.CharField(max_length=500)),
                ('inq_cnt', models.IntegerField()),
                ('clip_cnt', models.IntegerField()),
                ('like_cnt', models.IntegerField()),
                ('img_url', models.CharField(max_length=200)),
                ('reg_date', models.DateTimeField()),
                ('mod_date', models.DateTimeField(auto_now_add=True)),
                ('normmed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='normmedrv_normmed', to='chaeum.NormMed')),
                ('usr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='normmedrv_usr', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'TBNORMMEDREVIEW',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=200)),
                ('push_tkn', models.CharField(max_length=200)),
                ('get_push', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('device', models.CharField(choices=[('A', 'Android'), ('I', 'IOS')], max_length=1)),
                ('gender', models.CharField(choices=[('M', 'Man'), ('W', 'Woman')], max_length=1)),
                ('location', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SpecMed',
            fields=[
                ('specmed_id', models.AutoField(primary_key=True, serialize=False)),
                ('specmed_nm', models.CharField(max_length=200)),
                ('inq_cnt', models.IntegerField()),
                ('clip_cnt', models.IntegerField()),
                ('like_cnt', models.IntegerField()),
                ('img_url', models.CharField(max_length=200)),
                ('insur_yn', models.CharField(max_length=1)),
                ('effect', models.CharField(max_length=500)),
                ('usg_cap', models.CharField(max_length=500)),
                ('forbid', models.CharField(max_length=500)),
                ('careful_med', models.CharField(max_length=500)),
                ('side_effect', models.CharField(max_length=500)),
                ('brnd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specmeds', to='chaeum.Brnd')),
                ('comp', models.ManyToManyField(to='chaeum.Comp')),
            ],
            options={
                'db_table': 'TBSPECMED',
            },
        ),
        migrations.CreateModel(
            name='SpecMedReview',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('score', models.IntegerField()),
                ('good_thing', models.CharField(max_length=500)),
                ('bad_thing', models.CharField(max_length=500)),
                ('tips', models.CharField(max_length=500)),
                ('inq_cnt', models.IntegerField()),
                ('clip_cnt', models.IntegerField()),
                ('like_cnt', models.IntegerField()),
                ('img_url', models.CharField(max_length=200)),
                ('reg_date', models.DateTimeField()),
                ('mod_date', models.DateTimeField(auto_now_add=True)),
                ('specmed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specmedrv_specmed', to='chaeum.SpecMed')),
                ('usr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specmedrv_usr', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'TBSPECMEDREVIEW',
            },
        ),
        migrations.CreateModel(
            name='Surgery',
            fields=[
                ('surgery_id', models.AutoField(primary_key=True, serialize=False)),
                ('surgery_nm', models.CharField(max_length=200)),
                ('inq_cnt', models.IntegerField()),
                ('clip_cnt', models.IntegerField()),
                ('like_cnt', models.IntegerField()),
                ('reg_date', models.DateTimeField()),
                ('mod_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'TBSURGERY',
            },
        ),
        migrations.CreateModel(
            name='SurgeryReview',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('score', models.IntegerField()),
                ('good_thing', models.CharField(max_length=500)),
                ('bad_thing', models.CharField(max_length=500)),
                ('tips', models.CharField(max_length=500)),
                ('inq_cnt', models.IntegerField()),
                ('clip_cnt', models.IntegerField()),
                ('like_cnt', models.IntegerField()),
                ('img_url', models.CharField(max_length=200)),
                ('reg_date', models.DateTimeField()),
                ('mod_date', models.DateTimeField(auto_now_add=True)),
                ('surgery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='surgeryrv_surgery', to='chaeum.Surgery')),
                ('usr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='surgeryrv_usr', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'TBSURGERYREVIEW',
            },
        ),
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('tip_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('tip_ctnt', models.CharField(max_length=4000)),
                ('img_url', models.CharField(max_length=200)),
                ('inq_cnt', models.IntegerField()),
                ('like_cnt', models.IntegerField()),
                ('clip_cnt', models.IntegerField()),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('mod_date', models.DateTimeField(auto_now_add=True)),
                ('usr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tips', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'TBTIP',
            },
        ),
        migrations.AddField(
            model_name='hairshopreview',
            name='hairshop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hairshoprv_hairshop', to='chaeum.SpecMed'),
        ),
        migrations.AddField(
            model_name='hairshopreview',
            name='usr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hairshoprv_usr', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='hairprgset',
            name='hairshop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hairprgset_hairshop', to='chaeum.HairShop'),
        ),
        migrations.AddField(
            model_name='hairprg',
            name='hairprgset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hairprg_hairprgset', to='chaeum.HairShop'),
        ),
        migrations.AddField(
            model_name='clinicsurgery',
            name='surgery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chaeum.Surgery'),
        ),
        migrations.AddField(
            model_name='clinic',
            name='surgeries',
            field=models.ManyToManyField(through='chaeum.ClinicSurgery', to='chaeum.Surgery'),
        ),
    ]
