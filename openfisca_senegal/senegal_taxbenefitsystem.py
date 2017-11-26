# -*- coding: utf-8 -*-

import os

from openfisca_core.taxbenefitsystems import TaxBenefitSystem

from . import entities, scenarios


COUNTRY_DIR = os.path.dirname(os.path.abspath(__file__))


class SenegalTaxBenefitSystem(TaxBenefitSystem):
    """Senegalese tax and benefit system"""
    CURRENCY = u"FCFA"

    def __init__(self):
        super(SenegalTaxBenefitSystem, self).__init__(entities.entities)
        self.Scenario = scenarios.Scenario
        self.add_variables_from_file(os.path.join(COUNTRY_DIR, 'model.py'))
        self.load_parameters(os.path.join(COUNTRY_DIR, 'parameters'))
