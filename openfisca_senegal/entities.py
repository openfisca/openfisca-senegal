# -*- coding: utf-8 -*-


from openfisca_core.entities import AbstractEntity


class Familles(AbstractEntity):
    index_for_person_variable_name = 'id_famille'
    key_plural = 'familles'
    key_singular = 'famille'
    label = u'Famille'
    max_cardinality_by_role_key = {'parents': 2}
    role_for_person_variable_name = 'role_dans_famille'
    roles_key = ['parents', 'enfants']
    label_by_role_key = {
        'enfants': u'Enfants',
        'parents': u'Parents',
        }
    symbol = 'fam'

    def iter_member_persons_role_and_id(self, member):
        role = 0

        parents_id = member['parents']
        assert 1 <= len(parents_id) <= 2
        for parent_role, parent_id in enumerate(parents_id, role):
            assert parent_id is not None
            yield parent_role, parent_id
        role += 2

        enfants_id = member.get('enfants')
        if enfants_id is not None:
            for enfant_role, enfant_id in enumerate(enfants_id, role):
                assert enfant_id is not None
                yield enfant_role, enfant_id


class Individus(AbstractEntity):
    is_persons_entity = True
    key_plural = 'individus'
    key_singular = 'individu'
    label = u'Personne'
    symbol = 'ind'


entities = [Familles, Individus]
