import logging

import requests
from django.shortcuts import render

logger = logging.getLogger(__name__)


def say_hello(request):
    try:

        logging.info("Calling httpbin")
        response = requests.get("https://httpbin.org/delay/2")
        logging.info("Received the response")
        data = response.json()
    except requests.ConnectionError:
        logger.critical("Httpbin is offline")
    return render(request, "hello.html", {"name": data})
