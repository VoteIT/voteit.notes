""" Fanstatic lib"""
from arche.interfaces import IBaseView
from arche.interfaces import IViewInitializedEvent
from fanstatic import Library
from fanstatic import Resource

from voteit.core.fanstaticlib import voteit_main_css
from voteit.core.fanstaticlib import base_js

voteit_notes_lib = Library('voteit_notes_lib', 'static')

notes_scripts = Resource(voteit_notes_lib, 'scripts.js', depends=(base_js,))


def include_resources(view, event):
    if view.request.meeting:
        notes_scripts.need()


def includeme(config):
    config.add_subscriber(include_resources, [IBaseView, IViewInitializedEvent])
