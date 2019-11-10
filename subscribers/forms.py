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


class LoginForm(forms.Form):
    email = forms.EmailField(label='email', required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=100, label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    def clean_password(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            qs = Subscriber.objects.filter(email=email).first()
            if qs == None:
                raise forms.ValidationError('Пользователя с таким е-мейлом не существует')
            elif password != qs.password:
                raise forms.ValidationError('Не верный пароль')

        return email

class SubscriberHiddenEmailForm(forms.ModelForm):
    city = forms.ModelChoiceField(label='Город', queryset=City.objects.all(),
                                  widget=forms.Select(attrs={'class': 'form-control'}))
    specialty = forms.ModelChoiceField(label='Специальность', queryset=Specialty.objects.all(),
                                       widget=forms.Select(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=100, label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.HiddenInput())
    is_active = forms.BooleanField(label='Получать рассылку?', required=False, widget=forms.CheckboxInput)

    class Meta:
        model = Subscriber
        fields = ('email', 'city', 'specialty', 'password', 'is_active',)


