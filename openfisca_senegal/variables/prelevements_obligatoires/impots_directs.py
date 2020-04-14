# -*- coding: utf-8 -*-

from numpy import (
    clip,
    floor_divide,
    )


from openfisca_core.model_api import *
from openfisca_senegal.entities import *


class categorie_cgu(Variable):
    # prod A: revendeurs de ciments et de denrées alimentaires
    # prod B: autres commerçants ou revendeurs (CGU )
    # [CGU comm/prod A < CGU comm/prod B < CGU service] -> 0, 1 ,2
    # NaNs are -1
    value_type = int
    entity = Person
    default_value = -1
    definition_period = YEAR
    label = "Index de la catgeorie CGU de l'individu"


class contribution_generale_unique(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR

    def formula_2013(individu, period, parameters):
        categorie_cgu = individu('categorie_cgu', period)
        revenu_non_salarie = individu('revenu_non_salarie', period)
        cgu = parameters(period).prelevements_obligatoires.impots_directs.cgu.post_2013
        taux_revendeurs_ciment_et_denrees_alimentaires = cgu.revendeurs_ciment_et_denrees_alimentaires
        taux_autres_producteurs_et_revendeurs = cgu.autres_producteurs_et_revendeurs
        taux_prestataires_service = cgu.prestataires_service

        taux = (
            (categorie_cgu == 0) * taux_revendeurs_ciment_et_denrees_alimentaires.calc(
                revenu_non_salarie)
            + (categorie_cgu == 1) * taux_autres_producteurs_et_revendeurs.calc(
                revenu_non_salarie)
            + (categorie_cgu == 2) * taux_prestataires_service.calc(
                revenu_non_salarie)
            )
        return taux * revenu_non_salarie

    def formula_2007(individu, period, parameters):
        categorie_cgu = individu('categorie_cgu', period)
        revenu_non_salarie = individu('revenu_non_salarie', period)
        cgu = parameters(period).prelevements_obligatoires.impots_directs.cgu.pre_2013
        montant_revendeurs_ciment_et_denrees_alimentaires = cgu.revendeurs_ciment_et_denrees_alimentaires
        montant_autres_producteurs_et_revendeurs = cgu.autres_producteurs_et_revendeurs
        montant_prestataires_service = cgu.prestataires_service
        montant = (
            (categorie_cgu == 0) * montant_revendeurs_ciment_et_denrees_alimentaires.calc(
                revenu_non_salarie)
            + (categorie_cgu == 1) * montant_autres_producteurs_et_revendeurs.calc(
                revenu_non_salarie)
            + (categorie_cgu == 2) * montant_prestataires_service.calc(
                revenu_non_salarie)
            )
        return montant


class droit_progressif(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR

    def formula_2013(individu, period, parameters):
        abattement = parameters(period).prelevements_obligatoires.impots_directs.abattement_proportionnel
        abattement_salaire_max = parameters(period).prelevements_obligatoires.impots_directs.abattement_salaire_max
        salaire = individu('salaire_imposable', period, options = [ADD])
        salaire_abattement = min_(abattement.abattement_salaire * salaire, abattement_salaire_max)
        salaire_imposable = salaire - salaire_abattement

        pension_retraite = individu('pension_retraite', period, options = [ADD])
        abattement_retraite_min = parameters(period).prelevements_obligatoires.impots_directs.abattement_retraite_min
        pension_abbattement = max_(pension_retraite * abattement.abattement_retaire, abattement_retraite_min) * (pension_retraite > 0)
        retraite_imposable = pension_retraite - pension_abbattement
        benefices_non_salarie = individu('benefices_non_salarie', period, options = [ADD])
        benefice_abattement = benefices_non_salarie * abattement.abattement_benefice
        benefices_imposable = benefices_non_salarie - benefice_abattement

        revenus_arrondis = floor_divide(salaire_imposable + retraite_imposable + benefices_imposable, 1000) * 1000
        revenus_imposable = max_(0, revenus_arrondis)

        bareme_impot_progressif = parameters(period).prelevements_obligatoires.impots_directs.bareme_impot_progressif
        return bareme_impot_progressif.calc(revenus_imposable)

    def formula_2007(individu, period, parameters):
        abattement = parameters(period).prelevements_obligatoires.impots_directs.abattement_proportionnel
        salaire = individu('salaire_imposable', period)
        salaire_abattement = abattement.abattement_salaire * salaire
        salaire_imposable = salaire - salaire_abattement

        pension_retraite = individu('pension_retraite', period)
        abattement_retraite_min = parameters(period).prelevements_obligatoires.impots_directs.abattement_retraite_min
        pension_abbattement = max_(pension_retraite * abattement.abattement_retaire, abattement_retraite_min) * (pension_retraite > 0)
        retraite_imposable = pension_retraite - pension_abbattement

        revenus_arrondis = floor_divide(
            salaire_imposable + retraite_imposable,
            1000
            ) * 1000
        revenus_imposable = max_(0, revenus_arrondis)

        bareme_impot_progressif = parameters(period).prelevements_obligatoires.impots_directs.bareme_impot_progressif
        return bareme_impot_progressif.calc(revenus_imposable)


class droit_proportionnel(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    end = '2012-12-31'

    def formula(individu, period, parameters):
        bareme_impot_proportionnel = parameters(period).prelevements_obligatoires.impots_directs.bareme_impot_proportionnel
        revenus_fonciers_brut = individu('revenus_fonciers_brut', period)
        salaire = individu('salaire_imposable', period)
        actions_interets = individu('actions_interets', period)
        obligations = individu('obligations', period)
        lots = individu('lots', period)
        jetons_et_autres_remunerations = individu('jetons_et_autres_remunerations', period,)
        produits_des_comptes = individu('produits_des_comptes', period,)
        salaires_au_dela_du_seuil = (salaire > bareme_impot_proportionnel.seuil_imposabilite)

        return (
            bareme_impot_proportionnel.salaires_imposables * salaires_au_dela_du_seuil
            + bareme_impot_proportionnel.revenus_fonciers * revenus_fonciers_brut
            + bareme_impot_proportionnel.actions_interets * actions_interets
            + bareme_impot_proportionnel.obligations * obligations
            + bareme_impot_proportionnel.lots * lots
            + bareme_impot_proportionnel.jetons_et_autres_remunerations * jetons_et_autres_remunerations
            + bareme_impot_proportionnel.produits_des_comptes * produits_des_comptes
            )


class impots_directs(Variable):
    value_type = float
    entity = Household
    definition_period = YEAR
    label = "Impôts directs payés par le ménage"

    def formula(household, period):
        impot_revenus = household.members('impot_revenus', period)
        return household.sum(impot_revenus)


class impot_revenu(Variable):
    value_type = float
    entity = Household
    definition_period = YEAR
    label = "Impôt sur le revenu par le ménage"

    def formula(household, period):
        impot_revenus = household.members('impot_revenus', period)
        return household.sum(impot_revenus)


class impot_revenus(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR

    def formula_2013(individu, period):
        droit_progressif = individu('droit_progressif', period)
        reduction_impots_pour_charge_famille = individu('reduction_impots_pour_charge_famille', period)
        impot_apres_reduction_famille = droit_progressif - reduction_impots_pour_charge_famille
        return max_(0, impot_apres_reduction_famille)


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


class reduction_impots_pour_charge_famille(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR

    def formula_2013(individu, period, parameters):
        droit_progressif = individu('droit_progressif', period)

        nombre_de_parts = individu('nombre_de_parts', period)
        reductions_pour_charge_de_famille = parameters(period).prelevements_obligatoires.impots_directs.reductions_pour_charge_de_famille

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

        reduction_impot = clip(droit_progressif * taux, a_min = minimum, a_max = maximum)
        return reduction_impot


class salaire_net_a_payer(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Salaire net à payer"

    def formula(person, period, parameters):
        return (
            person('salaire_imposable', period)
            - person('impot_revenus', period)
            )
