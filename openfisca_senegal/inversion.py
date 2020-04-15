from openfisca_core.model_api import *
from openfisca_senegal.entities import *


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


class salaire_brut(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Salaire brut"

    def formula(individu, period, parameters):
        salaire = individu('salaire', period)
        bareme = parameters(period).prelevements_obligatoires.impots_directs.bareme_impot_progressif.copy()
        retraite = parameters(period).prelevements_obligatoires.prelevements_sociaux.retraite.salarie_ipres.copy()
        retraite_complementaire = parameters(period).prelevements_obligatoires.prelevements_sociaux.retraite.salarie_cadres.copy()
        prelevements_sociaux = retraite.copy()
        prelevements_sociaux.add_tax_scale(retraite_complementaire)
        salaire_imposable = bareme.inverse().calc(salaire)
        salaire_brut = 12 * prelevements_sociaux.inverse().calc(salaire_imposable / 12)
        return salaire_brut




# helpers

def inverse_amount_tax_scale(tax_scale, net_income):
    # B = N + M(B) => B = N + M_i /. N >= S_i - M_i & N < S_(i+1) - M_(i+1)
    gross_tax_scale = tax_scale.copy()
    gross_tax_scale.thresholds = [
        max(threshold - amount, 0)  # Excluding negatove net incomes
        for (threshold, amount) in zip([0] + tax_scale.thresholds[1:], tax_scale.amounts)
        ]
    # print(gross_tax_scale)
    return net_income + gross_tax_scale.calc(net_income)


