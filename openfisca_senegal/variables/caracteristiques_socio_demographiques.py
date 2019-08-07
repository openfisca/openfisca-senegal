# -*- coding: utf-8 -*-


from openfisca_core.model_api import *
from openfisca_senegal.entities import *


class est_marie(Variable):
    value_type = bool
    entity = Individu
    label = u"Est marié"
    set_input = set_input_dispatch_by_period
    definition_period = YEAR


class est_divorce(Variable):
    value_type = bool
    entity = Individu
    label = u"Est divorcé"
    definition_period = YEAR
    set_input = set_input_dispatch_by_period


class est_veuf(Variable):
    value_type = bool
    entity = Individu
    label = u"Est veuf"
    definition_period = YEAR
    set_input = set_input_dispatch_by_period


class est_celibataire(Variable):
    value_type = bool
    entity = Individu
    label = u"Est célibataire"
    definition_period = YEAR
    set_input = set_input_dispatch_by_period


class nombre_enfants(Variable):
    value_type = int
    entity = Individu
    definition_period = YEAR


class date_naissance(Variable):
    value_type = date
    default_value = date(1970, 1, 1)
    entity = Individu
    label = u"Date de naissance"
    definition_period = ETERNITY  # This variable cannot change over time.


class age(Variable):
    value_type = int
    entity = Individu
    definition_period = YEAR
    label = u"Âge de l'individu (en années)"

    # A person's age is computed according to its birth date.
    def formula(individu, period, parameters):
        date_naissance = individu('date_naissance', period)
        birth_year = date_naissance.astype('datetime64[Y]').astype(int) + 1970
        birth_month = date_naissance.astype('datetime64[M]').astype(int) % 12 + 1
        birth_day = (date_naissance - date_naissance.astype('datetime64[M]') + 1).astype(int)

        is_birthday_past = (
            (birth_month < period.start.month) + (birth_month == period.start.month) * (birth_day <= period.start.day)
            )
        # If the birthday is not passed this year, subtract one year
        return (period.start.year - birth_year) - where(is_birthday_past, 0, 1)
