from .models import Items
from django import forms

years=[]
for i in Items.objects.all():
    if i.thedate.year not in years:
        years.append(i.thedate.year)

class FilterDate(forms.Form):
    date1=forms.DateField(widget=forms.widgets.SelectDateWidget(years=years,
        empty_label=('Выберите год', 'Выберите месяц', 'Выберите число')), label='Период с')
    date2 = forms.DateField(widget=forms.widgets.SelectDateWidget(years=years,
        empty_label=('Выберите год', 'Выберите месяц', 'Выберите число')), label='по')
