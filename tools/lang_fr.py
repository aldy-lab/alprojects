# -*- coding: utf-8 -*-
"""
French. Keys are the English source exactly as built -- see tools/i18n.py.

TERMINOLOGY
    The trade vocabulary is the part that has to be right, because the readers
    are the people who use it daily:
        non-destructive testing  -> contrôle non destructif (CND)
        rope access              -> travaux sur cordes  (IRATA's own term)
        pipe fitter              -> tuyauteur           (not "monteur de tubes")
        WPS / WPQR               -> DMOS / QMOS         (the French standard names)
        root pass                -> passe de racine
        penetrant testing        -> ressuage
        undercut                 -> caniveau
        handover dossier         -> dossier des ouvrages exécutés (DOE)
        scope (of work)          -> périmètre           (not "portée")
    "Offshore" and "spool" are used untranslated in French industry and are
    left alone deliberately.

⚠️ Have a native French speaker in the market review the services, sectors and
   certification copy before go-live, and a lawyer review the privacy policy.
"""

S = {
    '3 photographs, 2 stages':
        '3 photographies, 2 étapes',
    '5 photographs, 4 stages':
        '5 photographies, 4 étapes',
    '6 photographs, 5 stages':
        '6 photographies, 5 étapes',
    '<span class="case-num">02</span> <span class="case-kicker">Shop fabrication and welding</span>':
        '<span class="case-num">02</span> <span class="case-kicker">Fabrication et soudage en atelier</span>',
    '<span class="case-num">03</span> <span class="case-kicker">Mechanical installation and welding &middot; tank farm</span>':
        '<span class="case-num">03</span> <span class="case-kicker">Montage mécanique et soudage &middot; parc de stockage</span>',
    '<span class="case-num">04</span> <span class="case-kicker">Mechanical installation and welding</span>':
        '<span class="case-num">04</span> <span class="case-kicker">Montage mécanique et soudage</span>',
    '<span class="case-num">05</span> <span class="case-kicker">Mechanical installation</span>':
        '<span class="case-num">05</span> <span class="case-kicker">Montage mécanique</span>',
    '<span class="slide-label">Stage</span> <span class="slide-count">01 / 04</span>':
        '<span class="slide-label">Étape</span> <span class="slide-count">01 / 04</span>',
    '<span class="slide-label">Stage</span> <span class="slide-count">02 / 04</span>':
        '<span class="slide-label">Étape</span> <span class="slide-count">02 / 04</span>',
    '<span class="slide-label">Stage</span> <span class="slide-count">03 / 04</span>':
        '<span class="slide-label">Étape</span> <span class="slide-count">03 / 04</span>',
    '<span class="slide-label">Stage</span> <span class="slide-count">04 / 04</span>':
        '<span class="slide-label">Étape</span> <span class="slide-count">04 / 04</span>',
    '<span>© 2019–2026 ALPROJECTS GROUP. All rights reserved.</span> <span class="legal-ids">Company code 305137109 &middot; VAT LT100012753216</span> <a class="made-by" href="https://aldystudio.com" target="_blank" rel="noopener">Made by <b>ALDY</b></a>':
        '<span>© 2019–2026 ALPROJECTS GROUP. Tous droits réservés.</span> <span class="legal-ids">Code d’entreprise 305137109 &middot; TVA LT100012753216</span> <a class="made-by" href="https://aldystudio.com" target="_blank" rel="noopener">Réalisé par <b>ALDY</b></a>',
    'Company code 305137109 &middot; VAT LT100012753216':
        'Code d’entreprise 305137109 &middot; TVA LT100012753216',
    '<b>ISO 9001 &middot; 14001 &middot; 45001</b><span>Certified by DNV</span>':
        '<b>ISO 9001 &middot; 14001 &middot; 45001</b><span>Certifi\u00e9 par DNV</span>',
    '<b>300+</b><span>Specialists on the books</span>':
        '<b>300+</b><span>Sp\u00e9cialistes inscrits</span>',
    '<b>6 countries</b><span>9 project bases</span>':
        '<b>6 pays</b><span>9 bases de projet</span>',
    '<b>Strongest in Lithuania</b><span>Creditinfo, 2025&ndash;2026</span>':
        '<b>Entreprise la plus solide de Lituanie</b><span>Creditinfo, 2025&ndash;2026</span>',
    'Key facts':
        'Chiffres cl\u00e9s',
    'Next step':
        'Étape suivante',
    'Book a 30-minute call':
        'Réserver 30 minutes',
    'Direct contact':
        'Contact direct',
    '<span class="cta-direct-label">Phone</span><a href="tel:+37063663744">+370 636 63 744</a>':
        '<span class="cta-direct-label">Téléphone</span><a href="tel:+37063663744">+370 636 63 744</a>',
    '<span class="cta-direct-label">WhatsApp</span><a href="https://wa.me/37063663744" target="_blank" rel="noopener">+370 636 63 744</a>':
        '<span class="cta-direct-label">WhatsApp</span><a href="https://wa.me/37063663744" target="_blank" rel="noopener">+370 636 63 744</a>',
    'GWO':
        'GWO',
    'Home':
        'Accueil',
    'News':
        'Actualités',
    'Apply':
        'Postuler',
    'Award':
        'Distinction',
    'Close':
        'Fermer',
    'Email':
        'E-mail',
    'Legal':
        'Mentions légales',
    'Other':
        'Autre',
    'Phone':
        'Téléphone',
    'Scale':
        'Effectif',
    'Marine':
        'Naval',
    'NDT UT':
        'CND UT',
    'NDT VT':
        'CND VT',
    'Norway':
        'Norvège',
    'Poland':
        'Pologne',
    'Seafox':
        'Seafox',
    'Sector':
        'Secteur',
    'Select':
        'Sélectionner',
    'Belgium':
        'Belgique',
    'Careers':
        'Carrières',
    'Company':
        'Entreprise',
    'Denmark':
        'Danemark',
    'General':
        'Général',
    'Germany':
        'Allemagne',
    'Hamburg':
        'Hambourg',
    'Rigging':
        'Levage',
    'Rostock':
        'Rostock',
    'Sectors':
        'Secteurs',
    'Welders':
        'Soudeurs',
    'Ålesund':
        'Ålesund',
    'About Us':
        'À propos',
    'All news':
        'Toutes les actualités',
    'Contacts':
        'Contact',
    'Email us':
        'Nous écrire',
    'Facebook':
        'Facebook',
    'IRATA L1':
        'IRATA N1',
    'IRATA L2':
        'IRATA N2',
    'IRATA L3':
        'IRATA N3',
    'ISO:9001':
        'ISO:9001',
    'Language':
        'Langue',
    'LinkedIn':
        'LinkedIn',
    'Offshore':
        'Offshore',
    'Orkanger':
        'Orkanger',
    'Our news':
        'Actualités',
    'Position':
        'Poste',
    'Projects':
        'Projets',
    'Services':
        'Services',
    'Countries':
        'Pays',
    'Frankfurt':
        'Francfort',
    'From site':
        'Depuis le chantier',
    'Full name':
        'Nom complet',
    'ISO:14001':
        'ISO:14001',
    'ISO:45001':
        'ISO:45001',
    'Instagram':
        'Instagram',
    'Issued by':
        'Délivré par',
    'Lithuania':
        'Lituanie',
    'NDT PT/MT':
        'CND PT/MT',
    'Newcastle':
        'Newcastle',
    'Open menu':
        'Ouvrir le menu',
    'Read more':
        'Lire la suite',
    'Subscribe':
        'S’abonner',
    'VCA / SCC':
        'VCA / SCC',
    '1 location':
        '1 site',
    '7. Changes':
        '7. Modifications',
    'Continuous':
        'En continu',
    'Discipline':
        'Métier',
    'Hiring now':
        'Recrutement en cours',
    'Industrial':
        'Industrie',
    'Industries':
        'Secteurs',
    'Newsletter':
        'Newsletter',
    'Our people':
        'Nos équipes',
    'Renewables':
        'Renouvelables',
    'Talk to us':
        'Parlons-en',
    'What we do':
        'Ce que nous faisons',
    '2 locations':
        '2 sites',
    '3 locations':
        '3 sites',
    'Book a call':
        'Réserver un appel',
    'Head office':
        'Siège social',
    'Netherlands':
        'Pays-Bas',
    'Rope access':
        'Travaux sur cordes',
    'Ship Repair':
        'Réparation navale',
    'Ship repair':
        'Réparation navale',
    '2 to 5 years':
        '2 à 5 ans',
    '23 June 2026':
        '23 juin 2026',
    'All services':
        'Tous les services',
    'Certified to':
        'Certifié selon',
    'Download PDF':
        'Télécharger le PDF',
    'Electricians':
        'Électriciens',
    'Headquarters':
        'Siège',
    'Made by ALDY':
        'Réalisé par ALDY',
    'Next service':
        'Service suivant',
    'Our Services':
        'Nos services',
    'Our services':
        'Nos services',
    'Pipe Fitters':
        'Tuyauteurs',
    'Pipe Fitting':
        'Tuyauterie',
    'Pipe fitting':
        'Tuyauterie',
    'Shipbuilding':
        'Construction navale',
    'What we need':
        'Ce que nous recherchons',
    'Working from':
        'Implantations',
    '1. Who we are':
        '1. Qui nous sommes',
    '5 to 10 years':
        '5 à 10 ans',
    '<b>Norway</b>':
        '<b>Norvège</b>',
    'Certification':
        'Certification',
    'Meet the team':
        'L’équipe',
    'Open position':
        'Poste ouvert',
    'Our footprint':
        'Notre implantation',
    'Project bases':
        'Bases projet',
    'Status: Ready':
        'Statut : prêt',
    'Steel Fitters':
        'Monteurs métalliers',
    'Thermo Fisher':
        'Thermo Fisher',
    'Welding (TIG)':
        'Soudage (TIG)',
    'Where we work':
        'Où nous intervenons',
    '4. Legal basis':
        '4. Base légale',
    '6. Your rights':
        '6. Vos droits',
    '<b>Belgium</b>':
        '<b>Belgique</b>',
    '<b>Germany</b>':
        '<b>Allemagne</b>',
    'Available from':
        'Disponible à partir du',
    'Certifications':
        'Certifications',
    'NDT Inspectors':
        'Contrôleurs CND',
    'NDT inspection':
        'Contrôle non destructif',
    'Open positions':
        'Postes ouverts',
    'Our advantages':
        'Nos atouts',
    'Privacy Policy':
        'Politique de confidentialité',
    'United Kingdom':
        'Royaume-Uni',
    'View more news':
        'Voir plus d’actualités',
    'privacy policy':
        'politique de confidentialité',
    'Company Profile':
        'Présentation de l’entreprise',
    'Independent NDT':
        'CND indépendant',
    'MIG/MAG 131/135':
        'MIG/MAG 131/135',
    'Main navigation':
        'Navigation principale',
    'Next photograph':
        'Photo suivante',
    'On our own jobs':
        'Sur nos propres chantiers',
    'Quality Control':
        'Contrôle qualité',
    'Skip to content':
        'Aller au contenu',
    'Start a project':
        'Démarrer un projet',
    'What to include':
        'Ce qu’il faut nous transmettre',
    'What we do here':
        'Ce que nous y faisons',
    'What we work on':
        'Nos domaines d’intervention',
    'Working English':
        'Anglais professionnel',
    '<b>Lithuania</b>':
        '<b>Lituanie</b>',
    'Back to homepage':
        'Retour à l’accueil',
    'Creditinfo Group':
        'Creditinfo Group',
    'Enter Your Email':
        'Saisissez votre e-mail',
    'Name and surname':
        'Nom et prénom',
    'Open application':
        'Candidature spontanée',
    'Previous service':
        'Service précédent',
    'QA/QC Inspectors':
        'Inspecteurs QA/QC',
    'See our projects':
        'Voir nos projets',
    'Send application':
        'Envoyer la candidature',
    'Site supervision':
        'Supervision de chantier',
    'Welding Services':
        'Soudage',
    'Welding services':
        'Soudage',
    '3D Laser Scanning':
        'Scanner laser 3D',
    '3D laser scanning':
        'Scanner laser 3D',
    'Company documents':
        'Documents de l’entreprise',
    'Less than 2 years':
        'Moins de 2 ans',
    'Mobile navigation':
        'Navigation mobile',
    'Mode: Engineering':
        'Mode : ingénierie',
    'More on the award':
        'En savoir plus sur cette distinction',
    'Open in browser <span class="arr">&#8593;</span>':
        'Ouvrir dans le navigateur <span class="arr">&#8593;</span>',
    'Open the calendar':
        'Ouvrir le calendrier',
    'Phone or WhatsApp':
        'Téléphone ou WhatsApp',
    'Project enquiries':
        'Demandes de projet',
    'Send us the scope':
        'Envoyez-nous le périmètre',
    'Welding (MIG/MAG)':
        'Soudage (MIG/MAG)',
    '2. What we collect':
        '2. Ce que nous collectons',
    '<b>Netherlands</b>':
        '<b>Pays-Bas</b>',
    'Local, no rotation':
        'Local, sans rotation',
    'More than 10 years':
        'Plus de 10 ans',
    'Project photograph':
        'Photo de chantier',
    'Reference Projects':
        'Projets de référence',
    'See open positions':
        'Voir les postes ouverts',
    'We did not weld it':
        'Nous ne l’avons pas soudé',
    'What matters to us':
        'Ce qui compte pour nous',
    'Where we work from':
        'D’où nous opérons',
    '03 &middot; Company':
        '03 &middot; Entreprise',
    'All twelve services':
        'Les douze services',
    'Apply for this role':
        'Postuler à ce poste',
    'Industrial projects':
        'Projets industriels',
    'Inspection & Access':
        'Inspection & accès',
    'Integrated Workflow':
        'Processus intégré',
    'Medical certificate':
        'Certificat médical',
    'Mobile Repair Teams':
        'Équipes d’intervention mobiles',
    'Previous photograph':
        'Photo précédente',
    'Technical personnel':
        'Personnel technique',
    '06 &middot; Industry':
        '06 &middot; Industrie',
    '3a. Recruitment data':
        '3a. Données de recrutement',
    'Call +370 636 63 744':
        'Appeler le +370 636 63 744',
    'Certified TIG Welder':
        'Soudeur TIG certifié',
    'EN ISO 9606 (welder)':
        'EN ISO 9606 (soudeur)',
    'Full Project Control':
        'Maîtrise complète du projet',
    'Offshore / North Sea':
        'Offshore / Mer du Nord',
    'Rope Access Services':
        'Travaux sur cordes',
    'Rope access services':
        'Travaux sur cordes',
    'Send us your details':
        'Envoyez-nous votre profil',
    'Work with ALPROJECTS':
        'Travailler avec ALPROJECTS',
    'calendly.com/privacy':
        'calendly.com/privacy',
    '<b>United Kingdom</b>':
        '<b>Royaume-Uni</b>',
    'BLRT Group · Klaipėda':
        'BLRT Group · Klaipėda',
    'Company Profile (PDF)':
        'Présentation de l’entreprise (PDF)',
    'Selected key projects':
        'Projets clés sélectionnés',
    'Specialized personnel':
        'Personnel spécialisé',
    'Take a 30-minute slot':
        'Réservez un créneau de 30 minutes',
    '5. How long we keep it':
        '5. Durée de conservation',
    'Mechanical Contracting':
        'Montage mécanique',
    'Mechanical contracting':
        'Montage mécanique',
    'Select your discipline':
        'Sélectionnez votre métier',
    'Strongest in Lithuania':
        'Strongest in Lithuania',
    'Why choose AL Projects':
        'Pourquoi choisir AL Projects',
    'ALPROJECTS Group — home':
        'ALPROJECTS Group — accueil',
    'Head Office (Lithuania)':
        'Siège social (Lituanie)',
    'Inspection &amp; access':
        'Inspection &amp; accès',
    'Instrument pipe fitting':
        'Tuyauterie instrumentation',
    'Mechanical & Industrial':
        'Mécanique & industrie',
    'Mechanical installation':
        'Montage mécanique',
    'News — ALPROJECTS Group':
        'Actualités — ALPROJECTS Group',
    'Non-Destructive Testing':
        'Contrôle non destructif',
    'Non-destructive testing':
        'Contrôle non destructif',
    'Operating Across Europe':
        'Présents dans toute l’Europe',
    'Quality Control / QA/QC':
        'Contrôle qualité / QA/QC',
    'Quality control / QA/QC':
        'Contrôle qualité / QA/QC',
    'Rope Access Technicians':
        'Techniciens cordistes',
    '02 &middot; Shipbuilding':
        '02 &middot; Construction navale',
    'Cross-Industry Expertise':
        'Expertise multisectorielle',
    'Internal quality control':
        'Contrôle qualité interne',
    "On somebody else's welds":
        'Sur les soudures d’un tiers',
    'One crew, several trades':
        'Une équipe, plusieurs métiers',
    'Quality control and QAQC':
        'Contrôle qualité et QA/QC',
    'Specialists on the books':
        'Spécialistes dans nos effectifs',
    'WhatsApp +370 636 63 744':
        'WhatsApp +370 636 63 744',
    'Wind Turbine Technicians':
        'Techniciens éoliens',
    'Prefer not to fill a form':
        'Vous préférez ne pas remplir de formulaire',
    'Quality control and QA/QC':
        'Contrôle qualité et QA/QC',
    'Short notice mobilisation':
        'Mobilisation à court préavis',
    'Careers — ALPROJECTS Group':
        'Carrières — ALPROJECTS Group',
    'Company — ALPROJECTS Group':
        'Entreprise — ALPROJECTS Group',
    'European Quality Standards':
        'Normes de qualité européennes',
    'Heavy Equipment Relocation':
        'Transfert d’équipements lourds',
    'Heavy equipment relocation':
        'Transfert d’équipements lourds',
    'Lithuania, Belgium, Norway':
        'Lituanie, Belgique, Norvège',
    'Mechanical repair on board':
        'Réparations mécaniques à bord',
    '01 &middot; Quality Control':
        '01 &middot; Contrôle qualité',
    '05 &middot; Energy Projects':
        '05 &middot; Projets énergie',
    'Contacts — ALPROJECTS Group':
        'Contact — ALPROJECTS Group',
    'Experience and availability':
        'Expérience et disponibilité',
    'Initialize project sequence':
        'Lancer la séquence de projet',
    'It never counts as sign off':
        'Cela ne vaut jamais validation',
    'Lift planning and execution':
        'Étude et exécution des levages',
    'No scaffolding, no shutdown':
        'Sans échafaudage, sans arrêt',
    'Offshore — ALPROJECTS Group':
        'Offshore — ALPROJECTS Group',
    'Onshore project experience.':
        'Expérience de projets terrestres.',
    'Projects — ALPROJECTS Group':
        'Projets — ALPROJECTS Group',
    'Services — ALPROJECTS Group':
        'Services — ALPROJECTS Group',
    'fuel loading terminal scope':
        'chantier de terminal de chargement',
    'Dry dock and quayside scopes':
        'Interventions en cale sèche et à quai',
    'Engineering-Driven Decisions':
        'Des décisions guidées par l’ingénierie',
    'Last updated: 15 August 2026':
        'Dernière mise à jour : 15 août 2026',
    'This page could not be found':
        'Page introuvable',
    'Welding quality requirements':
        'Exigences de qualité en soudage',
    '<span class="txt">Home</span>':
        '<span class="txt">Accueil</span>',
    '<span class="txt">News</span>':
        '<span class="txt">Actualités</span>',
    'ALPROJECTS Group project site':
        'Chantier ALPROJECTS Group',
    'Engine room and system piping':
        'Salle des machines et circuits de tuyauterie',
    'Industrial — ALPROJECTS Group':
        'Industrie — ALPROJECTS Group',
    'No interruption to production':
        'Sans interruption de production',
    'Non-destructive testing (NDT)':
        'Contrôle non destructif (CND)',
    'Renewable and energy projects':
        'Projets énergies renouvelables',
    'Renewables — ALPROJECTS Group':
        'Renouvelables — ALPROJECTS Group',
    'Rigging and technical support':
        'Levage et assistance technique',
    'Scalable Project Architecture':
        'Organisation de projet évolutive',
    'Valve manifolds over the bund':
        'Collecteurs de vannes au-dessus de la rétention',
    '<b>6</b><span>Countries</span>':
        '<b>6</b><span>Pays</span>',
    'Completed tank farm pipe racks':
        'Racks à tuyauterie achevés sur un parc de stockage',
    'Offshore and renewable energy.':
        'Offshore et énergies renouvelables.',
    'Ship repair — ALPROJECTS Group':
        'Réparation navale — ALPROJECTS Group',
    'Structural fitting and welding':
        'Montage et soudage de structure',
    '04 &middot; Industrial Projects':
        '04 &middot; Projets industriels',
    'Delivered across five countries':
        'Réalisé dans cinq pays',
    'Fast mobilisation to the vessel':
        'Mobilisation rapide sur le navire',
    'Fuel loading terminal completed':
        'Terminal de chargement de carburant achevé',
    'HKZ Alpha &amp; Beta — Petrofac':
        'HKZ Alpha &amp; Beta — Petrofac',
    'Pipe fitting — ALPROJECTS Group':
        'Tuyauterie — ALPROJECTS Group',
    'Rigging &amp; Technical Support':
        'Levage &amp; assistance technique',
    'Shipbuilding — ALPROJECTS Group':
        'Construction navale — ALPROJECTS Group',
    'We do not certify our own welds':
        'Nous ne certifions pas nos propres soudures',
    'Welding services (TIG, MIG/MAG)':
        'Soudage (TIG, MIG/MAG)',
    '<span class="txt">Careers</span>':
        '<span class="txt">Carrières</span>',
    '<span class="txt">Company</span>':
        '<span class="txt">Entreprise</span>',
    'Offshore and industrial projects':
        'Projets offshore et industriels',
    'Site to site moves across Europe':
        'Déplacements d’un site à l’autre partout en Europe',
    '<span class="txt">Contacts</span>':
        '<span class="txt">Contact</span>',
    '<span class="txt">Projects</span>':
        '<span class="txt">Projets</span>',
    '<span class="txt">Services</span>':
        '<span class="txt">Services</span>',
    'Page not found — ALPROJECTS Group':
        'Page introuvable — ALPROJECTS Group',
    'Privacy Policy — ALPROJECTS Group':
        'Politique de confidentialité — ALPROJECTS Group',
    'Site coordination and supervision':
        'Coordination et supervision de chantier',
    '3. Third parties that receive data':
        '3. Tiers destinataires des données',
    'Clash detection before fabrication':
        'Détection de collisions avant fabrication',
    'Mobile repair teams for refineries':
        'Équipes d’intervention mobiles pour raffineries',
    'Our supervisors and our QA on site':
        'Nos encadrants et notre qualité sur site',
    'Completed pipe runs at a substation':
        'Réseaux de tuyauterie achevés sur un poste électrique',
    'Offshore, shipbuilding and industry':
        'Offshore, construction navale et industrie',
    'Profile &amp;<br>Reference Projects':
        'Présentation &amp;<br>projets de référence',
    'Welding services — ALPROJECTS Group':
        'Soudage — ALPROJECTS Group',
    '3D laser scanning — ALPROJECTS Group':
        'Scanner laser 3D — ALPROJECTS Group',
    '<b>30</b><span>Open positions</span>':
        '<b>30</b><span>Postes ouverts</span>',
    'IRATA and SOFT certified technicians':
        'Techniciens certifiés IRATA et SOFT',
    'Independent third party verification':
        'Vérification indépendante par tierce partie',
    'Steel renewal and piping replacement':
        'Renouvellement de tôles et remplacement de tuyauteries',
    'Data in the client&rsquo;s CAD format':
        'Données au format CAO du client',
    'Download the Company Profile as a PDF':
        'Télécharger la présentation de l’entreprise en PDF',
    'Foundation fit-up and final alignment':
        'Ajustage sur massif et alignement final',
    'Open the Company Profile in a new tab':
        'Ouvrir la présentation de l’entreprise dans un nouvel onglet',
    'Load handling and installation support':
        'Manutention des charges et assistance au montage',
    'Outfitting and mechanical installation':
        'Armement et montage mécanique',
    'Pipe fitting and piping prefabrication':
        'Tuyauterie et préfabrication de tuyauterie',
    'Pipe runs erected along a plant facade':
        'Réseaux de tuyauterie montés le long d’une façade d’usine',
    'Piping installation in the engine room':
        'Montage de tuyauterie en salle des machines',
    'Reporting in the client&rsquo;s format':
        'Rapports au format du client',
    'TIG root pass on a prefabricated spool':
        'Passe de racine TIG sur un tronçon préfabriqué',
    'Cover of the ALPROJECTS Company Profile':
        'Couverture de la présentation d’entreprise ALPROJECTS',
    'Four Sectors,<br>One Set of Disciplines':
        'Quatre secteurs,<br>un même socle de métiers',
    'Mechanical contracting and installation':
        'Montage et installation mécanique',
    'Piping and steel structure verification':
        'Vérification des tuyauteries et des structures métalliques',
    'Rope access services — ALPROJECTS Group':
        'Travaux sur cordes — ALPROJECTS Group',
    'Strongest in Lithuania, 2025&ndash;2026':
        'Strongest in Lithuania, 2025&ndash;2026',
    'Teams that follow the yard&rsquo;s plan':
        'Des équipes qui suivent le planning du chantier naval',
    'Download the Reference Projects as a PDF':
        'Télécharger les projets de référence en PDF',
    'Inspection and mechanical work at height':
        'Inspection et travaux mécaniques en hauteur',
    'Open the Reference Projects in a new tab':
        'Ouvrir les projets de référence dans un nouvel onglet',
    'Rescue plan and supervision on every job':
        'Plan de secours et encadrement sur chaque chantier',
    'Traceability down to the individual weld':
        'Traçabilité jusqu’à la soudure individuelle',
    'Transformer packages and plant equipment':
        'Ensembles transformateurs et équipements d’usine',
    'Weld, material and structural inspection':
        'Contrôle des soudures, des matériaux et des structures',
    'delivered across five European countries':
        'livré dans cinq pays européens',
    '<span class="step-n">02</span> Your trade':
        '<span class="step-n">02</span> Votre métier',
    '<span>Contract</span><b>Project-based</b>':
        '<span>Contrat</span><b>Au projet</b>',
    '<span>Positions</span><b>30 positions</b>':
        '<span>Postes</span><b>30 postes</b>',
    'As-built survey of existing installations':
        'Relevé d’existant des installations en place',
    'Mechanical contracting — ALPROJECTS Group':
        'Montage mécanique — ALPROJECTS Group',
    'Phone <span class="opt">(optional)</span>':
        'Téléphone <span class="opt">(facultatif)</span>',
    'Project coordination and site supervision':
        'Coordination de projet et supervision de chantier',
    'We recruit regularly in these disciplines':
        'Nous recrutons régulièrement dans ces métiers',
    '<b>3</b><span>Working days to reply</span>':
        '<b>3</b><span>Jours ouvrés pour répondre</span>',
    '<span class="step-n">01</span> Who you are':
        '<span class="step-n">01</span> Qui vous êtes',
    'A European provider of industrial services':
        'Un prestataire européen de services industriels',
    'Among the strongest companies in Lithuania':
        'Parmi les entreprises les plus solides de Lituanie',
    'Cover of the ALPROJECTS Reference Projects':
        'Couverture des projets de référence ALPROJECTS',
    'Non-destructive testing — ALPROJECTS Group':
        'Contrôle non destructif — ALPROJECTS Group',
    'Project Updates &amp; Engineering Insights':
        'Avancement des projets &amp; regards d’ingénierie',
    'e.g. TIG 141, IRATA Level 2, VT/PT Level 2':
        'ex. TIG 141, IRATA niveau 2, VT/PT niveau 2',
    '<span class="step-n">03</span> Availability':
        '<span class="step-n">03</span> Disponibilité',
    'Dismantling, skidding, jacking, positioning':
        'Démontage, ripage, vérinage, mise en place',
    'Gas pipeline fabrication &amp; installation':
        'Fabrication &amp; pose de canalisations de gaz',
    'Turnarounds, shutdowns and breakdown repair':
        'Grands arrêts, arrêts de tranche et dépannages',
    'Dimensional control of structures and piping':
        'Contrôle dimensionnel des structures et de la tuyauterie',
    'Mechanical scopes and independent inspection':
        'Périmètres mécaniques et inspection indépendante',
    'Quality control and QA/QC — ALPROJECTS Group':
        'Contrôle qualité et QA/QC — ALPROJECTS Group',
    'TIG for piping, root runs and stainless work':
        'TIG pour la tuyauterie, les passes de racine et l’inox',
    '<span class="step-n">04</span> Your documents':
        '<span class="step-n">04</span> Vos documents',
    'Equipment alignment and mechanical completion':
        'Alignement des équipements et achèvement mécanique',
    'Heavy equipment relocation — ALPROJECTS Group':
        'Transfert d’équipements lourds — ALPROJECTS Group',
    'Jack-up vessel maintenance &amp; repair works':
        'Maintenance &amp; réparation de navires auto-élévateurs',
    'Project Updates &amp;<br>Engineering Insights':
        'Avancement des projets &amp;<br>regards d’ingénierie',
    'Steel fabrication and mechanical installation':
        'Fabrication métallique et montage mécanique',
    '<time datetime="2026-06-23">23 Jun 2026</time>':
        '<time datetime="2026-06-23">23 juin 2026</time>',
    '<time datetime="2026-07-25">25 Jul 2026</time>':
        '<time datetime="2026-07-25">25 juil. 2026</time>',
    '<time datetime="2026-08-01">01 Aug 2026</time>':
        '<time datetime="2026-08-01">01 août 2026</time>',
    '<time datetime="2026-08-08">08 Aug 2026</time>':
        '<time datetime="2026-08-08">08 août 2026</time>',
    '<time datetime="2026-08-13">13 Aug 2026</time>':
        '<time datetime="2026-08-13">13 août 2026</time>',
    'Open the Company Profile as a PDF in a new tab':
        'Ouvrir la présentation de l’entreprise en PDF dans un nouvel onglet',
    'Process lines run alongside insulated ductwork':
        'Lignes process cheminant le long de gaines calorifugées',
    'Mechanical, marine<br>&amp; inspection services':
        'Mécanique, naval<br>&amp; inspection',
    'Pipe rack and cable trays on the loading gantry':
        'Rack à tuyauterie et chemins de câbles sur le portique de chargement',
    'Stainless pipework around a transformer package':
        'Tuyauterie inox autour d’un ensemble transformateur',
    '<b>300</b><span>Specialists on our roster</span>':
        '<b>300</b><span>Spécialistes dans nos effectifs</span>',
    'Carbon steel lines being set out on a plant roof':
        'Lignes en acier carbone implantées en toiture d’usine',
    'Experience with pipe and steel structure welding':
        'Expérience du soudage de tuyauteries et de structures métalliques',
    'One contract, one schedule, one point of contact':
        'Un contrat, un planning, un interlocuteur',
    'Read more about the Strongest in Lithuania award':
        'En savoir plus sur la distinction Strongest in Lithuania',
    'Refrigeration systems · industrial modifications':
        'Installations frigorifiques · modifications industrielles',
    'Rigging and technical support — ALPROJECTS Group':
        'Levage et assistance technique — ALPROJECTS Group',
    'Support at client and third party witness points':
        'Assistance aux points d’arrêt client et tierce partie',
    'Anything else <span class="opt">(optional)</span>':
        'Autre chose <span class="opt">(facultatif)</span>',
    'Mechanical package installed beneath the bushings':
        'Ensemble mécanique installé sous les traversées',
    'Not on the list? Add it in the notes field below.':
        'Absent de la liste ? Indiquez-le dans le champ de remarques ci-dessous.',
    'Offshore commissioning &amp; installation support':
        'Mise en service offshore &amp; assistance au montage',
    'Open the Reference Projects as a PDF in a new tab':
        'Ouvrir les projets de référence en PDF dans un nouvel onglet',
    'Certifications <span class="opt">(optional)</span>':
        'Certifications <span class="opt">(facultatif)</span>',
    'Cooling and process lines at the transformer plant':
        'Lignes de refroidissement et process à l’usine de transformateurs',
    'Fuel loading terminal completed — ALPROJECTS Group':
        'Terminal de chargement de carburant achevé — ALPROJECTS Group',
    'Photographs from delivered and in-progress scopes.':
        'Photographies de chantiers livrés et en cours.',
    'We do not certify our own welds — ALPROJECTS Group':
        'Nous ne certifions pas nos propres soudures — ALPROJECTS Group',
    '© 2019–2026 ALPROJECTS GROUP. All rights reserved.':
        '© 2019–2026 ALPROJECTS GROUP. Tous droits réservés.',
    'Vessel and pipe run carried along the building line':
        'Capacité et tuyauterie acheminées le long du bâtiment',
    'Pump skids and valve stations, terminal loading area':
        'Skids de pompage et postes de vannes, zone de chargement du terminal',
    'Welding coordination and traceability under ISO 3834':
        'Coordination en soudage et traçabilité selon ISO 3834',
    'Mobile repair teams for refineries — ALPROJECTS Group':
        'Équipes d’intervention mobiles pour raffineries — ALPROJECTS Group',
    'Phone: <a href="tel:+37063663744">+370 636 63 744</a>':
        'Téléphone : <a href="tel:+37063663744">+370 636 63 744</a>',
    'Pipe rack running to storage tanks at a fuel terminal':
        'Rack à tuyauterie desservant les réservoirs d’un terminal carburant',
    'TIG welder working on a large-diameter stainless pipe':
        'Soudeur TIG sur une tuyauterie inox de grand diamètre',
    'We needed 30 certified TIG welders — ALPROJECTS Group':
        'Il nous fallait 30 soudeurs TIG certifiés — ALPROJECTS Group',
    'Work under the plant&rsquo;s permit and safety regime':
        'Travaux sous le régime de permis et de sécurité du site',
    'A transformer mechanical package across five countries':
        'Un ensemble mécanique de transformateur dans cinq pays',
    'ALPROJECTS Group — Engineering for Industry & Offshore':
        'ALPROJECTS Group — Ingénierie pour l’industrie et l’offshore',
    'Disconnection and reconnection of piping and utilities':
        'Déconnexion et reconnexion des tuyauteries et des utilités',
    'Fitters working inside a hull block under construction':
        'Monteurs au travail dans un bloc de coque en construction',
    'Preferred rotation <span class="opt">(optional)</span>':
        'Rotation souhaitée <span class="opt">(facultatif)</span>',
    'Subscribe to receive company news and project updates.':
        'Abonnez-vous pour recevoir nos actualités et l’avancement de nos projets.',
    'Transformer package, five countries — ALPROJECTS Group':
        'Ensemble transformateur, cinq pays — ALPROJECTS Group',
    '<span>8 pages</span><span>PDF</span><span>2.7 MB</span>':
        '<span>8 pages</span><span>PDF</span><span>2,7 Mo</span>',
    '<span>Location</span><b>Project sites across Europe</b>':
        '<span>Lieu</span><b>Chantiers en Europe</b>',
    'Years of experience <span class="opt">(optional)</span>':
        'Années d’expérience <span class="opt">(facultatif)</span>',
    '<span>16 pages</span><span>PDF</span><span>2.1 MB</span>':
        '<span>16 pages</span><span>PDF</span><span>2,1 Mo</span>',
    "Among Lithuania's strongest companies — ALPROJECTS Group":
        'Parmi les entreprises les plus solides de Lituanie — ALPROJECTS Group',
    'Country of residence <span class="opt">(optional)</span>':
        'Pays de résidence <span class="opt">(facultatif)</span>',
    'Discuss a project <span class="ar-e" aria-hidden="true">&#8593;</span>':
        'Discuter d’un projet <span class="ar-e" aria-hidden="true">&#8593;</span>',
    'Fit-up, alignment and dimensional control before welding':
        'Accostage, alignement et contrôle dimensionnel avant soudage',
    'Photographs of certificates taken with a phone are fine.':
        'Des photos de certificats prises au téléphone conviennent parfaitement.',
    'TIG root pass being welded on a prefabricated pipe spool':
        'Passe de racine TIG sur un tronçon de tuyauterie préfabriqué',
    'Wind turbine technicians on site at an onshore wind farm':
        'Techniciens éoliens sur un parc éolien terrestre',
    'Piping installation in the engine room — ALPROJECTS Group':
        'Montage de tuyauterie en salle des machines — ALPROJECTS Group',
    '<span>Cert. C550875</span><span>Valid to 07.08.2028</span>':
        '<span>Cert. C550875</span><span>Valable jusqu’au 07.08.2028</span>',
    '<span>Cert. C550877</span><span>Valid to 07.08.2028</span>':
        '<span>Cert. C550877</span><span>Valable jusqu’au 07.08.2028</span>',
    '<span>Cert. C760290</span><span>Valid to 28.07.2028</span>':
        '<span>Cert. C760290</span><span>Valable jusqu’au 28.07.2028</span>',
    'ALPROJECTS GROUP <span>&middot;</span> KLAIPĖDA, LITHUANIA':
        'ALPROJECTS GROUP <span>&middot;</span> KLAIPĖDA, LITUANIE',
    'ALPROJECTS, UAB<br>Šilutės pl. 2, LT-92298<br>Klaipėda':
        'ALPROJECTS, UAB<br>Šilutės pl. 2, LT-92298<br>Klaipėda',
    'not loaded until you press &ldquo;Open the calendar&rdquo;':
        'n’est pas chargé tant que vous n’avez pas cliqué sur &ldquo;Ouvrir le calendrier&rdquo;',
    'ALPROJECTS engineer working from isometric drawings on site':
        'Ingénieur ALPROJECTS travaillant d’après des isométriques sur site',
    'Handover dossier assembled as the work goes, not at the end':
        'Dossier des ouvrages exécutés constitué au fil du chantier, pas à la fin',
    'Welder running a TIG root pass on a prefabricated pipe spool':
        'Soudeur réalisant une passe de racine TIG sur un tronçon de tuyauterie préfabriqué',
    'Countries you can work in <span class="opt">(optional)</span>':
        'Pays où vous pouvez travailler <span class="opt">(facultatif)</span>',
    'Structural steel, pressure retaining piping and pipe supports':
        'Charpente métallique, tuyauterie sous pression et supportage',
    'Valid TIG welding certification with supporting documentation':
        'Certification de soudage TIG en cours de validité, avec les justificatifs',
    'Industrial maintenance · equipment &amp; hydro-turbine repairs':
        'Maintenance industrielle · réparation d’équipements &amp; de turbines hydrauliques',
    'WPS and WPQR to EN ISO 15614, written for the project standard':
        'DMOS et QMOS selon EN ISO 15614, rédigés pour la norme du projet',
    'MIG and semi-automatic MAG for structural steel and fill passes':
        'MIG et MAG semi-automatique pour la charpente et les passes de remplissage',
    'Process and utility piping: carbon steel, stainless, large bore':
        'Tuyauterie process et utilités : acier carbone, inox, gros diamètre',
    'Project updates and engineering insights from ALPROJECTS Group.':
        'Avancement des projets et regards d’ingénierie d’ALPROJECTS Group.',
    'Willingness to travel and work on site across several countries':
        'Disponibilité pour se déplacer et travailler sur chantier dans plusieurs pays',
    'Email us</a> <a class="btn-bracket" href="/careers">Careers':
        'Nous écrire</a> <a class="btn-bracket" href="/careers">Carrières',
    'Jack-up structures · steel erection · welding · offshore support':
        'Structures auto-élévatrices · montage métallique · soudage · assistance offshore',
    'ALPROJECTS Group — Integrated Engineering for Industry & Offshore':
        'ALPROJECTS Group — Ingénierie intégrée pour l’industrie et l’offshore',
    'ALPROJECTS, UAB — Šilutės pl. 2, LT-92298 Klaipėda, Lithuania':
        'ALPROJECTS, UAB — Šilutės pl. 2, LT-92298 Klaipėda, Lituanie',
    'Email: <a href="mailto:info@alprojects.eu">info@alprojects.eu</a>':
        'E-mail : <a href="mailto:info@alprojects.eu">info@alprojects.eu</a>',
    'Railway bridges · steel fitting · structural repairs · 5G welding':
        'Ponts ferroviaires · montage métallique · réparations structurelles · soudage 5G',
    'Start a project</a> <a class="btn-bracket" href="/news/">All news':
        'Démarrer un projet</a> <a class="btn-bracket" href="/news/">Toutes les actualités',
    'We needed 30 certified TIG welders. Europe could not supply them.':
        'Il nous fallait 30 soudeurs TIG certifiés. L’Europe n’a pas pu les fournir.',
    'Welder running a TIG root pass on a large-diameter stainless pipe':
        'Soudeur réalisant une passe de racine TIG sur une tuyauterie inox de grand diamètre',
    'A serious approach to safety in complex and confined environments.':
        'Une approche rigoureuse de la sécurité en milieu complexe et confiné.',
    'Welder qualifications to EN ISO 9606, verified before mobilisation':
        'Qualifications de soudeurs selon EN ISO 9606, vérifiées avant mobilisation',
    'ALPROJECTS Group — integrated engineering for industry and offshore':
        'ALPROJECTS Group — ingénierie intégrée pour l’industrie et l’offshore',
    'Our services</a> <a class="btn-bracket" href="/#team">Meet the team':
        'Nos services</a> <a class="btn-bracket" href="/#team">L’équipe',
    'Rope access technician working beneath an offshore platform walkway':
        'Cordiste au travail sous une passerelle de plateforme offshore',
    'Send us the scope and we will come back with a price and crew dates.':
        'Envoyez-nous le périmètre et nous reviendrons avec un prix et des dates d’équipe.',
    'Stainless pipework and transformer package installed at a substation':
        'Tuyauterie inox et ensemble transformateur installés sur un poste électrique',
    'Willingness to travel &mdash; our projects run in several countries.':
        'Disponibilité pour se déplacer &mdash; nos projets se déroulent dans plusieurs pays.',
    'Working English; Lithuanian, Russian or Polish are useful additions.':
        'Anglais professionnel ; le lituanien, le russe ou le polonais sont un plus.',
    'Sea water, bilge, ballast and fuel lines going in on board right now.':
        'Circuits d’eau de mer, de cale, de ballast et de combustible en cours de montage à bord.',
    '<span class="srv-n">07</span><span class="srv-name">Ship Repair</span>':
        '<span class="srv-n">07</span><span class="srv-name">Réparation navale</span>',
    'DNV management system certificate — ISO 9001:2015, certificate C760290':
        'Certificat de système de management DNV — ISO 9001:2015, certificat C760290',
    'Site installation, flange assembly and support during pressure testing':
        'Montage sur site, assemblage des brides et assistance aux épreuves de pression',
    '<span class="srv-n">02</span><span class="srv-name">Pipe Fitting</span>':
        '<span class="srv-n">02</span><span class="srv-name">Tuyauterie</span>',
    '<span class="srv-n">06</span><span class="srv-name">Shipbuilding</span>':
        '<span class="srv-n">06</span><span class="srv-name">Construction navale</span>',
    '<strong>GitHub, Inc.</strong> &mdash; website hosting and request logs.':
        '<strong>GitHub, Inc.</strong> &mdash; hébergement du site et journaux de requêtes.',
    'Completed pipe rack running to storage tanks at a fuel loading terminal':
        'Rack à tuyauterie achevé desservant les réservoirs d’un terminal de chargement',
    'DNV management system certificate — ISO 14001:2015, certificate C550875':
        'Certificat de système de management DNV — ISO 14001:2015, certificat C550875',
    'DNV management system certificate — ISO 45001:2018, certificate C550877':
        'Certificat de système de management DNV — ISO 45001:2018, certificat C550877',
    'Disciplines you work in, years of experience, and when you could start.':
        'Vos métiers, vos années d’expérience et votre date de disponibilité.',
    'Open the ISO 9001:2015 certificate as a PDF, certificate number C760290':
        'Ouvrir le certificat ISO 9001:2015 en PDF, certificat n° C760290',
    'Or write to <a href="mailto:info@alprojects.eu">info@alprojects.eu</a>.':
        'Ou écrivez-nous à <a href="mailto:info@alprojects.eu">info@alprojects.eu</a>.',
    'Send us the drawings and we will come back with a price and crew dates.':
        'Envoyez-nous les plans et nous reviendrons avec un prix et des dates d’équipe.',
    'Engineering expertise backed by certified specialists and safe execution':
        'Une expertise d’ingénierie portée par des spécialistes certifiés et une exécution sûre',
    'Open the ISO 14001:2015 certificate as a PDF, certificate number C550875':
        'Ouvrir le certificat ISO 14001:2015 en PDF, certificat n° C550875',
    'Open the ISO 45001:2018 certificate as a PDF, certificate number C550877':
        'Ouvrir le certificat ISO 45001:2018 en PDF, certificat n° C550877',
    'ALPROJECTS, UAB<br> Šilutės pl. 2<br> LT-92298 Klaipėda<br> Lithuania':
        'ALPROJECTS, UAB<br> Šilutės pl. 2<br> LT-92298 Klaipėda<br> Lituanie',
    'Overlay the drafting sheet — grid, registration marks and live dimensions':
        'Afficher le calque de dessin — trame, repères de calage et cotes en direct',
    'Spool prefabrication from isometrics, marked and traceable to the drawing':
        'Préfabrication de tronçons à partir des isométriques, repérés et traçables au plan',
    'How ALPROJECTS Group handles personal data collected through this website.':
        'Comment ALPROJECTS Group traite les données personnelles collectées via ce site.',
    'Marine pipe fitters: engine room and system piping on newbuilds and repair':
        'Tuyauteurs navals : salle des machines et circuits, en construction neuve comme en réparation',
    '<span class="srv-n">01</span><span class="srv-name">Welding Services</span>':
        '<span class="srv-n">01</span><span class="srv-name">Soudage</span>',
    '<span class="srv-n">10</span><span class="srv-name">3D Laser Scanning</span>':
        '<span class="srv-n">10</span><span class="srv-name">Scanner laser 3D</span>',
    'September 2025 to April 2026. Twelve specialists. Over 11,000 hours on site.':
        'De septembre 2025 à avril 2026. Douze spécialistes. Plus de 11 000 heures sur site.',
    'Certificates you hold <span class="opt">(optional, tap all that apply)</span>':
        'Certifications que vous détenez <span class="opt">(facultatif, sélectionnez tout ce qui s’applique)</span>',
    'Our services</a> <a class="btn-bracket" href="/contacts">Start a project':
        'Nos services</a> <a class="btn-bracket" href="/contacts">Démarrer un projet',
    'Valid certification for your discipline, and the documentation to support it.':
        'Une certification en cours de validité pour votre métier, et les justificatifs correspondants.',
    '<span class="srv-n">05</span><span class="srv-name">Mobile Repair Teams</span>':
        '<span class="srv-n">05</span><span class="srv-name">Équipes d’intervention mobiles</span>',
    '<span class="srv-n">09</span><span class="srv-name">Rope Access Services</span>':
        '<span class="srv-n">09</span><span class="srv-name">Travaux sur cordes</span>',
    'Hull block under construction with fitters working inside the scaffolded section':
        'Bloc de coque en construction, monteurs au travail dans la section échafaudée',
    '<span class="srv-n">03</span><span class="srv-name">Mechanical Contracting</span>':
        '<span class="srv-n">03</span><span class="srv-name">Montage mécanique</span>',
    '<span class="srv-n">08</span><span class="srv-name">Non-Destructive Testing</span>':
        '<span class="srv-n">08</span><span class="srv-name">Contrôle non destructif</span>',
    '<span class="srv-n">11</span><span class="srv-name">Quality Control / QA/QC</span>':
        '<span class="srv-n">11</span><span class="srv-name">Contrôle qualité / QA/QC</span>',
    'Instrument pipe fitters: small bore, tubing, impulse lines and instrument hook-ups':
        'Tuyauteurs instrumentation : petit diamètre, tubing, lignes d’impulsion et raccordements d’instruments',
    'Cruise &amp; river vessels · piping systems · pressure testing · structural welding':
        'Navires de croisière &amp; fluviaux · réseaux de tuyauterie · épreuves de pression · soudage structurel',
    'Offshore reel manufacturing · ship repair · piping systems · industrial maintenance':
        'Fabrication de touret offshore · réparation navale · réseaux de tuyauterie · maintenance industrielle',
    'Our NDT does not replace your inspector. We use it to catch our own mistakes first.':
        'Nos CND ne remplacent pas votre contrôleur. Nous les utilisons d’abord pour détecter nos propres erreurs.',
    'Planning a project across shipbuilding, piping or industrial services? Let us talk.':
        'Vous préparez un projet en construction navale, tuyauterie ou services industriels ? Parlons-en.',
    'Send us the scope</a> <a class="btn-outline" href="/projects">See our projects':
        'Envoyez-nous le périmètre</a> <a class="btn-outline" href="/projects">Voir nos projets',
    'Send us the scope or the drawings and we will come back with a price and crew dates.':
        'Envoyez-nous le périmètre ou les plans et nous reviendrons avec un prix et des dates d’équipe.',
    '<span class="srv-n">04</span><span class="srv-name">Heavy Equipment Relocation</span>':
        '<span class="srv-n">04</span><span class="srv-name">Transfert d’équipements lourds</span>',
    'If you hold the ticket and you are willing to travel, we would like to hear from you.':
        'Si vous avez la qualification et que vous acceptez de vous déplacer, écrivez-nous.',
    '<strong>Industrial</strong> — plant installation, transformer packages, process piping.':
        '<strong>Industrie</strong> — installation d’unités, ensembles transformateurs, tuyauterie process.',
    'Spool base &amp; offshore platforms · pipeline welding · fabrication · offshore support':
        'Base de tronçons &amp; plateformes offshore · soudage de pipelines · fabrication · assistance offshore',
    'Certificate numbers and expiry dates, projects you have worked on, when you could start.':
        'Numéros et dates de validité des certifications, projets sur lesquels vous avez travaillé, date de disponibilité.',
    '<span class="srv-n">12</span><span class="srv-name">Rigging &amp; Technical Support</span>':
        '<span class="srv-n">12</span><span class="srv-name">Levage &amp; assistance technique</span>',
    '<span>30 positions</span><span>Project sites across Europe</span><span>Project-based</span>':
        '<span>30 postes</span><span>Chantiers en Europe</span><span>Au projet</span>',
    '<strong>Offshore</strong> — inspection, access and mechanical works on offshore facilities.':
        '<strong>Offshore</strong> — inspection, accès et travaux mécaniques sur installations offshore.',
    'The skilled trades shortage is not an abstraction when it is your project that cannot start.':
        'La pénurie de métiers qualifiés n’a rien d’abstrait quand c’est votre projet qui ne peut pas démarrer.',
    'The link may be out of date, or the page may have moved. Everything we do is on the homepage.':
        'Le lien est peut-être obsolète, ou la page a été déplacée. L’ensemble de nos activités figure sur la page d’accueil.',
    '<span class="num">03</span><span>23 Jun 2026 &middot; Company</span><span class="arr">&#8593;</span>':
        '<span class="num">03</span><span>23 juin 2026 &middot; Entreprise</span><span class="arr">&#8593;</span>',
    '<strong>Energy and renewables</strong> — fuel handling infrastructure and wind energy support.':
        '<strong>Énergie et renouvelables</strong> — infrastructures de manutention de carburant et assistance à l’éolien.',
    '<span class="num">06</span><span>25 Jul 2026 &middot; Industry</span><span class="arr">&#8593;</span>':
        '<span class="num">06</span><span>25 juil. 2026 &middot; Industrie</span><span class="arr">&#8593;</span>',
    '<span class="bp-key" aria-hidden="true">B</span> <span class="bp-hint-label">Drawing mode</span>':
        '<span class="bp-key" aria-hidden="true">B</span> <span class="bp-hint-label">Mode dessin</span>',
    'Lifts go wrong at the planning stage. We plan them, and we send the people who run them on site.':
        'Un levage se rate à l’étude. Nous les étudions, et nous envoyons les personnes qui les conduisent sur site.',
    '<strong>Shipbuilding</strong> — piping and mechanical installation on vessels under construction.':
        '<strong>Construction navale</strong> — tuyauterie et montage mécanique sur navires en construction.',
    'UAB “ALprojects” has been awarded the Strongest in Lithuania 2025–2026 certificate by Creditinfo.':
        'UAB « ALprojects » s’est vu décerner par Creditinfo le certificat Strongest in Lithuania 2025–2026.',
    'We read every application and reply within three working days when a project matches your profile.':
        'Nous lisons chaque candidature et répondons sous trois jours ouvrés lorsqu’un projet correspond à votre profil.',
    '<span class="num">02</span><span>08 Aug 2026 &middot; Shipbuilding</span><span class="arr">&#8593;</span>':
        '<span class="num">02</span><span>08 août 2026 &middot; Construction navale</span><span class="arr">&#8593;</span>',
    '<span class="num">03</span><span>23 Jun 2026 &middot; Company</span><span class="arr">&#8593;</span>':
        '<span class="num">03</span><span>23 juin 2026 &middot; Entreprise</span><span class="arr">&#8593;</span>',
    '<span class="num">06</span><span>25 Jul 2026 &middot; Industry</span><span class="arr">&#8593;</span>':
        '<span class="num">06</span><span>25 juil. 2026 &middot; Industrie</span><span class="arr">&#8593;</span>',
    'Straight into the diary of someone who can answer technical questions — scope, standards, crew dates.':
        'Directement dans l’agenda de quelqu’un capable de répondre aux questions techniques : périmètre, normes, dates d’équipe.',
    '<span class="num">01</span><span>13 Aug 2026 &middot; Quality Control</span><span class="arr">&#8593;</span>':
        '<span class="num">01</span><span>13 août 2026 &middot; Contrôle qualité</span><span class="arr">&#8593;</span>',
    '<span class="num">05</span><span>25 Jul 2026 &middot; Energy Projects</span><span class="arr">&#8593;</span>':
        '<span class="num">05</span><span>25 juil. 2026 &middot; Projets énergie</span><span class="arr">&#8593;</span>',
    'If this policy changes, the revised version will be published on this page with a new date at the top.':
        'En cas de modification de la présente politique, la version révisée sera publiée sur cette page avec une nouvelle date en tête.',
    'Qualified specialists, available for project-based, short-term and long-term assignments across Europe.':
        'Des spécialistes qualifiés, disponibles pour des missions au projet, à court et à long terme partout en Europe.',
    '<span class="contact-label">General</span> <a href="mailto:office@alprojects.eu">office@alprojects.eu</a>':
        '<span class="contact-label">Général</span> <a href="mailto:office@alprojects.eu">office@alprojects.eu</a>',
    '<span class="num">02</span><span>08 Aug 2026 &middot; Shipbuilding</span><span class="arr">&#8593;</span>':
        '<span class="num">02</span><span>08 août 2026 &middot; Construction navale</span><span class="arr">&#8593;</span>',
    'Six fields are required. Everything else helps us match you faster, but you can send the form without it.':
        'Six champs sont obligatoires. Le reste nous aide à vous positionner plus vite, mais vous pouvez envoyer le formulaire sans.',
    'Stainless steel piping, cooling systems and precision installation — repeated across five European sites.':
        'Tuyauterie inox, circuits de refroidissement et montage de précision — répétés sur cinq sites européens.',
    '<span class="num">04</span><span>01 Aug 2026 &middot; Industrial Projects</span><span class="arr">&#8593;</span>':
        '<span class="num">04</span><span>01 août 2026 &middot; Projets industriels</span><span class="arr">&#8593;</span>',
    '<span class="num">01</span><span>13 Aug 2026 &middot; Quality Control</span><span class="arr">&#8593;</span>':
        '<span class="num">01</span><span>13 août 2026 &middot; Contrôle qualité</span><span class="arr">&#8593;</span>',
    '<span class="num">05</span><span>25 Jul 2026 &middot; Energy Projects</span><span class="arr">&#8593;</span>':
        '<span class="num">05</span><span>25 juil. 2026 &middot; Projets énergie</span><span class="arr">&#8593;</span>',
    'Contact ALPROJECTS Group — Šilutės pl. 2, Klaipėda, Lithuania. Project enquiries and personnel requests.':
        'Contacter ALPROJECTS Group — Šilutės pl. 2, Klaipėda, Lituanie. Demandes de projet et de personnel.',
    'Mechanical contracting, pipe fitting, welding services, QAQC, rope access and NDT for industry and offshore.':
        'Montage mécanique, tuyauterie, soudage, QA/QC, travaux sur cordes et CND pour l’industrie et l’offshore.',
    'Welding, piping and mechanical works across Europe and Scandinavia. Inspected by people who did not do the welding.':
        'Soudage, tuyauterie et travaux mécaniques dans toute l’Europe et la Scandinavie. Contrôlés par ceux qui n’ont pas exécuté la soudure.',
    'Shipbuilding, offshore, industrial and renewable energy projects delivered by ALPROJECTS Group across Europe.':
        'Projets de construction navale, offshore, industriels et d’énergies renouvelables réalisés par ALPROJECTS Group partout en Europe.',
    '<span>Offshore &amp; Marine</span><span>Energy</span><span>Heavy Industry</span><span>Steel Fabrication</span>':
        '<span>Offshore &amp; naval</span><span>Énergie</span><span>Industrie lourde</span><span>Fabrication métallique</span>',
    'This website has no user accounts, no analytics and sets no cookies of its own. Data reaches us in three ways:':
        'Ce site ne comporte ni compte utilisateur, ni outil de mesure d’audience, et ne dépose aucun cookie qui lui soit propre. Les données nous parviennent de trois manières :',
    '<span class="contact-label">Project enquiries</span> <a href="mailto:info@alprojects.eu">info@alprojects.eu</a>':
        '<span class="contact-label">Demandes de projet</span> <a href="mailto:info@alprojects.eu">info@alprojects.eu</a>',
    '<span class="num">04</span><span>01 Aug 2026 &middot; Industrial Projects</span><span class="arr">&#8593;</span>':
        '<span class="num">04</span><span>01 août 2026 &middot; Projets industriels</span><span class="arr">&#8593;</span>',
    '<span>Industrial Plants</span><span>Offshore Structures</span><span>Wind Energy</span><span>Infrastructure</span>':
        '<span>Sites industriels</span><span>Structures offshore</span><span>Éolien</span><span>Infrastructures</span>',
    'Yard schedules do not move. Our crews slot into them and take engine room piping, structural steel and outfitting.':
        'Les plannings de chantier naval ne bougent pas. Nos équipes s’y insèrent et prennent la tuyauterie de salle des machines, la charpente et l’armement.',
    '<span>Offshore</span><span>Industrial Construction</span><span>Energy Projects</span><span>Marine Facilities</span>':
        '<span>Offshore</span><span>Construction industrielle</span><span>Projets énergie</span><span>Installations navales</span>',
    'This page could not be found. Return to the ALPROJECTS Group homepage for industrial, offshore and energy services.':
        'Page introuvable. Retournez à l’accueil d’ALPROJECTS Group pour nos services industriels, offshore et énergie.',
    'Tell us your discipline and certifications. We read every application and reply when a project matches your profile.':
        'Indiquez-nous votre métier et vos certifications. Nous lisons chaque candidature et revenons vers vous dès qu’un projet correspond à votre profil.',
    '<span>Offshore Platforms</span><span>Wind Turbines</span><span>Industrial Towers</span><span>Marine Structures</span>':
        '<span>Plateformes offshore</span><span>Éoliennes</span><span>Tours industrielles</span><span>Structures navales</span>',
    '<strong>Calendly LLC</strong> &mdash; the scheduling calendar on the contacts page, and only if you choose to open it.':
        '<strong>Calendly LLC</strong> &mdash; le calendrier de prise de rendez-vous de la page contact, et uniquement si vous choisissez de l’ouvrir.',
    '<b>Attach drawings or a specification</b> <span>Choose files, or drag them here. PDF, DWG, STEP, images or ZIP, up to 10 MB each.</span>':
        '<b>Joignez vos plans ou votre cahier des charges</b> <span>Choisissez des fichiers ou déposez-les ici. PDF, DWG, STEP, images ou ZIP, 10 Mo maximum chacun.</span>',
    '<b>Attach your CV and certificates</b> <span>Choose files, or drag them here. PDF, JPG or PNG, up to 10 MB each.</span>':
        '<b>Joignez votre CV et vos certificats</b> <span>Choisissez des fichiers ou déposez-les ici. PDF, JPG ou PNG, 10 Mo maximum chacun.</span>',
    '<span class="sector-name">INDUSTRIAL</span> <span class="sector-fact">Plant installation and transformer packages</span>':
        '<span class="sector-name">INDUSTRIE</span> <span class="sector-fact">Installation d’unités et ensembles transformateurs</span>',
    '<span class="sector-name">OFFSHORE</span> <span class="sector-fact">Rope access, NDT and mechanical works offshore</span>':
        '<span class="sector-name">OFFSHORE</span> <span class="sector-fact">Travaux sur cordes, CND et travaux mécaniques en mer</span>',
    '<strong>Legitimate interest</strong> (Art. 6(1)(f)) — responding to enquiries, and keeping the site secure and available.':
        '<strong>Intérêt légitime</strong> (art. 6, §1, f) — répondre aux demandes et maintenir le site sûr et disponible.',
    'Mobilised as complete crews with supervision, certification records and QA documentation in place before the first shift.':
        'Mobilisés en équipes complètes, avec encadrement, dossiers de certification et documentation qualité en place avant le premier poste.',
    '<span class="sector-name">RENEWABLES</span> <span class="sector-fact">Cable works and turbine support on wind farms</span>':
        '<span class="sector-name">RENOUVELABLES</span> <span class="sector-fact">Travaux de câblage et assistance aux éoliennes</span>',
    '<span>Offshore Oil &amp; Gas</span><span>Wind Energy</span><span>Industrial Facilities</span><span>Steel Structures</span>':
        '<span>Pétrole &amp; gaz offshore</span><span>Éolien</span><span>Installations industrielles</span><span>Structures métalliques</span>',
    'Certified to deliver safety, quality and compliance &mdash; <span class="certs-body">independently certified by DNV</span>':
        'Certifiés pour garantir sécurité, qualité et conformité &mdash; <span class="certs-body">certification indépendante DNV</span>',
    'Send the drawings or the scope and we will come back with a price and crew dates. If it is a shutdown, tell us the window.':
        'Envoyez les plans ou le périmètre et nous reviendrons avec un prix et des dates d’équipe. S’il s’agit d’un arrêt, précisez-nous la fenêtre.',
    'The calendar is hosted by Calendly. It loads only when you press the button, so nothing reaches them before you ask for it.':
        'Le calendrier est hébergé par Calendly. Il ne se charge qu’au clic sur le bouton : rien ne leur est transmis avant votre demande.',
    'Work in progress, completed scopes, and what we are learning across shipbuilding, offshore, industrial and energy projects.':
        'Chantiers en cours, périmètres livrés et ce que nous apprenons en construction navale, offshore, industrie et énergie.',
    'Cable installation, rigging and offshore support on wind farms, plus the fuel handling infrastructure that sits behind them.':
        'Pose de câbles, levage et assistance offshore sur les parcs éoliens, ainsi que les infrastructures de manutention de carburant qui les accompagnent.',
    'ALPROJECTS Group is a European provider of industrial services for the shipbuilding, offshore, industrial and energy sectors.':
        'ALPROJECTS Group est un prestataire européen de services industriels pour la construction navale, l’offshore, l’industrie et l’énergie.',
    'ALPROJECTS Group serves the shipbuilding, offshore, industrial and energy sectors, from a head office in Klaipėda, Lithuania.':
        'ALPROJECTS Group intervient dans la construction navale, l’offshore, l’industrie et l’énergie, depuis son siège de Klaipėda, en Lituanie.',
    'Attach your CV and certificates to the email that opens when you submit &mdash; we do not accept file uploads through this page.':
        'Joignez votre CV et vos certificats à l’e-mail qui s’ouvre lors de l’envoi &mdash; cette page n’accepte pas le dépôt de fichiers.',
    '<span class="sector-name">SHIPBUILDING</span> <span class="sector-fact">Engine room piping, structural steel and outfitting</span>':
        '<span class="sector-name">CONSTRUCTION NAVALE</span> <span class="sector-fact">Tuyauterie de salle des machines, charpente et armement</span>',
    'Lithuania &middot; Belgium &middot; Norway &mdash; serving offshore, shipbuilding and industry across Northern and Western Europe.':
        'Lituanie &middot; Belgique &middot; Norvège &mdash; au service de l’offshore, de la construction navale et de l’industrie en Europe du Nord et de l’Ouest.',
    '<span class="value" data-count="90" data-suffix="+">0+</span> <span class="label">Projects delivered across multiple countries</span>':
        '<span class="value" data-count="90" data-suffix="+">0+</span> <span class="label">Projets livrés dans plusieurs pays</span>',
    '<span class="value" data-count="98" data-suffix="%">0%</span> <span class="label">Early risk detection by certified specialists</span>':
        '<span class="value" data-count="98" data-suffix="%">0%</span> <span class="label">Détection précoce des risques par des spécialistes certifiés</span>',
    'ALPROJECTS, UAB (&ldquo;ALPROJECTS Group&rdquo;, &ldquo;we&rdquo;) is the controller of personal data collected through alprojects.co.':
        'ALPROJECTS, UAB (&ldquo;ALPROJECTS Group&rdquo;, &ldquo;nous&rdquo;) est le responsable du traitement des données personnelles collectées via alprojects.co.',
    'Plant installation, process piping and mechanical packages, delivered as a whole scope with our own supervisors and our own QA on site.':
        'Installation d’unités, tuyauterie process et ensembles mécaniques, livrés en périmètre complet avec nos propres encadrants et notre propre qualité sur site.',
    'Recruiting thirty certified TIG welders for a single scope of work turned out to be materially harder than the engineering it supported.':
        'Recruter trente soudeurs TIG certifiés pour un seul lot de travaux s’est révélé nettement plus difficile que l’ingénierie qu’il servait.',
    'That matters more than a logo on a wall. It is the difference between a contractor who can carry a scope to completion and one who cannot.':
        'Cela compte davantage qu’un logo au mur. C’est la différence entre une entreprise capable de mener un périmètre à son terme et une autre qui ne le peut pas.',
    '<span class="value" data-count="40" data-suffix="%">0%</span> <span class="label">Reduced inspection time through optimized workflows</span>':
        '<span class="value" data-count="40" data-suffix="%">0%</span> <span class="label">Temps d’inspection réduit grâce à des processus optimisés</span>',
    'Job applications, including any CV and certificates, are kept for 24 months from the date you send them, or until you ask us to delete them.':
        'Les candidatures, y compris les CV et certificats, sont conservées 24 mois à compter de leur envoi, ou jusqu’à votre demande de suppression.',
    'Old drawings lie. We measure what is really there and hand the data to your engineers, so the clash shows up on a screen instead of on site.':
        'Les vieux plans mentent. Nous mesurons ce qui existe réellement et remettons les données à vos ingénieurs : la collision apparaît à l’écran plutôt que sur le chantier.',
    '<span class="value" data-count="1200" data-suffix="+">0+</span> <span class="label">Safe execution in complex and confined environments</span>':
        '<span class="value" data-count="1200" data-suffix="+">0+</span> <span class="label">Exécution sûre en milieu complexe et confiné</span>',
    'Delivered projects with photography from site — shipyards, offshore structures, industrial plants and energy terminals across Northern Europe.':
        'Projets réalisés, en images depuis le chantier — chantiers navals, structures offshore, sites industriels et terminaux énergétiques en Europe du Nord.',
    'Yard schedules do not move. Our crews slot into them and take engine room piping, structural steel and outfitting, on newbuilds and on repair.':
        'Les plannings de chantier naval ne bougent pas. Nos équipes s’y insèrent et prennent la tuyauterie de salle des machines, la charpente et l’armement, en construction neuve comme en réparation.',
    'Project enquiries, personnel requests and open applications all reach the same inbox — it is read by people who can answer technical questions.':
        'Demandes de projet, besoins en personnel et candidatures spontanées arrivent dans la même boîte — lue par des personnes capables de répondre aux questions techniques.',
    'The scope ran from September 2025 to April 2026 and was delivered by a team of twelve specialists, accumulating more than 11,000 hours on site.':
        'Le chantier s’est déroulé de septembre 2025 à avril 2026 et a été réalisé par une équipe de douze spécialistes, totalisant plus de 11 000 heures sur site.',
    '<span class="fp-idx">06</span> <span class="fp-name">Belgium</span> <span class="fp-badge">1 location</span> <span class="fp-city">Antwerp</span>':
        '<span class="fp-idx">06</span> <span class="fp-name">Belgique</span> <span class="fp-badge">1 site</span> <span class="fp-city">Anvers</span>',
    'The order of work stays the same on every job. Most of the time in a machinery space goes on getting the routing right, not on the welding itself.':
        'L’ordre des opérations reste le même sur chaque chantier. En salle des machines, l’essentiel du temps passe dans le cheminement, pas dans le soudage lui-même.',
    'Work with ALPROJECTS Group — welding, pipe fitting, NDT, rope access and mechanical contracting on industrial and offshore projects across Europe.':
        'Rejoignez ALPROJECTS Group — soudage, tuyauterie, CND, travaux sur cordes et montage mécanique sur des projets industriels et offshore partout en Europe.',
    'Welding, pipe fitting, mechanical contracting, marine works, NDT, rope access and quality control for industrial and offshore projects across Europe.':
        'Soudage, tuyauterie, montage mécanique, travaux navals, CND, travaux sur cordes et contrôle qualité pour des projets industriels et offshore partout en Europe.',
    '<span class="fp-idx">05</span> <span class="fp-name">Lithuania</span> <span class="fp-badge">Headquarters</span> <span class="fp-city">Klaipėda</span>':
        '<span class="fp-idx">05</span> <span class="fp-name">Lituanie</span> <span class="fp-badge">Siège</span> <span class="fp-city">Klaipėda</span>',
    'Mobilising a team offshore is expensive and a shutdown is more expensive still. Rope access and NDT carry most of this work, with mechanical scopes al':
        'Mobiliser une équipe en offshore coûte cher et un arrêt coûte plus cher encore. Les travaux sur cordes et les CND portent l’essentiel de ces prestations, avec des lots mécaniques en',
    '<span class="fp-idx">03</span> <span class="fp-name">Netherlands</span> <span class="fp-badge">1 location</span> <span class="fp-city">Rotterdam</span>':
        '<span class="fp-idx">03</span> <span class="fp-name">Pays-Bas</span> <span class="fp-badge">1 site</span> <span class="fp-city">Rotterdam</span>',
    "Repair work is decided in days, not months. We take steel renewal, piping replacement and mechanical repairs, to class and to the owner's requirements.":
        'Une réparation se décide en jours, pas en mois. Nous prenons en charge le renouvellement de tôles, le remplacement de tuyauteries et les réparations mécaniques, aux exigences de la société de classification et de l’armateur.',
    'Scaffolding costs more in downtime than in steel. Certified technicians reach the same place on rope, inspect it and repair it while the plant keeps...':
        'L’échafaudage coûte plus cher en immobilisation qu’en acier. Des techniciens certifiés atteignent le même point sur corde, l’inspectent et le réparent pendant que l’usine continue...',
    'A weld is only as good as the paperwork behind it. We weld structural steel and piping systems in TIG, MIG and semi-automatic processes, under an ISO...':
        'Une soudure ne vaut que par le dossier qui l’accompagne. Nous soudons charpente métallique et réseaux de tuyauterie en TIG, MIG et procédés semi-automatiques, sous un système ISO...',
    'Nobody should be signing off their own work. We inspect welds, materials and structures without stopping production, and we report to the client, not...':
        'Personne ne devrait valider son propre travail. Nous contrôlons soudures, matériaux et structures sans arrêter la production, et nous rendons compte au client, pas...',
    'Some clients need the whole scope taken off their hands. We install plant and equipment, fabricate steel and build transformer packages, with our own...':
        'Certains clients veulent confier le périmètre entier. Nous installons unités et équipements, fabriquons la charpente et montons les ensembles transformateurs, avec nos propres...',
    '<strong>Newsletter.</strong> If you submit the newsletter form, we receive the email address you enter, in order to send you company and project updates.':
        '<strong>Newsletter.</strong> Si vous envoyez le formulaire d’abonnement, nous recevons l’adresse e-mail que vous saisissez, afin de vous adresser nos actualités et l’avancement de nos projets.',
    'Most delays in piping start with a bad fit-up. We supply fitters for process, utility and engine room systems, instrument fitters for small bore work,...':
        'La plupart des retards en tuyauterie commencent par un mauvais accostage. Nous fournissons des tuyauteurs pour les circuits process, utilités et salle des machines, des tuyauteurs instrumentation pour le petit diamètre,...',
    'Outline map of Europe marking the six countries ALPROJECTS Group operates in: Norway, the United Kingdom, the Netherlands, Belgium, Germany and Lithuania':
        'Carte de l’Europe indiquant les six pays où opère ALPROJECTS Group : Norvège, Royaume-Uni, Pays-Bas, Belgique, Allemagne et Lituanie',
    '<span class="fp-idx">02</span> <span class="fp-name">United Kingdom</span> <span class="fp-badge">1 location</span> <span class="fp-city">Newcastle</span>':
        '<span class="fp-idx">02</span> <span class="fp-name">Royaume-Uni</span> <span class="fp-badge">1 site</span> <span class="fp-city">Newcastle</span>',
    'Every hour a unit stays down has a price. Our crews mobilise at short notice for turnarounds, shutdowns and breakdowns, and they carry welding, fitting...':
        'Chaque heure d’arrêt d’une unité a un coût. Nos équipes se mobilisent à court préavis pour les grands arrêts, les arrêts de tranche et les dépannages, et réunissent soudage, montage...',
    'Moving a production line is a scheduling problem before it is a lifting problem. We dismantle, move, re-install and align it, inside a running plant or...':
        'Déplacer une ligne de production est d’abord un problème de planning, pas de levage. Nous la démontons, la déplaçons, la réinstallons et l’alignons, dans une usine en marche ou...',
    'Quality is what you can prove afterwards. We inspect piping and steel structures and leave documentation that holds up when the client, the surveyor or...':
        'La qualité, c’est ce que l’on peut prouver après coup. Nous contrôlons tuyauteries et structures métalliques et laissons une documentation qui tient quand le client, l’expert ou...',
    'Who we are, where we operate, the sectors we serve and the standards we are certified to. Includes our footprint across six countries and selected clients.':
        'Qui nous sommes, où nous opérons, les secteurs que nous servons et les normes qui nous certifient. Avec notre implantation dans six pays et une sélection de clients.',
    '<span class="fp-idx">01</span> <span class="fp-name">Norway</span> <span class="fp-badge">2 locations</span> <span class="fp-city">Ålesund · Orkanger</span>':
        '<span class="fp-idx">01</span> <span class="fp-name">Norvège</span> <span class="fp-badge">2 sites</span> <span class="fp-city">Ålesund · Orkanger</span>',
    'I agree that ALPROJECTS may store these details to consider me for current and future roles, as described in the <a href="/privacy">privacy policy</a>.':
        'J’accepte qu’ALPROJECTS conserve ces informations afin d’étudier ma candidature pour les postes actuels et futurs, dans les conditions décrites dans la <a href="/privacy">politique de confidentialité</a>.',
    'Repair work is decided in days, not months. We take steel renewal, piping replacement and mechanical repairs, to class and to the owner&rsquo;s requirements.':
        'Une réparation se décide en jours, pas en mois. Nous prenons en charge le renouvellement de tôles, le remplacement de tuyauteries et les réparations mécaniques, aux exigences de la société de classification et de l’armateur.',
    'Scaffolding costs more in downtime than in steel. Certified technicians reach the same place on rope, inspect it and repair it while the plant keeps running.':
        'L’échafaudage coûte plus cher en immobilisation qu’en acier. Des techniciens certifiés atteignent le même point sur corde, l’inspectent et le réparent pendant que l’usine continue de tourner.',
    'Mobilising a team offshore is expensive and a shutdown is more expensive still. Rope access and NDT carry most of this work, with mechanical scopes alongside.':
        'Mobiliser une équipe en offshore coûte cher et un arrêt coûte plus cher encore. Les travaux sur cordes et les CND portent l’essentiel de ces prestations, avec des lots mécaniques en parallèle.',
    'ALPROJECTS Group delivers mechanical contracting, pipe fitting, welding, QAQC, rope access and NDT services for industrial and offshore projects across Europe.':
        'ALPROJECTS Group réalise des prestations de montage mécanique, de tuyauterie, de soudage, de QA/QC, de travaux sur cordes et de CND pour des projets industriels et offshore partout en Europe.',
    '<span class="kp-num">04</span> <span class="kp-name">Hywind Tampen</span> <span class="kp-scope">Rotational team support for offshore pull-in operations.</span>':
        '<span class="kp-num">04</span> <span class="kp-name">Hywind Tampen</span> <span class="kp-scope">Équipes en rotation en appui des opérations de tirage offshore.</span>',
    'Four project types, one set of disciplines. The engineering is largely the same; the environment, the standards and the consequences of getting it wrong are not.':
        'Quatre types de projets, un même socle de métiers. L’ingénierie est en grande partie la même ; l’environnement, les normes et les conséquences d’une erreur ne le sont pas.',
    'We are recruiting thirty certified TIG welders for upcoming project scopes. This is the constraint on our current pipeline, so applications are reviewed quickly.':
        'Nous recrutons trente soudeurs TIG certifiés pour des périmètres de projet à venir. C’est le facteur limitant de notre carnet de commandes actuel : les candidatures sont donc traitées rapidement.',
    'Welding is carried out under <strong>ISO 3834</strong>. Every joint is documented, and NDT and pressure testing are done before insulation and final coating go on.':
        'Le soudage est réalisé sous <strong>ISO 3834</strong>. Chaque assemblage est documenté ; les CND et les épreuves de pression sont effectués avant la pose du calorifuge et du revêtement final.',
    '<span class="kp-num">03</span> <span class="kp-name">Ostwind Offshore Wind Farm</span> <span class="kp-scope">Cable jointers, cable mates and rigging support.</span>':
        '<span class="kp-num">03</span> <span class="kp-name">Parc éolien offshore Ostwind</span> <span class="kp-scope">Jointeurs de câbles, aides-câbliers et appui levage.</span>',
    'Consistency across borders is a documentation problem as much as a fabrication one — which is where certified personnel and a single quality system earn their place.':
        'La constance d’un pays à l’autre relève autant de la documentation que de la fabrication — c’est là que du personnel certifié et un système qualité unique prennent tout leur sens.',
    'We perform NDT inspections of welds, materials and structures without interrupting operations. Defects are identified at early stages to ensure safety and compliance.':
        'Nous réalisons des contrôles non destructifs sur les soudures, les matériaux et les structures sans interrompre l’exploitation. Les défauts sont détectés au plus tôt, pour garantir la sécurité et la conformité.',
    '<span>© 2019–2026 ALPROJECTS GROUP. All rights reserved.</span> <a class="made-by" href="https://aldystudio.com" target="_blank" rel="noopener">Made by <b>ALDY</b></a>':
        '<span>© 2019–2026 ALPROJECTS GROUP. Tous droits réservés.</span> <a class="made-by" href="https://aldystudio.com" target="_blank" rel="noopener">Réalisé par <b>ALDY</b></a>',
    '<span class="fp-idx">04</span> <span class="fp-name">Germany</span> <span class="fp-badge">3 locations</span> <span class="fp-city">Rostock · Hamburg · Frankfurt</span>':
        '<span class="fp-idx">04</span> <span class="fp-name">Allemagne</span> <span class="fp-badge">3 sites</span> <span class="fp-city">Rostock · Hambourg · Francfort</span>',
    '<strong>Direct contact.</strong> If you email or call us, we receive whatever you choose to send — typically your name, contact details and the content of your enquiry.':
        '<strong>Contact direct.</strong> Si vous nous écrivez ou nous appelez, nous recevons ce que vous choisissez de transmettre — généralement votre nom, vos coordonnées et le contenu de votre demande.',
    'Even when a role is not advertised, we keep qualified specialists on file and make contact when a project matches. These are the areas our project teams are built from:':
        'Même en l’absence d’annonce, nous conservons les profils qualifiés et reprenons contact dès qu’un projet correspond. Voici les métiers qui composent nos équipes :',
    'Some clients need the whole scope taken off their hands. We install plant and equipment, fabricate steel and build transformer packages, with our own supervisors on site.':
        'Certains clients veulent confier le périmètre entier. Nous installons unités et équipements, fabriquons la charpente et montons les ensembles transformateurs, avec nos propres encadrants sur site.',
    '<span class="kp-num">02</span> <span class="kp-name">Thor Offshore Wind Farm</span> <span class="kp-scope">Cable installation, rigging and offshore support services.</span>':
        '<span class="kp-num">02</span> <span class="kp-name">Parc éolien offshore Thor</span> <span class="kp-scope">Pose de câbles, levage et services d’assistance offshore.</span>',
    'Moving a production line is a scheduling problem before it is a lifting problem. We dismantle, move, re-install and align it, inside a running plant or between two countries.':
        'Déplacer une ligne de production est d’abord un problème de planning, pas de levage. Nous la démontons, la déplaçons, la réinstallons et l’alignons, dans une usine en marche ou entre deux pays.',
    'Quality is what you can prove afterwards. We inspect piping and steel structures and leave documentation that holds up when the client, the surveyor or the auditor asks for it.':
        'La qualité, c’est ce que l’on peut prouver après coup. Nous contrôlons tuyauteries et structures métalliques et laissons une documentation qui tient quand le client, l’expert ou l’auditeur la demande.',
    '<strong>Welded, tested, then closed.</strong> Welding under ISO 3834. Every joint is documented, and NDT and pressure testing are done before insulation and final coating go on.':
        '<strong>Soudé, éprouvé, puis fermé.</strong> Soudage sous ISO 3834. Chaque assemblage est documenté ; les CND et les épreuves de pression sont réalisés avant la pose du calorifuge et du revêtement final.',
    'Even when a role is not advertised we keep qualified specialists on file and make contact when a project matches. Select your discipline and it goes straight into the form below.':
        'Même en l’absence d’annonce, nous conservons les profils qualifiés et reprenons contact dès qu’un projet correspond. Sélectionnez votre métier : il est repris directement dans le formulaire ci-dessous.',
    'We deliver mechanical contracting, welding, inspection and access services on industrial and offshore projects across Europe. The work is technical, certified and mostly on site.':
        'Nous réalisons des travaux de montage mécanique, de soudage, d’inspection et d’accès sur des projets industriels et offshore partout en Europe. Un travail technique, certifié et majoritairement sur chantier.',
    '<strong>Server logs.</strong> The site is hosted on GitHub Pages. GitHub records technical request data, including IP address and browser user-agent, for security and reliability.':
        '<strong>Journaux serveur.</strong> Le site est hébergé sur GitHub Pages. GitHub enregistre des données techniques de requête, dont l’adresse IP et l’agent utilisateur du navigateur, à des fins de sécurité et de fiabilité.',
    'Numbers like 11,000 hours are worth stating plainly: they are what a project of this size actually costs in skilled labour, and planning against a lower figure is how schedules fail.':
        'Un chiffre comme 11 000 heures mérite d’être donné tel quel : c’est ce qu’un chantier de cette taille coûte réellement en main-d’œuvre qualifiée, et planifier sur une base plus basse est la manière dont les plannings dérapent.',
    'ALPROJECTS, UAB<br>Šilutės pl. 2, LT-92298 Klaipėda, Lithuania<br> <a href="mailto:info@alprojects.eu">info@alprojects.eu</a> &middot; <a href="tel:+37063663744">+370 636 63 744</a>':
        'ALPROJECTS, UAB<br>Šilutės pl. 2, LT-92298 Klaipėda, Lituanie<br> <a href="mailto:info@alprojects.eu">info@alprojects.eu</a> &middot; <a href="tel:+37063663744">+370 636 63 744</a>',
    'It is worth being direct about this, because the answer is not a recruitment campaign. It is training, certification pathways, and treating the trades as a career rather than a stopgap.':
        'Autant le dire franchement : la réponse n’est pas une campagne de recrutement. Ce sont la formation, les parcours de certification, et le fait de traiter ces métiers comme une carrière et non comme un pis-aller.',
    'Scope on all three: inspection and industrial maintenance services for onshore and offshore installations. Issued by DNV Business Assurance Finland. Select a certificate to open the PDF.':
        'Périmètre commun aux trois : services d’inspection et de maintenance industrielle pour installations terrestres et offshore. Délivrés par DNV Business Assurance Finland. Sélectionnez un certificat pour ouvrir le PDF.',
    '<strong>Consent</strong> (GDPR Art. 6(1)(a)) — newsletter subscription, and loading the scheduling calendar, which happens only when you press the button. You may withdraw it at any time.':
        '<strong>Consentement</strong> (RGPD, art. 6, §1, a) — abonnement à la newsletter et chargement du calendrier de rendez-vous, qui n’intervient qu’après un clic sur le bouton. Vous pouvez le retirer à tout moment.',
    'Head office in Klaipėda, Lithuania, with operations in <strong>Belgium</strong> and <strong>Norway</strong>, serving offshore, shipbuilding and industry across Northern and Western Europe.':
        'Siège à Klaipėda, en Lituanie, avec des opérations en <strong>Belgique</strong> et en <strong>Norvège</strong>, au service de l’offshore, de la construction navale et de l’industrie en Europe du Nord et de l’Ouest.',
    'Nobody should be signing off their own work. We inspect welds, materials and structures without stopping production, and we report to the client, not to the contractor who did the welding.':
        'Personne ne devrait valider son propre travail. Nous contrôlons soudures, matériaux et structures sans arrêter la production, et nous rendons compte au client, pas à l’entreprise qui a soudé.',
    '<span class="kp-num">01</span> <span class="kp-name">SylWin Alpha Converter Platform</span> <span class="kp-scope">Offshore bridge repairs, steel fitting and structural welding works.</span>':
        '<span class="kp-num">01</span> <span class="kp-name">Plateforme de conversion SylWin Alpha</span> <span class="kp-scope">Réparation de passerelles offshore, montage métallique et soudage structurel.</span>',
    'Every hour a unit stays down has a price. Our crews mobilise at short notice for turnarounds, shutdowns and breakdowns, and they carry welding, fitting and mechanical skills in the same team.':
        'Chaque heure d’arrêt d’une unité a un coût. Nos équipes se mobilisent à court préavis pour les grands arrêts, les arrêts de tranche et les dépannages, et réunissent soudage, montage et mécanique dans la même équipe.',
    'Our own technicians come in before that. They go over the joint while the crew is still on the job, and if something has to come out, it comes out before anyone else is invited to look at it.':
        'Nos propres techniciens interviennent en amont. Ils reprennent l’assemblage pendant que l’équipe est encore sur place, et si quelque chose doit être repris, cela l’est avant que quiconque d’autre ne soit invité à regarder.',
    'Our crew is installing engine room systems on vessels under construction: seawater, bilge, ballast, fuel and service lines running from small bore up to DN200 around the main engine foundations.':
        'Notre équipe monte les circuits de salle des machines sur des navires en construction : eau de mer, cale, ballast, combustible et servitudes, du petit diamètre jusqu’au DN200, autour des berceaux du moteur principal.',
    '<strong>Manifolds, sea chests, tank connections.</strong> Gate valves, strainers and remote operated units set out and aligned on the tank top. Flange faces stay capped until the system is closed.':
        '<strong>Collecteurs, prises d’eau de mer, piquages sur capacités.</strong> Vannes à opercule, crépines et organes télécommandés implantés et alignés sur le plafond de ballast. Les portées de brides restent obturées jusqu’à la fermeture du circuit.',
    'The certificate recognises companies with a high credit score and a proven record of financial stability. It is issued by Creditinfo Group and was awarded on 23 June 2026 for the 2025–2026 period.':
        'Le certificat distingue les entreprises présentant une notation de crédit élevée et une stabilité financière avérée. Il est délivré par Creditinfo Group et a été décerné le 23 juin 2026 pour la période 2025–2026.',
    '<strong>Drawn first, then built.</strong> Isometrics are checked before anything is cut. Spools are prefabricated in the shop, fitted on board and hung so the line can move without loading the welds.':
        '<strong>Dessiné d’abord, construit ensuite.</strong> Les isométriques sont vérifiés avant toute coupe. Les tronçons sont préfabriqués en atelier, ajustés à bord et supportés de sorte que la ligne puisse se dilater sans solliciter les soudures.',
    'If you believe we have handled your data improperly, you may lodge a complaint with the Lithuanian State Data Protection Inspectorate (Valstybine duomenu apsaugos inspekcija), L. Sapiegos g. 17, Vilnius.':
        'Si vous estimez que nous avons traité vos données de manière incorrecte, vous pouvez introduire une réclamation auprès de l’Inspection nationale lituanienne de la protection des données (Valstybine duomenu apsaugos inspekcija), L. Sapiegos g. 17, Vilnius.',
    'You can also send them to <a href="mailto:info@alprojects.eu?subject=CV%20and%20certificates">info@alprojects.eu</a> or by <a href="https://wa.me/37063663744" target="_blank" rel="noopener">WhatsApp</a>.':
        'Vous pouvez aussi les envoyer à <a href="mailto:info@alprojects.eu?subject=CV%20and%20certificates">info@alprojects.eu</a> ou par <a href="https://wa.me/37063663744" target="_blank" rel="noopener">WhatsApp</a>.',
    '<strong>Consent</strong> (GDPR Art. 6(1)(a)) — newsletter subscription, job applications, and loading the scheduling calendar, which happens only when you press the button. You may withdraw it at any time.':
        '<strong>Consentement</strong> (RGPD, art. 6, §1, a) — abonnement à la newsletter, candidatures et chargement du calendrier de rendez-vous, qui n’intervient qu’après un clic sur le bouton. Vous pouvez le retirer à tout moment.',
    'A transformer mechanical package covers the stainless steel piping and cooling systems that keep the unit within its operating envelope. The tolerances are tight and the commissioning window is usually short.':
        'Un ensemble mécanique de transformateur regroupe la tuyauterie inox et les circuits de refroidissement qui maintiennent l’appareil dans son domaine de fonctionnement. Les tolérances sont serrées et la fenêtre de mise en service généralement courte.',
    'What made this scope demanding was not any single site but the repetition: the same package delivered across five European countries, each with its own site conditions, inspection regime and local requirements.':
        'La difficulté de ce chantier ne tenait pas à un site en particulier mais à la répétition : le même ensemble livré dans cinq pays européens, chacun avec ses conditions de site, son régime d’inspection et ses exigences locales.',
    'CVs and certificate documents are stored with the application and are seen only by the people resourcing projects. We do not pass them to third parties, and we do not use them for anything other than recruitment.':
        'Les CV et les certificats sont conservés avec la candidature et ne sont consultés que par les personnes chargées de doter les projets. Nous ne les transmettons à aucun tiers et ne les utilisons à aucune autre fin que le recrutement.',
    'UAB &ldquo;ALprojects&rdquo; holds the <strong>Strongest in Lithuania</strong> certificate, awarded by Creditinfo Group on 23 June 2026 to companies with a high credit score and a proven record of financial stability.':
        'UAB &ldquo;ALprojects&rdquo; est titulaire du certificat <strong>Strongest in Lithuania</strong>, décerné par Creditinfo Group le 23 juin 2026 aux entreprises présentant une notation de crédit élevée et une stabilité financière avérée.',
    '<strong>Booking a call.</strong> If you open the scheduling calendar on the contacts page and book a slot, Calendly receives the name, email address and any notes you enter, together with your IP address and time zone.':
        '<strong>Prise de rendez-vous.</strong> Si vous ouvrez le calendrier de la page contact et réservez un créneau, Calendly reçoit le nom, l’adresse e-mail et les éventuelles remarques que vous saisissez, ainsi que votre adresse IP et votre fuseau horaire.',
    'Fuel handling infrastructure concentrates every discipline we work in — mechanical installation, pipe fitting, welding, and the inspection and documentation that has to accompany all three when the medium is flammable.':
        'Les infrastructures de manutention de carburant concentrent tous nos métiers — montage mécanique, tuyauterie, soudage, et l’inspection et la documentation qui doivent accompagner les trois dès lors que le fluide est inflammable.',
    'Execution quality control for piping and steel structures. Inspection and verification in accordance with WPS, drawings and applicable standards. Traceability, documentation and control maintained throughout all stages.':
        'Contrôle qualité d’exécution pour la tuyauterie et les structures métalliques. Inspection et vérification conformément au DMOS, aux plans et aux normes applicables. Traçabilité, documentation et contrôle maintenus à toutes les étapes.',
    '<strong>Measured against the criteria.</strong> Cap height, width, undercut, profile. Each one is checked against the acceptance criteria for the job, and the joint is not presented until the numbers sit inside the limits.':
        '<strong>Mesuré au regard des critères.</strong> Surépaisseur, largeur, caniveau, profil. Chaque valeur est confrontée aux critères d’acceptation du chantier, et l’assemblage n’est pas présenté tant que les mesures ne sont pas dans les limites.',
    '<strong>A stable partner is a safer project.</strong> In heavy industry, projects run for months and commitments run for years. Independent proof of financial stability is proof that we will be there to see the work through.':
        '<strong>Un partenaire solide, c’est un projet plus sûr.</strong> Dans l’industrie lourde, les projets durent des mois et les engagements des années. Une preuve indépendante de solidité financière est la preuve que nous serons là jusqu’au bout.',
    'Simply browsing this site loads no third-party scripts, fonts, analytics or embeds. The typeface is served from our own domain, so reading these pages does not disclose your IP address to any advertising or analytics company.':
        'La simple consultation de ce site ne charge aucun script, police, outil de mesure ou contenu embarqué de tiers. La typographie est servie depuis notre propre domaine : lire ces pages ne communique donc votre adresse IP à aucune régie publicitaire ni société de mesure d’audience.',
    "So there are two different things with the same equipment behind them. On our own jobs it is internal quality control, and it never counts as sign-off. On somebody else's welds it is independent NDT, because we did not weld it.":
        'Il s’agit donc de deux choses différentes derrière le même matériel. Sur nos propres chantiers, c’est du contrôle qualité interne, et cela ne vaut jamais validation. Sur les soudures d’un tiers, c’est du CND indépendant, parce que nous ne les avons pas soudées.',
    'I agree that ALPROJECTS, UAB stores my details and documents for recruitment purposes for 24 months. I can ask for them to be deleted at any time by writing to info@alprojects.eu. See the <a href="/privacy">privacy policy</a>.':
        'J’accepte qu’ALPROJECTS, UAB conserve mes informations et mes documents à des fins de recrutement pendant 24 mois. Je peux en demander la suppression à tout moment en écrivant à info@alprojects.eu. Voir la <a href="/privacy">politique de confidentialité</a>.',
    '<strong>Where the line sits.</strong> Nobody should be signing off their own work, and we do not try to. Independent verification stays where the contract puts it, normally with the client or the class surveyor, and nothing we do changes that.':
        '<strong>Où passe la limite.</strong> Personne ne devrait valider son propre travail, et nous ne cherchons pas à le faire. La vérification indépendante reste là où le contrat la place, généralement chez le client ou l’expert de la société de classification, et rien de ce que nous faisons ne change cela.',
    'The shortage is discussed across European industry in general terms. It becomes concrete when a project is resourced, scheduled and funded, and the constraint is simply the number of people who hold the certification and are willing to travel.':
        'On parle de cette pénurie dans toute l’industrie européenne, en termes généraux. Elle devient concrète quand un projet est doté, planifié et financé, et que la seule contrainte est le nombre de personnes qui détiennent la certification et acceptent de se déplacer.',
    '<strong>Job applications.</strong> If you send the careers form we receive the details you enter &mdash; name, contact details, discipline, certificates, availability and any notes &mdash; together with any CV or certificate documents you attach.':
        '<strong>Candidatures.</strong> Si vous envoyez le formulaire de candidature, nous recevons les informations saisies &mdash; nom, coordonnées, métier, certifications, disponibilité et remarques &mdash; ainsi que les CV et certificats que vous joignez.',
    '<strong>What the eye cannot pick up.</strong> Clean the weld, apply the penetrant, let the developer draw it back out. Surface cracks and porosity that nobody would catch by eye show up in red, and anything outside the limits is repaired on the spot.':
        '<strong>Ce que l’œil ne voit pas.</strong> Nettoyer la soudure, appliquer le pénétrant, laisser le révélateur le faire ressortir. Les fissures de surface et les porosités que personne ne repérerait à l’œil apparaissent en rouge, et tout ce qui sort des limites est repris sur place.',
    'The company employs between 51 and 200 people directly and draws on a roster of more than 300 certified specialists across Europe. Projects are resourced from that roster rather than subcontracted on, which is what keeps the quality system meaningful.':
        'L’entreprise emploie directement entre 51 et 200 personnes et s’appuie sur un vivier de plus de 300 spécialistes certifiés en Europe. Les projets sont dotés à partir de ce vivier plutôt que sous-traités : c’est ce qui donne sa portée réelle au système qualité.',
    'Execution of 3D laser scanning to capture precise as-built geometry of structures and piping systems. Point cloud data supports dimensional control, clash detection and retrofit engineering. Improves accuracy and reduces rework during installation and fabrication.':
        'Relevés par scan laser 3D pour saisir la géométrie exacte des structures et réseaux de tuyauterie existants. Le nuage de points alimente le contrôle dimensionnel, la détection de collisions et les études de rénovation. Il améliore la précision et réduit les reprises en fabrication comme au montage.',
    'A weld is only as good as the paperwork behind it. We weld structural steel and piping systems in TIG, MIG and semi-automatic processes, under an ISO 3834 quality system. The welders hold current qualifications and the procedure is approved before the first arc is struck.':
        'Une soudure ne vaut que par le dossier qui l’accompagne. Nous soudons charpente métallique et réseaux de tuyauterie en TIG, MIG et procédés semi-automatiques, sous système qualité ISO 3834. Les soudeurs disposent de qualifications en cours de validité et le mode opératoire est approuvé avant le premier amorçage.',
    'Newsletter addresses are kept until you unsubscribe or ask us to remove them. Business correspondence is kept as long as needed for the enquiry or project and any statutory retention period that applies to it. Hosting logs are retained according to GitHub&rsquo;s own schedule.':
        'Les adresses de la newsletter sont conservées jusqu’à votre désabonnement ou votre demande de suppression. La correspondance commerciale est conservée le temps nécessaire à la demande ou au projet, ainsi que pendant toute durée légale de conservation applicable. Les journaux d’hébergement sont conservés selon le calendrier propre à GitHub.',
    'Most delays in piping start with a bad fit-up. We supply fitters for process, utility and engine room systems, instrument fitters for small bore work, and workshop crews who build spools straight from the isometrics. The dimensions are checked before the welder arrives, not after.':
        'La plupart des retards en tuyauterie commencent par un mauvais accostage. Nous fournissons des tuyauteurs pour les circuits process, utilités et salle des machines, des tuyauteurs instrumentation pour le petit diamètre, et des équipes d’atelier qui fabriquent les tronçons directement d’après les isométriques. Les cotes sont vérifiées avant l’arrivée du soudeur, pas après.',
    'Under the GDPR you may request access to your data, correction, erasure, restriction of processing, portability, and you may object to processing based on legitimate interest. Write to <a href="mailto:info@alprojects.eu">info@alprojects.eu</a> and we will respond within one month.':
        'En vertu du RGPD, vous pouvez demander l’accès à vos données, leur rectification, leur effacement, la limitation du traitement, leur portabilité, et vous opposer à un traitement fondé sur l’intérêt légitime. Écrivez à <a href="mailto:info@alprojects.eu">info@alprojects.eu</a> et nous répondrons sous un mois.',
    'Headquartered in Klaipėda, Lithuania, with active project bases supporting clients in six countries. Offices in <strong>Lithuania</strong>, <strong>Poland</strong>, <strong>Germany</strong> and <strong>Norway</strong> sit close to our clients&rsquo; yards, ports and offshore terminals.':
        'Siège à Klaipėda, en Lituanie, et des bases projet actives au service de clients dans six pays. Nos bureaux en <strong>Lituanie</strong>, en <strong>Pologne</strong>, en <strong>Allemagne</strong> et en <strong>Norvège</strong> sont proches des chantiers navals, des ports et des terminaux offshore de nos clients.',
    'Send us the scope or the drawings and we will come back with a price and crew dates. The fastest route to a useful answer is the scope, the location, the standards that apply and the window you are working to. For personnel requests, tell us the disciplines, certifications and headcount.':
        'Envoyez-nous le périmètre ou les plans et nous reviendrons avec un prix et des dates d’équipe. Le chemin le plus court vers une réponse utile : le périmètre, le lieu, les normes applicables et la fenêtre d’intervention. Pour un besoin en personnel, précisez les métiers, les certifications et l’effectif.',
    'Fuel handling infrastructure and wind energy support. Our <a href="/news/fuel-loading-terminal-completed">fuel loading terminal scope</a> ran from September 2025 to April 2026 with twelve specialists and over 11,000 hours on site — a useful figure for anyone planning work of that size.':
        'Infrastructures de manutention de carburant et assistance à l’éolien. Notre <a href="/news/fuel-loading-terminal-completed">chantier de terminal de chargement</a> s’est déroulé de septembre 2025 à avril 2026 avec douze spécialistes et plus de 11 000 heures sur site — un repère utile pour qui planifie un chantier de cette taille.',
    'Execution of lifting, rigging and installation works for industrial and offshore projects. Planning, coordination and supervision of lifting operations in accordance with project requirements and site conditions. Work is performed with controlled procedures and safety compliance at all stages.':
        'Réalisation de travaux de levage, d’élingage et d’installation pour projets industriels et offshore. Planification, coordination et supervision des opérations de levage selon les exigences du projet et les conditions du site. Les travaux suivent des procédures maîtrisées et respectent la sécurité à chaque étape.',
    'Applications are held for <strong>24 months</strong> from the date you send them, so that we can contact you when a project matches your discipline. You can ask us to delete them at any time by writing to <a href="mailto:info@alprojects.eu">info@alprojects.eu</a>, and we will do so without needing a reason.':
        'Les candidatures sont conservées <strong>24 mois</strong> à compter de leur envoi, afin que nous puissions vous contacter dès qu’un projet correspond à votre métier. Vous pouvez en demander la suppression à tout moment en écrivant à <a href="mailto:info@alprojects.eu">info@alprojects.eu</a>, et nous le ferons sans avoir à en connaître le motif.',
    'Execution of installation, inspection and maintenance works at height using IRATA and SOFT certified rope access methods. Supports welding, NDT, mechanical works and structural repairs in areas where conventional access is not feasible. Work is performed in compliance with safety standards and site procedures.':
        'Réalisation de travaux d’installation, d’inspection et de maintenance en hauteur par accès sur cordes, selon les méthodes certifiées IRATA et SOFT. En appui du soudage, des CND, des travaux mécaniques et des réparations structurelles là où l’accès conventionnel est impossible. Les travaux respectent les normes de sécurité et les procédures du site.',
    'Inspection, access and mechanical works on offshore facilities, where mobilising a team is expensive and a shutdown is more expensive still. Rope access and NDT carry most of this work; visual inspection plays a central role in confirming the safety and operational integrity of oil, gas and wind energy assets.':
        'Inspection, accès et travaux mécaniques sur installations offshore, où mobiliser une équipe coûte cher et un arrêt coûte plus cher encore. Les travaux sur cordes et les CND portent l’essentiel de ces prestations ; le contrôle visuel joue un rôle central pour confirmer la sécurité et l’intégrité opérationnelle des actifs pétroliers, gaziers et éoliens.',
    'ALPROJECTS Group holds <strong>ISO 3834</strong> for welding quality requirements, alongside ISO 9001, ISO 14001 and ISO 45001 covering quality, environmental and occupational health and safety management. Certification is what allows a client to accept our documentation without re-doing the inspection themselves.':
        'ALPROJECTS Group est certifié <strong>ISO 3834</strong> pour les exigences de qualité en soudage, ainsi qu’ISO 9001, ISO 14001 et ISO 45001 pour le management de la qualité, de l’environnement et de la santé et sécurité au travail. C’est la certification qui permet à un client d’accepter notre documentation sans refaire lui-même le contrôle.',
    'Awarded to UAB &ldquo;ALprojects&rdquo; by Creditinfo Group on 23 June 2026, recognising a high credit score and a proven record of financial stability. In heavy industry, projects run for months and commitments run for years &mdash; independent proof of stability is proof we will be there to see the work through.':
        'Décerné à UAB &ldquo;ALprojects&rdquo; par Creditinfo Group le 23 juin 2026, en reconnaissance d’une notation de crédit élevée et d’une stabilité financière avérée. Dans l’industrie lourde, les projets durent des mois et les engagements des années &mdash; une preuve indépendante de solidité est la preuve que nous serons là jusqu’au bout.',
    'Piping and mechanical installation on vessels under construction — seawater, bilge and fuel systems routed through compartments that are already full of machinery, structure and other trades. Prefabrication and installation are handled together, because a spool built to drawing but not to the as-built compartment is scrap.':
        'Tuyauterie et montage mécanique sur navires en construction — circuits d’eau de mer, de cale et de combustible cheminant dans des compartiments déjà encombrés de machines, de structure et d’autres corps de métier. Préfabrication et montage sont traités ensemble, car un tronçon conforme au plan mais pas au compartiment réel part à la ferraille.',
    'We specialise in piping prefabrication and installation, steel fabrication and mechanical installation, and we provide certified technical personnel to projects across Europe. In practice that means we are engaged either to deliver a defined mechanical scope, or to supply the qualified people a project is short of &mdash; often both on the same site.':
        'Nous sommes spécialisés dans la préfabrication et le montage de tuyauterie, la fabrication métallique et le montage mécanique, et nous mettons du personnel technique certifié à disposition de projets partout en Europe. Concrètement, on nous confie soit un périmètre mécanique défini, soit les compétences qualifiées qui manquent au projet &mdash; souvent les deux sur le même site.',
    'In heavy industry, projects run for months and commitments run for years. Independent proof of financial stability is proof that we will be there to see the work through &mdash; which is a different question from whether the welding is any good, and worth answering separately. <a href="/news/strongest-in-lithuania-2025-2026">More on the award</a>.':
        'Dans l’industrie lourde, les projets durent des mois et les engagements des années. Une preuve indépendante de solidité financière est la preuve que nous serons là jusqu’au bout &mdash; question distincte de la qualité du soudage, et qui mérite d’être traitée séparément. <a href="/news/strongest-in-lithuania-2025-2026">En savoir plus sur cette distinction</a>.',
    'Plant installation, process piping and mechanical packages. A recent example is a transformer mechanical package — stainless steel piping and cooling systems &mdash; <a href="/news/transformer-mechanical-package">delivered across five European countries</a>, where consistency across borders was as much a documentation problem as a fabrication one.':
        'Installation d’unités, tuyauterie process et ensembles mécaniques. Exemple récent : un ensemble mécanique de transformateur — tuyauterie inox et circuits de refroidissement &mdash; <a href="/news/transformer-mechanical-package">livré dans cinq pays européens</a>, où la constance d’un pays à l’autre relevait autant de la documentation que de la fabrication.',
    'The one exception is the scheduling calendar on the contacts page. It is supplied by Calendly LLC and is <strong>not loaded until you press &ldquo;Open the calendar&rdquo;</strong>. Until you do, no request is made to Calendly and they receive nothing about you. Once you open it, Calendly receives your IP address and sets its own cookies in order to run the calendar, and the details you submit if you book a slot. Calendly is a US company and transfers are covered by the EU Standard Contractual Clauses; see <a href="https://calendly.com/privacy" target="_blank" rel="noopener">calendly.com/privacy</a>. You can book a call by email instead if you prefer not to use it.':
        'La seule exception est le calendrier de rendez-vous de la page contact. Il est fourni par Calendly LLC et <strong>n’est pas chargé tant que vous n’avez pas cliqué sur &ldquo;Ouvrir le calendrier&rdquo;</strong>. Jusque-là, aucune requête n’est adressée à Calendly et ils ne reçoivent rien vous concernant. Une fois ouvert, Calendly reçoit votre adresse IP et dépose ses propres cookies pour faire fonctionner le calendrier, ainsi que les informations que vous saisissez si vous réservez un créneau. Calendly est une société américaine et les transferts sont encadrés par les clauses contractuelles types de l’UE ; voir <a href="https://calendly.com/privacy" target="_blank" rel="noopener">calendly.com/privacy</a>. Vous pouvez aussi réserver un appel par e-mail si vous préférez ne pas l’utiliser.',

    # --- contact form (contacts.html) ---
    'Enquiries':
        'Demandes',
    'Send us a message':
        'Envoyez-nous un message',
    'Send us the scope or the drawings and we will come back with a price and crew dates. The fastest route to a useful answer is the scope, the location, the standards that apply and the window you are working to.':
        'Envoyez-nous le périmètre ou les plans et nous reviendrons avec un prix et des dates d’équipe. Le chemin le plus court vers une réponse utile : le périmètre, le lieu, les normes applicables et la fenêtre d’intervention.',
    'For personnel requests, tell us the disciplines, the certifications and the headcount.':
        'Pour les demandes de personnel, indiquez-nous les métiers, les certifications et les effectifs.',
    'Applying for a job? The application form on the <a href="/careers">careers page</a> takes your CV and certificates with it.':
        'Vous postulez à un poste ? Le formulaire de la <a href="/careers">page carrières</a> accepte votre CV et vos certificats.',
    'Service group':
        'Domaine de services',
    'Select a service group':
        'Choisissez un domaine',
    'Not sure yet':
        'Je ne sais pas encore',
    'Type of enquiry':
        'Type de demande',
    'Select a type of enquiry':
        'Choisissez un type de demande',
    'Project enquiry':
        'Demande de projet',
    'Request for personnel':
        'Demande de personnel',
    'Inspection, NDT or rope access':
        'Inspection, CND ou travaux sur cordes',
    'Invoicing or administration':
        'Facturation ou administration',
    'Something else':
        'Autre sujet',
    'First name':
        'Prénom',
    'Last name':
        'Nom',
    'Company <span class="opt">(optional)</span>':
        'Société <span class="opt">(facultatif)</span>',
    'How can we help?':
        'Comment pouvons-nous vous aider ?',
    'I agree that ALPROJECTS, UAB may store these details in order to answer my enquiry. See the <a href="/privacy">privacy policy</a>.':
        'J’accepte qu’ALPROJECTS, UAB conserve ces informations afin de répondre à ma demande. Voir la <a href="/privacy">politique de confidentialité</a>.',
    'Website':
        'Site web',
    'Send the enquiry':
        'Envoyer la demande',
    'Company name':
        'Nom de la société',
    'Scope, location, standards and dates.':
        'Périmètre, lieu, normes et dates.',

    # --- homepage service slider ---
    '<span>Shipbuilding</span><span>Offshore</span><span>Industrial Facilities</span><span>Steel Structures</span>':
        '<span>Construction navale</span><span>Offshore</span><span>Sites industriels</span><span>Charpente métallique</span>',
    '<span>Shipbuilding</span><span>Process Plant</span><span>Engine Rooms</span><span>Utilities</span>':
        '<span>Construction navale</span><span>Unités de process</span><span>Salles des machines</span><span>Utilités</span>',
    '<span>Industrial Facilities</span><span>Energy Projects</span><span>Offshore</span><span>Steel Structures</span>':
        '<span>Sites industriels</span><span>Projets énergie</span><span>Offshore</span><span>Charpente métallique</span>',

    # --- homepage facts block (evidence set) ---

    # --- This is ALPROJECTS (TZ part 6) ---
    'This is ALPROJECTS':
        'Voici ALPROJECTS',
    'What we are here to do, and the rules we work by. Written down so a client can hold us to them.':
        'Ce que nous sommes là pour faire, et les règles que nous suivons. Écrites pour qu’un client puisse nous y tenir.',
    'Our vision':
        'Notre vision',
    'Industrial work that comes with its own evidence.':
        'Des travaux industriels qui apportent leurs propres preuves.',
    'Europe has no shortage of contractors who can weld. It has a shortage of contractors who can hand over the evidence with the work, in a form the client, the surveyor and the auditor all accept.':
        'L’Europe ne manque pas d’entreprises capables de souder. Elle manque d’entreprises capables de livrer les preuves avec les travaux, sous une forme que le client, l’expert et l’auditeur acceptent tous.',
    'Our mission':
        'Notre mission',
    'Certified people on site, and independent proof of what they did.':
        'Du personnel certifié sur site, et une preuve indépendante de son travail.',
    'We take mechanical scopes and deliver them with our own supervision. We supply the qualified people a project is short of. And we inspect the result with people who did not do the work.':
        'Nous prenons des périmètres mécaniques et les livrons avec notre propre encadrement. Nous fournissons le personnel qualifié qui manque à un projet. Et nous contrôlons le résultat avec des personnes qui n’ont pas exécuté les travaux.',
    'Three hundred specialists, and a schedule that does not wait':
        'Trois cents spécialistes, et un planning qui n’attend pas',
    'Welders, pipe fitters, shipbuilders, mechanics, NDT inspectors and rope access technicians. Most carry a second trade, which is why one of our people often covers what usually takes two.':
        'Soudeurs, tuyauteurs, constructeurs navals, mécaniciens, contrôleurs CND et cordistes. La plupart exercent un second métier, ce qui explique qu’un des nôtres couvre souvent ce qui demande habituellement deux personnes.',
    'They travel. A crew that mobilises to Norway on Monday can be in Rostock the following month. That is the job, and everyone who joins us knows it before the first rotation.':
        'Ils se déplacent. Une équipe mobilisée en Norvège un lundi peut être à Rostock le mois suivant. C’est le métier, et chacun le sait avant sa première rotation.',
    'We keep the roster current. Certificates, medicals and availability are checked before anyone is offered to a project.':
        'Nous tenons le fichier à jour. Certificats, visites médicales et disponibilités sont vérifiés avant de proposer quelqu’un à un projet.',
    'Work with us':
        'Travailler avec nous',
    'Meet the management':
        'La direction',
    'Our values':
        'Nos valeurs',
    'Values are worth writing down only if someone can hold you to them. Ours are written so a client can.':
        'Des valeurs ne valent d’être écrites que si quelqu’un peut vous y tenir. Les nôtres sont écrites pour qu’un client le puisse.',
    'We keep learning on every job':
        'Nous apprenons sur chaque chantier',
    'We debrief after each mobilisation and write down what we would do differently.':
        'Nous faisons un débriefing après chaque mobilisation et notons ce que nous ferions autrement.',
    'We share procedures between crews, so the second job runs faster than the first.':
        'Nous partageons les procédures entre équipes, pour que le deuxième chantier aille plus vite que le premier.',
    'We ask the client&rsquo;s supervisor what went wrong before he has to tell us.':
        'Nous demandons au responsable du client ce qui n’a pas marché avant qu’il ait à nous le dire.',
    'We bring people up to a second trade, because two skills in one man are worth more offshore.':
        'Nous formons nos gens à un second métier, car deux compétences chez un même homme valent plus en offshore.',
    'We are responsible for the scope':
        'Nous répondons du périmètre',
    'We take the work with our own supervision and our own quality control.':
        'Nous prenons les travaux avec notre propre encadrement et notre propre contrôle qualité.',
    'When the mistake is ours, we say so and we correct it at our cost.':
        'Quand l’erreur vient de nous, nous le disons et nous la corrigeons à nos frais.',
    'We never hand a problem down to the next contractor in the chain.':
        'Nous ne refilons jamais un problème à l’entreprise suivante dans la chaîne.',
    'We get everyone home at the end of the rotation.':
        'Nous ramenons tout le monde chez soi à la fin de la rotation.',
    'We look for the work others avoid':
        'Nous cherchons les chantiers que d’autres évitent',
    'We take scopes with difficult access, tight windows and unclear starting conditions.':
        'Nous prenons des périmètres à accès difficile, à fenêtres courtes et à conditions de départ incertaines.',
    'We answer enquiries that arrive at short notice, because that is when a client needs a contractor most.':
        'Nous répondons aux demandes qui arrivent au dernier moment, car c’est là qu’un client a le plus besoin d’une entreprise.',
    'We invest in certification before the market starts asking for it.':
        'Nous investissons dans la certification avant que le marché ne la réclame.',
    'We build the business together, across offices and across crews.':
        'Nous construisons l’entreprise ensemble, entre les bureaux et entre les équipes.',
    'We look after people and the site':
        'Nous prenons soin des personnes et du site',
    'We work to the client&rsquo;s permit system and add our own where theirs is thinner.':
        'Nous travaillons sous le régime de permis du client et ajoutons le nôtre là où le sien est plus léger.',
    'We leave the area cleaner than we found it.':
        'Nous laissons la zone plus propre que nous l’avons trouvée.',
    'We ask for help early. Nobody on a rope is expected to manage alone.':
        'Nous demandons de l’aide tôt. Personne sur corde n’est censé se débrouiller seul.',
    'We follow the law and our own procedures when nobody is watching.':
        'Nous respectons la loi et nos propres procédures quand personne ne regarde.',
    'We keep the date we gave':
        'Nous tenons la date annoncée',
    'A mobilisation date is given only when the people are actually free.':
        'Une date de mobilisation n’est donnée que lorsque les personnes sont réellement disponibles.',
    'We plan so that the safe method is also the fast one.':
        'Nous planifions pour que la méthode sûre soit aussi la plus rapide.',
    'We remind the client of his deadlines as well as ours.':
        'Nous rappelons au client ses échéances autant que les nôtres.',
    'A yard schedule does not move, so ours has to hold.':
        'Le planning d’un chantier naval ne bouge pas : le nôtre doit donc tenir.',
    'We say it early and we say it plainly':
        'Nous le disons tôt et nous le disons clairement',
    'We explain the scope and the risks before the work starts.':
        'Nous expliquons le périmètre et les risques avant le début des travaux.',
    'A problem is reported the day it appears. Friday is too late.':
        'Un problème est signalé le jour où il apparaît. Le vendredi, c’est trop tard.',
    'We confirm that we understood the client, and that he understood us.':
        'Nous confirmons que nous avons compris le client, et qu’il nous a compris.',
    'We write documentation a person can actually read.':
        'Nous rédigeons une documentation qu’une personne peut réellement lire.',
    'Anyone on our crew can stop a job.':
        'Chacun de notre équipe peut arrêter un chantier.',
    'ALPROJECTS Group &middot; Value 02':
        'ALPROJECTS Group &middot; Valeur 02',
    'HSEQ':
        'HSEQ',
    'Zero harm is a target, and we report against it':
        'Le zéro dommage est un objectif, et nous en rendons compte',
    'We work inside the client&rsquo;s permit system and add our own where theirs is thinner. Every scope gets a risk assessment and a method statement before mobilisation, and both are written for the actual site. Copying the paperwork from the last job is how people get hurt.':
        'Nous travaillons dans le régime de permis du client et ajoutons le nôtre là où le sien est plus léger. Chaque périmètre reçoit une analyse de risques et un mode opératoire avant mobilisation, tous deux rédigés pour le site réel. Recopier les documents du chantier précédent, c’est ainsi que les gens se blessent.',
    'Our management systems are certified to four standards. Certification is what lets a client accept our documentation without repeating the inspection themselves.':
        'Nos systèmes de management sont certifiés selon quatre normes. C’est la certification qui permet à un client d’accepter notre documentation sans refaire lui-même le contrôle.',
    '<b>No injuries</b><span>to our people, to the client&rsquo;s people, to anyone else on site.</span>':
        '<b>Aucune blessure</b><span>ni chez les nôtres, ni chez ceux du client, ni chez quiconque sur le site.</span>',
    '<b>No occupational illness</b><span>from the way we organise the work.</span>':
        '<b>Aucune maladie professionnelle</b><span>due à notre organisation du travail.</span>',
    '<b>No spills</b><span>to the sea, to the ground or to the drain.</span>':
        '<b>Aucun déversement</b><span>en mer, dans le sol ou à l’égout.</span>',
    '<b>No damage</b><span>to the structure we were sent to work on.</span>':
        '<b>Aucun dommage</b><span>à l’ouvrage sur lequel nous avons été envoyés.</span>',
    'We publish our safety figures once a year: hours worked, incidents, and what we changed as a result. A target nobody measures is a slogan.':
        'Nous publions nos chiffres de sécurité une fois par an : heures travaillées, incidents, et ce que nous avons changé en conséquence. Un objectif que personne ne mesure est un slogan.',
    '<b>ISO 3834</b><span>Welding quality</span>':
        '<b>ISO 3834</b><span>Qualité en soudage</span>',
    '<b>ISO 9001</b><span>Quality</span>':
        '<b>ISO 9001</b><span>Qualité</span>',
    '<b>ISO 14001</b><span>Environment</span>':
        '<b>ISO 14001</b><span>Environnement</span>',
    '<b>ISO 45001</b><span>Health and safety</span>':
        '<b>ISO 45001</b><span>Santé et sécurité</span>',
    'If this is how you want your contractor to work, send us the scope':
        'Si c’est ainsi que vous voulez voir travailler votre entreprise, envoyez-nous le périmètre',
    'We reply to project enquiries within one working day.':
        'Nous répondons aux demandes de projet sous un jour ouvré.',
    'ALPROJECTS crew on a wind farm site':
        'Équipe ALPROJECTS sur un parc éolien',
    'Rope access technician working on a turbine blade':
        'Cordiste intervenant sur une pale d’éolienne',
    'Rope access descent onto an offshore topside':
        'Descente sur corde vers une superstructure offshore',
    'This is ALPROJECTS &mdash; vision, values and HSEQ':
        'Voici ALPROJECTS &mdash; vision, valeurs et HSEQ',
    'Vision, values and HSEQ. What ALPROJECTS Group is here to do, and the rules we work by.':
        'Vision, valeurs et HSEQ. Ce qu’ALPROJECTS Group est là pour faire, et les règles que nous suivons.',
    'This is ALPROJECTS — ALPROJECTS Group':
        'Voici ALPROJECTS — ALPROJECTS Group',
    'Our management systems are certified to ISO 9001, 14001 and 45001, and our welding to ISO 3834. Certification is what lets a client accept our documentation without repeating the inspection themselves.':
        'Nos systèmes de management sont certifiés ISO 9001, 14001 et 45001, et notre soudage ISO 3834. C’est la certification qui permet à un client d’accepter notre documentation sans refaire l’inspection lui-même.',
    '<b>Shipbuilding</b> <span>Piping and mechanical installation on vessels under construction.</span> <em class="ar-e" aria-hidden="true">&#8593;</em>':
        '<b>Construction navale</b> <span>Tuyauterie et montage mécanique sur navires en construction.</span> <em class="ar-e" aria-hidden="true">&#8593;</em>',
    '<b>Offshore</b> <span>Inspection, access and mechanical works on offshore facilities.</span> <em class="ar-e" aria-hidden="true">&#8593;</em>':
        '<b>Offshore</b> <span>Inspection, accès et travaux mécaniques sur installations offshore.</span> <em class="ar-e" aria-hidden="true">&#8593;</em>',
    '<b>Industrial</b> <span>Plant installation, transformer packages, process piping.</span> <em class="ar-e" aria-hidden="true">&#8593;</em>':
        '<b>Industrie</b> <span>Montage d’usine, packages de transformateurs, tuyauterie de procédé.</span> <em class="ar-e" aria-hidden="true">&#8593;</em>',
    '<b>Energy and renewables</b> <span>Fuel handling infrastructure and wind energy support.</span> <em class="ar-e" aria-hidden="true">&#8593;</em>':
        '<b>Énergie et renouvelables</b> <span>Infrastructures de manutention de carburant et support éolien.</span> <em class="ar-e" aria-hidden="true">&#8593;</em>',
    '<span class="value" data-count="300" data-suffix="+">0+</span><span class="label">Certified specialists on the roster</span>':
        '<span class="value" data-count="300" data-suffix="+">0+</span><span class="label">Spécialistes certifiés dans le vivier</span>',
    '<span class="value" data-count="6">0</span><span class="label">Countries we work in</span>':
        '<span class="value" data-count="6">0</span><span class="label">Pays où nous intervenons</span>',
    '<span class="value" data-count="4">0</span><span class="label">Sectors, one set of disciplines</span>':
        '<span class="value" data-count="4">0</span><span class="label">Secteurs, une seule série de métiers</span>',
    'ALPROJECTS, UAB &middot; Šilutės pl. 2, LT-92298 Klaipėda, Lithuania<br> <a href="mailto:info@alprojects.eu">info@alprojects.eu</a> &middot; <a href="tel:+37063663744">+370 636 63 744</a>':
        'ALPROJECTS, UAB &middot; Šilutės pl. 2, LT-92298 Klaipėda, Lituanie<br> <a href="mailto:info@alprojects.eu">info@alprojects.eu</a> &middot; <a href="tel:+37063663744">+370 636 63 744</a>',
    'Standing':
        'Notre assise',
    'We deliver the scope, or we supply the people a scope is short of':
        'Nous livrons le périmètre, ou nous fournissons le personnel qui lui manque',
    'Often both, on the same site. We specialise in piping prefabrication and installation, steel fabrication and mechanical installation, and we provide certified technical personnel to projects across Europe.':
        'Souvent les deux, sur le même site. Nous sommes spécialisés dans la préfabrication et la pose de tuyauterie, la construction métallique et le montage mécanique, et nous fournissons du personnel technique certifié à des projets partout en Europe.',
    'The company employs between 51 and 200 people directly and draws on a roster of more than 300 certified specialists. Projects are resourced from that roster rather than subcontracted on, which is what keeps the quality system meaningful.':
        'L’entreprise emploie directement entre 51 et 200 personnes et s’appuie sur un vivier de plus de 300 spécialistes certifiés. Les projets sont pourvus à partir de ce vivier plutôt que sous-traités, et c’est ce qui donne du sens au système qualité.',
    'In heavy industry, projects run for months and commitments run for years. Independent proof of financial stability is proof that we will be there to see the work through &mdash; a different question from whether the welding is any good, and worth answering separately.':
        'Dans l’industrie lourde, les projets durent des mois et les engagements des années. Une preuve indépendante de solidité financière est la preuve que nous serons là pour mener le travail à son terme &mdash; une autre question que celle de la qualité des soudures, et qui mérite d’être traitée à part.',
    'What it is':
        'Ce que c’est',
    'The scaffold costs more than the repair':
        'L’échafaudage coûte plus cher que la réparation',
    'Nobody buys rope access because they want ropes. They buy it because the alternative is a scaffold, a crane, a vessel day or a shutdown. Each of those costs more than the work itself.':
        'Personne n’achète du travail sur corde par envie de cordes. On l’achète parce que l’alternative est un échafaudage, une grue, une journée de navire ou un arrêt d’installation. Chacun coûte plus cher que le travail lui-même.',
    'Our technicians hold IRATA and SOFT certification and most of them carry a second trade: inspection, welding or mechanical. One person on the rope replaces a scaffold crew and an inspector standing behind them.':
        'Nos techniciens sont certifiés IRATA et SOFT et la plupart exercent un second métier : inspection, soudage ou mécanique. Une personne sur corde remplace une équipe d’échafaudeurs et l’inspecteur qui se tient derrière elle.',
    'Every crew works with a written rescue plan and a supervisor on site. Without both, the job does not start.':
        'Chaque équipe travaille avec un plan de secours écrit et un superviseur sur site. Sans les deux, le chantier ne démarre pas.',
    'IRATA and SOFT':
        'IRATA et SOFT',
    'Typical mobilisation':
        'Mobilisation type',
    'short notice, crews of 2&ndash;6':
        'court préavis, équipes de 2&ndash;6',
    'offshore wind, oil and gas, industry, marine':
        'éolien offshore, pétrole et gaz, industrie, maritime',
    'Deliverable':
        'Livrable',
    'report in the client&rsquo;s format':
        'rapport au format du client',
    'The same crew works offshore topsides, turbine blades and onshore wind. Rope access is how they get there; the trade they carry is what they do once they arrive.':
        'La même équipe intervient sur les topsides offshore, les pales d’éoliennes et l’éolien terrestre. Le travail sur corde est la façon d’y accéder ; le métier qu’ils exercent est ce qu’ils font une fois arrivés.',
    'Rope access technician descending onto an offshore topside above open water':
        'Technicien cordiste descendant sur un topside offshore au-dessus de la mer',
    'Rope access technician working on a wind turbine blade':
        'Technicien cordiste travaillant sur une pale d’éolienne',
    'Three technicians on a wind farm site at first light':
        'Trois techniciens sur un parc éolien au lever du jour',
    'VCA':
        'VCA',
    'EBN Certification':
        'EBN Certification',
    'VCA certification mark issued by EBN Certification':
        'Marque de certification VCA délivrée par EBN Certification',
    'Scope on the three ISO certificates: inspection and industrial maintenance services for onshore and offshore installations, issued by DNV Business Assurance Finland. VCA is certified by EBN Certification. Select a certificate to open the PDF.':
        'Périmètre des trois certificats ISO : services d’inspection et de maintenance industrielle pour installations terrestres et offshore, délivrés par DNV Business Assurance Finland. Le VCA est certifié par EBN Certification. Sélectionnez un certificat pour ouvrir le PDF.',
    '<span>EBN Certification</span>':
        '<span>EBN Certification</span>',
    'ALPROJECTS, UAB<br>Šilutės pl. 2, LT-92298 Klaipėda, Lithuania<br> <a href="mailto:info@alprojects.eu">info@alprojects.eu</a><br> <a href="tel:+37063663744">+370 636 63 744</a>':
        'ALPROJECTS, UAB<br>Šilutės pl. 2, LT-92298 Klaipėda, Lituanie<br> <a href="mailto:info@alprojects.eu">info@alprojects.eu</a><br> <a href="tel:+37063663744">+370 636 63 744</a>',
    'Scaffolding costs more in downtime than in steel. IRATA and SOFT certified technicians reach the same place on rope, inspect it and repair it while the plant keeps running.':
        'Un échafaudage coûte plus cher en arrêt de production qu’en acier. Des techniciens certifiés IRATA et SOFT atteignent le même point sur corde, l’inspectent et le réparent pendant que l’installation continue de tourner.',
    'Inspection &amp; Access':
        'Inspection &amp; accès',
    '<span>Offshore Oil &amp; Gas</span><span>Wind Energy</span><span>Industrial Facilities</span><span>Marine</span>':
        '<span>Pétrole &amp; gaz offshore</span><span>Éolien</span><span>Installations industrielles</span><span>Maritime</span>',
    '<span class="value" data-count="300" data-suffix="+">300+</span> <span class="label">Certified specialists on the roster</span>':
        '<span class="value" data-count="300" data-suffix="+">300+</span> <span class="label">Spécialistes certifiés dans le vivier</span>',
    '<span class="value" data-count="6">6</span> <span class="label">Countries we work in</span>':
        '<span class="value" data-count="6">6</span> <span class="label">Pays où nous intervenons</span>',
    '<span class="value" data-count="4">4</span> <span class="label">Sectors, one set of disciplines</span>':
        '<span class="value" data-count="4">4</span> <span class="label">Secteurs, une seule série de métiers</span>',
    '<span class="value" data-count="3">3</span> <span class="label">ISO management systems, certified by DNV</span>':
        '<span class="value" data-count="3">3</span> <span class="label">Systèmes de management ISO, certifiés par DNV</span>',
    '<span class="value" data-count="90" data-suffix="+">90+</span> <span class="label">Projects delivered across multiple countries</span>':
        '<span class="value" data-count="90" data-suffix="+">90+</span> <span class="label">Projets livrés dans plusieurs pays</span>',
    '<span class="value" data-count="98" data-suffix="%">98%</span> <span class="label">Early risk detection by certified specialists</span>':
        '<span class="value" data-count="98" data-suffix="%">98%</span> <span class="label">Détection précoce des risques par des spécialistes certifiés</span>',
    '<span class="value" data-count="40" data-suffix="%">40%</span> <span class="label">Reduced inspection time through optimized workflows</span>':
        '<span class="value" data-count="40" data-suffix="%">40%</span> <span class="label">Temps d’inspection réduit grâce à des processus optimisés</span>',
    '<span class="value" data-count="1200" data-suffix="+">1,200+</span> <span class="label">Safe execution in complex and confined environments</span>':
        '<span class="value" data-count="1200" data-suffix="+">1 200+</span> <span class="label">Exécution sûre en milieu complexe et confiné</span>',
    '03 &middot; Industrial Projects':
        '03 &middot; Projets industriels',
    '<span class="num">03</span><span>01 Aug 2026 &middot; Industrial Projects</span><span class="arr">&#8593;</span>':
        '<span class="num">03</span><span>01 août 2026 &middot; Projets industriels</span><span class="arr">&#8593;</span>',
    '04 &middot; Energy Projects':
        '04 &middot; Projets énergie',
    '<span class="num">04</span><span>25 Jul 2026 &middot; Energy Projects</span><span class="arr">&#8593;</span>':
        '<span class="num">04</span><span>25 juil. 2026 &middot; Projets énergie</span><span class="arr">&#8593;</span>',
    '05 &middot; Industry':
        '05 &middot; Industrie',
    '<span class="num">05</span><span>25 Jul 2026 &middot; Industry</span><span class="arr">&#8593;</span>':
        '<span class="num">05</span><span>25 juil. 2026 &middot; Industrie</span><span class="arr">&#8593;</span>',
    '06 &middot; Company':
        '06 &middot; Entreprise',
    '<span class="num">06</span><span>23 Jun 2026 &middot; Company</span><span class="arr">&#8593;</span>':
        '<span class="num">06</span><span>23 juin 2026 &middot; Entreprise</span><span class="arr">&#8593;</span>',
    '<span class="num">03</span><span>01 Aug 2026 &middot; Industrial Projects</span><span class="arr">&#8593;</span>':
        '<span class="num">03</span><span>01 août 2026 &middot; Projets industriels</span><span class="arr">&#8593;</span>',
    '<span class="num">04</span><span>25 Jul 2026 &middot; Energy Projects</span><span class="arr">&#8593;</span>':
        '<span class="num">04</span><span>25 juil. 2026 &middot; Projets énergie</span><span class="arr">&#8593;</span>',
    '<span class="num">05</span><span>25 Jul 2026 &middot; Industry</span><span class="arr">&#8593;</span>':
        '<span class="num">05</span><span>25 juil. 2026 &middot; Industrie</span><span class="arr">&#8593;</span>',
    '<span class="num">06</span><span>23 Jun 2026 &middot; Company</span><span class="arr">&#8593;</span>':
        '<span class="num">06</span><span>23 juin 2026 &middot; Entreprise</span><span class="arr">&#8593;</span>',
    'Quality control (QA/QC)':
        'Contrôle qualité (QA/QC)',
    'Welder qualifications to EN ISO 9606-1, verified before mobilisation':
        'Qualifications de soudeurs selon EN ISO 9606-1, vérifiées avant mobilisation',
    'Welding coordination and traceability under ISO 3834-2':
        'Coordination en soudage et traçabilité selon ISO 3834-2',
    '<b>30</b><span>Positions to fill</span>':
        '<b>30</b><span>Postes à pourvoir</span>',
    '<b>No injuries</b><span>to our people, to the client&rsquo;s people, or to anyone else on site.</span>':
        '<b>Aucune blessure</b><span>ni chez les nôtres, ni chez ceux du client, ni chez quiconque sur le site.</span>',
    '<span class="kp-num">03</span> <span class="kp-name">Ostwind Offshore Wind Farm</span> <span class="kp-scope">Cable jointers, jointer&rsquo;s mates and rigging support.</span>':
        '<span class="kp-num">03</span> <span class="kp-name">Parc éolien offshore Ostwind</span> <span class="kp-scope">Jointeurs de câbles, aides-jointeurs et appui levage.</span>',
    '<span class="srv-n">11</span><span class="srv-name">Quality control (QA/QC)</span>':
        '<span class="srv-n">11</span><span class="srv-name">Contrôle qualité (QA/QC)</span>',
    'A weld is only as good as the paperwork behind it. We weld structural steel and piping systems by TIG (141), MAG (135) and flux-cored (136) processes, under an ISO 3834-2 quality system. The welders hold current qualifications and the procedure is approved before the first arc is struck.':
        'Une soudure ne vaut que la documentation qui l’accompagne. Nous soudons la charpente métallique et les tuyauteries en TIG (141), MAG (135) et fil fourré (136), sous un système qualité ISO 3834-2. Les soudeurs détiennent des qualifications en cours de validité et le mode opératoire est approuvé avant le premier arc.',
    'A weld is only as good as the paperwork behind it. We weld structural steel and piping systems by TIG (141), MAG (135) and flux-cored (136) processes,...':
        'Une soudure ne vaut que la documentation qui l’accompagne. Nous soudons la charpente métallique et les tuyauteries en TIG (141), MAG (135) et...',
    'ALPROJECTS, UAB has been awarded the Strongest in Lithuania 2025–2026 certificate by Creditinfo Group.':
        'ALPROJECTS, UAB a reçu le certificat Strongest in Lithuania 2025–2026 décerné par Creditinfo Group.',
    'ALPROJECTS, UAB holds the <strong>Strongest in Lithuania</strong> certificate, awarded by Creditinfo Group on 23 June 2026 to companies with a high credit score and a proven record of financial stability.':
        'ALPROJECTS, UAB détient le certificat <strong>Strongest in Lithuania</strong>, décerné par Creditinfo Group le 23 juin 2026 aux entreprises présentant une notation de crédit élevée et une solidité financière avérée.',
    'Abnormal load permits, escort and cargo securing to EN 12195-1, with CMR cover':
        'Autorisations de transport exceptionnel, escorte et arrimage selon EN 12195-1, avec couverture CMR',
    'Acceptance to EN ISO 5817 and ISO 10675, or to the project specification':
        'Critères d’acceptation selon EN ISO 5817 et ISO 10675, ou selon la spécification du projet',
    'Certificates you hold <span class="opt">(optional, select all that apply)</span>':
        'Certifications que vous détenez <span class="opt">(facultatif, sélectionnez tout ce qui s’applique)</span>',
    'Dismantling, skidding, jacking and positioning on SPMT or hydraulic gantry':
        'Démontage, ripage, levage et positionnement sur SPMT ou portique hydraulique',
    'Engine room piping: fuel, lube oil, cooling water, ballast and bilge systems, including spool prefabrication':
        'Tuyauterie de salle des machines : combustible, huile de graissage, eau de refroidissement, ballast et cale, y compris la préfabrication des tronçons',
    'Foundation preparation, chocking, grouting and laser shaft alignment':
        'Préparation des massifs, calage, scellement au coulis et alignement laser des lignes d’arbres',
    'Hull structural fitting and welding to class-approved procedures':
        'Montage et soudage de la structure de coque selon des procédures approuvées par la société de classification',
    'IRATA-certified technicians, Levels 1 to 3, with an IRATA Level 3 supervisor on every site':
        'Techniciens certifiés IRATA, niveaux 1 à 3, avec un superviseur IRATA niveau 3 sur chaque site',
    'If you believe we have handled your data improperly, you may lodge a complaint with the Lithuanian State Data Protection Inspectorate (Valstybinė duomenų apsaugos inspekcija), L. Sapiegos g. 17, LT-10312 Vilnius, <a href="mailto:ada@ada.lt">ada@ada.lt</a>, <a href="https://vdai.lrv.lt" target="_blank" rel="noopener">vdai.lrv.lt</a>.':
        'Si vous estimez que nous avons traité vos données de manière inappropriée, vous pouvez déposer une réclamation auprès de l’Inspection nationale de la protection des données de Lituanie (Valstybinė duomenų apsaugos inspekcija), L. Sapiegos g. 17, LT-10312 Vilnius, <a href="mailto:ada@ada.lt">ada@ada.lt</a>, <a href="https://vdai.lrv.lt" target="_blank" rel="noopener">vdai.lrv.lt</a>.',
    'Independent third-party verification, reported to the client in their format':
        'Vérification indépendante par tierce partie, rapportée au client dans son format',
    'Inspection and Test Plans (ITP) with hold, witness and review points agreed before work starts':
        'Plans de contrôle et d’essais (ITP) avec points d’arrêt, de convocation et de revue convenus avant le début des travaux',
    'Inspection with the plant running, where the method allows it':
        'Contrôle avec l’installation en service, lorsque la méthode le permet',
    'Instrument pipe fitters: small-bore, tubing, impulse lines and instrument hook-ups':
        'Tuyauteurs instrumentation : petit diamètre, tubing, lignes d’impulsion et raccordements d’instruments',
    'MAG (135) for structural steel fill and capping passes; MIG (131) for aluminium and non-ferrous work':
        'MAG (135) pour les passes de remplissage et de finition sur acier de construction ; MIG (131) pour l’aluminium et les métaux non ferreux',
    'Magnetic particle testing (MT) to EN ISO 17638 and ultrasonic testing (UT) to EN ISO 17640':
        'Magnétoscopie (MT) selon EN ISO 17638 et ultrasons (UT) selon EN ISO 17640',
    'Manufacturing Record Book (MRB) assembled as the work goes, not at the end':
        'Manufacturing Record Book (MRB) constitué au fil des travaux, et non à la fin',
    'Mobile repair teams':
        'Équipes mobiles de réparation',
    'Mobile repair teams — ALPROJECTS Group':
        'Équipes mobiles de réparation — ALPROJECTS Group',
    'Most delays in piping start with a bad fit-up. We supply fitters for process, utility and engine room systems, instrument fitters for small-bore work, and workshop crews who build spools straight from the isometrics. The dimensions are checked before the welder arrives, not after.':
        'La plupart des retards en tuyauterie commencent par un mauvais accostage. Nous fournissons des tuyauteurs pour les systèmes de procédé, d’utilités et de salle des machines, des tuyauteurs instrumentation pour le petit diamètre, et des équipes d’atelier qui préfabriquent les tronçons directement d’après les isométriques. Les cotes sont vérifiées avant l’arrivée du soudeur, pas après.',
    'Most delays in piping start with a bad fit-up. We supply fitters for process, utility and engine room systems, instrument fitters for small-bore work,...':
        'La plupart des retards en tuyauterie commencent par un mauvais accostage. Nous fournissons des tuyauteurs pour les systèmes de procédé, d’utilités...',
    'Moving a production line is a scheduling problem before it is a lifting problem. We dismantle, move, reinstall and align it, inside a running plant or between two countries.':
        'Déplacer une ligne de production est d’abord un problème de planning avant d’être un problème de levage. Nous la démontons, la déplaçons, la réinstallons et l’alignons, à l’intérieur d’une usine en service ou entre deux pays.',
    'Moving a production line is a scheduling problem before it is a lifting problem. We dismantle, move, reinstall and align it, inside a running plant or...':
        'Déplacer une ligne de production est d’abord un problème de planning avant d’être un problème de levage. Nous la démontons, la déplaçons, la...',
    'Nobody should be signing off their own work. UT, PT and MT let us inspect while the plant keeps running; radiography is planned around production windows. We report to the client, not to the contractor who did the welding.':
        'Personne ne devrait valider son propre travail. Les contrôles UT, PT et MT nous permettent d’intervenir sans arrêter l’installation ; la radiographie est planifiée autour des fenêtres de production. Nous rendons compte au client, et non à l’entreprise qui a réalisé la soudure.',
    'Nobody should be signing off their own work. UT, PT and MT let us inspect while the plant keeps running; radiography is planned around production...':
        'Personne ne devrait valider son propre travail. Les contrôles UT, PT et MT nous permettent d’intervenir sans arrêter l’installation ; la...',
    'Often without scaffolding, and usually without a shutdown':
        'Souvent sans échafaudage, et généralement sans arrêt d’installation',
    'On-board mechanical repairs':
        'Réparations mécaniques à bord',
    'Our management systems are certified to ISO 9001, 14001 and 45001, and our welding to ISO 3834. Certification is what lets a client accept our documentation without repeating the inspection.':
        'Nos systèmes de management sont certifiés ISO 9001, 14001 et 45001, et notre soudage ISO 3834. C’est la certification qui permet à un client d’accepter notre documentation sans refaire l’inspection.',
    'Our supervisors and our QA/QC engineers on site':
        'Nos superviseurs et nos ingénieurs QA/QC sur site',
    'Our technicians hold IRATA and SOFT certification and most of them carry a second trade: inspection, welding or mechanical fitting. One person on the rope replaces a scaffold crew and an inspector standing behind them.':
        'Nos techniciens sont certifiés IRATA et SOFT et la plupart exercent un second métier : inspection, soudage ou montage mécanique. Une personne sur corde remplace une équipe d’échafaudeurs et l’inspecteur qui se tient derrière elle.',
    'Phased array (PAUT) and TOFD where radiography is not practical':
        'Phased array (PAUT) et TOFD lorsque la radiographie n’est pas praticable',
    'Prefer not to fill in a form?':
        'Vous préférez ne pas remplir de formulaire ?',
    'Pressure piping to EN 13480 and PED 2014/68/EU, with pressure testing before insulation':
        'Tuyauterie sous pression selon EN 13480 et DESP 2014/68/UE, avec essai de pression avant calorifugeage',
    'Process and utility piping in carbon steel and stainless steel, small bore to large bore':
        'Tuyauterie de procédé et d’utilités en acier au carbone et en acier inoxydable, du petit au grand diamètre',
    'Quality assurance and quality control (QA/QC)':
        'Assurance et contrôle qualité (QA/QC)',
    'Quality assurance and quality control (QA/QC) — ALPROJECTS Group':
        'Assurance et contrôle qualité (QA/QC) — ALPROJECTS Group',
    'Quality system certified to ISO 9001; welding under ISO 3834-2':
        'Système qualité certifié ISO 9001 ; soudage selon ISO 3834-2',
    'Railway bridges · steel fitting · structural repairs · pipe welding, 5G position':
        'Ponts ferroviaires · montage métallique · réparations structurelles · soudage de tuyauterie, position 5G',
    'Repair work is decided in days, not months. We take steel renewal, piping replacement and mechanical repairs to class and to the owner&rsquo;s requirements.':
        'Une réparation se décide en jours, pas en mois. Nous prenons en charge le renouvellement de tôles, le remplacement de tuyauteries et les réparations mécaniques selon les exigences de la société de classification et de l’armateur.',
    'Repair work is decided in days, not months. We take steel renewal, piping replacement and mechanical repairs to class and to the owner\'s requirements.':
        'Une réparation se décide en jours, pas en mois. Nous prenons en charge le renouvellement de tôles, le remplacement de tuyauteries et les réparations mécaniques selon les exigences de la société de classification et de l’armateur.',
    'Scopes delivered to the yard&rsquo;s schedule and class-approved drawings':
        'Lots livrés selon le planning du chantier naval et les plans approuvés par la société de classification',
    'Short-notice mobilisation':
        'Mobilisation à court préavis',
    'Site-to-site moves across Europe':
        'Transferts de site à site dans toute l’Europe',
    'Six fields are required. Everything else helps us match you faster, but the form will send without them.':
        'Six champs sont obligatoires. Le reste nous aide à vous orienter plus vite, mais le formulaire part sans eux.',
    'Steel fabrication to EN 1090, mechanical completion documented and handed over as a package':
        'Construction métallique selon EN 1090, mechanical completion documentée et remise comme un ensemble',
    'Structural steel welding to EN 1090-1 and EN 1090-2, execution classes EXC2 and EXC3':
        'Soudage de charpente métallique selon EN 1090-1 et EN 1090-2, classes d’exécution EXC2 et EXC3',
    'Structural steel, pressure-retaining piping and pipe supports':
        'Charpente métallique, tuyauterie sous pression et supports de tuyauterie',
    'Support at client and third-party hold and witness points':
        'Assistance aux points d’arrêt et de convocation du client et des tiers',
    'Technicians certified to ISO 9712 Level II and Level III':
        'Techniciens certifiés ISO 9712 niveau II et niveau III',
    'This website has no user accounts, no analytics and sets no cookies of its own. Data reaches us in the following ways:':
        'Ce site n’a pas de comptes utilisateurs, pas d’analytique et ne dépose aucun cookie qui lui soit propre. Les données nous parviennent des façons suivantes :',
    'Transformer packages: bushings, coolers, conservators and connecting pipework':
        'Ensembles transformateurs : traversées, réfrigérants, conservateurs et tuyauterie de raccordement',
    'Turnarounds, shutdowns and breakdown repairs':
        'Grands arrêts, arrêts programmés et réparations d’avarie',
    'Visual testing (VT) to EN ISO 17637 and penetrant testing (PT) to EN ISO 3452':
        'Contrôle visuel (VT) selon EN ISO 17637 et ressuage (PT) selon EN ISO 3452',
    'WPS to EN ISO 15609-1, qualified by WPQR to EN ISO 15614-1, written for the project standard':
        'DMOS selon EN ISO 15609-1, qualifié par PV de qualification (WPQR) selon EN ISO 15614-1, rédigé pour la norme du projet',
    'We are recruiting 30 certified TIG welders for upcoming project scopes. This is the constraint on our current pipeline, so applications are reviewed quickly.':
        'Nous recrutons 30 soudeurs TIG certifiés pour des lots de projets à venir. C’est la contrainte de notre carnet actuel, donc les candidatures sont examinées rapidement.',
    'We ask the client&rsquo;s supervisor what went wrong before they have to tell us.':
        'Nous demandons au superviseur du client ce qui n’a pas marché avant qu’il ait à nous le dire.',
    'We bring people up to a second trade, because two skills in one person are worth more offshore.':
        'Nous formons nos équipes à un second métier, parce que deux compétences chez une même personne valent davantage en offshore.',
    'We remind the client of their deadlines as well as ours.':
        'Nous rappelons au client ses échéances autant que les nôtres.',
    'Working level of English (B1 or better)':
        'Niveau d’anglais professionnel (B1 ou plus)',
    'Yard schedules move, and the penalty lands on the subcontractor. We plan for that, and take engine room piping, structural steel and outfitting as complete scopes, on newbuilds and on repair.':
        'Les plannings des chantiers navals bougent, et la pénalité retombe sur le sous-traitant. Nous le prévoyons, et prenons en charge la tuyauterie de salle des machines, la charpente métallique et l’armement comme des lots complets, en construction neuve comme en réparation.',
    'Fuel handling infrastructure and wind energy support. Our <a href="/news/fuel-loading-terminal-completed">fuel loading terminal scope</a> ran from September 2025 to April 2026 with 12 specialists and over 11,000 hours on site — a useful figure for anyone planning work of that size.':
        'Infrastructures de manutention de carburant et support éolien. Notre <a href="/news/fuel-loading-terminal-completed">lot de terminal de chargement</a> s’est déroulé de septembre 2025 à avril 2026 avec 12 spécialistes et plus de 11 000 heures sur site — un repère utile pour qui planifie un chantier de cette taille.',
    'Yard schedules move, and the penalty lands on the subcontractor. We plan for that, and take engine room piping, structural steel and outfitting as com':
        'Les plannings des chantiers navals bougent, et la pénalité retombe sur le sous-traitant. Nous le prévoyons, et prenons en charge la tuyauterie de salle',

    # ---- Chantiers /projects/* (livraison client, 27 août 2026) ----
    # Vocabulaire réservoirs : virole (course), robe (shell), piquage
    # (nozzle), platine d'appui (pad plate), taquet provisoire
    # (temporary clip), palonnier (spreader beam), chevron (rafter).
    'Recent work':
        'Travaux récents',
    'All projects':
        'Tous les projets',
    'From this job':
        'Sur ce chantier',
    'Disciplines on this job':
        'Métiers sur ce chantier',
    'Four scopes, photographed as they were built.':
        'Quatre chantiers, photographiés pendant leur exécution.',
    'Read the job <span class="arr">&#8593;</span>':
        'Voir le chantier <span class="arr">&#8593;</span>',
    '6 photographs. Press one to open it full size.':
        '6 photographies. Cliquez sur l’une d’elles pour l’ouvrir en grand format.',
    '5 photographs. Press one to open it full size.':
        '5 photographies. Cliquez sur l’une d’elles pour l’ouvrir en grand format.',
    '3 photographs. Press one to open it full size.':
        '3 photographies. Cliquez sur l’une d’elles pour l’ouvrir en grand format.',
    'Shop fabrication and welding':
        'Fabrication et soudage en atelier',
    'Mechanical installation and welding':
        'Montage mécanique et soudage',
    'Mechanical installation and welding &middot; tank farm':
        'Montage mécanique et soudage &middot; parc de stockage',
    'Project &middot; Mechanical installation':
        'Chantier &middot; Montage mécanique',
    'Project &middot; Shop fabrication and welding':
        'Chantier &middot; Fabrication et soudage en atelier',
    'Project &middot; Mechanical installation and welding':
        'Chantier &middot; Montage mécanique et soudage',
    'Project &middot; Mechanical installation and welding &middot; tank farm':
        'Chantier &middot; Montage mécanique et soudage &middot; parc de stockage',
    'Tank and vessel fabrication':
        'Fabrication de réservoirs et de capacités',
    'Valve station and tie-in piping':
        'Poste de vannes et tuyauterie de raccordement',
    'Tank internals, nozzles and attachments':
        'Internes de réservoir, piquages et accessoires soudés',
    'Agitator replacement inside a storage tank':
        'Remplacement d’agitateur dans un réservoir de stockage',
    'Tank and vessel fabrication — ALPROJECTS Group':
        'Fabrication de réservoirs et de capacités — ALPROJECTS Group',
    'Valve station and tie-in piping — ALPROJECTS Group':
        'Poste de vannes et tuyauterie de raccordement — ALPROJECTS Group',
    'Tank internals, nozzles and attachments — ALPROJECTS Group':
        'Internes de réservoir, piquages et accessoires soudés — ALPROJECTS Group',
    'Agitator replacement inside a storage tank — ALPROJECTS Group':
        'Remplacement d’agitateur dans un réservoir de stockage — ALPROJECTS Group',
    'Send us the drawings.':
        'Envoyez-nous les plans.',
    'Send us the scope.':
        'Envoyez-nous le périmètre.',
    'Tell us what goes inside and we will price it.':
        'Dites-nous ce qui va à l’intérieur et nous le chiffrons.',
    'Tell us what is going in and we will look at it.':
        'Dites-nous ce qui doit être installé et nous l’étudions.',
    'Shell held up on packing, work going on underneath.':
        'Robe maintenue sur cales, travaux en dessous.',
    'The nozzles go in before the course goes on the stack.':
        'Les piquages sont posés avant que la virole ne rejoigne l’empilage.',
    'Vessel closed up.':
        'Capacité refermée.',
    'Inside the shell, with the temporary clips round the courses.':
        'À l’intérieur de la robe, avec les taquets provisoires autour des viroles.',
    'Lifted on slings from welded lugs.':
        'Levée par élingues sur oreilles soudées.',
    'The shop floor.':
        'L’atelier.',
    'Valves levelled before anything was tacked.':
        'Vannes mises de niveau avant tout pointage.',
    'The valve station.':
        'Le poste de vannes.',
    'Finished root.':
        'Racine terminée.',
    'Tied into the existing rack.':
        'Raccordé au rack existant.',
    'Work front under temporary cover.':
        'Front de travail sous abri provisoire.',
    'The pad plate goes on before the bracket.':
        'La platine se pose avant la console.',
    'Internal pipe off the shell nozzle.':
        'Tuyauterie interne au départ du piquage de robe.',
    'Roof rafters into the centre ring.':
        'Chevrons de toit vers l’anneau central.',
    'Looking up the shaft to the roof.':
        'Vue de l’arbre vers le toit.',
    'The bearing at the floor.':
        'Le palier au fond.',
    'Lower impeller on the shaft.':
        'Mobile inférieur sur l’arbre.',
    'Welder working under a tank shell held up and secured on timber packing, with bottom plates laid out on the shop floor':
        'Soudeur au travail sous une robe de réservoir maintenue et calée sur des cales en bois, tôles de fond disposées au sol de l’atelier',
    'Vessel shell course being lowered onto the course below by overhead crane, with the nozzles already welded in':
        'Virole de capacité descendue au pont roulant sur la virole inférieure, piquages déjà soudés',
    'Assembled vessel standing on blocks, with nozzles, a side manway and a drawing taped to the shell':
        'Capacité assemblée posée sur cales, avec ses piquages, un trou d’homme latéral et un plan scotché sur la robe',
    'Inside a tank shell, a long pipe on trestles and temporary clips welded round the courses above the bottom plates':
        'À l’intérieur d’une robe de réservoir, une longue tuyauterie sur tréteaux et des taquets provisoires soudés autour des viroles au-dessus des tôles de fond',
    'Tank shell lifted on slings from lugs welded to the top course':
        'Robe de réservoir levée par élingues depuis des oreilles soudées sur la virole supérieure',
    'Fabrication hall with tank shells, a vessel on packing, and a spreader beam with slings on the floor':
        'Halle de fabrication avec des robes de réservoir, une capacité sur cales et un palonnier avec ses élingues au sol',
    'Row of valves and piping levelled and aligned before tacking':
        'Rangée de vannes et de tuyauterie mises de niveau et alignées avant pointage',
    'Valves on a tank valve station, with a spirit level laid across a valve during setting out':
        'Vannes d’un poste de vannes de réservoir, avec un niveau à bulle posé en travers d’une vanne pendant le réglage',
    'Finished root run on a butt weld, photographed down the pipe bore from the open end of a spool':
        'Passe de racine terminée sur une soudure bout à bout, photographiée dans l’alésage depuis l’extrémité ouverte d’un tronçon',
    'Tie-in piping and flanged joints running from the valve station into the existing rack':
        'Tuyauterie de raccordement et assemblages à brides reliant le poste de vannes au rack existant',
    'Valve station under temporary cover at the base of a storage tank':
        'Poste de vannes sous abri provisoire au pied d’un réservoir de stockage',
    'External bracket welded to a pad plate on the tank shell, with the pad welded all round':
        'Console extérieure soudée sur une platine d’appui de la robe du réservoir, la platine étant soudée sur tout son pourtour',
    'Internal pipe connected to a shell nozzle inside a tank, with bottom plates below':
        'Tuyauterie interne raccordée à un piquage de robe à l’intérieur d’un réservoir, tôles de fond en dessous',
    'Tank roof on radial rafters into the centre ring, with a nozzle opening cut':
        'Toit de réservoir sur chevrons radiaux vers l’anneau central, avec une ouverture de piquage découpée',
    'Agitator shaft running the full height of a storage tank up to the roof, with the upper impeller near the top':
        'Arbre d’agitateur sur toute la hauteur d’un réservoir de stockage jusqu’au toit, le mobile supérieur près du sommet',
    'Agitator bearing at the tank floor, with levelling tools in place':
        'Palier d’agitateur au fond du réservoir, outils de mise de niveau en place',
    'Lower agitator impeller bolted to the shaft inside a storage tank, with the bearing on the floor below it':
        'Mobile d’agitation inférieur boulonné sur l’arbre à l’intérieur d’un réservoir de stockage, avec le palier au fond en dessous',
    'We weld the nozzles into the courses before they go on the stack, weld out the seams under a crane, and cut and fit the bottoms on the shop floor.':
        'Nous soudons les piquages dans les viroles avant leur mise en empilage, remplissons les soudures sous pont roulant, et découpons et ajustons les fonds au sol de l’atelier.',
    'We weld the nozzles into the courses before they go on the stack, weld out the seams under a crane, and cut and fit the bottoms on the shop...':
        'Nous soudons les piquages dans les viroles avant leur mise en empilage, remplissons les soudures sous pont roulant, et découpons et ajustons les fonds...',
    'Nozzles and manways go into the shell courses before they go on the stack, while a course can still be worked from both sides. The welder works downhand and can get at the back of the joint. By the time a course goes on the stack the nozzles are already in it.':
        'Les piquages et les trous d’homme sont posés dans les viroles avant leur mise en empilage, tant qu’une virole reste accessible des deux côtés. Le soudeur travaille à plat et peut atteindre l’envers du joint. Au moment où une virole rejoint l’empilage, ses piquages y sont déjà.',
    'The first course goes on timber packing. The next comes down on it under the crane, landed and held while the seam is tacked, and then welded out.':
        'La première virole est posée sur cales en bois. La suivante y est descendue au pont roulant, posée et maintenue le temps du pointage, puis la soudure est remplie.',
    'The large tanks go together the other way up. The shell is held up on packing and the next course goes on underneath it, with a row of temporary clips round the inside holding it while the seams are welded out.':
        'Les grands réservoirs se montent dans l’autre sens. La robe est maintenue en l’air sur cales et la virole suivante vient se placer en dessous, une rangée de taquets provisoires à l’intérieur la tenant pendant le remplissage des soudures.',
    'Those clips and the lifting lugs come off when the shell is done, and the places where they were welded are dressed back level with the plate.':
        'Ces taquets et les oreilles de levage sont déposés une fois la robe terminée, et leurs zones de soudure sont arasées au nu de la tôle.',
    'Lifting is done on the overhead crane, using slings and a spreader beam. Bottom plates are cut and fitted on the shop floor.':
        'Le levage se fait au pont roulant, avec élingues et palonnier. Les tôles de fond sont découpées et ajustées au sol de l’atelier.',
    'In the shop the welding is done under cover and under a crane.':
        'En atelier, le soudage se fait à l’abri et sous pont roulant.',
    'A new valve station at the base of a storage tank. We set and levelled the valves, fitted the spools, welded and bolted the joints, and tied the run into the existing pipe rack.':
        'Un nouveau poste de vannes au pied d’un réservoir de stockage. Nous avons réglé et mis de niveau les vannes, posé les tronçons, soudé et boulonné les assemblages, et raccordé la ligne au rack à tuyauterie existant.',
    'A new valve station at the base of a storage tank. We set and levelled the valves, fitted the spools, welded and bolted the joints, and tied the run...':
        'Un nouveau poste de vannes au pied d’un réservoir de stockage. Nous avons réglé et mis de niveau les vannes, posé les tronçons, soudé et boulonné...',
    'A storage tank needed a new valve station and a connection into the existing pipe rack.':
        'Un réservoir de stockage devait recevoir un nouveau poste de vannes et un raccordement au rack à tuyauterie existant.',
    'The valves went on adjustable stands and we levelled them before anything was fixed. We did not tack until the run was straight and the flange faces were parallel.':
        'Les vannes ont été posées sur supports réglables et mises de niveau avant toute fixation. Nous n’avons pointé qu’une fois la ligne droite et les portées de brides parallèles.',
    'Some of the joints are welded, the rest are flanged and bolted. The spools went in between them.':
        'Une partie des assemblages est soudée, le reste est à brides boulonnées. Les tronçons ont été posés entre les deux.',
    'The close-up shows a finished root, taken down the bore from the open end of a spool.':
        'Le gros plan montre une racine terminée, prise dans l’alésage depuis l’extrémité ouverte d’un tronçon.',
    'The work front sat under temporary cover, with the plant live around it.':
        'Le front de travail était sous abri provisoire, l’installation restant en service autour.',
    'Internal pipe off a shell nozzle, brackets on pad plates, roof rafters into the centre ring.':
        'Tuyauterie interne au départ d’un piquage de robe, consoles sur platines d’appui, chevrons de toit vers l’anneau central.',
    'Internal pipe off a shell nozzle, brackets on pad plates, roof rafters into the centre...':
        'Tuyauterie interne au départ d’un piquage de robe, consoles sur platines d’appui, chevrons de toit vers...',
    'On this job no bracket went straight onto the shell. Every attachment sat on a pad plate, and the pad was welded to the shell. The close-up shows one. If the bracket ever has to come off, it comes off the pad and the shell is untouched.':
        'Sur ce chantier, aucune console n’a été soudée directement sur la robe. Chaque accessoire repose sur une platine d’appui, et c’est la platine qui est soudée à la robe. Le gros plan en montre une. Si la console doit un jour être déposée, elle se dépose de la platine et la robe reste intacte.',
    'Pads went down on the bottom plates as well, the stands went on the pads and the pipe sat on the stands. When the stands come off, the pads take the damage instead of the bottom plates.':
        'Des platines ont également été posées sur les tôles de fond ; les supports sont venus sur les platines et la tuyauterie sur les supports. À la dépose des supports, ce sont les platines qui encaissent, pas les tôles de fond.',
    'The internal pipe runs from a shell nozzle across the tank, and the roof goes on radial rafters into a centre ring.':
        'La tuyauterie interne part d’un piquage de robe et traverse le réservoir ; le toit repose sur des chevrons radiaux convergeant vers un anneau central.',
    'Temporary steel goes on and comes off all the way through a job like this. Every place it was welded is ground back flush before the tank is painted.':
        'Sur un chantier de ce type, les pièces provisoires sont soudées puis déposées en permanence. Chaque zone soudée est meulée à ras avant la mise en peinture du réservoir.',
    'The shaft runs from the drive mounting on the roof down to a bearing at the floor, with two impellers on it.':
        'L’arbre descend du support d’entraînement en toiture jusqu’à un palier au fond, avec deux mobiles d’agitation.',
    'The shaft runs from the drive mounting on the roof down to a bearing at the floor, with two impellers on...':
        'L’arbre descend du support d’entraînement en toiture jusqu’à un palier au fond, avec deux mobiles...',
    'The agitator in this tank was being replaced. The shaft runs the full height of the tank, from the drive mounting on the roof down to a bearing at the floor. Two impellers on it, one low down and one near the roof.':
        'L’agitateur de ce réservoir était en cours de remplacement. L’arbre occupe toute la hauteur du réservoir, du support d’entraînement en toiture jusqu’à un palier au fond. Deux mobiles d’agitation dessus, un en partie basse et un près du toit.',
    'The fitting work was done inside the tank, with the tank out of service.':
        'Le montage a été réalisé à l’intérieur du réservoir, celui-ci étant hors service.',
    'The bearing at the floor went in first. We levelled it before any of the shaft went in, and checked the shaft once it was down. Everything above depends on that bearing.':
        'Le palier au fond a été posé en premier. Nous l’avons mis de niveau avant toute mise en place de l’arbre, puis contrôlé l’arbre une fois descendu. Tout ce qui se trouve au-dessus dépend de ce palier.',
    'We fitted the lower impeller from the tank floor and the upper one from temporary access.':
        'Nous avons monté le mobile inférieur depuis le fond du réservoir et le supérieur depuis un accès provisoire.',

    # ---- plate-sequence redesign of /projects/*, 27 Aug 2026 ----
    'Scope':
        'Périmètre',
    'Plates':
        'Planches',
    'Setting':
        'Contexte',
    'More projects':
        'Autres chantiers',
    '6 photographs':
        '6 photographies',
    '3 photographs':
        '3 photographies',
    'How it was built':
        'Le déroulement du chantier',
    'Tank out of service':
        'Réservoir hors service',
    'Tank being fitted out':
        'Réservoir en cours d’équipement',
    'Fabrication shop, under a crane':
        'Atelier de fabrication, sous pont roulant',
    'Live plant, work front under cover':
        'Installation en service, front de travail sous abri',
    'The roof goes on radial rafters into a centre ring.':
        'Le toit repose sur des chevrons radiaux convergeant vers un anneau central.',
    'One plate to a stage. Press a plate to open it full size.':
        'Une planche par étape. Cliquez sur une planche pour l’ouvrir en grand format.',
    'The internal pipe runs from a shell nozzle across the tank.':
        'La tuyauterie interne part d’un piquage de robe et traverse le réservoir.',
    '<span class="case-num">04</span> <span class="case-kicker">Mechanical installation</span>':
        '<span class="case-num">04</span> <span class="case-kicker">Montage mécanique</span>',
    '<span class="case-num">01</span> <span class="case-kicker">Shop fabrication and welding</span>':
        '<span class="case-num">01</span> <span class="case-kicker">Fabrication et soudage en atelier</span>',
    '<span class="case-num">03</span> <span class="case-kicker">Mechanical installation and welding</span>':
        '<span class="case-num">03</span> <span class="case-kicker">Montage mécanique et soudage</span>',
    '<span class="case-num">02</span> <span class="case-kicker">Mechanical installation and welding &middot; tank farm</span>':
        '<span class="case-num">02</span> <span class="case-kicker">Montage mécanique et soudage &middot; parc de stockage</span>',
    '<span class="eyebrow">Index</span> <span class="case-next-t">All projects</span> <span class="arr" aria-hidden="true">&#8593;</span>':
        '<span class="eyebrow">Index</span> <span class="case-next-t">Tous les projets</span> <span class="arr" aria-hidden="true">&#8593;</span>',
    '<span class="eyebrow">Next project</span> <span class="case-next-t">Tank and vessel fabrication</span> <span class="arr" aria-hidden="true">&#8593;</span>':
        '<span class="eyebrow">Chantier suivant</span> <span class="case-next-t">Fabrication de réservoirs et de capacités</span> <span class="arr" aria-hidden="true">&#8593;</span>',
    '<span class="eyebrow">Next project</span> <span class="case-next-t">Valve station and tie-in piping</span> <span class="arr" aria-hidden="true">&#8593;</span>':
        '<span class="eyebrow">Chantier suivant</span> <span class="case-next-t">Poste de vannes et tuyauterie de raccordement</span> <span class="arr" aria-hidden="true">&#8593;</span>',
    '<span class="eyebrow">Next project</span> <span class="case-next-t">Tank internals, nozzles and attachments</span> <span class="arr" aria-hidden="true">&#8593;</span>':
        '<span class="eyebrow">Chantier suivant</span> <span class="case-next-t">Internes de réservoir, piquages et accessoires soudés</span> <span class="arr" aria-hidden="true">&#8593;</span>',
    '<span class="eyebrow">Next project</span> <span class="case-next-t">Agitator replacement inside a storage tank</span> <span class="arr" aria-hidden="true">&#8593;</span>':
        '<span class="eyebrow">Chantier suivant</span> <span class="case-next-t">Remplacement d’agitateur dans un réservoir de stockage</span> <span class="arr" aria-hidden="true">&#8593;</span>',
    'On this job no bracket went straight onto the shell. Every attachment sat on a pad plate, and the pad was welded to the shell. The close-up above shows one. If the bracket ever has to come off, it comes off the pad and the shell is untouched.':
        'Sur ce chantier, aucune console n’a été soudée directement sur la robe. Chaque accessoire repose sur une platine d’appui, et c’est la platine qui est soudée à la robe. Le gros plan ci-dessus en montre une. Si la console doit un jour être déposée, elle se dépose de la platine et la robe reste intacte.',

    # ---- sticky plate deck, 27 Aug 2026 ----
    '<span class="slide-label">Stage</span> <span class="slide-count">01 / 02</span>':
        '<span class="slide-label">Étape</span> <span class="slide-count">01 / 02</span>',
    '<span class="slide-label">Stage</span> <span class="slide-count">01 / 05</span>':
        '<span class="slide-label">Étape</span> <span class="slide-count">01 / 05</span>',
    '<span class="slide-label">Stage</span> <span class="slide-count">02 / 02</span>':
        '<span class="slide-label">Étape</span> <span class="slide-count">02 / 02</span>',
    '<span class="slide-label">Stage</span> <span class="slide-count">02 / 05</span>':
        '<span class="slide-label">Étape</span> <span class="slide-count">02 / 05</span>',
    '<span class="slide-label">Stage</span> <span class="slide-count">03 / 05</span>':
        '<span class="slide-label">Étape</span> <span class="slide-count">03 / 05</span>',
    '<span class="slide-label">Stage</span> <span class="slide-count">04 / 05</span>':
        '<span class="slide-label">Étape</span> <span class="slide-count">04 / 05</span>',
    '<span class="slide-label">Stage</span> <span class="slide-count">05 / 05</span>':
        '<span class="slide-label">Étape</span> <span class="slide-count">05 / 05</span>',

    # ---- 26 Aug audit, remaining Block 2/4 corrections ----
    'Where we have delivered':
        'Où nous sommes intervenus',
    'Drydock and afloat (alongside) repair scopes':
        'Réparations en cale sèche et à flot (à quai)',
    'We aim to reply to project enquiries within one working day.':
        'Nous nous efforçons de répondre aux demandes de projet sous un jour ouvré.',
    'The scope ran from September 2025 to April 2026 and was delivered by a team of 12 specialists, accumulating more than 11,000 hours on site.':
        'Le lot s’est déroulé de septembre 2025 à avril 2026 et a été réalisé par une équipe de 12 spécialistes, totalisant plus de 11 000 heures sur site.',
    'Yard schedules move, and the penalty lands on the subcontractor. We plan for that, and take engine room piping, structural steel and outfitting as...':
        'Les plannings des chantiers navals bougent, et la pénalité retombe sur le sous-traitant. Nous le prévoyons, et prenons en charge la tuyauterie de salle...',
    'We track hours worked, incidents and what we changed as a result, and we share the figures with clients on request. A target nobody measures is a slogan.':
        'Nous suivons les heures travaillées, les incidents et ce que nous avons changé en conséquence, et nous communiquons les chiffres aux clients sur demande. Un objectif que personne ne mesure n’est qu’un slogan.',
    'Yard schedules move, and the penalty lands on the subcontractor. We plan for that, and take engine room piping, structural steel and outfitting as complete scopes.':
        'Les plannings des chantiers navals bougent, et la pénalité retombe sur le sous-traitant. Nous le prévoyons, et prenons en charge la tuyauterie de salle des machines, la charpente métallique et l’armement comme des lots complets.',
    'Head office in Klaipėda, Lithuania, with project bases in <strong>six countries</strong>, serving offshore, shipbuilding and industry across Northern and Western Europe.':
        'Siège à Klaipėda, en Lituanie, avec des bases projet dans <strong>six pays</strong>, au service de l’offshore, de la construction navale et de l’industrie en Europe du Nord et de l’Ouest.',
    'We draw on a roster of more than 300 certified specialists. Projects are resourced from that roster rather than subcontracted on, which is what keeps the quality system meaningful.':
        'Nous nous appuyons sur un vivier de plus de 300 spécialistes certifiés. Les chantiers sont dotés à partir de ce vivier plutôt que sous-traités, et c’est ce qui donne son sens au système qualité.',
    'Lithuania &middot; Norway &middot; United Kingdom &middot; Netherlands &middot; Germany &middot; Belgium &mdash; offshore, shipbuilding and industry across Northern and Western Europe.':
        'Lituanie &middot; Norvège &middot; Royaume-Uni &middot; Pays-Bas &middot; Allemagne &middot; Belgique &mdash; offshore, construction navale et industrie en Europe du Nord et de l’Ouest.',
    'Scaffolding costs more in downtime than in steel. IRATA-certified technicians, Levels 1 to 3, with an IRATA Level 3 supervisor on every site reach the same place on rope, inspect it and repair it while the plant keeps running.':
        'L’échafaudage coûte plus cher en arrêt de production qu’en acier. Des techniciens certifiés IRATA, niveaux 1 à 3, avec un superviseur IRATA niveau 3 sur chaque site, atteignent le même point sur corde, l’inspectent et le réparent pendant que l’installation continue de tourner.',
    'Awarded to ALPROJECTS, UAB by Creditinfo Group on 23 June 2026, recognising a high credit score and a proven record of financial stability. In heavy industry, projects run for months and commitments run for years &mdash; independent proof of stability is proof we will be there to see the work through.':
        'Décerné à ALPROJECTS, UAB par Creditinfo Group le 23 juin 2026, en reconnaissance d’une notation de crédit élevée et d’une solidité financière avérée. Dans l’industrie lourde, les chantiers durent des mois et les engagements des années &mdash; une preuve indépendante de solidité est la preuve que nous serons là jusqu’au bout.',

    # ---- audit Block 5: privacy sections, consent, abbreviations ----
    '9. Cookies':
        '9. Cookies',
    '12. Changes':
        '12. Modifications',
    '11. Children':
        '11. Mineurs',
    '7. Your rights':
        '7. Vos droits',
    '5. Legal basis':
        '5. Base légale',
    '4. Recruitment data':
        '4. Données de recrutement',
    '10. How we protect it':
        '10. Comment nous la protégeons',
    '6. How long we keep it':
        '6. Durée de conservation',
    '8. Health data in applications':
        '8. Données de santé dans les candidatures',
    'The site is served over HTTPS only, with HTTP redirected.':
        'Le site est servi exclusivement en HTTPS, le HTTP étant redirigé.',
    'Access is removed when someone leaves the company or changes role.':
        'Les accès sont retirés lorsqu’une personne quitte l’entreprise ou change de fonction.',
    'It is a static site: no database, no user accounts and no login to compromise.':
        'C’est un site statique : pas de base de données, pas de comptes utilisateurs et aucune connexion à compromettre.',
    'We do not carry out automated decision-making or profiling, including in recruitment.':
        'Nous ne pratiquons pas de décision automatisée ni de profilage, y compris en recrutement.',
    'This website is not intended for persons under 16, and we do not knowingly collect their personal data.':
        'Ce site n’est pas destiné aux personnes de moins de 16 ans, et nous ne collectons pas sciemment leurs données personnelles.',
    'Application documents reach us by email and are stored in the company account, access limited to the people resourcing projects.':
        'Les dossiers de candidature nous parviennent par e-mail et sont conservés dans le compte de l’entreprise, l’accès étant limité aux personnes chargées de doter les chantiers.',
    'Industrial Rope Access Trade Association (IRATA) certified technicians, Levels 1 to 3, with an IRATA Level 3 supervisor on every site':
        'Techniciens certifiés Industrial Rope Access Trade Association (IRATA), niveaux 1 à 3, avec un superviseur IRATA niveau 3 sur chaque site',
    'You may also withdraw consent at any time, without affecting the lawfulness of processing carried out before withdrawal (Article 7(3)).':
        'Vous pouvez également retirer votre consentement à tout moment, sans que cela affecte la licéité du traitement effectué avant le retrait (article 7, paragraphe 3).',
    'Welding Procedure Specification (WPS) to EN ISO 15609-1, qualified by Welding Procedure Qualification Record (WPQR) to EN ISO 15614-1, written for the project standard':
        'Descriptif de mode opératoire de soudage (DMOS / WPS) selon EN ISO 15609-1, qualifié par procès-verbal de qualification (QMOS / WPQR) selon EN ISO 15614-1, rédigé pour la norme du projet',
    'This section describes how the site and our handling are <em>designed</em>. It is not a statement that we hold an ISO 27001 certificate or any other security attestation, because we do not.':
        'Cette section décrit la manière dont le site et notre traitement sont <em>conçus</em>. Elle n’affirme pas que nous détenons un certificat ISO 27001 ou toute autre attestation de sécurité, car ce n’est pas le cas.',
    'This website sets no cookies of its own. It has no analytics, no advertising tags, no tracking pixels and no user accounts, so there is nothing to consent to and no cookie banner to dismiss.':
        'Ce site ne dépose aucun cookie qui lui soit propre. Il n’a ni analytique, ni balises publicitaires, ni pixels de suivi, ni comptes utilisateurs : il n’y a donc rien à accepter et aucune bannière de cookies à fermer.',
    'By subscribing you agree that ALPROJECTS, UAB will process your email address to send company news and project updates. You can unsubscribe at any time. See our <a href="/privacy">Privacy Policy</a>.':
        'En vous abonnant, vous acceptez qu’ALPROJECTS, UAB traite votre adresse e-mail pour vous envoyer des actualités de l’entreprise et des informations sur les projets. Vous pouvez vous désabonner à tout moment. Voir notre <a href="/privacy">Politique de confidentialité</a>.',
    'The one exception is the scheduling calendar on the contacts page. It is not loaded until you press the button that opens it; if you do, Calendly sets its own cookies at that point. Nothing is set if you do not.':
        'La seule exception est le calendrier de rendez-vous sur la page contacts. Il n’est chargé que lorsque vous appuyez sur le bouton qui l’ouvre ; si vous le faites, Calendly dépose alors ses propres cookies. Rien n’est déposé si vous ne le faites pas.',
    'Some applicants choose to upload a medical or fitness certificate. This is health data and falls under Article 9 GDPR. We process it only where it is necessary for obligations in the field of employment and occupational health and safety law (Article 9(2)(b)), we store it separately from other application data, and access is limited to the people responsible for mobilisation.':
        'Certains candidats choisissent de téléverser un certificat médical ou d’aptitude. Il s’agit de données de santé, relevant de l’article 9 du RGPD. Nous ne les traitons que lorsque cela est nécessaire aux obligations en matière de droit du travail et de santé et sécurité au travail (article 9, paragraphe 2, point b), nous les conservons séparément des autres pièces de candidature, et l’accès est limité aux personnes chargées de la mobilisation.',

    # ---- slide 3 valve-station photograph, 29 Aug 2026 ----
    'Tie-in piping and valve station at a tank farm, with gate and globe valves set on stands and the run tying into the existing rack':
        'Tuyauterie de raccordement et poste de vannes dans un parc de stockage, avec des vannes à opercule et des robinets à soupape posés sur supports et la ligne raccordée au rack à tuyauterie existant',

    # ---- stats photo, nozzle tie-in, 29 Aug 2026 ----

    # ---- hero foot, 29 Aug 2026 ----
    '<span>Klaip&#279;da, Lithuania</span> <span class="hero-scroll">Scroll<i></i></span>':
        '<span>Klaip&#279;da, Lituanie</span> <span class="hero-scroll">Faire d&#233;filer<i></i></span>',

    # ---- sector titles disambiguated + news description, 29 Aug 2026 ----
    'Industrial sector — ALPROJECTS Group':
        'Secteur industriel — ALPROJECTS Group',
    'Offshore sector — ALPROJECTS Group':
        'Secteur offshore — ALPROJECTS Group',
    'Renewables sector — ALPROJECTS Group':
        'Secteur des énergies renouvelables — ALPROJECTS Group',
    'Shipbuilding sector — ALPROJECTS Group':
        'Secteur de la construction navale — ALPROJECTS Group',
    'Project updates and engineering insights from ALPROJECTS Group — welding, piping, NDT and offshore scopes across Northern and Western Europe.':
        'Actualités de chantiers et retours d’ingénierie d’ALPROJECTS Group — soudage, tuyauterie, CND et lots offshore en Europe du Nord et de l’Ouest.',

    # --- case: engine room piping and machinery installation -------------
    'Engine room piping and machinery installation':
        'Tuyauterie et montage des machines en salle des machines',
    'Engine room piping and machinery installation — ALPROJECTS Group':
        'Tuyauterie et montage des machines en salle des machines — ALPROJECTS Group',
    'Mechanical installation and piping · Shipbuilding':
        'Montage mécanique et tuyauterie · Construction navale',
    'Project &middot; Mechanical installation and piping · Shipbuilding':
        'Chantier &middot; Montage mécanique et tuyauterie · Construction navale',
    'Vessel under construction, machinery spaces':
        'Navire en construction, locaux machines',
    'Machinery on resilient mounts, and the seawater, bilge and fuel lines that connect it. The mounts went down first; the piping followed, through a compartment that was already full.':
        'Des machines sur supports élastiques, et les circuits d’eau de mer, de cale et de combustible qui les relient. Les supports d’abord, la tuyauterie ensuite, dans un local déjà encombré.',
    'The mounts go down before anything else. We land the machine on them all at once, then set each mount so it takes its share of the load and sits within the deflection the maker allows. The alignment is checked and recorded before the first flange is made up, and again once the lines are connected.':
        'Les supports sont posés avant tout le reste. Nous reposons la machine sur l’ensemble des supports en une seule fois, puis réglons chacun d’eux pour qu’il porte sa part de la charge et reste dans la flèche admise par le constructeur. L’alignement est contrôlé et consigné avant l’assemblage de la première bride, puis de nouveau une fois les lignes raccordées.',
    'The drawing gives the route; the dimensions come off the steel. By the time the piping starts the space is full, so we build the valves, the strainer and the branches up on one frame outside the compartment and land the group as a unit, with the bolt holes matching and the flange faces square. Set out that way, somebody standing in front of it can reach every handwheel.':
        'Le plan donne le tracé ; les cotes sont relevées sur l’acier. Quand la tuyauterie commence, le local est déjà plein : nous montons donc les vannes, le filtre et les piquages sur un même châssis à l’extérieur du compartiment et posons l’ensemble d’un seul tenant, trous de boulons en correspondance et faces de brides d’équerre. Disposé ainsi, quelqu’un qui se tient devant atteint chaque volant.',
    'We set the valve groups out to keep the tank access clear, because the covers have to come off in service. Open ends are capped whenever work stops on a line, and the system is blanked at its boundaries for the pressure test. Each line is tagged to the drawing as it is finished.':
        'Nous disposons les ensembles de vannes de manière à dégager l’accès aux capacités, car les trappes doivent pouvoir être déposées en exploitation. Les extrémités ouvertes sont obturées dès que le travail s’arrête sur une ligne, et le circuit est bridé à ses limites pour l’épreuve en pression. Chaque ligne est repérée d’après le plan à mesure qu’elle est terminée.',
    'Resiliently mounted machinery moves, and the hull works at sea. Flexible hoses take that movement at the machine connections. On the runs, mechanical couplings take up misalignment, and we anchor and guide the pipe either side of them so the coupling is not left carrying the line.':
        'Une machine sur supports élastiques bouge, et la coque travaille en mer. Aux raccordements de la machine, des flexibles absorbent ce mouvement. Sur les lignes, des raccords mécaniques rattrapent le désalignement, et nous ancrons et guidons la tuyauterie de part et d’autre pour que le raccord ne se retrouve pas à porter la ligne.',
    'Resilient mounts on the machined seating.':
        'Supports élastiques sur l’assise usinée.',
    'The seating, with the mounts set and the first lines alongside.':
        'L’assise, supports posés et premières lignes le long.',
    'Valve and strainer group on the bulkhead.':
        'Ensemble vannes et filtre sur la cloison.',
    'Mechanical couplings on the large-bore runs.':
        'Raccords mécaniques sur les lignes de gros diamètre.',
    'Valve group around the tank access cover.':
        'Ensemble de vannes autour de la trappe de visite.',
    'Machined seating in an engine room with resilient mounts bolted down, studs and nuts set, and timber packing alongside':
        'Assise usinée en salle des machines avec supports élastiques boulonnés, goujons et écrous posés, et cales en bois à côté',
    'A row of resilient mounts along the machined seating, with the first pipe runs and capped flanges laid in beside them':
        'Une rangée de supports élastiques le long de l’assise usinée, avec les premières lignes et des brides obturées posées à côté',
    'Valve and strainer group made up on a frame against an engine room bulkhead, with globe valves, a basket strainer and capped branches':
        'Ensemble vannes et filtre préfabriqué sur châssis contre une cloison de salle des machines, avec robinets à soupape, filtre à panier et piquages obturés',
    'Large-bore pipe runs under a deckhead, with mechanical couplings on the vertical drop and anchors either side of them':
        'Lignes de gros diamètre sous plafond, avec raccords mécaniques sur la descente verticale et points fixes de part et d’autre',
    'Valve group set out around a bolted tank access cover, with the covers left clear and every open end capped':
        'Ensemble de vannes disposé autour d’une trappe de visite boulonnée, les trappes restant dégagées et chaque extrémité ouverte obturée',
    'Send the drawings or the scope and we will come back with a price and crew dates. If it is a yard slot, tell us the window.':
        'Envoyez les plans ou le périmètre et nous reviendrons avec un prix et des dates d’équipe. S’il s’agit d’un créneau au chantier naval, précisez-nous la fenêtre.',
    'Send us the drawings':
        'Envoyez-nous les plans',
    '<span class="case-num">01</span> <span class="case-kicker">Mechanical installation and piping · Shipbuilding</span>':
        '<span class="case-num">01</span> <span class="case-kicker">Montage mécanique et tuyauterie · Construction navale</span>',
    '<span class="eyebrow">Next project</span> <span class="case-next-t">Engine room piping and machinery installation</span> <span class="arr" aria-hidden="true">&#8593;</span>':
        '<span class="eyebrow">Chantier suivant</span> <span class="case-next-t">Tuyauterie et montage des machines en salle des machines</span> <span class="arr" aria-hidden="true">&#8593;</span>',

    # --- case: foundations, penetrations and equipment installation -----
    'Foundations, penetrations and equipment installation':
        'Berceaux, traversées de cloison et montage des équipements',
    'Foundations, penetrations and equipment installation — ALPROJECTS Group':
        'Berceaux, traversées de cloison et montage des équipements — ALPROJECTS Group',
    'Steel fabrication and mechanical installation · Shipbuilding':
        'Fabrication acier et montage mécanique · Construction navale',
    'Project &middot; Steel fabrication and mechanical installation · Shipbuilding':
        'Chantier &middot; Fabrication acier et montage mécanique · Construction navale',
    'Vessel under construction, machinery and tank spaces':
        'Navire en construction, locaux machines et capacités',
    'The steel that has to be in place before the equipment. We made and set the seats and frames, cut the openings and welded in the bulkhead penetrations, and fitted the supports for the cable and pipe routes.':
        'L’acier qui doit être en place avant les équipements. Nous avons fabriqué et posé les berceaux et les châssis, découpé les ouvertures et soudé les traversées de cloison, et monté les supports des cheminements de câbles et de tuyauteries.',
    'Frames and seats are fabricated to the drawing, then set to the steel that is actually there. We land the frame on the marked position, check it for position and level, and weld it down once it sits right. A unit light enough to be landed with its frame goes in first. Anything heavier goes on after the frame is welded down, and stays under cover until commissioning.':
        'Les châssis et les berceaux sont fabriqués d’après le plan, puis ajustés à l’acier réellement en place. Nous posons le châssis sur la position tracée, contrôlons sa position et son niveau, et le soudons dès qu’il porte correctement. Un ensemble assez léger pour être descendu avec son châssis entre en premier. Tout ce qui est plus lourd vient après le soudage du châssis et reste sous bâche jusqu’à la mise en service.',
    'We mark the opening from the ring that goes into it, cut it, and prepare the edge before the ring is offered up. That way the root gap is even the whole way round. On a watertight boundary the gap is what the weld has to close, and an uneven one shows up at the tightness test.':
        'Nous traçons l’ouverture d’après la virole qui doit y prendre place, la découpons et préparons le bord avant de présenter la virole. Le jeu à la racine est ainsi régulier sur tout le pourtour. Sur un cloisonnement étanche, c’est ce jeu que la soudure doit refermer, et une irrégularité se voit à l’essai d’étanchéité.',
    'The ring is worked from both sides at once. One fitter checks the alignment inside the opening while another dresses the prep outside, and we tack in a balanced sequence so the ring does not pull as it is welded out.':
        'La virole est travaillée des deux côtés à la fois. Un monteur contrôle l’alignement à l’intérieur de l’ouverture pendant qu’un autre reprend le chanfrein à l’extérieur, et nous pointons selon une séquence équilibrée pour que la virole ne tire pas au fur et à mesure du soudage.',
    'Supports for cable and pipe routes go on before the boundary is closed in. We set the brackets clear of the insulation and the pins that hold it, so the tray runs at its own height and nothing has to be cut back when the lining goes on.':
        'Les supports des cheminements de câbles et de tuyauteries sont posés avant la fermeture du cloisonnement. Nous plaçons les consoles à l’écart de l’isolation et des goujons qui la tiennent, pour que le chemin de câbles reste à sa propre hauteur et que rien n’ait à être recoupé lors de la pose de l’habillage.',
    'Coming down on the marked position.':
        'Descente sur la position tracée.',
    'The unit on its frame, covered until commissioning.':
        'L’ensemble sur son châssis, sous bâche jusqu’à la mise en service.',
    'The opening cut, and the penetration piece ready to go in.':
        'L’ouverture découpée et la pièce de traversée prête à être posée.',
    'Dressing the prep before the penetration is welded out.':
        'Reprise du chanfrein avant le soudage de la traversée.',
    'Cable tray supports on an insulated boundary.':
        'Supports de chemin de câbles sur un cloisonnement isolé.',
    'Cylindrical steel unit in a fabricated frame, suspended on chain hoists over its marked position on the deck of a vessel under construction':
        'Ensemble cylindrique en acier dans un châssis fabriqué, suspendu à des palans à chaîne au-dessus de sa position tracée sur le pont d’un navire en construction',
    'Machinery unit under protective covers on a fabricated steel frame in a shipyard hall':
        'Ensemble mécanique sous bâches de protection sur un châssis acier fabriqué, dans un hall de chantier naval',
    'Circular opening cut in a bulkhead, with the penetration piece standing ready on the deck beside it':
        'Ouverture circulaire découpée dans une cloison, la pièce de traversée posée prête sur le pont à côté',
    'Two fitters at a bulkhead penetration, one checking alignment inside the opening while the other dresses the edge with a grinder':
        'Deux monteurs à une traversée de cloison, l’un contrôlant l’alignement à l’intérieur de l’ouverture pendant que l’autre reprend le bord à la meuleuse',
    'Cable trays and brackets fitted to an insulated bulkhead, with insulation pins welded across the plate':
        'Chemins de câbles et consoles posés sur une cloison isolée, avec des goujons d’isolation soudés sur toute la tôle',
    '<span class="case-num">02</span> <span class="case-kicker">Steel fabrication and mechanical installation · Shipbuilding</span>':
        '<span class="case-num">02</span> <span class="case-kicker">Fabrication acier et montage mécanique · Construction navale</span>',
    '<span class="eyebrow">Next project</span> <span class="case-next-t">Foundations, penetrations and equipment installation</span> <span class="arr" aria-hidden="true">&#8593;</span>':
        '<span class="eyebrow">Chantier suivant</span> <span class="case-next-t">Berceaux, traversées de cloison et montage des équipements</span> <span class="arr" aria-hidden="true">&#8593;</span>',
    '<span class="case-num">03</span> <span class="case-kicker">Shop fabrication and welding</span>':
        '<span class="case-num">03</span> <span class="case-kicker">Fabrication et soudage en atelier</span>',
    '<span class="case-num">04</span> <span class="case-kicker">Mechanical installation and welding &middot; tank farm</span>':
        '<span class="case-num">04</span> <span class="case-kicker">Montage mécanique et soudage &middot; parc de stockage</span>',
    '<span class="case-num">05</span> <span class="case-kicker">Mechanical installation and welding</span>':
        '<span class="case-num">05</span> <span class="case-kicker">Montage mécanique et soudage</span>',
    '<span class="case-num">06</span> <span class="case-kicker">Mechanical installation</span>':
        '<span class="case-num">06</span> <span class="case-kicker">Montage mécanique</span>',
    'The steel that has to be in place before the equipment. We made and set the seats and frames, cut the openings and welded in the bulkhead penetrations, and fitted the supports for the cable and...':
        'L’acier qui doit être en place avant les équipements. Nous avons fabriqué et posé les berceaux et les châssis, découpé les ouvertures et soudé les traversées de cloison, et monté les supports des...',

    # --- case: large-bore pipe replacement -------------------------------
    'Large-bore pipe replacement':
        'Remplacement de tuyauterie de gros diamètre',
    'Large-bore pipe replacement — ALPROJECTS Group':
        'Remplacement de tuyauterie de gros diamètre — ALPROJECTS Group',
    'Mechanical installation and welding · Industrial':
        'Montage mécanique et soudage · Industrie',
    'Project &middot; Mechanical installation and welding · Industrial':
        'Chantier &middot; Montage mécanique et soudage · Industrie',
    'Existing plant, scaffolded work fronts':
        'Installation existante, fronts de travail échafaudés',
    'Large-bore pipework replaced inside an existing plant. We prefabricated the spools, rigged them into position on chain hoists off the plant steel, and welded them in place.':
        'Remplacement de tuyauterie de gros diamètre dans une installation existante. Nous avons préfabriqué les tronçons, les avons mis en place sur des palans à chaîne accrochés à la charpente de l’installation, et les avons soudés en place.',
    'We put the covers down before anything hot starts — blankets under the work front, sheeting across what is behind it, and the grating below closed off. A spark that goes through the grating lands on whatever is on the level under you.':
        'Les protections sont posées avant tout travail à chaud — couvertures sous le front de travail, bâches sur tout ce qui se trouve derrière, et le caillebotis en dessous obturé. Une étincelle qui passe à travers le caillebotis retombe sur ce qui se trouve au niveau inférieur.',
    'Branches and stubs go on at floor level, where the piece can be turned and the weld is made in the flat position. The spool goes up as one piece with its openings already in it. Every branch done down here is one less weld made overhead.':
        'Les piquages et les embouts sont soudés au sol, où la pièce peut être tournée et la soudure exécutée à plat. Le tronçon monte d’une seule pièce, ses ouvertures déjà réalisées. Chaque piquage fait en bas est une soudure de moins à faire en plafond.',
    'There is no crane over the work front, so the load comes off the plant steel. We agree the attachment points with the plant first, then hang beam clamps and chain hoists at each end and walk the spool into line by hand.':
        'Il n’y a pas de pont roulant au-dessus du front de travail : la charge est donc reprise sur la charpente de l’installation. Nous validons d’abord les points d’accrochage avec l’exploitant, puis suspendons des pinces à poutre et des palans à chaîne à chaque extrémité et amenons le tronçon dans l’axe à la main.',
    'Fit-up decides the joint. We set the gap and hold it the whole way round before an arc is struck, and the root goes in first — in this frame it is part way round, with the gap above still open. The joint is cleaned and checked before the fill and cap go on.':
        'L’accostage décide du joint. Nous réglons le jeu et le maintenons sur tout le pourtour avant d’amorcer, et la passe de racine passe en premier — sur cette image, elle est faite sur une partie du tour, le jeu au-dessus étant encore ouvert. Le joint est nettoyé et contrôlé avant les passes de remplissage et de finition.',
    'The new run in place.':
        'La nouvelle ligne en place.',
    'The work front covered before hot work starts.':
        'Le front de travail protégé avant le début des travaux à chaud.',
    'Branch and stub welded on before the spool goes up.':
        'Piquage et embout soudés avant le levage du tronçon.',
    'Beam clamps and chain hoists off the existing steel.':
        'Pinces à poutre et palans à chaîne sur la charpente existante.',
    'The root run part way round the joint.':
        'La passe de racine exécutée sur une partie du tour du joint.',
    'New large-bore pipework and a fabricated bend installed among existing lines and ducts inside an industrial plant':
        'Nouvelle tuyauterie de gros diamètre et coude fabriqué, posés entre des lignes et des gaines existantes dans une installation industrielle',
    'Protective sheeting and welding blankets laid over plant grating around a pipe spool standing ready for installation':
        'Bâches de protection et couvertures de soudage étalées sur le caillebotis autour d’un tronçon de tuyauterie prêt à être posé',
    'Prefabricated pipe bend with a welded branch and stub, standing on timber on plant grating':
        'Coude de tuyauterie préfabriqué avec piquage et embout soudés, posé sur des cales en bois sur le caillebotis',
    'Two beam clamps and chain hoists rigged from overhead steel, taking the weight of a large-bore pipe':
        'Deux pinces à poutre et leurs palans à chaîne accrochés à la charpente en hauteur, reprenant le poids d’un tuyau de gros diamètre',
    'Close-up of a pipe butt joint with an even root gap and the root run part way round':
        'Gros plan d’un joint bout à bout avec un jeu à la racine régulier et la passe de racine exécutée sur une partie du tour',
    '<span class="case-num">03</span> <span class="case-kicker">Mechanical installation and welding · Industrial</span>':
        '<span class="case-num">03</span> <span class="case-kicker">Montage mécanique et soudage · Industrie</span>',
    '<span class="eyebrow">Next project</span> <span class="case-next-t">Large-bore pipe replacement</span> <span class="arr" aria-hidden="true">&#8593;</span>':
        '<span class="eyebrow">Chantier suivant</span> <span class="case-next-t">Remplacement de tuyauterie de gros diamètre</span> <span class="arr" aria-hidden="true">&#8593;</span>',
    '<span class="case-num">04</span> <span class="case-kicker">Shop fabrication and welding</span>':
        '<span class="case-num">04</span> <span class="case-kicker">Fabrication et soudage en atelier</span>',
    '<span class="case-num">05</span> <span class="case-kicker">Mechanical installation and welding &middot; tank farm</span>':
        '<span class="case-num">05</span> <span class="case-kicker">Montage mécanique et soudage &middot; parc de stockage</span>',
    '<span class="case-num">06</span> <span class="case-kicker">Mechanical installation and welding</span>':
        '<span class="case-num">06</span> <span class="case-kicker">Montage mécanique et soudage</span>',
    '<span class="case-num">07</span> <span class="case-kicker">Mechanical installation</span>':
        '<span class="case-num">07</span> <span class="case-kicker">Montage mécanique</span>',

    # --- case: grate bar replacement -------------------------------------
    'Grate bar replacement':
        'Remplacement des barreaux de grille',
    'Grate bar replacement — ALPROJECTS Group':
        'Remplacement des barreaux de grille — ALPROJECTS Group',
    'Mechanical maintenance · Waste to energy':
        'Maintenance mécanique · Valorisation énergétique des déchets',
    'Project &middot; Mechanical maintenance · Waste to energy':
        'Chantier &middot; Maintenance mécanique · Valorisation énergétique des déchets',
    'Waste-to-energy plant, furnace during outage':
        'Usine de valorisation énergétique, foyer pendant l’arrêt de tranche',
    'Grate bars replaced inside the furnace of a waste-to-energy plant during the outage. The old bars came out one row at a time, cut free where they were seized, and the new ones went back set to the specified gap.':
        'Remplacement des barreaux de grille dans le foyer d’une usine de valorisation énergétique des déchets pendant l’arrêt de tranche. Les anciens barreaux sont sortis rangée par rangée, découpés là où ils étaient grippés, et les nouveaux sont remontés au jeu prescrit.',
    'How it was done':
        'Le déroulement de l’intervention',
    'The furnace is cold by the time we go in, but it is not clean. Everything inside is coated in fly ash and combustion residue, so the crew works in disposable coveralls and P3 respirators, and the suits come off at the door. Entry is under permit, with the space ventilated and the atmosphere monitored.':
        'Quand nous entrons, le foyer est froid mais pas propre. Tout y est couvert de cendres volantes et de résidus de combustion : l’équipe travaille donc en combinaisons jetables et masques P3, et les combinaisons restent à la porte. L’entrée se fait sous permis, l’espace ventilé et l’atmosphère surveillée.',
    'The bars sit in rows across the grate, and after a full run most of them are seized in place. They come out one row at a time — cut free where they will not move, lifted out by hand and stacked. The new ones go back set to the gap the maker specifies, because that gap is how the primary air reaches the bed.':
        'Les barreaux sont disposés en rangées sur la grille et, après une campagne complète, la plupart sont grippés. Ils sortent rangée par rangée — découpés là où ils ne bougent plus, dégagés à la main et empilés. Les neufs sont remontés au jeu prescrit par le constructeur, car c’est par ce jeu que l’air primaire atteint le lit de combustible.',
    'Cutting seized steel free.':
        'Découpe de l’acier grippé.',
    'Disposable coveralls and P3 respirators.':
        'Combinaisons jetables et masques P3.',
    'Old bars out, one row at a time.':
        'Anciens barreaux déposés, rangée par rangée.',
    'Worker in disposable coveralls and respirator cutting seized steel free with an oxy-fuel torch at the grate, with removed grate blocks in the foreground':
        'Ouvrier en combinaison jetable et masque découpant à la grille de l’acier grippé au chalumeau oxycoupeur, blocs de grille déposés au premier plan',
    'Worker in a hard hat, goggles and P3 respirator inside the cold furnace of a waste-to-energy plant':
        'Ouvrier en casque, lunettes et masque P3 dans le foyer froid d’une usine de valorisation énergétique des déchets',
    'Two workers in disposable coveralls levering an old grate bar out of its row, with removed bars stacked behind them':
        'Deux ouvriers en combinaisons jetables extrayant au levier un ancien barreau de sa rangée, barreaux déposés empilés derrière eux',
    'Send us the scope and we will come back with a price and crew dates. If it is an outage, tell us the window.':
        'Envoyez-nous le périmètre et nous reviendrons avec un prix et des dates d’équipe. S’il s’agit d’un arrêt de tranche, précisez-nous la fenêtre.',
    'Eight scopes, photographed as they were built.':
        'Huit chantiers, photographiés pendant leur exécution.',
    '<span class="case-num">04</span> <span class="case-kicker">Mechanical maintenance · Waste to energy</span>':
        '<span class="case-num">04</span> <span class="case-kicker">Maintenance mécanique · Valorisation énergétique des déchets</span>',
    '<span class="eyebrow">Next project</span> <span class="case-next-t">Grate bar replacement</span> <span class="arr" aria-hidden="true">&#8593;</span>':
        '<span class="eyebrow">Chantier suivant</span> <span class="case-next-t">Remplacement des barreaux de grille</span> <span class="arr" aria-hidden="true">&#8593;</span>',
    '<span class="case-num">05</span> <span class="case-kicker">Shop fabrication and welding</span>':
        '<span class="case-num">05</span> <span class="case-kicker">Fabrication et soudage en atelier</span>',
    '<span class="case-num">06</span> <span class="case-kicker">Mechanical installation and welding &middot; tank farm</span>':
        '<span class="case-num">06</span> <span class="case-kicker">Montage mécanique et soudage &middot; parc de stockage</span>',
    '<span class="case-num">07</span> <span class="case-kicker">Mechanical installation and welding</span>':
        '<span class="case-num">07</span> <span class="case-kicker">Montage mécanique et soudage</span>',
    '<span class="case-num">08</span> <span class="case-kicker">Mechanical installation</span>':
        '<span class="case-num">08</span> <span class="case-kicker">Montage mécanique</span>',
    'Grate bars replaced inside the furnace of a waste-to-energy plant during the outage. The old bars came out one row at a time, cut free where they were seized, and the new ones went back set to the...':
        'Remplacement des barreaux de grille dans le foyer d’une usine de valorisation énergétique des déchets pendant l’arrêt de tranche. Les anciens barreaux sont sortis rangée par rangée, découpés là où...',

    # --- case: offshore rope access welding (draft until consent) ---
    'Offshore rope access welding':
        'Soudage sur cordes en offshore',
    'Offshore rope access welding — ALPROJECTS Group':
        'Soudage sur cordes en offshore — ALPROJECTS Group',
    'Welding and rope access · Offshore':
        'Soudage et travaux sur cordes · Offshore',
    'Project &middot; Welding and rope access · Offshore':
        'Chantier &middot; Soudage et travaux sur cordes · Offshore',
    'Offshore platform, Northern Europe':
        'Plateforme offshore, Europe du Nord',
    'Welding on the outside of an offshore platform, carried out on rope access. There is no scaffold and no basket over the side, so the welder reaches the joint on ropes and works from the harness.':
        'Soudage sur la face extérieure d’une plateforme offshore, réalisé en travaux sur cordes. Il n’y a ni échafaudage ni nacelle par-dessus bord : le soudeur rejoint le joint sur cordes et travaille depuis son harnais.',
    'The platform has no quay and no road. Crew, tools and consumables arrive by vessel or helicopter and stay for the shift, and the working window is set by wind and sea state rather than by the programme.':
        'La plateforme n’a ni quai ni route. L’équipe, l’outillage et les consommables arrivent par navire ou par hélicoptère et restent pour le poste, et la fenêtre de travail est fixée par le vent et l’état de la mer, non par le planning.',
    'Welding is carried out from the harness, on a working line and a backup rigged from the structure above, with the team working in pairs. The joint is prepared before the arc is struck and completed in short runs. The return clamp is placed on the work close to the joint — over water the return path is part of the safety case, not a detail.':
        'Le soudage se fait depuis le harnais, sur une corde de travail et une corde de sécurité amarrées à la structure au-dessus, et toujours en binôme. Le joint est préparé avant l’amorçage et exécuté en passes courtes. La pince de masse est posée sur la pièce près du joint — au-dessus de l’eau, le circuit de retour fait partie de la démonstration de sécurité, pas des détails.',
    'Rope access over open water.':
        'Travaux sur cordes au-dessus de l’eau libre.',
    'Access by vessel or helicopter only.':
        'Accès uniquement par navire ou hélicoptère.',
    'Welding carried out from the harness.':
        'Soudage réalisé depuis le harnais.',
    'Rope access technician suspended in a harness on the outside of an offshore platform, with wind turbines on the horizon':
        'Technicien cordiste suspendu dans son harnais sur la face extérieure d’une plateforme offshore, éoliennes à l’horizon',
    'Side of an offshore platform above the sea, with wind turbines in low cloud on the horizon':
        'Flanc d’une plateforme offshore au-dessus de la mer, éoliennes dans les nuages bas à l’horizon',
    'Two rope access technicians suspended on twin ropes at a yellow structure on an offshore platform, one wearing a welding helmet, with cables run down from the deck above':
        'Deux techniciens cordistes suspendus sur cordes jumelées à une structure jaune d’une plateforme offshore, l’un portant un casque de soudage, les câbles descendus depuis le pont au-dessus',
    'Send us the scope and we will come back with a price and crew dates. For offshore work tell us the access, the vessel and the weather window.':
        'Envoyez-nous le périmètre et nous reviendrons avec un prix et des dates d’équipe. Pour des travaux offshore, précisez l’accès, le navire et la fenêtre météo.',
    'Nine scopes, photographed as they were built.':
        'Neuf chantiers, photographiés pendant leur exécution.',
    '<span class="case-num">05</span> <span class="case-kicker">Welding and rope access · Offshore</span>':
        '<span class="case-num">05</span> <span class="case-kicker">Soudage et travaux sur cordes · Offshore</span>',
    '<span class="eyebrow">Next project</span> <span class="case-next-t">Offshore rope access welding</span> <span class="arr" aria-hidden="true">&#8593;</span>':
        '<span class="eyebrow">Chantier suivant</span> <span class="case-next-t">Soudage sur cordes en offshore</span> <span class="arr" aria-hidden="true">&#8593;</span>',
    '<span class="case-num">06</span> <span class="case-kicker">Shop fabrication and welding</span>':
        '<span class="case-num">06</span> <span class="case-kicker">Fabrication et soudage en atelier</span>',
    '<span class="case-num">07</span> <span class="case-kicker">Mechanical installation and welding &middot; tank farm</span>':
        '<span class="case-num">07</span> <span class="case-kicker">Montage mécanique et soudage &middot; parc de stockage</span>',
    '<span class="case-num">08</span> <span class="case-kicker">Mechanical installation and welding</span>':
        '<span class="case-num">08</span> <span class="case-kicker">Montage mécanique et soudage</span>',
    '<span class="case-num">09</span> <span class="case-kicker">Mechanical installation</span>':
        '<span class="case-num">09</span> <span class="case-kicker">Montage mécanique</span>',

    # --- case: fan replacement and duct adaptation ------------------
    'Fan replacement and duct adaptation':
        'Remplacement d’un ventilateur et adaptation des gaines',
    'Fan replacement and duct adaptation — ALPROJECTS Group':
        'Remplacement d’un ventilateur et adaptation des gaines — ALPROJECTS Group',
    'Existing plant, outdoor process platform':
        'Installation existante, plateforme de procédé en extérieur',
    'An extraction fan replaced on a process platform. The ducting that was already there did not suit the new unit, so we cut it back, made the transition pieces to fit, and connected the fan on both sides.':
        'Remplacement d’un ventilateur d’extraction sur une plateforme de procédé. Les gaines en place ne convenaient pas au nouvel appareil : nous les avons recoupées, fabriqué les pièces de transition sur mesure et raccordé le ventilateur des deux côtés.',
    'The fan comes to site as one assembly — casing, impeller, motor and base frame together. What decides the job is not the fan itself but its connection dimensions: the inlet, the outlet and the bolt pattern under the frame. On a replacement they rarely match what is already there, and here they did not.':
        'Le ventilateur arrive sur site en un seul ensemble — volute, roue, moteur et châssis de base réunis. Ce qui décide du chantier n’est pas l’appareil lui-même mais ses cotes de raccordement : l’aspiration, le refoulement et les entraxes de fixation sous le châssis. Sur un remplacement, elles correspondent rarement à l’existant, et ici elles ne correspondaient pas.',
    'The fan is landed on its base and stays on the sling until it is fixed down. The old frame did not leave the seats where the new one needs them, so they are made to suit the new footprint before anything is bolted — a fan sitting on a base that is out carries that error straight into its bearings. Anything hot happens over a blanket, with an extinguisher at the work front.':
        'Le ventilateur est reposé sur son socle et reste sur l’élingue jusqu’à sa fixation. L’ancien châssis n’a pas laissé les appuis là où le nouveau les demande : ils sont donc reprises à l’emprise du nouveau avant tout boulonnage — un ventilateur posé sur un socle faux transmet ce défaut directement à ses paliers. Tout travail à chaud se fait au-dessus d’une couverture, extincteur au front de travail.',
    'The inlet side is where the old ducting has to give. We take the weight of the duct on a sling first, so nothing is hanging on the joint once it is open, then cut it back and set a stub into it to suit the fan inlet. The fan drawing gives the size; where the stub lands is measured on the duct itself.':
        'C’est du côté aspiration que la gaine existante doit céder. Nous reprenons d’abord son poids sur une élingue, pour que rien ne pende sur l’assemblage une fois ouvert, puis nous la recoupons et y montons une manchette adaptée à l’aspiration du ventilateur. Le plan du ventilateur donne la cote ; l’emplacement de la manchette se relève sur la gaine elle-même.',
    'The outlet goes up into the existing stack, and the two do not meet on their own. We make the transition, offer it up with the fan standing on its base, and mark it in position. Nothing is finish-welded until both ends have been proved against the openings they have to land on.':
        'Le refoulement monte dans la cheminée existante, et les deux ne se rejoignent pas d’eux-mêmes. Nous fabriquons la pièce de transition, la présentons ventilateur posé sur son socle, et la traçons en place. Rien n’est soudé définitivement avant que les deux extrémités n’aient été vérifiées contre les ouvertures sur lesquelles elles doivent tomber.',
    'Both connections finish on something flexible — a sleeve at the inlet and a bolted expansion joint at the outlet. The frame itself stands on anti-vibration mounts, so the machine is free to move a little; these two joints are what keep that movement out of the ducting, and they let the flanges sit a fraction out of line without loading either side. With those in, the adapter welds are dressed back and the expansion joint is bolted up all round.':
        'Les deux raccordements se terminent sur du souple — une manchette à l’aspiration et un compensateur boulonné au refoulement. Le châssis lui-même repose sur des plots antivibratoires : la machine peut donc bouger un peu ; ce sont ces deux liaisons qui empêchent ce mouvement d’atteindre les gaines, et elles laissent les brides se placer légèrement de travers sans charger aucun des deux côtés. Une fois en place, les soudures des pièces de transition sont reprises et le compensateur est boulonné sur tout le pourtour.',
    'The new fan, connected on both sides.':
        'Le nouveau ventilateur, raccordé des deux côtés.',
    'The new unit as delivered.':
        'L’appareil neuf tel que livré.',
    'Base work before the fan is bolted down.':
        'Travaux sur le socle avant boulonnage du ventilateur.',
    'The duct carried on a sling while the joint is open.':
        'La gaine reprise sur une élingue pendant que l’assemblage est ouvert.',
    'The outlet transition offered up in position.':
        'La pièce de transition du refoulement présentée en place.',
    'The expansion joint between fan and stack.':
        'Le compensateur entre le ventilateur et la cheminée.',
    'New blue centrifugal fan installed on a steel base on an outdoor grating platform, its outlet connected through an expansion joint to the existing painted exhaust stack':
        'Ventilateur centrifuge bleu neuf installé sur un socle acier sur une plateforme caillebotis extérieure, son refoulement raccordé par un compensateur à la cheminée d’extraction existante peinte',
    'New centrifugal fan and motor on a pallet as delivered to site, before installation':
        'Ventilateur centrifuge neuf et son moteur sur palette tels que livrés sur site, avant montage',
    'Worker at the base of the newly landed fan on the grating platform, with lifting slings, tools and a fire extinguisher laid out beside him':
        'Ouvrier au pied du ventilateur fraîchement posé sur la plateforme caillebotis, élingues, outillage et extincteur disposés à côté de lui',
    'Existing rectangular duct supported on a round sling while its open end is connected to the inlet of the new fan':
        'Gaine rectangulaire existante reprise sur une élingue ronde pendant que son extrémité ouverte est raccordée à l’aspiration du nouveau ventilateur',
    'New fan standing on its base with the outlet transition piece offered up under the existing stack':
        'Ventilateur neuf posé sur son socle, la pièce de transition du refoulement présentée sous la cheminée existante',
    'Fabric expansion joint with tie rods bolted between the fan outlet and the adapted exhaust duct above it':
        'Compensateur en tissu avec tirants, boulonné entre le refoulement du ventilateur et la gaine d’extraction adaptée au-dessus',
    '<span class="case-num">05</span> <span class="case-kicker">Mechanical installation and welding · Industrial</span>':
        '<span class="case-num">05</span> <span class="case-kicker">Montage mécanique et soudage · Industrie</span>',
    '<span class="eyebrow">Next project</span> <span class="case-next-t">Fan replacement and duct adaptation</span> <span class="arr" aria-hidden="true">&#8593;</span>':
        '<span class="eyebrow">Chantier suivant</span> <span class="case-next-t">Remplacement d’un ventilateur et adaptation des gaines</span> <span class="arr" aria-hidden="true">&#8593;</span>',
    'An extraction fan replaced on a process platform. The ducting that was already there did not suit the new unit, so we cut it back, made the transition pieces to fit, and connected the fan on both...':
        'Remplacement d’un ventilateur d’extraction sur une plateforme de procédé. Les gaines en place ne convenaient pas au nouvel appareil : nous les avons recoupées, fabriqué les pièces de transition...',
}
