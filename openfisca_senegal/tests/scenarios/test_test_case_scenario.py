from openfisca_senegal import CountryTaxBenefitSystem as SenegalTaxBenfitSystem


def test_senario():
    scenario = SenegalTaxBenfitSystem().new_scenario()

    scenario.init_single_entity(
        parent1 = {
            'salaire': 2800000,
            'est_marie': True,
            'conjoint_a_des_revenus': False,
            'nombre_enfants': 1,
            },
        period = '2017',
        )
