# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_senegal.entities import *


class benefices_non_salarie(Variable):
    value_type = float
    entity = Person
    label = "Bénéfices non salarié"
    definition_period = YEAR


class conjoint_a_des_revenus(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR


class pension_retraite(Variable):
    value_type = float
    entity = Person
    label = "Pension Retraite"
    definition_period = YEAR


class salaire(Variable):
    value_type = float
    entity = Person
    label = "Salaire"
    definition_period = YEAR


class salaire_brut(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Salaires et traitements brut tirés d'une activitée formelle"
