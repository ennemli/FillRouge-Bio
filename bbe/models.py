from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.conf import settings


class CustomUser(BaseUserManager):
    def create_user(
        self,
        username,
        first_name,
        last_name,
        password,
        birth_date,
        email,
        address,
        is_superuser=False,
        is_staff=False,
    ):
        email = self.normalize_email(email)
        user = self.model(
            is_superuser=is_superuser,
            email=email,
            is_staff=is_staff,
            username=username,
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            password=password,
            address=address
        )
        user.set_password(password)
        user.save()

    def create_superuser(
        self,
        username,
        first_name,
        last_name,
        password,
        birth_date,
        email,
        address,
        is_superuser=False,
        is_staff=False,
    ):
        return self.create_user(
            username,
            first_name,
            last_name,
            password,
            birth_date,
            email,
            address,
            is_superuser=True,
            is_staff=True,
        )


class Client(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        verbose_name="Nom d'utilisateur",
        max_length=30,
        unique=True,
    )
    first_name = models.CharField(verbose_name="Prénom", max_length=50)
    last_name = models.CharField(verbose_name="Nom de famille", max_length=50)
    email = models.EmailField(verbose_name="Email", unique=True, max_length=255)
    address = models.CharField(verbose_name="Addresse", default="", max_length=555)
    orders = models.IntegerField(verbose_name="ordres", default=0)
    birth_date = models.DateField(verbose_name="Date de naissance")
    password = models.CharField(verbose_name="Mot de pass", max_length=255)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    objects = CustomUser()
    REQUIRED_FIELDS = [
        "username",
        "first_name",
        "last_name",
        "birth_date",
        "address",
    ]

    def __str__(self):
        return self.username


class ProductImage(models.Model):
    image = models.TextField(max_length=100000000)


class Product(models.Model):
    price = models.FloatField()
    product_name = models.CharField(max_length=255)
    product_description = models.TextField(max_length=3000)
    max_quantity = models.IntegerField()
    left_quantity = models.IntegerField()
    is_available = models.BooleanField()
    image = models.ForeignKey(ProductImage, default="", on_delete=models.CASCADE)
    clients = models.ManyToManyField(
        settings.AUTH_USER_MODEL, through="ProductClient", related_name="products"
    )

    def __str__(self):
        return self.product_name


class ProductClient(models.Model):
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="ProductClient_client",
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product, related_name="ProductClient_product", on_delete=models.CASCADE
    )
    order_date = models.DateField(auto_now=True)
    bought = models.BooleanField(default=False)
    order_quantity = models.IntegerField(default=0)
