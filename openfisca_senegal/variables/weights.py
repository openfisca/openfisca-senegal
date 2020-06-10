
from openfisca_core.model_api import *
from openfisca_senegal.entities import *


class household_weight(Variable):
    default_value = 1.0
    is_period_size_independent = True
    value_type = float
    entity = Household
    label = "Poids du ménage"
    definition_period = YEAR


class person_weight(Variable):
    default_value = 1.0
    is_period_size_independent = True
    value_type = float
    entity = Person
    label = "Poids de l'individ"
    definition_period = YEAR
