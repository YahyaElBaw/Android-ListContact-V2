import os
import base64
from playwright.sync_api import sync_playwright

def get_b64(path):
    with open(path, "rb") as f:
        return f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"

def generate_pdf(html_content, output_path):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_content(html_content)
        page.pdf(
            path=output_path,
            format="A4",
            print_background=True,
            margin={"top": "15mm", "bottom": "15mm", "left": "15mm", "right": "15mm"}
        )
        browser.close()
    print(f"PDF generated: {output_path}")

BASE_CSS = """
    @page {
        size: A4;
        margin: 15mm;
        @bottom-right {
            content: counter(page);
        }
    }
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Helvetica, Arial, sans-serif; }
    body { color: #1E293B; line-height: 1.6; font-size: 13px; background: white; }
    h1 { color: #0F172A; font-size: 24px; margin-bottom: 8px; border-bottom: 2px solid #4A148C; padding-bottom: 6px; }
    h2 { color: #4A148C; font-size: 17px; margin-top: 18px; margin-bottom: 8px; border-bottom: 1px solid #E2E8F0; padding-bottom: 4px; }
    h3 { color: #334155; font-size: 14px; margin-top: 12px; margin-bottom: 4px; }
    p { margin-bottom: 8px; text-align: justify; }
    ul, ol { margin-left: 20px; margin-bottom: 10px; }
    li { margin-bottom: 4px; }
    .badge { display: inline-block; padding: 2px 8px; border-radius: 4px; font-weight: bold; font-size: 11px; }
    .badge-green { background: #DCFCE7; color: #166534; }
    .badge-blue { background: #DBEAFE; color: #1E40AF; }
    .badge-red { background: #FEE2E2; color: #991B1B; }
    table { width: 100%; border-collapse: collapse; margin: 12px 0; font-size: 12px; }
    th, td { border: 1px solid #CBD5E1; padding: 6px 10px; text-align: left; }
    th { background: #F1F5F9; color: #0F172A; font-weight: 600; }
    tr:nth-child(even) { background: #F8FAFC; }
    code { font-family: 'Consolas', monospace; background: #F1F5F9; color: #4A148C; padding: 2px 5px; border-radius: 4px; font-size: 12px; }
    pre { background: #0F172A; color: #F8FAFC; padding: 12px; border-radius: 6px; overflow-x: auto; font-size: 11px; line-height: 1.4; margin: 10px 0; font-family: 'Consolas', monospace; }
    .img-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin: 15px 0; }
    .img-card { background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 8px; text-align: center; }
    .img-card img { width: 100%; max-height: 260px; object-fit: contain; border-radius: 6px; }
    .img-caption { font-size: 11px; font-weight: 600; color: #475569; margin-top: 6px; }
    .header-box { background: linear-gradient(135deg, #311B92, #4A148C); color: white; padding: 20px; border-radius: 8px; margin-bottom: 20px; }
    .header-box h1 { color: white; border: none; font-size: 26px; }
    .header-meta { display: flex; gap: 20px; margin-top: 10px; font-size: 12px; opacity: 0.9; }
    .note-box { background: #F3E8FF; border-left: 4px solid #7E22CE; padding: 10px 14px; border-radius: 4px; margin: 10px 0; }
    .page-break { page-break-before: always; }
"""

