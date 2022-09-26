from multiprocessing import context
from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, "index.html")


def ping(request):
    return render(request, "ping.html")


def pong(request):
    # print(request)
    # print(dir(request))
    # print(request.GET.get('ball'))
    name = request.GET.get("ball")
    context = {
        "name": name,
    }

    return render(request, "pong.html", {"name": request.GET.get("ball")})


def is_odd_even(request, oddOrEven):
    res = ""
    if oddOrEven == 0:
        res += "0 "
    elif oddOrEven % 2 == 0:
        res += "짝수"
    elif oddOrEven % 2 == 1:
        res += "홀수"

    context = {
        "isoddOrEven": oddOrEven,
        "results": res,
    }
    return render(request, "is_odd_even.html", context)


# path("number/<int:number>", views.print_number), 의 넘버와 같아야 함
def print_number(request, number):
    context = {
        "number": number,
    }

    return render(request, "print_number.html", context)


def print_text(request):
    text = request.GET.get("_text")
    # request.GET[] 과 동일 << request.GET 결과가 딕셔너리기 때문
    context = {"text": text}

    return render(request, "text.html", context)


def calculate(request, prev, next):
    context = {
        "prev": prev,
        "next": next,
    }
    return render(request, "calculate.html", context)


def my_past_life(request):
    return render(request, "my_past_life.html")


def res(request):
    my_name = request.GET.get("my_name")
    li = ["말", "돼지", "개", "소", "개구리", "토끼", "다람쥐"]
    num = random.sample(range(0, 7), 1)
    context = {
        "res": my_name,
        "life": li[num[0]],
    }
    return render(request, "res.html", context)


def input(request):
    return render(request, "input.html")


def ran_li(word, para):
    res = []
    num = [x for x in range(int(word))]
    random.shuffle(num)
    word_li = ["바나나", "짜장면", "사과", "포도", "딸기"]
    for i in num:
        res.append(word_li[i % 5])
    return res


def output(request):
    para = request.GET.get("para")
    word = request.GET.get("word")
    res_list = []
    for i in range(int(para)):
        res_list.append(ran_li(word, para))
    context = {
        "para": para,
        "word": int(word),
        "range": range(int(para)),
        "range2": range(int(word)),
        "ran_word": ran_li(word, para),
        "ran_word_li": res_list,
    }

    return render(request, "output.html", context)
