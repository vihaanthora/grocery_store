from django.db import models

class Item(models.Model):
    name = models.CharField("item name", max_length=64, primary_key=True)
    category = models.CharField(max_length=64)
    price = models.IntegerField("item price")
    quantity_available = models.IntegerField("quantity available")

    class Meta:
        verbose_name = "item"
        verbose_name_plural = "items"
        
    def __str__(self):
        return self.name

class User(models.Model):
    phone_no = models.CharField("phone number", max_length=10, primary_key=True)
    name = models.CharField("user name", max_length=64)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return f"{self.phone_no} - {self.name}"

class Sales(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="User")
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Item")
    quantity = models.IntegerField("quantity purchased")
    date = models.DateTimeField("date of purchase", auto_now_add=True)

    class Meta:
        verbose_name = "sales"
        verbose_name_plural = "sales"

    def __str__(self):
        return f"{self.user} bought {self.quantity} of {self.item} on {self.date}"