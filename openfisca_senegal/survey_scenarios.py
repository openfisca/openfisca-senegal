# -*- coding: utf-8 -*-

import pandas as pd

from openfisca_core import periods
from openfisca_survey_manager.scenarios import AbstractSurveyScenario
from openfisca_survey_manager.utils import stata_files_to_data_frames

from openfisca_senegal import CountryTaxBenefitSystem as SenegalTaxBenefitSystem


class SenegalSurveyScenario(AbstractSurveyScenario):
    weight_column_name_by_entity = dict(
        menage = 'menage_weight',
        individu = 'individu_weight',
        )

    def __init__(self, tax_benefit_system = None, baseline_tax_benefit_system = None,
            data = None, year = None):
        super(SenegalSurveyScenario, self).__init__()
        if tax_benefit_system is None:
            tax_benefit_system = SenegalTaxBenefitSystem()
        self.set_tax_benefit_systems(
            tax_benefit_system = tax_benefit_system,
            baseline_tax_benefit_system = baseline_tax_benefit_system,
            )

        assert year is not None
        self.year = year

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

        else:
            variables_from_stata_files = stata_files_to_data_frames(data, period = year)
            self.used_as_input_variables = list(
                set(tax_benefit_system.variables.keys()).intersection(
                    set(variables_from_stata_files)
                    )
                )
            period = data["input_data_frame_by_entity_by_period"].keys()[0]
            input_data_frame_by_entity = data["input_data_frame_by_entity_by_period"].values()[0]
            individu_data_frame = input_data_frame_by_entity['individu']
            individu_data_frame['menage_id'] = individu_data_frame.id
            individu_data_frame['individu_id'] = individu_data_frame.id
            individu_data_frame['menage_legacy_role'] = 0
            data["input_data_frame_by_entity_by_period"][period] = dict(individu = individu_data_frame)

        self.init_from_data(data = data)
