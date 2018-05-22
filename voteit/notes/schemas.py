import colander
import deform

from voteit.notes import _


STATES_VALUES = (
    ('', _("- select -")),
    ('approve', _("Approve")),
    ('deny', _("Deny")),
    ('other', _("Other")),
)


class NotesSchema(colander.Schema):
    widget = deform.widget.FormWidget(
        template='voteit_form_inline',
    )
    propose = colander.SchemaNode(
        colander.String(),
        title = _("Your stance"),
        missing=colander.drop,
        widget = deform.widget.SelectWidget(values=STATES_VALUES),
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
