import json
import logging
from typing import Optional, List

import requests

from whatsapp.consts import ACCESS_TOKEN, FROM_PHONE_NUMBER_ID, TEST_TARGET_PHONE_NUMBER, Templates, AVAILABLE_TEMPLATES

logger: logging.Logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def generate_text_payload(body: str) -> dict:
    """Generate new text data payload for dispatching message request."""
    return {
        'type': 'text',
        'text': {
            'body': body
        }
    }


def generate_template_payload(template: str, components: Optional[List[dict]] = None) -> dict:
    """Generate new template data payload for dispatching message request.

    :param template: Name of the target template.
    :param components: Components object: https://developers.facebook.com/docs/whatsapp/cloud-api/reference/messages
    :return: dict. Data payload for dispatching a new message.
    """
    if not components:
        components = []

    return {
        'type': 'template',
        'template': {
            'name': template,
            'language': {
                'code': 'en_US'
            },
            'components': components
        }
    }


def dispatch_message(payload: dict, phone_number: str = TEST_TARGET_PHONE_NUMBER):
    data: dict = {
        'messaging_product': 'whatsapp',
        'recipient_type': 'individual',
        'to': phone_number,
        **payload
    }
    logger.info(json.dumps(data))
    response = requests.post(
        f'https://graph.facebook.com/v13.0/{FROM_PHONE_NUMBER_ID}/messages',
        headers={
            'Authorization': f'Bearer {ACCESS_TOKEN}',
            'Content-Type': 'application/json'
        },
        data=json.dumps(data)
    )

    logger.info(response.content)


def send_text_message(text: str):
    text_payload: dict = generate_text_payload(body=text)
    dispatch_message(text_payload)


def send_template_message(template: str, components: List[dict]):
    if template not in AVAILABLE_TEMPLATES:
        logging.warning(f'{template} is not valid template name: {AVAILABLE_TEMPLATES}')
        return
    template_payload: dict = generate_template_payload(template, components=components)
    dispatch_message(template_payload)
