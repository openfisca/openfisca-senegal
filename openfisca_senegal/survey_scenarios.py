# -*- coding: utf-8 -*-

from openfisca_senegal import CountryTaxBenefitSystem as SenegalTaxBenefitSystem

from openfisca_survey_manager.scenarios import AbstractSurveyScenario


class SenegalSurveyScenario(AbstractSurveyScenario):
    id_variable_by_entity_key = dict(
        famille = 'id_famille',
        )
    role_variable_by_entity_key = dict(
        famille = 'role_famille',
        )

    def __init__(self, input_data_frame = None, tax_benefit_system = None,
            baseline_tax_benefit_system = None, year = None):
        super(SenegalSurveyScenario, self).__init__()
        assert input_data_frame is not None
        assert year is not None
        self.year = year
        if tax_benefit_system is None:
            tax_benefit_system = SenegalTaxBenefitSystem()
        self.set_tax_benefit_systems(
            tax_benefit_system = tax_benefit_system,
            baseline_tax_benefit_system = baseline_tax_benefit_system
            )
        self.used_as_input_variables = list(
            set(tax_benefit_system.variables.keys()).intersection(
                set(input_data_frame.columns)
                ))
        self.init_from_data_frame(input_data_frame = input_data_frame)
        self.new_simulation()
        if baseline_tax_benefit_system is not None:
            self.new_simulation(use_baseline = True)
