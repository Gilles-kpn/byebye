"""Génère les pages légales de Zemi Dede (même gabarit que Cadence). Lancer : python3 zemi-dede/gen.py"""
from pathlib import Path

DIR = Path(__file__).parent
MAIL = "okpanou2@gmail.com"
DATE = "20 novembre 2026"
NAV = [("politique-confidentialite.html", "Confidentialité"), ("conditions-utilisation.html", "Conditions d'utilisation"),
       ("suppression-donnees.html", "Suppression des données")]


def head(title, desc):
    return f"""<!doctype html>
<html lang="fr">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>{title}</title>
        <meta name="description" content="{desc}" />
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:wght@500;600&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
        <link rel="stylesheet" href="./styles/zemi-dede.css" />
        <link rel="apple-touch-icon" sizes="180x180" href="./assets/icon-180.png" />
        <link rel="icon" type="image/png" sizes="32x32" href="./assets/icon-32.png" />
        <link rel="icon" type="image/png" sizes="16x16" href="./assets/icon-16.png" />
    </head>
    <body>
"""


def topbar(active=""):
    links = "".join(f'<a href="{h}"{" class=\"active\"" if h == active else ""}>{t}</a>' for h, t in NAV)
    return f"""        <header class="topbar">
            <div class="topbar-inner">
                <a href="./index.html" class="brand">
                    <span class="brand-mark"><img src="./assets/logo.png" alt="" width="32" height="32" /></span>
                    Zemi Dede
                </a>
                <nav class="doc-nav" aria-label="Documents">{links}</nav>
            </div>
        </header>
"""


def footer():
    links = "".join(f'\n                    <a href="{h}">{t}</a>' for h, t in NAV)
    return f"""
        <footer class="doc-footer">
            <div class="doc-footer-inner">
                <p>© 2026 Zemi Dede. Tous droits réservés.</p>
                <nav class="doc-footer-links" aria-label="Liens">{links}
                    <a href="mailto:{MAIL}">Contact</a>
                </nav>
            </div>
        </footer>
    </body>
</html>
"""


def doc(file, title, h1, desc, intro, sections):
    toc = "".join(f'<li><a href="#{sid}">{st}</a></li>' for sid, st, _ in sections)
    body = ""
    for i, (sid, st, html) in enumerate(sections, 1):
        body += f"""                <section id="{sid}">
                    <span class="section-num">{i:02d}</span>
                    <h2>{st}</h2>
{html}
                </section>

"""
    page = head(title, desc) + topbar(file) + f"""
        <div class="doc-hero">
            <span class="doc-eyebrow">Document légal</span>
            <h1 class="doc-title">{h1}</h1>
            <div class="doc-meta">
                <span><strong>Dernière mise à jour :</strong> {DATE}</span>
                <span><strong>Version :</strong> 1.0</span>
                <span><strong>Applicable à :</strong> Zemi Dede (Android)</span>
            </div>
            <p class="doc-intro">{intro}</p>
        </div>

        <div class="doc-body">
            <nav class="toc" aria-label="Table des matières">
                <div class="toc-label">Sommaire</div>
                <ol>{toc}</ol>
            </nav>
            <article class="doc-content">
{body}            </article>
        </div>
""" + footer()
    (DIR / file).write_text(page, encoding="utf-8")


def p(t):
    return f"                    <p>{t}</p>\n"


def ul(items):
    return "                    <ul>\n" + "".join(f"                        <li>{i}</li>\n" for i in items) + "                    </ul>\n"


def table(head_, rows):
    th = "".join(f"<th>{h}</th>" for h in head_)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'                    <table class="doc-table"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>\n'


def callout(kind, icon, t):
    return f'                    <div class="callout callout-{kind}"><span class="callout-icon">{icon}</span><p>{t}</p></div>\n'


M = f'<a href="mailto:{MAIL}">{MAIL}</a>'

