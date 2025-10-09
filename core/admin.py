from django.contrib import admin
from .models import Helmet, Reading

@admin.register(Helmet)
class HelmetAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "location")

@admin.register(Reading)
class ReadingAdmin(admin.ModelAdmin):
    list_display = ("helmet", "temp_c", "gas_ppm", "pulse_bpm", "battery_pct", "rssi_dbm", "alerts_count", "created_at")
    list_filter = ("helmet", "created_at")
