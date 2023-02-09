from django.contrib import admin
from .models import UserAccount
from django.apps import apps

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display= ('email','is_admin',)

admin.site.register(UserAccount,UserAdmin)


app= apps.get_app_config('graphql_auth')

# Register all models in the graphql_auth app
for model_name,model in app.models.items():
    admin.site.register(model)