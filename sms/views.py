from django.shortcuts import render
from django.contrib import messages
from .utils import send_sms, is_valid_phone_number

def send_sms_view(request):
    if request.method == "POST":
        to_number = request.POST.get("to")
        message = request.POST.get("message")

        # Validate input
        if not to_number or not message:
            messages.error(request, "Both 'to' and 'message' are required.")
            return render(request, "sms/send_sms.html")
        
        if not is_valid_phone_number(to_number):
            messages.error(request, "Invalid phone number format. Use international format (e.g., +639123456789).")
            return render(request, "sms/send_sms.html")
        
        # Send SMS
        success, response_message = send_sms(to_number, message)
        
        if success:
            messages.success(request, response_message)
        else:
            messages.error(request, response_message)

    return render(request, "sms/send_sms.html")
