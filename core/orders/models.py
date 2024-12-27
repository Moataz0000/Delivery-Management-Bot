from django.db import models
from django.utils import timezone
class Order(models.Model):
    class OrderStatus(models.TextChoices):
        PENDING = 'PD', 'Pending'
        IN_PROGRESS = 'IP', 'In Progress'
        DELIVERED = 'DF', 'Delivered'
    user_name = models.CharField(max_length=100, unique=True, db_index=True)
    product_name = models.CharField(max_length=255, db_index=True)
    address = models.TextField(max_length=500)
    status = models.CharField(max_length=15, choices=OrderStatus.choices, default=OrderStatus.PENDING)
    created = models.DateTimeField(auto_now_add=True)
    modifiyed = models.DateTimeField(timezone.now)



    def __str__(self):
        return f'Order #{self.id} - {self.product_name} | {self.status}'