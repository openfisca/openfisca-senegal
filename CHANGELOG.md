# Changelog

### 0.11.2 [#103](https://github.com/openfisca/openfisca-senegal/pull/103)

* Corrige la CI pour publier le paquet sur PyPi

### 0.11.1 [#100](https://github.com/openfisca/openfisca-senegal/pull/100)

* Corrige la CI pour publier le paquet sur PyPi

## 0.11.0 [#99](https://github.com/openfisca/openfisca-senegal/pull/99)

* Met à jour vers Python 3.11.
* Adaptation aux dernières versions d'Openfisca-Survey-Manager : modifications dans le survey-scenario
* Remplace la CircleCI par Github Action

## 0.10.3 [#86](https://github.com/openfisca/openfisca-senegal/pull/86)

* Fix CI and weights

### 0.9.2 [#58](https://github.com/openfisca/openfisca-senegal/pull/58)

* Mise à jour des dépendances notamment openfisca-ceq

### 0.9.1 [#52](https://github.com/openfisca/openfisca-senegal/pull/52)

* Amélioration technique
  - Utilise une notation cohérente pour `variation_factor`

## 0.9.0 [#51](https://github.com/openfisca/openfisca-senegal/pull/51)

* Amélioration technique
  - Permet de calculer le taux marginal d'imposition

## 0.8.0 [#39](https://github.com/openfisca/openfisca-senegal/pull/39)

* Amélioration technique
  - Construction des bases individus et ménages à partir des données brutes pour injection dans un SurveyScenario
  - Adapte à la dernière version de core (34.2.0) et survey-manager (0.20)
  - Ajoute variables de poids
  - Modifie les entités pour suivre celle de CEQ (comme Côte d'Ivoire et Mali)

## 0.7.6 [#37](https://github.com/openfisca/openfisca-senegal/pull/37)

* Évolution du système socio-fiscal.
* Zones impactées : `impots_directs`.
  - Ajoute: Nombre de parts pour veuf avec enfant

## 0.7.5 [#33](https://github.com/openfisca/openfisca-senegal/pull/33)

* Évolution du système socio-fiscal.
* Zones impactées : `impots_directs`.
  - Transformation des valeurs du code en paramètres de la législation

### 0.7.4 [#XX](https://github.com/openfisca/openfisca-senegal/pull/XX)

* Correction d'un crash
  - Rajoute scipy dans les dépendances

### 0.7.3 [#XX](https://github.com/openfisca/openfisca-senegal/pull/XX)

* Correction d'un crash
  - Corrige version de survey-manager dans les dépendances

### 0.7.2 [#XX](https://github.com/openfisca/openfisca-senegal/pull/XX)

* Correction d'un crash
  - Répare survey scenario

### 0.7.1 [#XX](https://github.com/openfisca/openfisca-senegal/pull/XX)

* Amélioration technique
  - Adapte à la dernière version de core et survey-manager (0.17.2)

## 0.7 [#12](https://github.com/openfisca/openfisca-senegal/pull/12)

* Amélioration technique
  - Adaptation du `SenegalSurveyScenario` pour coller à l'évolution d'OpenFisca-Survey-Manager

## 0.6

* Amélioration technique
  - Reoganisation du modèles pour coller à l'arborescence adoptée pour Mali et Côte d'Ivoire

### 0.5.6

* Correction de bug
* Détails : met à jour la dépendance à openfisca core et aux tests.

### 0.5.5

* Use core version up to 21.2

### 0.5.3

* Parameters no longer missing in package (fix MANIFEST.in)

### 0.5.2

* Migrate survey_scenario to core v20

### 0.5.1

* Add some links to execute notebooks on [mybinder](https://mybinder.org/)

## 0.5.0

* Migrate to core v20

### 0.4.3

* Migrate to core v14.1.2

### 0.4.2

* Use a core version that works with the api

### 0.4.1

* Fix OpenFisca-Survey-Manager dependency

## 0.4.0

* Add `SurveyScenario` class
* Add OpenFisca-Survey-Manager optional dependancy

### 0.3.1

* Clarify setup.cfg

## 0.3.0

* Add parameters.xml in MANIFEST.in

## 0.0.0

* Unreleased
