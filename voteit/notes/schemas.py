import colander

from voteit.notes import _



class NotesSchema(colander.Schema):

    propose = colander.SchemaNode(
        colander.String(),
        title = _("I want this to..."),

    )
    notes = colander.SchemaNode(
        colander.String(),

    )


def includeme(config):
    pass
