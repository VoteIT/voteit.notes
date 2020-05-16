# -*- coding: utf-8 -*-
from arche.views.base import BaseForm
from pyramid.decorator import reify
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from voteit.core.models.interfaces import IMeeting
from voteit.core.security import MODERATE_MEETING
from voteit.core.views.control_panel import control_panel_category
from voteit.core.views.control_panel import control_panel_link

from voteit.notes.interfaces import IMeetingNotesSettings
from voteit.notes import _


@view_config(context=IMeeting, name='proposal_notes_settings',
             permission=MODERATE_MEETING, renderer='arche:templates/form.pt')
class NotesSettingsForm(BaseForm):
    type_name = 'Notes'
    schema_name = 'settings'

    @reify
    def settings(self):
        return IMeetingNotesSettings(self.context)

    def appstruct(self):
        return dict(self.settings)

    def save_success(self, appstruct):
        self.settings.update(appstruct)
        self.flash_messages.add(self.default_success, type="success")
        return HTTPFound(location=self.request.resource_url(self.context))


def check_notes_enabled(context, request, va):
    return request.personal_notes_enabled


def includeme(config):
    config.scan(__name__)
    config.add_view_action(
        control_panel_category,
        'control_panel', 'personal_notes',
        panel_group='control_panel_personal_notes',
        title=_("Personal notes"),
        description=_(
            "control_panel_personal_notes_description",
            default="Allows users to annotate proposals with personal notes and a "
                    "preference on how they wish to vote later on."
        ),
        check_active=check_notes_enabled,
    )
    config.add_view_action(
        control_panel_link,
        'control_panel_personal_notes', 'settings',
        title=_("Settings"), view_name='proposal_notes_settings'
    )
