# -*- coding: utf-8 -*-


import pandas as pd


from openfisca_core import periods
from openfisca_survey_manager.scenarios import AbstractSurveyScenario


from openfisca_senegal import CountryTaxBenefitSystem as SenegalTaxBenefitSystem


class SenegalSurveyScenario(AbstractSurveyScenario):
    weight_column_name_by_entity = dict(
        household = 'household_weight',
        person = 'person_weight',
        )
    varying_variable = None


    def __init__(self, tax_benefit_system = None, baseline_tax_benefit_system = None, year = None,
            data = None, varying_variable = None):
        super(SenegalSurveyScenario, self).__init__()
        assert year is not None
        self.year = year
        if tax_benefit_system is None:
            tax_benefit_system = SenegalTaxBenefitSystem()
        self.set_tax_benefit_systems(
            tax_benefit_system = tax_benefit_system,
            baseline_tax_benefit_system = baseline_tax_benefit_system,
            )
        if data is None:
            return

        if 'input_data_frame_by_entity_by_period' in data:
            period = periods.period(year)
            dataframe_variables = set()
            for entity_dataframe in data['input_data_frame_by_entity_by_period'][period].values():
                if not isinstance(entity_dataframe, pd.DataFrame):
                    continue
                dataframe_variables = dataframe_variables.union(set(entity_dataframe.columns))
            self.used_as_input_variables = list(
                set(tax_benefit_system.variables.keys()).intersection(dataframe_variables)
                )

        elif 'input_data_frame' in data:
            input_data_frame = data.get('input_data_frame')
            self.used_as_input_variables = list(
                set(tax_benefit_system.variables.keys()).intersection(
                    set(input_data_frame.columns)
                    ))

        if varying_variable:
            self.varying_variable = varying_variable

        self.init_from_data(data = data)


    def custom_initialize(self, simulation):
        if simulation == self.baseline_simulation:
            return

        varying_variable = self.varying_variable
        assert varying_variable in self.baseline_tax_benefit_system.variables
        period = self.year
        varying_variable_value = self.baseline_simulation.calculate(varying_variable, period = period)
        delta = .03 * varying_variable_value
        new_variable_value = varying_variable_value + delta
        simulation.delete_arrays(varying_variable, period)
        simulation.set_input(varying_variable, period, new_variable_value)

    def compute_marginal_tax_rate(self, target_variable = None, period = None):
        varying_variable = self.varying_variable
        assert target_variable in self.tax_benefit_system.variables
        target = self.simulation.calculate(target_variable, period = period)
        baseline_target = self.baseline_simulation.calculate(target_variable, period = period)
        varying = self.simulation.calculate(varying_variable, period = period)
        baseline_varying = self.baseline_simulation.calculate(varying_variable, period = period)
        marginal_rate = 1 - (target - baseline_target) / (varying - baseline_varying)
        return marginal_rate
