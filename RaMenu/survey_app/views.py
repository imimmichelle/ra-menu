from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from desire_app.models import Desire, Category
from survey_app.models import Preference
from django.urls import reverse
import random
import string


# Create your views here.

def generate_string(length):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))

def newsurvey(request):
    category_list = Category.objects.all()
    if request.method == 'POST':
        temp = request.POST
        category = Category.objects.get(category_name=temp['category'])
        id = category.pk
        code = str(id) + '-' + generate_string(8)

        # check that the code is new
        for i in range(100):
            if Preference.objects.filter(code=code).exists():
                code = str(id) + '-' + generate_string(8)
        if Preference.objects.filter(code=code).exists():
            return HttpResponse("Unknown error with code")

        return HttpResponseRedirect(reverse('survey_app:survey', kwargs={'code':code}))

    context = {'category':category_list}
    return render(request, 'survey_app/newsurvey.html', context)



def entercode(request):
    if request.method == 'POST':
        temp = request.POST
        code = temp['code']
        # check if code exists and is used only once
        if not Preference.objects.filter(code=code).exists():
            return HttpResponseRedirect(reverse('survey_app:code_not_exists'))
        else:
            preferences = Preference.objects.filter(code=code)
            user_set = set()
            for p in preferences:
                user_set.add(p.user)
            if len(user_set) > 2:
                return HttpResponseRedirect(reverse('survey_app:wrong_code'))
            else:
                return HttpResponseRedirect(reverse('survey_app:survey', kwargs={'code':code}))
            
    return render(request, 'survey_app/entercode.html')
    
def code_not_exists(request):
    return render(request, 'survey_app/code_not_exists.html')

def survey(request, code):
    code_list = code.split('-')
    category_id = code_list[0]
    category = Category.objects.get(pk=category_id)
    # create survey form with: category prefilled, user prefilled, list of desires
    desires = Desire.objects.filter(category=category_id)
    if request.method == 'POST':
        temp = request.POST
        user_id = request.user.id

        # check if the user already answered. Delete old record if exists
        if Preference.objects.filter(code=code, user=request.user).exists():
            Preference.objects.filter(code=code, user=request.user).delete()

        # create new records for all desires
        for desire in desires: 
            preference = Preference()
            preference.code = code
            preference.user = User.objects.get(pk=user_id)
            preference.desire = desire
            preference.answer = temp[desire.desire_name]
            preference.save()

        return HttpResponseRedirect(reverse('survey_app:results', kwargs={'code':code}))
    
    context = {'category': category, 'desires':desires}
    return render(request, 'survey_app/survey.html', context)

def results(request, code):
    # if only one with code - wait
    # if both - see results
    
    preferences = Preference.objects.filter(code=code)
    print(preferences)
    users = [p.user for p in preferences]
    users = set(users)
    users = list(users)

    # check availability for this user
    if request.user not in users:
        return HttpResponse('Page not available to you')
    
    code_list = code.split('-')
    category_id = code_list[0]
    category = Category.objects.get(pk=category_id)
    desires = Desire.objects.filter(category=category_id)

    context = {'category':category, 'desires':desires, 'preferences':preferences, 'users':users}

    if len(users) > 2:
        # TOTHINK maybe it's okay to have more than two users? - later
        return HttpResponseRedirect(reverse('survey_app:wrong_code'))
   
    context['user1'] = users[0]
    context['user2'] = users[1] if len(users)>1 else None

    return render(request, 'survey_app/results.html', context)

def wrong_code(request):
    return render(request, 'survey_app/wrong_code.html')

def resultlist(request):
    preferences = Preference.objects.filter(user = request.user)
    all_preferences = Preference.objects.all()
    codes = [p.code for p in preferences]
    codes = set(codes)
    codes = list(codes)

    context = {'preferences':preferences, 'codes':codes, 'all_preferences':all_preferences}
    return render(request, 'survey_app/resultlist.html', context)