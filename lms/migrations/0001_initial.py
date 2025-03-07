# Generated by Django 3.0.5 on 2020-05-11 08:39

import datetime
from django.db import migrations, models
import django.db.models.deletion
import lms.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(default='', max_length=100)),
                ('author_name', models.CharField(default='', max_length=100)),
                ('book_edition', models.CharField(default='', max_length=100)),
                ('book_publisher', models.CharField(default='', max_length=100)),
                ('isbn_no', models.CharField(default='', max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('total_copies', models.PositiveIntegerField(default=0)),
                ('available_copies', models.PositiveIntegerField(default=0)),
                ('genre', models.CharField(choices=[('Adventure', 'Adventure'), ('Autobiography', 'Autobiography'), ('Art', 'Art'), ('Business', 'Business'), ('Biography', 'Biography'), ('Comic-Book', 'Comic-Book'), ('Cookbook', 'Cookbook'), ('Computer-Science', 'Computer-Science'), ('Encyclopedia', 'Encyclopedia'), ('Fantasy', 'Fantasy'), ('Fairytale', 'Fairytale'), ('History', 'History'), ('Horror', 'Horror'), ('Health', 'Health'), ('Mystery', 'Mystery'), ('Motivational', 'Motivational'), ('Mathematics', 'Mathematics'), ('Poetry', 'Poetry'), ('Religion', 'Religion'), ('Romance', 'Romance'), ('Satire', 'Satire'), ('Science-Fiction', 'Science-Fiction'), ('Self-help', 'Self-help'), ('Science', 'Science'), ('Thriller', 'Thriller')], max_length=50)),
                ('stack_no', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=5)),
                ('shelf_no', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], max_length=5)),
                ('row_no', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('roll_no', models.CharField(default='', max_length=25)),
                ('year', models.CharField(choices=[('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV'), ('V', 'V')], default='', max_length=25)),
                ('department', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('Electrical Engg', 'Electrical Engg'), ('Mech Engg', 'Mech Engg'), ('Civil Engg', 'Civil Engg'), ('Prod Engg', 'Prod Engg'), ('Chemical Engg', 'Chemical Engg'), ('BBA', 'BBA'), ('MBA', 'MBA'), ('PHD', 'PHD')], default='', max_length=50)),
                ('contact_no', models.CharField(default='', max_length=15)),
                ('email_id', models.EmailField(default='', max_length=50)),
                ('no_of_issued_books', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ReturnBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actual_return_date', models.DateField(default=datetime.datetime.today)),
                ('fine_amount', models.PositiveIntegerField(default=0)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.Book')),
                ('student_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateField(default=datetime.datetime.today)),
                ('expected_return_date', models.DateField(default=lms.models.get_expected_return_date)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.Book')),
                ('student_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.Student')),
            ],
        ),
    ]
