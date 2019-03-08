# -*- coding: utf-8 -*-

import logging

log = logging.getLogger(__name__)


# def init_single_entity(scenario, axes = None, enfants = None, household = None, parent1 = None, parent2 = None,
#         period = None):
#     if enfants is None:
#         enfants = []
#     assert parent1 is not None
#     household = household.copy() if household is not None else {}
#     persons = []
#     for index, person in enumerate([parent1, parent2] + (enfants or [])):
#         if person is None:
#             continue
#         id = person.get('id')
#         if id is None:
#             person = person.copy()
#             person['id'] = id = 'ind{}'.format(index)
#         persons.append(person)
#         if index <= 1:
#             household.setdefault('parents', []).append(id)
#         else:
#             household.setdefault('enfants', []).append(id)
#     household.setdefault('enfants', [])
#     conv.check(self.make_json_or_python_to_attributes())(dict(
#         axes = axes,
#         period = period,
#         test_case = dict(
#             households = [household],
#             persons = persons,
#             ),
#         ))
#     return self


def init_single_entity(scenario, axes = None, enfants = None, household = None, parent1 = None, parent2 = None, period = None):
    if enfants is None:
        enfants = []
    assert parent1 is not None

    households = {}
    individus = {}

    count_so_far = 0
    for nth in range(0, 1):
        household_nth = household.copy() if household is not None else {}
        group = [parent1, parent2] + (enfants or [])
        for index, individu in enumerate(group):
            if individu is None:
                continue
            id = individu.get('id')
            if id is None:
                individu = individu.copy()
                id = 'ind{}'.format(index + count_so_far)
            individus[id] = individu
            if index <= 1:
                if index == 0:
                    household_nth['personne_de_reference'] = id
                else:
                    household_nth['conjoint'] = id
            else:
                household_nth.setdefault('enfants', []).append(id)

        count_so_far += len(group)
        households["m{}".format(nth)] = household_nth

    test_data = {
        'period': period,
        'households': households,
        'individus': individus
        }
    if axes:
        test_data['axes'] = axes
    scenario.init_from_dict(test_data)
    return scenario
