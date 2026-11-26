# OpenFisca Sénégal

Senegalese tax and benefit system for OpenFisca.

> Warning: this is highly experimental!

## Rôle dans l'écosystème CEQ

Ce paquet fournit le système socio-fiscal du **Sénégal** sous forme de
`CountryTaxBenefitSystem` OpenFisca. Il est consommé par les analyses
[Commitment to Equity (CEQ)](https://github.com/openfisca/openfisca-ceq) :
le cœur [`openfisca-ceq`](https://github.com/openfisca/openfisca-ceq) y greffe les
variables de concepts de revenu CEQ via `add_ceq_framework`, et l'étude
[`openfisca-ceq-afrique-ouest`](https://github.com/openfisca/openfisca-ceq-afrique-ouest)
en fait l'un de ses trois pays (avec le Mali et la Côte d'Ivoire).

```python
from openfisca_senegal import CountryTaxBenefitSystem
from openfisca_ceq.tools.tax_benefit_system_ceq_completion import add_ceq_framework

tbs = CountryTaxBenefitSystem()
add_ceq_framework(tbs, ...)  # voir la doc du cœur openfisca-ceq
```

### Variables

Les variables sont organisées sous `openfisca_senegal/variables/` :
caractéristiques socio-démographiques, revenus, consommation, prestations, et
prélèvements obligatoires (impôts directs / indirects, prélèvements sociaux).

## OGP Paris Hackathon
This work was done during the first [OGP hackathon in Paris](https://en.2016.ogpsummit.org/osem/conference/ogp-summit/)

See the [Jupyter Notebook](/notebooks/hackathon_ogp_paris.ipynb) or [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/openfisca/senegal/master?filepath=notebooks%2Fhackathon_ogp_paris.ipynb).


## Dakar Hackathon for technological innovation for the Senegalese tax administration
This work was done during the first [hackathon in Dakar for Innovation and Collaboration for the Senegalese Tax System](http://www.imf.org/en/News/Events/Hackathon-Technological-Innovation-for-the-Senegalese-Tax-Administration)

See the [Jupyter Notebook](/notebooks/Senegalese%20tax%20and%20benefit%20system%20from%20scratch.ipynb) or [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/openfisca/senegal/master?filepath=notebooks%2FSenegalese%20tax%20and%20benefit%20system%20from%20scratch.ipynb).

## Links

- http://www.gouv.sn/IMG/pdf/cgi2013.pdf
- http://www.impotsetdomaines.gouv.sn/sites/default/files/formulaires/ir_declarationsanspagedegarde.pdf
- http://www.impotsetdomaines.gouv.sn/fr/simulateur-dimpots

## API

### Installation

```sh
make install # needs to be executed in the folder containing the Makefile
```

### Testing

```sh
make test # needs to be executed in the folder containing the Makefile
```

### Run with the Web API

```sh
pip install OpenFisca-Web-API[paster]
paster serve api/api_config.ini
```

To test with a sample file:

```sh
curl http://localhost:2000/api/1/calculate -X POST --data @./api/test.json --header 'Content-type: application/json'
```
