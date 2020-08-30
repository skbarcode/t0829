from django.db import models
from django.contrib.auth.models import User
from mdeditor.fields import MDTextField


# from DjangoUeditor.models import UEditorField

# from rbac.models import UserInfo as RbacUserInfo


# Create your models here.


class Supplier(models.Model):  # 供应商
    name = models.CharField(max_length=64, verbose_name='供应商', unique=True)
    tel = models.CharField(max_length=256, verbose_name='优势品牌', blank=True, null=True)
    contact = models.CharField(max_length=64, verbose_name='联系人', blank=True, null=True)
    phone = models.CharField(max_length=13, verbose_name='联系手机', blank=True, null=True)
    date = models.DateField(verbose_name='更改日期', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '供应商'
        verbose_name_plural = '供应商'


class Brand(models.Model):
    name = models.CharField(max_length=24, verbose_name='品牌')
    date = models.DateField(verbose_name='更改日期', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '品牌'
        verbose_name_plural = '品牌'


class Unit(models.Model):
    name = models.CharField(max_length=12, verbose_name='单位')
    date = models.DateField(verbose_name='更改日期', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '单位'
        verbose_name_plural = '单位'


class Type(models.Model):
    name = models.CharField(max_length=12, verbose_name='分类')
    date = models.DateField(verbose_name='更改日期', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'


class Goods(models.Model):  # 货品资料
    brand = models.ForeignKey(to='Brand', verbose_name='品牌', on_delete=models.CASCADE)
    Gmodel = models.CharField(max_length=64, unique=True, verbose_name='品名规格')
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, verbose_name='单位')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='分类')
    # attribute = models.CharField(max_length=64, verbose_name='属性', blank=True, null=True)
    price = models.FloatField(verbose_name='产品进价', default=0)
    min_price = models.FloatField(verbose_name='最低售价', default=0)
    meno = models.TextField(verbose_name='备注', default='', blank=True, null=True)
    supplier = models.ForeignKey(to='Supplier', verbose_name='供应商', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='操作员', on_delete=models.CASCADE, editable=False, null=True)
    date = models.DateField(verbose_name='更改日期', auto_now=True)

    class Meta:
        verbose_name = '产品'
        verbose_name_plural = '产品信息'

    def __str__(self):
        return self.Gmodel


class Knowledge(models.Model):
    title = models.CharField(max_length=128, verbose_name='标题', blank=True, null=True)
    details = MDTextField()
    date = models.DateField(verbose_name='更改日期', auto_now=True)

    class Meta:
        verbose_name = '经验'
        verbose_name_plural = '经验'

    def __str__(self):
        return self.title


class Attribute(models.Model):
    pass
