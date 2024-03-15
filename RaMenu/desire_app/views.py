from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from desire_app.models import Desire, Category
from desire_app.forms import DesireForm, CategoryForm, DesiresForm
from django.urls import reverse

# Create your views here.

def newcategory(request):
    category = CategoryForm()
    if request.method == 'POST':
        category = CategoryForm(request.POST)
        if category.is_valid():
            if Category.objects.filter(category_name=category.data.get('category_name')).exists():
                return HttpResponseRedirect(reverse('desire_app:category_exists'))
            else:
                category.save(commit=True)
                id = category.instance.id
                return HttpResponseRedirect(reverse('desire_app:newdesirelist', kwargs={'category_id':id}))
        else:
            print('ERROR form invalid')
    context={'category': category}
    return render(request, 'desire_app/newcategory.html', context )

def category_exists(request):
    return render(request, 'desire_app/category_exists.html')

def newdesire(request):
    desire = DesireForm()
    if request.method == 'POST':
        desire = DesireForm(request.POST)
        if desire.is_valid():
            desire.save(commit=True)
            return HttpResponseRedirect(reverse('index'))
        else:
            print('ERROR form invalid')
    context={'desire': desire}
    return render(request, 'desire_app/newdesire.html', context )

def newdesirelist(request, category_id):
    category = Category.objects.get(pk=category_id)
    desires = []
    if request.method == 'POST':
        temp = request.POST['desires']
        desires = temp.split('\n')
        # create new records for all desires
        for desire in desires: 
            desire = desire.replace('\r', '')
            new_desire = Desire()
            new_desire.desire_name = desire
            new_desire.category = category
            new_desire.save()
        
        return HttpResponseRedirect(reverse('index'))
    else:
        print('ERROR form invalid')
    context={'desires': desires, 'category' : category}
    return render(request, 'desire_app/newdesirelist.html', context )


    # desires_data = DesiresForm(initial={"category": category})
    # if request.method == 'POST':
    #     desires_data = DesiresForm(request.POST)
    #     print(desires_data)
    #     if desires_data.is_valid():
    #         desires_data.save(commit=False)
    #         desires_data = desires_list.cleaned_data['desires_list']
    #         desires_list = desires_data.splitline()
    #         for desire in desires_list:
    #             new_desire = Desire()
    #             new_desire.desire_name = desire['desire_name']
    #             new_desire.category = category
    #             new_desire.save(commit=True)
            

def categories(request):
    categories = list(Category.objects.all())
    desires = Desire.objects.all
    context = {'categories':categories, 'desires':desires}
    #print(users_list)
    #context_dict = {'users': users_list}
    return render(request, 'desire_app/categories.html', context)
    #output = ", ".join([q.user_name for q in users_list])
    #return HttpResponse(output)

def category_list(request, category_id):
    category = Category.objects.get(pk=category_id)
    desires_list = Desire.objects.filter(category=category_id)
    context = {'category': category, 'desires': desires_list}
    return render(request, 'desire_app/category_list.html', context)

    #user1 = UserDraft.objects.get(pk=user1_id)