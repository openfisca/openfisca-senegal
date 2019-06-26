# Changelog

## 0.9.0 [#XX](https://github.com/openfisca/openfisca-senegal/pull/XX)

* Amélioration technique
  - Permet de calculer le taux marginal d'imosition

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
