from django.db import models

# Create your models here.

# Categories - maybe not needed

class AnswerDraft(models.Model):
    #desire = models.ForeignKey(Desire, on_delete=models.CASCADE, default='unknown')
    answer = models.CharField(max_length=64)

# Desires
class DesireDraft(models.Model):
    desire_name = models.CharField(max_length=264)
    category = models.CharField(max_length=128)
    #answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return self.desire_name
    


#class Survey(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    #desire = models.ForeignKey(Desire, on_delete=models.CASCADE)
    #answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

class UserDraft(models.Model):
    user_name = models.CharField(max_length=128)
    desires = models.ManyToManyField(DesireDraft, through='UserDesireDraft')
    
    def __str__(self):
        return self.user_name

# Users preferences
class UserDesireDraft(models.Model):
    # create fields for desires - many to many relationship
    # fields user, desire, answer
    # in the future not boolean
    user = models.ForeignKey(UserDraft, on_delete=models.CASCADE)
    desire = models.ForeignKey(DesireDraft, on_delete=models.CASCADE)
    #answer = models.CharField(max_length=64, default='unknown')


# class AtomicPreferenceTwoUsers(models.Model):
#     user_from = models.ForeignKey(User, on_delete=models.CASCADE)
#     user_to = models.ForeignKey(User, on_delete=models.CASCADE)
#     desire = models.ForeignKey(Desire, on_delete=models.CASCADE)
#     answer = models.CharField(max_length=64)




'''class Compatibility(models.Model):
    # combined preferences of two users
    # fields user1, user2, desire, answer1, answer2, result
    user1 = models.ForeignKey(User, on_delete=models.CASCADE)
    #user2 = models.ForeignKey(User, on_delete=models.CASCADE)
    desire = models.ForeignKey(Desire, on_delete=models.CASCADE)
    #answer1 = models.BooleanField()
    #answer2 = models.BooleanField()
    answer = models.BooleanField()
    '''
    





