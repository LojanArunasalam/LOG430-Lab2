Template tirée de [Documenting architecture decisions - Michael Nygard](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions) venant de [Github](https://github.com/joelparkerhenderson/architecture-decision-record/tree/main/locales/en/templates/decision-record-template-by-michael-nygard) 
# 02 - Architectural decision record

# Séparation des responsabilités

## Status

Accepté

## Contexte

L'application cible est un système de caisse pour un petit magasin de quartier. Il faut donc concevoir une architecture simple afin de supporter les opérations nécessaires, comme l'enregistrement d'un produit ou gérer les retours. Dans le but de rendre le système modulaire, il est essentiel de découper l'application en modules afin de mieux séparer les responsabilités.

## Décision

Le systeme de point de vente doit respecter une architecture client/serveur (2-tier)

## Justification

Dans un systeme aussi simple, il y aura le client qui s'occupe du UI, et le serveur qui est la base de données, ce qui rend l'application plus modulaire et facilement maintenable. Également, cette architecture permet une evolution facile vers des architectures complexes, qui sera le cas dans les futurs laboratoires. 

## Conséquences
- Restreint à juste deux couches logiques, pas plus. 
- Évolution plus facile de l'application