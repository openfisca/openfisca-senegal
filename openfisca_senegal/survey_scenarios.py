import pandas as pd


from openfisca_core import periods
from openfisca_survey_manager.scenarios.reform_scenario import ReformScenario


from openfisca_senegal import CountryTaxBenefitSystem as SenegalTaxBenefitSystem


class SenegalSurveyScenario(ReformScenario):
    weight_variable_by_entity = dict(
        household = 'household_weight',
        person = 'person_weight',
        )
    varying_variable = None

    def __init__(self, tax_benefit_system = None, baseline_tax_benefit_system = None, period = None,
            data = None, use_marginal_tax_rate = False, varying_variable = None, variation_factor = 0.03):
        super(SenegalSurveyScenario, self).__init__()
        assert period is not None
        self.period = period

        if tax_benefit_system is None:
            tax_benefit_system = SenegalTaxBenefitSystem()
        if baseline_tax_benefit_system is not None:
            self.set_tax_benefit_systems(
                tax_benefit_systems = {"reform" : tax_benefit_system, "baseline" : baseline_tax_benefit_system},
                )
        else:
            self.set_tax_benefit_systems(
                tax_benefit_systems = {"baseline" : tax_benefit_system},
                )

        if use_marginal_tax_rate:
            assert varying_variable is not None
            assert varying_variable in self.tax_benefit_system.variables
            self.variation_factor = variation_factor
            self.varying_variable = varying_variable

        if data is None:
            return

        if 'input_data_frame_by_entity_by_period' in data:
            period = periods.period(period)
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

        self.init_from_data(data = data, use_marginal_tax_rate = use_marginal_tax_rate)
