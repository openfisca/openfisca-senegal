from openfisca_senegal import CountryTaxBenefitSystem as SenegalTaxBenfitSystem
from openfisca_senegal.scenarios import init_single_entity


def test_senario():
    scenario = SenegalTaxBenfitSystem().new_scenario()
    init_single_entity(
        scenario,
        parent1 = {
            'salaire_imposable': 2800000,
            'est_marie': True,
            'conjoint_a_des_revenus': False,
            'nombre_enfants': 1,
            },
        period = '2017',
        )
