import numpy as np
from numpy.testing import assert_allclose

from openfisca_core.rates import marginal_rate


from openfisca_senegal import CountryTaxBenefitSystem as SenegalTaxBenfitSystem
from openfisca_senegal.scenarios import init_single_entity
from openfisca_senegal.inversion import compute_bareme_retraite


def test_inversion_pension():
    scenario = SenegalTaxBenfitSystem().new_scenario()
    period = 2011
    nombre_de_parts_values = np.linspace(1, 5, 8 + 1)
    for nombre_de_parts_value in nombre_de_parts_values:
        init_single_entity(
            scenario,
            parent1 = {
                'salaire_brut': 0,
                'conjoint_a_des_revenus': False,
                'nombre_de_parts': nombre_de_parts_value,
                },
            axes = [[{
                'count': 1000,
                'min': 0,
                'max': 20e6,
                'name': 'pension_retraite_brut',
                }]],
            period = period,
            )
        simulation = scenario.new_simulation()
        pension_retraite_brut = simulation.calculate('pension_retraite_brut', period)
        droit_progressif_pension_retraite = simulation.calculate('droit_progressif_pension_retraite', period)
        droit_progressif = simulation.calculate('droit_progressif', period)

        adjusted_bareme = compute_bareme_retraite(scenario.tax_benefit_system.parameters, period, nombre_de_parts_value)
        droit_progressif_adjusted = nombre_de_parts_value * adjusted_bareme.calc(pension_retraite_brut / nombre_de_parts_value)

        assert_allclose(
            droit_progressif,
            droit_progressif_adjusted,
            rtol = 1e-6,
            atol = 1,
            )

        assert_allclose(
            droit_progressif_pension_retraite,
            droit_progressif_adjusted,
            rtol = 1e-6,
            atol = 1,
            )

        # assert_allclose(
        #     marginal_rate(pension_retraite_brut - droit_progressif, pension_retraite_brut),
        #     marginal_rate(pension_retraite_brut - adjusted_bareme.calc(pension_retraite_brut), pension_retraite_brut),
        #     rtol = 1e-3,
        #     )
