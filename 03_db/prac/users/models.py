from django.db import models

class Doctor(models.Model):
    name = models.TextField()

class Patient(models.Model):
    name = models.TextField()

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)