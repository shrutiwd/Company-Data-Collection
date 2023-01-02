from django.shortcuts import render, redirect
from .forms import CompanyForm
from .models import Company
import csv
import pandas as pd
import json
# Create your views here.


def company_details(request):
    company_form = CompanyForm(request.POST or None)
    context = {"company_form": company_form}
    if request.method == "POST":
        if company_form.is_valid():
            with open('sp500_companies.csv', 'a') as file:
                writer = csv.DictWriter(
                    file, fieldnames=company_form.cleaned_data.keys(), lineterminator='\n')
                writer.writerow(company_form.cleaned_data)
            return redirect('/company-details')  
            # company_form.save()
        else:
            print("Form is invalid")
    return render(request, 'company_data\index.html', context)


def show(request):
    df = pd.read_csv("sp500_companies.csv")
    json_records = df.reset_index().to_json(orient='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
    return render(request, 'company_data\show.html', context)
