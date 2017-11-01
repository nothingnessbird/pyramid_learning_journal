"""Default view."""

from pyramid.response import Response
from pyramid.view import view_config
import os
import io


HERE = os.path.dirname(__file__)


@view_config(route_name='home', renderer='../templates/index.html')
def list_view(request):
    """Serve all journal entries on home page."""
    path = os.path.join(HERE, '../templates/index.html')
    with io.open(path) as file:
        return Response(file.read())


@view_config(route_name='detail', renderer='../templates/detail.html')
def detail_view(request):
    """Serve detail of journal entry."""
    path = os.path.join(HERE, '../templates/detail.html')
    with io.open(path) as file:
        return Response(file.read())


@view_config(route_name='create', renderer='../templates/new.html')
def create_view(request):
    """Serve page to create new entry."""
    path = os.path.join(HERE, '../templates/new.html')
    with io.open(path) as file:
        return Response(file.read())


@view_config(route_name='edit', renderer='../templates/edit.html')
def update_view(request):
    """Serve page to edit an existing entry."""
    path = os.path.join(HERE, '../templates/edit.html')
    with io.open(path) as file:
        return Response(file.read())
