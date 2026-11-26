# Inversion des revenus

## Inversion des salaires

### Rappel des concepts

On suppose que la variable que l'enquête ne fournit que le salaire net de cotisations sociales et de l'impôt sur le revenu supposé prélevé à la source sous la forme de la variable `salaire`.

La législation nous permet de calculer les cotisations sociales employeur et salarié à partir du `salaire_brut`.
On aura alors:
```
salaire_imposable =  salaire_brut - cotisations_salariales
```
où `salaire_imposable` est le salaire entrant dans la formule de l'impôt sur le revenu avant les abattements pour cotisations de retraite (13,2%) et pour frais professionnels (10%).
Le coût du travail vaudra lui:
```
cout_du_travail =  salaire_brut + cotisations_employeur
```
Enfin le lien avec la variable fournie par l'enquête est:
```
salaire =  salaire_imposable - impot_revenu =  salaire_brut - cotisations_salariales - impot_revenu
```

### Processus d'inversion

Le but est de retrouver le `salaire_brut` comme variable essentielle au niveau de la législation.
Comme  `impot_revenu` est une fonction de `salaire_imposable`, l'inversion de
```
salaire =  salaire_imposable - impot_revenu
```
nous permet de retrouver le `salaire_imposable` à partir du brut.
De même comme `cotisations_salariales` est une fonction de `salaire_brut`, l'inversion de
```
salaire_imposable =  salaire_brut - cotisations_salariales
```
nous permet de retrouver `salaire_brut`.
