# -*- coding: utf-8 -*-
from pyramid.interfaces import IDict
from zope.interface import Attribute
from zope.interface import Interface


class IMeetingNotes(Interface):
    data = Attribute("Storage")
    context = Attribute("Adapted meeting")
    request = Attribute("Adapted request")
    data_attr = Attribute("Which attribute data is stored on in context")

    def __init__(context, request):
        """ Wraps meeting and request. """

    def clear_all():
        """ Clear all data for ALL users. """

    # Regular dict-like api
    def __contains__(uid):
        pass

    def __getitem__(uid):
        pass

    def get(uid, default=None):
        pass

    def __setitem__(uid, item):
        pass

    def __delitem__(uid):
        pass

    def clear():
        """ Clear for current user"""

    def __iter__():
        pass

    def __len__():
        pass


class IMeetingNotesSettings(IDict):
    """ Per-meeting settings. """

