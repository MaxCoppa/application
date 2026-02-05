# Probabilité de survie sur le Titanic

Pour pouvoir utiliser ce projet, il
est recommandé de créer un fichier `config.yaml`
ayant la structure suivante:

```yaml
jeton_api: ####
data_path: ####
```

# Quelques Commandes


Qualité du code

```bash
pip install pylint
pip install black
pip install ruff
```

Nettoyage code
```bash
pip install vulture
vulture .
```

Test Unitaire
```bash
coverage run -m unittest tests/test_pipeline.py
coverage report -m
```
