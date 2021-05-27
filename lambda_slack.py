# -*- coding: utf-8 -*-
###############################################################################
#                   Call lambda_handler_() to test                            #
###############################################################################


import json
import logging
import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()

# ===================== Log Configuration ===================== #
LOG_FORMAT = '{levelname}:{name}:{funcName}:{message}'
LOG_STYLE = '{'
logging.basicConfig(format=LOG_FORMAT, style=LOG_STYLE)
logger = logging.getLogger('my-first-aws-lambda')
logger.setLevel(logging.DEBUG)

# ==== Enviroment variables
SLACK_URL_WEBHOOK = os.getenv('SLACK_URL_WEB_HOOK', '')

def send_slack_hook():
    try:
        logger.info("sending slack webhook...")
        slack_msg = {'text': 'We are testing AWS Lambda with slack webhook'}
        r = requests.post(SLACK_URL_WEBHOOK, json=slack_msg)
    except Exception as e:
        logger.error(f"Exception ocurred: {e}", exc_info=True)


def lambda_handler(event=None, context=None):
    send_slack_hook()
