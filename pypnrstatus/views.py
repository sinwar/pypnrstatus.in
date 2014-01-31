from django.conf import settings
if not settings.configured:
    settings.configure()

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from pypnrstatus.models import PNRNotification
from pypnrstatus.pnr_utils import get_and_schedule_pnr_notification, caluclate_next_schedule_time
import datetime

def index(request):
    if request.method == "POST":
        pnr_no = request.POST.get('pnrno')
        notification_type = request.POST.get('notification_type')
        notification_type_value = request.POST.get('email_or_phone')
        notification_frequency = request.POST.get('notification_frequency')
        notification_frequency_value = request.POST.get('notifyValue')

        timenow = datetime.datetime.now()

        next_schedule_time = caluclate_next_schedule_time(timenow,
                notification_frequency,
                notification_frequency_value)

        pnr_notify = PNRNotification.objects.create( pnr_no=pnr_no, notification_type=notification_type,
            notification_type_value=notification_type_value, notification_frequency=notification_frequency,
            notification_frequency_value=notification_frequency_value, next_schedule_time=next_schedule_time )

        pnr_status = get_and_schedule_pnr_notification(pnr_notify)
        return render(request, 'pnr_status.html', pnr_status)
    else:
        return render(request, 'index.html')
