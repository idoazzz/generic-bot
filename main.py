# TODO: Write webhooks
# TODO: Support buttons
# TODO: Get few sample graphs to test the json schema.
# TODO: Add in graph CRUD DB operations.
# TODO: Tests
# TODO: Support custom end/start messages (first message is template)

import logging
from typing import List, Optional

from conversations.consts import SAMPLE_BOT
from conversations.graph import ConversationGraph
from whatsapp.utils import dispatch_message, send_text_message
from conversations.controller import simulate_conversation, apply_action

logging.basicConfig(level=logging.INFO)
logger: logging.Logger = logging.getLogger(__name__)

graph: ConversationGraph = ConversationGraph(**SAMPLE_BOT)


def simulate_whatsapp_bot_graph(target_graph: ConversationGraph, users_actions: List[str]):
    """Simulate a conversation with customer.

    users_actions is the users picked actions during the conversation. In the future we'll get those actions from
    the Webhooks endpoints.
    This function send whatsapp messages according to the bot graph.
    """
    for action in users_actions:
        payload: Optional[dict] = apply_action(target_graph, action)
        if not payload or not isinstance(payload, dict):
            illegal_choice_message: str = f'Illegal action: {action}'
            send_text_message(text=illegal_choice_message)
            logger.warning(illegal_choice_message)
            continue

        else:
            dispatch_message(payload=payload)


simulate_conversation(graph)
simulate_whatsapp_bot_graph(graph, users_actions=['1', '1', '2', '5', '5', '4', 'X'])
