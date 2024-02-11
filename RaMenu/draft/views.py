from django.shortcuts import render
from django.http import HttpResponse
from draft.models import UserDraft, DesireDraft, UserDesireDraft, AnswerDraft
from draft.forms import UserFormDraft, DesireFormDraft, PreferenceFormDraft, AnswerFormDraft

# Create your views here.

def index(request):
    return render(request, 'draft/indexd.html')

#def results(request):
	#context_dict = {'help_insert' : 'HELP PAGE ffs'}
	#return render(request, 'my_app/help.html', context=context_dict)

def users(request):
    users_list = UserDraft.objects.order_by("user_name")
    print(users_list)
    context_dict = {'users': users_list}
    return render(request, 'draft/users.html', context=context_dict)
    #output = ", ".join([q.user_name for q in users_list])
    #return HttpResponse(output)

def preferences(request):
    preferences_list = UserDesireDraft.objects.order_by('user_id')
    context_dict = {'preferences': preferences_list}
    return render(request, 'draft/preferences.html', context=context_dict)
    # output = ''
    # for p in preferences_list:
    #     output += p.user.user_name + ' '
    #     output += p.desire.desire_name + ' '
    #     output += str(p.answer) + ' '
    #     output += ', '
	

def usersform(request):
    form = UserFormDraft()
    if request.method == 'POST':
        form = UserFormDraft(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR form invalid')
    
    return render(request, 'draft/userform.html', context={'form': form})

def newdesire(request):
    desire = DesireFormDraft()
    if request.method == 'POST':
        desire = DesireFormDraft(request.POST)
        if desire.is_valid():
            desire.save(commit=True)
            return index(request)
        else:
            print('ERROR form invalid')
    
    return render(request, 'draft/newdesire.html', context={'desire': desire})


def survey(request):
    preference = PreferenceFormDraft()
    if request.method == 'POST':
        preference = PreferenceFormDraft(request.POST)
        if preference.is_valid():
            preference.save(commit=True)
            return index(request)
        else:
            print('ERROR form invalid')
    
    return render(request, 'draft/survey.html', context={'preference': preference})

def compatibility(request):
    preferences_list = UserDesireDraft.objects.order_by('user_id')
    #users_list = User.objects.order_by("user_name")
    context_dict = {'preferences': preferences_list}
    return render(request, 'draft/compatibility.html', context=context_dict)

def users_smb(request, user1_id, user2_id):
    preferences1_list = UserDesireDraft.objects.filter(user=user1_id)
    preferences2_list = UserDesireDraft.objects.filter(user=user2_id)
    #users = User.objects.order_by('user_name')
    #for usr in users:
        #if usr.user_name == 'Sasha':
            #break
    #preferences_sasha = UserPreference.objects.filter(user=usr)

    user1 = UserDraft.objects.get(pk=user1_id)
    user2 = UserDraft.objects.get(pk=user2_id)
    context_dict = {'preferences1':preferences1_list, 'preferences2':preferences2_list}
    context_dict['user1'] = user1
    context_dict['user2'] = user2
    return render(request, 'draft/compatibility.html', context=context_dict)

def newanswer(request):
    desires_list = DesireDraft.objects.order_by("desire_name")
    # for every desire make an input for answer
    # save it to the model
    if request.method == 'POST':
        #answer = AnswerForm()
        temp = request.POST
        print('submitted?')
        for desire in desires_list:
            print(desire.desire_name,temp[desire.desire_name])
        return index(request)
    else:
        pass
        #return index(request)
    return render(request, 'draft/newanswer.html', context={'desires': desires_list})


    #     user_form = UserForm(data=request.POST)
    #     profile_form = ProfileForm(data=request.POST)

    #     if user_form.is_valid() and profile_form.is_valid():

    #         user = user_form.save()
    #         # hashing the password
    #         user.set_password(user.password)
    #         user.save()

    #         profile = profile_form.save(commit=False)
    #         profile.user = user

    #         if 'profile_pic' in request.FILES:
    #             profile.profile_pic = request.FILES['profile_pic']
    #         profile.save()

    #         registered = True

    #     else:
    #         print(user_form.errors, profile_form.errors)

    # else:
    #     user_form = UserForm()
    #     profile_form = ProfileForm()

    # context = {'user_form':user_form, 'profile_form':profile_form, 'registered':registered}
    # return render(request, 'user_app/registration.html', context=context)

    # answer = AnswerForm()
    # if request.method == 'POST':
    #     answer = AnswerForm(request.POST)
    #     if answer.is_valid():
    #         answer.save(commit=True)
    #         return index(request)
    #     else:
    #         print('ERROR form invalid')
    # 'answer': answer,
    
    