from django.db import models
from django.contrib.auth.models import AbstractUser

# MVT: Model
class CustomUser(AbstractUser):
    """
    Custom User model to extend Django's default user, allowing for
    different user types and an admin approval flag.
    """
    USER_TYPE_CHOICES = (
        ("Chairman", "Chairman"),
        ("Member", "Member"),
        ("Watchman", "Watchman"),
        ("Visitor", "Visitor"),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default="Member")
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Member(models.Model):
    """
    Model for a society member. Uses a one-to-one relationship with CustomUser
    for database normalization.
    """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    flat_number = models.CharField(max_length=10, null=True, blank=True)
    
    def __str__(self):
        return f"Member: {self.user.username}"

class Watchman(models.Model):
    """
    Model for a society watchman.
    """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"Watchman: {self.user.username}"

class Notice(models.Model):
    """
    Model for society notices.
    """
    subject = models.CharField(max_length=200)
    description = models.TextField()
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.subject

class Event(models.Model):
    """
    Model for society events.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Visitor(models.Model):
    """
    Model for visitors.
    """
    name = models.CharField(max_length=100)
    flat_number = models.CharField(max_length=10)
    entry_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True, blank=True)
    watchman = models.ForeignKey(Watchman, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} visiting flat {self.flat_number}"

class Transaction(models.Model):
    """
    Model for transactions (e.g., maintenance fees).
    """
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction for {self.member.user.username} - {self.amount}"