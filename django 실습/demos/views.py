#views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cal

# Create your views here.


# Create your views here.
def index(request):
    return HttpResponse("안녕하세요")


def calculator(request):
    if request.method == "POST":
        # 1. 데이터 확인
        num1 = request.POST["num1"]
        num2 = request.POST["num2"]
        operators = request.POST["operators"]

        # 2. 계산
        if operators == "+":
            result = int(num1) + int(num2)
        elif operators == "-":
            result = int(num1) - int(num2)
        elif operators == "*":
            result = int(num1) * int(num2)
        elif operators == "/":
            result = int(num1) / int(num2)
        else:
            result = 0
        # 3. 객체 생성
        Cal.objects.create(
            first_num=num1,
            second_num=num2,
            operator=operators,
            result=result,
        )
        return redirect("/")
    elif request.method == "GET":
        results = Cal.objects.all()

    # 3. 응답
    return render(request, "calculator.html", {"results": results})
