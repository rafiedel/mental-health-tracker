from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306245485',
        'name': 'Rafie Asadel Tarigan',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)