# ── Politique de confidentialité ────────────────────────────────────────────
doc("politique-confidentialite.html", "Politique de confidentialité — Zemi Dede", "Politique de confidentialité",
    "Politique de confidentialité du jeu Zemi Dede : données collectées, services tiers, vos droits.",
    f"Zemi Dede est un jeu de zémidjan à Cotonou. Cette politique explique quelles données le jeu utilise, pourquoi, et comment les refuser. Une question : {M}.",
    [
        ("collecte", "Données collectées",
         p("Zemi Dede se joue sans compte : pas d'inscription, pas d'e-mail, pas de mot de passe.")
         + "                    <h3>Sur votre téléphone uniquement</h3>\n"
         + ul(["Votre progression (missions, argent du jeu, moto, réglages)",
               "Le pseudo que vous choisissez pour le jeu en réseau local"])
         + "                    <h3>Statistiques et rapports de plantage (facultatifs)</h3>\n"
         + table(["Donnée", "Finalité"], [
             ["Événements de jeu anonymes (partie lancée, mission terminée, qualité graphique choisie, images par seconde)", "Comprendre ce qui plaît et ce qui rame, pour améliorer le jeu"],
             ["Rapport de plantage : appareil, version d'Android, version du jeu, trace de l'erreur", "Corriger les bugs"],
             ["Identifiant d'installation aléatoire généré par Firebase", "Compter les joueurs sans savoir qui ils sont"]])
         + callout("info", "ℹ️", "Zemi Dede ne collecte ni votre nom, ni votre position réelle, ni vos contacts, ni vos photos, ni le micro. Il n'affiche aucune publicité et n'utilise pas l'identifiant publicitaire. Sans les services Google (téléphones Huawei, par exemple), le jeu fonctionne normalement et n'envoie rien.")),
        ("finalites", "Finalités du traitement",
         p("Les statistiques servent uniquement à améliorer le jeu : trouver les bugs, mesurer la fluidité sur les différents téléphones et savoir quelles missions sont trop dures. Elles ne servent jamais à la publicité ni au profilage.")),
        ("base-legale", "Base légale",
         ul(["<strong>Votre consentement</strong> pour les statistiques : vous pouvez les couper à tout moment dans <em>Réglages › Statistiques anonymes</em>",
             "<strong>Notre intérêt légitime</strong> à corriger les plantages et à sécuriser le jeu",
             "<strong>L'exécution du contrat</strong> pour les achats intégrés, s'il y en a un jour"])),
        ("partage", "Partage avec des tiers",
         p("Zemi Dede ne vend, ne loue et ne partage jamais vos données à des fins commerciales ou publicitaires.")
         + table(["Service", "Ce qui lui est envoyé", "Quand"], [
             ["Google Firebase Analytics et Crashlytics (Google LLC)", "Événements de jeu anonymes et rapports de plantage", "Si les statistiques sont activées et que les services Google sont présents"],
             ["Google Play (Google LLC)", "Ce qu'il faut pour vérifier et livrer un achat ou une mise à jour", "Lors d'un achat intégré ou d'une mise à jour proposée par le Play Store"],
             ["Autres joueurs du même Wi-Fi", "Votre pseudo, la couleur de votre moto et votre position dans le jeu", "Seulement pendant une partie en réseau local que vous avez lancée ou rejointe"]])
         + p("Le jeu en réseau local passe directement d'un téléphone à l'autre sur votre Wi-Fi : aucun serveur à nous ne reçoit ces échanges.")
         + callout("warning", "⚠️", "Nous pouvons divulguer des données si la loi l'exige, notamment en réponse à une demande judiciaire valide.")),
        ("paiements", "Achats intégrés",
         p("Le jeu est gratuit. Si des achats intégrés sont proposés plus tard, le paiement est entièrement géré par Google Play : nous ne recevons jamais votre numéro de carte ni vos coordonnées bancaires, seulement la confirmation de l'achat.")),
        ("stockage", "Stockage et sécurité",
         p("Votre progression est stockée dans l'espace privé du jeu sur votre téléphone, inaccessible aux autres applications. Les statistiques sont envoyées chiffrées (HTTPS/TLS) et hébergées par Google Firebase.")
         + p("Aucun système n'est infaillible. En cas d'incident affectant des données personnelles, nous vous en informerons dans les meilleurs délais, conformément aux obligations légales.")),
        ("conservation", "Durée de conservation",
         p("Les statistiques Firebase sont conservées au plus 14 mois, puis effacées automatiquement. Les rapports de plantage sont conservés 90 jours. Votre progression reste sur votre téléphone jusqu'à ce que vous désinstalliez le jeu.")
         + p('Voir <a href="suppression-donnees.html">comment supprimer vos données</a>.')),
        ("droits", "Vos droits",
         p("Conformément aux réglementations applicables (RGPD pour les résidents européens et lois équivalentes), vous disposez des droits d'accès, de rectification, d'effacement, d'opposition et de retrait du consentement.")
         + p(f"Pour les exercer, écrivez à {M}. Nous répondons dans un délai maximal de 30 jours.")),
        ("mineurs", "Protection des mineurs",
         p(f"Zemi Dede n'est pas destiné aux enfants de moins de 13 ans et nous ne collectons pas sciemment leurs données. Si vous pensez qu'un enfant nous a transmis des données, écrivez à {M} pour que nous les supprimions.")),
        ("transferts", "Transferts internationaux",
         p("Google peut traiter les statistiques sur des serveurs situés hors de votre pays, notamment aux États-Unis, dans le cadre de mécanismes reconnus (clauses contractuelles types).")),
        ("modifications", "Modifications de cette politique",
         p("Nous pouvons mettre à jour cette politique. La date de dernière mise à jour figure en haut de ce document ; toute modification importante sera signalée dans le jeu.")),
        ("contact", "Nous contacter",
         p(f"Pour toute question : {M}.")
         + p("Si vous estimez que vos droits n'ont pas été respectés, vous pouvez saisir l'autorité de protection des données de votre pays (au Bénin, l'APDP ; en France, la CNIL).")),
    ])

