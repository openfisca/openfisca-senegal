# -*- coding: utf-8 -*-

from openfisca_senegal.base import *
from numpy import clip, floor_divide


class date_de_naissance(Variable):
    column = DateCol
    entity = Individu
    label = u"Date de naissance"


class salaire(Variable):
    column = FloatCol
    entity = Individu
    label = "Salaire"
    set_input = set_input_divide_by_period


class est_marie(Variable):
    column = BoolCol
    entity = Individu
    label = u"Est marié"
    set_input = set_input_dispatch_by_period

class est_divorce(Variable):
    column = BoolCol
    entity = Individu
    label = u"Est divorcé"
    set_input = set_input_dispatch_by_period

class est_veuf(Variable):
    column = BoolCol
    entity = Individu
    label = u"Est veuf"
    set_input = set_input_dispatch_by_period

class est_celibataire(Variable):
    column = BoolCol
    entity = Individu
    label = u"Est célibataire"
    set_input = set_input_dispatch_by_period

class conjoint_a_des_revenus(Variable):
    column = BoolCol
    entity = Individu


class nombre_enfants(Variable):
    column = IntCol
    entity = Individu


class pension_retraite(Variable):
    column = FloatCol
    entity = Individu
    label = "Pension Retraite"
    set_input = set_input_divide_by_period

class benefices_non_salarie(Variable):
    column = FloatCol
    entity = Individu
    label = "Bénéfices non salarié"
    set_input = set_input_divide_by_period

class nombre_de_parts(Variable):
    column = FloatCol
    entity = Individu
    label = u"Nombre de parts"

    def function(individu, period):
        nombre_de_parts_enfants = individu('nombre_enfants', period) * 0.5

        conjoint_a_des_revenus = individu('conjoint_a_des_revenus', period)
        est_marie = individu('est_marie', period)
        nombre_de_parts_conjoint = est_marie * 0.5 + (1 - conjoint_a_des_revenus) * 0.5

        nombre_de_parts = 1 + nombre_de_parts_conjoint + nombre_de_parts_enfants

        return period, min_(5, nombre_de_parts)


class impot_avant_reduction_famille(Variable):
    column = FloatCol
    entity = Individu

    def function(individu, period, legislation):
        salaire = individu('salaire', period, options = [ADD])
        salaire_abattement = 0.3 * salaire
        salaire_imposable = salaire - salaire_abattement

        pension_retraite = individu('pension_retraite', period, options = [ADD])
        pension_abbattement = max_(pension_retraite * 0.4, 1800000)
        retraite_imposable = pension_retraite - pension_abbattement

        benefices_non_salarie = individu('benefices_non_salarie', period, options = [ADD])
        benefice_abattement = benefices_non_salarie*0.15
        benefices_imposable = benefices_non_salarie - benefice_abattement

        revenus_arrondis = floor_divide(salaire_imposable + retraite_imposable + benefices_imposable, 1000) * 1000
        revenus_imposable = max_(0, revenus_arrondis)
        
        revenus_imposable = salaire_imposable + retraite_imposable + benefices_imposable

        bareme_impot_progressif = legislation(period).bareme_impot_progressif

        return period, bareme_impot_progressif.calc(revenus_imposable)


class reduction_impots_pour_charge_famille(Variable):
    column = FloatCol
    entity = Individu

    def function(individu, period, legislation):
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

        return period, reduction_impot


class impot_revenus(Variable):
    column = FloatCol
    entity = Individu

    def function(individu, period):
        impot_avant_reduction_famille = individu('impot_avant_reduction_famille', period)
        reduction_impots_pour_charge_famille = individu('reduction_impots_pour_charge_famille', period)
        impot_apres_reduction_famille = impot_avant_reduction_famille - reduction_impots_pour_charge_famille
        return period, max_(0, impot_apres_reduction_famille)


