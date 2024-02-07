from django.shortcuts import render

from django.http import HttpResponse
from django.db.models import Count
import pandas as pd
from .models import ExcelData





# Create your views here.
def Home(request):
    eng_katta_tulovlar = ExcelData.objects.order_by('-tulov')[:10]

    
    return render(request, 'index.html',{'eng_katta_tulovlar':eng_katta_tulovlar})



def Dashboard(request):
    eng_katta_tulovlar = ExcelData.objects.order_by('-tulov')[:10]

    return render(request, 'dashboard.html',{'eng_katta_tulovlar':eng_katta_tulovlar})

def Documentation(request):
    return render(request, 'documentation.html')

def Profile(request):
    return render(request, 'profile.html')



def Sign_In(request):
    return render(request, 'sign-in.html')

def Sign_Up(request):
    return render(request, 'sign-up.html')

def Tables(request):
    excel_data = ExcelData.objects.all()[:500]
    dublikat_qatorlar = ExcelData.objects.values('ID_user', 'Company_name', 'User_name', 'price', 'tulov', 'foyda', 'chiqim', 'product0', 'firma', 'foiz').annotate(Count('id')).filter(id__count__gt=1)
    
    for qator in dublikat_qatorlar:
        qatorlar = ExcelData.objects.filter(
            ID_user=qator['ID_user'],
            Company_name=qator['Company_name'],
            User_name=qator['User_name'],
            price=qator['price'],
            tulov=qator['tulov'],
            foyda=qator['foyda'],
            chiqim=qator['chiqim'],
            product0=qator['product0'],
            firma=qator['firma'],
            foiz=qator['foiz']
        )
        # Birinchi qatorni saqlab qolamiz
        birinchi_qator = qatorlar.first()
        # Qolgan barcha qatorlarni o'chiramiz
        qatorlar.exclude(pk=birinchi_qator.pk).delete()

    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        df = pd.read_excel(file)

        for index, row in df.iterrows():
            ExcelData.objects.create(
                ID_user=row['ID_user'],
                Company_name=row['Company_name'],
                User_name=row['User_name'],
                price=row['price'],
                tulov=row['tulov'],
                foyda=row['foyda'],
                chiqim=row['chiqim'],
                product0=row['product0'],
                firma=row['firma'],
                foiz=row['foiz']
            )

    return render(request, 'tables.html', {'excel_data': excel_data})