def create_v2_compte_rendu():
    base_dir = r"D:/L3MDW/Mobile/ListContactV2/screenshots"
    img1 = get_b64(f"{base_dir}/v2_01_main_list.png")
    img2 = get_b64(f"{base_dir}/v2_02_detail_view.png")
    img3 = get_b64(f"{base_dir}/v2_03_modification.png")

    html = f"""
    <!DOCTYPE html>
    <html>
    <head><meta charset="utf-8"><style>{BASE_CSS}</style></head>
    <body>
        <div class="header-box">
            <h1>Compte Rendu de Réalisation — Contacts Version 2</h1>
            <p>Application Android Native en Kotlin : Architecture multi-activités et Intents explicites / implicites</p>
            <div class="header-meta">
                <span><strong>Projet :</strong> Contacts V2</span>
                <span><strong>Niveau :</strong> Étudiant L3 MDW</span>
                <span><strong>Technologies :</strong> 2 Activités, Intents Explicites &amp; Implicites, Caméra &amp; Galerie</span>
                <span><strong>Status :</strong> Validé (100%)</span>
            </div>
        </div>

        <h2>1. Présentation du Travail Réalisé</h2>
        <p>L'application <strong>Contacts V2</strong> fait évoluer la gestion de contacts vers une architecture complète à deux écrans :</p>
        <ul>
            <li><code>MainActivity</code> : Affiche la liste des contacts dans une <code>ListView</code> personnalisée avec avatar, nom, prénom et numéro de téléphone.</li>
            <li><code>DetailActivity</code> : Fiche détaillée ouverte par <strong>Intent explicite</strong> permettant de modifier les données du contact, de passer un appel téléphonique (<strong>Intent implicite ACTION_DIAL</strong>), d'envoyer un courriel (<strong>Intent implicite ACTION_SENDTO</strong>), ou de changer sa photo via la galerie ou la caméra du smartphone.</li>
            <li><strong>Retour de résultat d'activité :</strong> Utilisation du contrat moderne <code>ActivityResultContracts.StartActivityForResult()</code> pour renvoyer le contact modifié à <code>MainActivity</code> et rafraîchir l'affichage en temps réel.</li>
        </ul>

        <h2>2. Galerie des Captures d'Écran de l'Application</h2>
        <div class="img-grid">
            <div class="img-card">
                <img src="{img1}" alt="MainActivity" />
                <div class="img-caption">Vue 1 : MainActivity (Liste personnalisée avec avatars)</div>
            </div>
            <div class="img-card">
                <img src="{img2}" alt="DetailActivity" />
                <div class="img-caption">Vue 2 : DetailActivity (Consultation &amp; Actions)</div>
            </div>
            <div class="img-card">
                <img src="{img3}" alt="Modification" />
                <div class="img-caption">Vue 3 : Modification d'un contact et validation</div>
            </div>
        </div>

        <div class="page-break"></div>

        <h2>3. Validation des Scénarios de Test</h2>
        <table>
            <thead>
                <tr>
                    <th>Fonctionnalité testée</th>
                    <th>Comportement attendu</th>
                    <th>Résultat obtenu</th>
                    <th>Statut</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Clic sur « Dupont Claire »</td>
                    <td>Ouverture de DetailActivity avec données pré-remplies</td>
                    <td>Intent explicite déclenché avec extras</td>
                    <td><span class="badge badge-green">SUCCÈS</span></td>
                </tr>
                <tr>
                    <td>Bouton Appeler (icône téléphone)</td>
                    <td>Ouverture du composeur avec numéro pré-rempli</td>
                    <td>Intent(Intent.ACTION_DIAL, "tel:...")</td>
                    <td><span class="badge badge-green">SUCCÈS</span></td>
                </tr>
                <tr>
                    <td>Bouton E-mail (icône enveloppe)</td>
                    <td>Ouverture de l'application de messagerie</td>
                    <td>Intent(Intent.ACTION_SENDTO, "mailto:...")</td>
                    <td><span class="badge badge-green">SUCCÈS</span></td>
                </tr>
                <tr>
                    <td>Boutons Photos (Galerie / Caméra)</td>
                    <td>Lancement des sélecteurs système sans crash</td>
                    <td>ActivityResultContracts enregistrés</td>
                    <td><span class="badge badge-green">SUCCÈS</span></td>
                </tr>
                <tr>
                    <td>Bouton Enregistrer</td>
                    <td>Renvoi du Contact à MainActivity et actualisation de la liste</td>
                    <td>setResult(RESULT_OK) + notifyDataSetChanged()</td>
                    <td><span class="badge badge-green">SUCCÈS</span></td>
                </tr>
                <tr>
                    <td>Bouton Annuler</td>
                    <td>Retour à la liste sans modification des données</td>
                    <td>setResult(RESULT_CANCELED)</td>
                    <td><span class="badge badge-green">SUCCÈS</span></td>
                </tr>
            </tbody>
        </table>

        <h2>4. Points Pédagogiques Clés</h2>
        <div class="note-box">
            <ul>
                <li><strong>Différence Intent explicite vs implicite :</strong> L'Intent explicite nomme expressément la classe cible (<code>DetailActivity::class.java</code>), tandis que l'Intent implicite exprime une action générique (<code>ACTION_DIAL</code>) déléguée au système Android.</li>
                <li><strong>Remplacement de onActivityResult :</strong> L'ancienne méthode dépréciée a été avantageusement remplacée par <code>registerForActivityResult()</code>, garantissant la sûreté du typage et la robustesse du cycle de vie.</li>
            </ul>
        </div>
    </body>
    </html>
    """
    generate_pdf(html, r"D:\L3MDW\Mobile\ListContactV2\Compte_Rendu_ListContactV2.pdf")

