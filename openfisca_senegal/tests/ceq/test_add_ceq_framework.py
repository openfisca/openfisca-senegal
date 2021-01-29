import logging
import pytest
import sys

from openfisca_ceq.tools.tax_benefit_system_ceq_completion import ceq
from openfisca_senegal import CountryTaxBenefitSystem as SenegalTaxBenefitSystem
from openfisca_senegal.survey_scenarios import SenegalSurveyScenario
from openfisca_senegal.tests.test_survey_scenario_from_stata_data import (
    data_is_available,
    create_data_from_stata,
    )


log = logging.getLogger(__name__)


@pytest.mark.skip(reason = "FileNotFoundError: [Errno 2] No such file or directory: '/home/benjello/Dropbox/Projet_Micro_Sim/B_all_final_dta/TaxeIneq_prep_inc_SEN.dta'")
def test_add_ceq_framework_to_senegal():
    tax_benefit_system = SenegalTaxBenefitSystem()
    tax_benefit_system.legislation_country = "senegal"
    ceq_enhanced_tax_benefit_system = ceq(tax_benefit_system)
    if not data_is_available:
        return
    data = create_data_from_stata()
    survey_scenario = SenegalSurveyScenario(
        tax_benefit_system = ceq_enhanced_tax_benefit_system,
        data = data,
        year = 2017,
        )
    log.info(survey_scenario.calculate_variable('impot_revenus', period = 2017)[0:10])
    log.info(survey_scenario.calculate_variable('personal_income_tax', period = 2017).sum())
    log.info(survey_scenario.compute_aggregate('personal_income_tax', period = 2017))
    return survey_scenario


if __name__ == "__main__":
    logging.basicConfig(level = logging.INFO, stream = sys.stdout)
    test_add_ceq_framework_to_senegal()
