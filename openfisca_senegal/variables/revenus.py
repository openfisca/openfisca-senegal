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


class revenus_fonciers(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Revenus fonciers"


class actions_interets(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Produits des actions, parts sociales et parts d’intérêts des sociétés civiles"

class obligations(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Obligations"


class lots(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Lots"


class autres_revenus_capitaux(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Autres revenus notamment les jetons de présence et autres rémunérations"


class produits_des_comptes(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Les intérêts, arrérages et autres produits des comptes de dépôts et des comptes courants"


class sup_700000(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Variable binaire indiquant si le salaire est supérieur à 700 000"

    def formula(Person, period):
        sup_700000 = Person.salaire > 700000
        return sup_700000
