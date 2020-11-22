from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class User(AbstractUser):
    pass


STATUS = (
    (0, "Inactive"),
    (1, "Active")
)
CATEGORY = {}


class Category(models.Model):
    #auclist = models.ForeignKey(List, on_delete=models.CASCADE, related_name="list")
    types = models.CharField(max_length=100, unique=True)

    class Meta():
        ordering = ["types"]

    def __str__(self):
        return self.types


class Bid(models.Model):
    #auclist = models.ForeignKey(List, on_delete=models.CASCADE, related_name="auclists", default="")
    title = models.CharField(max_length=200, null=False, default="")
    author = models.CharField(max_length=200, null=False, default="")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    bid_on = models.DateTimeField(default=now)

    class Meta:
        ordering = ["-price"]

        def __str__(self):
            return self.price


class List(models.Model):
    title = models.CharField(max_length=200, unique=True)
    url = models.CharField(max_length=500, unique=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="auc_list", default='')
    price = models.ForeignKey(Bid, on_delete=models.CASCADE, related_name="bids", default=0.00)
    updated_on = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="item_list", null=True)
    discription = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return "$"+self.title


class Comment(models.Model):
    auclist = models.ForeignKey(List, on_delete=models.CASCADE, related_name="comments", default="")
    name = models.CharField(max_length=80)
    # email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    # active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default="")
    item = models.ManyToManyField(List)

    def __str__(self):
        return str(self.title)
