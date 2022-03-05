from django import forms

GENDER_CHOICES = (('Male', 'Male'), ('Female', 'Female'), ('Other','Other'))
class DateInput(forms.DateInput):
    input_type = 'date'


class ClientForm(forms.Form):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class':'form-control',
               'placeholder': 'First Name', 'id':'first_name'}
    ))
    second_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class':'form-control',
               'placeholder': 'Enter Second Name', 'id':'second_name'}
    ))
    surname = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class':'form-control',
               'placeholder': 'Enter surname', 'id':'surname'}
    ))
    gender = forms.CharField(
        widget=forms.RadioSelect(
        choices=GENDER_CHOICES))

    dob = forms.DateField(label="Date of birth", widget=DateInput)
    county = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class':'form-control',
               'placeholder': 'Select County', 'id':'county'}
    ))
    sub_county = forms.CharField(label='Select Sub County', max_length=100, widget=forms.TextInput(
        attrs={'class':'form-control',
               'placeholder': 'Select Sub County', 'id':'sub_county'}
    ))
    ward = forms.CharField(label='Select Sub County', max_length=100, widget=forms.TextInput(
        attrs={'class':'form-control',
               'placeholder': 'Selects Ward', 'id':'ward'}
    ))
    national_id = forms.CharField(label='Select Sub County', max_length=100, widget=forms.TextInput(
        attrs={'class':'form-control',
               'placeholder': 'Enter National ID', 'id':'national_id'}
    ))

    ccc_number = forms.CharField(label='Select Sub County', max_length=100, widget=forms.TextInput(
        attrs={'class':'form-control',
               'placeholder': 'CCC Number', 'id':'ccc_number'}
    ))
    village = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class':'form-control',
               'placeholder': 'Enter Village', 'id':'village'}
    ))
    phone_number = forms.CharField(label='Select Sub County', max_length=100, widget=forms.TextInput(
        attrs={'class':'form-control',
               'placeholder': 'Enter Village', 'id':'phone_number'}
    ))

class SearchForm(forms.Form):
    keyword = forms.CharField(required=False, max_length=100, widget=forms.TextInput(
        attrs={'class':'form-control',
               'placeholder': 'Type Keyword to search', 'id':'keyword'}
    ))
    county = forms.CharField(required=False, max_length=100, widget=forms.TextInput(
        attrs={'class':'form-control',
               'placeholder': 'Select County', 'id':'county'}
    ))
    sub_county = forms.CharField(required=False, max_length=100, widget=forms.TextInput(
        attrs={'class':'form-control',
               'placeholder': 'Select Sub County', 'id':'sub_county'}
    ))
    ward = forms.CharField(required=False, max_length=100, widget=forms.TextInput(
        attrs={'class':'form-control',
               'placeholder': 'Selects Ward', 'id':'ward'}
    ))
    phone_number = forms.CharField(required=False, max_length=12, widget=forms.TextInput(
        attrs={'class':'form-control',
               'placeholder': 'Enter Village', 'id':'phone_number'}
    ))
    first_name = forms.CharField(required=False, max_length=100,widget=forms.TextInput(
        attrs={'class':'form-control',
               'placeholder': 'First Name', 'id':'first_name'}
    ))
    second_name = forms.CharField(required=False,max_length=100, widget=forms.TextInput(
        attrs={'class':'form-control',
               'placeholder': 'Enter Second Name', 'id':'second_name'}
    ))
    surname = forms.CharField(required=False , max_length=100, widget=forms.TextInput(
        attrs={'class':'form-control',
               'placeholder': 'Enter surname', 'id':'surname'}
    ))
    national_id = forms.CharField(required=False , max_length=100, widget=forms.TextInput(
        attrs={'class':'form-control',
               'placeholder': 'Enter National ID', 'id':'national_id'}
    ))
    facility = forms.CharField(required=False , max_length=100, widget=forms.TextInput(
        attrs={'class':'form-control',
               'placeholder': 'Enter Facility Name', 'id':'facility'}
    ))