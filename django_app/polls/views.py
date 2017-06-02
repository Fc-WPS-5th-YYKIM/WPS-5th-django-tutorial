from django.contrib import messages
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse

from .models import Question, Choice


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
    if request.method == 'POST':
        # 전달받은 데이터중 'choice'기에 해당하는 값을
        # HttpResponse에 적절히 돌려준다
        data = request.POST
        try:
            choice_id = data['choice']

            #choice키에 해당하는 Choice 인스턴스의 vote값을 1 증가 시키고
            # 데이터 베이스에 변경사항을 반영
            choice = Choice.objects.get(id=choice_id)
            choice.votes += 1
            choice.save()
            # return HttpResponse('Choice is %s' % choice_id)

            # 이후 results페이지로 redirect
            return redirect('polls:results', question_id)
        except (KeyError, Choice.DoesNotExist):
            # message 프레임 워크를 사용하여 에러메시지 출력
            # request에 메시지를 저장해놓고 해당 request에 대한
            # response를 돌려줄 때 메시지를 담아 보낸다
            messages.add_message(
                request,
                messages.ERROR,
                "You didn't select a choice",
            )
            return redirect('polls:detail', question_id)
    else:
        return HttpResponse("You're voting")