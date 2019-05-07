from django.shortcuts import render, redirect
import first.views as first_view

def main(request):
    return render(request, 'main.html')
    # ->가져와서 출력해라
    
 

    
