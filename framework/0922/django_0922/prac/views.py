from multiprocessing import context
from django.shortcuts import render
import random

# Create your views here.

def index(request):
    
    return render(request, "index.html")


def template(request):
    
    number_list =[1, 2, 3, 4]

    context = {
        'numbers' : number_list
    }

    return render(request, "template.html", context)

def today_dinner(request):
    dinner_list = ["삼겹살", "돈까스", "떡볶이", "치킨"]
    dinner_img = ["sam", "don", "ddeok", "chi"]
    ran_num = random.randrange(0,4)

    context = {
        'dinner' : dinner_list[ran_num],
        'din_img' : dinner_img[ran_num]
    }

    return render(request, "today_dinner.html", context)

def lotto(request):
    lt_list = []
    correct_list = [3, 11, 15, 29, 35, 44, 10]
    rank_dict = {3:'5등', 4:'4등', 5:'3등', 6:'1등', 7:'1등'}
    
    for i in range(5):
        lt_list.append(random.sample(range(1, 46), 7))
        lt_list[i] = sorted(lt_list[i][0:6]) + [lt_list[i][-1]]
        cnt = len(set(lt_list[i]) & set(correct_list))
        if cnt == 6 and lt_list[i][-2] in correct_list:
            lt_list[i] += ["2등"]
        elif cnt < 3:
            lt_list[i] += ["꽝"]
        else:
            lt_list[i] += [rank_dict[cnt]]
        
        if i == 4:
            lt_list[i] = [3,11,15,29,35,10, 44]
            cnt = len(set(lt_list[i]) & set(correct_list))
            if cnt == 6 and lt_list[i][-2] in correct_list:
                lt_list[i] += ["2등"]
            elif cnt < 3:
                lt_list[i] += ["꽝"]
            else:
                lt_list[i] += [rank_dict[cnt]]

    context = {
        'res' : lt_list,
    }

    return render(request, "lotto.html", context)