from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import CreateView, DeleteView, UpdateView, ListView


# Create your views here.

class PatientListView(ListView):
    model = Patient


class PatientCreateView(CreateView):
    model = Patient
    success_url = reverse_lazy('index')
    fields = ('firstName', 'lastName', 'age')


class PatientUpdateView(UpdateView):
    model = Patient
    success_url = reverse_lazy('index')
    fields = ('firstName', 'lastName', 'age')


class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('index')
    fields = ('firstName', 'lastName', 'age')


def addData(request, **kwargs):
    form = ClinicalDataForm()
    patient = Patient.objects.get(id=kwargs['pk'])
    if request.method == 'POST':
        form = ClinicalDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'clinicalApp/clinicaldata_form.html', {'form': form, 'patient': patient})


def analyze(request, **kwargs):
    data = ClinicalData.objects.filter(patient_id=kwargs['pk'])
    responseData = []
    for eachEntry in data:
        if eachEntry.componentName == 'hw':
            heightAndWeight = eachEntry.componentValues.split('/')
            if len(heightAndWeight) > 1:
                feetToMeter = float(heightAndWeight[0]) * 0.4536
                BMI = (float(heightAndWeight[1])) / (feetToMeter * feetToMeter)
                if BMI < 16:
                    print("Extreme low")
                bmiEntry = ClinicalData()
                bmiEntry.componentName = 'BMI'
                bmiEntry.componentValues = BMI
                responseData.append(bmiEntry)
        responseData.append(eachEntry)
    return render(request, 'clinicalApp/generateReport.html', {'data': responseData})
