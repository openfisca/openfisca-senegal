# -*- coding: utf-8 -*-

import os
import xml.etree.ElementTree

from openfisca_core import conv, legislationsxml
from openfisca_core.taxbenefitsystems import TaxBenefitSystem

from . import entities, scenarios


COUNTRY_DIR = os.path.dirname(os.path.abspath(__file__))


class SenegalTaxBenefitSystem(TaxBenefitSystem):
    """Senegalese tax and benefit system"""
    CURRENCY = u"FCFA"

    def __init__(self):
        super(SenegalTaxBenefitSystem, self).__init__(entities.entities)
        self.Scenario = scenarios.Scenario

    def add_legislation_params(self, xml_string):
        def input_to_xml_element(value, state=None):
            return xml.etree.ElementTree.fromstring(value.encode('utf-8')), None

        self._legislation_json = conv.check(conv.pipe(
            input_to_xml_element,
            legislationsxml.xml_legislation_to_json,
            legislationsxml.validate_legislation_xml_json,
            conv.function(lambda value: legislationsxml.transform_node_xml_json_to_json(value)[1]),
            ))(xml_string)