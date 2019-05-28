# -*- coding: utf-8 -*-


import logging
import os
import pkg_resources


import pandas as pd
from slugify import slugify


from openfisca_ceq.tools import add_ceq_framework
from openfisca_senegal import CountryTaxBenefitSystem as SenegalTaxBenefitSystem
from openfisca_senegal.survey_scenarios import SenegalSurveyScenario
from openfisca_senegal.tests.test_survey_scenario_from_stata_data import (
    data_is_available,
    create_data_from_stata,
    )


def create_survey_sceanrio():
    tax_benefit_system = SenegalTaxBenefitSystem()
    ceq_enhanced_tax_benefit_system = add_ceq_framework(tax_benefit_system)
    if not data_is_available:
        return
    data = create_data_from_stata()
    survey_scenario = SenegalSurveyScenario(
        tax_benefit_system = ceq_enhanced_tax_benefit_system,
        data = data,
        year = 2017,
        )
    return survey_scenario


def read_aggregates():
    package_path = pkg_resources.get_distribution("openfisca-senegal").location
    asset_path = os.path.join(package_path, "openfisca_senegal", 'assets')
    file_path = os.path.join(asset_path, 'general_government_budget.csv')
    recettes = pd.read_csv(file_path)
    recettes.columns = [slugify(column, separator = "_") for column in recettes.columns]
    # print(recettes.columns)
    government_revenue_spending_in_milliards_fcfa_by_variable = {
        "impot_revenus": "Personal Income Tax"
        }

    recette_by_variable = dict(
        (variable, recettes.loc[
            recettes.government_revenue_spending_in_milliards_fcfa == government_revenue_spending_in_milliards_fcfa,
            "currency_amounts_in_administ_accounts_otherwise_specified"
            ].values[0])
        for variable, government_revenue_spending_in_milliards_fcfa in government_revenue_spending_in_milliards_fcfa_by_variable.items()
        )
    # print(recette_by_variable)
    return recette_by_variable


def test_aggregates():
    recette_by_variable = read_aggregates()
    survey_scenario = create_survey_sceanrio()
    period = 2017
    if survey_scenario is not None:
        for variable, recette in recette_by_variable.items():
            logging.info("Aggregats de la variable {}".format(variable))
            logging.info(survey_scenario.compute_aggregate(variable, period = period) / 1e9)
            logging.info(recette)


if __name__ == '__main__':
    import sys
    logging.basicConfig(level = logging.INFO, stream = sys.stdout)
    test_aggregates()
