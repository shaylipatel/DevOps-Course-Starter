class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def done_items(self):
        return [item for item in self.items if item.status == 'Done']

    @property
    def to_do_items(self):
        return [item for item in self.items if item.status == 'To Do']

    @property
    def in_progress_items(self):
        return [item for item in self.items if item.status == 'In Progress']