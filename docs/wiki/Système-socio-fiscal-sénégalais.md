# openfisca-senegal

## Système socio-fiscal sénégalais

Le Code Général des Impôts (CGI) qui est en vigueur est celui du 31 décembre 2012 adopté suite à la réforme fiscale de 2013. Cependant, les données de l'ESPS-2011 que nous mobilisons pour évaluer la politique fiscale sont collectées en 2011 c'est-à-dire au moment où c'est le CGI de 2007 qui était en vigueur. Il est important de décrire aussi ce dernier code pour pouvoir reconstituer le revenu avant imposition pour pouvoir simuler le CGI de 2013 qui est en vigueur. C'est pour ça que dans la suite, nous adoptons une démarche qui présente la réforme fiscale afin d'avoir des éléments des deux codes fiscales. L'ensemble des recettes fiscales collectées par le gouvernement est disponible sous sous forme d'un fichier [Excel](https://github.com/openfisca/openfisca-senegal/blob/master/openfisca_senegal/assets/General%20government%20budget_Mouk.xlsx) ou [csv](https://github.com/openfisca/openfisca-senegal/blob/master/openfisca_senegal/assets/General%20government%20budget_Mouk.csv).

Voir aussi http://www.impotsetdomaines.gouv.sn/fr/fiscalite

## Présentation synthétique de la réforme fiscale

### Taxes directes

Les taxes directes comprennent l’impôt prélevé sur les sociétés et l’impôt sur les revenus des personnes physiques. Ces deux types d’impôt sont présentés par la suite :

#### Impôt sur les sociétés

L’impôt sur les sociétés s’applique sur les bénéfices (article 4, CGI 2012):
1.  des sociétés anonymes
2.  des sociétés à responsabilité limitée à l’exception des sociétés unipersonnelles à responsabilité limitée où l’associé unique est une personne physique (article 4, CGI 2012)
3. des sociétés civiles ou les établissements publics qui se livrent à une activité de caractère industriel ou commercial (article 4, CGI 2012) sont également soumises à cet impôt.

En revanche, les sociétés qui poursuivent un objectif social sont exemptées de l’impôt sur les sociétés (voir article 5 du CGI 2012).

Les changements intervenus dans le CGI 2012 par rapport à celui de 2007 concernent le taux de l'impôt sur les sociétés et le calcul de l'impôt minimum forfaitaire.

1. Le taux d’imposition qui était de 25 % dans l’ancien code (article 19, CGI 2007) est passé à 30 % dans le nouveau code général des impôts (article 36, CGI 2012).

2. Lorsque les sociétés et les personnes morales passibles de l’impôt sur le revenu sont déficitaires ou si leurs résultats ne permettent pas de générer un impôt sur les sociétés supérieur à 500 000 francs CFA, un impôt minimum forfaitaire (IMF) sur le chiffre d’affaires hors taxe est appliqué.

Il représente 0,5% du chiffre d'affaire hors taxe et ne peut en aucun  cas, être ni inférieur  à 500 000 francs CFA ni supérieur à 5 000 000  francs CFA (articles 38, 39 CGI 2012).

Dans l'ancien code (article 24, CGI 2007), l'IMF est un montant  forfaitaire qui varie en fonction du chiffre (tableau 3.1 ).

Tableau 3.1 : Impôt minimum forfaitaire

|Chiffre d'affaires hors taxe (Francs CFA) |Tarif (Francs CFA)|
|-------------------------------------------|-----------------|
|Jusqu'à 250 000 000 | 500 000 |
|De 250 000 001 à 500 000 000 | 750 000 |
| Au-delà de 500 000 000 | 1 000 000 |


#### Impôt sur le revenu des personnes physiques (IRPP)

L’impôt sur les revenus des personnes physiques est calculé sur la base du revenu imposable global du contribuable constitué par les revenus fonciers, les bénéfices industriels et commerciaux, les bénéfices non commerciaux et revenus assimilés, les bénéfices de l’exploitation agricole, les revenus des capitaux mobiliers ainsi que les salaires et retraites.

**Trois modifications majeures ont été introduites à la suite de la réforme.**

La **première modification** est relative au calcul de l’impôt sur les salaires et les retraites.

Dans le CGI de 2007, l’IRPP sur les salaires représente la somme d’un droit proportionnel et d’un droit progressif (article 104, CGI 2007).

