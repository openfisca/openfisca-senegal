# Contribuer à OpenFisca-Sénégal

Avant tout, merci de votre volonté de contribuer au bien commun qu'est OpenFisca !

Afin de faciliter la réutilisation d'OpenFisca et d'améliorer la qualité du code, les contributions à OpenFisca suivent certaines règles.

Certaines règles sont communes à tous les dépôts OpenFisca et sont détaillées dans [la documentation générale](http://openfisca.org/doc/contribute/guidelines.html).


## Format du Changelog

Les évolutions d'OpenFisca-Sénégal doivent pouvoir être comprises par des réutilisateurs qui n'interviennent pas nécessairement sur le code. Le Changelog, rédigé en français, se doit donc d'être le plus explicite possible.

Chaque évolution sera documentée par les élements suivants :

- Sur la première ligne figure en guise de titre le numéro de version, et un lien vers la Pull Request introduisant le changement. Le niveau de titre doit correspondre au niveau d'incrémentation de la version.

> Par exemple :
> # 13.0.0 - [#671](https://github.com/openfisca/openfisca-france/pull/671)
>
> ## 13.2.0 - [#676](https://github.com/openfisca/openfisca-france/pull/676)
>
> ### 13.1.5 - [#684](https://github.com/openfisca/openfisca-france/pull/684)

- La deuxième ligne indique de quel type de changement il s'agit. Les types possibles sont :
  - `Évolution du système socio-fiscal` : Amélioration, correction, mise à jour d'un calcul. Impacte les réutilisateurs intéressés par les calculs.
  - `Amélioration technique` : Amélioration des performances, évolution de la procédure d'installation, de la syntaxe des formules… Impacte les réutilisateurs rédigeant des règles et/ou déployant leur propre instance.
  - `Correction d'un crash` : Impacte tous les réutilisateurs.
  - `Changement mineur` : Refactoring, métadonnées… N'a aucun impact sur les réutilisateurs.

- **Dans le cas d'une `Évolution du système socio-fiscal`** , il est ensuite précisé :
  - Les périodes concernées par l'évolution. Les dates doivent être données au jour près pour lever toute ambiguïté : on écrira `au 01/01/2017` et non `pour 2017` (qui garde une ambiguïté sur l'inclusion de l'année en question).
  - Les zones du modèle de calcul impactées. Ces zones correspondent à l'arborescence des fichiers dans le modèle, sans l'extension `.py`.

> Par exemple :
> - Périodes concernées : Jusqu'au 31/12/2015.
> - Zones impactées : `prestations/minima_sociaux/cmu`

- Enfin, dans tous les cas hors `Changement mineur`, les corrections apportées doivent être explicitées de détails donnés d'un point de vue fonctionnel : dans quel cas d'usage constatait-on un erreur / un problème ? Quelle nouvelle fonctionalité est disponible ? Quel nouveau comportement est adopté ?

> Par exemple:
>
> * Détails :
>   - Ces variables renvoient désormais un montant annuel et non mensuel :
>     - `acs`
>     - `bourse_college`
>     - `bourse_lycee`
>   - _Les valeurs mensuelles précédentes étaient obtenues par une division par 12 et non par un calcul réel._
>
> Ou :
>
> * Détails :
>   - Déplacement du test runner depuis `openfisca-france` vers `core`.
>   - _Il devient possible d'exécuter `openfisca test` sur un fichier YAML. [Plus d'informations](https://openfisca.org/doc/openfisca-python-api/openfisca-run-test.html)._

Dans le cas où une Pull Request contient plusieurs évolutions distinctes, plusieurs paragraphes peuvent être ajoutés au Changelog.

## Utiliser une branche spécifique d'OpenFisca-Core pour faire passer les tests d'intégration continue

Certaines interventions sur OpenFica concernent à la fois [OpenFica-Core](https://github.com/openfisca/openfisca-core) et OpenFisca-Sénégal.

C'est par exemple le cas lorsqu'une version à paraître de Core contient un changement non-rétrocompatible, et que l'on souhaite s'assurer qu'il est possible d'adapter OpenFisca-Sénégal à cette nouvelle version.

Dans ce cas, il peut être pertinent de faire tourner les tests d'OpenFisca-Sénégal en se basant sur une version non-publiée de Core, disponible sur une branche spécifique. Pour ce faire, éditer le fichier de configuration `workflow.yml` comme suit :

```diff
(...)
-     - run: pip install .[dev]dependencies:
+     - run: pip install .[dev] --editable git+https://github.com/openfisca/openfisca-core.git@SPECIFIC_BRANCH_NAME#egg=OpenFisca-Core
(...)
```
En remplaçant `SPECIFIC_BRANCH_NAME` par le nom de votre branche Core.

Bien sûr, une fois la version spécifique de core publiée, **ce changement doit être reverté** avant le merge de la pull request sur OpenFisca-Sénégal.
