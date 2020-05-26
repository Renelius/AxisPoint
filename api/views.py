from django.shortcuts import render
from .forms import FilterDate
from django.http import HttpResponse
from .models import Items
from .serializers import ItemsSerializer
from django.http import JsonResponse
import os, xlwt
import mimetypes
import datetime
import json



def items(request):
    if request.method == 'POST':
        form=FilterDate(request.POST)
        if form.is_valid():
            date1=form.cleaned_data['date1']
            date2=form.cleaned_data['date2']
        items = Items.objects.filter(thedate__lte=date2).filter(thedate__gte=date1)
        serializer = ItemsSerializer(items, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        form=FilterDate()
        context={'form': form}
        return render(request, 'api/items.html', context)


def items_ajax(request):
    form = FilterDate()
    context = {'form': form}
    return render(request, 'api/items_ajax.html', context)


def ajax_response(request):# Для обработки AJAX запросов
    if request.method == 'GET':
        items = Items.objects.all()[:2]
        serializer = ItemsSerializer(items, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data= json.loads(request.body.decode('UTF-8'))
        date1=datetime.date(int(data['date1_year']), int(data['date1_month']), int(data['date1_day']))
        date2=datetime.date(int(data['date2_year']), int(data['date2_month']), int(data['date2_day']))
        items = Items.objects.filter(thedate__lte=date2).filter(thedate__gte=date1)
        serializer = ItemsSerializer(items, many=True)
        return JsonResponse(serializer.data, safe=False)


def send_xml(request):# отправка exel
    if request.method == 'POST':
        form = FilterDate(request.POST)
        if form.is_valid():
            date1 = form.cleaned_data['date1']
            date2 = form.cleaned_data['date2']
        items = Items.objects.filter(thedate__lte=date2).filter(thedate__gte=date1)
        attr_items=['category','from_items', 'title', 'text', 'thedate', 'id_items']
        wb = xlwt.Workbook()
        ws = wb.add_sheet('list1')
        for i in range(6):
            ws.write(1, i, f'{attr_items[i]}')
        for item in enumerate(items):
            for i in enumerate(attr_items):
                write=item[1].__dict__[attr_items[i[0]]]
                ws.write(item[0]+2, i[0], f'{write}')
        wb.save('items_exel.xls')
        fp = open('items_exel.xls', "rb")
        response = HttpResponse(fp.read())
        fp.close()
        file_type = mimetypes.guess_type('items_exel.xls')
        if file_type is None:
            file_type = 'application/octet-stream'
        response['Content-Type'] = file_type
        response['Content-Length'] = str(os.stat('items_exel.xls').st_size)
        response['Content-Disposition'] = "attachment; filename=items_exel.xls"
        return response
    else:
        form=FilterDate()
        context={'form': form}
        return render(request, 'api/send_xml.html', context)