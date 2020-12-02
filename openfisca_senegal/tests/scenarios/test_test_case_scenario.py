from openfisca_senegal import CountryTaxBenefitSystem as SenegalTaxBenfitSystem
from openfisca_senegal.scenarios import init_single_entity


def test_senario():
    scenario = SenegalTaxBenfitSystem().new_scenario()
    init_single_entity(
        scenario,
        parent1 = {
            'salaire_imposable': 2800000,
            'marie': True,
            'conjoint_a_des_revenus': False,
            'nombre_enfants': 1,
            },
        period = '2017',
        )


def test_senario_pension():
    scenario = SenegalTaxBenfitSystem().new_scenario()
    period = 2011
    init_single_entity(
        scenario,
        parent1 = {
            'salaire_brut': 0,
            'conjoint_a_des_revenus': False,
            'nombre_enfants': 1,
            },
        axes = [[{
            'count': 100,
            'min': 0,
            'max': 15e6,
            'name': 'pension_retraite_brut',
            }]],
        period = period,
        )

    from matplotlib import pyplot as plt
    simulation = scenario.new_simulation()
    plt.plot(
        simulation.calculate('pension_retraite_brut', period),
        simulation.calculate('droit_progressif', period),
        )


if __name__ == "__main__":
    test_senario_pension()
