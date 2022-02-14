from distutils.command.upload import upload
import imp
from re import T
from tabnanny import verbose
from tkinter import CASCADE
from xmlrpc.client import boolean
from django.db import models
from django.forms import CharField
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class Product (models.Model):
    PRDName = models.CharField(max_length=100, verbose_name=_("product name"))
    PRDCategory = models.ForeignKey(
        'Category', on_delete=models.CASCADE, null=True, blank=True)
    PRDBrand = models.ForeignKey(
        'Brand', on_delete=models.CASCADE, null=True, blank=True)

    PRDDesc = models.TextField(verbose_name=_("product description"))
    PRDImage = models.ImageField(verbose_name=_(
        "product image"), null=True, blank=True)
    PRDPrice = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name=_("product price"))
    PRDDiscountPrice = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name=_("product Discount price"))

    PRDCost = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name=_("product cost"))
    PRDCreatedAt = models.DateTimeField(verbose_name=_("created at "))

    PRDSlug = models.SlugField(null=True, blank=True)

    PRDIsnew = models.BooleanField(default=True)
    PRDIsBestSeller = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.PRDSlug:
            self.PRDSlug = slugify(self.PRDName)

        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.PRDName


class ProductImage(models.Model):
    PRDIProduct = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name=_("product id"))

    PRDImage = models.ImageField(
        upload_to='products_images/', verbose_name=_("product image "))

    def __str__(self):
        return str(self.PRDIProduct)


class Category(models.Model):

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    CATName_Category = models.CharField(
        max_length=50, verbose_name=_("category name"))

    CATParent = models.ForeignKey(
        'self', on_delete=models.CASCADE, limit_choices_to={
            'CATParent__isnull': True
        }, blank=True, null=True, verbose_name=_("main category"))

    CATDesc = models.TextField(verbose_name=_("category desc"))

    CATImage = models.ImageField(
        upload_to="categories_images/", verbose_name=_("category image"))

    def __str__(self):
        return str(self.CATName_Category)


class Product_Alternative(models.Model):
    PALProduct = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='main_product', verbose_name=_("product id"))
    PALAlternatives = models.ManyToManyField(
        Product, related_name='alternative_products', verbose_name=_("product alternatives"))

    def __str__(self):
        return str(self.PALProduct)


class Product_Accessories(models.Model):

    class Meta:
        verbose_name = ("Product Accessory")
        verbose_name_plural = ("Product Accessories")

    PACProduct = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='mainAccessory_product', verbose_name=_("product id"))
    PACAlternatives = models.ManyToManyField(
        Product, related_name='accessories_products', verbose_name=_("product accessories"))

    def __str__(self):
        return str(self.PACProduct)


class Brand(models.Model):
    BRAName = models.CharField(max_length=40)
    BRADesc = models.TextField()

    def __str__(self) -> str:
        return self.BRAName


class Variant(models.Model):
    VARName = models.CharField(max_length=40)
    VARDesc = models.TextField()

    def __str__(self) -> str:
        return self.VARName
