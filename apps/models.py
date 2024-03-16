from uuid import uuid4

from django.contrib.auth.models import User, AbstractUser
from django.db.models import Model, CharField, TextField, ForeignKey, DateTimeField, CASCADE, PositiveIntegerField, \
    ImageField, Q, UUIDField
from django_filters import FilterSet, CharFilter


class Category(Model):
    id = UUIDField(primary_key=True, default=uuid4, editable=False)
    name = CharField(max_length=100)
    description = TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Product(Model):
    id = UUIDField(primary_key=True, default=uuid4, editable=False)
    title = CharField(max_length=200)
    price = PositiveIntegerField()
    description = TextField()
    owner = ForeignKey(User, on_delete=CASCADE)
    created_at = DateTimeField(auto_now_add=True)
    category = ForeignKey(Category, on_delete=CASCADE)
    attribute1 = CharField(max_length=100)
    attribute2 = CharField(max_length=100)

    def __str__(self):
        return self.title


class ProductImage(Model):
    product = ForeignKey(Product, on_delete=CASCADE)
    image = ImageField(upload_to='product_images/')


class ProductFilter(FilterSet):
    search = CharFilter(method='filter_search')

    class Meta:
        model = Product
        fields = []

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) |
            Q(description__icontains=value)
        )