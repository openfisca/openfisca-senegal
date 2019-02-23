# -*- coding: utf-8 -*-


import configparser
import logging
import os
import pandas as pd


from openfisca_survey_manager import default_config_files_directory as config_files_directory
from openfisca_core import periods


log = logging.getLogger(__file__)


config_parser = configparser.SafeConfigParser()
config_parser.read(os.path.join(config_files_directory, 'raw_data.ini'))
data_is_available = config_parser.has_section("senegal")
if not data_is_available:
    log.info("No data available for Sénégal")


def get_data_file_path():
    file_path_by_year = dict(config_parser.items("senegal"))
    return file_path_by_year['2011']


def create_dataframes_from_stata_data():
    data_file_path = get_data_file_path()
    import pprint
    dico_labels = pd.read_stata(data_file_path, iterator=True)
    pprint.pprint(dico_labels.variable_labels())
    dataframe = pd.read_stata(data_file_path)
    person_variables = [
        'age',
        'link_to_head',
        'sex',
        'wage_formal_ind',
        ]
    person_dataframe = dataframe[person_variables].copy()
    person_dataframe['salaire'] = person_dataframe.wage_formal_ind
    print(person_dataframe.link_to_head.value_counts())
    # person_dataframe['household_legacy_role'] = (
    #     0 * (person_dataframe.link_to_head == 'chef de menage')
    #     + 1 * (person_dataframe.link_to_head == 'epouse ou mari')
    #     + 2 * (
    #         (person_dataframe.link_to_head != 'chef de menage') & (person_dataframe.link_to_head != 'epouse ou mari')
    #         )
    #     )

    # household_id_by_hhid = (person_dataframe.hhid
    #     .drop_duplicates()
    #     .sort_values()
    #     .reset_index(drop = True)
    #     .reset_index()
    #     .rename(columns = {'index': 'household_id'})
    #     .set_index('hhid')
    #     .squeeze()
    #     )

    # person_dataframe['household_id'] = person_dataframe['hhid'].map(household_id_by_hhid)
    person_dataframe['person_id'] = range(len(person_dataframe))
    # person_dataframe = person_dataframe.rename(columns = {
    #     'inc_pension_ind': 'pension',
    #     'sex': 'sexe',
    #     'pond': 'person_weight',
    #     })

    # assert (dataframe.groupby('hhid')['weight'].nunique() == 1).all()

    # household_weight = dataframe.groupby('hhid')['weight'].mean()
    # household_dataframe = pd.DataFrame(
    #     dict(
    #         household_id = range(person_dataframe.household_id.max() + 1),
    #         household_weight = household_weight.values,
    #         )
    #     )

    return person_dataframe, household_dataframe


def create_data_from_stata(create_dataframes = True):
    year = 2017
    data = dict()

    if create_dataframes:
        person_dataframe, household_dataframe = create_dataframes_from_stata_data()
        input_data_frame_by_entity = {
            'person': person_dataframe,
            'household': household_dataframe,
            }
        input_data_frame_by_entity_by_period = {periods.period(year): input_data_frame_by_entity}
        data['input_data_frame_by_entity_by_period'] = input_data_frame_by_entity_by_period

    else:
        data_file_path = get_data_file_path()
        data['stata_file_by_entity'] = dict(
            # household = os.path.join(data_directory, 'household.dta'),
            person = data_file_path,
            )
    return data


if __name__ == '__main__':
    import sys
    logging.basicConfig(level = logging.DEBUG, stream = sys.stdout)
    person_dataframe, household_dataframe = create_dataframes_from_stata_data()
