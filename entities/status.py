# TODO: What is this class for?
# TODO: This feels like a duplicate of Confirmation. Revisit and potentially consolidate
class Status:
    def __init__(self, order_id: str, status_type: str):
        self.order_id = order_id
        self.status_type = status_type