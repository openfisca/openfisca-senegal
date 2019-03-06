# -*- coding: utf-8 -*-


from openfisca_core import conv
from openfisca_core.scenarios import AbstractScenario


class Scenario(AbstractScenario):
    def init_single_entity(self, axes = None, enfants = None, household = None, parent1 = None, parent2 = None,
            period = None):
        if enfants is None:
            enfants = []
        assert parent1 is not None
        household = household.copy() if household is not None else {}
        persons = []
        for index, person in enumerate([parent1, parent2] + (enfants or [])):
            if person is None:
                continue
            id = person.get('id')
            if id is None:
                person = person.copy()
                person['id'] = id = 'ind{}'.format(index)
            persons.append(person)
            if index <= 1:
                household.setdefault('parents', []).append(id)
            else:
                household.setdefault('enfants', []).append(id)
        household.setdefault('enfants', [])
        conv.check(self.make_json_or_python_to_attributes())(dict(
            axes = axes,
            period = period,
            test_case = dict(
                households = [household],
                persons = persons,
                ),
            ))
        return self
