from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align: center">术士之战</h1>'
    line4 = '<a href="/play/">进入游戏界面</a>'
    line3 = '<hr>'
    line2 = '<img src="https://img0.baidu.com/it/u=2896101387,78902208&fm=253&fmt=auto&app=138&f=PNG?w=480&h=270" width=1200>'
    return HttpResponse(line1 + line4 + line3 + line2)

def play(request):
    line1 = '<h1 style="text-align: center">游戏界面</h1>'
    line3 = '<a href="/">返回主页面</a>'
    line2 = '<img src="https://img1.baidu.com/it/u=954823891,2849422542&fm=253&fmt=auto&app=138&f=JPEG?w=464&h=640" width=1200>'
    return HttpResponse(line1 + line3 + line2)
