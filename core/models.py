from django.db import models

class Helmet(models.Model):
    name = models.CharField(max_length=50, unique=True)      # p.ej. "Casco 1"
    location = models.CharField(max_length=120, blank=True)  # p.ej. "Zona Norte – Frente 12"

    def __str__(self):
        return self.name

class Reading(models.Model):
    helmet = models.ForeignKey(Helmet, on_delete=models.CASCADE, related_name="readings")
    temp_c = models.DecimalField(max_digits=5, decimal_places=1)
    gas_ppm = models.IntegerField()
    pulse_bpm = models.IntegerField()
    battery_pct = models.IntegerField()
    rssi_dbm = models.IntegerField()
    alerts_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]  # la primera es la más reciente
