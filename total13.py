import pdfplumber
import os

def extraire_total_13e_salaire(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        total_13e_salaire = None
        # Parcours de chaque page du PDF
        for page in pdf.pages:
            texte = page.extract_text()
            # Cherche la mention "13e salaire" dans le texte
            if "13ème salaire" in texte:
                # On peut ajuster ce code pour extraire précisément le montant
                # Par exemple, une recherche de toutes les occurrences numériques suivant "13e salaire"
                for ligne in texte.split('\n'):
                    if "13ème salaire" in ligne:
                        # Ici, on cherche à extraire le montant, supposons qu'il soit après un certain mot-clé
                        mots = ligne.split()
                        for mot in mots:
                            if mot.replace(',', '').isdigit():  # Si le mot est un nombre
                                total_13e_salaire = float(mot.replace(',', '.'))  # Remplace la virgule par un point si besoin
        return total_13e_salaire

dossier_pdf = "C:/Users/LocalAdmin/Documents/fichesSalaireFlexsis"
total_13e_salaire = 0

# Parcours tous les fichiers PDF dans le dossier
for fichier in os.listdir(dossier_pdf):
    if fichier.endswith(".pdf"):
        chemin_pdf = os.path.join(dossier_pdf, fichier)
        montant = extraire_total_13e_salaire(chemin_pdf)
        if montant:
            total_13e_salaire += montant

print(f"Le total des 13e salaires est : {total_13e_salaire} CHF")
