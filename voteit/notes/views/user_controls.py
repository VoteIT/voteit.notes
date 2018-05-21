# -*- coding: utf-8 -*-
from betahaus.viewcomponent import view_action

from voteit.notes import _
from voteit.notes.interfaces import IMeetingNotesSettings


# @view_action('user_menu', 'personal_notes', title = _("Personal notes"))
# def user_profile_link(context, request, va, **kw):
#     if request.meeting is not None:
#         if IMeetingNotesSettings(request.meeting, {}).get('active', False):
#             return '<li><a href="%s">%s</a></li>' % \
#                    (request.resource_url(request.meeting, 'personal_notes_settings'),
#                     request.localizer.translate(va.title))


def includeme(config):
    config.scan(__name__)
