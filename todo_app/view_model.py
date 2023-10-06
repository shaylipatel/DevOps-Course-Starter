class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def done_items(self):
        done_list = []
        for item in self.items:
            if item.status == 'Done':
                done_list.append(item)
        return done_list

    @property
    def to_do_items(self):
        to_do_list = []
        for item in self.items:
            if item.status == 'To Do':
                to_do_list.append(item)
        return to_do_list

    @property
    def in_progress_items(self):
        in_progress_list = []
        for item in self.items:
            if item.status == 'In Progress':
                in_progress_list.append(item)
        return in_progress_list
