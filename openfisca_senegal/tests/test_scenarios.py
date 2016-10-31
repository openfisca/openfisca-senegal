# -*- coding: utf-8 -*-

from __future__ import division

import datetime

from openfisca_core import periods
from openfisca_core.tools import assert_near
from nose.tools import assert_equal

from openfisca_senegal import SenegalTaxBenefitSystem


tax_benefit_system = SenegalTaxBenefitSystem()


def test_basic_scenario():
    period = periods.period('2015')
    scenario = tax_benefit_system.new_scenario()
    scenario.init_single_entity(
        period=period,
        parent1=dict(
            date_de_naissance=datetime.date(1972, 1, 1),
            salaire=50000,
            ),
        )
    simulation = scenario.new_simulation()
    salaire = simulation.calculate('salaire', period)
    assert_equal(salaire, [50000])
    impot_revenu = simulation.calculate('impot_revenu', period)
    assert_near(impot_revenu, [15000], absolute_error_margin=0.01)
