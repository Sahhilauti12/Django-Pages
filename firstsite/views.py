from django.http import HttpResponse


def home(request):
    return HttpResponse(" <a href='page1/'>Page1</a> | <a href='page2/'>Page2</a> | <a href='page3/'>Page3</a> | <a href='page4/'>Page4</a> <body bgcolor='yellow'><center><h1><b>Home Page</b></h1></center></body>")

def page1(request):
    return HttpResponse("<a href='/'>Home Page</a>  <body bgcolor='yellow'><center><h1><b>Page 1</b></h1></center></body>")

def page2(request):
    return HttpResponse("<a href='/'>Home Page</a> <body bgcolor='yellow'><center><h1><b>Page 2</b></h1></center></body>")

def page3(request):
    return HttpResponse("<a href='/'>Home page</a> <body bgcolor='yellow'><center><h1><b>Page 3</b></h1></center></body>")

def page4(request):
    return HttpResponse("<a href='/'>Home Page</a> <body bgcolor='yellow'><center><h1><b>Page 4</b></h1></center></body>")