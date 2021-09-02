from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests

@csrf_exempt
def hello(request):
    print("="*100)
    url = json.loads(request.POST["payload"])["response_url"]
    print(url)
    x = requests.post(url, data = json.dumps({"blocks":
        """
        [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "This message was replaced through slack webhook"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Sample Button",
                        "emoji": true
                    },
                    "value": "click_me_123",
                    "action_id": "button-action"
                }
            }
        ]
        """}))
    print(x.text)
    print("="*100)
    return HttpResponse("thanks")