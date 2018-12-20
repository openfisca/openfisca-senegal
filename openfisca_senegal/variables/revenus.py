# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_senegal.entities import *


class benefices_non_salarie(Variable):
    value_type = float
    entity = Individu
    label = u"Bénéfices non salarié"
    definition_period = YEAR
    set_input = set_input_divide_by_period


class conjoint_a_des_revenus(Variable):
    value_type = bool
    entity = Individu
    definition_period = YEAR


class pension_retraite(Variable):
    value_type = float
    entity = Individu
    label = u"Pension Retraite"
    definition_period = YEAR
    set_input = set_input_divide_by_period


class salaire(Variable):
    value_type = float
    entity = Individu
    label = "Salaire"
    set_input = set_input_divide_by_period
    definition_period = YEAR