# ── Conditions d'utilisation ────────────────────────────────────────────────
doc("conditions-utilisation.html", "Conditions d'utilisation — Zemi Dede", "Conditions d'utilisation",
    "Conditions générales d'utilisation du jeu Zemi Dede.",
    "En installant ou en jouant à Zemi Dede, vous acceptez ces conditions. Merci de les lire.",
    [
        ("objet", "Objet",
         p("Zemi Dede est un jeu vidéo en monde ouvert où l'on incarne un conducteur de zémidjan (moto-taxi) à Cotonou. Ces conditions encadrent son utilisation sur Android.")),
        ("licence", "Licence d'utilisation",
         p("Nous vous accordons une licence personnelle, non exclusive, non transférable et révocable pour installer et jouer à Zemi Dede à des fins privées et non commerciales.")
         + p("Vous pouvez filmer vos parties et les publier (YouTube, TikTok…), y compris monétisées, tant que vous ne présentez pas le jeu comme le vôtre.")),
        ("fiction", "Une œuvre de fiction",
         p("Le jeu s'inspire de vraies rues de Cotonou, mais ses personnages, ses histoires et ses situations sont fictifs. Toute ressemblance avec des personnes réelles est fortuite. Les comportements montrés dans le jeu (conduite dangereuse, fuite devant la police, etc.) ne doivent jamais être reproduits dans la réalité.")
         + callout("warning", "⚠️", "Sur une vraie moto : casque, prudence et respect du code de la route. Zemi Dede veut dire « conduis-moi doucement ».")),
        ("conduite", "Règles de conduite en réseau local",
         ul(["Ne choisissez pas de pseudo injurieux, haineux ou usurpant l'identité de quelqu'un",
             "N'utilisez pas de logiciel de triche qui gâche la partie des autres joueurs",
             "Ne tentez pas de perturber, pirater ou désassembler le jeu pour nuire à autrui"])),
        ("achats", "Achats intégrés",
         p("Le jeu est gratuit. Si des achats intégrés (objets ou monnaie virtuels) sont proposés, ils sont vendus par Google Play selon ses propres conditions et politique de remboursement. Les objets virtuels n'ont aucune valeur monétaire réelle et ne peuvent être ni échangés ni convertis en argent.")),
        ("mises-a-jour", "Mises à jour",
         p("Nous publions régulièrement des mises à jour. Le jeu peut vous proposer de l'installer depuis le Play Store ; certaines fonctions, comme le jeu en réseau, peuvent exiger que tous les joueurs aient la même version.")),
        ("propriete", "Propriété intellectuelle",
         p("Le jeu, son code, ses textes, ses images et ses sons appartiennent à leurs auteurs. Certains modèles 3D et sons sont utilisés sous licence libre (Creative Commons et assimilées) ; leurs auteurs sont crédités dans l'écran <em>Crédits</em> du jeu. Les données de carte proviennent d'OpenStreetMap © ses contributeurs (licence ODbL).")),
        ("responsabilite", "Responsabilité",
         p("Le jeu est fourni « tel quel ». Nous faisons de notre mieux pour qu'il fonctionne bien, mais ne garantissons pas l'absence de bugs, ni la compatibilité avec tous les téléphones. Pensez aux pauses : jouer longtemps peut faire chauffer le téléphone et fatiguer les yeux.")),
        ("donnees", "Données personnelles",
         p('Le traitement de vos données est décrit dans la <a href="politique-confidentialite.html">politique de confidentialité</a>.')),
        ("modifications", "Modification des conditions",
         p("Nous pouvons modifier ces conditions. La date en haut de la page indique la dernière version ; continuer à jouer après une modification vaut acceptation.")),
        ("droit", "Droit applicable et contact",
         p(f"Ces conditions sont régies par le droit du Bénin, sans préjudice des droits impératifs que vous accorde la loi de votre pays de résidence. Pour toute question ou litige, écrivez d'abord à {M} : nous chercherons une solution à l'amiable.")),
    ])

