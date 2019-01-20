# -*- coding: utf-8 -*-

from openfisca_senegal import CountryTaxBenefitSystem as SenegalTaxBenefitSystem

from openfisca_survey_manager.scenarios import AbstractSurveyScenario


class SenegalSurveyScenario(AbstractSurveyScenario):
    id_variable_by_entity_key = dict(
        menage = 'id_menage',
        )
    role_variable_by_entity_key = dict(
        menage = 'role_menage',
        )

    def __init__(self, tax_benefit_system = None, baseline_tax_benefit_system = None, year = None,
            data = None):
        super(SenegalSurveyScenario, self).__init__()
        assert year is not None
        self.year = year
        if tax_benefit_system is None:
            tax_benefit_system = SenegalTaxBenefitSystem()
        self.set_tax_benefit_systems(
            tax_benefit_system = tax_benefit_system,
            baseline_tax_benefit_system = baseline_tax_benefit_system
            )
        if data is None:
            return

        if data is not None:
            input_data_frame = data.get('input_data_frame')

        if input_data_frame is None:
            return

        if input_data_frame is not None:
            self.used_as_input_variables = list(
                set(tax_benefit_system.variables.keys()).intersection(
                    set(input_data_frame.columns)
                    ))
        self.init_from_data(data = data)
