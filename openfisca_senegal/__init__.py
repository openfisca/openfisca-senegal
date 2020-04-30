import configparser
import logging
import os


from openfisca_core.taxbenefitsystems import TaxBenefitSystem
from openfisca_senegal import entities


log = logging.getLogger(__name__)


COUNTRY_DIR = os.path.dirname(os.path.abspath(__file__))


class CountryTaxBenefitSystem(TaxBenefitSystem):
    def __init__(self, coicop = True, inversion = True):
        super(CountryTaxBenefitSystem, self).__init__(entities.entities)
        self.add_variables_from_directory(os.path.join(COUNTRY_DIR, 'variables'))
        param_path = os.path.join(COUNTRY_DIR, 'parameters')
        self.load_parameters(param_path)
        if coicop:
            try:
                from openfisca_ceq.tests.test_indirect_tax_variables_generator import add_coicop_item_to_tax_benefit_system
                add_coicop_item_to_tax_benefit_system(self, country = "senegal")
            except (configparser.NoSectionError, ModuleNotFoundError) as e:
                log.info("No coicop consumption variable: \n")
                log.info(e)
                log.info("Passing")
        self.legislation_country = "senegal"
        if inversion:
            from openfisca_senegal.inversion import (
                pension_retraite_brut,
                revenu_foncier_brut,
                revenu_non_salarie_brut,
                salaire_brut,
                )

            self.update_variable(pension_retraite_brut)
            self.update_variable(revenu_foncier_brut)
            self.update_variable(revenu_non_salarie_brut)
            self.update_variable(salaire_brut)
