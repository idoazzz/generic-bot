import json
from typing import Optional, List

import requests

from whatsapp.consts import ACCESS_TOKEN, FROM_PHONE_NUMBER_ID


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


def dispatch_message(payload: dict):
    data: dict = {
        'messaging_product': 'whatsapp',
        'recipient_type': 'individual',
        'to': '972542214311',
        **payload
    }

    response = requests.post(
        f'https://graph.facebook.com/v13.0/{FROM_PHONE_NUMBER_ID}/messages',
        headers={
            'Authorization': ACCESS_TOKEN,
            'Content-Type': 'application/json'
        },
        data=json.dumps(data)
    )

    print(response.content)
