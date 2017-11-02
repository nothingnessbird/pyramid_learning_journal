"""Default view."""

from pyramid.response import Response
import os
import io


HERE = os.path.dirname(__file__)


def list_view(request):
    """Serve all journal entries on home page."""
    path = os.path.join(HERE, '../templates/index.html')
    with io.open(path) as file:
        return Response(file.read())


def detail_view(request):
    """Serve detail of journal entry."""
    path = os.path.join(HERE, '../templates/detail.html')
    with io.open(path) as file:
        return Response(file.read())


def create_view(request):
    """Serve page to create new entry."""
    path = os.path.join(HERE, '../templates/new.html')
    with io.open(path) as file:
        return Response(file.read())


def update_view(request):
    """Serve page to edit an existing entry."""
    path = os.path.join(HERE, '../templates/edit.html')
    with io.open(path) as file:
        return Response(file.read())
