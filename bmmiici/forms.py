from django.forms import ModelForm
from django.forms.widgets import Select
from bmmiici.models import Doctor, Specialization, DoctorSpecialization, Patient

class DoctorForm(ModelForm):
    class Meta:
        CHOICES = Specialization.objects.all()
        model = Doctor
        fields = '__all__'
        widgets = {
            'specializations': Select(choices=( (x.id, x.name) for x in CHOICES )),
        }

class SpecializationForm(ModelForm):
    class Meta:
        model = Specialization
        fields = '__all__'

class DoctorSpecializationForm(ModelForm):
    class Meta:
        model = DoctorSpecialization
        fields = '__all__'
        
class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'