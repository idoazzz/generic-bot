import logging
from typing import Optional

from conversations.graph import ConversationGraph

logger: logging.Logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def simulate_conversation(graph: ConversationGraph):
    """Start to run over conversation graph."""
    current_node_name: str = graph.current_node_name
    if not graph.nodes or current_node_name not in graph.nodes:
        graph.reset()
        return

    current_choices: dict = graph.get_node_choices(current_node_name)
    choice: str = input(f'Enter next node from choices {current_choices}:')
    if choice not in current_choices:
        return
    next_node: str = current_choices[choice]

    if next_node not in graph.nodes:
        return

    graph.set_current_node(next_node)
    simulate_conversation(graph)


def apply_action(graph: ConversationGraph, choice: str) -> Optional[dict]:
    """Go to next action from current state in the conversation graph.

    :return dict. Whatsapp API message payload."""
    nodes: dict = graph.nodes
    current_node_name: str = graph.current_node_name

    if not nodes or current_node_name not in nodes:
        logging.warning(f'"{current_node_name}" not in nodes: {nodes}')
        return

    current_choices: dict = graph.get_node_choices(current_node_name)
    if choice not in current_choices:
        logging.warning(f'"{choice}" not in edges: {current_choices}')
        return

    next_node: str = current_choices[choice]
    if next_node not in nodes:
        logging.warning(f'"{next_node}" not in edges: {nodes}')
        return

    graph.set_current_node(next_node)
    return graph.get_node_payload(next_node)
