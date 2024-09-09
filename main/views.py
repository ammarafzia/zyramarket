from django.shortcuts import render

def show_main(request):
    context = {
        'app_store' : 'zyramarket',
        'name': 'Ammara Fasha Zia',
        'class': 'PBP B',
        'stock' : '10',
    }

    return render(request, "main.html", context)
