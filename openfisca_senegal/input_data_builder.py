
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
    person_variables = [
        'age',
        'hhid',
        'link_to_head',
        'mstatus_ind',
        'inc_pension_ind',
        'weight_pc',
        'sex',
        'wage_formal_ind',
        ]

    person_dataframe = dataframe[person_variables].copy()
    person_dataframe['age'] = person_dataframe['age'].replace({
        "98 ans et plus": "98.0",
        "NSP": "50.0",
        }).fillna("50").astype(float).astype(int)

    person_dataframe['salaire_imposable'] = person_dataframe.wage_formal_ind
    assert (person_dataframe.mstatus_ind.isin([
        "Celibataire",
        "Marie",
        "Non concerne",
        "Veuf, Divorce",
        ])).all()
    person_dataframe['statut_marital'] = person_dataframe.mstatus_ind.map({
        "Marie": 0,
        "Celibataire": 1,
        "Veuf, Divorce": 2,
        "Non concerne": 3,
        })
    assert (person_dataframe.statut_marital.isin([0, 1, 2, 3])).all()
    # print(person_dataframe.link_to_head.value_counts())
    person_dataframe['household_role_index'] = (
        0 * (person_dataframe.link_to_head == 1)
        + 1 * (person_dataframe.link_to_head == 2)
        + 2 * (person_dataframe.link_to_head > 2)
        )

    household_id_by_hhid = (person_dataframe.hhid
        .drop_duplicates()
        .sort_values()
        .reset_index(drop = True)
        .reset_index()
        .rename(columns = {'index': 'household_id'})
        .set_index('hhid')
        .squeeze()
        )
    person_dataframe['household_id'] = person_dataframe['hhid'].map(household_id_by_hhid)
    person_dataframe['person_id'] = range(len(person_dataframe))
    person_dataframe = person_dataframe.rename(columns = {
        'inc_pension_ind': 'pension',
        'sex': 'sexe',
        'weight_pc': 'person_weight',
        })

    assert (dataframe.groupby('hhid')['weight_pc'].nunique() == 1).all()

    household_weight = dataframe.groupby('hhid')['weight_pc'].mean()
    household_dataframe = pd.DataFrame(
        dict(
            household_id = range(person_dataframe.household_id.max() + 1),
            household_weight = household_weight.values,
            )
        )
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
    data = create_data_from_stata()
