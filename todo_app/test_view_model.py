import pytest

from todo_app.data.trello_items import Item
from todo_app.view_model import ViewModel


def test_view_model_done_property():
    # arrange
    items = [Item('1', 'Item 1', 'In Progress'),
             Item('2', 'Item 2', 'Done'),
             Item('3', 'Item 3', 'To Do')]
    view_model = ViewModel(items)

    # act
    returned_items = view_model.done_items

    # assert
    assert len(returned_items) == 1
    single_item = returned_items[0]
    assert single_item.status == 'Done'


def test_view_model_done_property_with_no_done_tasks():
    # arrange
    items = [Item('1', 'Item 1', 'In Progress'),
             Item('2', 'Item 2', 'To Do')]
    view_model = ViewModel(items)

    # act
    returned_items = view_model.done_items

    # assert
    assert len(returned_items) == 0
    assert returned_items == []


def test_view_model_to_do_property():
    # arrange
    items = [Item('1', 'Item 1', 'In Progress'),
             Item('2', 'Item 2', 'Done'),
             Item('3', 'Item 3', 'To Do')]
    view_model = ViewModel(items)

    # act
    returned_items = view_model.to_do_items

    # assert
    assert len(returned_items) == 1
    single_item = returned_items[0]
    assert single_item.status == 'To Do'


def test_view_model_to_do_property_with_no_to_do_items():
    # arrange
    items = [Item('1', 'Item 1', 'In Progress'),
             Item('2', 'Item 2', 'Done')]
    view_model = ViewModel(items)

    # act
    returned_items = view_model.to_do_items

    # assert
    assert len(returned_items) == 0
    assert returned_items == []


def test_view_model_in_progress_property():
    # arrange
    items = [Item('1', 'Item 1', 'In Progress'),
             Item('2', 'Item 2', 'Done'),
             Item('3', 'Item 3', 'To Do')]
    view_model = ViewModel(items)

    # act
    returned_items = view_model.in_progress_items

    # assert
    assert len(returned_items) == 1
    single_item = returned_items[0]
    assert single_item.status == 'In Progress'


def test_view_model_in_progress_property_with_no_in_progress_items():
    # arrange
    items = [Item('1', 'Item 1', 'Done'),
             Item('2', 'Item 2', 'To Do')]
    view_model = ViewModel(items)

    # act
    returned_items = view_model.in_progress_items

    # assert
    assert len(returned_items) == 0
    assert returned_items == []
