from django.forms import ModelForm
from bmmiici.models import Doctor, Specialization, DoctorSpecialization, Patient

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

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