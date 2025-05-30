Template tirée de [Documenting architecture decisions - Michael Nygard](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions) venant de [Github](https://github.com/joelparkerhenderson/architecture-decision-record/tree/main/locales/en/templates/decision-record-template-by-michael-nygard)
# 01 - Architectural decision record

# Choix du mécanisme de base de données

## Status

Accepté

## Contexte

Le systême de point de vente doit persister beaucoup de données. Alors, de nombreux choix se présentent: des base de données noSQL comme MongoDB, ou des base de données relationnelles, comme PostgreSQL, SQLite ou Oracle. Ces bases de données doivent soit être en local ou serveur afin de rouler l'application.

## Décision

J'ai choisi d'utiliser PostgreSQL comme mécanisme de base de données pour persister les données.

## Justification

La raison pour laquelle j'ai choisi PostgreSQL est parce que SQLAlchemy, qui est le ORM choisi, est compatible avec cette base de données. De plus, PostgreSQL est une base de données qui supporte des transactions ACID, et est parfait pour représenter les relations entre les différentes entités du systême de point de vente en question, soit les utilisateurs, les produits et les ventes. Bien que PostgreSQL roule localement dans notre application sur un port distinct, il serait plus facile de le faire évoluer vers des architectures plus complexes, contrairement à SQLite, qui lui roule localement. 

## Conséquences

- Ajout de service dans le ```docker-compose.yml```; un conteneur supplémentaire Docker doit être crée pour faire fonctionner l'application. 
- Dépendance de plus à ajouter dans notre ```requirements.txt``` (psycopg2)
