# -*- coding: utf-8 -*-

import os

from openfisca_core.taxbenefitsystems import TaxBenefitSystem

from . import entities, scenarios


COUNTRY_DIR = os.path.dirname(os.path.abspath(__file__))


class SenegalTaxBenefitSystem(TaxBenefitSystem):
    """Senegalese tax and benefit system"""

    def __init__(self):
        TaxBenefitSystem.__init__(self, entities.entities)
        self.Scenario = scenarios.Scenario
        self.add_variables_from_file(os.path.join(COUNTRY_DIR, 'model.py'))
