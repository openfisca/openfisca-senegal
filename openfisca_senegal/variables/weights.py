# -*- coding: utf-8 -*-


from openfisca_core.model_api import *
from openfisca_senegal.entities import *


class menage_weight(Variable):
    default_value = 1.0
    is_period_size_independent = True
    value_type = float
    entity = Menage
    label = u"Poids du ménage"
    definition_period = YEAR


class individu_weight(Variable):
    default_value = 1.0
    is_period_size_independent = True
    value_type = float
    entity = Individu
    label = u"Poids de l'individu"
    definition_period = YEAR
