from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.template import loader
from django.http import Http404
from django.urls import reverse

from .models import Choice, Question


# Create your views here.
""" 
    每个视图需要做两件事：1. 返回一个包含请求页面的HttpResponse对象或者弹出一个类似Http404的异常。 2. 其他随意
"""


def index(request):
    """ 根据发布日期显示最近的五个投票问卷 """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    # return HttpResponse("Hello, World! ")
    """
        快捷方式：render
            在实际运用中，加载模板、传递参数，返回HttpResponse对象，Django提供的快捷方式
        render()函数的第一个位置参数是请求对象（就是view函数的第一个参数），第二个位置参数是模板，还有一个可选的第三参数 - 字典，包含
        需要传递给模板的数据。
        render()函数返回一个经过字典数据渲染过的模板封装而成的HttpResponse对象。
    """
    # template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list}
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist.")
    """ 快捷方式：get_object_or_404()
    get_object_or_404()方法将一个Django模型作为第一个位置参数，后面可以跟上任意个数的关键字参数，如果对象不存在则弹出Http404错误。
    ** 使用get_object_or_404()辅助函数而不自己捕获ObjectDoesNotExist异常的原因在于：减少模型层和视图层的耦合性。
    Django指导思想之一就是保证松散耦合。一些受控的耦合将会被包含在django.shortcuts模块中

    类似地，get_list_or_404()函数用来替代filter()函数，当查询列表为空时弹出404错误。
        filter是模型API中用来过滤结果的函数，它的结果是一个列表集，而get则是查询一个结果的方法，和filter是一个和多个的关系。
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    # return HttpResponse("You are looking at question %s." % question_id)


def results(request, question_id):
    response = "You are looking at the results of question %s." % question_id
    return HttpResponse(response)


def vote(request, question_id):
    # return HttpResponse("You are voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])  # 此处返回被选择选项的ID，并且值的类型为字符串。
        # request.POST是一个类似字典的对象，允许你通过键名访问提交的数据。同上可以获取GET请求发送过来的数据。
    except(KeyError, Choice.DoesNotExist):  # 若POST数据中没有提供choice键值，前面的操作就可能引发KeyError异常。
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # HttpResponseRedirect需要一个参数：重定向的URL。
        # 这里有一个建议，当你成功处理POST数据后，应当保持一个良好的习惯，始终返回一个HttpResponseRedirect。这不仅仅是对Django而言，它是一个良好的WEB开发习惯。
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))  # 此处的reverse()函数能够帮助我们避免在视图函数中硬编码URL。
