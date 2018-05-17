# -*- coding: utf-8 -*-
from BTrees.OOBTree import OOBTree
from pyramid.decorator import reify
from arche.compat import IterableUserDict
from pyramid.interfaces import IRequest
from voteit.core.models.interfaces import IMeeting
from zope.component import adapter
from zope.interface import implementer

from voteit.notes.interfaces import IMeetingNotes


@implementer(IMeetingNotes)
@adapter(IMeeting, IRequest)
class MeetingNotes(object):
    """ A multi-adapter that handles personal notes for the currently authenticated user.
        Has a dict-like interface where UID is expected to be the key.
    """
    userid = None
    data_attr = '_user_notes_data'

    def __init__(self, context, request):
        self.context = context
        self.request = request
        # To make testing or scripting easier :)
        self.userid = request.authenticated_userid

    @reify
    def data(self):
        return getattr(self.context, self.data_attr, {}).get(self.userid, {})

    def _create_storage(self):
        if self.userid is None:
            raise ValueError("Can't create storage when userid is None")
        if not hasattr(self.context, self.data_attr):
            self.context._user_notes_data = OOBTree()
        if self.userid not in self.context._user_notes_data:
            self.context._user_notes_data[self.userid] = OOBTree()
        self.data = self.context._user_notes_data[self.userid]

    def __contains__(self, uid):
        return uid in self.data

    def __getitem__(self, uid):
        if uid in self.data:
            return self.data[uid]
        raise KeyError(uid)

    def get(self, uid, default=None):
        return self.data.get(uid, default)

    def __setitem__(self, uid, item):
        if not isinstance(self.data, OOBTree):
            self._create_storage()
        self.data[uid] = item

    def __delitem__(self, uid):
        del self.data[uid]

    def clear(self):
        """ Clear data for current user, if any exist. """
        self.data.clear()

    def clear_all(self):
        """ Clear all data for ALL users. """
        getattr(self.context, self.data_attr, {}).clear()

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)


    # def __iter__(self):
    #     return iter(self.data)
    #
    # def __contains__(self, key):
    #     return key in self.data
    #
    # def get(self, key, failobj=None):
    #     if key not in self:
    #         return failobj
    #     return self[key]
    #
    # def setdefault(self, key, failobj=None):
    #     if key not in self:
    #         self[key] = failobj
    #     return self[key]
    #
    # def __repr__(self):
    #     return repr(self.data)
    #
    # def __cmp__(self, dict):
    #     return cmp(self.data, dict)
    #
    # __hash__ = None # Avoid Py3k warning
    #
    # def __len__(self):
    #     return len(self.data)
    #
    # def __getitem__(self, key):
    #     if key in self.data:
    #         return self.data[key]
    #     raise KeyError(key)
    #
    # def __setitem__(self, key, item):
    #     if not isinstance(self.data, OOBTree):
    #         self.data = self.context._user_notes_data = OOBTree()
    #     self.data[key] = item
    #
    # def __delitem__(self, key):
    #     del self.data[key]




def includeme(config):
    config.registry.registerAdapter(MeetingNotes, )