from django.shortcuts import render_to_response
from models import DeliveryCDEK
import xlrd

def points_sdk_view(request):
    rb = xlrd.open_workbook('/var/www/ftrend/delivery/sdek.xls', formatting_info=True)
    sheet = rb.sheet_by_index(0)
    for rownum in range(sheet.nrows):
        row = sheet.row_values(rownum)
        obj = DeliveryCDEK(name=row[0], code=row[1], address=row[2], phone=row[3], mail=row[4], time=row[5])
        obj.save()
        print obj.mail
    return render_to_response("points_sdk_view.html")
