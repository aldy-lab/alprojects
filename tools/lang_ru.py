# -*- coding: utf-8 -*-
"""
Russian. Keys are the English source exactly as built -- see tools/i18n.py.

SCOPE: THE CAREERS PAGE, AND ONLY THAT
This is a partial language -- see i18n.PAGES. The crews this company recruits
are reached through Russian-language channels and a job advert links straight
to /ru/careers; the other forty pages stay in the four languages the clients
read. So this table covers careers.html and the chrome around it, 163 units,
and nothing else. Add a page to i18n.PAGES and the build will tell you exactly
which strings are missing.

REGISTER
The reader is a welder, a fitter or a site supervisor deciding whether to send
his documents -- not a buyer. Trade Russian as it is actually spoken on Baltic
and Nordic sites, not a literal rendering of the English marketing register.

TERMINOLOGY, and why each one rather than the obvious alternative
    TIG (141)                -> аргонодуговая сварка (TIG)
                                "TIG" stays in brackets: it is what the
                                certificate says and what a welder searches for
    MIG/MAG (131/135)        -> полуавтоматическая сварка (MIG/MAG)
    MMA (111)                -> ручная дуговая сварка (MMA)
    flux-cored (136)         -> порошковой проволокой (136)
    pipe fitter              -> монтажник трубопроводов
                                not "трубопроводчик", which in Russian usage
                                leans to plumbing rather than industrial piping
    hull assembler           -> судосборщик
    fit-up                   -> сборка под сварку
    root run                 -> корневой проход
    tack welding             -> прихватка
    spool                    -> катушка (трубная катушка)
    isometric drawing        -> изометрическая схема
    non-destructive testing  -> неразрушающий контроль (НК)
    NDT VT / PT-MT / UT      -> ВИК / ПВК и МК / УЗК
                                the Russian abbreviations are what a certificate
                                issued in the region carries
    rope access              -> промышленный альпинизм
                                IRATA's own Russian-market term
    rigging                  -> такелажные работы
    site supervision         -> руководство работами на объекте
    rotation                 -> вахта, and "8 / 2" style ratios are left as they
                                are printed -- they are read, not translated
    scope (of work)          -> объём работ

LEFT UNTRANSLATED ON PURPOSE
Certification names, because they are the text printed on the document the
applicant holds and a translated version would not match anything he can show:
IRATA L1/L2/L3, GWO, VCA / SCC, EN ISO 9606, MIG/MAG 131/135. Company name,
company code, VAT number. "Offshore" is used as is in Russian industry.

THE CONSENT TEXT IS A LEGAL STATEMENT
The two strings that carry consent -- the application form's and the
newsletter's -- are drafted here, not authorised. They name a retention period,
a controller and a deletion route, and they are what the site relies on to say
the box was ticked against a specific wording. i18n.PUBLISH decides whether
this language ships; sign those two off before the link goes into a job advert.
"""