def create_v2_guide_etudiant():
    base_dir = r"D:/L3MDW/Mobile/ListContactV2/screenshots"
    img1 = get_b64(f"{base_dir}/v2_02_detail_view.png")

    html = f"""
    <!DOCTYPE html>
    <html>
    <head><meta charset="utf-8"><style>{BASE_CSS}</style></head>
    <body>
        <div class="header-box">
            <h1>Guide Étudiant : Activités, Navigation et Intents sous Android</h1>
            <p>Comprendre la communication inter-activités, le passage de données et les fonctionnalités système</p>
            <div class="header-meta">
                <span><strong>Projet #5 :</strong> Contacts Version 2</span>
                <span><strong>Niveau :</strong> Étudiant / Intermédiaire</span>
                <span><strong>Notions :</strong> Intent explicite/implicite, Activity Result API</span>
            </div>
        </div>

        <h2>1. Présentation du TP</h2>
        <p>Dans cette Version 2 de notre gestionnaire de contacts, nous franchissons une étape majeure : concevoir une application Android multi-écrans. Vous allez apprendre comment faire communiquer deux activités entre elles, comment transmettre un objet complet, et comment interagir avec les applications système du smartphone (téléphone, messagerie, caméra et galerie photo).</p>

        <div style="display: flex; gap: 20px; align-items: center; margin: 15px 0;">
            <div style="flex: 1;">
                <p><strong>Les deux types d'Intents fondamentaux :</strong></p>
                <ul>
                    <li><strong>Intent Explicite :</strong> Utilisé pour naviguer à l'intérieur de notre propre application vers un écran précis. Exemple : Passer de <code>MainActivity</code> à <code>DetailActivity</code>.</li>
                    <li><strong>Intent Implicite :</strong> Utilisé pour demander à Android d'accomplir une tâche sans connaître l'application qui s'en chargera. Exemple : « Ouvre le composeur téléphonique avec ce numéro » ou « Envoie un e-mail à cette adresse ».</li>
                </ul>
            </div>
            <div style="width: 140px; text-align: center;">
                <img src="{img1}" style="width: 130px; border-radius: 8px; border: 1px solid #CBD5E1;" alt="Detail view" />
            </div>
        </div>

        <h2>2. Étapes de Réalisation Pas à Pas</h2>

        <h3>Étape 1 : Le Modèle Contact sérialisable (Contact.kt)</h3>
        <p>Pour pouvoir faire transiter un objet dans un <code>Intent</code> (via <code>putExtra</code>), notre classe doit implémenter <code>Serializable</code> ou <code>Parcelable</code> :</p>
        <pre>data class Contact(
    val id: Long = 0,
    var nom: String,
    var prenom: String,
    var telephone: String,
    var email: String,
    var photoUri: String? = null
) : Serializable</pre>

        <div class="page-break"></div>

        <h3>Étape 2 : L'Intent Explicite avec retour de résultat moderne</h3>
        <p>Dans <code>MainActivity.kt</code>, nous enregistrons un lanceur d'activité qui écoute le retour :</p>
        <pre>private val detailLauncher = registerForActivityResult(
    ActivityResultContracts.StartActivityForResult()
) {{ result ->
    if (result.resultCode == Activity.RESULT_OK) {{
        val contactModifie = result.data?.getSerializableExtra(DetailActivity.EXTRA_CONTACT) as? Contact
        val pos = result.data?.getIntExtra(DetailActivity.EXTRA_POSITION, -1) ?: -1
        if (contactModifie != null && pos != -1) {{
            contacts[pos] = contactModifie
            adapter.notifyDataSetChanged() // Mise à jour immédiate
        }}
    }}
}}</pre>

        <h3>Étape 3 : Les Intents Implicites (Appel et E-mail)</h3>
        <p>Dans <code>DetailActivity.kt</code>, nous déclenchons les actions du système :</p>
        <pre>// 1. Ouvrir le composeur téléphonique
val intentTel = Intent(Intent.ACTION_DIAL, Uri.parse("tel:$telephone"))
startActivity(intentTel)

// 2. Ouvrir le client de messagerie
val intentMail = Intent(Intent.ACTION_SENDTO, Uri.parse("mailto:$email"))
startActivity(intentMail)</pre>

        <h3>Étape 4 : Sélection photo et caméra</h3>
        <p>Android simplifie grandement la sélection avec les contrats d'activité :</p>
        <pre>// Pour la galerie
val pickImageLauncher = registerForActivityResult(ActivityResultContracts.GetContent()) {{ uri ->
    uri?.let {{ binding.ivDetailAvatar.setImageURI(it) }}
}}

// Pour l'appareil photo
val takePhotoLauncher = registerForActivityResult(ActivityResultContracts.TakePicturePreview()) {{ bitmap ->
    bitmap?.let {{ binding.ivDetailAvatar.setImageBitmap(it) }}
}}</pre>

        <h2>3. Conseils d'Expert pour les Étudiants</h2>
        <div class="note-box">
            <ul>
                <li><strong>ACTION_DIAL vs ACTION_CALL :</strong> Utilisez toujours <code>ACTION_DIAL</code> ! Il pré-remplit le numéro dans le composeur et ne nécessite <em>aucune permission sensible</em> dans le manifest. <code>ACTION_CALL</code> lance l'appel directement et exige une autorisation utilisateur complexe à gérer.</li>
                <li><strong>Déclaration dans AndroidManifest.xml :</strong> N'oubliez jamais de déclarer chaque nouvelle activité créée dans votre manifest, sinon l'application plantera avec un <code>ActivityNotFoundException</code>.</li>
            </ul>
        </div>
    </body>
    </html>
    """
    generate_pdf(html, r"D:\L3MDW\Mobile\pdfs\05_Guide_Etudiant_Contacts_V2_Activites_Intents.pdf")

if __name__ == "__main__":
    create_v2_compte_rendu()
    create_v2_guide_etudiant()
