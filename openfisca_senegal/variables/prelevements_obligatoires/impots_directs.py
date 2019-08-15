# -*- coding: utf-8 -*-

from numpy import (
    clip,
    floor_divide,
    )


from openfisca_core.model_api import *
from openfisca_senegal.entities import *


class nombre_de_parts(Variable):
    value_type = float
    entity = Person
    label = "Nombre de parts"
    definition_period = YEAR

    def formula(individu, period, parameters):
        nombre_de_parts_par_enfant = parameters(period).nombre_de_parts.par_enfant
        limite_nombre_de_parts = parameters(period).nombre_de_parts.limite_max
        repartition_marie_conjoint = parameters(period).nombre_de_parts.repartition_marie_conjoint
        veuf_avec_enfant = parameters(period).nombre_de_parts.veuf_avec_enfant

        est_marie = individu('est_marie', period)
        est_veuf = individu('est_veuf', period)
        nombre_enfants = individu('nombre_enfants', period)
        parts_enfant_veuf = est_veuf * veuf_avec_enfant * min_(1, nombre_enfants)

        nombre_de_parts_enfants = nombre_enfants * nombre_de_parts_par_enfant + parts_enfant_veuf
        conjoint_a_des_revenus = individu('conjoint_a_des_revenus', period)
        nombre_de_parts_conjoint = est_marie * repartition_marie_conjoint * (1 + not_(conjoint_a_des_revenus))

        nombre_de_parts = 1 + nombre_de_parts_conjoint + nombre_de_parts_enfants

        return min_(limite_nombre_de_parts, nombre_de_parts)


class impot_avant_reduction_famille(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR

    def formula(individu, period, legislation):
        salaire = individu('salaire', period, options = [ADD])
        salaire_abattement = min_(0.3 * salaire, 900000)
        salaire_imposable = salaire - salaire_abattement

        pension_retraite = individu('pension_retraite', period, options = [ADD])
        pension_abbattement = max_(pension_retraite * 0.4, 1800000) * (pension_retraite > 0)
        retraite_imposable = pension_retraite - pension_abbattement
        benefices_non_salarie = individu('benefices_non_salarie', period, options = [ADD])
        benefice_abattement = benefices_non_salarie * 0.15
        benefices_imposable = benefices_non_salarie - benefice_abattement

        revenus_arrondis = floor_divide(salaire_imposable + retraite_imposable + benefices_imposable, 1000) * 1000
        revenus_imposable = max_(0, revenus_arrondis)

        bareme_impot_progressif = legislation(period).bareme_impot_progressif
        return bareme_impot_progressif.calc(revenus_imposable)


class reduction_impots_pour_charge_famille(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR

    def formula(individu, period, legislation):
        impot_avant_reduction_famille = individu('impot_avant_reduction_famille', period)

        nombre_de_parts = individu('nombre_de_parts', period)
        reductions_pour_charge_de_famille = legislation(period).reductions_pour_charge_de_famille

        taux = (nombre_de_parts == 1) * reductions_pour_charge_de_famille.taux_1 + \
            (nombre_de_parts == 1.5) * reductions_pour_charge_de_famille.taux_2 + \
            (nombre_de_parts == 2) * reductions_pour_charge_de_famille.taux_3 + \
            (nombre_de_parts == 2.5) * reductions_pour_charge_de_famille.taux_4 + \
            (nombre_de_parts == 3) * reductions_pour_charge_de_famille.taux_5 + \
            (nombre_de_parts == 3.5) * reductions_pour_charge_de_famille.taux_6 + \
            (nombre_de_parts == 4) * reductions_pour_charge_de_famille.taux_7 + \
            (nombre_de_parts == 4.5) * reductions_pour_charge_de_famille.taux_8 + \
            (nombre_de_parts == 5) * reductions_pour_charge_de_famille.taux_9
        minimum = (nombre_de_parts == 1) * reductions_pour_charge_de_famille.min_1 + \
            (nombre_de_parts == 1.5) * reductions_pour_charge_de_famille.min_2 + \
            (nombre_de_parts == 2) * reductions_pour_charge_de_famille.min_3 + \
            (nombre_de_parts == 2.5) * reductions_pour_charge_de_famille.min_4 + \
            (nombre_de_parts == 3) * reductions_pour_charge_de_famille.min_5 + \
            (nombre_de_parts == 3.5) * reductions_pour_charge_de_famille.min_6 + \
            (nombre_de_parts == 4) * reductions_pour_charge_de_famille.min_7 + \
            (nombre_de_parts == 4.5) * reductions_pour_charge_de_famille.min_8 + \
            (nombre_de_parts == 5) * reductions_pour_charge_de_famille.min_9
        maximum = (nombre_de_parts == 1) * reductions_pour_charge_de_famille.max_1 + \
            (nombre_de_parts == 1.5) * reductions_pour_charge_de_famille.max_2 + \
            (nombre_de_parts == 2) * reductions_pour_charge_de_famille.max_3 + \
            (nombre_de_parts == 2.5) * reductions_pour_charge_de_famille.max_4 + \
            (nombre_de_parts == 3) * reductions_pour_charge_de_famille.max_5 + \
            (nombre_de_parts == 3.5) * reductions_pour_charge_de_famille.max_6 + \
            (nombre_de_parts == 4) * reductions_pour_charge_de_famille.max_7 + \
            (nombre_de_parts == 4.5) * reductions_pour_charge_de_famille.max_8 + \
            (nombre_de_parts == 5) * reductions_pour_charge_de_famille.max_9

        reduction_impot = clip(impot_avant_reduction_famille * taux, a_min = minimum, a_max = maximum)
        return reduction_impot


class impot_revenus(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR

    def formula(individu, period):
        impot_avant_reduction_famille = individu('impot_avant_reduction_famille', period)
        reduction_impots_pour_charge_famille = individu('reduction_impots_pour_charge_famille', period)
        impot_apres_reduction_famille = impot_avant_reduction_famille - reduction_impots_pour_charge_famille
        return max_(0, impot_apres_reduction_famille)
