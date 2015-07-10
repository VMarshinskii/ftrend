from django.shortcuts import render_to_response
import xlrd

def points_sdk_view(request):
    rb = xlrd.open_workbook('/var/www/ftrend/delivery/sdek.xls', formatting_info=True)
    sheet = rb.sheet_by_index(0)
    for rownum in range(sheet.nrows):
        row = sheet.row_values(rownum)
        for c_el in row:
            print c_el
    return render_to_response("points_sdk_view.html")
