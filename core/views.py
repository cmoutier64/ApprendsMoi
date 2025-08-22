from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone

def index(request):
    return render(request,'index.html')

def pricing(request):
    return render(request,'pricing.html')

def meeting(request):
    return render(request,'meeting.html',{'room_slug':'demo'})

def calendar_view(request):
    return render(request,'calendar.html')

def calendar_feed(request):
    now = timezone.now()
    events=[]
    for i in range(3):
        start=(now+timezone.timedelta(days=i+1)).replace(hour=10,minute=0,second=0,microsecond=0)
        end=start+timezone.timedelta(hours=1)
        events.append({'id':i+1,'title':f'Créneau {i+1}','start':start.isoformat(),'end':end.isoformat()})
    return JsonResponse(events, safe=False)
