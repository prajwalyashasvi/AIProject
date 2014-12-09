
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.template import context
#from django.http import HttpResponse
#import gamelogic
from gamelogic import DbFunctions
from gamelogic import AnswerGuess
from gamelogic import getCharacters


from models import CharacterSet
from models import QuestionDB

# Create your views here.

def home(request):
    request.session['Qcount'] = -1
    request.session['Characters'] = getCharacters()
    return render_to_response("indexgame.html")

'''def reset_game():
   #Kills the session.
      session.kill()
'''
def startgame(request):
    question = DbFunctions().initialQuestion() #type here code for selecting a random question
    if not 'initial_questions' in request.session :
       request.session['initial_questions'] = question
    request.session['Qcount'] += 1
    return render_to_response("qstatic.html", {'QAsk':question,'counter':request.session['Qcount']}, context_instance=RequestContext(request))
    
def guessWho(request):
   ACTIONS = (('Yes', 1),('No', -1))     
   for key,value in ACTIONS:
        if key in request.POST:
            request.session['Qcount'] += 1
            count=request.session['Qcount']
            responseString = DbFunctions().loader(value,count)
   if count > 7 :
       return render_to_response("AddCharacter.html", locals(), context_instance=RequestContext(request))
   elif responseString not in request.session['Characters']:
       return render_to_response("qstatic.html", {'QAsk':responseString,'counter':count}, context_instance=RequestContext(request))
   else :
       return render_to_response("AnswerPage.html",{'Guess':responseString,'counter':count}, context_instance=RequestContext(request))

    
def addCharacter(request):
    return render_to_response("AddCharacter.html", locals(), context_instance=RequestContext(request))

def correctGuess(request):
    return render_to_response("correctGuess.html", locals(), context_instance=RequestContext(request))
    
