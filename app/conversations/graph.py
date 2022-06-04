import dataclasses


@dataclasses.dataclass
class ConversationGraph:
    def __init__(self, customer: dict, root: str, nodes: dict, current_node: str = None):
        self.root = root
        self.nodes = nodes
        self.customer = customer
        self.__current_node_name = None
        self.set_current_node(current_node)

    @property
    def current_node_name(self) -> str:
        return self.__current_node_name or self.root

    @property
    def current_node(self) -> dict:
        return self.nodes.get(self.current_node_name, {})

    def reset(self):
        self.set_current_node(node_name=self.root)

    def set_current_node(self, node_name: str):
        if node_name not in self.nodes:
            self.__current_node_name = self.root
            return
        self.__current_node_name = node_name

    def get_node_payload(self, node_name: str):
        node: dict = self.nodes.get(node_name)
        if not node:
            return

        node_payload: dict = node.copy()
        node_payload.pop('metadata')
        return node_payload

    def get_node_choices(self, node_name: str):
        node_name: dict = self.nodes.get(node_name)
        if not node_name:
            return

        return node_name.get('metadata', {}).get('choices').copy()
