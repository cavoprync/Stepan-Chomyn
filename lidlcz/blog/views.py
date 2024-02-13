from django.shortcuts import render

from django.http import HttpResponse
import  random

def models_list(request):
    counter = 1
    while True:
        random_n = random.randint(1, 100)
        if counter % 5 == 0 and random_n % 2 == 1:
            random_n += 1  # Zvýšíme liché číslo o 1, aby bylo sudé
        counter += 1
        return HttpResponse(f"Testing of views {random_n}")


