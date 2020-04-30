import numpy as np


from openfisca_core.model_api import *
from openfisca_senegal.entities import *
from openfisca_core.taxscales import MarginalRateTaxScale


class autres_revenus_du_capital_brut(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Revenu des capitaux brut"

    # Pas valable après 2013
    def formula(individu, period, parameters):
        autres_revenus_du_capital = individu("autres_revenus_du_capital", period)
        bareme_impot_proportionnel = parameters(period).prelevements_obligatoires.impots_directs.bareme_impot_proportionnel
        taux_imposition_commun = bareme_impot_proportionnel.produits_des_comptes
        return autres_revenus_du_capital / (1 - taux_imposition_commun)


class revenu_foncier_brut(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Revenu locatif (foncier) brut"

    # Pas valable après 2013
    def formula(individu, period, parameters):
        revenu_locatif = individu("revenu_locatif", period)
        bareme_impot_proportionnel = parameters(period).prelevements_obligatoires.impots_directs.bareme_impot_proportionnel
        return revenu_locatif / (1 - bareme_impot_proportionnel.revenus_fonciers)


class revenu_non_salarie_brut(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Revenu non salarie brut"

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
        # B = N + T = N + taux * B => B = N / (1 - taux)
        return revenu_non_salarie / (1 - taux)

    def formula_2007(individu, period, parameters):
        categorie_cgu = individu('categorie_cgu', period)
        revenu_non_salarie = individu('revenu_non_salarie', period)
        cgu = parameters(period).prelevements_obligatoires.impots_directs.cgu.pre_2013

        montant_revendeurs_ciment_et_denrees_alimentaires = cgu.revendeurs_ciment_et_denrees_alimentaires
        montant_autres_producteurs_et_revendeurs = cgu.autres_producteurs_et_revendeurs
        montant_prestataires_service = cgu.prestataires_service
        revenu_non_salarie_brut = (
            (categorie_cgu == -1) * revenu_non_salarie
            + (categorie_cgu == 0) * inverse_amount_tax_scale(
                montant_revendeurs_ciment_et_denrees_alimentaires,
                revenu_non_salarie
                )
            + (categorie_cgu == 1) * inverse_amount_tax_scale(
                montant_autres_producteurs_et_revendeurs,
                revenu_non_salarie
                )
            + (categorie_cgu == 2) * inverse_amount_tax_scale(
                montant_prestataires_service,
                revenu_non_salarie
                )
            )
        inverse_amount_tax_scale(
            montant_revendeurs_ciment_et_denrees_alimentaires, revenu_non_salarie
            )

        return revenu_non_salarie_brut


class pension_retraite_brut(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR

    def formula(individu, period, parameters):
        # Valable entre 20007 et avant la réforme de 2013
        nombre_de_parts = individu('nombre_de_parts', period)
        pension_retraite = individu('pension_retraite', period)

        nombre_de_parts_values = np.unique(nombre_de_parts)
        pension_retraite_brut = 0
        for nombre_de_parts_value in nombre_de_parts_values:
            bareme = compute_bareme_retraite(parameters, period, nombre_de_parts_value)
            pension_retraite_brut += (
                (nombre_de_parts == nombre_de_parts_value)
                * nombre_de_parts
                * bareme.inverse().calc(pension_retraite / nombre_de_parts)
                )

        return pension_retraite_brut * (pension_retraite > 0)


def compute_bareme_retraite(parameters, period, nombre_de_parts_value):
    impots_directs = parameters(period).prelevements_obligatoires.impots_directs
    bareme = impots_directs.bareme_impot_progressif.copy()
    abattement_retraite = impots_directs.abattement_proportionnel.abattement_retraite
    abattement_retraite_min = impots_directs.abattement_retraite_min / nombre_de_parts_value
    # abattement_retraite_min matches first threshold
    adjusted_bareme = MarginalRateTaxScale()
    adjusted_bareme.add_bracket(0, 0)
    facteur_abattement = 1 - abattement_retraite
    previous_rate = None
    first_to_cross = "not yet"
    for rate, threshold in zip(bareme.rates, bareme.thresholds):
        if rate == 0:
            continue
        if threshold * abattement_retraite < abattement_retraite_min:
            adjusted_bareme.add_bracket(
                threshold = threshold + abattement_retraite_min,
                rate = rate,
                )

    for threshold in adjusted_bareme.thresholds.copy():
        if threshold > abattement_retraite_min / abattement_retraite:
            delete_bracket_matching_threshold(adjusted_bareme, threshold)

    for rate, threshold in zip(bareme.rates, bareme.thresholds):
        if rate == 0:
            continue
        if threshold / facteur_abattement > (abattement_retraite_min / abattement_retraite):
            first_to_cross = "yes" if (first_to_cross == "not yet") else "already"
            adjusted_bareme.add_bracket(
                threshold = threshold / facteur_abattement,
                rate = rate * facteur_abattement,
                )

        if first_to_cross == "yes":
            adjusted_bareme.add_bracket(
                threshold = abattement_retraite_min / abattement_retraite,
                rate = previous_rate * facteur_abattement,
                )

        previous_rate = rate

    return adjusted_bareme


def delete_bracket_matching_threshold(tax_scale, threshold):
    index = tax_scale.thresholds.index(threshold)
    del tax_scale.thresholds[index]
    del tax_scale.rates[index]


class salaire_brut(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Salaire brut"

    def formula(individu, period, parameters):
        # Valable entre 20007 et avant la réforme de 2013
        salaire = individu('salaire', period)
        est_cadre = individu('est_cadre', period)
        impots_directs = parameters(period).prelevements_obligatoires.impots_directs
        bareme = impots_directs.bareme_impot_progressif.copy()
        abattements = impots_directs.abattement_proportionnel
        # On suppose qu'on est au régime de la retenue à la source
        facteur_abattements = (
            (1 - abattements.abattement_salaire)
            * (1 - abattements.abattement_forfaitaire)
            )
        bareme.multiply_rates(facteur_abattements)
        bareme.multiply_thresholds(1 / facteur_abattements)

        taux_impot_proportionnel = impots_directs.bareme_impot_proportionnel.salaires_imposables
        seuil_imposabilite = impots_directs.bareme_impot_proportionnel.seuil_imposabilite

        bareme_droit_porportionnel = MarginalRateTaxScale()
        bareme_droit_porportionnel.add_bracket(0, 0)
        bareme_droit_porportionnel.add_bracket(
            threshold = seuil_imposabilite / (1 - abattements.abattement_salaire),
            rate = taux_impot_proportionnel * (1 - abattements.abattement_salaire),
            )
        bareme.add_tax_scale(bareme_droit_porportionnel)
        salaire_imposable = bareme.inverse().calc(salaire)

        retraite = parameters(period).prelevements_obligatoires.prelevements_sociaux.retraite.salarie_ipres.copy()
        sante = parameters(period).prelevements_obligatoires.prelevements_sociaux.maladie.salarie_taux_minimal
        retraite_complementaire = parameters(period).prelevements_obligatoires.prelevements_sociaux.retraite.salarie_cadres.copy()
        prelevements_sociaux = retraite.copy()
        prelevements_sociaux.add_tax_scale(sante)
        prelevements_sociaux_cadre = prelevements_sociaux.copy()
        prelevements_sociaux_cadre.add_tax_scale(retraite_complementaire)
        salaire_brut = 12 * (
            not_(est_cadre) * prelevements_sociaux.inverse().calc(salaire_imposable / 12)
            + est_cadre * prelevements_sociaux_cadre.calc(salaire_imposable / 12)
            )
        return salaire_brut * (salaire > 0)


# helpers

def inverse_amount_tax_scale(tax_scale, net_income):
    # B = N + M(B) => B = N + M_i /. N >= S_i - M_i & N < S_(i+1) - M_(i+1)
    gross_tax_scale = tax_scale.copy()
    gross_tax_scale.thresholds = [
        max(threshold - amount, 0)  # Excluding negatove net incomes
        for (threshold, amount) in zip([0] + tax_scale.thresholds[1:], tax_scale.amounts)
        ]
    return net_income + gross_tax_scale.calc(net_income)
