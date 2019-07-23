from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, Http404

from django.template import loader

from .models import Question
# from datetime import datetime

# Create your views here.

# index #1
# def index(request):
# 	latest_question_list = Question.objects.order_by('-pub_date')[:5]
# 	output = ', '.join([q.question_text for q in latest_question_list])
# 	return HttpResponse(output)

# index #2
# def index(request):
# 	latest_question_list = Question.objects.order_by('-pub_date')[:5]
# 	template = loader.get_template('polls/index.html')
# 	context = {
# 		'latest_question_list': latest_question_list,
# 	}
# 	return HttpResponse(template.render(context, request))

# index #3
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request,'polls/index.html',context)

# def index(request, nama = "", umur = ""):
# 	return HttpResponse("Hello World, %s <br/> Nama %s <br/> Umur %s" %(
# 			request.path,
# 			nama,
# 			str(umur)
# 		))

# def time(request):
# 	now = datetime.now()
# 	return HttpResponse("Waktu Sekarang Adalah %s" % now)

# detail #1
# def detail(request, question_id):
# 	return HttpResponse("You're looking at question %s." % question_id)

# detail #2
# def detail(request, question_id):
# 	try:
# 		question = Question.objects.get(pk=question_id)
# 	except Question.DoesNotExist:
# 		raise Http404("Question does not exist")
# 	return render(request,'polls/detail.html',{'question':question})

# detail #3
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)				