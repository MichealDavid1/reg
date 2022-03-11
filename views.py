from django.shortcuts import render
from .models import RegInfo, Myform
from datetime import datetime, date


def get(request):
    if request.method == 'POST':
        reg_form = Myform(request.POST)
        if reg_form.is_valid():
            data = reg_form.cleaned_data
            info1 = data['sponsor_name']
            info2 = data['sponsor_address']
            info3 = data['sponsor_phone']
            info4 = data['sponsor_email']
            info5 = data['next_of_kin']
            info6 = data['next_of_kin_phone']
            info7 = data['date_of_birth']
            info8 = data['biography']
            info9 = data['name']
            info10 = data['email']
            info11 = data['phone']
            info12 = data['address1']
            info13 = data['address2']
            info14 = data['state']
            info15 = data['lga']
            reg1 = RegInfo.objects.count()
            reg1 = str(reg1 + 1)
            reg1 = list(reg1)
            a = len(reg1)
            while a < 3:
                reg1.insert(0,"0")
                a += 1
            reg1 = ''.join(reg1)
            a = date.today()
            a = a.year
            a = str(a)
            b = f'SCI{a[2:]}CSC{reg1}'
            date_of_registration = datetime.now()
            RegInfo.objects.create(
                sponsor_name=info1, sponsor_address=info2,sponsor_phone=info3, sponsor_email=info4,
                next_of_kin=info5, next_of_kin_phone=info6, date_of_birth=info7, biography=info8, name=info9,
                email=info10, phone=info11, address1=info12, address2=info13, state=info14, lga=info15,
                id_number=b, date_of_registration=date_of_registration,
            )
        return render(request, 'reg/number.html', {'id_no': [b, info9]})
    else:
        return render(request, 'reg/regpage.html', {'form': Myform})
08108984117
08089767389