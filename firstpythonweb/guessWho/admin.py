from django.contrib import admin
from guessWho.models import CharacterSet
from guessWho.models import QuestionDB
from guessWho.models import Attributevalue
from guessWho.models import questionLog
# Register your models here.
admin.site.register(CharacterSet)
admin.site.register(QuestionDB)
admin.site.register(Attributevalue)
admin.site.register(questionLog)
