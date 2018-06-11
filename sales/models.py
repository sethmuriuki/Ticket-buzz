from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Events(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_events(self):
        self.save()

    def delete_events(self):
        self.delete()

class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Tickets(models.Model):
    buyer_name = models.CharField(max_length=40)
    venue = models.CharField(max_length=40)
    ticket_number = models.PositiveIntegerField(default=0)
    user_email = models.CharField(validators.validate_email)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    category = models.ForeignKey(Categories)
    location = models.ForeignKey(Location)
    quantity = models.PositiveIntegerField(default=0)
    time_uloaded = models.DateTimeField(auto_now_add=True, null=True)

    def save_item(self):
        self.save()

    def delete_item(self):
        self.delete()
