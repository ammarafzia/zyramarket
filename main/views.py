from django.shortcuts import render

def show_main(request):
    context = {
        'app_store' : 'apalah',
        'name': 'Pak Bepe',
        'class': 'PBP E',
        'stock' : '10',
    }

    return render(request, "main.html", context)