Le droit proportionnel est différent selon le type de revenu. Il est fixé à:
* 0% pour les salaires inférieurs à 700 000 FCFA
* 11% pour les salaires supérieurs qui dépassent 700 000 FCFA.
* 20% pour les revenus fonciers.

En ce qui concerne les revenus des capitaux, il est prélevé un taux de:
* 10% pour les produits des actions, parts sociales et parts d’intérêts des sociétés civiles,
* 13% pour les obligations, 15% pour les lots,
* 16% pour les autres revenus notamment les jetons de présence et autres rémunérations d’administrateurs ainsi que les revenus des créances, dépôts et cautionnements
* 8% pour les intérêts, arrérages et autres produits des comptes de dépôts et des comptes courants ouverts dans une banque, un agent de change, un courtier valeurs mobilières et des comptables du trésor.

Dans le CGI de 2012, le droit proportionnel est supprimé.

L’IRPP sur les salaires suivant le CGI 2012  est uniquement calculé sur la base d’un droit progressif. Le barème de ce droit est différent de celui du CGI 2007.

* Dans l’ancien code (CGI 2007), le barème du droit progressif est appliqué au salaire imposable divisé par un certain nombre de parts en fonction de la situation familiale (article 105, CGI 2007).

* Dans le CGI de 2012 (article 173, CGI 2012) par contre, le barème est appliqué directement au salaire imposable avec notamment moins de tranches (tableau 3.2).

Tableau 3.2 : Droit progressif

| Tranche de revenu par parts avant la réforme (FCFA) | Taux (%) | Tranche de revenu après la réforme (FCFA) | Taux (%) |
|------------------|--|------------------|--|
| 0 à 600 000 | 0 | 0 à 630 000 | 0 |
| 600 001 à 890 000 | 18 | 630 001 à 1 500 000 | 20 |
| 890 001 à 1 010 000 | 22 | 1 500 001 à 4 000 000| 30 |
| 1 010 001 à 1 410 000 | 25 | 4 000 001 à 8 000 000 | 35 |
| 1 410 001 à 2 475 000| 28 | 8 000 001 à 13 500 000 |37 |
| 2 475 001 à 3 540 000 | 30 | Plus de 13 500 001 | 40 |
| 3 540 001 à 7 650 000 | 35 | | |
|7 650 001 à 9 650 000 | 40 | | |
| 9 650 001 à 12 650 000 | 45 | | |
| Plus de 12 650 001 | 50 | | |
|NB: le montant de l’impôt ne peut excéder 50% du revenu imposable en aucun cas.| |NB : le montant de l’impôt ne peut excéder 40% du revenu imposable en aucun cas.|
Source : DGID/MEF

Enfin, les charges de famille sont prises en compte différemment dans le calcul de l’IRPP sur les salaires dans le nouveau code.

* Avant la réforme (art 105, CGI 2007), la prise en compte des charges de famille consiste à diviser le salaire imposable par le nombre de parts compte tenu de la situation de famille.

* Alors qu’après la réforme (art 174, CGI 2012), un taux de réduction sur le montant d’impôt (avec des bornes min et max) est appliqué en fonction du nombre de parts. Le nombre de parts ne peut excéder 5.

Le tableau 3.4 présente les taux de réduction d’impôt introduits à la suite de la réforme.

Tableau 3.3: Taux de réduction d’impôt pour charges de famille

