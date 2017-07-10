# -*- coding: utf-8 -*-

from datetime import date

from openfisca_core.model_api import *

from numpy import maximum as max_, minimum as min_, logical_not as not_, where, select

from openfisca_senegal.entities import Famille, Individu
