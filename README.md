#  SenSante

##  Description
SenSante est un projet de Machine Learning visant à aider au pré-diagnostic médical au Sénégal.  
Il permet d’analyser les symptômes des patients afin de prédire certaines maladies comme :
- Paludisme
- Grippe
- Typhoïde

---

##  Objectif
Mettre en place un système intelligent capable d’assister les professionnels de santé dans le diagnostic.

---

##  Structure du projet

- `data/` : Contient les données des patients (CSV)
- `models/` : Contiendra le modèle Machine Learning
- `api/` : Code backend (API)
- `frontend/` : Interface utilisateur
- `notebooks/` : Scripts Python d’analyse

---

##  Technologies utilisées

- Python
- Pandas
- Matplotlib
- Git

---

##  Dataset

Le projet utilise un dataset de 500 patients provenant de la région de Dakar avec :
- âge
- sexe
- température
- symptômes
- diagnostic

---

##  Installation

```bash
git clone https://github.com/ton_nom/sensante.git
cd sensante
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt