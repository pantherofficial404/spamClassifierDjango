from django.views.generic import ListView,DetailView,UpdateView
from django.shortcuts import render,redirect,get_object_or_404
from . models import Articles
from .forms import requestForm
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from manage import importAlgo
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import string
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
def ArticleViews(request):
    if request.method == "POST":
        CV,NB = importAlgo()
        text = CV.transform(['Hello You have Won Lottery'])
        result = NB.predict(text)
        context = {"Prediction":result}
        return render(request,'index.html',context)
    else:    
        articles  = Articles.objects.all()
        context = {'articles':articles}
        return render(request,'index.html',context)
@login_required(login_url='/account/login/')
def ArticleDetailsViews(request,pk):
    article = Articles.objects.get(id=pk)
    context = {"articles":article}
    return render(request,'blogs.html',context)

def form(request):
    if request.method=="POST":
        form = requestForm(request.POST)
        if form.is_valid():
            new_article = Articles(title=request.POST['title'],text=request.POST['context'])
            new_article.save()  
        return redirect('articles')
    else:
        form = requestForm()
    context = {'form':form}
    return render(request,'create.html',context)


# def editForm(request,pk):
#     instance = get_object_or_404(Articles,id=pk)
#     form = requestForm(request.POST or None,instance=instance)
#     context = {'form':form}     
#     return render(request,'edit.html',context)

class editForm(UpdateView):
    model = Articles
    template_name = 'edit.html'
    fields = ["title","text"]
@login_required(login_url='/account/login/')
def passwordChange(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form':form}
    return render(request,'forgot.html',context)

def deleteForm(request,pk):
    instance = get_object_or_404(Articles,id=pk)
    instance.delete()
    return redirect('articles')

def signupView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request,user)
            print(user)
            return redirect('articles')
    else:
        form = UserCreationForm()
    context = {'form':form}
    return render(request,'signup.html',context)
