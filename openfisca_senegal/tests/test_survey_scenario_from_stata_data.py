# -*- coding: utf-8 -*-


import logging
import os
from openfisca_senegal.input_data_builder import (
    data_is_available,
    create_data_from_stata,
    )
from openfisca_senegal.survey_scenarios import SenegalSurveyScenario


log = logging.getLogger(__file__)


def test_survey_scenario(create_dataframes = True):
    circleci = 'CIRCLECI' in os.environ
    if circleci or not data_is_available:
        return

    year = 2017
    data = create_data_from_stata(create_dataframes = create_dataframes)
    survey_scenario = SenegalSurveyScenario(
        data = data,
        year = year,
        )
    df_by_entity = survey_scenario.create_data_frame_by_entity(
        variables = ['age', 'salaire', 'impot_avant_reduction_famille', 'impot_revenus']
        )

    for entity, df in df_by_entity.items():
        assert not df.empty, "{} dataframe is empty".format(entity)
        log.debug(df)


if __name__ == '__main__':
    import sys
    logging.basicConfig(level = logging.DEBUG, stream = sys.stdout)
    test_survey_scenario()
