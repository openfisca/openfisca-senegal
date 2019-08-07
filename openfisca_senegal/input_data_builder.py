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
    # dico_labels = pd.read_stata(data_file_path, iterator=True)
    # import pprint
    # pprint.pprint(dico_labels.variable_labels())
    dataframe = pd.read_stata(data_file_path)
    individu_variables = [
        'age',
        'hhid',
        'link_to_head',
        'mstatus_ind',
        'inc_pension_ind',
        'weight_pc',
        'sex',
        'wage_formal_ind',
        ]

    individu_dataframe = dataframe[individu_variables].copy()
    individu_dataframe['age'] = individu_dataframe['age'].replace({
        "98 ans et plus": "98.0",
        "NSP": "50.0",
        }).fillna("50").astype(float).astype(int)

    individu_dataframe['salaire'] = individu_dataframe.wage_formal_ind
    assert (individu_dataframe.mstatus_ind.isin([
        "Celibataire",
        "Marie",
        "Non concerne",
        "Veuf, Divorce",
        ])).all()
    individu_dataframe['statut_marital'] = individu_dataframe.mstatus_ind.map({
        "Marie": 0,
        "Celibataire": 1,
        "Veuf, Divorce": 2,
        "Non concerne": 3,
        })
    assert (individu_dataframe.statut_marital.isin([0, 1, 2, 3])).all()
    # print(individu_dataframe.link_to_head.value_counts())
    individu_dataframe['menage_legacy_role'] = (
        0 * (individu_dataframe.link_to_head == 1)
        + 1 * (individu_dataframe.link_to_head == 2)
        + 2 * (individu_dataframe.link_to_head > 2)
        )

    menage_id_by_hhid = (individu_dataframe.hhid
        .drop_duplicates()
        .sort_values()
        .reset_index(drop = True)
        .reset_index()
        .rename(columns = {'index': 'menage_id'})
        .set_index('hhid')
        .squeeze()
        )
    individu_dataframe['menage_id'] = individu_dataframe['hhid'].map(menage_id_by_hhid)
    individu_dataframe['individu_id'] = range(len(individu_dataframe))
    individu_dataframe = individu_dataframe.rename(columns = {
        'inc_pension_ind': 'pension',
        'sex': 'sexe',
        'weight_pc': 'individu_weight',
        })

    assert (dataframe.groupby('hhid')['weight_pc'].nunique() == 1).all()

    menage_weight = dataframe.groupby('hhid')['weight_pc'].mean()
    menage_dataframe = pd.DataFrame(
        dict(
            menage_id = range(individu_dataframe.menage_id.max() + 1),
            menage_weight = menage_weight.values,
            )
        )
    return individu_dataframe, menage_dataframe


def create_data_from_stata(create_dataframes = True):
    year = 2017
    data = dict()

    if create_dataframes:
        individu_dataframe, menage_dataframe = create_dataframes_from_stata_data()
        input_data_frame_by_entity = {
            'individu': individu_dataframe,
            'menage': menage_dataframe,
            }
        input_data_frame_by_entity_by_period = {periods.period(year): input_data_frame_by_entity}
        data['input_data_frame_by_entity_by_period'] = input_data_frame_by_entity_by_period

    else:
        data_file_path = get_data_file_path()
        data['stata_file_by_entity'] = dict(
            # menage = os.path.join(data_directory, 'menage.dta'),
            individu = data_file_path,
            )
    return data


if __name__ == '__main__':
    import sys
    logging.basicConfig(level = logging.DEBUG, stream = sys.stdout)
    individu_dataframe, menage_dataframe = create_dataframes_from_stata_data()
    data = create_data_from_stata()
