from django.shortcuts import render,redirect
from .models import Catagory,BlogPost,Book,BankAccount
from .forms import UserLoginForm,AddBookFrom,AccountForm,ChakBalanceForm

def category_name(request):
    all_post = Catagory.objects.all()
    contex = {'category_list':all_post}
    return render(request,'blog/catagory.html',contex)





def post_list(request,id):
    all_post = BlogPost.objects.filter(category__id= id)
    print("all post",all_post)
    contex = {'post_list':all_post}
    return render(request,'blog/postlist.html',contex)



def post_details(request,num):
    all_post = BlogPost.objects.get(id = num)
    print("test",all_post)
    contex = {'post_datels':all_post}
    return render(request,'blog/postdetails.html', contex)





def user_login(request):
    if request.method=='POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
    form = UserLoginForm()
    context = {'forms':form}
    return render(request,'blog/login.html',context)


def add_book(request):
    if request.method =='POST':
        form = AddBookFrom(request.POST)
        if form.is_valid():
            book_name= form.cleaned_data['name']
            book_price = form.cleaned_data['price']

            Book.objects.create(name=book_name,price = book_price)

            return redirect('book_list')

    form = AddBookFrom()
    contxt = {'forms':form}
    return render(request,'blog/add_book.html',contxt)


def all_book(request):
    book_list = Book.objects.all()
    contex = {'book_lists':book_list}
    return render(request,'blog/book_list.html',contex)


def delete_book(request,id):
    select = Book.objects.get(id=id)
    select.delete()
    return redirect('book_list')

def edit_book(request,id):
    select = Book.objects.get(id=id)
    form = AddBookFrom (isinstance=select)
    contxt = {'forms':form}
    return render(request,'blog/edit_book.html',contxt)


def add_account(request):
    if request.method == 'POST':
        forms = AccountForm(request.POST)
        if forms.is_valid():
            forms.save()
    forms = AccountForm()
    context = {'forms':forms}
    return render(request,'account/add_account.html',context)


def all_account(request):
    account_list = BankAccount.objects.all()
    contex = {'acc_lists':account_list}
    return render(request,'account/account_list.html',contex)


def check_balance(request):
    if request.method == 'POST':
        forms = ChakBalanceForm(request.POST)
        if forms.is_valid():
            account = forms.cleaned_data["account_no"]
            try :
                account_obj = BankAccount.objects.get(acc_no = account)
                context = {'blance':account_obj.balance, 'name':account_obj.name,'forms': forms}
                return render(request,'account/checkblance.html',context)
    
            except:
                context={'Error':"Account not found",'forms': forms}
                return render(request,'account/checkblance.html',context)


    forms = ChakBalanceForm()
    context = {'forms':forms}
    return render(request,'account/checkblance.html',context)
    
