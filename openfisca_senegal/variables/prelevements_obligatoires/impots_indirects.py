from openfisca_core.model_api import *
from openfisca_senegal.entities import *


class impots_indirects(Variable):
    value_type = float
    entity = Household
    definition_period = YEAR

    def formula(menage, period):
        return menage('tva', period)