| | Nombre de parts | Taux de réduction (%) | Montant minimum de réduction | Montant maximum de réduction |
|--|---|--|--|---|
|Célibataire, divorcé ou veuf sans enfant en charge | 1 | 0 | 0 | 0 |
|Marié sans enfant en charge | 1,5 | 10 | 100 000 | 300 000 |
|Célibataire ou divorcé ayant 1 enfant en charge | 1,5 | 10 | 100 000 |300 000|
|Marié ou veuf ayant 1 enfant en charge | 2 | 15 | 200 000 | 650 000|
|Célibataire ou divorcé ayant 2 enfants en charge| 2 | 15 | 200 000 | 650 000 |
| Marié ou veuf ayant 2 enfants en charge | 2,5 | 20 | 300 000 | 1 100 000 |
|Célibataire ou divorcé ayant 3 enfants à charge | 2,5 | 20 | 300 000 | 1 100 000 |
|Marié ou veuf ayant 3 enfants en charge | 3 | 25 | 400 000 | 1 650 000 |
|Célibataire ou divorcé ayant 4 enfants en charge | 3 | 25 | 400 000 | 1 650 000 |
| Marié ou veuf ayant 4 enfants en charge | 3,5 | 30 | 500 000 | 2 030 000 |
|Célibataire ou divorcé ayant 5 enfants en charge | 3,5 |30 | 500 000 | 2 030 000 |
|Marié ou veuf ayant 5 enfants en charge | 4 | 35 | 600 000 | 2 490 000 |
| Célibataire ou divorcé ayant 6 enfants en charge | 4 | 35 | 600 000 | 2 490 000 |
| Marié ou veuf ayant 6 enfants en charge | 4,5 | 40 | 700 000 | 2 755 000 |
|Célibataire ou divorcé ayant 7 enfants en charge | 4,5 | 40 | 700 000 | 2 755 000|
|Marié ou veuf ayant 7 enfants en charge | 5 |45 |800 000 |3 180 000|
|Célibataire ou divorcé ayant 8 enfants en charge |5 | 45 | 800 000 | 3 180 000 |
|NB :Avant la réforme, le salaire imposable est obtenu après déduction : abattement proportionnel de 13,2% (pour cotisations obligatoires voir article 99 b. CGI 2007) et abattement forfaitaire de 700 000 FCFA pour le droit proportionnel (voir art 111, CGI 2007). Pour les pensions de retraite l'abattement est égal à 1/3 de la pension sans être inférieur à 1 800 000 (voir art 96 CGI 2007)|  | NB : Après la réforme, le salaire imposable est obtenu après déduction : abattement proportionnel de 30% avec un plafond de 900 000 fcfa  (pour cotisations obligatoires voir article 168 b. CGI 2012). En ce qui concerne les retraites, l'abattement est de 40% sans être inférieur à 1 800 000 FCFA (voir art 164 CGI 2012).

La **deuxième modification** concerne la contribution globale unique (CGU) qui est un impôt prévu pour les catégories de contribuables dont le niveau d’activité est modeste.

* Cette taxe est un impôt synthétique représentatif de toutes les obligations fiscales (impôt sur le revenu, impôt du minimum fiscal, contribution des patentes, taxe sur la valeur ajoutée, etc.).

* Les contribuables éligibles au régime de la CGU sont les personnes physiques dont le chiffre d’affaire annuel n’excède pas 50 millions FCFA ou 25 millions FCFA selon la nature de leur activité (tableau 3.4 à 3.6).

* Avant la réforme, la CGU représentait une taxe forfaitaire variant selon la tranche de chiffre d’affaire (art 74a, 77 bis, 77 ter, CGI 2007). La réforme a non seulement simplifié le prélèvement de la CGU en diminuant le nombre de tranches mais également le prélèvement est effectué en proportion du chiffre d’affaire (art. 134, 141, CGI 2012).

Tableau 3.4 : Contribution globale unique (CGU) des prestataires de service

| Avant la reforme 	|  	| Après la reforme 	|  	|
|---------------------------	|---------------------------	|---------------------------	|-----------------------	|
| Chiffre d'affaires (FCFA) 	| Montant de l'impôt (FCFA) 	| Chiffre d'affaires (FCFA) 	| Taux d'imposition (%) 	|
| 0 à 330 000 	| 10 000 	| 0 à 500 000 	| 4 	|
| 330 001 à 500 000 	| 20 000 	| 500 001 à 3 000 000 	| 5 	|
| 500 001 à 1 000 000 	| 40 000 	| 3 000 001 à 10 000 000 	| 6 	|
| 1 000 001 à 2 000 000 	| 80 000 	| 10 000 001 à 37 000 000 	| 7 	|
| 2 000 001 à 3 000 000 	| 150 000 	| 37 000 001 à 50 000 000 	| 8 	|
| 3 000 001 à 5 000 000 	| 300 000 	|  	|  	|
| 5 000 001 à 7 500 000 	| 500 000 	|  	|  	|
| 7 500 001 à 10 000 000 	| 800 000 	|  	|  	|
| 10 000 001 à 15 000 000 	| 1 200 000 	|  	|  	|
| 15 000 001 à 20 000 000 	| 1 400 000 	|  	|  	|
| 20 000 001 à 25 000 000 	| 2 000 000 	|  	|  	|


