from openfisca_core.model_api import *
from openfisca_senegal.entities import *


class accidents_du_travail(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Cotisation sociale accidents du travail (employeur)"

    def formula(person, period, parameters):
        salaire_brut_annuel = person('salaire_brut', period)
        accidents_du_travail = parameters(period).prelevements_obligatoires.prelevements_sociaux.accidents_du_travail
        taux_1pct = accidents_du_travail.taux_1
        return 12 * taux_1pct.calc(salaire_brut_annuel / 12)


class cotisations_employeur(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Cotisation sociale employeur"

    def formula(person, period):
        return (
            person('accidents_du_travail', period)
            + person('famille', period)
            + person('retraite_employeur', period)
            + person('sante_employeur', period)
            )


class cotisations_salariales(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Cotisation sociale salariales"

    def formula(person, period):
        return (
            person('retraite_salarie', period)
            + person('sante_employeur', period)
            )


class famille(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Cotisation sociale prestations familiales (employeur)"

    def formula(person, period, parameters):
        salaire_brut_annuel = person('salaire_brut', period)
        famille = parameters(period).prelevements_obligatoires.prelevements_sociaux.prestations_familiales
        return 12 * famille.calc(salaire_brut_annuel / 12)


class retraite_employeur(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Cotisation sociale retraite (employeur)"

    def formula(person, period, parameters):
        est_cadre = person('est_cadre', period)
        salaire_brut_annuel = person('salaire_brut', period)
        retraite = parameters(period).prelevements_obligatoires.prelevements_sociaux.retraite
        return (
            12 * retraite.employeur_ipres.calc(salaire_brut_annuel / 12)
            + 12 * est_cadre * retraite.employeur_cadres.calc(salaire_brut_annuel / 12)
            )


class retraite_salarie(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Cotisation sociale retraite (salarié)"

    def formula(person, period, parameters):
        salaire_brut_annuel = person('salaire_brut', period)
        est_cadre = person('est_cadre', period)
        retraite = parameters(period).prelevements_obligatoires.prelevements_sociaux.retraite
        return (
            12 * retraite.salarie_ipres.calc(salaire_brut_annuel / 12)
            + (12 * est_cadre * retraite.salarie_cadres.calc(salaire_brut_annuel / 12))
            )

class sante_employeur(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Cotisation sociale maladie (employeur)"

    def formula(person, period, parameters):
        salaire_brut_annuel = person('salaire_brut', period)
        maladie = parameters(period).prelevements_obligatoires.prelevements_sociaux.maladie.employeur_taux_minimal
        return (
            12 * maladie.calc(salaire_brut_annuel / 12)
            )

class sante_salarie(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Cotisation sociale maladie (salarié)"

    def formula(person, period, parameters):
        salaire_brut_annuel = person('salaire_brut', period)
        maladie = parameters(period).prelevements_obligatoires.prelevements_sociaux.maladie.salarie_taux_minimal
        return (
            12 * maladie.calc(salaire_brut_annuel / 12)
            )


class salaire_imposable(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Salaire imposable"

    def formula(person, period, parameters):
        salaire_brut_annuel = person('salaire_brut', period)
        cotisations_salariales = person('cotisations_salariales', period)
        return salaire_brut_annuel - cotisations_salariales


class salaire_super_brut(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Salaire super brut"

    def formula(person, period, parameters):
        salaire_brut_annuel = person('salaire_brut', period)
        cotisations_employeur = person('cotisations_employeur', period)
        return salaire_brut_annuel + cotisations_employeur
