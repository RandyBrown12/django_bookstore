# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Authors(models.Model):
    author_id = models.AutoField(primary_key=True)
    author_first_name = models.TextField()
    author_last_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'authors'
        unique_together = (('author_first_name', 'author_last_name'),)


class BookToAuthor(models.Model):
    book_to_author_id = models.AutoField(primary_key=True)
    book = models.ForeignKey('Books', models.DO_NOTHING)
    author = models.ForeignKey(Authors, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'book_to_author'
        unique_together = (('book', 'author'),)


class BookToPublisher(models.Model):
    book_to_publisher_id = models.AutoField(primary_key=True)
    book = models.ForeignKey('Books', models.DO_NOTHING)
    publisher = models.ForeignKey('Publishers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'book_to_publisher'
        unique_together = (('book', 'publisher'),)


class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.TextField()
    category = models.TextField()
    language = models.TextField()
    page_count = models.IntegerField()
    description = models.TextField()
    book_count = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.BinaryField()

    class Meta:
        managed = False
        db_table = 'books'


class CartInformation(models.Model):
    cart_information_id = models.AutoField(primary_key=True)
    customer_id = models.CharField()
    book_id = models.CharField()
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cart_information'

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class OrderBooks(models.Model):
    order_books_id = models.AutoField(primary_key=True)
    order = models.ForeignKey('Orders', models.DO_NOTHING, blank=True, null=True)
    book = models.ForeignKey(Books, models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_books'


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class PgbenchAccounts(models.Model):
    aid = models.IntegerField(primary_key=True)
    bid = models.IntegerField(blank=True, null=True)
    abalance = models.IntegerField(blank=True, null=True)
    filler = models.CharField(max_length=84, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pgbench_accounts'


class PgbenchBranches(models.Model):
    bid = models.IntegerField(primary_key=True)
    bbalance = models.IntegerField(blank=True, null=True)
    filler = models.CharField(max_length=88, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pgbench_branches'


class PgbenchHistory(models.Model):
    tid = models.IntegerField(blank=True, null=True)
    bid = models.IntegerField(blank=True, null=True)
    aid = models.IntegerField(blank=True, null=True)
    delta = models.IntegerField(blank=True, null=True)
    mtime = models.DateTimeField(blank=True, null=True)
    filler = models.CharField(max_length=22, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pgbench_history'


class PgbenchTellers(models.Model):
    tid = models.IntegerField(primary_key=True)
    bid = models.IntegerField(blank=True, null=True)
    tbalance = models.IntegerField(blank=True, null=True)
    filler = models.CharField(max_length=84, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pgbench_tellers'


class Publishers(models.Model):
    publisher_id = models.AutoField(primary_key=True)
    publisher = models.TextField()
    publisher_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'publishers'
        unique_together = (('publisher_id', 'publisher'),)

class BookInformation(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    language = models.TextField(blank=True, null=True)
    page_count = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    book_count = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.BinaryField(blank=True, null=True)
    authors = models.TextField(blank=True, null=True)
    publishers = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_information'