Pour les commerçants et producteurs :

Tableau 3.5 : Contribution globale unique (CGU) des revendeurs de ciment et de denrées alimentaires


| Avant la reforme 	|  	| Après la reforme 	|  	|
|---------------------------	|---------------------------	|---------------------------	|-----------------------	|
| Chiffre d'affaires (FCFA) 	| Montant de l'impôt (FCFA) 	| Chiffre d'affaires (FCFA) 	| Taux d'imposition (%) 	|
| 0 à 330 000 	| 5 000 	| 0 à 10 000 000 	| 1 	|
| 330 001 à 500 000 	| 12 500 	| 10 000 001 à 37 000 000 	| 2 	|
| 500 001 à 1 000 000 	| 25 250 	| 37 000 001 à 50 000 000 	| 2,8 	|
| 1 000 001 à 2 000 000 	| 50 000 	|  	|  	|
| 2 000 001 à 3 000 000 	| 75 000 	|  	|  	|
| 3 000 001 à 4 000 000 	| 100 000 	|  	|  	|
| 4 000 001 à 5 000 000 	| 125 000 	|  	|  	|
| 5 000 001 à 7 500 000 	| 187 500 	|  	|  	|
| 7 500 001 à 10 000 000 	| 250 000 	|  	|  	|
| 10 000 001 à 15 000 000 	| 375 000 	|  	|  	|
| 15 000 001 à 20 000 000 	| 500 000 	|  	|  	|
| 20 000 001 à 25 000 000 	| 625 000 	|  	|  	|
| 25 000 001 à 28 000 000 	| 700 000 	|  	|  	|
| 28 000 001 à 31 000 000 	| 775 000 	|  	|  	|
| 31 000 001 à 34 000 000 	| 850 000 	|  	|  	|
| 34 000 001 à 37 000 000 	| 925 000 	|  	|  	|
| 37 000 001 à 41 000 000 	| 1 025 000 	|  	|  	|
| 41 000 001 à 44 000 000 	| 1 100 000 	|  	|  	|
| 44 000 001 à 47 000 000 	| 1 175 000 	|  	|  	|
| 47 000 001 à 50 000 000 	| 1 250 000 	|  	|  	|


Tableau 3.6 : Contribution globale unique (CGU) des autres catégories de producteurs et revendeurs


| Avant la réforme 	|  	| Après la réforme 	|  	|
|---------------------------	|---------------------------	|---------------------------	|-----------------------	|
| Chiffre d'affaires (FCFA) 	| Montant de l'impôt (FCFA) 	| Chiffre d'affaires (FCFA) 	| Taux d'imposition (%) 	|
| 0 à 330 000 	| 5 000 	| 0 à 10 000 000 	| 2 	|
| 330 001 à 500 000 	| 15 000 	| 10 000 001 à 37 000 000 	| 3 	|
| 500 001 à 1 000 000 	| 30 000 	| 37 000 001 à 50 000 000 	| 3,8 	|
| 1 000 001 à 2 000 000 	| 60 000 	|  	|  	|
| 2 000 001 à 3 000 000 	| 90 000 	|  	|  	|
| 3 000 001 à 4 000 000 	| 120 000 	|  	|  	|
| 4 000 001 à 5 000 000 	| 150 000 	|  	|  	|
| 5 000 001 à 7 500 000 	| 225 000 	|  	|  	|
| 7 500 001 à 10 000 000 	| 300 000 	|  	|  	|
| 10 000 001 à 15 000 000 	| 450 000 	|  	|  	|
| 15 000 001 à 20 000 000 	| 600 000 	|  	|  	|
| 20 000 001 à 25 000 000 	| 750 000 	|  	|  	|
| 25 000 001 à 28 000 000 	| 840 000 	|  	|  	|
| 28 000 001 à 31 000 000 	| 930 000 	|  	|  	|
| 31 000 001 à 34 000 000 	| 1 020 000 	|  	|  	|
| 34 000 001 à 37 000 000 	| 1 110 000 	|  	|  	|
| 37 000 001 à 41 000 000 	| 1 230 000 	|  	|  	|
| 41 000 001 à 44 000 000 	| 1 320 000 	|  	|  	|
| 44 000 001 à 47 000 000 	| 1 410 000 	|  	|  	|
| 47 000 001 à 50 000 000 	| 1 500 000 	|  	|  	|

