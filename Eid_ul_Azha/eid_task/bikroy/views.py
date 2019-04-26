from django.shortcuts import render
from .models import City,BiCategory,Product,BankAccount
from .forms import userlogin,AccountForm,ChekeBalanceForm


def city_name(request):
    city= City.objects.all()
    category= BiCategory.objects.all()

    contex = {'city_list': city,
                'category_list':category}
    return render (request,'bikroy/home.html',contex)




def post_list(request,category_name):
    all_product = Product.objects.filter(Category__Name = category_name)
    contex = {'post_list':all_product}
    return render(request,'bikroy/postlist.html',contex)


def product_list(request,location_name):
    all_product = Product.objects.filter(Location__Name = location_name)
    contex = {'post_list':all_product}
    return render(request,'bikroy/postlist.html',contex)


def post_details(request,num):
    all_post = Product.objects.get(id = num)
    contex = {'post_datels':all_post}
    return render(request,'bikroy/postdetails.html',contex)






def user_login(request):
    if request.method=='POST':
        form = userlogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
    form = userlogin()
    context = {'forms':form}
    return render(request,'bikroy/login.html',context)


def add_account(request):
    if request.method == 'POST':
        forms = AccountForm(request.POST)
        if  forms .is_valid():
            forms.save()
    forms = AccountForm()
    context = {'form':forms}
    return render(request,'bank/add_account.html',context)


def all_account(request):
    account_list = BankAccount.objects.all()
    context = {'acc_list':account_list}
    return render (request,'bank/all_account.html',context)


def cheke_blance(request):
    if request.method == 'POST':
        forms = ChekeBalanceForm(request.POST)
        if forms.is_valid():
            account = forms.cleaned_data["account_no"]
            try:
                account_obj = BankAccount,objects.get(acc_no = account)
                context = {'balance':account_obj.balance,
                            'name':account_obj.name,
                            'form':forms
                            }
                return render(request,'bank/ckekeblance.html',context)
    
            except:
                 context={'Error':"Account not found",'forms': forms}
                 return render (request,'bank/ckekeblance.html',context)
    
    forms = ChekeBalanceForm()
    context = {'form':forms}
    return render(request,'bank/ckekeblance.html',context)


    