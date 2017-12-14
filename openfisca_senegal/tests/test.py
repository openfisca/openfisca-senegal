# -*- coding: utf-8 -*-

from openfisca_senegal import CountryTaxBenefitSystem as SenegalTBS

tax_benefit_system = SenegalTBS()

scenario = tax_benefit_system.new_scenario()

scenario.init_single_entity(
    parent1 = {
        'salaire': 1800000,
        'est_marie': True,
        'conjoint_a_des_revenus': False,
        'nombre_enfants': 2,
        },
    period='2015',
    )

simulation = scenario.new_simulation()

print('Salaire retenu :')
print(simulation.individu('salaire', period='2015'))
print('Impot avant réduction famille :')
print(simulation.individu('impot_avant_reduction_famille', period='2015'))
print('Réduction pour charge famille :')
print(simulation.individu('reduction_impots_pour_charge_famille', period='2015'))
print('Impot pour la famille :')
print(simulation.individu('impot_revenus', period='2015'))
