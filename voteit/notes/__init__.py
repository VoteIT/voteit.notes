import logging

from pyramid.i18n import TranslationStringFactory


_ = TranslationStringFactory("voteit.notes")


logger = logging.getLogger(__name__)


def includeme(config):
    config.include('.fanstaticlib')
    config.include('.models')
    config.include('.schemas')
    config.include('.views')
    # Add templates dir
    from pyramid_deform import configure_zpt_renderer
    configure_zpt_renderer(['voteit.notes:templates/widgets'])
    #config.add_translation_dirs('voteit.notes:locale/')
    cache_max_age = int(config.registry.settings.get('arche.cache_max_age', 60*60*24))
    config.add_static_view('notes_static', 'voteit.notes:static', cache_max_age = cache_max_age)
