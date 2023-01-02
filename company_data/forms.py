from django import forms
from . models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"
        widgets = {
            'exchange': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Exchange'}),
            'symbol': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Company Symbol'}),
            'short_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Company Short Name'}),
            'long_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Company Long Name'}),
            'sector': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Company Sector'}),
            'industry': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Industry'}),
            'current_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Current Price'}),
            'market_cap': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Market Cap'}),
            'ebitda': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter EBITDA'}),
            'revenue_growth': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Revenue Growth'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter City'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter State Initials'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Country'}),
            'fulltime_employees': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of Fulltime Employees'}),
            'long_business_summary': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Business Summary', "rows": 1, "cols": 20}),
            'weight': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Weight'}),
        }
