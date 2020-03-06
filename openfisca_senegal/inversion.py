from openfisca_core.model_api import *
from openfisca_mali.entities import *


class salaire_brut(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Salaire brut"

    def formula(person, period, parameters):
        salaire = person('salaire', period)

        impot_traitement_salaire = parameters(period).prelevements_obligatoires.impots_directs.impot_traitement_salaire.copy()

        retraite = parameters(period).prelevements_obligatoires.prelevements_sociaux.retraite.salarie.copy()
        retraite_complementaire = parameters(period).prelevements_obligatoires.prelevements_sociaux..retraite_complementaire.salarie

        prelevements_sociaux = retraite.copy()
        prelevements_sociaux.add_tax_scale(maladie)
        salaire_imposable = impot_traitement_salaire.inverse().calc(salaire)
        salaire_brut = 12 * prelevements_sociaux.inverse().calc(salaire_imposable / 12)
        return salaire_brut
