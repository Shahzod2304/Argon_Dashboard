from django.shortcuts import render
from django.db.models import Sum
from django.http import HttpResponse
from django.db.models import Count
import pandas as pd
from .models import ExcelData, Contact





# Create your views here.
def Home(request):
    eng_katta_tulovlar = ExcelData.objects.order_by('-tulov')[:10]
    excel_data = ExcelData.objects.all()
    total_tulov = ExcelData.objects.aggregate(total_tulov=Sum('tulov'))
    total_foyda = ExcelData.objects.aggregate(total_foyda=Sum('foyda'))
    unique_company_count = ExcelData.objects.values('Company_name').distinct().count()
    return render(request, 'index.html',{'eng_katta_tulovlar':eng_katta_tulovlar, 'excel_data':excel_data, 'total_tulov':total_tulov,'total_foyda':total_foyda, 'unique_company_count':unique_company_count})



def Dashboard(request):
    eng_katta_tulovlar = ExcelData.objects.order_by('-tulov')[:10]
    excel_data = ExcelData.objects.all()
    total_tulov = ExcelData.objects.aggregate(total_tulov=Sum('tulov'))
    total_foyda = ExcelData.objects.aggregate(total_foyda=Sum('foyda'))
    unique_company_count = ExcelData.objects.values('Company_name').distinct().count()
    return render(request, 'dashboard.html',{'eng_katta_tulovlar':eng_katta_tulovlar, 'excel_data':excel_data, 'total_tulov':total_tulov,'total_foyda':total_foyda, 'unique_company_count':unique_company_count})

def Documentation(request):
    return render(request, 'documentation.html')

def Profile(request):
    return render(request, 'profile.html')


def Contact_data(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        data_contact = Contact(name=name, email=email, message=message)
        data_contact.save()
    return render(request, 'dist/index.html')



def Sign_In(request):
    return render(request, 'sign-in.html')

def Sign_Up(request):
    return render(request, 'sign-up.html')

def Tables(request):
    excel_data = ExcelData.objects.all()
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