S = {
    # ---------------- chrome: navigation, footer, switcher ----------------
    'Home': 'Главная',
    'News': 'Новости',
    'Company': 'Компания',
    'About Us': 'О компании',
    'Services': 'Услуги',
    'Our Services': 'Наши услуги',
    'Projects': 'Проекты',
    'Careers': 'Вакансии',
    'Contacts': 'Контакты',
    'Privacy Policy': 'Политика конфиденциальности',
    'Book a call': 'Заказать звонок',
    'Main navigation': 'Основная навигация',
    'Mobile navigation': 'Мобильная навигация',
    'Open menu': 'Открыть меню',
    'Skip to content': 'Перейти к содержанию',
    'ALPROJECTS Group — home': 'ALPROJECTS Group — на главную',
    'Company Profile (PDF)': 'Профиль компании (PDF)',
    'LinkedIn': 'LinkedIn',
    'Facebook': 'Facebook',
    'Instagram': 'Instagram',
    'ALPROJECTS, UAB': 'ALPROJECTS, UAB',
    'Šilutės pl. 2, LT-92298<br>Klaipėda, Lithuania':
        'Šilutės pl. 2, LT-92298<br>Клайпеда, Литва',
    '<span class="txt">Home</span>': '<span class="txt">Главная</span>',
    '<span class="txt">News</span>': '<span class="txt">Новости</span>',
    '<span class="txt">Company</span>': '<span class="txt">Компания</span>',
    '<span class="txt">Services</span>': '<span class="txt">Услуги</span>',
    '<span class="txt">Projects</span>': '<span class="txt">Проекты</span>',
    '<span class="txt">Careers</span>': '<span class="txt">Вакансии</span>',
    '<span class="txt">Contacts</span>': '<span class="txt">Контакты</span>',

    # the drawing title block in the footer
    'Sheet': 'Лист',
    'No.': '№',
    'Rev': 'Изм.',
    'Scale': 'Масштаб',
    'Projection': 'Проекция',

    '<span>© 2019–2026 ALPROJECTS GROUP. All rights reserved.</span> <span class="legal-ids">Company code 305137109 &middot; VAT LT100012753216</span> <a class="made-by" href="https://aldystudio.com" target="_blank" rel="noopener">Made by <b>ALDY</b></a>':
        '<span>© 2019–2026 ALPROJECTS GROUP. Все права защищены.</span> <span class="legal-ids">Код предприятия 305137109 &middot; НДС LT100012753216</span> <a class="made-by" href="https://aldystudio.com" target="_blank" rel="noopener">Сделано <b>ALDY</b></a>',

    # ---------------- newsletter in the footer ----------------
    'Newsletter': 'Рассылка',
    'Subscribe': 'Подписаться',
    'Enter Your Email': 'Укажите e-mail',
    'Subscribe to receive company news and project updates.':
        'Подпишитесь на новости компании и отчёты о проектах.',
    'By subscribing you agree that ALPROJECTS, UAB will process your email address to send company news and project updates. You can unsubscribe at any time. See our <a href="/privacy">Privacy Policy</a>.':
        'Подписываясь, вы соглашаетесь, что ALPROJECTS, UAB будет обрабатывать ваш адрес электронной почты для отправки новостей компании и отчётов о проектах. Вы можете отписаться в любой момент. См. <a href="/privacy">Политику конфиденциальности</a>.',

    # ---------------- page head ----------------
    'Careers — ALPROJECTS Group': 'Вакансии — ALPROJECTS Group',
    'Work with ALPROJECTS': 'Работа в ALPROJECTS',
    'Work with ALPROJECTS Group — welding, pipe fitting, NDT, rope access and mechanical contracting on industrial and offshore projects across Europe.':
        'Работа в ALPROJECTS Group — сварка, монтаж трубопроводов, неразрушающий контроль, промышленный альпинизм и механомонтаж на промышленных и офшорных проектах по всей Европе.',
    'We deliver mechanical contracting, welding, inspection and rope access services on industrial and offshore projects across Europe. The work is technical, certified and mostly on site.':
        'Мы выполняем механомонтаж, сварку, контроль качества и работы методом промышленного альпинизма на промышленных и офшорных проектах по всей Европе. Работа техническая, сертифицированная и в основном на объекте.',

    # ---------------- the schedule of vacancies ----------------
    'Open positions': 'Открытые вакансии',
    'Role': 'Должность',
    'Location': 'Место работы',
    'Contract': 'Договор',
    'Project sites across Europe': 'Объекты по всей Европе',
    'Project-based': 'По проекту',
    'What we need': 'Что требуется',
    'Apply for this role': 'Откликнуться на вакансию',

    'Certified TIG Welder': 'Сварщик TIG с аттестацией',
    'Piping, root runs and stainless steel systems on shipyard and industrial projects. You weld to an approved procedure, and the fit-up is checked before you start.':
        'Трубопроводы, корневые проходы и системы из нержавеющей стали на судостроительных и промышленных объектах. Сварка по аттестованной технологии, сборка под сварку проверяется до начала работ.',
    'Valid TIG qualification with supporting documents':
        'Действующая аттестация по TIG с подтверждающими документами',
    'Experience with pipe welding and stainless steel':
        'Опыт сварки трубопроводов и нержавеющей стали',
    'Able to work from a welding procedure and an isometric drawing':
        'Умение работать по технологической карте сварки и изометрической схеме',
    'Ready to travel and work on site in several countries':
        'Готовность к разъездам и работе на объектах в нескольких странах',
    'Working English, B1 or better': 'Английский на рабочем уровне, B1 и выше',

    'MIG / MAG / MMA Welder': 'Сварщик MIG / MAG / MMA',
    'Structural steel, fill and capping passes, fabrication in the workshop and repair work on site. Plate, profiles and supports, mostly in shipyards and industrial plants.':
        'Металлоконструкции, заполняющие и облицовочные проходы, изготовление в цеху и ремонтные работы на объекте. Листовой металл, профиль и опоры, в основном на судозаводах и промышленных предприятиях.',
    'Valid qualification for MAG (135), flux-cored (136) or MMA (111)':
        'Действующая аттестация по MAG (135), сварке порошковой проволокой (136) или MMA (111)',
    'Experience with structural steel and plate work':
        'Опыт работы с металлоконструкциями и листовым металлом',
    'Able to read drawings and work to a procedure':
        'Умение читать чертежи и работать по технологической карте',
    'Tack welding and confident use of alignment tools':
        'Прихватка и уверенное владение инструментом для выставления',

    'Pipe Fitter': 'Монтажник трубопроводов',
    'Spool prefabrication on fitting tables, routing and installation of complete systems, fit-up and alignment before the welder arrives. We work from isometric drawings and 3D models.':
        'Изготовление трубных катушек на сборочных столах, трассировка и монтаж систем целиком, сборка под сварку и выставление до прихода сварщика. Работаем по изометрическим схемам и 3D-моделям.',
    'Experience with process, utility or engine room piping':
        'Опыт работы с технологическими, вспомогательными или машинно-отделенческими трубопроводами',
    'Able to work from isometrics and 3D models':
        'Умение работать по изометрическим схемам и 3D-моделям',
    'Fit-up, alignment and dimensional control before welding':
        'Сборка под сварку, выставление и контроль размеров до сварки',

    'Site Supervisor': 'Руководитель работ на объекте',
    'You run the crew on site. Planning the sequence, holding the schedule, keeping the safety rules and dealing with the client day to day. You report to our project manager, not to the shipyard.':
        'Вы руководите бригадой на объекте: планируете последовательность работ, держите график, следите за соблюдением правил безопасности и ежедневно работаете с заказчиком. Подчиняетесь нашему руководителю проекта, а не судозаводу.',
    'Experience leading welding, piping or mechanical crews on site':
        'Опыт руководства сварочными, трубопроводными или механомонтажными бригадами на объекте',
    'Able to plan the work sequence and report progress to the client':
        'Умение планировать последовательность работ и отчитываться заказчику о ходе',
    'Confident with safety rules and site documentation':
        'Уверенное знание правил безопасности и документации на объекте',
    'English at working level, German is an advantage':
        'Английский на рабочем уровне, немецкий будет преимуществом',

    'Hull Assembler': 'Судосборщик',
    'Assembly of hull sections and blocks in the shipyard. Setting plates and profiles, alignment, tack welding and preparing the joints for the welders, on newbuilds and on repair work.':
        'Сборка секций и блоков корпуса на судозаводе. Установка листов и профиля, выставление, прихватка и подготовка стыков под сварку — на новостроях и в ремонте.',
    'Experience with hull assembly on newbuilds or ship repair':
        'Опыт сборки корпуса на новостроях или в судоремонте',
    'Able to read shipbuilding drawings': 'Умение читать судостроительные чертежи',

    # ---------------- open application ----------------
    'Your trade is not on the list?': 'Вашей специальности нет в списке?',
    'We also take on NDT technicians, rope access teams and mechanical fitters between projects. Send your CV and certificates, and we will come back to you when a scope matches.':
        'Мы также берём специалистов по неразрушающему контролю, бригады промышленного альпинизма и слесарей-монтажников между проектами. Пришлите резюме и сертификаты — ответим, когда появится подходящий объём работ.',
    'We recruit regularly in these disciplines':
        'Мы регулярно набираем по этим специальностям',
    'Even when a role is not advertised we keep qualified specialists on file and make contact when a project matches. Select your discipline and it goes straight into the form below.':
        'Даже когда вакансия не опубликована, мы держим аттестованных специалистов в базе и связываемся, когда появляется подходящий проект. Выберите специальность — она подставится в форму ниже.',

    # ---------------- the application form ----------------
    'Apply': 'Отклик',
    'Send us your details': 'Пришлите свои данные',
    'Six fields are required. Everything else helps us match you faster, but the form will send without them.':
        'Шесть полей обязательны. Остальное помогает нам подобрать вам объект быстрее, но форма отправится и без них.',
    '<span class="step-n">01</span> Who you are': '<span class="step-n">01</span> Кто вы',
    '<span class="step-n">02</span> Your trade': '<span class="step-n">02</span> Специальность',
    '<span class="step-n">03</span> Availability': '<span class="step-n">03</span> Готовность',
    '<span class="step-n">04</span> Your documents': '<span class="step-n">04</span> Документы',

    'Full name': 'Имя и фамилия',
    'Name and surname': 'Имя и фамилия',
    'Email': 'E-mail',
    'Phone or WhatsApp': 'Телефон или WhatsApp',
    'Country of residence <span class="opt">(optional)</span>':
        'Страна проживания <span class="opt">(необязательно)</span>',
    'Discipline': 'Специальность',
    'Select': 'Выберите',
    'Select your discipline': 'Выберите специальность',
    'Not on the list? Add it in the notes field below.':
        'Нет в списке? Укажите в поле для примечаний ниже.',
    'Years of experience <span class="opt">(optional)</span>':
        'Стаж работы <span class="opt">(необязательно)</span>',
    'Less than 2 years': 'Менее 2 лет',
    '2 to 5 years': 'От 2 до 5 лет',
    '5 to 10 years': 'От 5 до 10 лет',
    'More than 10 years': 'Более 10 лет',
    'Available from': 'Готов с',
    'Preferred rotation <span class="opt">(optional)</span>':
        'Предпочтительная вахта <span class="opt">(необязательно)</span>',
    'Continuous': 'Без вахты, постоянно',
    'Local, no rotation': 'Местная работа, без вахты',
    'Countries you can work in <span class="opt">(optional)</span>':
        'Страны, где вы можете работать <span class="opt">(необязательно)</span>',
    'Norway': 'Норвегия',
    'Germany': 'Германия',
    'Netherlands': 'Нидерланды',
    'United Kingdom': 'Великобритания',
    'Belgium': 'Бельгия',
    'Denmark': 'Дания',
    'Poland': 'Польша',
    'Lithuania': 'Литва',
    'Other': 'Другая',
    'Certifications': 'Аттестации',
    'Certificates you hold <span class="opt">(optional, select all that apply)</span>':
        'Имеющиеся сертификаты <span class="opt">(необязательно, отметьте все подходящие)</span>',
    'Medical certificate': 'Медицинская справка',
    'Anything else <span class="opt">(optional)</span>':
        'Что-то ещё <span class="opt">(необязательно)</span>',
    'Certificate numbers and expiry dates, projects you have worked on, when you could start.':
        'Номера сертификатов и сроки действия, проекты, на которых вы работали, когда можете начать.',
    '<b>Attach your CV and certificates</b> <span>Choose files, or drag them here. PDF, JPG or PNG, up to 10 MB each.</span>':
        '<b>Приложите резюме и сертификаты</b> <span>Выберите файлы или перетащите их сюда. PDF, JPG или PNG, до 10 МБ каждый.</span>',
    'Photographs of certificates taken with a phone are fine.':
        'Фотографии сертификатов, снятые на телефон, подойдут.',
    'Send application': 'Отправить заявку',
    'We read every application and reply within three working days when a project matches your profile.':
        'Мы читаем каждую заявку и отвечаем в течение трёх рабочих дней, если есть проект под ваш профиль.',

    # The consent record. A legal statement -- see the note at the top of this
    # file. The retention period, the controller and the deletion route are the
    # three things that have to survive translation unchanged.
    'I agree that ALPROJECTS, UAB stores my details and documents for recruitment purposes for 24 months. I can ask for them to be deleted at any time by writing to info@alprojects.eu. See the <a href="/privacy">privacy policy</a>.':
        'Я согласен, что ALPROJECTS, UAB хранит мои данные и документы в целях подбора персонала в течение 24 месяцев. Я могу в любой момент потребовать их удаления, написав на info@alprojects.eu. См. <a href="/privacy">политику конфиденциальности</a>.',

    'Prefer not to fill in a form?': 'Не хотите заполнять форму?',
    'You can also send them to <a href="mailto:info@alprojects.eu?subject=CV%20and%20certificates">info@alprojects.eu</a> or by <a href="https://wa.me/37063663744" target="_blank" rel="noopener">WhatsApp</a>.':
        'Вы также можете прислать их на <a href="mailto:info@alprojects.eu?subject=CV%20and%20certificates">info@alprojects.eu</a> или через <a href="https://wa.me/37063663744" target="_blank" rel="noopener">WhatsApp</a>.',

    # ---------------- discipline list (shared with the form) ----------------
    'Welding (TIG)': 'Аргонодуговая сварка (TIG)',
    'Welding (MIG/MAG)': 'Полуавтоматическая сварка (MIG/MAG)',
    'Pipe fitting': 'Монтаж трубопроводов',
    'Instrument pipe fitting': 'Монтаж импульсных трубопроводов КИП',
    'Mechanical installation': 'Механомонтаж',
    'Shipbuilding': 'Судостроение',
    'Ship repair': 'Судоремонт',
    'NDT inspection': 'Неразрушающий контроль',
    'Rope access': 'Промышленный альпинизм',
    'Quality control (QA/QC)': 'Контроль качества (QA/QC)',
    'Rigging': 'Такелажные работы',
    'Site supervision': 'Руководство работами на объекте',

    # ---------------- certificate names: left as printed ----------------
    'EN ISO 9606 (welder)': 'EN ISO 9606 (сварщик)',
    'MIG/MAG 131/135': 'MIG/MAG 131/135',
    'IRATA L1': 'IRATA L1',
    'IRATA L2': 'IRATA L2',
    'IRATA L3': 'IRATA L3',
    'VCA / SCC': 'VCA / SCC',
    'NDT VT': 'ВИК',
    'NDT PT/MT': 'ПВК / МК',
    'NDT UT': 'УЗК',
    'GWO': 'GWO',

    # ---------------- service names in the footer ----------------
    'Welding Services': 'Сварочные работы',
    'Pipe Fitting': 'Монтаж трубопроводов',
    'Mechanical Contracting': 'Механомонтаж',
    'Heavy Equipment Relocation': 'Перемещение тяжёлого оборудования',
    'Mobile Repair Teams': 'Мобильные ремонтные бригады',
    'Ship Repair': 'Судоремонт',
    'Non-Destructive Testing': 'Неразрушающий контроль',
    'Rope Access Services': 'Промышленный альпинизм',
    '3D Laser Scanning': '3D-лазерное сканирование',
    'Rigging &amp; Technical Support': 'Такелаж и техническая поддержка',
}