# ── Suppression des données ─────────────────────────────────────────────────
doc("suppression-donnees.html", "Suppression des données — Zemi Dede", "Supprimer vos données Zemi Dede",
    "Comment supprimer vos données du jeu Zemi Dede.",
    "Zemi Dede n'a pas de compte. Voici comment effacer votre progression et les statistiques anonymes.",
    [
        ("progression", "Votre progression",
         p("Votre progression est uniquement sur votre téléphone. Pour l'effacer :")
         + '                    <ol class="steps">\n'
         + "                        <li>Ouvrez les <strong>Paramètres</strong> d'Android, puis <strong>Applications › Zemi Dede</strong>.</li>\n"
         + "                        <li>Touchez <strong>Stockage › Effacer les données</strong>, ou désinstallez simplement le jeu.</li>\n"
         + "                    </ol>\n"),
        ("statistiques", "Statistiques anonymes",
         p("Pour que le jeu n'envoie plus rien, coupez <em>Réglages › Statistiques anonymes</em> dans le jeu.")
         + p(f"Pour supprimer les statistiques déjà envoyées, écrivez à <a href=\"mailto:{MAIL}?subject=Suppression%20de%20mes%20donn%C3%A9es%20Zemi%20Dede\">{MAIL}</a> avec pour objet « Suppression de mes données Zemi Dede », en joignant l'identifiant affiché dans <em>Réglages › À propos</em>. Nous les supprimons sous 30 jours et vous le confirmons.")),
        ("achats", "Achats",
         p("L'historique de vos achats Google Play est conservé par Google selon ses propres règles, et peut être consulté depuis votre compte Google Play.")),
        ("conservation", "Données conservées après suppression",
         p("Nous ne conservons aucune copie de vos données après suppression, sauf si la loi nous y oblige. Sans demande de votre part, les statistiques sont effacées automatiquement après 14 mois.")),
    ])

# ── Accueil ─────────────────────────────────────────────────────────────────
cards = [
    ("politique-confidentialite.html", "Politique de confidentialité", "Quelles données le jeu utilise, comment les refuser, et vos droits."),
    ("conditions-utilisation.html", "Conditions d'utilisation", "Les règles du jeu : licence, achats, jeu en réseau, responsabilité."),
    ("suppression-donnees.html", "Suppression des données", "Effacer votre progression et les statistiques anonymes."),
    (f"mailto:{MAIL}", "Contact", f"Une question, un bug ou une faille à signaler : {MAIL}"),
]
grid = "".join(f"""
            <a class="hub-card" href="{h}">
                <h2>{t}</h2>
                <p>{d}</p>
            </a>""" for h, t, d in cards)
(DIR / "index.html").write_text(head("Zemi Dede — documents", "Zemi Dede : jeu de zémidjan à Cotonou. Confidentialité, conditions d'utilisation et suppression des données.") + topbar() + f"""
        <section class="hub-hero">
            <img src="./assets/icon-192.png" alt="Icône de Zemi Dede" />
            <div>
                <h1>Zemi Dede</h1>
                <p>Conduis-moi doucement. Prends la moto, charge tes clients et traverse Cotonou en zémidjan, seul ou à plusieurs sur le même Wi-Fi.</p>
            </div>
        </section>

        <main class="hub-grid">{grid}
        </main>
""" + footer(), encoding="utf-8")
print("ok")
