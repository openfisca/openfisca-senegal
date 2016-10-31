# -*- coding: utf-8 -*-


from openfisca_core.columns import IntCol, DateCol, FloatCol
from openfisca_core.formulas import set_input_divide_by_period
from openfisca_core.variables import Variable

from openfisca_senegal.entities import Individus


class id_famille(Variable):
    column = IntCol
    entity_class = Individus
    is_permanent = True
    label = u"Identifiant de la famille"


class role_dans_famille(Variable):
    column = IntCol
    entity_class = Individus
    is_permanent = True
    label = u"Rôle dans la famille"


class date_de_naissance(Variable):
    column = DateCol
    entity_class = Individus
    label = u"Date de naissance"


class salaire(Variable):
    column = FloatCol
    entity_class = Individus
    label = "Salaire"
    set_input = set_input_divide_by_period


class impot_revenu(Variable):
    column = FloatCol
    entity_class = Individus
    label = u"Impôt sur le revenu"

    def function(self, simulation, period):
        salaire = simulation.calculate_add('salaire', period)
        return period, salaire * 0.3
