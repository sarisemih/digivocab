from django.apps import AppConfig

class ProfilesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "profiles"

    def read(self):
        from profiles import signals