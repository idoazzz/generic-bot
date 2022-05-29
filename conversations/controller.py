from conversations.graph import ConversationGraph


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


def get_next_action(graph: ConversationGraph):
    """Start to run over conversation graph."""
    current_node_name: str = graph.current_node_name
    if not graph.nodes or current_node_name not in graph.nodes:
        return

    current_choices: dict = graph.get_node_choices(current_node_name)
    choice: str = input(f'Enter next node from choices {current_choices}:')
    if choice not in current_choices:
        return

    next_node: str = current_choices[choice]
    if next_node not in graph.nodes:
        return

    graph.set_current_node(next_node)