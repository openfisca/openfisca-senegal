# -*- coding: utf-8 -*-

# This file defines the entities needed by our legislation.
from openfisca_core.entities import build_entity

Menage = build_entity(
    key = "menage",
    plural = "menages",
    label = u"Occupants d'un logement principal",
    doc = '''
    Ménage est un exemple d'entité groupe.
    Une entité groupe contient un ou plusieurs individus.
    Chaque individu dans une entité groupe a un rôle (e.g. parent ou enfant).
    Certains rôles ne peuvent être tenus que par un nombre limité d'individus (e.g. a 'premier_parent' ne peut être tenu que
    par un individu), alors que d'autres peuvent avoir un nombre illimité d'individus (e.g. 'enfant').

    Exemple :
    Les variables de logement (e.g. 'taxe_habitation') sont généralement définies pour une entité groupe telle que 'Menage'.

    Utilisation :
    Vérifier le nombre d'individus d'un rôle spécifique (e.g. vérifier s'il y a un 'second_parent') avec
    menage.nb_persons(Menage.PREMIER_PARENT).
    Calculer une variable appliquée à chaque individu de l'entité groupe (e.g. calculer le 'salaire' de chaque membre
    du 'Menage') avec salaires = menage.members('salaire', period = MONTH);
    sum_salaries = menage.sum(salaires).

    Pour en savoir plus, consulter ce lien : https://openfisca.org/doc/coding-the-legislation/50_entities.html
    ''',
    roles = [
        {
            'key': 'parent',
            'plural': 'parents',
            'label': u'Parents',
            'max': 2,
            'subroles': ['premier_parent', 'second_parent'],
            'doc': u'Le ou les deux adultes en charge du ménage.'
            },
        {
            'key': 'enfant',
            'plural': 'enfants',
            'label': u'Enfant',
            'doc': u'Autres individus vivant au sein du ménage.'
            }
        ]
    )

Individu = build_entity(
    key = "individu",
    plural = "individus",
    label = u'Individu',
    doc = '''
    Un Individu représente l'entité légale minimale à laquelle la législation peut s'appliquer.

    Exemple :
    Les variables 'salaire' and 'impot_revenus' sont généralement définies pour l'entité 'Individu'.

    Utilisation :
    Calculer une variable s'appliquant à un 'Individu' (e.g. accéder au 'salaire' d'un mois donné) avec
    individu('salaire', "2017-05").
    Vérifier le rôle d'un 'Individu' dans une entité groupe (e.g. vérifier si 'Individu' est 'premier_parent' 
    dans une entité 'Menage') avec individu.has_role(Menage.PREMIER_PARENT)).

    Pour en savoir plus, consulter ce lien : https://openfisca.org/doc/coding-the-legislation/50_entities.html
    ''',
    is_person = True,
    )

entities = [Menage, Individu]
