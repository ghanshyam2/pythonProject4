from django.db import models


class Patient(models.Model):
    lastName = models.CharField(max_length=150)
    firstName = models.CharField(max_length=150)
    age = models.IntegerField()

    def __str__(self):
        return self.firstName


class ClinicalData(models.Model):
    COMPONENT_NAME = [('hw','height/weight'),('bp', 'Blood Pressure'),('hr', 'Heart Rate')]
    componentName = models.CharField(max_length=166, choices=COMPONENT_NAME)
    componentValues = models.CharField(max_length=166)
    measureDateTime = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
