# Seloger scraping

Un scraper du site seloger.com pour obtenir des informations sur les différents biens d'une ou
plusieurs villes.

## License

Ce projet est sous license MIT : voir le [fichier de license](./LICENSE).

## Installation

Il est conseillé de construire un environnement virtuel.

```bash
python3 -m venv venv
source venv/bin/activate
```

Et d'y installer les différents packages requis.

```bash
pip install -r requirements
```

## Utilisation

Le fichier principal se trouve dans [seloger_scraping/src/main.py](./seloger_scraping/src/main.py).

Il peut être appelé de la façon suivante :

```bash
python seloger_scraping/src/main.py
```

## Modifier le fichier principal

Pour le moment voici ce qu'il est possible de faire:
- selectionner la rubrique "louer" ("acheter" par défaut) : `select_louer()`
- décocher l'option "maison" (coché par défaut) : `uncheck_field_house()`
- décocher l'option "appart" (coché par défaut) : `uncheck_field_appart()`
- faire une recherche sur une ou plusieurs villes. `fill_field_city(city)` ou `fill_field_city_with_several_cities(cities)`
