# Generated by Django 4.0.2 on 2022-03-02 17:16

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
            name='County',
            fields=[
                ('county', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Edu_Level',
            fields=[
                ('level', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='Education Level')),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('gender', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cv_file', models.FileField(blank=True, null=True, upload_to='allFiles', verbose_name='Upload CV')),
                ('aP_file', models.FileField(blank=True, null=True, upload_to='allFiles', verbose_name='Upload Application Letter')),
                ('gD_file', models.FileField(blank=True, null=True, upload_to='allFiles', verbose_name='Upload Good Conduct')),
                ('sL_file', models.FileField(blank=True, null=True, upload_to='allFiles', verbose_name='Upload School Letter')),
                ('natID_file', models.ImageField(blank=True, null=True, upload_to='allFiles', verbose_name='Upload National ID')),
                ('pP_file', models.FileField(blank=True, null=True, upload_to='allFiles', verbose_name='Upload PassPort')),
                ('personalAcc_file', models.FileField(blank=True, null=True, upload_to='allFiles', verbose_name='Upload Personal Accidents Cover')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Secondary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_high', models.CharField(blank=True, max_length=100, null=True, verbose_name='HighSchool Name')),
                ('kcse_file', models.FileField(blank=True, null=True, upload_to='allFiles', verbose_name='Upload KCSE')),
                ('sec_start_date', models.DateField(blank=True, null=True, verbose_name='Starting Date')),
                ('sec_finish_date', models.DateField(blank=True, null=True, verbose_name='Finishing Date')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Primary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_pri', models.CharField(blank=True, max_length=100, null=True, verbose_name='Primary School Name')),
                ('kcpe_file', models.FileField(blank=True, null=True, upload_to='allFiles', verbose_name='Upload KCPE')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Starting Date')),
                ('finish_date', models.DateField(blank=True, null=True, verbose_name='Finishing Date')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Next',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kin_nat_id', models.IntegerField(blank=True, null=True, unique=True, verbose_name='Next Of National ID')),
                ('kin_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Kin Full Name')),
                ('kin_phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='Kin Phone Number')),
                ('kin_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Kin Email')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Higher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(blank=True, max_length=100, null=True, verbose_name='Institution Name')),
                ('course', models.CharField(blank=True, max_length=100, null=True, verbose_name='Course')),
                ('uni_start_date', models.DateField(verbose_name='Starting Date')),
                ('uni_finish_date', models.DateField(verbose_name='Finishing Date')),
                ('level', models.ForeignKey(default='Certificate', on_delete=django.db.models.deletion.CASCADE, to='App1.edu_level', verbose_name='Education Level')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nat_id', models.IntegerField(blank=True, null=True, unique=True, verbose_name='National ID')),
                ('full_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Full Name')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='Age')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='Phone Number')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Address')),
                ('postal_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='Postal Code')),
                ('date_register', models.DateTimeField(auto_now_add=True, verbose_name='Register Date')),
                ('county', models.ForeignKey(default='Nairobi', on_delete=django.db.models.deletion.CASCADE, to='App1.county', verbose_name='County')),
                ('gender', models.ForeignKey(default='Unspecified', on_delete=django.db.models.deletion.CASCADE, to='App1.gender', verbose_name='Gender')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]