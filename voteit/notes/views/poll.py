# -*- coding: utf-8 -*-
from arche.views.base import BaseView
from pyramid.decorator import reify
from pyramid.view import view_config
from voteit.core.models.interfaces import IPoll
from voteit.core.security import ADD_VOTE

from voteit.notes.interfaces import IMeetingNotes
from voteit.notes.schemas import STATE_ICONS_CLS
from voteit.notes.schemas import STATE_TXT_CLS


@view_config(context=IPoll,
             name="personal_notes_for_poll",
             permission=ADD_VOTE,
             renderer='voteit.notes:templates/personal_notes_for_poll.pt')
class NotesForPollView(BaseView):

    @reify
    def notes(self):
        return self.request.registry.getMultiAdapter((self.request.meeting, self.request), IMeetingNotes)

    def __call__(self):
        results = []
        for prop in self.context.get_proposal_objects():
            note = self.notes.get(prop.uid, None)
            if note:
                item = {'note': note, 'uid': prop.uid}
                if prop is not None:
                    item['prop'] = prop
                results.append(item)
        return {'results': results}

    def get_ptag(self, item, default=''):
        propose = item['note'].get('propose', default)
        if propose:
            return """<span class="%s %s"></span>&nbsp;""" % \
                   (STATE_ICONS_CLS.get(propose, STATE_ICONS_CLS['']),
                    STATE_TXT_CLS.get(propose, STATE_TXT_CLS['']),)
        return default

    def get_txt(self, item, default=''):
        txt = item['note'].get('notes', default)
        if txt:
            return self.request.transform_text(txt)
        return default


def includeme(config):
    config.scan(__name__)
