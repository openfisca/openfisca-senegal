from openfisca_core.model_api import *
from openfisca_senegal.entities import *


class salaire_brut(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Salaire brut"

    def formula(person, period, parameters):
        salaire = person('salaire', period)
        bareme = parameters(period).prelevements_obligatoires.impots_directs.bareme_impot_progressif.copy()
        retraite = parameters(period).prelevements_obligatoires.prelevements_sociaux.retraite.salarie_ipres.copy()
        retraite_complementaire = parameters(period).prelevements_obligatoires.prelevements_sociaux.retraite.salarie_cadres.copy()
        prelevements_sociaux = retraite.copy()
        prelevements_sociaux.add_tax_scale(retraite_complementaire)
        salaire_imposable = bareme.inverse().calc(salaire)
        salaire_brut = 12 * prelevements_sociaux.inverse().calc(salaire_imposable / 12)
        return salaire_brut
