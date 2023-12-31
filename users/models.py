import uuid
from django.db import models


class CustomerUser(models.Model):
    first_name = models.CharField(max_length=32, null=True)
    last_name = models.CharField(max_length=32, null=True)

    details = models.CharField(max_length=255, blank=True, null=True)

    phone_number = models.CharField(max_length=11, unique=True)
    is_active = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name


class CustomerLoginCode(models.Model):
    customer = models.OneToOneField(CustomerUser, on_delete=models.CASCADE)
    code = models.PositiveIntegerField(null=True)
    failed_tries = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CustomerLoginSession(models.Model):
    customer = models.ForeignKey(
        CustomerUser, on_delete=models.CASCADE, related_name="sessions"
    )
    session_guid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    last_try = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    client_ip = models.CharField(max_length=255)
    client_user_agent = models.CharField(max_length=255)
