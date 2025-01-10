import os
from PyPDF2 import PdfMerger

def fusion_pdf(dossier_pdf, fichier_sortie):
    merger = PdfMerger()
    for fichier in os.listdir(dossier_pdf):
        if fichier.endswith(".pdf"):
            chemin_pdf = os.path.join(dossier_pdf, fichier)
            print(f"Ajout de {chemin_pdf} à la fusion...")
            merger.append(chemin_pdf)
    merger.write(fichier_sortie)
    merger.close()
    print(f"PDF fusionné enregistré sous {fichier_sortie}")
    
# Exemple d'utilisation
dossier_pdf = "C:/Users/LocalAdmin/Documents/fichesSalaireFlexsis/Novembre"
fichier_sortie = "C:/Users/LocalAdmin/Documents/fichesSalaireFlexsis/Fusion_Novembre.pdf"
    
fusion_pdf(dossier_pdf, fichier_sortie)