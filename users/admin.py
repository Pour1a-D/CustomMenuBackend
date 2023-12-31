from django.contrib import admin
from users.models import CustomerUser, CustomerLoginCode, CustomerLoginSession


@admin.register(CustomerUser)
class CustomerUserAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "phone_number",
        "is_active",
        "created_at",
    ]

    # readonly_fields = [
    #     "phone_number",
    # ]

    list_filter = [
        "phone_number",
    ]

    search_fields = [
        "persian_name",
        "phone_number",
    ]


@admin.register(CustomerLoginCode)
class CustomerLoginCodeAdmin(admin.ModelAdmin):
    list_display = [
        "customer",
        "code",
        "failed_tries",
        "created_at",
        "updated_at",
    ]


@admin.register(CustomerLoginSession)
class CustomerLoginSessionCodeAdmin(admin.ModelAdmin):
    list_display = [
        "customer",
        "session_guid",
        "client_ip",
        "client_user_agent",
        "last_try",
        "created_at",
    ]
