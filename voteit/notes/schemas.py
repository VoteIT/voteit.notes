import colander
import deform

from voteit.notes import _


STATES_VALUES = (
    ('', _("Undecided")),
    ('approve', _("Approve")),
    ('deny', _("Deny")),
)

STATE_ICONS_CLS = {
    'approve': 'glyphicon glyphicon-approved',
    'deny': 'glyphicon glyphicon-denied',
    '': 'glyphicon glyphicon-question-sign',
}

STATE_TXT_CLS = {
    'approve': 'text-success',
    'deny': 'text-danger',
    '': 'text-warning',
}


class NotesSchema(colander.Schema):
    widget = deform.widget.FormWidget(
        template='voteit_form_inline',
    )
    propose = colander.SchemaNode(
        colander.String(),
        title = _("Your stance"),
        missing=colander.drop,
        default="",
        widget = deform.widget.RadioChoiceWidget(
            values=STATES_VALUES,
            icon_cls=STATE_ICONS_CLS,
            txt_cls=STATE_TXT_CLS,
            template='btn_radios',
        ),
    )
    notes = colander.SchemaNode(
        colander.String(),
        title = _("Notes"),
        missing=colander.drop,
        widget = deform.widget.TextAreaWidget(
            rows=4, cols=30,
        )
    )


class NotesSettingsSchema(colander.Schema):
    active = colander.SchemaNode(
        colander.Bool(),
        title = _("Activate this plugin?"),
    )


class PersonalNotesControlsSchema(colander.Schema):
    pass


def includeme(config):
    config.add_schema('Notes', NotesSchema, 'edit')
    config.add_schema('Notes', NotesSettingsSchema, 'settings')
    config.add_schema('Notes', PersonalNotesControlsSchema, 'personal_notes_settings')
