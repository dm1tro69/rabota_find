from django import forms
from subscribers.models import Subscriber, City, Specialty

class SubscriberModelForm(forms.ModelForm):
    email = forms.EmailField(label='email', required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    city = forms.ModelChoiceField(label='Город', queryset=City.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    specialty = forms.ModelChoiceField(label='Специальность', queryset=Specialty.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=100, label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Subscriber
        fields = ('email', 'city', 'specialty', 'password')
        exclude = ('is_active',)