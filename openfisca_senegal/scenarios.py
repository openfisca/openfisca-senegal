# -*- coding: utf-8 -*-


from openfisca_core import conv
from openfisca_core.scenarios import AbstractScenario


class Scenario(AbstractScenario):
    def init_single_entity(self, axes = None, enfants = None, menage = None, parent1 = None, parent2 = None,
            period = None):
        if enfants is None:
            enfants = []
        assert parent1 is not None
        menage = menage.copy() if menage is not None else {}
        individus = []
        for index, individu in enumerate([parent1, parent2] + (enfants or [])):
            if individu is None:
                continue
            id = individu.get('id')
            if id is None:
                individu = individu.copy()
                individu['id'] = id = 'ind{}'.format(index)
            individus.append(individu)
            if index <= 1:
                menage.setdefault('parents', []).append(id)
            else:
                menage.setdefault('enfants', []).append(id)
        menage.setdefault('enfants', [])
        conv.check(self.make_json_or_python_to_attributes())(dict(
            axes = axes,
            period = period,
            test_case = dict(
                menages = [menage],
                individus = individus,
                ),
            ))
        return self