La **troisième modification** est l’introduction de la contribution globale foncière (CGF) alors qu’elle n’existait pas dans l’ancien code qui prévoyait un impôt proportionnel de 20% sur les revenus fonciers. La CGF permet aux titulaires de revenus fonciers modestes de s’acquitter de leurs obligations fiscales. Elle concerne les personnes physiques dont les revenus fonciers n’excèdent pas 3 millions de FCFA. Le tarif de la contribution globale foncière est le suivant:

* 8% pour la catégorie de 1 à 1 800 000 FCFA

* 10% pour la catégorie de 1 800 001 à 2 100 000FCFA

* 12% pour la catégorie de 2 100 001 à 2 400 000 FCFA

* 14% pour la catégorie de 2 400 001 à 3 000 000 FCFA

En aucun cas, le montant de la contribution globale foncière ne peut être inférieur à 50 000 FCFA.

### Retenu à la source

Par ailleurs tout exploitant individuel non soumis au régime réel paie une retenue à la source (voir art 200 CGI 2012). Le taux est fixé à 5% du montant brut hors taxe des sommes versées ou produits reçus. Ce taux n'a pas changé suite à la reforme.

### Taxes indirectes avant et après la réforme de 2012

Le tableau 3.8 montre les modifications de la fiscalité indirecte.

* Les changements ont essentiellement porté sur les droits d’accise et les droits de douane.

* Les modifications des taux des droits d’accise vont dans le sens d’une hausse puisque le taux des taxes spécifiques sur le tabac passe de 20% à 40% et la taxe d’accise sur les boissons alcoolisées passe de 30% à 40%.

* En revanche, les taux pour les droits de douanes augmentent pur certains produits alors que pour d’autres les taux baissent. Les produits concernés par la baisse des droits de douane sont par exemple les huiles raffinés, les ovins et bovins sur pied. Les droits de douanes sur le riz importé, le poisson frais ainsi que la pâtisserie de conservation  ont quant à eux augmenté.

* L’ensemble des taxes sur les produits sont présentés de manière détaillée dans [un fichier csv](https://github.com/openfisca/openfisca-senegal/blob/788c4da99e89cdf1e24fba09b312ce03549ec3f2/taux_taxe_indirect.csv).

Tableau 3.8 : Synthèse des modifications des taxes indirectes


| Taxe sur la Valeur Ajoutée (TVA) 	| Avant 	| Après 	|
|---------------------------------------------------------------------------------------	|-------	|-------	|
| **Inchangé**	| 18% 	| 18% 	|


| Droits d’Accise 	| Avant 	| Après 	|
|---------------------------------------------------------------------------------------	|-------	|-------	|
| **En hausse** 	|  	|  	|
| Café et thé 	| 3,80% 	| 5% 	|
| Bière, autres boissons alcoolisées et malt 	| 30% 	| 40% 	|
| Tabac-cigarettes 	| 20% 	| 40% 	|



| Droits de Douanes 	| Avant 	| Après 	|
|---------------------------------------------------------------------------------------	|-------	|-------	|
| **En baisse** 	|  	|  	|
| Huile raffinée végétale (arachide, coton, colza) 	| 22% 	| 7% 	|
| Ovins sur pied 	| 22% 	| 12% 	|
| Bovins sur pied 	|  22% 	|  12%	|
| Café et thé transformé 	| 22% 	| 12% 	|
| Plantes et fleurs 	|  22% 	|  12%	|
| Produits édités et imprimés 	| 12% 	| 7% 	|
| Pétrole lampant 	| 12% 	| 7% 	|
| **En hausse** 	|  	|  	|
| Riz importé 	|  7% 	|  12%	|
| Arachides coques 	|  7% 	|  12%	|
| Autres farines, céréales transformées, sons, résidus de meunerie et produits amylacés 	| 7% 	| 12% 	|
| Grosses réparations 	|  7% 	|  12%	|
| Poisson frais 	| 12% 	| 22% 	|
| Pâtisserie de conservation, biscuits 	| 22% 	| 37% 	|
