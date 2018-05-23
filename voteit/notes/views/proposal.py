# -*- coding: utf-8 -*-
from arche.views.base import BaseForm
from betahaus.viewcomponent import view_action
from pyramid.response import Response
from pyramid.view import view_config
from voteit.core.models.interfaces import IProposal
from voteit.core.security import VIEW

from voteit.notes import _


@view_action('metadata_listing', 'personal_notes',
             permission = VIEW,
             interface = IProposal,
             priority = 50)
def personal_notes_btn(context, request, va, **kw):
    if not request.personal_notes_enabled:
        return
    has_data = context.uid in request.personal_meeting_notes
    data = {'role': 'button',
            'class': 'btn btn-default btn-xs',
            'data-external-popover-loaded': 'false',
            'data-popover-for': context.uid,
            'data-placement': 'bottom',
            'title': request.localizer.translate(_("Your private notes")),
            'href': request.resource_url(context, 'edit_personal_notes'),}
    return """<a %s>&nbsp;%s<span class="glyphicon glyphicon-pushpin text-primary"></span>&nbsp;</a> """ % \
           (" ".join('%s="%s"' % (k, v) for (k, v) in data.items()),
            has_data and '<span class="glyphicon glyphicon-asterisk text-primary">' or '')


@view_config(context=IProposal, name='edit_personal_notes', renderer='arche:templates/form.pt')
class PersonalNotesForm(BaseForm):
    #response_template = 'voteit.core:templates/portlets/inline_add_button_prop.pt'
    formid = 'edit_personal_notes'
    update_selector = '#ai-proposals'
    type_name = 'Notes'
    schema_name = 'edit'
    use_ajax = True
    update_structure_tpl = 'voteit.core:templates/snippets/js_update_structure.pt'

    @property
    def notes(self):
        return self.request.personal_meeting_notes

    def appstruct(self):
        return dict(self.notes.get(self.context.uid, {}))

    def _response(self, destroy=True):
        kwargs = {}
        selector = '[data-popover-for="%s"]' % self.context.uid
        if destroy:
            kwargs['destroy_popover'] = selector
        else:
            kwargs['hide_popover'] = selector
        return Response(
            self.render_template(self.update_structure_tpl, **kwargs)
        )

    def save_success(self, appstruct):
        self.notes[self.context.uid] = appstruct
        return self._response()

    def cancel(self, *args):
        return self._response()

    cancel_success = cancel_failure = cancel


def includeme(config):
    config.scan(__name__)
