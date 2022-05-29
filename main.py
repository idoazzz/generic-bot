# TODO: Change the schema to hold metadata, the rest of the properties will be as FB API demands.
# TODO: Copy everything we return from methods (mutable).
# TODO: Get few sample graphs to test the json schema.
# TODO: Add in graph CRUD DB operations.
# TODO: Support custom end/start messages (first message is template)
from typing import List

from conversations.consts import SAMPLE_BOT
from conversations.controller import simulate_conversation
from conversations.graph import ConversationGraph
from whatsapp.consts import Templates
from whatsapp.utils import generate_template_payload, generate_text_payload


simulate_conversation(ConversationGraph(**SAMPLE_BOT))


components: List[dict] = [
    {
        'type': 'body', 'parameters': [{'type': 'text', 'text': 'ido'}]
    }
]

template_payload: dict = generate_template_payload(Templates.Order, components=components)
# dispatch_message(template_payload)

text_payload: dict = generate_text_payload(body='ido')
# dispatch_message(text_payload)
