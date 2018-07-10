# OpenFisca Sénégal

Senegalese tax and benefit system for OpenFisca

> Warning: this is highly experimental!

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
