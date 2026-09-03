# -*- coding: utf-8 -*-
"""
German. Keys are the English source exactly as built -- see tools/i18n.py.

TERMINOLOGY
    non-destructive testing  -> zerstoerungsfreie Pruefung (ZfP)
    rope access              -> Seilzugangstechnik      (IRATA's own term)
    pipe fitter              -> Rohrleitungsmonteur
    WPS / WPQR               -> Schweissanweisung / Schweissverfahrenspruefung
    root pass                -> Wurzellage
    penetrant testing        -> Farbeindringpruefung
    undercut                 -> Einbrandkerbe
    scope (of work)          -> Leistungsumfang
    turnaround / shutdown    -> Grossstillstand / Anlagenstillstand
    handover dossier         -> Abnahmedokumentation
    class surveyor           -> Besichtiger der Klassifikationsgesellschaft
    "Offshore" is used untranslated in German industry and is left alone.

    German is the longest of the four: see the :lang(de) rules in css/style.css
    for the measure and hyphenation this needs.

WARNING: Have a native German speaker in the market review the services,
   sectors and certification copy before go-live, and a lawyer review the
   privacy policy.
"""

S = {
    '3 photographs, 2 stages':
        '3 Aufnahmen, 2 Arbeitsschritte',
    '5 photographs, 4 stages':
        '5 Aufnahmen, 4 Arbeitsschritte',
    '6 photographs, 5 stages':
        '6 Aufnahmen, 5 Arbeitsschritte',
    '<span class="case-num">02</span> <span class="case-kicker">Shop fabrication and welding</span>':
        '<span class="case-num">02</span> <span class="case-kicker">Fertigung und Schweißen in der Werkstatt</span>',
    '<span class="case-num">03</span> <span class="case-kicker">Mechanical installation and welding &middot; tank farm</span>':
        '<span class="case-num">03</span> <span class="case-kicker">Mechanische Montage und Schweißen &middot; Tanklager</span>',
    '<span class="case-num">04</span> <span class="case-kicker">Mechanical installation and welding</span>':
        '<span class="case-num">04</span> <span class="case-kicker">Mechanische Montage und Schweißen</span>',
    '<span class="case-num">05</span> <span class="case-kicker">Mechanical installation</span>':
        '<span class="case-num">05</span> <span class="case-kicker">Mechanische Montage</span>',
    '<span class="slide-label">Stage</span> <span class="slide-count">01 / 04</span>':
        '<span class="slide-label">Arbeitsschritt</span> <span class="slide-count">01 / 04</span>',
    '<span class="slide-label">Stage</span> <span class="slide-count">02 / 04</span>':
        '<span class="slide-label">Arbeitsschritt</span> <span class="slide-count">02 / 04</span>',
    '<span class="slide-label">Stage</span> <span class="slide-count">03 / 04</span>':
        '<span class="slide-label">Arbeitsschritt</span> <span class="slide-count">03 / 04</span>',
    '<span class="slide-label">Stage</span> <span class="slide-count">04 / 04</span>':
        '<span class="slide-label">Arbeitsschritt</span> <span class="slide-count">04 / 04</span>',
    '<span>© 2019–2026 ALPROJECTS GROUP. All rights reserved.</span> <span class="legal-ids">Company code 305137109 &middot; VAT LT100012753216</span> <a class="made-by" href="https://aldystudio.com" target="_blank" rel="noopener">Made by <b>ALDY</b></a>':
        '<span>© 2019–2026 ALPROJECTS GROUP. Alle Rechte vorbehalten.</span> <span class="legal-ids">Firmencode 305137109 &middot; USt-IdNr. LT100012753216</span> <a class="made-by" href="https://aldystudio.com" target="_blank" rel="noopener">Umgesetzt von <b>ALDY</b></a>',
    'Company code 305137109 &middot; VAT LT100012753216':
        'Firmencode 305137109 &middot; USt-IdNr. LT100012753216',
    '<b>ISO 9001 &middot; 14001 &middot; 45001</b><span>Certified by DNV</span>':
        '<b>ISO 9001 &middot; 14001 &middot; 45001</b><span>Zertifiziert durch DNV</span>',
    '<b>300+</b><span>Specialists on the books</span>':
        '<b>300+</b><span>Fachkr\u00e4fte im Bestand</span>',
    '<b>6 countries</b><span>9 project bases</span>':
        '<b>6 L\u00e4nder</b><span>9 Projektstandorte</span>',
    '<b>Strongest in Lithuania</b><span>Creditinfo, 2025&ndash;2026</span>':
        '<b>St\u00e4rkstes Unternehmen Litauens</b><span>Creditinfo, 2025&ndash;2026</span>',
    'Key facts':
        'Kennzahlen',
    'Next step':
        'Nächster Schritt',
    'Book a 30-minute call':
        '30 Minuten buchen',
    'Direct contact':
        'Direkter Kontakt',
    '<span class="cta-direct-label">Phone</span><a href="tel:+37063663744">+370 636 63 744</a>':
        '<span class="cta-direct-label">Telefon</span><a href="tel:+37063663744">+370 636 63 744</a>',
    '<span class="cta-direct-label">WhatsApp</span><a href="https://wa.me/37063663744" target="_blank" rel="noopener">+370 636 63 744</a>':
        '<span class="cta-direct-label">WhatsApp</span><a href="https://wa.me/37063663744" target="_blank" rel="noopener">+370 636 63 744</a>',
    'GWO':
        'GWO',
    'Home':
        'Startseite',
    'News':
        'Aktuelles',
    'Apply':
        'Bewerben',
    'Award':
        'Auszeichnung',
    'Close':
        'Schließen',
    'Email':
        'E-Mail',
    'Legal':
        'Rechtliches',
    'Other':
        'Andere',
    'Phone':
        'Telefon',
    'Scale':
        'Größe',
    'Marine':
        'Schiffbau',
    'NDT UT':
        'ZfP UT',
    'NDT VT':
        'ZfP VT',
    'Norway':
        'Norwegen',
    'Poland':
        'Polen',
    'Seafox':
        'Seafox',
    'Sector':
        'Branche',
    'Select':
        'Auswählen',
    'Belgium':
        'Belgien',
    'Careers':
        'Karriere',
    'Company':
        'Unternehmen',
    'Denmark':
        'Dänemark',
    'General':
        'Allgemein',
    'Germany':
        'Deutschland',
    'Hamburg':
        'Hamburg',
    'Rigging':
        'Hebetechnik',
    'Rostock':
        'Rostock',
    'Sectors':
        'Branchen',
    'Welders':
        'Schweißer',
    'Ålesund':
        'Ålesund',
    'About Us':
        'Über uns',
    'All news':
        'Alle Meldungen',
    'Contacts':
        'Kontakt',
    'Email us':
        'Schreiben Sie uns',
    'Facebook':
        'Facebook',
    'IRATA L1':
        'IRATA L1',
    'IRATA L2':
        'IRATA L2',
    'IRATA L3':
        'IRATA L3',
    'ISO:9001':
        'ISO:9001',
    'LinkedIn':
        'LinkedIn',
    'Offshore':
        'Offshore',
    'Orkanger':
        'Orkanger',
    'Our news':
        'Aktuelles',
    'Position':
        'Position',
    'Projects':
        'Projekte',
    'Services':
        'Leistungen',
    'Countries':
        'Länder',
    'Frankfurt':
        'Frankfurt',
    'From site':
        'Von der Baustelle',
    'Full name':
        'Vollständiger Name',
    'ISO:14001':
        'ISO:14001',
    'ISO:45001':
        'ISO:45001',
    'Instagram':
        'Instagram',
    'Issued by':
        'Ausgestellt von',
    'Lithuania':
        'Litauen',
    'NDT PT/MT':
        'ZfP PT/MT',
    'Newcastle':
        'Newcastle',
    'Open menu':
        'Menü öffnen',
    'Read more':
        'Weiterlesen',
    'Subscribe':
        'Abonnieren',
    'VCA / SCC':
        'VCA / SCC',
    '1 location':
        '1 Standort',
    '7. Changes':
        '7. Änderungen',
    'Continuous':
        'Durchgehend',
    'Discipline':
        'Gewerk',
    'Hiring now':
        'Wir stellen ein',
    'Industrial':
        'Industrie',
    'Industries':
        'Branchen',
    'Newsletter':
        'Newsletter',
    'Our people':
        'Unser Team',
    'Renewables':
        'Erneuerbare Energien',
    'Talk to us':
        'Sprechen Sie uns an',
    'What we do':
        'Was wir tun',
    '2 locations':
        '2 Standorte',
    '3 locations':
        '3 Standorte',
    'Book a call':
        'Termin buchen',
    'Head office':
        'Hauptsitz',
    'Netherlands':
        'Niederlande',
    'Rope access':
        'Seilzugangstechnik',
    'Ship Repair':
        'Schiffsreparatur',
    'Ship repair':
        'Schiffsreparatur',
    '2 to 5 years':
        '2 bis 5 Jahre',
    '23 June 2026':
        '23. Juni 2026',
    'All services':
        'Alle Leistungen',
    'Certified to':
        'Zertifiziert nach',
    'Download PDF':
        'PDF herunterladen',
    'Electricians':
        'Elektriker',
    'Headquarters':
        'Hauptsitz',
    'Next service':
        'Nächste Leistung',
    'Our Services':
        'Unsere Leistungen',
    'Our services':
        'Unsere Leistungen',
    'Pipe Fitters':
        'Rohrleitungsmonteure',
    'Pipe Fitting':
        'Rohrleitungsbau',
    'Pipe fitting':
        'Rohrleitungsbau',
    'Shipbuilding':
        'Schiffbau',
    'What we need':
        'Was wir suchen',
    'Working from':
        'Standorte',
    '1. Who we are':
        '1. Wer wir sind',
    '5 to 10 years':
        '5 bis 10 Jahre',
    '<b>Norway</b>':
        '<b>Norwegen</b>',
    'Certification':
        'Zertifizierung',
    'Meet the team':
        'Das Team',
    'Open position':
        'Offene Stelle',
    'Our footprint':
        'Unsere Präsenz',
    'Project bases':
        'Projektstandorte',
    'Status: Ready':
        'Status: bereit',
    'Steel Fitters':
        'Stahlbaumonteure',
    'Thermo Fisher':
        'Thermo Fisher',
    'Welding (TIG)':
        'Schweißen (WIG)',
    'Where we work':
        'Wo wir arbeiten',
    '4. Legal basis':
        '4. Rechtsgrundlage',
    '6. Your rights':
        '6. Ihre Rechte',
    '<b>Belgium</b>':
        '<b>Belgien</b>',
    '<b>Germany</b>':
        '<b>Deutschland</b>',
    'Available from':
        'Verfügbar ab',
    'Certifications':
        'Zertifizierungen',
    'NDT Inspectors':
        'ZfP-Prüfer',
    'NDT inspection':
        'Zerstörungsfreie Prüfung',
    'Open positions':
        'Offene Stellen',
    'Our advantages':
        'Unsere Stärken',
    'Privacy Policy':
        'Datenschutzerklärung',
    'United Kingdom':
        'Vereinigtes Königreich',
    'View more news':
        'Weitere Meldungen',
    'Company Profile':
        'Unternehmensprofil',
    'Independent NDT':
        'Unabhängige ZfP',
    'MIG/MAG 131/135':
        'MIG/MAG 131/135',
    'Main navigation':
        'Hauptnavigation',
    'Next photograph':
        'Nächstes Foto',
    'On our own jobs':
        'Auf eigenen Baustellen',
    'Quality Control':
        'Qualitätskontrolle',
    'Skip to content':
        'Zum Inhalt springen',
    'Start a project':
        'Projekt starten',
    'What to include':
        'Was Sie uns senden sollten',
    'What we do here':
        'Was wir hier tun',
    'What we work on':
        'Woran wir arbeiten',
    'Working English':
        'Verhandlungssicheres Englisch',
    '<b>Lithuania</b>':
        '<b>Litauen</b>',
    'Back to homepage':
        'Zurück zur Startseite',
    'Creditinfo Group':
        'Creditinfo Group',
    'Enter Your Email':
        'E-Mail-Adresse eingeben',
    'Name and surname':
        'Vor- und Nachname',
    'Open application':
        'Initiativbewerbung',
    'Previous service':
        'Vorherige Leistung',
    'QA/QC Inspectors':
        'QA/QC-Prüfer',
    'See our projects':
        'Unsere Projekte',
    'Send application':
        'Bewerbung senden',
    'Site supervision':
        'Bauaufsicht',
    'Welding Services':
        'Schweißtechnik',
    'Welding services':
        'Schweißtechnik',
    '3D Laser Scanning':
        '3D-Laserscanning',
    '3D laser scanning':
        '3D-Laserscanning',
    'Company documents':
        'Unternehmensunterlagen',
    'Less than 2 years':
        'Weniger als 2 Jahre',
    'Mobile navigation':
        'Mobile Navigation',
    'Mode: Engineering':
        'Modus: Engineering',
    'Open in browser <span class="arr">&#8593;</span>':
        'Im Browser öffnen <span class="arr">&#8593;</span>',
    'Open the calendar':
        'Kalender öffnen',
    'Phone or WhatsApp':
        'Telefon oder WhatsApp',
    'Project enquiries':
        'Projektanfragen',
    'Send us the scope':
        'Senden Sie uns den Leistungsumfang',
    'Welding (MIG/MAG)':
        'Schweißen (MIG/MAG)',
    '2. What we collect':
        '2. Was wir erheben',
    '<b>Netherlands</b>':
        '<b>Niederlande</b>',
    'Local, no rotation':
        'Lokal, keine Rotation',
    'More than 10 years':
        'Mehr als 10 Jahre',
    'Project photograph':
        'Projektfoto',
    'Reference Projects':
        'Referenzprojekte',
    'See open positions':
        'Offene Stellen ansehen',
    'We did not weld it':
        'Wir haben sie nicht geschweißt',
    'What matters to us':
        'Worauf es uns ankommt',
    'Where we work from':
        'Von wo aus wir arbeiten',
    '03 &middot; Company':
        '03 &middot; Unternehmen',
    'All twelve services':
        'Alle zwölf Leistungen',
    'Apply for this role':
        'Auf diese Stelle bewerben',
    'Industrial projects':
        'Industrieprojekte',
    'Inspection & Access':
        'Prüfung & Zugangstechnik',
    'Integrated Workflow':
        'Durchgängiger Ablauf',
    'Medical certificate':
        'Ärztliche Bescheinigung',
    'Mobile Repair Teams':
        'Mobile Reparaturteams',
    'Previous photograph':
        'Vorheriges Foto',
    'Technical personnel':
        'Technisches Personal',
    '06 &middot; Industry':
        '06 &middot; Industrie',
    '3a. Recruitment data':
        '3a. Bewerberdaten',
    'Call +370 636 63 744':
        'Anrufen: +370 636 63 744',
    'Certified TIG Welder':
        'Zertifizierter WIG-Schweißer',
    'EN ISO 9606 (welder)':
        'EN ISO 9606 (Schweißer)',
    'Full Project Control':
        'Vollständige Projektkontrolle',
    'Offshore / North Sea':
        'Offshore / Nordsee',
    'Rope Access Services':
        'Seilzugangstechnik',
    'Rope access services':
        'Seilzugangstechnik',
    'Send us your details':
        'Senden Sie uns Ihr Profil',
    'Work with ALPROJECTS':
        'Arbeiten bei ALPROJECTS',
    '<b>United Kingdom</b>':
        '<b>Vereinigtes Königreich</b>',
    'BLRT Group · Klaipėda':
        'BLRT Group · Klaipėda',
    'Company Profile (PDF)':
        'Unternehmensprofil (PDF)',
    'Selected key projects':
        'Ausgewählte Schlüsselprojekte',
    'Specialized personnel':
        'Spezialisiertes Personal',
    'Take a 30-minute slot':
        'Buchen Sie 30 Minuten',
    '5. How long we keep it':
        '5. Speicherdauer',
    'Mechanical Contracting':
        'Anlagenmontage',
    'Mechanical contracting':
        'Anlagenmontage',
    'Select your discipline':
        'Wählen Sie Ihr Gewerk',
    'Strongest in Lithuania':
        'Strongest in Lithuania',
    'Why choose AL Projects':
        'Warum AL Projects',
    'ALPROJECTS Group — home':
        'ALPROJECTS Group — Startseite',
    'Head Office (Lithuania)':
        'Hauptsitz (Litauen)',
    'Inspection &amp; access':
        'Prüfung &amp; Zugangstechnik',
    'Instrument pipe fitting':
        'Instrumentenrohrleitungsbau',
    'Mechanical & Industrial':
        'Montage & Industrie',
    'Mechanical installation':
        'Mechanische Montage',
    'News — ALPROJECTS Group':
        'Aktuelles — ALPROJECTS Group',
    'Non-Destructive Testing':
        'Zerstörungsfreie Prüfung',
    'Non-destructive testing':
        'Zerstörungsfreie Prüfung',
    'Operating Across Europe':
        'Europaweit im Einsatz',
    'Quality Control / QA/QC':
        'Qualitätskontrolle / QA/QC',
    'Quality control / QA/QC':
        'Qualitätskontrolle / QA/QC',
    'Rope Access Technicians':
        'Seilzugangstechniker',
    '02 &middot; Shipbuilding':
        '02 &middot; Schiffbau',
    'Cross-Industry Expertise':
        'Branchenübergreifende Expertise',
    'Internal quality control':
        'Interne Qualitätskontrolle',
    "On somebody else's welds":
        'An fremden Schweißnähten',
    'One crew, several trades':
        'Eine Mannschaft, mehrere Gewerke',
    'Quality control and QAQC':
        'Qualitätskontrolle und QA/QC',
    'Specialists on the books':
        'Fachkräfte in der Stammbelegschaft',
    'WhatsApp +370 636 63 744':
        'WhatsApp +370 636 63 744',
    'Wind Turbine Technicians':
        'Windkrafttechniker',
    'Prefer not to fill a form':
        'Lieber kein Formular',
    'Quality control and QA/QC':
        'Qualitätskontrolle und QA/QC',
    'Short notice mobilisation':
        'Kurzfristige Mobilisierung',
    'Careers — ALPROJECTS Group':
        'Karriere — ALPROJECTS Group',
    'Company — ALPROJECTS Group':
        'Unternehmen — ALPROJECTS Group',
    'European Quality Standards':
        'Europäische Qualitätsstandards',
    'Heavy Equipment Relocation':
        'Verlagerung schwerer Anlagen',
    'Heavy equipment relocation':
        'Verlagerung schwerer Anlagen',
    'Lithuania, Belgium, Norway':
        'Litauen, Belgien, Norwegen',
    'Mechanical repair on board':
        'Mechanische Reparaturen an Bord',
    '01 &middot; Quality Control':
        '01 &middot; Qualitätskontrolle',
    '05 &middot; Energy Projects':
        '05 &middot; Energieprojekte',
    'Contacts — ALPROJECTS Group':
        'Kontakt — ALPROJECTS Group',
    'Experience and availability':
        'Erfahrung und Verfügbarkeit',
    'Initialize project sequence':
        'Projektsequenz initialisieren',
    'It never counts as sign off':
        'Sie gilt nie als Freigabe',
    'Lift planning and execution':
        'Hebeplanung und -durchführung',
    'No scaffolding, no shutdown':
        'Kein Gerüst, kein Stillstand',
    'Offshore — ALPROJECTS Group':
        'Offshore — ALPROJECTS Group',
    'Onshore project experience.':
        'Erfahrung aus Onshore-Projekten.',
    'Projects — ALPROJECTS Group':
        'Projekte — ALPROJECTS Group',
    'Services — ALPROJECTS Group':
        'Leistungen — ALPROJECTS Group',
    'Dry dock and quayside scopes':
        'Arbeiten im Dock und an der Pier',
    'Engineering-Driven Decisions':
        'Technisch begründete Entscheidungen',
    'Last updated: 15 August 2026':
        'Zuletzt aktualisiert: 15. August 2026',
    'This page could not be found':
        'Seite nicht gefunden',
    'Welding quality requirements':
        'Qualitätsanforderungen an das Schweißen',
    '<span class="txt">Home</span>':
        '<span class="txt">Startseite</span>',
    '<span class="txt">News</span>':
        '<span class="txt">Aktuelles</span>',
    'ALPROJECTS Group project site':
        'ALPROJECTS Group Baustelle',
    'Engine room and system piping':
        'Maschinenraum- und Systemrohrleitungen',
    'Industrial — ALPROJECTS Group':
        'Industrie — ALPROJECTS Group',
    'No interruption to production':
        'Ohne Unterbrechung des Betriebs',
    'Non-destructive testing (NDT)':
        'Zerstörungsfreie Prüfung (ZfP)',
    'Renewable and energy projects':
        'Projekte für erneuerbare Energien',
    'Renewables — ALPROJECTS Group':
        'Erneuerbare Energien — ALPROJECTS Group',
    'Rigging and technical support':
        'Hebetechnik und technische Unterstützung',
    'Scalable Project Architecture':
        'Skalierbare Projektorganisation',
    'Valve manifolds over the bund':
        'Armaturenverteiler über der Auffangwanne',
    '<b>6</b><span>Countries</span>':
        '<b>6</b><span>Länder</span>',
    'Completed tank farm pipe racks':
        'Fertiggestellte Rohrbrücken im Tanklager',
    'Offshore and renewable energy.':
        'Offshore und erneuerbare Energien.',
    'Ship repair — ALPROJECTS Group':
        'Schiffsreparatur — ALPROJECTS Group',
    'Structural fitting and welding':
        'Stahlbaumontage und Schweißen',
    '04 &middot; Industrial Projects':
        '04 &middot; Industrieprojekte',
    'Delivered across five countries':
        'In fünf Ländern ausgeführt',
    'Fast mobilisation to the vessel':
        'Schnelle Mobilisierung zum Schiff',
    'Fuel loading terminal completed':
        'Kraftstoff-Verladeterminal fertiggestellt',
    'HKZ Alpha &amp; Beta — Petrofac':
        'HKZ Alpha &amp; Beta — Petrofac',
    'Pipe fitting — ALPROJECTS Group':
        'Rohrleitungsbau — ALPROJECTS Group',
    'Rigging &amp; Technical Support':
        'Hebetechnik &amp; technische Unterstützung',
    'Shipbuilding — ALPROJECTS Group':
        'Schiffbau — ALPROJECTS Group',
    'We do not certify our own welds':
        'Wir zertifizieren unsere eigenen Nähte nicht',
    'Welding services (TIG, MIG/MAG)':
        'Schweißtechnik (WIG, MIG/MAG)',
    '<span class="txt">Careers</span>':
        '<span class="txt">Karriere</span>',
    '<span class="txt">Company</span>':
        '<span class="txt">Unternehmen</span>',
    'Offshore and industrial projects':
        'Offshore- und Industrieprojekte',
    'Site to site moves across Europe':
        'Verlagerungen zwischen Standorten in ganz Europa',
    '<span class="txt">Contacts</span>':
        '<span class="txt">Kontakt</span>',
    '<span class="txt">Projects</span>':
        '<span class="txt">Projekte</span>',
    '<span class="txt">Services</span>':
        '<span class="txt">Leistungen</span>',
    'Page not found — ALPROJECTS Group':
        'Seite nicht gefunden — ALPROJECTS Group',
    'Privacy Policy — ALPROJECTS Group':
        'Datenschutzerklärung — ALPROJECTS Group',
    'Site coordination and supervision':
        'Baustellenkoordination und Aufsicht',
    '3. Third parties that receive data':
        '3. Empfänger der Daten',
    'Clash detection before fabrication':
        'Kollisionsprüfung vor der Fertigung',
    'Mobile repair teams for refineries':
        'Mobile Reparaturteams für Raffinerien',
    'Our supervisors and our QA on site':
        'Unsere Bauleiter und unsere QS vor Ort',
    'Completed pipe runs at a substation':
        'Fertiggestellte Rohrleitungen an einem Umspannwerk',
    'Offshore, shipbuilding and industry':
        'Offshore, Schiffbau und Industrie',
    'Profile &amp;<br>Reference Projects':
        'Profil &amp;<br>Referenzprojekte',
    'Welding services — ALPROJECTS Group':
        'Schweißtechnik — ALPROJECTS Group',
    '3D laser scanning — ALPROJECTS Group':
        '3D-Laserscanning — ALPROJECTS Group',
    '<b>30</b><span>Open positions</span>':
        '<b>30</b><span>Offene Stellen</span>',
    'IRATA and SOFT certified technicians':
        'IRATA- und SOFT-zertifizierte Techniker',
    'Independent third party verification':
        'Unabhängige Prüfung durch Dritte',
    'Steel renewal and piping replacement':
        'Stahlerneuerung und Rohrleitungstausch',
    'Data in the client&rsquo;s CAD format':
        'Daten im CAD-Format des Kunden',
    'Download the Company Profile as a PDF':
        'Unternehmensprofil als PDF herunterladen',
    'Foundation fit-up and final alignment':
        'Fundamentanpassung und Endausrichtung',
    'Open the Company Profile in a new tab':
        'Unternehmensprofil in neuem Tab öffnen',
    'Load handling and installation support':
        'Lasthandling und Montageunterstützung',
    'Outfitting and mechanical installation':
        'Ausrüstung und mechanische Montage',
    'Pipe fitting and piping prefabrication':
        'Rohrleitungsbau und Rohrvorfertigung',
    'Pipe runs erected along a plant facade':
        'Rohrleitungen entlang einer Anlagenfassade montiert',
    'Piping installation in the engine room':
        'Rohrleitungsmontage im Maschinenraum',
    'Reporting in the client&rsquo;s format':
        'Berichte im Format des Kunden',
    'TIG root pass on a prefabricated spool':
        'WIG-Wurzellage an einem vorgefertigten Rohrspool',
    'Cover of the ALPROJECTS Company Profile':
        'Titelseite des ALPROJECTS Unternehmensprofils',
    'Four Sectors,<br>One Set of Disciplines':
        'Vier Branchen,<br>ein Satz an Gewerken',
    'Mechanical contracting and installation':
        'Anlagenmontage und Installation',
    'Piping and steel structure verification':
        'Prüfung von Rohrleitungen und Stahlbau',
    'Rope access services — ALPROJECTS Group':
        'Seilzugangstechnik — ALPROJECTS Group',
    'Strongest in Lithuania, 2025&ndash;2026':
        'Strongest in Lithuania, 2025&ndash;2026',
    'Teams that follow the yard&rsquo;s plan':
        'Teams, die dem Terminplan der Werft folgen',
    'Download the Reference Projects as a PDF':
        'Referenzprojekte als PDF herunterladen',
    'Inspection and mechanical work at height':
        'Prüfung und mechanische Arbeiten in der Höhe',
    'Open the Reference Projects in a new tab':
        'Referenzprojekte in neuem Tab öffnen',
    'Rescue plan and supervision on every job':
        'Rettungskonzept und Aufsicht bei jedem Einsatz',
    'Traceability down to the individual weld':
        'Rückverfolgbarkeit bis zur einzelnen Schweißnaht',
    'Transformer packages and plant equipment':
        'Transformatorenpakete und Anlagentechnik',
    'Weld, material and structural inspection':
        'Prüfung von Schweißnähten, Werkstoffen und Konstruktionen',
    '<span class="step-n">02</span> Your trade':
        '<span class="step-n">02</span> Ihr Gewerk',
    '<span>Contract</span><b>Project-based</b>':
        '<span>Vertrag</span><b>Projektbezogen</b>',
    '<span>Positions</span><b>30 positions</b>':
        '<span>Stellen</span><b>30 Stellen</b>',
    'As-built survey of existing installations':
        'Bestandsaufnahme vorhandener Anlagen',
    'Mechanical contracting — ALPROJECTS Group':
        'Anlagenmontage — ALPROJECTS Group',
    'Phone <span class="opt">(optional)</span>':
        'Telefon <span class="opt">(optional)</span>',
    'Project coordination and site supervision':
        'Projektkoordination und Bauaufsicht',
    'We recruit regularly in these disciplines':
        'In diesen Gewerken rekrutieren wir regelmäßig',
    '<b>3</b><span>Working days to reply</span>':
        '<b>3</b><span>Werktage bis zur Antwort</span>',
    '<span class="step-n">01</span> Who you are':
        '<span class="step-n">01</span> Wer Sie sind',
    'A European provider of industrial services':
        'Ein europäischer Anbieter industrieller Dienstleistungen',
    'Among the strongest companies in Lithuania':
        'Zu den stärksten Unternehmen Litauens',
    'Cover of the ALPROJECTS Reference Projects':
        'Titelseite der ALPROJECTS Referenzprojekte',
    'Non-destructive testing — ALPROJECTS Group':
        'Zerstörungsfreie Prüfung — ALPROJECTS Group',
    'Project Updates &amp; Engineering Insights':
        'Projektberichte &amp; technische Einblicke',
    'e.g. TIG 141, IRATA Level 2, VT/PT Level 2':
        'z. B. WIG 141, IRATA Level 2, VT/PT Stufe 2',
    '<span class="step-n">03</span> Availability':
        '<span class="step-n">03</span> Verfügbarkeit',
    'Dismantling, skidding, jacking, positioning':
        'Demontage, Verschieben, Anheben, Positionieren',
    'Gas pipeline fabrication &amp; installation':
        'Fertigung &amp; Montage von Gasleitungen',
    'Turnarounds, shutdowns and breakdown repair':
        'Großstillstände, Anlagenstillstände und Störungsbehebung',
    'Dimensional control of structures and piping':
        'Maßkontrolle von Konstruktionen und Rohrleitungen',
    'Mechanical scopes and independent inspection':
        'Mechanische Gewerke und unabhängige Prüfung',
    'Quality control and QA/QC — ALPROJECTS Group':
        'Qualitätskontrolle und QA/QC — ALPROJECTS Group',
    'TIG for piping, root runs and stainless work':
        'WIG für Rohrleitungen, Wurzellagen und Edelstahl',
    '<span class="step-n">04</span> Your documents':
        '<span class="step-n">04</span> Ihre Unterlagen',
    'Equipment alignment and mechanical completion':
        'Ausrichtung der Anlagen und mechanische Fertigstellung',
    'Heavy equipment relocation — ALPROJECTS Group':
        'Verlagerung schwerer Anlagen — ALPROJECTS Group',
    'Jack-up vessel maintenance &amp; repair works':
        'Wartungs- &amp; Reparaturarbeiten an Hubschiffen',
    'Project Updates &amp;<br>Engineering Insights':
        'Projektberichte &amp;<br>technische Einblicke',
    'Steel fabrication and mechanical installation':
        'Stahlbaufertigung und mechanische Montage',
    '<time datetime="2026-06-23">23 Jun 2026</time>':
        '<time datetime="2026-06-23">23. Juni 2026</time>',
    '<time datetime="2026-07-25">25 Jul 2026</time>':
        '<time datetime="2026-07-25">25. Juli 2026</time>',
    '<time datetime="2026-08-01">01 Aug 2026</time>':
        '<time datetime="2026-08-01">01. Aug. 2026</time>',
    '<time datetime="2026-08-08">08 Aug 2026</time>':
        '<time datetime="2026-08-08">08. Aug. 2026</time>',
    '<time datetime="2026-08-13">13 Aug 2026</time>':
        '<time datetime="2026-08-13">13. Aug. 2026</time>',
    'Open the Company Profile as a PDF in a new tab':
        'Unternehmensprofil als PDF in neuem Tab öffnen',
    'Process lines run alongside insulated ductwork':
        'Prozessleitungen neben isolierten Kanälen verlegt',
    'Mechanical, marine<br>&amp; inspection services':
        'Montage, Schiffbau<br>&amp; Prüfung',
    'Pipe rack and cable trays on the loading gantry':
        'Rohrbrücke und Kabeltrassen am Verladeportal',
    'Stainless pipework around a transformer package':
        'Edelstahlrohrleitungen um ein Transformatorenpaket',
    '<b>300</b><span>Specialists on our roster</span>':
        '<b>300</b><span>Fachkräfte in der Stammbelegschaft</span>',
    'Carbon steel lines being set out on a plant roof':
        'Kohlenstoffstahlleitungen auf einem Anlagendach ausgelegt',
    'Experience with pipe and steel structure welding':
        'Erfahrung im Schweißen von Rohrleitungen und Stahlbau',
    'One contract, one schedule, one point of contact':
        'Ein Vertrag, ein Terminplan, ein Ansprechpartner',
    'Read more about the Strongest in Lithuania award':
        'Mehr über die Auszeichnung Strongest in Lithuania',
    'Refrigeration systems · industrial modifications':
        'Kälteanlagen · industrielle Umbauten',
    'Rigging and technical support — ALPROJECTS Group':
        'Hebetechnik und technische Unterstützung — ALPROJECTS Group',
    'Support at client and third party witness points':
        'Begleitung an Haltepunkten von Kunde und Dritten',
    'Anything else <span class="opt">(optional)</span>':
        'Sonstiges <span class="opt">(optional)</span>',
    'Mechanical package installed beneath the bushings':
        'Mechanisches Paket unterhalb der Durchführungen montiert',
    'Not on the list? Add it in the notes field below.':
        'Nicht in der Liste? Tragen Sie es unten im Bemerkungsfeld ein.',
    'Offshore commissioning &amp; installation support':
        'Offshore-Inbetriebnahme &amp; Montageunterstützung',
    'Open the Reference Projects as a PDF in a new tab':
        'Referenzprojekte als PDF in neuem Tab öffnen',
    'Certifications <span class="opt">(optional)</span>':
        'Zertifikate <span class="opt">(optional)</span>',
    'Cooling and process lines at the transformer plant':
        'Kühl- und Prozessleitungen im Transformatorenwerk',
    'Fuel loading terminal completed — ALPROJECTS Group':
        'Kraftstoff-Verladeterminal fertiggestellt — ALPROJECTS Group',
    'Photographs from delivered and in-progress scopes.':
        'Aufnahmen aus abgeschlossenen und laufenden Projekten.',
    'We do not certify our own welds — ALPROJECTS Group':
        'Wir zertifizieren unsere eigenen Nähte nicht — ALPROJECTS Group',
    'Vessel and pipe run carried along the building line':
        'Behälter und Rohrleitung entlang der Gebäudeflucht geführt',
    'Pump skids and valve stations, terminal loading area':
        'Pumpenskids und Armaturenstationen im Verladebereich',
    'Welding coordination and traceability under ISO 3834':
        'Schweißaufsicht und Rückverfolgbarkeit nach ISO 3834',
    'Mobile repair teams for refineries — ALPROJECTS Group':
        'Mobile Reparaturteams für Raffinerien — ALPROJECTS Group',
    'Phone: <a href="tel:+37063663744">+370 636 63 744</a>':
        'Telefon: <a href="tel:+37063663744">+370 636 63 744</a>',
    'Pipe rack running to storage tanks at a fuel terminal':
        'Rohrbrücke zu den Lagertanks eines Kraftstoffterminals',
    'TIG welder working on a large-diameter stainless pipe':
        'WIG-Schweißer an einer Edelstahlleitung großen Durchmessers',
    'We needed 30 certified TIG welders — ALPROJECTS Group':
        'Wir brauchten 30 zertifizierte WIG-Schweißer — ALPROJECTS Group',
    'Work under the plant&rsquo;s permit and safety regime':
        'Arbeiten unter dem Erlaubnis- und Sicherheitsregime der Anlage',
    'A transformer mechanical package across five countries':
        'Ein mechanisches Transformatorenpaket in fünf Ländern',
    'ALPROJECTS Group — Engineering for Industry & Offshore':
        'ALPROJECTS Group — Engineering für Industrie und Offshore',
    'Disconnection and reconnection of piping and utilities':
        'Trennen und Wiederanschluss von Rohrleitungen und Medien',
    'Fitters working inside a hull block under construction':
        'Monteure in einer im Bau befindlichen Rumpfsektion',
    'Preferred rotation <span class="opt">(optional)</span>':
        'Gewünschte Rotation <span class="opt">(optional)</span>',
    'Subscribe to receive company news and project updates.':
        'Abonnieren Sie Unternehmensnachrichten und Projektberichte.',
    'Transformer package, five countries — ALPROJECTS Group':
        'Transformatorenpaket, fünf Länder — ALPROJECTS Group',
    '<span>8 pages</span><span>PDF</span><span>2.7 MB</span>':
        '<span>8 Seiten</span><span>PDF</span><span>2,7 MB</span>',
    '<span>Location</span><b>Project sites across Europe</b>':
        '<span>Einsatzort</span><b>Baustellen in ganz Europa</b>',
    'Years of experience <span class="opt">(optional)</span>':
        'Berufsjahre <span class="opt">(optional)</span>',
    '<span>16 pages</span><span>PDF</span><span>2.1 MB</span>':
        '<span>16 Seiten</span><span>PDF</span><span>2,1 MB</span>',
    "Among Lithuania's strongest companies — ALPROJECTS Group":
        'Zu den stärksten Unternehmen Litauens — ALPROJECTS Group',
    'Country of residence <span class="opt">(optional)</span>':
        'Wohnsitzland <span class="opt">(optional)</span>',
    'Discuss a project <span class="ar-e" aria-hidden="true">&#8593;</span>':
        'Projekt besprechen <span class="ar-e" aria-hidden="true">&#8593;</span>',
    'Fit-up, alignment and dimensional control before welding':
        'Passung, Ausrichtung und Maßkontrolle vor dem Schweißen',
    'Photographs of certificates taken with a phone are fine.':
        'Mit dem Handy fotografierte Zeugnisse sind völlig ausreichend.',
    'TIG root pass being welded on a prefabricated pipe spool':
        'WIG-Wurzellage an einem vorgefertigten Rohrspool',
    'Wind turbine technicians on site at an onshore wind farm':
        'Windkrafttechniker in einem Onshore-Windpark',
    'Piping installation in the engine room — ALPROJECTS Group':
        'Rohrleitungsmontage im Maschinenraum — ALPROJECTS Group',
    '<span>Cert. C550875</span><span>Valid to 07.08.2028</span>':
        '<span>Zert. C550875</span><span>Gültig bis 07.08.2028</span>',
    '<span>Cert. C550877</span><span>Valid to 07.08.2028</span>':
        '<span>Zert. C550877</span><span>Gültig bis 07.08.2028</span>',
    '<span>Cert. C760290</span><span>Valid to 28.07.2028</span>':
        '<span>Zert. C760290</span><span>Gültig bis 28.07.2028</span>',
    'ALPROJECTS GROUP <span>&middot;</span> KLAIPĖDA, LITHUANIA':
        'ALPROJECTS GROUP <span>&middot;</span> KLAIPĖDA, LITAUEN',
    'ALPROJECTS, UAB<br>Šilutės pl. 2, LT-92298<br>Klaipėda':
        'ALPROJECTS, UAB<br>Šilutės pl. 2, LT-92298<br>Klaipėda',
    'ALPROJECTS engineer working from isometric drawings on site':
        'ALPROJECTS Ingenieur arbeitet vor Ort nach Isometrien',
    'Handover dossier assembled as the work goes, not at the end':
        'Abnahmedokumentation entsteht laufend, nicht erst am Ende',
    'Welder running a TIG root pass on a prefabricated pipe spool':
        'Schweißer bei der WIG-Wurzellage an einem vorgefertigten Rohrspool',
    'Countries you can work in <span class="opt">(optional)</span>':
        'Länder, in denen Sie arbeiten können <span class="opt">(optional)</span>',
    'Structural steel, pressure retaining piping and pipe supports':
        'Stahlbau, drucktragende Rohrleitungen und Rohrhalterungen',
    'Valid TIG welding certification with supporting documentation':
        'Gültige WIG-Schweißerprüfung mit den zugehörigen Nachweisen',
    'Industrial maintenance · equipment &amp; hydro-turbine repairs':
        'Industrieinstandhaltung · Reparatur von Anlagen &amp; Wasserturbinen',
    'WPS and WPQR to EN ISO 15614, written for the project standard':
        'Schweißanweisung und Verfahrensprüfung nach EN ISO 15614, auf die Projektnorm zugeschnitten',
    'MIG and semi-automatic MAG for structural steel and fill passes':
        'MIG und teilmechanisiertes MAG für Stahlbau und Fülllagen',
    'Process and utility piping: carbon steel, stainless, large bore':
        'Prozess- und Versorgungsleitungen: Kohlenstoffstahl, Edelstahl, große Nennweiten',
    'Project updates and engineering insights from ALPROJECTS Group.':
        'Projektberichte und technische Einblicke von ALPROJECTS Group.',
    'Willingness to travel and work on site across several countries':
        'Reisebereitschaft und Einsatz auf Baustellen in mehreren Ländern',
    'Jack-up structures · steel erection · welding · offshore support':
        'Hubinselstrukturen · Stahlmontage · Schweißen · Offshore-Unterstützung',
    'ALPROJECTS Group — Integrated Engineering for Industry & Offshore':
        'ALPROJECTS Group — Integriertes Engineering für Industrie und Offshore',
    'ALPROJECTS, UAB — Šilutės pl. 2, LT-92298 Klaipėda, Lithuania':
        'ALPROJECTS, UAB — Šilutės pl. 2, LT-92298 Klaipėda, Litauen',
    'Email: <a href="mailto:info@alprojects.eu">info@alprojects.eu</a>':
        'E-Mail: <a href="mailto:info@alprojects.eu">info@alprojects.eu</a>',
    'Railway bridges · steel fitting · structural repairs · 5G welding':
        'Eisenbahnbrücken · Stahlbaumontage · Instandsetzung · Schweißen in Position 5G',
    'We needed 30 certified TIG welders. Europe could not supply them.':
        'Wir brauchten 30 zertifizierte WIG-Schweißer. Europa konnte sie nicht liefern.',
    'Welder running a TIG root pass on a large-diameter stainless pipe':
        'Schweißer bei der WIG-Wurzellage an einer Edelstahlleitung großen Durchmessers',
    'A serious approach to safety in complex and confined environments.':
        'Ein konsequenter Umgang mit Sicherheit in komplexen und beengten Umgebungen.',
    'Welder qualifications to EN ISO 9606, verified before mobilisation':
        'Schweißerprüfungen nach EN ISO 9606, vor der Mobilisierung geprüft',
    'ALPROJECTS Group — integrated engineering for industry and offshore':
        'ALPROJECTS Group — integriertes Engineering für Industrie und Offshore',
    'Rope access technician working beneath an offshore platform walkway':
        'Seilzugangstechniker unter dem Laufsteg einer Offshore-Plattform',
    'Send us the scope and we will come back with a price and crew dates.':
        'Senden Sie uns den Leistungsumfang und wir melden uns mit Preis und Einsatzterminen.',
    'Stainless pipework and transformer package installed at a substation':
        'Edelstahlrohrleitungen und Transformatorenpaket in einem Umspannwerk montiert',
    'Willingness to travel &mdash; our projects run in several countries.':
        'Reisebereitschaft &mdash; unsere Projekte laufen in mehreren Ländern.',
    'Working English; Lithuanian, Russian or Polish are useful additions.':
        'Verhandlungssicheres Englisch; Litauisch, Russisch oder Polnisch sind von Vorteil.',
    'Sea water, bilge, ballast and fuel lines going in on board right now.':
        'Seewasser-, Bilge-, Ballast- und Kraftstoffleitungen werden gerade an Bord montiert.',
    '<span class="srv-n">07</span><span class="srv-name">Ship Repair</span>':
        '<span class="srv-n">07</span><span class="srv-name">Schiffsreparatur</span>',
    'DNV management system certificate — ISO 9001:2015, certificate C760290':
        'DNV-Managementsystemzertifikat — ISO 9001:2015, Zertifikat C760290',
    'Site installation, flange assembly and support during pressure testing':
        'Montage vor Ort, Flanschverbindungen und Begleitung der Druckprüfung',
    '<span class="srv-n">02</span><span class="srv-name">Pipe Fitting</span>':
        '<span class="srv-n">02</span><span class="srv-name">Rohrleitungsbau</span>',
    '<span class="srv-n">06</span><span class="srv-name">Shipbuilding</span>':
        '<span class="srv-n">06</span><span class="srv-name">Schiffbau</span>',
    '<strong>GitHub, Inc.</strong> &mdash; website hosting and request logs.':
        '<strong>GitHub, Inc.</strong> &mdash; Hosting der Website und Zugriffsprotokolle.',
    'Completed pipe rack running to storage tanks at a fuel loading terminal':
        'Fertiggestellte Rohrbrücke zu den Lagertanks eines Kraftstoff-Verladeterminals',
    'DNV management system certificate — ISO 14001:2015, certificate C550875':
        'DNV-Managementsystemzertifikat — ISO 14001:2015, Zertifikat C550875',
    'DNV management system certificate — ISO 45001:2018, certificate C550877':
        'DNV-Managementsystemzertifikat — ISO 45001:2018, Zertifikat C550877',
    'Disciplines you work in, years of experience, and when you could start.':
        'Ihre Gewerke, Ihre Berufsjahre und Ihr möglicher Starttermin.',
    'Open the ISO 9001:2015 certificate as a PDF, certificate number C760290':
        'ISO 9001:2015-Zertifikat als PDF öffnen, Zertifikatsnummer C760290',
    'Or write to <a href="mailto:info@alprojects.eu">info@alprojects.eu</a>.':
        'Oder schreiben Sie an <a href="mailto:info@alprojects.eu">info@alprojects.eu</a>.',
    'Send us the drawings and we will come back with a price and crew dates.':
        'Senden Sie uns die Zeichnungen und wir melden uns mit Preis und Einsatzterminen.',
    'Engineering expertise backed by certified specialists and safe execution':
        'Technische Kompetenz, getragen von zertifizierten Fachkräften und sicherer Ausführung',
    'Open the ISO 14001:2015 certificate as a PDF, certificate number C550875':
        'ISO 14001:2015-Zertifikat als PDF öffnen, Zertifikatsnummer C550875',
    'Open the ISO 45001:2018 certificate as a PDF, certificate number C550877':
        'ISO 45001:2018-Zertifikat als PDF öffnen, Zertifikatsnummer C550877',
    'ALPROJECTS, UAB<br> Šilutės pl. 2<br> LT-92298 Klaipėda<br> Lithuania':
        'ALPROJECTS, UAB<br> Šilutės pl. 2<br> LT-92298 Klaipėda<br> Litauen',
    'Overlay the drafting sheet — grid, registration marks and live dimensions':
        'Zeichnungsraster einblenden — Raster, Passmarken und laufende Maße',
    'Spool prefabrication from isometrics, marked and traceable to the drawing':
        'Spool-Vorfertigung nach Isometrien, gekennzeichnet und zur Zeichnung rückverfolgbar',
    'How ALPROJECTS Group handles personal data collected through this website.':
        'Wie ALPROJECTS Group personenbezogene Daten verarbeitet, die über diese Website erhoben werden.',
    'Marine pipe fitters: engine room and system piping on newbuilds and repair':
        'Schiffsrohrleger: Maschinenraum- und Systemrohrleitungen bei Neubau und Reparatur',
    '<span class="srv-n">01</span><span class="srv-name">Welding Services</span>':
        '<span class="srv-n">01</span><span class="srv-name">Schweißtechnik</span>',
    '<span class="srv-n">10</span><span class="srv-name">3D Laser Scanning</span>':
        '<span class="srv-n">10</span><span class="srv-name">3D-Laserscanning</span>',
    'September 2025 to April 2026. Twelve specialists. Over 11,000 hours on site.':
        'September 2025 bis April 2026. Zwölf Fachkräfte. Über 11.000 Stunden vor Ort.',
    'Certificates you hold <span class="opt">(optional, tap all that apply)</span>':
        'Ihre Zertifikate <span class="opt">(optional, alles Zutreffende antippen)</span>',
    'Valid certification for your discipline, and the documentation to support it.':
        'Eine gültige Qualifikation für Ihr Gewerk und die zugehörigen Nachweise.',
    '<span class="srv-n">05</span><span class="srv-name">Mobile Repair Teams</span>':
        '<span class="srv-n">05</span><span class="srv-name">Mobile Reparaturteams</span>',
    '<span class="srv-n">09</span><span class="srv-name">Rope Access Services</span>':
        '<span class="srv-n">09</span><span class="srv-name">Seilzugangstechnik</span>',
    'Hull block under construction with fitters working inside the scaffolded section':
        'Rumpfsektion im Bau, Monteure arbeiten im eingerüsteten Bereich',
    '<span class="srv-n">03</span><span class="srv-name">Mechanical Contracting</span>':
        '<span class="srv-n">03</span><span class="srv-name">Anlagenmontage</span>',
    '<span class="srv-n">08</span><span class="srv-name">Non-Destructive Testing</span>':
        '<span class="srv-n">08</span><span class="srv-name">Zerstörungsfreie Prüfung</span>',
    '<span class="srv-n">11</span><span class="srv-name">Quality Control / QA/QC</span>':
        '<span class="srv-n">11</span><span class="srv-name">Qualitätskontrolle / QA/QC</span>',
    'Instrument pipe fitters: small bore, tubing, impulse lines and instrument hook-ups':
        'Monteure für Mess- und Instrumentierungsleitungen: kleine Nennweiten, Tubing, Impulsleitungen und Messanschlüsse',
    'Cruise &amp; river vessels · piping systems · pressure testing · structural welding':
        'Kreuzfahrt- &amp; Flussschiffe · Rohrleitungssysteme · Druckprüfung · Konstruktionsschweißen',
    'Offshore reel manufacturing · ship repair · piping systems · industrial maintenance':
        'Fertigung von Offshore-Trommeln · Schiffsreparatur · Rohrleitungssysteme · Industrieinstandhaltung',
    'Our NDT does not replace your inspector. We use it to catch our own mistakes first.':
        'Unsere ZfP ersetzt nicht Ihren Prüfer. Wir setzen sie ein, um zuerst unsere eigenen Fehler zu finden.',
    'Planning a project across shipbuilding, piping or industrial services? Let us talk.':
        'Planen Sie ein Projekt in Schiffbau, Rohrleitungsbau oder Industriedienstleistungen? Sprechen wir darüber.',
    'Send us the scope or the drawings and we will come back with a price and crew dates.':
        'Senden Sie uns den Leistungsumfang oder die Zeichnungen und wir melden uns mit Preis und Einsatzterminen.',
    '<span class="srv-n">04</span><span class="srv-name">Heavy Equipment Relocation</span>':
        '<span class="srv-n">04</span><span class="srv-name">Verlagerung schwerer Anlagen</span>',
    'If you hold the ticket and you are willing to travel, we would like to hear from you.':
        'Wenn Sie die Qualifikation haben und reisebereit sind, melden Sie sich bei uns.',
    '<strong>Industrial</strong> — plant installation, transformer packages, process piping.':
        '<strong>Industrie</strong> — Anlagenmontage, Transformatorenpakete, Prozessrohrleitungen.',
    'Spool base &amp; offshore platforms · pipeline welding · fabrication · offshore support':
        'Spoolbase &amp; Offshore-Plattformen · Pipelineschweißen · Fertigung · Offshore-Unterstützung',
    'Certificate numbers and expiry dates, projects you have worked on, when you could start.':
        'Zertifikatsnummern und Gültigkeitsdaten, Projekte, an denen Sie gearbeitet haben, möglicher Starttermin.',
    '<span class="srv-n">12</span><span class="srv-name">Rigging &amp; Technical Support</span>':
        '<span class="srv-n">12</span><span class="srv-name">Hebetechnik &amp; technische Unterstützung</span>',
    '<span>30 positions</span><span>Project sites across Europe</span><span>Project-based</span>':
        '<span>30 Stellen</span><span>Baustellen in ganz Europa</span><span>Projektbezogen</span>',
    '<strong>Offshore</strong> — inspection, access and mechanical works on offshore facilities.':
        '<strong>Offshore</strong> — Prüfung, Zugangstechnik und mechanische Arbeiten an Offshore-Anlagen.',
    'The skilled trades shortage is not an abstraction when it is your project that cannot start.':
        'Der Fachkräftemangel ist nichts Abstraktes, wenn das eigene Projekt deshalb nicht anlaufen kann.',
    'The link may be out of date, or the page may have moved. Everything we do is on the homepage.':
        'Der Link ist möglicherweise veraltet oder die Seite wurde verschoben. Alles, was wir tun, finden Sie auf der Startseite.',
    '<span class="num">03</span><span>23 Jun 2026 &middot; Company</span><span class="arr">&#8593;</span>':
        '<span class="num">03</span><span>23. Juni 2026 &middot; Unternehmen</span><span class="arr">&#8593;</span>',
    '<strong>Energy and renewables</strong> — fuel handling infrastructure and wind energy support.':
        '<strong>Energie und erneuerbare Energien</strong> — Infrastruktur für Kraftstoffumschlag und Unterstützung der Windenergie.',
    '<span class="num">06</span><span>25 Jul 2026 &middot; Industry</span><span class="arr">&#8593;</span>':
        '<span class="num">06</span><span>25. Juli 2026 &middot; Industrie</span><span class="arr">&#8593;</span>',
    '<span class="bp-key" aria-hidden="true">B</span> <span class="bp-hint-label">Drawing mode</span>':
        '<span class="bp-key" aria-hidden="true">B</span> <span class="bp-hint-label">Zeichnungsmodus</span>',
    'Lifts go wrong at the planning stage. We plan them, and we send the people who run them on site.':
        'Hübe scheitern in der Planung. Wir planen sie und stellen die Leute, die sie vor Ort durchführen.',
    '<strong>Shipbuilding</strong> — piping and mechanical installation on vessels under construction.':
        '<strong>Schiffbau</strong> — Rohrleitungs- und Maschinenmontage auf Schiffen im Bau.',
    'UAB “ALprojects” has been awarded the Strongest in Lithuania 2025–2026 certificate by Creditinfo.':
        'UAB „ALprojects“ wurde von Creditinfo mit dem Zertifikat Strongest in Lithuania 2025–2026 ausgezeichnet.',
    'We read every application and reply within three working days when a project matches your profile.':
        'Wir lesen jede Bewerbung und antworten innerhalb von drei Werktagen, sobald ein Projekt zu Ihrem Profil passt.',
    '<span class="num">02</span><span>08 Aug 2026 &middot; Shipbuilding</span><span class="arr">&#8593;</span>':
        '<span class="num">02</span><span>08. Aug. 2026 &middot; Schiffbau</span><span class="arr">&#8593;</span>',
    '<span class="num">03</span><span>23 Jun 2026 &middot; Company</span><span class="arr">&#8593;</span>':
        '<span class="num">03</span><span>23. Juni 2026 &middot; Unternehmen</span><span class="arr">&#8593;</span>',
    '<span class="num">06</span><span>25 Jul 2026 &middot; Industry</span><span class="arr">&#8593;</span>':
        '<span class="num">06</span><span>25. Juli 2026 &middot; Industrie</span><span class="arr">&#8593;</span>',
    'Straight into the diary of someone who can answer technical questions — scope, standards, crew dates.':
        'Direkt in den Kalender von jemandem, der technische Fragen beantworten kann — Leistungsumfang, Normen, Einsatztermine.',
    '<span class="num">01</span><span>13 Aug 2026 &middot; Quality Control</span><span class="arr">&#8593;</span>':
        '<span class="num">01</span><span>13. Aug. 2026 &middot; Qualitätskontrolle</span><span class="arr">&#8593;</span>',
    '<span class="num">05</span><span>25 Jul 2026 &middot; Energy Projects</span><span class="arr">&#8593;</span>':
        '<span class="num">05</span><span>25. Juli 2026 &middot; Energieprojekte</span><span class="arr">&#8593;</span>',
    'If this policy changes, the revised version will be published on this page with a new date at the top.':
        'Wird diese Erklärung geändert, erscheint die überarbeitete Fassung mit neuem Datum auf dieser Seite.',
    'Qualified specialists, available for project-based, short-term and long-term assignments across Europe.':
        'Qualifizierte Fachkräfte für projektbezogene, kurz- und langfristige Einsätze in ganz Europa.',
    '<span class="contact-label">General</span> <a href="mailto:office@alprojects.eu">office@alprojects.eu</a>':
        '<span class="contact-label">Allgemein</span> <a href="mailto:office@alprojects.eu">office@alprojects.eu</a>',
    '<span class="num">02</span><span>08 Aug 2026 &middot; Shipbuilding</span><span class="arr">&#8593;</span>':
        '<span class="num">02</span><span>08. Aug. 2026 &middot; Schiffbau</span><span class="arr">&#8593;</span>',
    'Six fields are required. Everything else helps us match you faster, but you can send the form without it.':
        'Sechs Felder sind Pflicht. Alles Weitere hilft uns, Sie schneller zuzuordnen, ist aber nicht erforderlich.',
    'Stainless steel piping, cooling systems and precision installation — repeated across five European sites.':
        'Edelstahlrohrleitungen, Kühlsysteme und Präzisionsmontage — an fünf europäischen Standorten wiederholt.',
    '<span class="num">04</span><span>01 Aug 2026 &middot; Industrial Projects</span><span class="arr">&#8593;</span>':
        '<span class="num">04</span><span>01. Aug. 2026 &middot; Industrieprojekte</span><span class="arr">&#8593;</span>',
    '<span class="num">01</span><span>13 Aug 2026 &middot; Quality Control</span><span class="arr">&#8593;</span>':
        '<span class="num">01</span><span>13. Aug. 2026 &middot; Qualitätskontrolle</span><span class="arr">&#8593;</span>',
    '<span class="num">05</span><span>25 Jul 2026 &middot; Energy Projects</span><span class="arr">&#8593;</span>':
        '<span class="num">05</span><span>25. Juli 2026 &middot; Energieprojekte</span><span class="arr">&#8593;</span>',
    'Contact ALPROJECTS Group — Šilutės pl. 2, Klaipėda, Lithuania. Project enquiries and personnel requests.':
        'Kontakt zu ALPROJECTS Group — Šilutės pl. 2, Klaipėda, Litauen. Projektanfragen und Personalanfragen.',
    'Mechanical contracting, pipe fitting, welding services, QAQC, rope access and NDT for industry and offshore.':
        'Anlagenmontage, Rohrleitungsbau, Schweißtechnik, QA/QC, Seilzugangstechnik und ZfP für Industrie und Offshore.',
    'Welding, piping and mechanical works across Europe and Scandinavia. Inspected by people who did not do the welding.':
        'Schweißen, Rohrleitungsbau und mechanische Arbeiten in ganz Europa und Skandinavien. Geprüft von Prüfern, die die Naht nicht selbst geschweißt haben.',
    'Shipbuilding, offshore, industrial and renewable energy projects delivered by ALPROJECTS Group across Europe.':
        'Projekte in Schiffbau, Offshore, Industrie und erneuerbaren Energien, ausgeführt von ALPROJECTS Group in ganz Europa.',
    '<span>Offshore &amp; Marine</span><span>Energy</span><span>Heavy Industry</span><span>Steel Fabrication</span>':
        '<span>Offshore &amp; Schiffbau</span><span>Energie</span><span>Schwerindustrie</span><span>Stahlbaufertigung</span>',
    'This website has no user accounts, no analytics and sets no cookies of its own. Data reaches us in three ways:':
        'Diese Website hat keine Benutzerkonten, keine Reichweitenmessung und setzt keine eigenen Cookies. Daten erreichen uns auf drei Wegen:',
    '<span class="contact-label">Project enquiries</span> <a href="mailto:info@alprojects.eu">info@alprojects.eu</a>':
        '<span class="contact-label">Projektanfragen</span> <a href="mailto:info@alprojects.eu">info@alprojects.eu</a>',
    '<span class="num">04</span><span>01 Aug 2026 &middot; Industrial Projects</span><span class="arr">&#8593;</span>':
        '<span class="num">04</span><span>01. Aug. 2026 &middot; Industrieprojekte</span><span class="arr">&#8593;</span>',
    '<span>Industrial Plants</span><span>Offshore Structures</span><span>Wind Energy</span><span>Infrastructure</span>':
        '<span>Industrieanlagen</span><span>Offshore-Strukturen</span><span>Windenergie</span><span>Infrastruktur</span>',
    'Yard schedules do not move. Our crews slot into them and take engine room piping, structural steel and outfitting.':
        'Werftterminpläne verschieben sich nicht. Unsere Teams fügen sich ein und übernehmen Maschinenraumrohrleitungen, Stahlbau und Ausrüstung.',
    '<span>Offshore</span><span>Industrial Construction</span><span>Energy Projects</span><span>Marine Facilities</span>':
        '<span>Offshore</span><span>Industriebau</span><span>Energieprojekte</span><span>Maritime Anlagen</span>',
    'This page could not be found. Return to the ALPROJECTS Group homepage for industrial, offshore and energy services.':
        'Seite nicht gefunden. Zurück zur Startseite von ALPROJECTS Group für Leistungen in Industrie, Offshore und Energie.',
    'Tell us your discipline and certifications. We read every application and reply when a project matches your profile.':
        'Nennen Sie uns Ihr Gewerk und Ihre Qualifikationen. Wir lesen jede Bewerbung und melden uns, sobald ein Projekt zu Ihrem Profil passt.',
    '<span>Offshore Platforms</span><span>Wind Turbines</span><span>Industrial Towers</span><span>Marine Structures</span>':
        '<span>Offshore-Plattformen</span><span>Windkraftanlagen</span><span>Industrietürme</span><span>Maritime Strukturen</span>',
    '<strong>Calendly LLC</strong> &mdash; the scheduling calendar on the contacts page, and only if you choose to open it.':
        '<strong>Calendly LLC</strong> &mdash; der Terminkalender auf der Kontaktseite, und nur wenn Sie ihn selbst öffnen.',
    '<b>Attach drawings or a specification</b> <span>Choose files, or drag them here. PDF, DWG, STEP, images or ZIP, up to 10 MB each.</span>':
        '<b>Zeichnungen oder Leistungsverzeichnis anhängen</b> <span>Dateien auswählen oder hierher ziehen. PDF, DWG, STEP, Bilder oder ZIP, je bis 10 MB.</span>',
    '<b>Attach your CV and certificates</b> <span>Choose files, or drag them here. PDF, JPG or PNG, up to 10 MB each.</span>':
        '<b>Lebenslauf und Zeugnisse anhängen</b> <span>Dateien auswählen oder hierher ziehen. PDF, JPG oder PNG, je bis 10 MB.</span>',
    '<span class="sector-name">INDUSTRIAL</span> <span class="sector-fact">Plant installation and transformer packages</span>':
        '<span class="sector-name">INDUSTRIE</span> <span class="sector-fact">Anlagenmontage und Transformatorenpakete</span>',
    '<span class="sector-name">OFFSHORE</span> <span class="sector-fact">Rope access, NDT and mechanical works offshore</span>':
        '<span class="sector-name">OFFSHORE</span> <span class="sector-fact">Seilzugangstechnik, ZfP und mechanische Arbeiten offshore</span>',
    '<strong>Legitimate interest</strong> (Art. 6(1)(f)) — responding to enquiries, and keeping the site secure and available.':
        '<strong>Berechtigtes Interesse</strong> (Art. 6 Abs. 1 lit. f) — Beantwortung von Anfragen sowie Sicherheit und Verfügbarkeit der Website.',
    'Mobilised as complete crews with supervision, certification records and QA documentation in place before the first shift.':
        'Mobilisiert als komplette Mannschaften mit Aufsicht, Qualifikationsnachweisen und QS-Dokumentation, bereits vor der ersten Schicht.',
    '<span class="sector-name">RENEWABLES</span> <span class="sector-fact">Cable works and turbine support on wind farms</span>':
        '<span class="sector-name">ERNEUERBARE</span> <span class="sector-fact">Kabelarbeiten und Servicearbeiten an Windenergieanlagen in Windparks</span>',
    '<span>Offshore Oil &amp; Gas</span><span>Wind Energy</span><span>Industrial Facilities</span><span>Steel Structures</span>':
        '<span>Offshore-Öl &amp; -Gas</span><span>Windenergie</span><span>Industrieanlagen</span><span>Stahlkonstruktionen</span>',
    'Certified to deliver safety, quality and compliance &mdash; <span class="certs-body">independently certified by DNV</span>':
        'Zertifiziert für Sicherheit, Qualität und Konformität &mdash; <span class="certs-body">unabhängig zertifiziert durch DNV</span>',
    'Send the drawings or the scope and we will come back with a price and crew dates. If it is a shutdown, tell us the window.':
        'Senden Sie die Zeichnungen oder den Leistungsumfang und wir melden uns mit Preis und Einsatzterminen. Bei einem Stillstand nennen Sie uns bitte das Zeitfenster.',
    'The calendar is hosted by Calendly. It loads only when you press the button, so nothing reaches them before you ask for it.':
        'Der Kalender wird von Calendly gehostet. Er lädt erst, wenn Sie die Schaltfläche drücken — vorher erreicht Calendly nichts über Sie.',
    'Work in progress, completed scopes, and what we are learning across shipbuilding, offshore, industrial and energy projects.':
        'Laufende Arbeiten, abgeschlossene Projekte und was wir in Schiffbau, Offshore, Industrie und Energie lernen.',
    'Cable installation, rigging and offshore support on wind farms, plus the fuel handling infrastructure that sits behind them.':
        'Kabelverlegung, Hebetechnik und Offshore-Unterstützung in Windparks, dazu die dahinterliegende Infrastruktur für den Kraftstoffumschlag.',
    'ALPROJECTS Group is a European provider of industrial services for the shipbuilding, offshore, industrial and energy sectors.':
        'ALPROJECTS Group ist ein europäischer Anbieter industrieller Dienstleistungen für Schiffbau, Offshore, Industrie und Energie.',
    'ALPROJECTS Group serves the shipbuilding, offshore, industrial and energy sectors, from a head office in Klaipėda, Lithuania.':
        'ALPROJECTS Group ist in Schiffbau, Offshore, Industrie und Energie tätig, mit Hauptsitz in Klaipėda, Litauen.',
    'Attach your CV and certificates to the email that opens when you submit &mdash; we do not accept file uploads through this page.':
        'Fügen Sie Lebenslauf und Zeugnisse der E-Mail bei, die sich beim Absenden öffnet &mdash; über diese Seite nehmen wir keine Dateien entgegen.',
    '<span class="sector-name">SHIPBUILDING</span> <span class="sector-fact">Engine room piping, structural steel and outfitting</span>':
        '<span class="sector-name">SCHIFFBAU</span> <span class="sector-fact">Maschinenraumrohrleitungen, Stahlbau und Ausrüstung</span>',
    'Lithuania &middot; Belgium &middot; Norway &mdash; serving offshore, shipbuilding and industry across Northern and Western Europe.':
        'Litauen &middot; Belgien &middot; Norwegen &mdash; für Offshore, Schiffbau und Industrie in Nord- und Westeuropa.',
    '<span class="value" data-count="90" data-suffix="+">0+</span> <span class="label">Projects delivered across multiple countries</span>':
        '<span class="value" data-count="90" data-suffix="+">0+</span> <span class="label">Projekte in mehreren Ländern ausgeführt</span>',
    '<span class="value" data-count="98" data-suffix="%">0%</span> <span class="label">Early risk detection by certified specialists</span>':
        '<span class="value" data-count="98" data-suffix="%">0%</span> <span class="label">Frühe Risikoerkennung durch zertifizierte Fachkräfte</span>',
    'ALPROJECTS, UAB (&ldquo;ALPROJECTS Group&rdquo;, &ldquo;we&rdquo;) is the controller of personal data collected through alprojects.co.':
        'ALPROJECTS, UAB (&ldquo;ALPROJECTS Group&rdquo;, &ldquo;wir&rdquo;) ist Verantwortlicher für die über alprojects.co erhobenen personenbezogenen Daten.',
    'Plant installation, process piping and mechanical packages, delivered as a whole scope with our own supervisors and our own QA on site.':
        'Anlagenmontage, Prozessrohrleitungen und mechanische Pakete, als Gesamtumfang ausgeführt mit eigenen Bauleitern und eigener QS vor Ort.',
    'Recruiting thirty certified TIG welders for a single scope of work turned out to be materially harder than the engineering it supported.':
        'Dreißig zertifizierte WIG-Schweißer für einen einzigen Leistungsumfang zu finden war deutlich schwieriger als die Technik, die dahinterstand.',
    'That matters more than a logo on a wall. It is the difference between a contractor who can carry a scope to completion and one who cannot.':
        'Das zählt mehr als ein Logo an der Wand. Es ist der Unterschied zwischen einem Auftragnehmer, der einen Umfang zu Ende bringt, und einem, der es nicht kann.',
    '<span class="value" data-count="40" data-suffix="%">0%</span> <span class="label">Reduced inspection time through optimized workflows</span>':
        '<span class="value" data-count="40" data-suffix="%">0%</span> <span class="label">Kürzere Prüfzeiten durch optimierte Abläufe</span>',
    'Job applications, including any CV and certificates, are kept for 24 months from the date you send them, or until you ask us to delete them.':
        'Bewerbungen einschließlich Lebenslauf und Zeugnissen werden 24 Monate ab Eingang gespeichert oder bis Sie deren Löschung verlangen.',
    'Old drawings lie. We measure what is really there and hand the data to your engineers, so the clash shows up on a screen instead of on site.':
        'Alte Zeichnungen lügen. Wir messen den tatsächlichen Bestand und übergeben die Daten Ihren Ingenieuren — die Kollision zeigt sich am Bildschirm statt auf der Baustelle.',
    '<span class="value" data-count="1200" data-suffix="+">0+</span> <span class="label">Safe execution in complex and confined environments</span>':
        '<span class="value" data-count="1200" data-suffix="+">0+</span> <span class="label">Sichere Ausführung in komplexen und beengten Umgebungen</span>',
    'Delivered projects with photography from site — shipyards, offshore structures, industrial plants and energy terminals across Northern Europe.':
        'Ausgeführte Projekte mit Aufnahmen von der Baustelle — Werften, Offshore-Strukturen, Industrieanlagen und Energieterminals in ganz Europa und Skandinavien.',
    'Yard schedules do not move. Our crews slot into them and take engine room piping, structural steel and outfitting, on newbuilds and on repair.':
        'Werftterminpläne verschieben sich nicht. Unsere Teams fügen sich ein und übernehmen Maschinenraumrohrleitungen, Stahlbau und Ausrüstung, bei Neubau wie Reparatur.',
    'Project enquiries, personnel requests and open applications all reach the same inbox — it is read by people who can answer technical questions.':
        'Projektanfragen, Personalanfragen und Initiativbewerbungen landen im selben Postfach — gelesen von Menschen, die technische Fragen beantworten können.',
    'The scope ran from September 2025 to April 2026 and was delivered by a team of twelve specialists, accumulating more than 11,000 hours on site.':
        'Das Projekt lief von September 2025 bis April 2026 und wurde von einem Team aus zwölf Fachkräften ausgeführt, mit über 11.000 Stunden vor Ort.',
    '<span class="fp-idx">06</span> <span class="fp-name">Belgium</span> <span class="fp-badge">1 location</span> <span class="fp-city">Antwerp</span>':
        '<span class="fp-idx">06</span> <span class="fp-name">Belgien</span> <span class="fp-badge">1 Standort</span> <span class="fp-city">Antwerpen</span>',
    'The order of work stays the same on every job. Most of the time in a machinery space goes on getting the routing right, not on the welding itself.':
        'Die Reihenfolge der Arbeiten bleibt auf jeder Baustelle gleich. Im Maschinenraum geht die meiste Zeit in die richtige Leitungsführung, nicht in das Schweißen selbst.',
    'Work with ALPROJECTS Group — welding, pipe fitting, NDT, rope access and mechanical contracting on industrial and offshore projects across Europe.':
        'Arbeiten bei ALPROJECTS Group — Schweißtechnik, Rohrleitungsbau, ZfP, Seilzugangstechnik und Anlagenmontage auf Industrie- und Offshore-Projekten in ganz Europa.',
    'Welding, pipe fitting, mechanical contracting, marine works, NDT, rope access and quality control for industrial and offshore projects across Europe.':
        'Schweißtechnik, Rohrleitungsbau, Anlagenmontage, Schiffbauarbeiten, ZfP, Seilzugangstechnik und Qualitätskontrolle für Industrie- und Offshore-Projekte in ganz Europa.',
    '<span class="fp-idx">05</span> <span class="fp-name">Lithuania</span> <span class="fp-badge">Headquarters</span> <span class="fp-city">Klaipėda</span>':
        '<span class="fp-idx">05</span> <span class="fp-name">Litauen</span> <span class="fp-badge">Hauptsitz</span> <span class="fp-city">Klaipėda</span>',
    'Mobilising a team offshore is expensive and a shutdown is more expensive still. Rope access and NDT carry most of this work, with mechanical scopes al':
        'Ein Team offshore zu mobilisieren ist teuer, ein Stillstand noch teurer. Seilzugangstechnik und ZfP tragen den größten Teil dieser Arbeit, ergänzt um',
    '<span class="fp-idx">03</span> <span class="fp-name">Netherlands</span> <span class="fp-badge">1 location</span> <span class="fp-city">Rotterdam</span>':
        '<span class="fp-idx">03</span> <span class="fp-name">Niederlande</span> <span class="fp-badge">1 Standort</span> <span class="fp-city">Rotterdam</span>',
    "Repair work is decided in days, not months. We take steel renewal, piping replacement and mechanical repairs, to class and to the owner's requirements.":
        'Über Reparaturen wird in Tagen entschieden, nicht in Monaten. Wir übernehmen Stahlerneuerung, Rohrleitungstausch und mechanische Instandsetzung, nach Klassevorgaben und Anforderungen des Reeders.',
    'Scaffolding costs more in downtime than in steel. Certified technicians reach the same place on rope, inspect it and repair it while the plant keeps...':
        'Ein Gerüst kostet mehr an Stillstand als an Stahl. Zertifizierte Techniker erreichen dieselbe Stelle am Seil, prüfen und reparieren sie, während die Anlage...',
    'A weld is only as good as the paperwork behind it. We weld structural steel and piping systems in TIG, MIG and semi-automatic processes, under an ISO...':
        'Eine Schweißnaht ist nur so gut wie ihre Dokumentation. Wir schweißen Stahlbau und Rohrleitungssysteme im WIG-, MIG- und teilmechanisierten Verfahren, unter einem ISO...',
    'Nobody should be signing off their own work. We inspect welds, materials and structures without stopping production, and we report to the client, not...':
        'Niemand sollte die eigene Arbeit freigeben. Wir prüfen Schweißnähte, Werkstoffe und Konstruktionen ohne Produktionsstillstand und berichten an den Kunden, nicht...',
    'Some clients need the whole scope taken off their hands. We install plant and equipment, fabricate steel and build transformer packages, with our own...':
        'Manche Kunden wollen den gesamten Umfang abgeben. Wir montieren Anlagen und Ausrüstung, fertigen Stahlbau und bauen Transformatorenpakete, mit eigenen...',
    '<strong>Newsletter.</strong> If you submit the newsletter form, we receive the email address you enter, in order to send you company and project updates.':
        '<strong>Newsletter.</strong> Wenn Sie das Newsletter-Formular absenden, erhalten wir die eingegebene E-Mail-Adresse, um Ihnen Unternehmens- und Projektnachrichten zu senden.',
    'Most delays in piping start with a bad fit-up. We supply fitters for process, utility and engine room systems, instrument fitters for small bore work,...':
        'Die meisten Verzögerungen im Rohrleitungsbau beginnen mit einer schlechten Passung. Wir stellen Monteure für Prozess-, Versorgungs- und Maschinenraumsysteme, Monteure für Mess- und Instrumentierungsleitungen für kleine Nennweiten,...',
    'Outline map of Europe marking the six countries ALPROJECTS Group operates in: Norway, the United Kingdom, the Netherlands, Belgium, Germany and Lithuania':
        'Umrisskarte Europas mit den sechs Ländern, in denen ALPROJECTS Group tätig ist: Norwegen, Vereinigtes Königreich, Niederlande, Belgien, Deutschland und Litauen',
    '<span class="fp-idx">02</span> <span class="fp-name">United Kingdom</span> <span class="fp-badge">1 location</span> <span class="fp-city">Newcastle</span>':
        '<span class="fp-idx">02</span> <span class="fp-name">Vereinigtes Königreich</span> <span class="fp-badge">1 Standort</span> <span class="fp-city">Newcastle</span>',
    'Every hour a unit stays down has a price. Our crews mobilise at short notice for turnarounds, shutdowns and breakdowns, and they carry welding, fitting...':
        'Jede Stunde Stillstand einer Anlage kostet Geld. Unsere Teams mobilisieren kurzfristig für Großstillstände, Anlagenstillstände und Störungen und vereinen Schweißen, Montage...',
    'Moving a production line is a scheduling problem before it is a lifting problem. We dismantle, move, re-install and align it, inside a running plant or...':
        'Eine Produktionslinie zu verlagern ist zuerst ein Terminproblem, dann ein Hebeproblem. Wir demontieren, verlagern, montieren neu und richten aus, in laufender Anlage oder...',
    'Quality is what you can prove afterwards. We inspect piping and steel structures and leave documentation that holds up when the client, the surveyor or...':
        'Qualität ist das, was sich hinterher belegen lässt. Wir prüfen Rohrleitungen und Stahlbau und hinterlassen eine Dokumentation, die standhält, wenn Kunde, Besichtiger oder...',
    'Who we are, where we operate, the sectors we serve and the standards we are certified to. Includes our footprint across six countries and selected clients.':
        'Wer wir sind, wo wir tätig sind, welche Branchen wir bedienen und nach welchen Normen wir zertifiziert sind. Mit unserer Präsenz in sechs Ländern und ausgewählten Kunden.',
    '<span class="fp-idx">01</span> <span class="fp-name">Norway</span> <span class="fp-badge">2 locations</span> <span class="fp-city">Ålesund · Orkanger</span>':
        '<span class="fp-idx">01</span> <span class="fp-name">Norwegen</span> <span class="fp-badge">2 Standorte</span> <span class="fp-city">Ålesund · Orkanger</span>',
    'I agree that ALPROJECTS may store these details to consider me for current and future roles, as described in the <a href="/privacy">privacy policy</a>.':
        'Ich bin damit einverstanden, dass ALPROJECTS diese Angaben speichert, um mich für aktuelle und künftige Stellen zu berücksichtigen, wie in der <a href="/privacy">Datenschutzerklärung</a> beschrieben.',
    'Repair work is decided in days, not months. We take steel renewal, piping replacement and mechanical repairs, to class and to the owner&rsquo;s requirements.':
        'Über Reparaturen wird in Tagen entschieden, nicht in Monaten. Wir übernehmen Stahlerneuerung, Rohrleitungstausch und mechanische Instandsetzung, nach Klassevorgaben und Anforderungen des Reeders.',
    'Scaffolding costs more in downtime than in steel. Certified technicians reach the same place on rope, inspect it and repair it while the plant keeps running.':
        'Ein Gerüst kostet mehr an Stillstand als an Stahl. Zertifizierte Techniker erreichen dieselbe Stelle am Seil, prüfen und reparieren sie, während die Anlage weiterläuft.',
    'Mobilising a team offshore is expensive and a shutdown is more expensive still. Rope access and NDT carry most of this work, with mechanical scopes alongside.':
        'Ein Team offshore zu mobilisieren ist teuer, ein Stillstand noch teurer. Seilzugangstechnik und ZfP tragen den größten Teil dieser Arbeit, ergänzt um mechanische Leistungen.',
    'ALPROJECTS Group delivers mechanical contracting, pipe fitting, welding, QAQC, rope access and NDT services for industrial and offshore projects across Europe.':
        'ALPROJECTS Group erbringt Anlagenmontage, Rohrleitungsbau, Schweißtechnik, QA/QC, Seilzugangstechnik und ZfP für Industrie- und Offshore-Projekte in ganz Europa.',
    '<span class="kp-num">04</span> <span class="kp-name">Hywind Tampen</span> <span class="kp-scope">Rotational team support for offshore pull-in operations.</span>':
        '<span class="kp-num">04</span> <span class="kp-name">Hywind Tampen</span> <span class="kp-scope">Teams im Rotationseinsatz zur Unterstützung von Offshore-Einzugsarbeiten.</span>',
    'Four project types, one set of disciplines. The engineering is largely the same; the environment, the standards and the consequences of getting it wrong are not.':
        'Vier Projektarten, ein Satz an Gewerken. Die Technik ist weitgehend dieselbe; die Umgebung, die Normen und die Folgen eines Fehlers sind es nicht.',
    'We are recruiting thirty certified TIG welders for upcoming project scopes. This is the constraint on our current pipeline, so applications are reviewed quickly.':
        'Wir suchen dreißig zertifizierte WIG-Schweißer für anstehende Projekte. Das ist derzeit der Engpass in unserer Auftragslage, deshalb werden Bewerbungen schnell geprüft.',
    'Welding is carried out under <strong>ISO 3834</strong>. Every joint is documented, and NDT and pressure testing are done before insulation and final coating go on.':
        'Geschweißt wird nach <strong>ISO 3834</strong>. Jede Naht wird dokumentiert; ZfP und Druckprüfung erfolgen vor Isolierung und Endbeschichtung.',
    '<span class="kp-num">03</span> <span class="kp-name">Ostwind Offshore Wind Farm</span> <span class="kp-scope">Cable jointers, cable mates and rigging support.</span>':
        '<span class="kp-num">03</span> <span class="kp-name">Offshore-Windpark Ostwind</span> <span class="kp-scope">Kabelmonteure, Kabelhelfer und Unterstützung bei der Hebetechnik.</span>',
    'Consistency across borders is a documentation problem as much as a fabrication one — which is where certified personnel and a single quality system earn their place.':
        'Gleichbleibende Qualität über Ländergrenzen hinweg ist ebenso eine Frage der Dokumentation wie der Fertigung — genau dort zahlen sich zertifiziertes Personal und ein einheitliches Qualitätssystem aus.',
    'We perform NDT inspections of welds, materials and structures without interrupting operations. Defects are identified at early stages to ensure safety and compliance.':
        'Wir führen ZfP an Schweißnähten, Werkstoffen und Konstruktionen durch, ohne den Betrieb zu unterbrechen. Fehler werden früh erkannt, um Sicherheit und Konformität zu gewährleisten.',
    '<span>© 2019–2026 ALPROJECTS GROUP. All rights reserved.</span> <a class="made-by" href="https://aldystudio.com" target="_blank" rel="noopener">Made by <b>ALDY</b></a>':
        '<span>© 2019–2026 ALPROJECTS GROUP. Alle Rechte vorbehalten.</span> <a class="made-by" href="https://aldystudio.com" target="_blank" rel="noopener">Umgesetzt von <b>ALDY</b></a>',
    '<span class="fp-idx">04</span> <span class="fp-name">Germany</span> <span class="fp-badge">3 locations</span> <span class="fp-city">Rostock · Hamburg · Frankfurt</span>':
        '<span class="fp-idx">04</span> <span class="fp-name">Deutschland</span> <span class="fp-badge">3 Standorte</span> <span class="fp-city">Rostock · Hamburg · Frankfurt</span>',
    '<strong>Direct contact.</strong> If you email or call us, we receive whatever you choose to send — typically your name, contact details and the content of your enquiry.':
        '<strong>Direkter Kontakt.</strong> Wenn Sie uns schreiben oder anrufen, erhalten wir, was Sie übermitteln — in der Regel Ihren Namen, Ihre Kontaktdaten und den Inhalt Ihrer Anfrage.',
    'Even when a role is not advertised, we keep qualified specialists on file and make contact when a project matches. These are the areas our project teams are built from:':
        'Auch ohne ausgeschriebene Stelle nehmen wir qualifizierte Fachkräfte in unsere Kartei auf und melden uns, sobald ein Projekt passt. Aus diesen Bereichen bauen wir unsere Projektteams:',
    'Some clients need the whole scope taken off their hands. We install plant and equipment, fabricate steel and build transformer packages, with our own supervisors on site.':
        'Manche Kunden wollen den gesamten Umfang abgeben. Wir montieren Anlagen und Ausrüstung, fertigen Stahlbau und bauen Transformatorenpakete, mit eigenen Bauleitern vor Ort.',
    '<span class="kp-num">02</span> <span class="kp-name">Thor Offshore Wind Farm</span> <span class="kp-scope">Cable installation, rigging and offshore support services.</span>':
        '<span class="kp-num">02</span> <span class="kp-name">Offshore-Windpark Thor</span> <span class="kp-scope">Kabelverlegung, Hebetechnik und Offshore-Unterstützung.</span>',
    'Moving a production line is a scheduling problem before it is a lifting problem. We dismantle, move, re-install and align it, inside a running plant or between two countries.':
        'Eine Produktionslinie zu verlagern ist zuerst ein Terminproblem, dann ein Hebeproblem. Wir demontieren, verlagern, montieren neu und richten aus, in laufender Anlage oder zwischen zwei Ländern.',
    'Quality is what you can prove afterwards. We inspect piping and steel structures and leave documentation that holds up when the client, the surveyor or the auditor asks for it.':
        'Qualität ist das, was sich hinterher belegen lässt. Wir prüfen Rohrleitungen und Stahlbau und hinterlassen eine Dokumentation, die standhält, wenn Kunde, Besichtiger oder Auditor sie verlangt.',
    '<strong>Welded, tested, then closed.</strong> Welding under ISO 3834. Every joint is documented, and NDT and pressure testing are done before insulation and final coating go on.':
        '<strong>Geschweißt, geprüft, dann geschlossen.</strong> Geschweißt wird nach ISO 3834. Jede Naht wird dokumentiert; ZfP und Druckprüfung erfolgen vor Isolierung und Endbeschichtung.',
    'Even when a role is not advertised we keep qualified specialists on file and make contact when a project matches. Select your discipline and it goes straight into the form below.':
        'Auch ohne ausgeschriebene Stelle nehmen wir qualifizierte Fachkräfte in unsere Kartei auf und melden uns, sobald ein Projekt passt. Wählen Sie Ihr Gewerk — es wird direkt in das Formular unten übernommen.',
    'We deliver mechanical contracting, welding, inspection and access services on industrial and offshore projects across Europe. The work is technical, certified and mostly on site.':
        'Wir erbringen Anlagenmontage, Schweißtechnik, Prüf- und Zugangsleistungen auf Industrie- und Offshore-Projekten in ganz Europa. Die Arbeit ist technisch, zertifiziert und überwiegend vor Ort.',
    '<strong>Server logs.</strong> The site is hosted on GitHub Pages. GitHub records technical request data, including IP address and browser user-agent, for security and reliability.':
        '<strong>Server-Protokolle.</strong> Die Website wird auf GitHub Pages gehostet. GitHub erfasst technische Zugriffsdaten, darunter IP-Adresse und Browserkennung, zu Zwecken der Sicherheit und Verfügbarkeit.',
    'Numbers like 11,000 hours are worth stating plainly: they are what a project of this size actually costs in skilled labour, and planning against a lower figure is how schedules fail.':
        'Zahlen wie 11.000 Stunden gehören klar benannt: So viel kostet ein Projekt dieser Größe tatsächlich an Facharbeit, und mit einer niedrigeren Annahme zu planen ist der Weg zu gerissenen Terminen.',
    'ALPROJECTS, UAB<br>Šilutės pl. 2, LT-92298 Klaipėda, Lithuania<br> <a href="mailto:info@alprojects.eu">info@alprojects.eu</a> &middot; <a href="tel:+37063663744">+370 636 63 744</a>':
        'ALPROJECTS, UAB<br>Šilutės pl. 2, LT-92298 Klaipėda, Litauen<br> <a href="mailto:info@alprojects.eu">info@alprojects.eu</a> &middot; <a href="tel:+37063663744">+370 636 63 744</a>',
    'It is worth being direct about this, because the answer is not a recruitment campaign. It is training, certification pathways, and treating the trades as a career rather than a stopgap.':
        'Man sollte das offen sagen, denn die Antwort ist keine Recruiting-Kampagne. Sie heißt Ausbildung, Qualifizierungswege und die Anerkennung dieser Berufe als Laufbahn statt als Notlösung.',
    'Scope on all three: inspection and industrial maintenance services for onshore and offshore installations. Issued by DNV Business Assurance Finland. Select a certificate to open the PDF.':
        'Geltungsbereich aller drei: Prüf- und Instandhaltungsleistungen für Onshore- und Offshore-Anlagen. Ausgestellt von DNV Business Assurance Finland. Wählen Sie ein Zertifikat, um das PDF zu öffnen.',
    '<strong>Consent</strong> (GDPR Art. 6(1)(a)) — newsletter subscription, and loading the scheduling calendar, which happens only when you press the button. You may withdraw it at any time.':
        '<strong>Einwilligung</strong> (DSGVO Art. 6 Abs. 1 lit. a) — Newsletter-Anmeldung und das Laden des Terminkalenders, das nur nach Klick auf die Schaltfläche erfolgt. Sie können sie jederzeit widerrufen.',
    'Head office in Klaipėda, Lithuania, with operations in <strong>Belgium</strong> and <strong>Norway</strong>, serving offshore, shipbuilding and industry across Northern and Western Europe.':
        'Hauptsitz in Klaipėda, Litauen, mit Niederlassungen in <strong>Belgien</strong> und <strong>Norwegen</strong>, für Offshore, Schiffbau und Industrie in Nord- und Westeuropa.',
    'Nobody should be signing off their own work. We inspect welds, materials and structures without stopping production, and we report to the client, not to the contractor who did the welding.':
        'Niemand sollte die eigene Arbeit freigeben. Wir prüfen Schweißnähte, Werkstoffe und Konstruktionen ohne Produktionsstillstand und berichten an den Kunden, nicht an die Firma, die geschweißt hat.',
    '<span class="kp-num">01</span> <span class="kp-name">SylWin Alpha Converter Platform</span> <span class="kp-scope">Offshore bridge repairs, steel fitting and structural welding works.</span>':
        '<span class="kp-num">01</span> <span class="kp-name">Konverterplattform SylWin Alpha</span> <span class="kp-scope">Instandsetzung von Offshore-Brücken, Stahlbaumontage und Konstruktionsschweißen.</span>',
    'Every hour a unit stays down has a price. Our crews mobilise at short notice for turnarounds, shutdowns and breakdowns, and they carry welding, fitting and mechanical skills in the same team.':
        'Jede Stunde Stillstand einer Anlage kostet Geld. Unsere Teams mobilisieren kurzfristig für Großstillstände, Anlagenstillstände und Störungen und vereinen Schweißen, Montage und Mechanik in einem Team.',
    'Our own technicians come in before that. They go over the joint while the crew is still on the job, and if something has to come out, it comes out before anyone else is invited to look at it.':
        'Unsere eigenen Techniker kommen davor. Sie prüfen die Naht, solange die Mannschaft noch vor Ort ist, und wenn etwas heraus muss, kommt es heraus, bevor irgendjemand sonst hinsieht.',
    'Our crew is installing engine room systems on vessels under construction: seawater, bilge, ballast, fuel and service lines running from small bore up to DN200 around the main engine foundations.':
        'Unser Team montiert Maschinenraumsysteme auf Schiffen im Bau: Seewasser-, Bilge-, Ballast-, Kraftstoff- und Versorgungsleitungen von kleinen Nennweiten bis DN200 rund um die Hauptmaschinenfundamente.',
    '<strong>Manifolds, sea chests, tank connections.</strong> Gate valves, strainers and remote operated units set out and aligned on the tank top. Flange faces stay capped until the system is closed.':
        '<strong>Verteiler, Seekästen, Tankanschlüsse.</strong> Absperrschieber, Schmutzfänger und fernbetätigte Armaturen werden auf der Tankdecke ausgelegt und ausgerichtet. Flanschflächen bleiben verschlossen, bis das System geschlossen ist.',
    'The certificate recognises companies with a high credit score and a proven record of financial stability. It is issued by Creditinfo Group and was awarded on 23 June 2026 for the 2025–2026 period.':
        'Das Zertifikat zeichnet Unternehmen mit hoher Bonität und nachgewiesener finanzieller Stabilität aus. Es wird von der Creditinfo Group ausgestellt und wurde am 23. Juni 2026 für den Zeitraum 2025–2026 verliehen.',
    '<strong>Drawn first, then built.</strong> Isometrics are checked before anything is cut. Spools are prefabricated in the shop, fitted on board and hung so the line can move without loading the welds.':
        '<strong>Erst gezeichnet, dann gebaut.</strong> Isometrien werden geprüft, bevor etwas geschnitten wird. Spools werden in der Werkstatt vorgefertigt, an Bord eingepasst und so aufgehängt, dass sich die Leitung bewegen kann, ohne die Nähte zu belasten.',
    'If you believe we have handled your data improperly, you may lodge a complaint with the Lithuanian State Data Protection Inspectorate (Valstybine duomenu apsaugos inspekcija), L. Sapiegos g. 17, Vilnius.':
        'Wenn Sie der Ansicht sind, dass wir Ihre Daten unrechtmäßig verarbeitet haben, können Sie Beschwerde bei der litauischen Datenschutzaufsicht (Valstybine duomenu apsaugos inspekcija), L. Sapiegos g. 17, Vilnius, einlegen.',
    'You can also send them to <a href="mailto:info@alprojects.eu?subject=CV%20and%20certificates">info@alprojects.eu</a> or by <a href="https://wa.me/37063663744" target="_blank" rel="noopener">WhatsApp</a>.':
        'Sie können sie auch an <a href="mailto:info@alprojects.eu?subject=CV%20and%20certificates">info@alprojects.eu</a> oder per <a href="https://wa.me/37063663744" target="_blank" rel="noopener">WhatsApp</a> senden.',
    '<strong>Consent</strong> (GDPR Art. 6(1)(a)) — newsletter subscription, job applications, and loading the scheduling calendar, which happens only when you press the button. You may withdraw it at any time.':
        '<strong>Einwilligung</strong> (DSGVO Art. 6 Abs. 1 lit. a) — Newsletter-Anmeldung, Bewerbungen und das Laden des Terminkalenders, das nur nach Klick auf die Schaltfläche erfolgt. Sie können sie jederzeit widerrufen.',
    'A transformer mechanical package covers the stainless steel piping and cooling systems that keep the unit within its operating envelope. The tolerances are tight and the commissioning window is usually short.':
        'Ein mechanisches Transformatorenpaket umfasst die Edelstahlrohrleitungen und Kühlsysteme, die das Gerät in seinem Betriebsbereich halten. Die Toleranzen sind eng und das Zeitfenster für die Inbetriebnahme meist kurz.',
    'What made this scope demanding was not any single site but the repetition: the same package delivered across five European countries, each with its own site conditions, inspection regime and local requirements.':
        'Anspruchsvoll war an diesem Auftrag nicht ein einzelner Standort, sondern die Wiederholung: dasselbe Paket in fünf europäischen Ländern, jedes mit eigenen Baustellenbedingungen, Prüfregimen und örtlichen Anforderungen.',
    'CVs and certificate documents are stored with the application and are seen only by the people resourcing projects. We do not pass them to third parties, and we do not use them for anything other than recruitment.':
        'Lebensläufe und Zeugnisse werden zusammen mit der Bewerbung gespeichert und nur von den Personen eingesehen, die Projekte besetzen. Wir geben sie nicht an Dritte weiter und nutzen sie ausschließlich für die Personalgewinnung.',
    'UAB &ldquo;ALprojects&rdquo; holds the <strong>Strongest in Lithuania</strong> certificate, awarded by Creditinfo Group on 23 June 2026 to companies with a high credit score and a proven record of financial stability.':
        'UAB &ldquo;ALprojects&rdquo; ist Träger des Zertifikats <strong>Strongest in Lithuania</strong>, das die Creditinfo Group am 23. Juni 2026 an Unternehmen mit hoher Bonität und nachgewiesener finanzieller Stabilität verliehen hat.',
    '<strong>Booking a call.</strong> If you open the scheduling calendar on the contacts page and book a slot, Calendly receives the name, email address and any notes you enter, together with your IP address and time zone.':
        '<strong>Terminbuchung.</strong> Wenn Sie den Kalender auf der Kontaktseite öffnen und einen Termin buchen, erhält Calendly den eingegebenen Namen, die E-Mail-Adresse und etwaige Anmerkungen sowie Ihre IP-Adresse und Zeitzone.',
    'Fuel handling infrastructure concentrates every discipline we work in — mechanical installation, pipe fitting, welding, and the inspection and documentation that has to accompany all three when the medium is flammable.':
        'Infrastruktur für den Kraftstoffumschlag bündelt alle unsere Gewerke — mechanische Montage, Rohrleitungsbau, Schweißen sowie die Prüfung und Dokumentation, die alle drei begleiten muss, wenn das Medium brennbar ist.',
    'Execution quality control for piping and steel structures. Inspection and verification in accordance with WPS, drawings and applicable standards. Traceability, documentation and control maintained throughout all stages.':
        'Ausführungsüberwachung für Rohrleitungen und Stahlbau. Prüfung und Verifizierung nach Schweißanweisung, Zeichnungen und geltenden Normen. Rückverfolgbarkeit, Dokumentation und Kontrolle über alle Phasen hinweg.',
    '<strong>Measured against the criteria.</strong> Cap height, width, undercut, profile. Each one is checked against the acceptance criteria for the job, and the joint is not presented until the numbers sit inside the limits.':
        '<strong>An den Kriterien gemessen.</strong> Nahtüberhöhung, Breite, Einbrandkerbe, Profil. Jeder Wert wird gegen die Abnahmekriterien des Auftrags geprüft, und die Naht wird erst vorgelegt, wenn die Werte innerhalb der Grenzen liegen.',
    '<strong>A stable partner is a safer project.</strong> In heavy industry, projects run for months and commitments run for years. Independent proof of financial stability is proof that we will be there to see the work through.':
        '<strong>Ein solider Partner ist ein sichereres Projekt.</strong> In der Schwerindustrie laufen Projekte über Monate und Verpflichtungen über Jahre. Ein unabhängiger Nachweis finanzieller Stabilität ist der Beleg dafür, dass wir bis zum Ende dabei sind.',
    'Simply browsing this site loads no third-party scripts, fonts, analytics or embeds. The typeface is served from our own domain, so reading these pages does not disclose your IP address to any advertising or analytics company.':
        'Das bloße Besuchen dieser Website lädt keine Skripte, Schriften, Analysewerkzeuge oder eingebetteten Inhalte Dritter. Die Schrift wird von unserer eigenen Domain ausgeliefert; das Lesen dieser Seiten gibt Ihre IP-Adresse also an kein Werbe- oder Analyseunternehmen weiter.',
    "So there are two different things with the same equipment behind them. On our own jobs it is internal quality control, and it never counts as sign-off. On somebody else's welds it is independent NDT, because we did not weld it.":
        'Es sind also zwei verschiedene Dinge mit derselben Technik dahinter. Auf eigenen Baustellen ist es interne Qualitätskontrolle, und sie gilt nie als Freigabe. An fremden Schweißnähten ist es unabhängige ZfP, weil wir sie nicht geschweißt haben.',
    'I agree that ALPROJECTS, UAB stores my details and documents for recruitment purposes for 24 months. I can ask for them to be deleted at any time by writing to info@alprojects.eu. See the <a href="/privacy">privacy policy</a>.':
        'Ich bin damit einverstanden, dass ALPROJECTS, UAB meine Angaben und Unterlagen zu Zwecken der Personalgewinnung 24 Monate speichert. Ich kann ihre Löschung jederzeit per E-Mail an info@alprojects.eu verlangen. Siehe die <a href="/privacy">Datenschutzerklärung</a>.',
    '<strong>Where the line sits.</strong> Nobody should be signing off their own work, and we do not try to. Independent verification stays where the contract puts it, normally with the client or the class surveyor, and nothing we do changes that.':
        '<strong>Wo die Grenze liegt.</strong> Niemand sollte die eigene Arbeit freigeben, und wir versuchen es auch nicht. Die unabhängige Prüfung bleibt dort, wo der Vertrag sie vorsieht, in der Regel beim Kunden oder beim Besichtiger der Klassifikationsgesellschaft — daran ändern wir nichts.',
    'The shortage is discussed across European industry in general terms. It becomes concrete when a project is resourced, scheduled and funded, and the constraint is simply the number of people who hold the certification and are willing to travel.':
        'In der europäischen Industrie wird der Mangel allgemein diskutiert. Konkret wird er, wenn ein Projekt besetzt, terminiert und finanziert ist und der Engpass schlicht die Zahl der Menschen ist, die die Qualifikation haben und reisen wollen.',
    '<strong>Job applications.</strong> If you send the careers form we receive the details you enter &mdash; name, contact details, discipline, certificates, availability and any notes &mdash; together with any CV or certificate documents you attach.':
        '<strong>Bewerbungen.</strong> Wenn Sie das Bewerbungsformular absenden, erhalten wir die eingegebenen Angaben &mdash; Name, Kontaktdaten, Gewerk, Zertifikate, Verfügbarkeit und Bemerkungen &mdash; sowie die von Ihnen angehängten Lebenslauf- und Zeugnisunterlagen.',
    '<strong>What the eye cannot pick up.</strong> Clean the weld, apply the penetrant, let the developer draw it back out. Surface cracks and porosity that nobody would catch by eye show up in red, and anything outside the limits is repaired on the spot.':
        '<strong>Was das Auge nicht sieht.</strong> Naht reinigen, Eindringmittel auftragen, Entwickler es wieder herausziehen lassen. Oberflächenrisse und Poren, die niemand mit bloßem Auge fände, zeichnen sich rot ab; alles außerhalb der Grenzwerte wird sofort nachgearbeitet.',
    'The company employs between 51 and 200 people directly and draws on a roster of more than 300 certified specialists across Europe. Projects are resourced from that roster rather than subcontracted on, which is what keeps the quality system meaningful.':
        'Das Unternehmen beschäftigt direkt zwischen 51 und 200 Mitarbeitende und greift auf einen Pool von über 300 zertifizierten Fachkräften in ganz Europa zurück. Projekte werden aus diesem Pool besetzt statt weitervergeben — nur so bleibt das Qualitätssystem aussagekräftig.',
    'Execution of 3D laser scanning to capture precise as-built geometry of structures and piping systems. Point cloud data supports dimensional control, clash detection and retrofit engineering. Improves accuracy and reduces rework during installation and fabrication.':
        '3D-Laserscanning zur genauen Erfassung der Bestandsgeometrie von Konstruktionen und Rohrleitungssystemen. Die Punktwolke dient der Maßkontrolle, der Kollisionsprüfung und der Umbauplanung. Das erhöht die Genauigkeit und reduziert Nacharbeit bei Fertigung und Montage.',
    'A weld is only as good as the paperwork behind it. We weld structural steel and piping systems in TIG, MIG and semi-automatic processes, under an ISO 3834 quality system. The welders hold current qualifications and the procedure is approved before the first arc is struck.':
        'Eine Schweißnaht ist nur so gut wie ihre Dokumentation. Wir schweißen Stahlbau und Rohrleitungssysteme im WIG-, MIG- und teilmechanisierten Verfahren, unter einem Qualitätssystem nach ISO 3834. Die Schweißer haben gültige Prüfungen und das Verfahren ist freigegeben, bevor der erste Lichtbogen gezündet wird.',
    'Newsletter addresses are kept until you unsubscribe or ask us to remove them. Business correspondence is kept as long as needed for the enquiry or project and any statutory retention period that applies to it. Hosting logs are retained according to GitHub&rsquo;s own schedule.':
        'Newsletter-Adressen speichern wir, bis Sie sich abmelden oder die Löschung verlangen. Geschäftskorrespondenz bewahren wir so lange auf, wie es für die Anfrage oder das Projekt erforderlich ist, zuzüglich geltender gesetzlicher Aufbewahrungsfristen. Für Hosting-Protokolle gelten die Fristen von GitHub.',
    'Most delays in piping start with a bad fit-up. We supply fitters for process, utility and engine room systems, instrument fitters for small bore work, and workshop crews who build spools straight from the isometrics. The dimensions are checked before the welder arrives, not after.':
        'Die meisten Verzögerungen im Rohrleitungsbau beginnen mit einer schlechten Passung. Wir stellen Monteure für Prozess-, Versorgungs- und Maschinenraumsysteme, Monteure für Mess- und Instrumentierungsleitungen für kleine Nennweiten und Werkstattteams, die Spools direkt nach Isometrien fertigen. Die Maße werden geprüft, bevor der Schweißer kommt, nicht danach.',
    'Under the GDPR you may request access to your data, correction, erasure, restriction of processing, portability, and you may object to processing based on legitimate interest. Write to <a href="mailto:info@alprojects.eu">info@alprojects.eu</a> and we will respond within one month.':
        'Nach der DSGVO können Sie Auskunft über Ihre Daten, Berichtigung, Löschung, Einschränkung der Verarbeitung und Datenübertragbarkeit verlangen sowie einer auf berechtigtem Interesse beruhenden Verarbeitung widersprechen. Schreiben Sie an <a href="mailto:info@alprojects.eu">info@alprojects.eu</a>; wir antworten innerhalb eines Monats.',
    'Headquartered in Klaipėda, Lithuania, with active project bases supporting clients in six countries. Offices in <strong>Lithuania</strong>, <strong>Poland</strong>, <strong>Germany</strong> and <strong>Norway</strong> sit close to our clients&rsquo; yards, ports and offshore terminals.':
        'Hauptsitz in Klaipėda, Litauen, mit aktiven Projektstandorten für Kunden in sechs Ländern. Unsere Büros in <strong>Litauen</strong>, <strong>Polen</strong>, <strong>Deutschland</strong> und <strong>Norwegen</strong> liegen nahe an den Werften, Häfen und Offshore-Terminals unserer Kunden.',
    'Send us the scope or the drawings and we will come back with a price and crew dates. The fastest route to a useful answer is the scope, the location, the standards that apply and the window you are working to. For personnel requests, tell us the disciplines, certifications and headcount.':
        'Senden Sie uns den Leistungsumfang oder die Zeichnungen und wir melden uns mit Preis und Einsatzterminen. Am schnellsten zu einer brauchbaren Antwort führen: Umfang, Ort, geltende Normen und Ihr Zeitfenster. Bei Personalanfragen nennen Sie uns Gewerke, Qualifikationen und Anzahl.',
    'Fuel handling infrastructure and wind energy support. Our <a href="/news/fuel-loading-terminal-completed">fuel loading terminal scope</a> ran from September 2025 to April 2026 with twelve specialists and over 11,000 hours on site — a useful figure for anyone planning work of that size.':
        'Infrastruktur für den Kraftstoffumschlag und Unterstützung der Windenergie. Unser <a href="/news/fuel-loading-terminal-completed">Auftrag am Kraftstoff-Verladeterminal</a> lief von September 2025 bis April 2026 mit zwölf Fachkräften und über 11.000 Stunden vor Ort — ein nützlicher Anhaltspunkt für alle, die Arbeiten dieser Größenordnung planen.',
    'Execution of lifting, rigging and installation works for industrial and offshore projects. Planning, coordination and supervision of lifting operations in accordance with project requirements and site conditions. Work is performed with controlled procedures and safety compliance at all stages.':
        'Ausführung von Hebe-, Anschlag- und Montagearbeiten für Industrie- und Offshore-Projekte. Planung, Koordination und Aufsicht der Hebevorgänge nach Projektanforderungen und Baustellenbedingungen. Die Arbeiten folgen kontrollierten Abläufen und erfüllen in allen Phasen die Sicherheitsvorgaben.',
    'Applications are held for <strong>24 months</strong> from the date you send them, so that we can contact you when a project matches your discipline. You can ask us to delete them at any time by writing to <a href="mailto:info@alprojects.eu">info@alprojects.eu</a>, and we will do so without needing a reason.':
        'Bewerbungen werden <strong>24 Monate</strong> ab Eingang gespeichert, damit wir Sie ansprechen können, sobald ein Projekt zu Ihrem Gewerk passt. Sie können die Löschung jederzeit per E-Mail an <a href="mailto:info@alprojects.eu">info@alprojects.eu</a> verlangen; wir kommen dem ohne Angabe von Gründen nach.',
    'Execution of installation, inspection and maintenance works at height using IRATA and SOFT certified rope access methods. Supports welding, NDT, mechanical works and structural repairs in areas where conventional access is not feasible. Work is performed in compliance with safety standards and site procedures.':
        'Ausführung von Montage-, Prüf- und Instandhaltungsarbeiten in der Höhe mit IRATA- und SOFT-zertifizierter Seilzugangstechnik. Unterstützt Schweißen, ZfP, mechanische Arbeiten und Instandsetzungen an Stellen, die konventionell nicht zugänglich sind. Die Arbeiten erfolgen nach den Sicherheitsnormen und den Vorgaben der Baustelle.',
    'Inspection, access and mechanical works on offshore facilities, where mobilising a team is expensive and a shutdown is more expensive still. Rope access and NDT carry most of this work; visual inspection plays a central role in confirming the safety and operational integrity of oil, gas and wind energy assets.':
        'Prüf-, Zugangs- und Montagearbeiten an Offshore-Anlagen, wo die Mobilisierung eines Teams teuer und ein Stillstand noch teurer ist. Seilzugangstechnik und ZfP tragen den größten Teil dieser Arbeit; die Sichtprüfung ist zentral für den Nachweis von Sicherheit und Betriebsintegrität von Öl-, Gas- und Windenergieanlagen.',
    'ALPROJECTS Group holds <strong>ISO 3834</strong> for welding quality requirements, alongside ISO 9001, ISO 14001 and ISO 45001 covering quality, environmental and occupational health and safety management. Certification is what allows a client to accept our documentation without re-doing the inspection themselves.':
        'ALPROJECTS Group ist nach <strong>ISO 3834</strong> für Qualitätsanforderungen beim Schweißen zertifiziert, ergänzt um ISO 9001, ISO 14001 und ISO 45001 für Qualitäts-, Umwelt- sowie Arbeits- und Gesundheitsschutzmanagement. Erst die Zertifizierung erlaubt es einem Kunden, unsere Dokumentation zu übernehmen, ohne die Prüfung selbst zu wiederholen.',
    'Awarded to UAB &ldquo;ALprojects&rdquo; by Creditinfo Group on 23 June 2026, recognising a high credit score and a proven record of financial stability. In heavy industry, projects run for months and commitments run for years &mdash; independent proof of stability is proof we will be there to see the work through.':
        'Am 23. Juni 2026 von der Creditinfo Group an UAB &ldquo;ALprojects&rdquo; verliehen, in Anerkennung einer hohen Bonität und nachgewiesener finanzieller Stabilität. In der Schwerindustrie laufen Projekte über Monate und Verpflichtungen über Jahre &mdash; ein unabhängiger Stabilitätsnachweis belegt, dass wir bis zum Ende dabei sind.',
    'Piping and mechanical installation on vessels under construction — seawater, bilge and fuel systems routed through compartments that are already full of machinery, structure and other trades. Prefabrication and installation are handled together, because a spool built to drawing but not to the as-built compartment is scrap.':
        'Rohrleitungs- und Maschinenmontage auf Schiffen im Bau — Seewasser-, Bilge- und Kraftstoffsysteme, geführt durch Räume, die bereits voller Maschinen, Struktur und anderer Gewerke sind. Vorfertigung und Montage laufen zusammen, denn ein Spool, der zur Zeichnung, aber nicht zum realen Raum passt, ist Ausschuss.',
    'We specialise in piping prefabrication and installation, steel fabrication and mechanical installation, and we provide certified technical personnel to projects across Europe. In practice that means we are engaged either to deliver a defined mechanical scope, or to supply the qualified people a project is short of &mdash; often both on the same site.':
        'Wir sind auf Rohrvorfertigung und -montage, Stahlbaufertigung und mechanische Montage spezialisiert und stellen zertifiziertes technisches Personal für Projekte in ganz Europa. In der Praxis heißt das: Man beauftragt uns entweder mit einem definierten mechanischen Umfang oder mit den qualifizierten Leuten, die einem Projekt fehlen &mdash; oft mit beidem auf derselben Baustelle.',
    'In heavy industry, projects run for months and commitments run for years. Independent proof of financial stability is proof that we will be there to see the work through &mdash; which is a different question from whether the welding is any good, and worth answering separately. <a href="/news/strongest-in-lithuania-2025-2026">More on the award</a>.':
        'In der Schwerindustrie laufen Projekte über Monate und Verpflichtungen über Jahre. Ein unabhängiger Nachweis finanzieller Stabilität belegt, dass wir bis zum Ende dabei sind &mdash; eine andere Frage als die, ob die Schweißarbeit gut ist, und eine, die man getrennt beantworten sollte. <a href="/news/strongest-in-lithuania-2025-2026">Mehr zur Auszeichnung</a>.',
    'Plant installation, process piping and mechanical packages. A recent example is a transformer mechanical package — stainless steel piping and cooling systems &mdash; <a href="/news/transformer-mechanical-package">delivered across five European countries</a>, where consistency across borders was as much a documentation problem as a fabrication one.':
        'Anlagenmontage, Prozessrohrleitungen und mechanische Pakete. Ein aktuelles Beispiel ist ein mechanisches Transformatorenpaket — Edelstahlrohrleitungen und Kühlsysteme &mdash; <a href="/news/transformer-mechanical-package">in fünf europäischen Ländern ausgeführt</a>, wo gleichbleibende Qualität über Ländergrenzen hinweg ebenso eine Frage der Dokumentation wie der Fertigung war.',
    'The one exception is the scheduling calendar on the contacts page. It is supplied by Calendly LLC and is <strong>not loaded until you press &ldquo;Open the calendar&rdquo;</strong>. Until you do, no request is made to Calendly and they receive nothing about you. Once you open it, Calendly receives your IP address and sets its own cookies in order to run the calendar, and the details you submit if you book a slot. Calendly is a US company and transfers are covered by the EU Standard Contractual Clauses; see <a href="https://calendly.com/privacy" target="_blank" rel="noopener">calendly.com/privacy</a>. You can book a call by email instead if you prefer not to use it.':
        'Die einzige Ausnahme ist der Terminkalender auf der Kontaktseite. Er stammt von Calendly LLC und wird <strong>erst geladen, wenn Sie &ldquo;Kalender öffnen&rdquo; drücken</strong>. Bis dahin geht keine Anfrage an Calendly und das Unternehmen erhält nichts über Sie. Sobald Sie ihn öffnen, erhält Calendly Ihre IP-Adresse und setzt eigene Cookies, um den Kalender zu betreiben, sowie die Angaben, die Sie bei einer Buchung machen. Calendly ist ein US-Unternehmen; Übermittlungen sind durch die EU-Standardvertragsklauseln abgedeckt, siehe <a href="https://calendly.com/privacy" target="_blank" rel="noopener">calendly.com/privacy</a>. Sie können einen Termin auch per E-Mail vereinbaren, wenn Sie den Kalender nicht nutzen möchten.',

    # --- contact form (contacts.html) ---
    'Enquiries':
        'Anfragen',
    'Send us a message':
        'Schreiben Sie uns',
    'Send us the scope or the drawings and we will come back with a price and crew dates. The fastest route to a useful answer is the scope, the location, the standards that apply and the window you are working to.':
        'Senden Sie uns den Leistungsumfang oder die Zeichnungen, und wir melden uns mit Preis und Personalterminen. Der schnellste Weg zu einer brauchbaren Antwort: Umfang, Ort, geltende Normen und Ihr Zeitfenster.',
    'For personnel requests, tell us the disciplines, the certifications and the headcount.':
        'Bei Personalanfragen nennen Sie uns die Gewerke, die Zertifizierungen und die Personenzahl.',
    'Applying for a job? The application form on the <a href="/careers">careers page</a> takes your CV and certificates with it.':
        'Sie bewerben sich? Das Formular auf der <a href="/careers">Karriereseite</a> nimmt Lebenslauf und Zeugnisse gleich mit auf.',
    'Service group':
        'Leistungsbereich',
    'Select a service group':
        'Leistungsbereich wählen',
    'Not sure yet':
        'Noch unklar',
    'Type of enquiry':
        'Art der Anfrage',
    'Select a type of enquiry':
        'Art der Anfrage wählen',
    'Project enquiry':
        'Projektanfrage',
    'Request for personnel':
        'Personalanfrage',
    'Inspection, NDT or rope access':
        'Prüfung, ZfP oder Seilzugangstechnik',
    'Invoicing or administration':
        'Rechnung oder Verwaltung',
    'Something else':
        'Anderes Anliegen',
    'First name':
        'Vorname',
    'Last name':
        'Nachname',
    'Company <span class="opt">(optional)</span>':
        'Firma <span class="opt">(optional)</span>',
    'How can we help?':
        'Wie können wir helfen?',
    'I agree that ALPROJECTS, UAB may store these details in order to answer my enquiry. See the <a href="/privacy">privacy policy</a>.':
        'Ich bin damit einverstanden, dass ALPROJECTS, UAB diese Angaben zur Beantwortung meiner Anfrage speichert. Siehe die <a href="/privacy">Datenschutzerklärung</a>.',
    'Website':
        'Website',
    'Send the enquiry':
        'Anfrage senden',
    'Company name':
        'Firmenname',
    'Scope, location, standards and dates.':
        'Umfang, Ort, Normen und Termine.',

    # --- homepage service slider ---
    '<span>Shipbuilding</span><span>Offshore</span><span>Industrial Facilities</span><span>Steel Structures</span>':
        '<span>Schiffbau</span><span>Offshore</span><span>Industrieanlagen</span><span>Stahlbau</span>',
    '<span>Shipbuilding</span><span>Process Plant</span><span>Engine Rooms</span><span>Utilities</span>':
        '<span>Schiffbau</span><span>Prozessanlagen</span><span>Maschinenräume</span><span>Versorgungstechnik</span>',
    '<span>Industrial Facilities</span><span>Energy Projects</span><span>Offshore</span><span>Steel Structures</span>':
        '<span>Industrieanlagen</span><span>Energieprojekte</span><span>Offshore</span><span>Stahlbau</span>',

    # --- homepage facts block (evidence set) ---

    # --- This is ALPROJECTS (TZ part 6) ---
    'This is ALPROJECTS':
        'Das ist ALPROJECTS',
    'What we are here to do, and the rules we work by. Written down so a client can hold us to them.':
        'Wofür wir da sind und nach welchen Regeln wir arbeiten. Aufgeschrieben, damit ein Kunde uns daran messen kann.',
    'Our vision':
        'Unsere Vision',
    'Industrial work that comes with its own evidence.':
        'Industriearbeit, die ihren Nachweis gleich mitbringt.',
    'Europe has no shortage of contractors who can weld. It has a shortage of contractors who can hand over the evidence with the work, in a form the client, the surveyor and the auditor all accept.':
        'Europa hat keinen Mangel an Firmen, die schweißen können. Es fehlen Firmen, die den Nachweis zusammen mit der Arbeit übergeben, in einer Form, die Kunde, Sachverständiger und Auditor gleichermaßen akzeptieren.',
    'Our mission':
        'Unsere Mission',
    'Certified people on site, and independent proof of what they did.':
        'Zertifizierte Fachkräfte vor Ort und ein unabhängiger Nachweis ihrer Arbeit.',
    'We take mechanical scopes and deliver them with our own supervision. We supply the qualified people a project is short of. And we inspect the result with people who did not do the work.':
        'Wir übernehmen mechanische Gewerke und führen sie mit eigener Bauleitung aus. Wir stellen die Fachkräfte, die einem Projekt fehlen. Und wir prüfen das Ergebnis mit Leuten, die die Arbeit nicht ausgeführt haben.',
    'Three hundred specialists, and a schedule that does not wait':
        'Dreihundert Fachkräfte und ein Terminplan, der nicht wartet',
    'Welders, pipe fitters, shipbuilders, mechanics, NDT inspectors and rope access technicians. Most carry a second trade, which is why one of our people often covers what usually takes two.':
        'Schweißer, Rohrleitungsmonteure, Schiffbauer, Mechaniker, ZfP-Prüfer und Seilzugangstechniker. Die meisten beherrschen ein zweites Gewerk, weshalb einer von uns oft abdeckt, wofür sonst zwei nötig sind.',
    'They travel. A crew that mobilises to Norway on Monday can be in Rostock the following month. That is the job, and everyone who joins us knows it before the first rotation.':
        'Unsere Mannschaften sind mobil. Eine Mannschaft, die am Montag nach Norwegen aufbricht, kann im Folgemonat in Rostock sein. Das ist der Beruf, und jeder weiß das vor der ersten Rotation.',
    'We keep the roster current. Certificates, medicals and availability are checked before anyone is offered to a project.':
        'Wir halten die Personalliste aktuell. Zertifikate, Tauglichkeiten und Verfügbarkeit werden geprüft, bevor jemand einem Projekt angeboten wird.',
    'Work with us':
        'Arbeiten Sie mit uns',
    'Meet the management':
        'Die Geschäftsleitung',
    'Our values':
        'Unsere Werte',
    'Values are worth writing down only if someone can hold you to them. Ours are written so a client can.':
        'Werte lohnt es aufzuschreiben nur, wenn jemand einen daran messen kann. Unsere sind so geschrieben, dass ein Kunde es kann.',
    'We keep learning on every job':
        'Wir lernen bei jedem Auftrag dazu',
    'We debrief after each mobilisation and write down what we would do differently.':
        'Nach jeder Mobilisierung machen wir eine Nachbesprechung und halten fest, was wir anders machen würden.',
    'We share procedures between crews, so the second job runs faster than the first.':
        'Wir teilen Verfahren zwischen den Mannschaften, damit der zweite Auftrag schneller läuft als der erste.',
    'We ask the client&rsquo;s supervisor what went wrong before he has to tell us.':
        'Wir fragen den Bauleiter des Kunden, was schieflief, bevor er es uns sagen muss.',
    'We bring people up to a second trade, because two skills in one man are worth more offshore.':
        'Wir bilden unsere Leute in einem zweiten Gewerk aus, denn zwei Fertigkeiten in einer Person sind offshore mehr wert.',
    'We are responsible for the scope':
        'Wir stehen für den Auftragsumfang ein',
    'We take the work with our own supervision and our own quality control.':
        'Wir übernehmen die Arbeit mit eigener Bauleitung und eigener Qualitätskontrolle.',
    'When the mistake is ours, we say so and we correct it at our cost.':
        'Wenn der Fehler bei uns liegt, sagen wir es und beheben ihn auf unsere Kosten.',
    'We never hand a problem down to the next contractor in the chain.':
        'Wir reichen ein Problem nie an den nächsten Auftragnehmer in der Kette weiter.',
    'We get everyone home at the end of the rotation.':
        'Am Ende der Rotation bringen wir alle nach Hause.',
    'We look for the work others avoid':
        'Wir suchen die Arbeit, die andere meiden',
    'We take scopes with difficult access, tight windows and unclear starting conditions.':
        'Wir übernehmen Gewerke mit schwierigem Zugang, engen Zeitfenstern und unklaren Ausgangsbedingungen.',
    'We answer enquiries that arrive at short notice, because that is when a client needs a contractor most.':
        'Wir beantworten Anfragen, die kurzfristig kommen, denn genau dann braucht ein Kunde einen Auftragnehmer am dringendsten.',
    'We invest in certification before the market starts asking for it.':
        'Wir investieren in Zertifizierung, bevor der Markt danach fragt.',
    'We build the business together, across offices and across crews.':
        'Wir bauen das Unternehmen gemeinsam auf, über Standorte und Mannschaften hinweg.',
    'We look after people and the site':
        'Wir achten auf die Menschen und den Standort',
    'We work to the client&rsquo;s permit system and add our own where theirs is thinner.':
        'Wir arbeiten nach dem Erlaubnisscheinsystem des Kunden und ergänzen unser eigenes, wo seines dünner ist.',
    'We leave the area cleaner than we found it.':
        'Wir hinterlassen den Bereich sauberer, als wir ihn vorgefunden haben.',
    'We ask for help early. Nobody on a rope is expected to manage alone.':
        'Wir bitten früh um Hilfe. Niemand am Seil soll allein zurechtkommen.',
    'We follow the law and our own procedures when nobody is watching.':
        'Wir halten Gesetz und eigene Verfahren ein, auch wenn niemand zusieht.',
    'We keep the date we gave':
        'Wir halten den zugesagten Termin',
    'A mobilisation date is given only when the people are actually free.':
        'Ein Mobilisierungstermin wird nur genannt, wenn die Leute tatsächlich frei sind.',
    'We plan so that the safe method is also the fast one.':
        'Wir planen so, dass die sichere Methode auch die schnelle ist.',
    'We remind the client of his deadlines as well as ours.':
        'Wir erinnern den Kunden an seine Termine ebenso wie an unsere.',
    'A yard schedule does not move, so ours has to hold.':
        'Ein Werftterminplan verschiebt sich nicht, also muss unserer halten.',
    'We say it early and we say it plainly':
        'Wir sagen es früh und wir sagen es klar',
    'We explain the scope and the risks before the work starts.':
        'Wir erklären Umfang und Risiken, bevor die Arbeit beginnt.',
    'A problem is reported the day it appears. Friday is too late.':
        'Ein Problem wird an dem Tag gemeldet, an dem es auftritt. Freitag ist zu spät.',
    'We confirm that we understood the client, and that he understood us.':
        'Wir bestätigen, dass wir den Kunden verstanden haben und er uns.',
    'We write documentation a person can actually read.':
        'Wir schreiben Dokumentation, die ein Mensch tatsächlich lesen kann.',
    'Anyone on our crew can stop a job.':
        'Jeder in unserer Mannschaft kann eine Arbeit stoppen.',
    'ALPROJECTS Group &middot; Value 02':
        'ALPROJECTS Group &middot; Wert 02',
    'HSEQ':
        'HSEQ',
    'Zero harm is a target, and we report against it':
        'Null Schaden ist ein Ziel, und wir berichten dagegen',
    'We work inside the client&rsquo;s permit system and add our own where theirs is thinner. Every scope gets a risk assessment and a method statement before mobilisation, and both are written for the actual site. Copying the paperwork from the last job is how people get hurt.':
        'Wir arbeiten im Erlaubnisscheinsystem des Kunden und ergänzen unser eigenes, wo seines dünner ist. Jedes Gewerk erhält vor der Mobilisierung eine Gefährdungsbeurteilung und eine Arbeitsanweisung, beide für die tatsächliche Baustelle geschrieben. Die Papiere vom letzten Auftrag zu kopieren, so kommen Menschen zu Schaden.',
    'Our management systems are certified to four standards. Certification is what lets a client accept our documentation without repeating the inspection themselves.':
        'Unsere Managementsysteme sind nach vier Normen zertifiziert. Die Zertifizierung ist es, die einem Kunden erlaubt, unsere Dokumentation anzunehmen, ohne die Prüfung selbst zu wiederholen.',
    '<b>No injuries</b><span>to our people, to the client&rsquo;s people, to anyone else on site.</span>':
        '<b>Keine Verletzungen</b><span>weder bei unseren Leuten noch bei denen des Kunden noch bei sonst jemandem auf der Baustelle.</span>',
    '<b>No occupational illness</b><span>from the way we organise the work.</span>':
        '<b>Keine Berufskrankheiten</b><span>durch die Art, wie wir die Arbeit organisieren.</span>',
    '<b>No spills</b><span>to the sea, to the ground or to the drain.</span>':
        '<b>Keine Austritte</b><span>ins Meer, in den Boden oder in die Kanalisation.</span>',
    '<b>No damage</b><span>to the structure we were sent to work on.</span>':
        '<b>Keine Schäden</b><span>an der Struktur, für die wir geschickt wurden.</span>',
    'We publish our safety figures once a year: hours worked, incidents, and what we changed as a result. A target nobody measures is a slogan.':
        'Wir veröffentlichen unsere Sicherheitszahlen einmal im Jahr: geleistete Stunden, Vorfälle und was wir daraufhin geändert haben. Ein Ziel, das niemand misst, ist ein Slogan.',
    '<b>ISO 3834</b><span>Welding quality</span>':
        '<b>ISO 3834</b><span>Schweißtechnische Qualität</span>',
    '<b>ISO 9001</b><span>Quality</span>':
        '<b>ISO 9001</b><span>Qualität</span>',
    '<b>ISO 14001</b><span>Environment</span>':
        '<b>ISO 14001</b><span>Umwelt</span>',
    '<b>ISO 45001</b><span>Health and safety</span>':
        '<b>ISO 45001</b><span>Arbeitsschutz</span>',
    'If this is how you want your contractor to work, send us the scope':
        'Wenn Ihr Auftragnehmer so arbeiten soll, senden Sie uns den Umfang',
    'We reply to project enquiries within one working day.':
        'Projektanfragen beantworten wir innerhalb eines Werktags.',
    'ALPROJECTS crew on a wind farm site':
        'ALPROJECTS-Mannschaft in einem Windpark',
    'Rope access technician working on a turbine blade':
        'Seilzugangstechniker bei der Arbeit an einem Rotorblatt',
    'Rope access descent onto an offshore topside':
        'Seilabstieg auf ein Offshore-Topside',
    'This is ALPROJECTS &mdash; vision, values and HSEQ':
        'Das ist ALPROJECTS &mdash; Vision, Werte und HSEQ',
    'Vision, values and HSEQ. What ALPROJECTS Group is here to do, and the rules we work by.':
        'Vision, Werte und HSEQ. Wofür ALPROJECTS Group da ist und nach welchen Regeln wir arbeiten.',
    'This is ALPROJECTS — ALPROJECTS Group':
        'Das ist ALPROJECTS — ALPROJECTS Group',
    'Our management systems are certified to ISO 9001, 14001 and 45001, and our welding to ISO 3834. Certification is what lets a client accept our documentation without repeating the inspection themselves.':
        'Unsere Managementsysteme sind nach ISO 9001, 14001 und 45001 zertifiziert, unser Schweißen nach ISO 3834. Die Zertifizierung ist es, die einem Kunden erlaubt, unsere Dokumentation zu akzeptieren, ohne die Prüfung selbst zu wiederholen.',
    '<b>Shipbuilding</b> <span>Piping and mechanical installation on vessels under construction.</span> <em class="ar-e" aria-hidden="true">&#8593;</em>':
        '<b>Schiffbau</b> <span>Rohrleitungs- und Maschinenmontage an Schiffen im Bau.</span> <em class="ar-e" aria-hidden="true">&#8593;</em>',
    '<b>Offshore</b> <span>Inspection, access and mechanical works on offshore facilities.</span> <em class="ar-e" aria-hidden="true">&#8593;</em>':
        '<b>Offshore</b> <span>Inspektion, Zugang und mechanische Arbeiten an Offshore-Anlagen.</span> <em class="ar-e" aria-hidden="true">&#8593;</em>',
    '<b>Industrial</b> <span>Plant installation, transformer packages, process piping.</span> <em class="ar-e" aria-hidden="true">&#8593;</em>':
        '<b>Industrie</b> <span>Anlagenmontage, Transformatorenpakete, Prozessrohrleitungen.</span> <em class="ar-e" aria-hidden="true">&#8593;</em>',
    '<b>Energy and renewables</b> <span>Fuel handling infrastructure and wind energy support.</span> <em class="ar-e" aria-hidden="true">&#8593;</em>':
        '<b>Energie und erneuerbare Energien</b> <span>Kraftstoffinfrastruktur und Unterstützung im Windbereich.</span> <em class="ar-e" aria-hidden="true">&#8593;</em>',
    '<span class="value" data-count="300" data-suffix="+">0+</span><span class="label">Certified specialists on the roster</span>':
        '<span class="value" data-count="300" data-suffix="+">0+</span><span class="label">Zertifizierte Fachkräfte in der Stammbelegschaft</span>',
    '<span class="value" data-count="6">0</span><span class="label">Countries we work in</span>':
        '<span class="value" data-count="6">0</span><span class="label">Länder, in denen wir arbeiten</span>',
    '<span class="value" data-count="4">0</span><span class="label">Sectors, one set of disciplines</span>':
        '<span class="value" data-count="4">0</span><span class="label">Sektoren, dieselben Gewerke</span>',
    'ALPROJECTS, UAB &middot; Šilutės pl. 2, LT-92298 Klaipėda, Lithuania<br> <a href="mailto:info@alprojects.eu">info@alprojects.eu</a> &middot; <a href="tel:+37063663744">+370 636 63 744</a>':
        'ALPROJECTS, UAB &middot; Šilutės pl. 2, LT-92298 Klaipėda, Litauen<br> <a href="mailto:info@alprojects.eu">info@alprojects.eu</a> &middot; <a href="tel:+37063663744">+370 636 63 744</a>',
    'Standing':
        'Unsere Bonität',
    'We deliver the scope, or we supply the people a scope is short of':
        'Wir liefern den Umfang, oder wir stellen die Leute, die dafür fehlen',
    'Often both, on the same site. We specialise in piping prefabrication and installation, steel fabrication and mechanical installation, and we provide certified technical personnel to projects across Europe.':
        'Oft beides, auf derselben Baustelle. Wir sind spezialisiert auf Rohrvorfertigung und -montage, Stahlbau und Maschinenmontage, und wir stellen Projekten in ganz Europa zertifiziertes technisches Personal.',
    'The company employs between 51 and 200 people directly and draws on a roster of more than 300 certified specialists. Projects are resourced from that roster rather than subcontracted on, which is what keeps the quality system meaningful.':
        'Das Unternehmen beschäftigt direkt zwischen 51 und 200 Menschen und greift auf einen Pool von mehr als 300 zertifizierten Fachkräften zurück. Projekte werden aus diesem Pool besetzt statt weitervergeben, und genau das hält das Qualitätssystem sinnvoll.',
    'In heavy industry, projects run for months and commitments run for years. Independent proof of financial stability is proof that we will be there to see the work through &mdash; a different question from whether the welding is any good, and worth answering separately.':
        'In der Schwerindustrie laufen Projekte über Monate und Verpflichtungen über Jahre. Ein unabhängiger Nachweis finanzieller Stabilität ist der Nachweis, dass wir da sein werden, um die Arbeit zu Ende zu bringen &mdash; eine andere Frage als die, ob die Schweißnähte gut sind, und es wert, getrennt beantwortet zu werden.',
    'More on the award':
        'Mehr zur Auszeichnung',
    'What it is':
        'Worum es geht',
    'The scaffold costs more than the repair':
        'Das Gerüst kostet mehr als die Reparatur',
    'Nobody buys rope access because they want ropes. They buy it because the alternative is a scaffold, a crane, a vessel day or a shutdown. Each of those costs more than the work itself.':
        'Niemand kauft Seilzugangstechnik, weil er Seile will. Man kauft sie, weil die Alternative ein Gerüst, ein Kran, ein Schiffstag oder ein Stillstand ist. Jedes davon kostet mehr als die Arbeit selbst.',
    'Our technicians hold IRATA and SOFT certification and most of them carry a second trade: inspection, welding or mechanical. One person on the rope replaces a scaffold crew and an inspector standing behind them.':
        'Unsere Techniker sind nach IRATA und SOFT zertifiziert, und die meisten bringen ein zweites Gewerk mit: Prüfung, Schweißen oder Mechanik. Eine Person am Seil ersetzt eine Gerüstkolonne und den Prüfer, der dahinter steht.',
    'Every crew works with a written rescue plan and a supervisor on site. Without both, the job does not start.':
        'Jede Mannschaft arbeitet mit einem schriftlichen Rettungsplan und einem Aufsichtführenden vor Ort. Ohne beides beginnt die Arbeit nicht.',
    'IRATA and SOFT':
        'IRATA und SOFT',
    'Typical mobilisation':
        'Typische Mobilisierung',
    'short notice, crews of 2&ndash;6':
        'kurzfristig, Teams von 2&ndash;6',
    'offshore wind, oil and gas, industry, marine':
        'Offshore-Wind, Öl und Gas, Industrie, Marine',
    'Deliverable':
        'Ergebnis',
    'report in the client&rsquo;s format':
        'Bericht im Format des Kunden',
    'The same crew works offshore topsides, turbine blades and onshore wind. Rope access is how they get there; the trade they carry is what they do once they arrive.':
        'Dieselbe Mannschaft arbeitet auf Offshore-Topsides, an Rotorblättern und im Onshore-Wind. Die Seilzugangstechnik ist der Weg dorthin; das Gewerk, das sie mitbringen, ist die Arbeit, die dort gemacht wird.',
    'Rope access technician descending onto an offshore topside above open water':
        'Seilzugangstechniker beim Abseilen auf ein Offshore-Topside über offener See',
    'Rope access technician working on a wind turbine blade':
        'Seilzugangstechniker bei der Arbeit an einem Rotorblatt',
    'Three technicians on a wind farm site at first light':
        'Drei Techniker auf einem Windpark im ersten Tageslicht',
    'VCA':
        'VCA',
    'EBN Certification':
        'EBN Certification',
    'VCA certification mark issued by EBN Certification':
        'VCA-Zertifizierungszeichen, ausgestellt von EBN Certification',
    'Scope on the three ISO certificates: inspection and industrial maintenance services for onshore and offshore installations, issued by DNV Business Assurance Finland. VCA is certified by EBN Certification. Select a certificate to open the PDF.':
        'Geltungsbereich der drei ISO-Zertifikate: Prüf- und Instandhaltungsleistungen für Anlagen an Land und offshore, ausgestellt von DNV Business Assurance Finland. VCA ist von EBN Certification zertifiziert. Wählen Sie ein Zertifikat, um das PDF zu öffnen.',
    '<span>EBN Certification</span>':
        '<span>EBN Certification</span>',
    'ALPROJECTS, UAB<br>Šilutės pl. 2, LT-92298 Klaipėda, Lithuania<br> <a href="mailto:info@alprojects.eu">info@alprojects.eu</a><br> <a href="tel:+37063663744">+370 636 63 744</a>':
        'ALPROJECTS, UAB<br>Šilutės pl. 2, LT-92298 Klaipėda, Litauen<br> <a href="mailto:info@alprojects.eu">info@alprojects.eu</a><br> <a href="tel:+37063663744">+370 636 63 744</a>',
    'Scaffolding costs more in downtime than in steel. IRATA and SOFT certified technicians reach the same place on rope, inspect it and repair it while the plant keeps running.':
        'Ein Gerüst kostet mehr an Stillstand als an Stahl. Nach IRATA und SOFT zertifizierte Techniker erreichen dieselbe Stelle am Seil, prüfen und reparieren sie, während die Anlage weiterläuft.',
    'Inspection &amp; Access':
        'Prüfung &amp; Zugang',
    '<span>Offshore Oil &amp; Gas</span><span>Wind Energy</span><span>Industrial Facilities</span><span>Marine</span>':
        '<span>Offshore-Öl &amp; -Gas</span><span>Windenergie</span><span>Industrieanlagen</span><span>Marine</span>',
    '<span class="value" data-count="300" data-suffix="+">300+</span> <span class="label">Certified specialists on the roster</span>':
        '<span class="value" data-count="300" data-suffix="+">300+</span> <span class="label">Zertifizierte Fachkräfte in der Stammbelegschaft</span>',
    '<span class="value" data-count="6">6</span> <span class="label">Countries we work in</span>':
        '<span class="value" data-count="6">6</span> <span class="label">Länder, in denen wir arbeiten</span>',
    '<span class="value" data-count="4">4</span> <span class="label">Sectors, one set of disciplines</span>':
        '<span class="value" data-count="4">4</span> <span class="label">Sektoren, dieselben Gewerke</span>',
    '<span class="value" data-count="3">3</span> <span class="label">ISO management systems, certified by DNV</span>':
        '<span class="value" data-count="3">3</span> <span class="label">ISO-Managementsysteme, von DNV zertifiziert</span>',
    '<span class="value" data-count="90" data-suffix="+">90+</span> <span class="label">Projects delivered across multiple countries</span>':
        '<span class="value" data-count="90" data-suffix="+">90+</span> <span class="label">Projekte in mehreren Ländern ausgeführt</span>',
    '<span class="value" data-count="98" data-suffix="%">98%</span> <span class="label">Early risk detection by certified specialists</span>':
        '<span class="value" data-count="98" data-suffix="%">98%</span> <span class="label">Frühe Risikoerkennung durch zertifizierte Fachkräfte</span>',
    '<span class="value" data-count="40" data-suffix="%">40%</span> <span class="label">Reduced inspection time through optimized workflows</span>':
        '<span class="value" data-count="40" data-suffix="%">40%</span> <span class="label">Kürzere Prüfzeiten durch optimierte Abläufe</span>',
    '<span class="value" data-count="1200" data-suffix="+">1,200+</span> <span class="label">Safe execution in complex and confined environments</span>':
        '<span class="value" data-count="1200" data-suffix="+">1.200+</span> <span class="label">Sichere Ausführung in komplexen und beengten Umgebungen</span>',
    '03 &middot; Industrial Projects':
        '03 &middot; Industrieprojekte',
    '<span class="num">03</span><span>01 Aug 2026 &middot; Industrial Projects</span><span class="arr">&#8593;</span>':
        '<span class="num">03</span><span>01. Aug. 2026 &middot; Industrieprojekte</span><span class="arr">&#8593;</span>',
    '04 &middot; Energy Projects':
        '04 &middot; Energieprojekte',
    '<span class="num">04</span><span>25 Jul 2026 &middot; Energy Projects</span><span class="arr">&#8593;</span>':
        '<span class="num">04</span><span>25. Juli 2026 &middot; Energieprojekte</span><span class="arr">&#8593;</span>',
    '05 &middot; Industry':
        '05 &middot; Industrie',
    '<span class="num">05</span><span>25 Jul 2026 &middot; Industry</span><span class="arr">&#8593;</span>':
        '<span class="num">05</span><span>25. Juli 2026 &middot; Industrie</span><span class="arr">&#8593;</span>',
    '06 &middot; Company':
        '06 &middot; Unternehmen',
    '<span class="num">06</span><span>23 Jun 2026 &middot; Company</span><span class="arr">&#8593;</span>':
        '<span class="num">06</span><span>23. Juni 2026 &middot; Unternehmen</span><span class="arr">&#8593;</span>',
    '<span class="num">03</span><span>01 Aug 2026 &middot; Industrial Projects</span><span class="arr">&#8593;</span>':
        '<span class="num">03</span><span>01. Aug. 2026 &middot; Industrieprojekte</span><span class="arr">&#8593;</span>',
    '<span class="num">04</span><span>25 Jul 2026 &middot; Energy Projects</span><span class="arr">&#8593;</span>':
        '<span class="num">04</span><span>25. Juli 2026 &middot; Energieprojekte</span><span class="arr">&#8593;</span>',
    '<span class="num">05</span><span>25 Jul 2026 &middot; Industry</span><span class="arr">&#8593;</span>':
        '<span class="num">05</span><span>25. Juli 2026 &middot; Industrie</span><span class="arr">&#8593;</span>',
    '<span class="num">06</span><span>23 Jun 2026 &middot; Company</span><span class="arr">&#8593;</span>':
        '<span class="num">06</span><span>23. Juni 2026 &middot; Unternehmen</span><span class="arr">&#8593;</span>',
    'Quality control (QA/QC)':
        'Qualitätskontrolle (QA/QC)',
    'Welder qualifications to EN ISO 9606-1, verified before mobilisation':
        'Schweißerprüfungen nach EN ISO 9606-1, vor der Mobilisierung geprüft',
    'Welding coordination and traceability under ISO 3834-2':
        'Schweißaufsicht und Rückverfolgbarkeit nach ISO 3834-2',
    '<b>30</b><span>Positions to fill</span>':
        '<b>30</b><span>Zu besetzende Stellen</span>',
    '<b>No injuries</b><span>to our people, to the client&rsquo;s people, or to anyone else on site.</span>':
        '<b>Keine Verletzungen</b><span>weder bei unseren Leuten noch bei denen des Kunden noch bei sonst jemandem auf der Baustelle.</span>',
    '<span class="kp-num">03</span> <span class="kp-name">Ostwind Offshore Wind Farm</span> <span class="kp-scope">Cable jointers, jointer&rsquo;s mates and rigging support.</span>':
        '<span class="kp-num">03</span> <span class="kp-name">Offshore-Windpark Ostwind</span> <span class="kp-scope">Kabelmonteure, Kabelmonteurhelfer und Unterstützung bei der Hebetechnik.</span>',
    '<span class="srv-n">11</span><span class="srv-name">Quality control (QA/QC)</span>':
        '<span class="srv-n">11</span><span class="srv-name">Qualitätskontrolle (QA/QC)</span>',
    'A weld is only as good as the paperwork behind it. We weld structural steel and piping systems by TIG (141), MAG (135) and flux-cored (136) processes, under an ISO 3834-2 quality system. The welders hold current qualifications and the procedure is approved before the first arc is struck.':
        'Eine Schweißnaht ist nur so gut wie die Dokumentation dahinter. Wir schweißen Stahlbau und Rohrleitungssysteme mit TIG (141), MAG (135) und Fülldraht (136) unter einem Qualitätssystem nach ISO 3834-2. Die Schweißer besitzen gültige Qualifikationen, und das Verfahren ist vor dem ersten Lichtbogen freigegeben.',
    'A weld is only as good as the paperwork behind it. We weld structural steel and piping systems by TIG (141), MAG (135) and flux-cored (136) processes,...':
        'Eine Schweißnaht ist nur so gut wie die Dokumentation dahinter. Wir schweißen Stahlbau und Rohrleitungssysteme mit TIG (141), MAG (135) und...',
    'ALPROJECTS, UAB has been awarded the Strongest in Lithuania 2025–2026 certificate by Creditinfo Group.':
        'ALPROJECTS, UAB wurde das Zertifikat Strongest in Lithuania 2025–2026 von Creditinfo Group verliehen.',
    'ALPROJECTS, UAB holds the <strong>Strongest in Lithuania</strong> certificate, awarded by Creditinfo Group on 23 June 2026 to companies with a high credit score and a proven record of financial stability.':
        'ALPROJECTS, UAB hält das Zertifikat <strong>Strongest in Lithuania</strong>, das Creditinfo Group am 23. Juni 2026 an Unternehmen mit hoher Bonität und nachgewiesener Finanzstabilität vergeben hat.',
    'Abnormal load permits, escort and cargo securing to EN 12195-1, with CMR cover':
        'Genehmigungen für Großraum- und Schwertransporte, Begleitung und Ladungssicherung nach EN 12195-1, mit CMR-Deckung',
    'Acceptance to EN ISO 5817 and ISO 10675, or to the project specification':
        'Bewertungsgruppen nach EN ISO 5817 und ISO 10675 oder nach Projektspezifikation',
    'Certificates you hold <span class="opt">(optional, select all that apply)</span>':
        'Ihre Zertifikate <span class="opt">(optional, alles Zutreffende auswählen)</span>',
    'Dismantling, skidding, jacking and positioning on SPMT or hydraulic gantry':
        'Demontage, Verschieben, Anheben und Positionieren auf SPMT oder hydraulischem Portal',
    'Engine room piping: fuel, lube oil, cooling water, ballast and bilge systems, including spool prefabrication':
        'Maschinenraum-Rohrleitungen: Brennstoff, Schmieröl, Kühlwasser, Ballast und Bilge, einschließlich Spool-Vorfertigung',
    'Foundation preparation, chocking, grouting and laser shaft alignment':
        'Fundamentvorbereitung, Unterfütterung, Vergussmörtel und Laser-Wellenausrichtung',
    'Hull structural fitting and welding to class-approved procedures':
        'Montage und Schweißen der Rumpfstruktur nach klassezugelassenen Verfahren',
    'IRATA-certified technicians, Levels 1 to 3, with an IRATA Level 3 supervisor on every site':
        'IRATA-zertifizierte Techniker der Stufen 1 bis 3, mit einem IRATA-Level-3-Aufsichtführenden auf jeder Baustelle',
    'If you believe we have handled your data improperly, you may lodge a complaint with the Lithuanian State Data Protection Inspectorate (Valstybinė duomenų apsaugos inspekcija), L. Sapiegos g. 17, LT-10312 Vilnius, <a href="mailto:ada@ada.lt">ada@ada.lt</a>, <a href="https://vdai.lrv.lt" target="_blank" rel="noopener">vdai.lrv.lt</a>.':
        'Wenn Sie der Ansicht sind, dass wir Ihre Daten unsachgemäß verarbeitet haben, können Sie Beschwerde bei der litauischen Datenschutzaufsicht (Valstybinė duomenų apsaugos inspekcija) einlegen, L. Sapiegos g. 17, LT-10312 Vilnius, <a href="mailto:ada@ada.lt">ada@ada.lt</a>, <a href="https://vdai.lrv.lt" target="_blank" rel="noopener">vdai.lrv.lt</a>.',
    'Independent third-party verification, reported to the client in their format':
        'Unabhängige Verifizierung durch Dritte, im Format des Kunden berichtet',
    'Inspection and Test Plans (ITP) with hold, witness and review points agreed before work starts':
        'Prüf- und Testpläne (ITP) mit Haltepunkten, Zeugenpunkten und Prüfpunkten, vor Arbeitsbeginn vereinbart',
    'Inspection with the plant running, where the method allows it':
        'Prüfung bei laufender Anlage, soweit das Verfahren es zulässt',
    'Instrument pipe fitters: small-bore, tubing, impulse lines and instrument hook-ups':
        'Monteure für Mess- und Instrumentierungsleitungen: kleine Nennweiten, Tubing, Impulsleitungen und Instrumentenanschlüsse',
    'MAG (135) for structural steel fill and capping passes; MIG (131) for aluminium and non-ferrous work':
        'MAG (135) für Füll- und Decklagen im Stahlbau; MIG (131) für Aluminium und Nichteisenmetalle',
    'Magnetic particle testing (MT) to EN ISO 17638 and ultrasonic testing (UT) to EN ISO 17640':
        'Magnetpulverprüfung (MT) nach EN ISO 17638 und Ultraschallprüfung (UT) nach EN ISO 17640',
    'Manufacturing Record Book (MRB) assembled as the work goes, not at the end':
        'Manufacturing Record Book (MRB), fortlaufend während der Arbeiten erstellt, nicht am Ende',
    'Mobile repair teams':
        'Mobile Reparaturteams',
    'Mobile repair teams — ALPROJECTS Group':
        'Mobile Reparaturteams — ALPROJECTS Group',
    'Most delays in piping start with a bad fit-up. We supply fitters for process, utility and engine room systems, instrument fitters for small-bore work, and workshop crews who build spools straight from the isometrics. The dimensions are checked before the welder arrives, not after.':
        'Die meisten Verzögerungen im Rohrleitungsbau beginnen mit einer schlechten Passung. Wir stellen Monteure für Prozess-, Versorgungs- und Maschinenraumsysteme, Monteure für Mess- und Instrumentierungsleitungen kleiner Nennweiten sowie Werkstattteams, die Spools direkt nach Isometrie fertigen. Die Maße werden geprüft, bevor der Schweißer kommt, nicht danach.',
    'Most delays in piping start with a bad fit-up. We supply fitters for process, utility and engine room systems, instrument fitters for small-bore work,...':
        'Die meisten Verzögerungen im Rohrleitungsbau beginnen mit einer schlechten Passung. Wir stellen Monteure für Prozess-, Versorgungs- und...',
    'Moving a production line is a scheduling problem before it is a lifting problem. We dismantle, move, reinstall and align it, inside a running plant or between two countries.':
        'Eine Produktionslinie zu verlagern ist zuerst ein Terminproblem und erst dann ein Hebeproblem. Wir demontieren, transportieren, montieren wieder und richten aus — innerhalb einer laufenden Anlage oder zwischen zwei Ländern.',
    'Moving a production line is a scheduling problem before it is a lifting problem. We dismantle, move, reinstall and align it, inside a running plant or...':
        'Eine Produktionslinie zu verlagern ist zuerst ein Terminproblem und erst dann ein Hebeproblem. Wir demontieren, transportieren, montieren wieder...',
    'Nobody should be signing off their own work. UT, PT and MT let us inspect while the plant keeps running; radiography is planned around production windows. We report to the client, not to the contractor who did the welding.':
        'Niemand sollte die eigene Arbeit abnehmen. UT, PT und MT erlauben die Prüfung bei laufender Anlage; die Durchstrahlungsprüfung wird um die Produktionsfenster herum geplant. Wir berichten dem Kunden, nicht dem Unternehmen, das geschweißt hat.',
    'Nobody should be signing off their own work. UT, PT and MT let us inspect while the plant keeps running; radiography is planned around production...':
        'Niemand sollte die eigene Arbeit abnehmen. UT, PT und MT erlauben die Prüfung bei laufender Anlage; die Durchstrahlungsprüfung wird um die...',
    'Often without scaffolding, and usually without a shutdown':
        'Oft ohne Gerüst und in der Regel ohne Anlagenstillstand',
    'On-board mechanical repairs':
        'Mechanische Reparaturen an Bord',
    'Our management systems are certified to ISO 9001, 14001 and 45001, and our welding to ISO 3834. Certification is what lets a client accept our documentation without repeating the inspection.':
        'Unsere Managementsysteme sind nach ISO 9001, 14001 und 45001 zertifiziert, unser Schweißen nach ISO 3834. Die Zertifizierung ist es, die einem Kunden erlaubt, unsere Dokumentation zu akzeptieren, ohne die Prüfung zu wiederholen.',
    'Our supervisors and our QA/QC engineers on site':
        'Unsere Bauleiter und unsere QA/QC-Ingenieure vor Ort',
    'Our technicians hold IRATA and SOFT certification and most of them carry a second trade: inspection, welding or mechanical fitting. One person on the rope replaces a scaffold crew and an inspector standing behind them.':
        'Unsere Techniker sind nach IRATA und SOFT zertifiziert, und die meisten bringen ein zweites Gewerk mit: Prüfung, Schweißen oder Maschinenmontage. Eine Person am Seil ersetzt eine Gerüstkolonne und den Prüfer, der dahinter steht.',
    'Phased array (PAUT) and TOFD where radiography is not practical':
        'Phased Array (PAUT) und TOFD, wo Durchstrahlungsprüfung nicht praktikabel ist',
    'Prefer not to fill in a form?':
        'Lieber kein Formular ausfüllen?',
    'Pressure piping to EN 13480 and PED 2014/68/EU, with pressure testing before insulation':
        'Druckrohrleitungen nach EN 13480 und DGRL 2014/68/EU, mit Druckprüfung vor der Isolierung',
    'Process and utility piping in carbon steel and stainless steel, small bore to large bore':
        'Prozess- und Versorgungsrohrleitungen in Kohlenstoffstahl und Edelstahl, von kleinen bis großen Nennweiten',
    'Quality assurance and quality control (QA/QC)':
        'Qualitätssicherung und Qualitätskontrolle (QA/QC)',
    'Quality assurance and quality control (QA/QC) — ALPROJECTS Group':
        'Qualitätssicherung und Qualitätskontrolle (QA/QC) — ALPROJECTS Group',
    'Quality system certified to ISO 9001; welding under ISO 3834-2':
        'Qualitätssystem nach ISO 9001 zertifiziert; Schweißen nach ISO 3834-2',
    'Railway bridges · steel fitting · structural repairs · pipe welding, 5G position':
        'Eisenbahnbrücken · Stahlmontage · Instandsetzung der Struktur · Rohrschweißen, Position 5G',
    'Repair work is decided in days, not months. We take steel renewal, piping replacement and mechanical repairs to class and to the owner&rsquo;s requirements.':
        'Über eine Reparatur wird in Tagen entschieden, nicht in Monaten. Wir übernehmen Stahlerneuerung, Rohrleitungstausch und mechanische Reparaturen nach den Anforderungen der Klassifikationsgesellschaft und des Reeders.',
    'Repair work is decided in days, not months. We take steel renewal, piping replacement and mechanical repairs to class and to the owner\'s requirements.':
        'Über eine Reparatur wird in Tagen entschieden, nicht in Monaten. Wir übernehmen Stahlerneuerung, Rohrleitungstausch und mechanische Reparaturen nach den Anforderungen der Klassifikationsgesellschaft und des Reeders.',
    'Scopes delivered to the yard&rsquo;s schedule and class-approved drawings':
        'Umfänge geliefert nach dem Terminplan der Werft und nach klassezugelassenen Zeichnungen',
    'Short-notice mobilisation':
        'Kurzfristige Mobilisierung',
    'Site-to-site moves across Europe':
        'Standortverlagerungen in ganz Europa',
    'Six fields are required. Everything else helps us match you faster, but the form will send without them.':
        'Sechs Felder sind Pflicht. Alles andere hilft uns, Sie schneller einzuordnen, aber das Formular lässt sich auch ohne absenden.',
    'Steel fabrication to EN 1090, mechanical completion documented and handed over as a package':
        'Stahlbau nach EN 1090, Mechanical Completion dokumentiert und als Paket übergeben',
    'Structural steel welding to EN 1090-1 and EN 1090-2, execution classes EXC2 and EXC3':
        'Stahlbauschweißen nach EN 1090-1 und EN 1090-2, Ausführungsklassen EXC2 und EXC3',
    'Structural steel, pressure-retaining piping and pipe supports':
        'Stahlbau, drucktragende Rohrleitungen und Rohrhalterungen',
    'Support at client and third-party hold and witness points':
        'Begleitung an Halte- und Zeugenpunkten des Kunden und Dritter',
    'Technicians certified to ISO 9712 Level II and Level III':
        'Techniker zertifiziert nach ISO 9712 Stufe II und Stufe III',
    'This website has no user accounts, no analytics and sets no cookies of its own. Data reaches us in the following ways:':
        'Diese Website hat keine Benutzerkonten, keine Analyse und setzt keine eigenen Cookies. Daten erreichen uns auf folgenden Wegen:',
    'Transformer packages: bushings, coolers, conservators and connecting pipework':
        'Transformatorenpakete: Durchführungen, Kühler, Ausdehnungsgefäße und Verbindungsrohrleitungen',
    'Turnarounds, shutdowns and breakdown repairs':
        'Turnarounds, Stillstände und Störungsreparaturen',
    'Visual testing (VT) to EN ISO 17637 and penetrant testing (PT) to EN ISO 3452':
        'Sichtprüfung (VT) nach EN ISO 17637 und Eindringprüfung (PT) nach EN ISO 3452',
    'WPS to EN ISO 15609-1, qualified by WPQR to EN ISO 15614-1, written for the project standard':
        'WPS nach EN ISO 15609-1, qualifiziert durch WPQR nach EN ISO 15614-1, erstellt für die Projektnorm',
    'We are recruiting 30 certified TIG welders for upcoming project scopes. This is the constraint on our current pipeline, so applications are reviewed quickly.':
        'Wir suchen 30 zertifizierte WIG-Schweißer für anstehende Projektumfänge. Das ist der Engpass unserer aktuellen Auftragslage, daher werden Bewerbungen schnell geprüft.',
    'We ask the client&rsquo;s supervisor what went wrong before they have to tell us.':
        'Wir fragen die Aufsicht des Kunden, was schiefgelaufen ist, bevor sie es uns sagen muss.',
    'We bring people up to a second trade, because two skills in one person are worth more offshore.':
        'Wir bilden unsere Leute in einem zweiten Gewerk aus, weil zwei Fertigkeiten in einer Person offshore mehr wert sind.',
    'We remind the client of their deadlines as well as ours.':
        'Wir erinnern den Kunden an seine Termine ebenso wie an unsere.',
    'Working level of English (B1 or better)':
        'Englischkenntnisse auf Arbeitsniveau (B1 oder besser)',
    'Yard schedules move, and the penalty lands on the subcontractor. We plan for that, and take engine room piping, structural steel and outfitting as complete scopes, on newbuilds and on repair.':
        'Werftterminpläne verschieben sich, und die Vertragsstrafe trifft den Nachunternehmer. Wir planen dafür und übernehmen Maschinenraum-Rohrleitungen, Stahlbau und Ausrüstung als vollständige Umfänge, im Neubau wie in der Reparatur.',
    'Fuel handling infrastructure and wind energy support. Our <a href="/news/fuel-loading-terminal-completed">fuel loading terminal scope</a> ran from September 2025 to April 2026 with 12 specialists and over 11,000 hours on site — a useful figure for anyone planning work of that size.':
        'Kraftstoffinfrastruktur und Unterstützung im Windbereich. Unser <a href="/news/fuel-loading-terminal-completed">Umfang am Verladeterminal</a> lief von September 2025 bis April 2026 mit 12 Fachkräften und über 11.000 Stunden vor Ort — ein nützlicher Anhaltspunkt für alle, die Arbeiten dieser Größe planen.',
    'Yard schedules move, and the penalty lands on the subcontractor. We plan for that, and take engine room piping, structural steel and outfitting as com':
        'Werftterminpläne verschieben sich, und die Vertragsstrafe trifft den Nachunternehmer. Wir planen dafür und übernehmen Maschinenraum-Rohrleitungen,',

    # ---- Baustellen /projects/* (Kundenlieferung, 27. August 2026) ----
    # Tankbau-Vokabular: Schuss (course), Mantel (shell), Stutzen
    # (nozzle), Futterblech (pad plate), Montagelasche (temporary clip),
    # Traverse (spreader beam), Sparren (rafter).
    'Recent work':
        'Aktuelle Projekte',
    'All projects':
        'Alle Projekte',
    'From this job':
        'Von dieser Baustelle',
    'Disciplines on this job':
        'Gewerke auf dieser Baustelle',
    'Four scopes, photographed as they were built.':
        'Vier Projekte, fotografiert während der Ausführung.',
    'Read the job <span class="arr">&#8593;</span>':
        'Zur Baustelle <span class="arr">&#8593;</span>',
    '6 photographs. Press one to open it full size.':
        '6 Aufnahmen. Zum Vergrößern eine davon anklicken.',
    '5 photographs. Press one to open it full size.':
        '5 Aufnahmen. Zum Vergrößern eine davon anklicken.',
    '3 photographs. Press one to open it full size.':
        '3 Aufnahmen. Zum Vergrößern eine davon anklicken.',
    'Shop fabrication and welding':
        'Fertigung und Schweißen in der Werkstatt',
    'Mechanical installation and welding':
        'Mechanische Montage und Schweißen',
    'Mechanical installation and welding &middot; tank farm':
        'Mechanische Montage und Schweißen &middot; Tanklager',
    'Project &middot; Mechanical installation':
        'Projekt &middot; Mechanische Montage',
    'Project &middot; Shop fabrication and welding':
        'Projekt &middot; Fertigung und Schweißen in der Werkstatt',
    'Project &middot; Mechanical installation and welding':
        'Projekt &middot; Mechanische Montage und Schweißen',
    'Project &middot; Mechanical installation and welding &middot; tank farm':
        'Projekt &middot; Mechanische Montage und Schweißen &middot; Tanklager',
    'Tank and vessel fabrication':
        'Tank- und Behälterbau',
    'Valve station and tie-in piping':
        'Armaturenstation und Anbindungsleitungen',
    'Tank internals, nozzles and attachments':
        'Tankeinbauten, Stutzen und Anbauteile',
    'Agitator replacement inside a storage tank':
        'Rührwerkstausch in einem Lagertank',
    'Tank and vessel fabrication — ALPROJECTS Group':
        'Tank- und Behälterbau — ALPROJECTS Group',
    'Valve station and tie-in piping — ALPROJECTS Group':
        'Armaturenstation und Anbindungsleitungen — ALPROJECTS Group',
    'Tank internals, nozzles and attachments — ALPROJECTS Group':
        'Tankeinbauten, Stutzen und Anbauteile — ALPROJECTS Group',
    'Agitator replacement inside a storage tank — ALPROJECTS Group':
        'Rührwerkstausch in einem Lagertank — ALPROJECTS Group',
    'Send us the drawings.':
        'Schicken Sie uns die Zeichnungen.',
    'Send us the scope.':
        'Schicken Sie uns den Leistungsumfang.',
    'Tell us what goes inside and we will price it.':
        'Sagen Sie uns, was hinein soll, und wir kalkulieren es.',
    'Tell us what is going in and we will look at it.':
        'Sagen Sie uns, was eingebaut werden soll, und wir sehen es uns an.',
    'Shell held up on packing, work going on underneath.':
        'Mantel auf Holzunterbau abgestützt, Arbeiten darunter.',
    'The nozzles go in before the course goes on the stack.':
        'Die Stutzen kommen hinein, bevor der Schuss aufgesetzt wird.',
    'Vessel closed up.':
        'Behälter geschlossen.',
    'Inside the shell, with the temporary clips round the courses.':
        'Im Mantel, mit den Montagelaschen rund um die Schüsse.',
    'Lifted on slings from welded lugs.':
        'An Anschlagmitteln von angeschweißten Ösen gehoben.',
    'The shop floor.':
        'Die Fertigungshalle.',
    'Valves levelled before anything was tacked.':
        'Armaturen ausgerichtet, bevor geheftet wurde.',
    'The valve station.':
        'Die Armaturenstation.',
    'Finished root.':
        'Fertige Wurzel.',
    'Tied into the existing rack.':
        'An die bestehende Rohrbrücke eingebunden.',
    'Work front under temporary cover.':
        'Arbeitsfront unter provisorischer Überdachung.',
    'The pad plate goes on before the bracket.':
        'Das Futterblech kommt vor der Konsole.',
    'Internal pipe off the shell nozzle.':
        'Innenleitung am Mantelstutzen.',
    'Roof rafters into the centre ring.':
        'Dachsparren zum Zentralring.',
    'Looking up the shaft to the roof.':
        'Blick an der Welle hinauf zum Dach.',
    'The bearing at the floor.':
        'Das Lager am Boden.',
    'Lower impeller on the shaft.':
        'Unteres Rührorgan auf der Welle.',
    'Welder working under a tank shell held up and secured on timber packing, with bottom plates laid out on the shop floor':
        'Schweißer bei der Arbeit unter einem Tankmantel, der auf Holzunterbau abgestützt und gesichert ist, mit Bodenblechen auf dem Hallenboden',
    'Vessel shell course being lowered onto the course below by overhead crane, with the nozzles already welded in':
        'Mantelschuss eines Behälters, der per Hallenkran auf den darunterliegenden Schuss abgesenkt wird, die Stutzen bereits eingeschweißt',
    'Assembled vessel standing on blocks, with nozzles, a side manway and a drawing taped to the shell':
        'Fertig montierter Behälter auf Böcken, mit Stutzen, seitlichem Mannloch und einer auf den Mantel geklebten Zeichnung',
    'Inside a tank shell, a long pipe on trestles and temporary clips welded round the courses above the bottom plates':
        'Im Tankmantel: ein langes Rohr auf Böcken und Montagelaschen, rund um die Schüsse über den Bodenblechen angeschweißt',
    'Tank shell lifted on slings from lugs welded to the top course':
        'Tankmantel an Anschlagmitteln von Ösen gehoben, die auf den obersten Schuss geschweißt sind',
    'Fabrication hall with tank shells, a vessel on packing, and a spreader beam with slings on the floor':
        'Fertigungshalle mit Tankmänteln, einem Behälter auf Holzunterbau und einer Traverse mit Anschlagmitteln am Boden',
    'Row of valves and piping levelled and aligned before tacking':
        'Reihe von Armaturen und Rohrleitungen, ausgerichtet und fluchtend vor dem Heften',
    'Valves on a tank valve station, with a spirit level laid across a valve during setting out':
        'Armaturen einer Tank-Armaturenstation, mit einer quer aufgelegten Wasserwaage beim Ausrichten',
    'Finished root run on a butt weld, photographed down the pipe bore from the open end of a spool':
        'Fertige Wurzellage an einer Stumpfnaht, durch die Rohrbohrung vom offenen Ende eines Spools aufgenommen',
    'Tie-in piping and flanged joints running from the valve station into the existing rack':
        'Anbindungsleitungen und Flanschverbindungen von der Armaturenstation in die bestehende Rohrbrücke',
    'Valve station under temporary cover at the base of a storage tank':
        'Armaturenstation unter provisorischer Überdachung am Fuß eines Lagertanks',
    'External bracket welded to a pad plate on the tank shell, with the pad welded all round':
        'Außenkonsole auf ein Futterblech am Tankmantel geschweißt, das Futterblech ringsum verschweißt',
    'Internal pipe connected to a shell nozzle inside a tank, with bottom plates below':
        'Innenleitung an einem Mantelstutzen im Tank, darunter die Bodenbleche',
    'Tank roof on radial rafters into the centre ring, with a nozzle opening cut':
        'Tankdach auf radialen Sparren zum Zentralring, mit ausgeschnittener Stutzenöffnung',
    'Agitator shaft running the full height of a storage tank up to the roof, with the upper impeller near the top':
        'Rührwerkswelle über die volle Höhe eines Lagertanks bis zum Dach, mit dem oberen Rührorgan nahe der Spitze',
    'Agitator bearing at the tank floor, with levelling tools in place':
        'Rührwerkslager am Tankboden, mit angesetztem Ausrichtwerkzeug',
    'Lower agitator impeller bolted to the shaft inside a storage tank, with the bearing on the floor below it':
        'Unteres Rührorgan auf die Welle geschraubt, im Lagertank, darunter das Lager am Boden',
    'We weld the nozzles into the courses before they go on the stack, weld out the seams under a crane, and cut and fit the bottoms on the shop floor.':
        'Wir schweißen die Stutzen in die Schüsse, bevor diese aufgesetzt werden, schweißen die Nähte unter dem Kran aus und schneiden und passen die Böden in der Halle ein.',
    'We weld the nozzles into the courses before they go on the stack, weld out the seams under a crane, and cut and fit the bottoms on the shop...':
        'Wir schweißen die Stutzen in die Schüsse, bevor diese aufgesetzt werden, schweißen die Nähte unter dem Kran aus und schneiden und passen die Böden...',
    'Nozzles and manways go into the shell courses before they go on the stack, while a course can still be worked from both sides. The welder works downhand and can get at the back of the joint. By the time a course goes on the stack the nozzles are already in it.':
        'Stutzen und Mannlöcher kommen in die Mantelschüsse, bevor diese aufgesetzt werden, solange ein Schuss noch von beiden Seiten zugänglich ist. Der Schweißer arbeitet in Wannenposition und kommt an die Rückseite der Naht. Wenn ein Schuss aufgesetzt wird, sind die Stutzen bereits drin.',
    'The first course goes on timber packing. The next comes down on it under the crane, landed and held while the seam is tacked, and then welded out.':
        'Der erste Schuss steht auf Holzunterbau. Der nächste wird mit dem Kran darauf abgesenkt, aufgesetzt und gehalten, während die Naht geheftet und anschließend ausgeschweißt wird.',
    'The large tanks go together the other way up. The shell is held up on packing and the next course goes on underneath it, with a row of temporary clips round the inside holding it while the seams are welded out.':
        'Die großen Tanks entstehen andersherum. Der Mantel wird auf Holzunterbau hochgehalten, und der nächste Schuss kommt darunter, gehalten von einer Reihe Montagelaschen innen, während die Nähte ausgeschweißt werden.',
    'Those clips and the lifting lugs come off when the shell is done, and the places where they were welded are dressed back level with the plate.':
        'Diese Laschen und die Hebeösen kommen ab, sobald der Mantel fertig ist, und ihre Schweißstellen werden bündig zum Blech verschliffen.',
    'Lifting is done on the overhead crane, using slings and a spreader beam. Bottom plates are cut and fitted on the shop floor.':
        'Gehoben wird mit dem Hallenkran, mit Anschlagmitteln und Traverse. Die Bodenbleche werden in der Halle zugeschnitten und eingepasst.',
    'In the shop the welding is done under cover and under a crane.':
        'In der Werkstatt wird überdacht und unter dem Kran geschweißt.',
    'A new valve station at the base of a storage tank. We set and levelled the valves, fitted the spools, welded and bolted the joints, and tied the run into the existing pipe rack.':
        'Eine neue Armaturenstation am Fuß eines Lagertanks. Wir haben die Armaturen gesetzt und ausgerichtet, die Spools eingepasst, die Verbindungen geschweißt und verschraubt und die Leitung an die bestehende Rohrbrücke angebunden.',
    'A new valve station at the base of a storage tank. We set and levelled the valves, fitted the spools, welded and bolted the joints, and tied the run...':
        'Eine neue Armaturenstation am Fuß eines Lagertanks. Wir haben die Armaturen gesetzt und ausgerichtet, die Spools eingepasst, die Verbindungen...',
    'A storage tank needed a new valve station and a connection into the existing pipe rack.':
        'Ein Lagertank brauchte eine neue Armaturenstation und eine Anbindung an die bestehende Rohrbrücke.',
    'The valves went on adjustable stands and we levelled them before anything was fixed. We did not tack until the run was straight and the flange faces were parallel.':
        'Die Armaturen kamen auf verstellbare Böcke, und wir haben sie ausgerichtet, bevor irgendetwas fixiert wurde. Geheftet wurde erst, als die Leitung gerade lief und die Flanschflächen parallel standen.',
    'Some of the joints are welded, the rest are flanged and bolted. The spools went in between them.':
        'Ein Teil der Verbindungen ist geschweißt, der Rest geflanscht und verschraubt. Dazwischen kamen die Spools.',
    'The close-up shows a finished root, taken down the bore from the open end of a spool.':
        'Die Nahaufnahme zeigt eine fertige Wurzel, aufgenommen durch die Bohrung vom offenen Ende eines Spools.',
    'The work front sat under temporary cover, with the plant live around it.':
        'Die Arbeitsfront lag unter provisorischer Überdachung, die Anlage ringsum in Betrieb.',
    'Internal pipe off a shell nozzle, brackets on pad plates, roof rafters into the centre ring.':
        'Innenleitung an einem Mantelstutzen, Konsolen auf Futterblechen, Dachsparren zum Zentralring.',
    'Internal pipe off a shell nozzle, brackets on pad plates, roof rafters into the centre...':
        'Innenleitung an einem Mantelstutzen, Konsolen auf Futterblechen, Dachsparren zum...',
    'On this job no bracket went straight onto the shell. Every attachment sat on a pad plate, and the pad was welded to the shell. The close-up shows one. If the bracket ever has to come off, it comes off the pad and the shell is untouched.':
        'Auf dieser Baustelle wurde keine Konsole direkt auf den Mantel geschweißt. Jedes Anbauteil sitzt auf einem Futterblech, und das Futterblech ist auf den Mantel geschweißt. Die Nahaufnahme zeigt eines. Muss die Konsole je herunter, kommt sie vom Futterblech, und der Mantel bleibt unberührt.',
    'Pads went down on the bottom plates as well, the stands went on the pads and the pipe sat on the stands. When the stands come off, the pads take the damage instead of the bottom plates.':
        'Auch auf die Bodenbleche kamen Futterbleche, auf die Futterbleche die Böcke und auf die Böcke das Rohr. Werden die Böcke entfernt, nehmen die Futterbleche den Schaden und nicht die Bodenbleche.',
    'The internal pipe runs from a shell nozzle across the tank, and the roof goes on radial rafters into a centre ring.':
        'Die Innenleitung führt von einem Mantelstutzen quer durch den Tank, und das Dach liegt auf radialen Sparren, die in einem Zentralring zusammenlaufen.',
    'Temporary steel goes on and comes off all the way through a job like this. Every place it was welded is ground back flush before the tank is painted.':
        'Bei einer solchen Arbeit werden ständig Hilfskonstruktionen angeschweißt und wieder entfernt. Jede Schweißstelle wird bündig verschliffen, bevor der Tank beschichtet wird.',
    'The shaft runs from the drive mounting on the roof down to a bearing at the floor, with two impellers on it.':
        'Die Welle läuft von der Antriebsaufnahme auf dem Dach bis zu einem Lager am Boden, mit zwei Rührorganen darauf.',
    'The shaft runs from the drive mounting on the roof down to a bearing at the floor, with two impellers on...':
        'Die Welle läuft von der Antriebsaufnahme auf dem Dach bis zu einem Lager am Boden, mit zwei...',
    'The agitator in this tank was being replaced. The shaft runs the full height of the tank, from the drive mounting on the roof down to a bearing at the floor. Two impellers on it, one low down and one near the roof.':
        'Das Rührwerk in diesem Tank wurde getauscht. Die Welle läuft über die volle Höhe des Tanks, von der Antriebsaufnahme auf dem Dach bis zu einem Lager am Boden. Zwei Rührorgane darauf, eines weit unten und eines nahe dem Dach.',
    'The fitting work was done inside the tank, with the tank out of service.':
        'Die Montage erfolgte im Tank, bei außer Betrieb genommenem Tank.',
    'The bearing at the floor went in first. We levelled it before any of the shaft went in, and checked the shaft once it was down. Everything above depends on that bearing.':
        'Das Lager am Boden kam zuerst. Wir haben es ausgerichtet, bevor die Welle eingebracht wurde, und die Welle geprüft, sobald sie unten war. Alles darüber hängt an diesem Lager.',
    'We fitted the lower impeller from the tank floor and the upper one from temporary access.':
        'Das untere Rührorgan haben wir vom Tankboden aus montiert, das obere von einem provisorischen Zugang.',

    # ---- plate-sequence redesign of /projects/*, 27 Aug 2026 ----
    'Scope':
        'Leistungsumfang',
    'Plates':
        'Tafeln',
    'Setting':
        'Umfeld',
    'More projects':
        'Weitere Projekte',
    '6 photographs':
        '6 Aufnahmen',
    '3 photographs':
        '3 Aufnahmen',
    'How it was built':
        'Wie es gebaut wurde',
    'Tank out of service':
        'Tank außer Betrieb',
    'Tank being fitted out':
        'Tank im Ausbau',
    'Fabrication shop, under a crane':
        'Fertigungshalle, unter dem Kran',
    'Live plant, work front under cover':
        'Anlage in Betrieb, Arbeitsfront überdacht',
    'The roof goes on radial rafters into a centre ring.':
        'Das Dach liegt auf radialen Sparren, die in einem Zentralring zusammenlaufen.',
    'One plate to a stage. Press a plate to open it full size.':
        'Eine Tafel je Arbeitsschritt. Zum Vergrößern eine Tafel anklicken.',
    'The internal pipe runs from a shell nozzle across the tank.':
        'Die Innenleitung führt von einem Mantelstutzen quer durch den Tank.',
    '<span class="case-num">04</span> <span class="case-kicker">Mechanical installation</span>':
        '<span class="case-num">04</span> <span class="case-kicker">Mechanische Montage</span>',
    '<span class="case-num">01</span> <span class="case-kicker">Shop fabrication and welding</span>':
        '<span class="case-num">01</span> <span class="case-kicker">Fertigung und Schweißen in der Werkstatt</span>',
    '<span class="case-num">03</span> <span class="case-kicker">Mechanical installation and welding</span>':
        '<span class="case-num">03</span> <span class="case-kicker">Mechanische Montage und Schweißen</span>',
    '<span class="case-num">02</span> <span class="case-kicker">Mechanical installation and welding &middot; tank farm</span>':
        '<span class="case-num">02</span> <span class="case-kicker">Mechanische Montage und Schweißen &middot; Tanklager</span>',
    '<span class="eyebrow">Index</span> <span class="case-next-t">All projects</span> <span class="arr" aria-hidden="true">&#8593;</span>':
        '<span class="eyebrow">Übersicht</span> <span class="case-next-t">Alle Projekte</span> <span class="arr" aria-hidden="true">&#8593;</span>',
    '<span class="eyebrow">Next project</span> <span class="case-next-t">Tank and vessel fabrication</span> <span class="arr" aria-hidden="true">&#8593;</span>':
        '<span class="eyebrow">Nächstes Projekt</span> <span class="case-next-t">Tank- und Behälterbau</span> <span class="arr" aria-hidden="true">&#8593;</span>',
    '<span class="eyebrow">Next project</span> <span class="case-next-t">Valve station and tie-in piping</span> <span class="arr" aria-hidden="true">&#8593;</span>':
        '<span class="eyebrow">Nächstes Projekt</span> <span class="case-next-t">Armaturenstation und Anbindungsleitungen</span> <span class="arr" aria-hidden="true">&#8593;</span>',
    '<span class="eyebrow">Next project</span> <span class="case-next-t">Tank internals, nozzles and attachments</span> <span class="arr" aria-hidden="true">&#8593;</span>':
        '<span class="eyebrow">Nächstes Projekt</span> <span class="case-next-t">Tankeinbauten, Stutzen und Anbauteile</span> <span class="arr" aria-hidden="true">&#8593;</span>',
    '<span class="eyebrow">Next project</span> <span class="case-next-t">Agitator replacement inside a storage tank</span> <span class="arr" aria-hidden="true">&#8593;</span>':
        '<span class="eyebrow">Nächstes Projekt</span> <span class="case-next-t">Rührwerkstausch in einem Lagertank</span> <span class="arr" aria-hidden="true">&#8593;</span>',
    'On this job no bracket went straight onto the shell. Every attachment sat on a pad plate, and the pad was welded to the shell. The close-up above shows one. If the bracket ever has to come off, it comes off the pad and the shell is untouched.':
        'Auf dieser Baustelle wurde keine Konsole direkt auf den Mantel geschweißt. Jedes Anbauteil sitzt auf einem Futterblech, und das Futterblech ist auf den Mantel geschweißt. Die Nahaufnahme oben zeigt eines. Muss die Konsole je herunter, kommt sie vom Futterblech, und der Mantel bleibt unberührt.',

    # ---- sticky plate deck, 27 Aug 2026 ----
    '<span class="slide-label">Stage</span> <span class="slide-count">01 / 02</span>':
        '<span class="slide-label">Arbeitsschritt</span> <span class="slide-count">01 / 02</span>',
    '<span class="slide-label">Stage</span> <span class="slide-count">01 / 05</span>':
        '<span class="slide-label">Arbeitsschritt</span> <span class="slide-count">01 / 05</span>',
    '<span class="slide-label">Stage</span> <span class="slide-count">02 / 02</span>':
        '<span class="slide-label">Arbeitsschritt</span> <span class="slide-count">02 / 02</span>',
    '<span class="slide-label">Stage</span> <span class="slide-count">02 / 05</span>':
        '<span class="slide-label">Arbeitsschritt</span> <span class="slide-count">02 / 05</span>',
    '<span class="slide-label">Stage</span> <span class="slide-count">03 / 05</span>':
        '<span class="slide-label">Arbeitsschritt</span> <span class="slide-count">03 / 05</span>',
    '<span class="slide-label">Stage</span> <span class="slide-count">04 / 05</span>':
        '<span class="slide-label">Arbeitsschritt</span> <span class="slide-count">04 / 05</span>',
    '<span class="slide-label">Stage</span> <span class="slide-count">05 / 05</span>':
        '<span class="slide-label">Arbeitsschritt</span> <span class="slide-count">05 / 05</span>',

    # ---- 26 Aug audit, remaining Block 2/4 corrections ----
    'Where we have delivered':
        'Wo wir gearbeitet haben',
    'Drydock and afloat (alongside) repair scopes':
        'Reparaturen im Dock und schwimmend (längsseits)',
    'We aim to reply to project enquiries within one working day.':
        'Wir bemühen uns, Projektanfragen innerhalb eines Werktags zu beantworten.',
    'The scope ran from September 2025 to April 2026 and was delivered by a team of 12 specialists, accumulating more than 11,000 hours on site.':
        'Der Auftrag lief von September 2025 bis April 2026 und wurde von einem Team von 12 Fachkräften ausgeführt, mit mehr als 11.000 Stunden vor Ort.',
    'Yard schedules move, and the penalty lands on the subcontractor. We plan for that, and take engine room piping, structural steel and outfitting as...':
        'Werftterminen verschieben sich, und die Vertragsstrafe trifft den Nachunternehmer. Wir planen das ein und übernehmen Maschinenraumrohrleitungen,...',
    'We track hours worked, incidents and what we changed as a result, and we share the figures with clients on request. A target nobody measures is a slogan.':
        'Wir erfassen geleistete Stunden, Vorfälle und was wir daraufhin geändert haben, und geben die Zahlen auf Anfrage an Kunden weiter. Ein Ziel, das niemand misst, ist ein Slogan.',
    'Yard schedules move, and the penalty lands on the subcontractor. We plan for that, and take engine room piping, structural steel and outfitting as complete scopes.':
        'Werftterminen verschieben sich, und die Vertragsstrafe trifft den Nachunternehmer. Wir planen das ein und übernehmen Maschinenraumrohrleitungen, Stahlbau und Ausrüstung als vollständige Lose.',
    'Head office in Klaipėda, Lithuania, with project bases in <strong>six countries</strong>, serving offshore, shipbuilding and industry across Northern and Western Europe.':
        'Hauptsitz in Klaipėda, Litauen, mit Projektstützpunkten in <strong>sechs Ländern</strong>, für Offshore, Schiffbau und Industrie in Nord- und Westeuropa.',
    'We draw on a roster of more than 300 certified specialists. Projects are resourced from that roster rather than subcontracted on, which is what keeps the quality system meaningful.':
        'Wir greifen auf einen Pool von mehr als 300 zertifizierten Fachkräften zurück. Projekte werden aus diesem Bestand besetzt und nicht weitervergeben, und genau das hält das Qualitätssystem belastbar.',
    'Lithuania &middot; Norway &middot; United Kingdom &middot; Netherlands &middot; Germany &middot; Belgium &mdash; offshore, shipbuilding and industry across Northern and Western Europe.':
        'Litauen &middot; Norwegen &middot; Vereinigtes Königreich &middot; Niederlande &middot; Deutschland &middot; Belgien &mdash; Offshore, Schiffbau und Industrie in Nord- und Westeuropa.',
    'Scaffolding costs more in downtime than in steel. IRATA-certified technicians, Levels 1 to 3, with an IRATA Level 3 supervisor on every site reach the same place on rope, inspect it and repair it while the plant keeps running.':
        'Ein Gerüst kostet mehr Stillstand als Stahl. IRATA-zertifizierte Techniker der Stufen 1 bis 3, mit einem IRATA-Level-3-Aufsichtsführenden auf jeder Baustelle, erreichen dieselbe Stelle am Seil, prüfen sie und setzen sie instand, während die Anlage weiterläuft.',
    'Awarded to ALPROJECTS, UAB by Creditinfo Group on 23 June 2026, recognising a high credit score and a proven record of financial stability. In heavy industry, projects run for months and commitments run for years &mdash; independent proof of stability is proof we will be there to see the work through.':
        'Verliehen an die ALPROJECTS, UAB durch die Creditinfo Group am 23. Juni 2026, in Anerkennung einer hohen Bonität und einer nachgewiesenen Finanzstabilität. In der Schwerindustrie laufen Projekte über Monate und Verpflichtungen über Jahre &mdash; ein unabhängiger Nachweis der Stabilität ist der Nachweis, dass wir die Arbeit zu Ende bringen.',

    # ---- audit Block 5: privacy sections, consent, abbreviations ----
    '9. Cookies':
        '9. Cookies',
    '12. Changes':
        '12. Änderungen',
    '11. Children':
        '11. Minderjährige',
    '7. Your rights':
        '7. Ihre Rechte',
    '5. Legal basis':
        '5. Rechtsgrundlage',
    '4. Recruitment data':
        '4. Bewerberdaten',
    '10. How we protect it':
        '10. Wie wir sie schützen',
    '6. How long we keep it':
        '6. Speicherdauer',
    '8. Health data in applications':
        '8. Gesundheitsdaten in Bewerbungen',
    'The site is served over HTTPS only, with HTTP redirected.':
        'Die Website wird ausschließlich über HTTPS ausgeliefert, HTTP wird umgeleitet.',
    'Access is removed when someone leaves the company or changes role.':
        'Zugänge werden entzogen, wenn jemand das Unternehmen verlässt oder die Funktion wechselt.',
    'It is a static site: no database, no user accounts and no login to compromise.':
        'Es ist eine statische Website: keine Datenbank, keine Benutzerkonten und kein Login, das kompromittiert werden könnte.',
    'We do not carry out automated decision-making or profiling, including in recruitment.':
        'Wir treffen keine automatisierten Entscheidungen und betreiben kein Profiling, auch nicht bei der Personalauswahl.',
    'This website is not intended for persons under 16, and we do not knowingly collect their personal data.':
        'Diese Website richtet sich nicht an Personen unter 16 Jahren, und wir erheben deren personenbezogene Daten nicht wissentlich.',
    'Application documents reach us by email and are stored in the company account, access limited to the people resourcing projects.':
        'Bewerbungsunterlagen erreichen uns per E-Mail und werden im Unternehmenskonto abgelegt; der Zugriff ist auf die Personen beschränkt, die Projekte besetzen.',
    'Industrial Rope Access Trade Association (IRATA) certified technicians, Levels 1 to 3, with an IRATA Level 3 supervisor on every site':
        'Von der Industrial Rope Access Trade Association (IRATA) zertifizierte Techniker der Stufen 1 bis 3, mit einem IRATA-Level-3-Aufsichtsführenden auf jeder Baustelle',
    'You may also withdraw consent at any time, without affecting the lawfulness of processing carried out before withdrawal (Article 7(3)).':
        'Sie können Ihre Einwilligung außerdem jederzeit widerrufen, ohne dass die Rechtmäßigkeit der bis zum Widerruf erfolgten Verarbeitung berührt wird (Artikel 7 Absatz 3).',
    'Welding Procedure Specification (WPS) to EN ISO 15609-1, qualified by Welding Procedure Qualification Record (WPQR) to EN ISO 15614-1, written for the project standard':
        'Schweißanweisung (WPS) nach EN ISO 15609-1, qualifiziert durch Schweißverfahrensprüfung (WPQR) nach EN ISO 15614-1, erstellt für die Projektnorm',
    'This section describes how the site and our handling are <em>designed</em>. It is not a statement that we hold an ISO 27001 certificate or any other security attestation, because we do not.':
        'Dieser Abschnitt beschreibt, wie die Website und unser Umgang damit <em>ausgelegt</em> sind. Er behauptet nicht, dass wir ein ISO-27001-Zertifikat oder einen anderen Sicherheitsnachweis besitzen, denn das tun wir nicht.',
    'This website sets no cookies of its own. It has no analytics, no advertising tags, no tracking pixels and no user accounts, so there is nothing to consent to and no cookie banner to dismiss.':
        'Diese Website setzt keine eigenen Cookies. Sie hat keine Analyse, keine Werbe-Tags, keine Tracking-Pixel und keine Benutzerkonten, also gibt es nichts einzuwilligen und kein Cookie-Banner wegzuklicken.',
    'By subscribing you agree that ALPROJECTS, UAB will process your email address to send company news and project updates. You can unsubscribe at any time. See our <a href="/privacy">Privacy Policy</a>.':
        'Mit dem Abonnement erklären Sie sich damit einverstanden, dass die ALPROJECTS, UAB Ihre E-Mail-Adresse verarbeitet, um Unternehmensnachrichten und Projektberichte zu versenden. Sie können sich jederzeit abmelden. Weitere Informationen in der <a href="/privacy">Datenschutzerklärung</a>.',
    'The one exception is the scheduling calendar on the contacts page. It is not loaded until you press the button that opens it; if you do, Calendly sets its own cookies at that point. Nothing is set if you do not.':
        'Die einzige Ausnahme ist der Terminkalender auf der Kontaktseite. Er wird erst geladen, wenn Sie die Schaltfläche drücken, die ihn öffnet; tun Sie das, setzt Calendly zu diesem Zeitpunkt eigene Cookies. Tun Sie es nicht, wird nichts gesetzt.',
    'Some applicants choose to upload a medical or fitness certificate. This is health data and falls under Article 9 GDPR. We process it only where it is necessary for obligations in the field of employment and occupational health and safety law (Article 9(2)(b)), we store it separately from other application data, and access is limited to the people responsible for mobilisation.':
        'Manche Bewerber laden ein ärztliches Attest oder eine Tauglichkeitsbescheinigung hoch. Das sind Gesundheitsdaten und fallen unter Artikel 9 DSGVO. Wir verarbeiten sie nur, soweit dies für Pflichten aus dem Arbeitsrecht und dem Arbeitsschutzrecht erforderlich ist (Artikel 9 Absatz 2 Buchstabe b), speichern sie getrennt von den übrigen Bewerbungsunterlagen, und der Zugriff ist auf die für die Mobilisierung zuständigen Personen beschränkt.',

    # ---- slide 3 valve-station photograph, 29 Aug 2026 ----
    'Tie-in piping and valve station at a tank farm, with gate and globe valves set on stands and the run tying into the existing rack':
        'Anbindungsleitungen und Armaturenstation in einem Tanklager, mit Absperrschiebern und Durchgangsventilen auf Böcken und der Leitung, die in die bestehende Rohrbrücke eingebunden ist',

    # ---- stats photo, nozzle tie-in, 29 Aug 2026 ----

    # ---- hero foot, 29 Aug 2026 ----
    '<span>Klaip&#279;da, Lithuania</span> <span class="hero-scroll">Scroll<i></i></span>':
        '<span>Klaip&#279;da, Litauen</span> <span class="hero-scroll">Scrollen<i></i></span>',

    # ---- sector titles disambiguated + news description, 29 Aug 2026 ----
    'Industrial sector — ALPROJECTS Group':
        'Sektor Industrie — ALPROJECTS Group',
    'Offshore sector — ALPROJECTS Group':
        'Sektor Offshore — ALPROJECTS Group',
    'Renewables sector — ALPROJECTS Group':
        'Sektor erneuerbare Energien — ALPROJECTS Group',
    'Shipbuilding sector — ALPROJECTS Group':
        'Sektor Schiffbau — ALPROJECTS Group',
    'Project updates and engineering insights from ALPROJECTS Group — welding, piping, NDT and offshore scopes across Northern and Western Europe.':
        'Projektberichte und Erfahrungen aus der Praxis von ALPROJECTS Group — Schweißen, Rohrleitungsbau, ZfP und Offshore-Lose in Nord- und Westeuropa.',

    # --- case: engine room piping and machinery installation -------------
    'Engine room piping and machinery installation':
        'Rohrleitungsbau und Maschinenmontage im Maschinenraum',
    'Engine room piping and machinery installation — ALPROJECTS Group':
        'Rohrleitungsbau und Maschinenmontage im Maschinenraum — ALPROJECTS Group',
    'Mechanical installation and piping · Shipbuilding':
        'Mechanische Montage und Rohrleitungsbau · Schiffbau',
    'Project &middot; Mechanical installation and piping · Shipbuilding':
        'Projekt &middot; Mechanische Montage und Rohrleitungsbau · Schiffbau',
    'Vessel under construction, machinery spaces':
        'Schiff im Bau, Maschinenräume',
    'Machinery on resilient mounts, and the seawater, bilge and fuel lines that connect it. The mounts went down first; the piping followed, through a compartment that was already full.':
        'Maschinen auf elastischer Lagerung und die Seewasser-, Bilge- und Brennstoffleitungen, die sie verbinden. Zuerst kam die Lagerung, dann die Rohrleitung — durch einen Raum, der bereits voll war.',
    'The mounts go down before anything else. We land the machine on them all at once, then set each mount so it takes its share of the load and sits within the deflection the maker allows. The alignment is checked and recorded before the first flange is made up, and again once the lines are connected.':
        'Die Lager kommen vor allem anderen. Wir setzen die Maschine in einem Zug auf alle Lager ab und stellen dann jedes Lager so ein, dass es seinen Anteil der Last trägt und innerhalb der vom Hersteller zugelassenen Einfederung bleibt. Die Ausrichtung wird geprüft und dokumentiert, bevor die erste Flanschverbindung hergestellt wird, und noch einmal, sobald die Leitungen angeschlossen sind.',
    'The drawing gives the route; the dimensions come off the steel. By the time the piping starts the space is full, so we build the valves, the strainer and the branches up on one frame outside the compartment and land the group as a unit, with the bolt holes matching and the flange faces square. Set out that way, somebody standing in front of it can reach every handwheel.':
        'Die Zeichnung gibt den Verlauf vor; die Maße werden am Stahl abgenommen. Wenn der Rohrleitungsbau beginnt, ist der Raum bereits voll; deshalb bauen wir Armaturen, Filter und Abzweige außerhalb des Raums auf einem Rahmen auf und setzen die Gruppe als Einheit ein — mit passenden Schraubenlöchern und planparallelen Flanschflächen. So angeordnet erreicht jemand, der davorsteht, jedes Handrad.',
    'We set the valve groups out to keep the tank access clear, because the covers have to come off in service. Open ends are capped whenever work stops on a line, and the system is blanked at its boundaries for the pressure test. Each line is tagged to the drawing as it is finished.':
        'Wir ordnen die Armaturengruppen so an, dass der Tankzugang frei bleibt, denn die Deckel müssen im Betrieb abgenommen werden können. Offene Enden werden verschlossen, sobald die Arbeit an einer Leitung unterbrochen wird, und für die Druckprüfung wird das System an seinen Grenzen abgeblindet. Jede Leitung wird nach Fertigstellung entsprechend der Zeichnung gekennzeichnet.',
    'Resiliently mounted machinery moves, and the hull works at sea. Flexible hoses take that movement at the machine connections. On the runs, mechanical couplings take up misalignment, and we anchor and guide the pipe either side of them so the coupling is not left carrying the line.':
        'Elastisch gelagerte Maschinen bewegen sich, und der Schiffskörper arbeitet auf See. An den Maschinenanschlüssen nehmen flexible Schlauchleitungen diese Bewegung auf. In den Strängen gleichen mechanische Kupplungen den Versatz aus, und wir setzen beiderseits davon Festpunkte und Führungen, damit die Kupplung die Leitung nicht tragen muss.',
    'Resilient mounts on the machined seating.':
        'Elastische Lager auf dem bearbeiteten Fundament.',
    'The seating, with the mounts set and the first lines alongside.':
        'Das Fundament mit gesetzten Lagern und den ersten Leitungen daneben.',
    'Valve and strainer group on the bulkhead.':
        'Armaturen- und Filtergruppe am Schott.',
    'Mechanical couplings on the large-bore runs.':
        'Mechanische Kupplungen an den Leitungen großer Nennweite.',
    'Valve group around the tank access cover.':
        'Armaturengruppe rund um den Tankdeckel.',
    'Machined seating in an engine room with resilient mounts bolted down, studs and nuts set, and timber packing alongside':
        'Bearbeitetes Fundament im Maschinenraum mit verschraubten elastischen Lagern, gesetzten Stiftschrauben und Muttern und Holzunterlagen daneben',
    'A row of resilient mounts along the machined seating, with the first pipe runs and capped flanges laid in beside them':
        'Eine Reihe elastischer Lager entlang des bearbeiteten Fundaments, daneben die ersten Rohrstränge und verschlossene Flansche',
    'Valve and strainer group made up on a frame against an engine room bulkhead, with globe valves, a basket strainer and capped branches':
        'Auf einem Rahmen vormontierte Armaturen- und Filtergruppe an einem Maschinenraumschott, mit Absperrventilen, einem Korbfilter und verschlossenen Abzweigen',
    'Large-bore pipe runs under a deckhead, with mechanical couplings on the vertical drop and anchors either side of them':
        'Rohrleitungen großer Nennweite unter der Decke, mit mechanischen Kupplungen am senkrechten Strang und Festpunkten beiderseits',
    'Valve group set out around a bolted tank access cover, with the covers left clear and every open end capped':
        'Armaturengruppe rund um einen verschraubten Tankdeckel angeordnet, die Deckel bleiben frei und jedes offene Ende ist verschlossen',
    'Send the drawings or the scope and we will come back with a price and crew dates. If it is a yard slot, tell us the window.':
        'Senden Sie die Zeichnungen oder den Leistungsumfang und wir melden uns mit Preis und Einsatzterminen. Bei einem Werfttermin nennen Sie uns bitte das Zeitfenster.',
    'Send us the drawings':
        'Schicken Sie uns die Zeichnungen',
    '<span class="case-num">01</span> <span class="case-kicker">Mechanical installation and piping · Shipbuilding</span>':
        '<span class="case-num">01</span> <span class="case-kicker">Mechanische Montage und Rohrleitungsbau · Schiffbau</span>',
    '<span class="eyebrow">Next project</span> <span class="case-next-t">Engine room piping and machinery installation</span> <span class="arr" aria-hidden="true">&#8593;</span>':
        '<span class="eyebrow">Nächstes Projekt</span> <span class="case-next-t">Rohrleitungsbau und Maschinenmontage im Maschinenraum</span> <span class="arr" aria-hidden="true">&#8593;</span>',

    # --- case: foundations, penetrations and equipment installation -----
    'Foundations, penetrations and equipment installation':
        'Fundamente, Durchführungen und Anlagenmontage',
    'Foundations, penetrations and equipment installation — ALPROJECTS Group':
        'Fundamente, Durchführungen und Anlagenmontage — ALPROJECTS Group',
    'Steel fabrication and mechanical installation · Shipbuilding':
        'Stahlfertigung und mechanische Montage · Schiffbau',
    'Project &middot; Steel fabrication and mechanical installation · Shipbuilding':
        'Projekt &middot; Stahlfertigung und mechanische Montage · Schiffbau',
    'Vessel under construction, machinery and tank spaces':
        'Schiff im Bau, Maschinen- und Tankräume',
    'The steel that has to be in place before the equipment. We made and set the seats and frames, cut the openings and welded in the bulkhead penetrations, and fitted the supports for the cable and pipe routes.':
        'Der Stahl, der vor der Ausrüstung stehen muss. Wir haben die Fundamente und Rahmen gefertigt und gesetzt, die Öffnungen geschnitten und die Schottdurchführungen eingeschweißt und die Halterungen für die Kabel- und Rohrtrassen montiert.',
    'Frames and seats are fabricated to the drawing, then set to the steel that is actually there. We land the frame on the marked position, check it for position and level, and weld it down once it sits right. A unit light enough to be landed with its frame goes in first. Anything heavier goes on after the frame is welded down, and stays under cover until commissioning.':
        'Rahmen und Fundamente werden nach Zeichnung gefertigt und dann auf den tatsächlich vorhandenen Stahl gesetzt. Wir setzen den Rahmen auf die angerissene Position, prüfen Lage und Waage und schweißen ihn fest, sobald er richtig sitzt. Eine Einheit, die leicht genug ist, um mit ihrem Rahmen eingebracht zu werden, kommt zuerst hinein. Alles Schwerere kommt erst nach dem Festschweißen des Rahmens hinzu und bleibt bis zur Inbetriebnahme abgedeckt.',
    'We mark the opening from the ring that goes into it, cut it, and prepare the edge before the ring is offered up. That way the root gap is even the whole way round. On a watertight boundary the gap is what the weld has to close, and an uneven one shows up at the tightness test.':
        'Wir reißen die Öffnung nach dem Ring an, der hineinkommt, schneiden sie und bereiten die Kante vor, bevor der Ring angesetzt wird. So ist der Wurzelspalt rundum gleichmäßig. An einer wasserdichten Begrenzung ist der Spalt das, was die Naht schließen muss, und ein ungleichmäßiger zeigt sich bei der Dichtheitsprüfung.',
    'The ring is worked from both sides at once. One fitter checks the alignment inside the opening while another dresses the prep outside, and we tack in a balanced sequence so the ring does not pull as it is welded out.':
        'Der Ring wird von beiden Seiten gleichzeitig bearbeitet. Ein Monteur prüft die Ausrichtung innerhalb der Öffnung, während ein zweiter außen die Schweißnahtvorbereitung nacharbeitet, und wir heften in ausgewogener Folge, damit sich der Ring beim Ausschweißen nicht verzieht.',
    'Supports for cable and pipe routes go on before the boundary is closed in. We set the brackets clear of the insulation and the pins that hold it, so the tray runs at its own height and nothing has to be cut back when the lining goes on.':
        'Die Halterungen für Kabel- und Rohrtrassen kommen an, bevor die Begrenzung geschlossen wird. Wir setzen die Konsolen frei von der Isolierung und den Isolierstiften, damit die Kabelbahn auf ihrer eigenen Höhe läuft und beim Anbringen der Verkleidung nichts zurückgeschnitten werden muss.',
    'Coming down on the marked position.':
        'Absenken auf die angerissene Position.',
    'The unit on its frame, covered until commissioning.':
        'Die Einheit auf ihrem Rahmen, abgedeckt bis zur Inbetriebnahme.',
    'The opening cut, and the penetration piece ready to go in.':
        'Die geschnittene Öffnung und das Durchführungsstück, bereit zum Einbau.',
    'Dressing the prep before the penetration is welded out.':
        'Nacharbeit der Schweißnahtvorbereitung vor dem Ausschweißen der Durchführung.',
    'Cable tray supports on an insulated boundary.':
        'Kabelbahnhalterungen an einer isolierten Begrenzung.',
    'Cylindrical steel unit in a fabricated frame, suspended on chain hoists over its marked position on the deck of a vessel under construction':
        'Zylindrische Stahleinheit in einem gefertigten Rahmen, an Kettenzügen über ihrer angerissenen Position auf dem Deck eines im Bau befindlichen Schiffes',
    'Machinery unit under protective covers on a fabricated steel frame in a shipyard hall':
        'Maschineneinheit unter Schutzabdeckungen auf einem gefertigten Stahlrahmen in einer Werfthalle',
    'Circular opening cut in a bulkhead, with the penetration piece standing ready on the deck beside it':
        'Runde Öffnung in einem Schott, daneben steht das Durchführungsstück bereit auf dem Deck',
    'Two fitters at a bulkhead penetration, one checking alignment inside the opening while the other dresses the edge with a grinder':
        'Zwei Monteure an einer Schottdurchführung: einer prüft die Ausrichtung innerhalb der Öffnung, der andere arbeitet die Kante mit dem Schleifer nach',
    'Cable trays and brackets fitted to an insulated bulkhead, with insulation pins welded across the plate':
        'Kabelbahnen und Konsolen an einem isolierten Schott, mit über die Platte verteilt aufgeschweißten Isolierstiften',
    '<span class="case-num">02</span> <span class="case-kicker">Steel fabrication and mechanical installation · Shipbuilding</span>':
        '<span class="case-num">02</span> <span class="case-kicker">Stahlfertigung und mechanische Montage · Schiffbau</span>',
    '<span class="eyebrow">Next project</span> <span class="case-next-t">Foundations, penetrations and equipment installation</span> <span class="arr" aria-hidden="true">&#8593;</span>':
        '<span class="eyebrow">Nächstes Projekt</span> <span class="case-next-t">Fundamente, Durchführungen und Anlagenmontage</span> <span class="arr" aria-hidden="true">&#8593;</span>',
    '<span class="case-num">03</span> <span class="case-kicker">Shop fabrication and welding</span>':
        '<span class="case-num">03</span> <span class="case-kicker">Fertigung und Schweißen in der Werkstatt</span>',
    '<span class="case-num">04</span> <span class="case-kicker">Mechanical installation and welding &middot; tank farm</span>':
        '<span class="case-num">04</span> <span class="case-kicker">Mechanische Montage und Schweißen &middot; Tanklager</span>',
    '<span class="case-num">05</span> <span class="case-kicker">Mechanical installation and welding</span>':
        '<span class="case-num">05</span> <span class="case-kicker">Mechanische Montage und Schweißen</span>',
    '<span class="case-num">06</span> <span class="case-kicker">Mechanical installation</span>':
        '<span class="case-num">06</span> <span class="case-kicker">Mechanische Montage</span>',
    'The steel that has to be in place before the equipment. We made and set the seats and frames, cut the openings and welded in the bulkhead penetrations, and fitted the supports for the cable and...':
        'Der Stahl, der vor der Ausrüstung stehen muss. Wir haben die Fundamente und Rahmen gefertigt und gesetzt, die Öffnungen geschnitten und die Schottdurchführungen eingeschweißt und die Halterungen...',

    # --- case: large-bore pipe replacement -------------------------------
    'Large-bore pipe replacement':
        'Austausch von Rohrleitungen großer Nennweite',
    'Large-bore pipe replacement — ALPROJECTS Group':
        'Austausch von Rohrleitungen großer Nennweite — ALPROJECTS Group',
    'Mechanical installation and welding · Industrial':
        'Mechanische Montage und Schweißen · Industrie',
    'Project &middot; Mechanical installation and welding · Industrial':
        'Projekt &middot; Mechanische Montage und Schweißen · Industrie',
    'Existing plant, scaffolded work fronts':
        'Bestandsanlage, eingerüstete Arbeitsfronten',
    'Large-bore pipework replaced inside an existing plant. We prefabricated the spools, rigged them into position on chain hoists off the plant steel, and welded them in place.':
        'Austausch von Rohrleitungen großer Nennweite in einer Bestandsanlage. Wir haben die Rohrspools vorgefertigt, sie mit Kettenzügen am Anlagenstahl in Position gebracht und vor Ort eingeschweißt.',
    'We put the covers down before anything hot starts — blankets under the work front, sheeting across what is behind it, and the grating below closed off. A spark that goes through the grating lands on whatever is on the level under you.':
        'Die Abdeckungen kommen, bevor irgendetwas Heißes beginnt — Schweißdecken unter der Arbeitsfront, Planen über allem, was dahinter liegt, und der Gitterrost darunter geschlossen. Ein Funke, der durch den Gitterrost fällt, landet auf dem, was eine Ebene tiefer steht.',
    'Branches and stubs go on at floor level, where the piece can be turned and the weld is made in the flat position. The spool goes up as one piece with its openings already in it. Every branch done down here is one less weld made overhead.':
        'Abzweige und Stutzen werden am Boden angeschweißt, wo sich das Teil drehen lässt und die Naht in Wannenlage ausgeführt wird. Der Rohrspool geht als ein Stück nach oben, die Öffnungen sind bereits darin. Jeder Abzweig, der hier unten fertig wird, ist eine Naht weniger über Kopf.',
    'There is no crane over the work front, so the load comes off the plant steel. We agree the attachment points with the plant first, then hang beam clamps and chain hoists at each end and walk the spool into line by hand.':
        'Über der Arbeitsfront gibt es keinen Kran, also wird die Last am Anlagenstahl aufgenommen. Die Anschlagpunkte stimmen wir zuerst mit dem Betreiber ab, hängen dann an beiden Enden Trägerklemmen und Kettenzüge ein und ziehen den Rohrspool von Hand in die Flucht.',
    'Fit-up decides the joint. We set the gap and hold it the whole way round before an arc is struck, and the root goes in first — in this frame it is part way round, with the gap above still open. The joint is cleaned and checked before the fill and cap go on.':
        'Der Zusammenbau entscheidet über die Naht. Wir stellen den Spalt ein und halten ihn rundum, bevor ein Lichtbogen gezündet wird, und zuerst kommt die Wurzellage — in dieser Aufnahme ist sie ein Stück weit herum, oben ist der Spalt noch offen. Die Naht wird gereinigt und geprüft, bevor Füll- und Decklage folgen.',
    'The new run in place.':
        'Die neue Leitung an ihrem Platz.',
    'The work front covered before hot work starts.':
        'Die Arbeitsfront abgedeckt, bevor die Heißarbeiten beginnen.',
    'Branch and stub welded on before the spool goes up.':
        'Abzweig und Stutzen angeschweißt, bevor der Rohrspool nach oben geht.',
    'Beam clamps and chain hoists off the existing steel.':
        'Trägerklemmen und Kettenzüge am vorhandenen Stahlbau.',
    'The root run part way round the joint.':
        'Die Wurzellage ein Stück weit um die Naht herum.',
    'New large-bore pipework and a fabricated bend installed among existing lines and ducts inside an industrial plant':
        'Neue Rohrleitungen großer Nennweite und ein gefertigter Bogen, eingebaut zwischen vorhandenen Leitungen und Kanälen in einer Industrieanlage',
    'Protective sheeting and welding blankets laid over plant grating around a pipe spool standing ready for installation':
        'Schutzplanen und Schweißdecken über dem Gitterrost der Anlage, rund um einen zum Einbau bereitstehenden Rohrspool',
    'Prefabricated pipe bend with a welded branch and stub, standing on timber on plant grating':
        'Vorgefertigter Rohrbogen mit angeschweißtem Abzweig und Stutzen, auf Holzunterlagen auf dem Gitterrost der Anlage',
    'Two beam clamps and chain hoists rigged from overhead steel, taking the weight of a large-bore pipe':
        'Zwei Trägerklemmen mit Kettenzügen, am darüberliegenden Stahlbau angeschlagen und das Gewicht eines Rohres großer Nennweite aufnehmend',
    'Close-up of a pipe butt joint with an even root gap and the root run part way round':
        'Nahaufnahme einer Rohrstumpfnaht mit gleichmäßigem Wurzelspalt und der Wurzellage, die ein Stück weit herumgeführt ist',
    '<span class="case-num">03</span> <span class="case-kicker">Mechanical installation and welding · Industrial</span>':
        '<span class="case-num">03</span> <span class="case-kicker">Mechanische Montage und Schweißen · Industrie</span>',
    '<span class="eyebrow">Next project</span> <span class="case-next-t">Large-bore pipe replacement</span> <span class="arr" aria-hidden="true">&#8593;</span>':
        '<span class="eyebrow">Nächstes Projekt</span> <span class="case-next-t">Austausch von Rohrleitungen großer Nennweite</span> <span class="arr" aria-hidden="true">&#8593;</span>',
    '<span class="case-num">04</span> <span class="case-kicker">Shop fabrication and welding</span>':
        '<span class="case-num">04</span> <span class="case-kicker">Fertigung und Schweißen in der Werkstatt</span>',
    '<span class="case-num">05</span> <span class="case-kicker">Mechanical installation and welding &middot; tank farm</span>':
        '<span class="case-num">05</span> <span class="case-kicker">Mechanische Montage und Schweißen &middot; Tanklager</span>',
    '<span class="case-num">06</span> <span class="case-kicker">Mechanical installation and welding</span>':
        '<span class="case-num">06</span> <span class="case-kicker">Mechanische Montage und Schweißen</span>',
    '<span class="case-num">07</span> <span class="case-kicker">Mechanical installation</span>':
        '<span class="case-num">07</span> <span class="case-kicker">Mechanische Montage</span>',

    # --- case: grate bar replacement -------------------------------------
    'Grate bar replacement':
        'Austausch von Roststäben',
    'Grate bar replacement — ALPROJECTS Group':
        'Austausch von Roststäben — ALPROJECTS Group',
    'Mechanical maintenance · Waste to energy':
        'Mechanische Instandhaltung · Müllheizkraftwerk',
    'Project &middot; Mechanical maintenance · Waste to energy':
        'Projekt &middot; Mechanische Instandhaltung · Müllheizkraftwerk',
    'Waste-to-energy plant, furnace during outage':
        'Müllheizkraftwerk, Feuerraum während der Revision',
    'Grate bars replaced inside the furnace of a waste-to-energy plant during the outage. The old bars came out one row at a time, cut free where they were seized, and the new ones went back set to the specified gap.':
        'Austausch der Roststäbe im Feuerraum eines Müllheizkraftwerks während der Revision. Die alten Stäbe kamen reihenweise heraus, dort freigeschnitten, wo sie festgefressen waren, und die neuen gingen mit dem vorgegebenen Spalt wieder hinein.',
    'How it was done':
        'Wie es ausgeführt wurde',
    'The furnace is cold by the time we go in, but it is not clean. Everything inside is coated in fly ash and combustion residue, so the crew works in disposable coveralls and P3 respirators, and the suits come off at the door. Entry is under permit, with the space ventilated and the atmosphere monitored.':
        'Wenn wir einfahren, ist der Feuerraum kalt, aber nicht sauber. Alles darin ist mit Flugasche und Verbrennungsrückständen bedeckt, deshalb arbeitet die Mannschaft in Einweg-Schutzanzügen und mit P3-Atemschutz, und die Anzüge bleiben am Ausstieg. Das Befahren erfolgt mit Erlaubnisschein, bei belüftetem Raum und überwachter Atmosphäre.',
    'The bars sit in rows across the grate, and after a full run most of them are seized in place. They come out one row at a time — cut free where they will not move, lifted out by hand and stacked. The new ones go back set to the gap the maker specifies, because that gap is how the primary air reaches the bed.':
        'Die Stäbe liegen in Reihen über den Rost, und nach einer vollen Reise sitzen die meisten fest. Sie kommen reihenweise heraus — freigeschnitten, wo sie sich nicht bewegen lassen, von Hand herausgehoben und gestapelt. Die neuen gehen mit dem vom Hersteller vorgegebenen Spalt wieder hinein, denn über diesen Spalt erreicht die Primärluft das Brennbett.',
    'Cutting seized steel free.':
        'Festgefressener Stahl wird freigeschnitten.',
    'Disposable coveralls and P3 respirators.':
        'Einweg-Schutzanzüge und P3-Atemschutz.',
    'Old bars out, one row at a time.':
        'Alte Stäbe heraus, Reihe für Reihe.',
    'Worker in disposable coveralls and respirator cutting seized steel free with an oxy-fuel torch at the grate, with removed grate blocks in the foreground':
        'Arbeiter in Einweg-Schutzanzug und mit Atemschutz schneidet am Rost festgefressenen Stahl mit dem Brennschneider frei, im Vordergrund ausgebaute Rostblöcke',
    'Worker in a hard hat, goggles and P3 respirator inside the cold furnace of a waste-to-energy plant':
        'Arbeiter mit Schutzhelm, Schutzbrille und P3-Atemschutz im kalten Feuerraum eines Müllheizkraftwerks',
    'Two workers in disposable coveralls levering an old grate bar out of its row, with removed bars stacked behind them':
        'Zwei Arbeiter in Einweg-Schutzanzügen hebeln einen alten Roststab aus seiner Reihe, dahinter gestapelte ausgebaute Stäbe',
    'Send us the scope and we will come back with a price and crew dates. If it is an outage, tell us the window.':
        'Senden Sie uns den Leistungsumfang und wir melden uns mit Preis und Einsatzterminen. Bei einer Revision nennen Sie uns bitte das Zeitfenster.',
    'Eight scopes, photographed as they were built.':
        'Acht Projekte, fotografiert während der Ausführung.',
    '<span class="case-num">04</span> <span class="case-kicker">Mechanical maintenance · Waste to energy</span>':
        '<span class="case-num">04</span> <span class="case-kicker">Mechanische Instandhaltung · Müllheizkraftwerk</span>',
    '<span class="eyebrow">Next project</span> <span class="case-next-t">Grate bar replacement</span> <span class="arr" aria-hidden="true">&#8593;</span>':
        '<span class="eyebrow">Nächstes Projekt</span> <span class="case-next-t">Austausch von Roststäben</span> <span class="arr" aria-hidden="true">&#8593;</span>',
    '<span class="case-num">05</span> <span class="case-kicker">Shop fabrication and welding</span>':
        '<span class="case-num">05</span> <span class="case-kicker">Fertigung und Schweißen in der Werkstatt</span>',
    '<span class="case-num">06</span> <span class="case-kicker">Mechanical installation and welding &middot; tank farm</span>':
        '<span class="case-num">06</span> <span class="case-kicker">Mechanische Montage und Schweißen &middot; Tanklager</span>',
    '<span class="case-num">07</span> <span class="case-kicker">Mechanical installation and welding</span>':
        '<span class="case-num">07</span> <span class="case-kicker">Mechanische Montage und Schweißen</span>',
    '<span class="case-num">08</span> <span class="case-kicker">Mechanical installation</span>':
        '<span class="case-num">08</span> <span class="case-kicker">Mechanische Montage</span>',
    'Grate bars replaced inside the furnace of a waste-to-energy plant during the outage. The old bars came out one row at a time, cut free where they were seized, and the new ones went back set to the...':
        'Austausch der Roststäbe im Feuerraum eines Müllheizkraftwerks während der Revision. Die alten Stäbe kamen reihenweise heraus, dort freigeschnitten, wo sie festgefressen waren, und die neuen gingen...',

    # --- case: offshore rope access welding (draft until consent) ---
    'Offshore rope access welding':
        'Schweißen mit Seilzugangstechnik offshore',
    'Offshore rope access welding — ALPROJECTS Group':
        'Schweißen mit Seilzugangstechnik offshore — ALPROJECTS Group',
    'Welding and rope access · Offshore':
        'Schweißen und Seilzugangstechnik · Offshore',
    'Project &middot; Welding and rope access · Offshore':
        'Projekt &middot; Schweißen und Seilzugangstechnik · Offshore',
    'Offshore platform, Northern Europe':
        'Offshore-Plattform, Nordeuropa',
    'Welding on the outside of an offshore platform, carried out on rope access. There is no scaffold and no basket over the side, so the welder reaches the joint on ropes and works from the harness.':
        'Schweißarbeiten an der Außenseite einer Offshore-Plattform, ausgeführt mit Seilzugangstechnik. Es gibt weder Gerüst noch Arbeitskorb über der Bordwand, also erreicht der Schweißer die Naht am Seil und arbeitet aus dem Gurt.',
    'The platform has no quay and no road. Crew, tools and consumables arrive by vessel or helicopter and stay for the shift, and the working window is set by wind and sea state rather than by the programme.':
        'Die Plattform hat weder Kai noch Straße. Mannschaft, Werkzeug und Verbrauchsmaterial kommen per Schiff oder Hubschrauber und bleiben für die Schicht, und das Arbeitsfenster bestimmen Wind und Seegang, nicht der Terminplan.',
    'Welding is carried out from the harness, on a working line and a backup rigged from the structure above, with the team working in pairs. The joint is prepared before the arc is struck and completed in short runs. The return clamp is placed on the work close to the joint — over water the return path is part of the safety case, not a detail.':
        'Geschweißt wird aus dem Gurt, an einem Arbeits- und einem Sicherungsseil, die von der Konstruktion darüber eingerichtet sind, und immer zu zweit. Die Naht wird vorbereitet, bevor der Lichtbogen gezündet wird, und in kurzen Raupen fertiggestellt. Die Masseklemme sitzt nah an der Naht am Werkstück — über Wasser gehört die Rückleitung zum Sicherheitskonzept und nicht zu den Details.',
    'Rope access over open water.':
        'Seilzugangstechnik über offenem Wasser.',
    'Access by vessel or helicopter only.':
        'Zugang nur per Schiff oder Hubschrauber.',
    'Welding carried out from the harness.':
        'Geschweißt wird aus dem Gurt.',
    'Rope access technician suspended in a harness on the outside of an offshore platform, with wind turbines on the horizon':
        'Seilzugangstechniker im Gurt an der Außenseite einer Offshore-Plattform, am Horizont Windkraftanlagen',
    'Side of an offshore platform above the sea, with wind turbines in low cloud on the horizon':
        'Flanke einer Offshore-Plattform über der See, am Horizont Windkraftanlagen in tiefer Bewölkung',
    'Two rope access technicians suspended on twin ropes at a yellow structure on an offshore platform, one wearing a welding helmet, with cables run down from the deck above':
        'Zwei Seilzugangstechniker an Doppelseilen an einer gelben Konstruktion auf einer Offshore-Plattform, einer mit Schweißerhelm, die Kabel sind vom Deck darüber herabgeführt',
    'Send us the scope and we will come back with a price and crew dates. For offshore work tell us the access, the vessel and the weather window.':
        'Senden Sie uns den Leistungsumfang und wir melden uns mit Preis und Einsatzterminen. Bei Offshore-Arbeiten nennen Sie uns bitte den Zugang, das Schiff und das Wetterfenster.',
    'Nine scopes, photographed as they were built.':
        'Neun Projekte, fotografiert während der Ausführung.',
    '<span class="case-num">05</span> <span class="case-kicker">Welding and rope access · Offshore</span>':
        '<span class="case-num">05</span> <span class="case-kicker">Schweißen und Seilzugangstechnik · Offshore</span>',
    '<span class="eyebrow">Next project</span> <span class="case-next-t">Offshore rope access welding</span> <span class="arr" aria-hidden="true">&#8593;</span>':
        '<span class="eyebrow">Nächstes Projekt</span> <span class="case-next-t">Schweißen mit Seilzugangstechnik offshore</span> <span class="arr" aria-hidden="true">&#8593;</span>',
    '<span class="case-num">06</span> <span class="case-kicker">Shop fabrication and welding</span>':
        '<span class="case-num">06</span> <span class="case-kicker">Fertigung und Schweißen in der Werkstatt</span>',
    '<span class="case-num">07</span> <span class="case-kicker">Mechanical installation and welding &middot; tank farm</span>':
        '<span class="case-num">07</span> <span class="case-kicker">Mechanische Montage und Schweißen &middot; Tanklager</span>',
    '<span class="case-num">08</span> <span class="case-kicker">Mechanical installation and welding</span>':
        '<span class="case-num">08</span> <span class="case-kicker">Mechanische Montage und Schweißen</span>',
    '<span class="case-num">09</span> <span class="case-kicker">Mechanical installation</span>':
        '<span class="case-num">09</span> <span class="case-kicker">Mechanische Montage</span>',

    # --- case: fan replacement and duct adaptation ------------------
    'Fan replacement and duct adaptation':
        'Ventilatortausch und Anpassung der Luftkanäle',
    'Fan replacement and duct adaptation — ALPROJECTS Group':
        'Ventilatortausch und Anpassung der Luftkanäle — ALPROJECTS Group',
    'Existing plant, outdoor process platform':
        'Bestandsanlage, Prozessbühne im Freien',
    'An extraction fan replaced on a process platform. The ducting that was already there did not suit the new unit, so we cut it back, made the transition pieces to fit, and connected the fan on both sides.':
        'Austausch eines Absaugventilators auf einer Prozessbühne. Die vorhandenen Luftkanäle passten nicht zum neuen Aggregat, deshalb haben wir sie zurückgeschnitten, die Übergangsstücke passgenau gefertigt und den Ventilator auf beiden Seiten angeschlossen.',
    'The fan comes to site as one assembly — casing, impeller, motor and base frame together. What decides the job is not the fan itself but its connection dimensions: the inlet, the outlet and the bolt pattern under the frame. On a replacement they rarely match what is already there, and here they did not.':
        'Der Ventilator kommt als komplette Einheit auf die Baustelle — Gehäuse, Laufrad, Motor und Grundrahmen zusammen. Über die Arbeit entscheidet nicht das Aggregat selbst, sondern seine Anschlussmaße: Saugseite, Druckseite und das Lochbild unter dem Rahmen. Bei einem Austausch passen sie selten zum Bestand, und hier passten sie nicht.',
    'The fan is landed on its base and stays on the sling until it is fixed down. The old frame did not leave the seats where the new one needs them, so they are made to suit the new footprint before anything is bolted — a fan sitting on a base that is out carries that error straight into its bearings. Anything hot happens over a blanket, with an extinguisher at the work front.':
        'Der Ventilator wird auf seinem Fundament abgesetzt und bleibt am Anschlagmittel, bis er befestigt ist. Der alte Rahmen hat die Auflager nicht dort hinterlassen, wo der neue sie braucht, deshalb werden sie vor dem Verschrauben auf das neue Aufstellmaß gearbeitet — ein Ventilator auf einem unebenen Fundament trägt diesen Fehler direkt in seine Lager. Alles Heiße geschieht über einer Schweißdecke, mit einem Feuerlöscher an der Arbeitsstelle.',
    'The inlet side is where the old ducting has to give. We take the weight of the duct on a sling first, so nothing is hanging on the joint once it is open, then cut it back and set a stub into it to suit the fan inlet. The fan drawing gives the size; where the stub lands is measured on the duct itself.':
        'Auf der Saugseite muss der alte Kanal nachgeben. Zuerst nehmen wir sein Gewicht am Anschlagmittel auf, damit nach dem Öffnen nichts an der Verbindung hängt, dann schneiden wir ihn zurück und setzen einen Stutzen passend zum Saugstutzen des Ventilators ein. Das Maß gibt die Zeichnung des Ventilators vor; wo der Stutzen sitzt, wird am Kanal selbst abgenommen.',
    'The outlet goes up into the existing stack, and the two do not meet on their own. We make the transition, offer it up with the fan standing on its base, and mark it in position. Nothing is finish-welded until both ends have been proved against the openings they have to land on.':
        'Die Druckseite geht nach oben in den bestehenden Schornstein, und von allein treffen die beiden nicht zusammen. Wir fertigen das Übergangsstück, setzen es bei auf dem Fundament stehendem Ventilator an und reißen es in Einbaulage an. Endgültig verschweißt wird nichts, bevor beide Enden gegen die Öffnungen geprüft sind, auf die sie treffen müssen.',
    'Both connections finish on something flexible — a sleeve at the inlet and a bolted expansion joint at the outlet. The frame itself stands on anti-vibration mounts, so the machine is free to move a little; these two joints are what keep that movement out of the ducting, and they let the flanges sit a fraction out of line without loading either side. With those in, the adapter welds are dressed back and the expansion joint is bolted up all round.':
        'Beide Anschlüsse enden elastisch — eine Manschette auf der Saugseite und ein verschraubter Kompensator auf der Druckseite. Der Rahmen selbst steht auf Schwingungsdämpfern, das Aggregat darf sich also ein wenig bewegen; diese beiden Verbindungen halten diese Bewegung aus den Kanälen heraus und lassen die Flansche einen Bruchteil versetzt sitzen, ohne eine der Seiten zu belasten. Sind sie eingebaut, werden die Nähte der Übergangsstücke nachgearbeitet und der Kompensator rundum verschraubt.',
    'The new fan, connected on both sides.':
        'Der neue Ventilator, auf beiden Seiten angeschlossen.',
    'The new unit as delivered.':
        'Das neue Aggregat im Lieferzustand.',
    'Base work before the fan is bolted down.':
        'Arbeiten am Fundament, bevor der Ventilator verschraubt wird.',
    'The duct carried on a sling while the joint is open.':
        'Der Kanal hängt am Anschlagmittel, solange die Verbindung offen ist.',
    'The outlet transition offered up in position.':
        'Das Übergangsstück der Druckseite in Einbaulage angesetzt.',
    'The expansion joint between fan and stack.':
        'Der Kompensator zwischen Ventilator und Schornstein.',
    'New blue centrifugal fan installed on a steel base on an outdoor grating platform, its outlet connected through an expansion joint to the existing painted exhaust stack':
        'Neuer blauer Radialventilator auf einem Stahlfundament auf einer Gitterrostbühne im Freien, die Druckseite über einen Kompensator an den bestehenden lackierten Abluftschornstein angeschlossen',
    'New centrifugal fan and motor on a pallet as delivered to site, before installation':
        'Neuer Radialventilator mit Motor auf einer Palette im Lieferzustand, vor der Montage',
    'Worker at the base of the newly landed fan on the grating platform, with lifting slings, tools and a fire extinguisher laid out beside him':
        'Arbeiter am Fundament des gerade abgesetzten Ventilators auf der Gitterrostbühne, daneben Anschlagmittel, Werkzeug und ein Feuerlöscher',
    'Existing rectangular duct supported on a round sling while its open end is connected to the inlet of the new fan':
        'Bestehender Rechteckkanal an einem Rundschlingen-Anschlagmittel abgefangen, während sein offenes Ende an die Saugseite des neuen Ventilators angeschlossen wird',
    'New fan standing on its base with the outlet transition piece offered up under the existing stack':
        'Neuer Ventilator auf seinem Fundament, das Übergangsstück der Druckseite unter dem bestehenden Schornstein angesetzt',
    'Fabric expansion joint with tie rods bolted between the fan outlet and the adapted exhaust duct above it':
        'Gewebekompensator mit Zugankern, verschraubt zwischen der Druckseite des Ventilators und dem angepassten Abluftkanal darüber',
    '<span class="case-num">05</span> <span class="case-kicker">Mechanical installation and welding · Industrial</span>':
        '<span class="case-num">05</span> <span class="case-kicker">Mechanische Montage und Schweißen · Industrie</span>',
    '<span class="eyebrow">Next project</span> <span class="case-next-t">Fan replacement and duct adaptation</span> <span class="arr" aria-hidden="true">&#8593;</span>':
        '<span class="eyebrow">Nächstes Projekt</span> <span class="case-next-t">Ventilatortausch und Anpassung der Luftkanäle</span> <span class="arr" aria-hidden="true">&#8593;</span>',
    'An extraction fan replaced on a process platform. The ducting that was already there did not suit the new unit, so we cut it back, made the transition pieces to fit, and connected the fan on both...':
        'Austausch eines Absaugventilators auf einer Prozessbühne. Die vorhandenen Luftkanäle passten nicht zum neuen Aggregat, deshalb haben wir sie zurückgeschnitten, die Übergangsstücke passgenau...',
}
