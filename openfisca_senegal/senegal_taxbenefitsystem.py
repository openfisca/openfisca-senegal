# -*- coding: utf-8 -*-

import os

from openfisca_core.taxbenefitsystems import TaxBenefitSystem

from openfisca_senegal import entities


COUNTRY_DIR = os.path.dirname(os.path.abspath(__file__))


class SenegalTaxBenefitSystem(TaxBenefitSystem):
    """Senegalese tax and benefit system"""
    CURRENCY = u"FCFA"

    def __init__(self):
        super(SenegalTaxBenefitSystem, self).__init__(entities.entities)
        self.add_variables_from_directory(os.path.join(COUNTRY_DIR, 'variables'))
        self.load_parameters(os.path.join(COUNTRY_DIR, 'parameters'))
