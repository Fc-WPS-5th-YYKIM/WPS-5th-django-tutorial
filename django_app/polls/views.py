from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # get_list_or_404 사용 예
    # 클래스 객체와 조건을 따로 넣어줘도 되고
    latest_question_list = get_object_or_404(
        Question.objects.order_by('_pub_date')[:5]
    )

    # latest_question_list 라는 키로 위 쿼리셋을 전달
    # polls/index.html을 이용해 render한 결과를 리턴
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context=context)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist as e:
    #     raise Http404('Question does not exist')

    # question.choise_set. 와
    # Choice.objects.filter(question=question). 는 동일하다.

    # get_list_or_404 사용 예
    question = get_object_or_404(Question, pk=question_id)
    # 클래스 객체와 조건을 따로 넣어줘도 되고
    # 쿼리셋을 통째로 넣어도 된다 Question.objects.get(pk=question_id)
    context = {
        'question': question,
    }
    return render(request, 'polls/detail.html', context=context)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on qeustion %s" % question_id)
