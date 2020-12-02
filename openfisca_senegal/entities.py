from openfisca_core.entities import build_entity

Household = build_entity(
    key = "household",
    plural = "households",
    label = 'Household',
    doc = '''
    Household is an example of a group entity.
    A group entity contains one or more individual·s.
    For more information, see: https://openfisca.org/doc/coding-the-legislation/50_entities.html
    ''',
    roles = [
        {
            'key': 'personne_de_reference',
            'plural': 'personnes_de_reference',
            'label': 'Personne de reference (Chef-fe de ménage)',
            'doc': 'La personne de référence dans le ménage.',
            'max': 1,
            },
        {
            'key': 'conjoint',
            'plural': 'conjoints',
            'label': 'Conjoint de la personne de référence',
            'doc': 'Le/la conjoint-e de la personne de référence.',
            'max': 1,
            },
        {
            'key': 'enfant',
            'plural': 'enfants',
            'label': 'Enfant',
            'doc': '''Enfant à la charge de la personne de référence et de son conjoint
            - il peut y avoir d'autres enfant dans le ménage '''
            },
        {
            'key': 'autre_membre',
            'plural': 'autres_membres',
            'label': 'Autres membres du ménage',
            'doc': 'Membres du ménage différents de la personne de référence, de son/sa conjoint-e et de leurs enfants'
            # 'Chef du menage',
            # 'Conjoint du CM',
            # 'Enfant du chef/conjoint du CM',
            # autre rassemble:
            # 'Pere/mere du CM/conjoint du CM',
            # 'Autre parent du CM/conjoint du CM',
            # 'Autres personnes non apparentees',
            # 'Domestique'
            }
        ]
    )


Person = build_entity(
    key = "person",
    plural = "persons",
    label = 'Person',
    doc = '''
    A Person represents an individual, the minimal legal entity on which a legislation might be applied.
    For more information, see: https://openfisca.org/doc/coding-the-legislation/50_entities.html
    ''',
    is_person = True,
    )

entities = [Household, Person]
