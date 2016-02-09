from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView

from polls.models import Choice, Question

# Add logging
import logging
logger = logging.getLogger(__name__)

class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]
    
    
class DetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'
    

class ResultsView(DetailView):
    model = Question
    template_name = 'polls/results.html'

    
#--- Function-based View
def vote(request, question_id):
    logger.debug("vote().question_id: %s" % question_id)
    p = get_object_or_404(Question, pk=question_id)
    
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Re-show the polls Form
        return render(request, 'polls/detail.html', {
                'question': p,
                'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Success POST's Data Procedure
        # To return HttpResponseRedirect, and procedure Redirect
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))