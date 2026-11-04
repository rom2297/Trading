from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('DV','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DVB','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
from reportlab.lib.fonts import addMapping
addMapping('DV',0,0,'DV');addMapping('DV',1,0,'DVB');addMapping('DV',0,1,'DV');addMapping('DV',1,1,'DVB')
B=ParagraphStyle('b',fontName='DV',fontSize=8.3,leading=10.6)
S=ParagraphStyle('s',parent=B,fontSize=7.2,leading=9)
H=ParagraphStyle('h',fontName='DVB',fontSize=10.5,leading=13,spaceBefore=5,spaceAfter=2,textColor=colors.HexColor('#1F3A5F'))
T=ParagraphStyle('t',fontName='DVB',fontSize=14,leading=17)
navy=colors.HexColor('#1F3A5F')
def P(t,st=B): return Paragraph(t,st)
def tbl(rows,widths,st=S):
    d=[[P(c,st) for c in r] for r in rows]
    t=Table(d,colWidths=widths,repeatRows=1)
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#DCE6F0')),('GRID',(0,0),(-1,-1),0.4,colors.grey),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2)]))
    return t
W=180*mm
st=[]
band=Table([[P('<b>Mode entraînement (à blanc)</b> — positions fictives jusqu\'au 30.11.2026',ParagraphStyle('x',parent=B,textColor=colors.white))]],colWidths=[W])
band.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),colors.HexColor('#C0392B')),('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3)]))
st+=[band,Spacer(1,4),P('Briefing marché — mercredi 4 novembre 2026',T),P('Préparé vers 13:00 CET. Cadre : 1 000 CHF, risque 10 CHF par position, actions/ETF uniquement, sans levier.',S),Spacer(1,4)]
v=Table([[P('<b>VERDICT DU JOUR : NE RIEN FAIRE.</b> Aucun achat avant le rapport sur l\'emploi US (vendredi 06.11, 14:30 CET). Les marchés bougent surtout sur deux événements « pile ou face » : l\'emploi US (qui décide de la hausse de taux de la Fed en décembre) et la guerre US-Iran (pétrole). Attendre est une bonne décision : aucun setup ne respecte le cadre avec des niveaux vérifiés.',B)]],colWidths=[W])
v.setStyle(TableStyle([('BOX',(0,0),(-1,-1),1.5,navy),('BACKGROUND',(0,0),(-1,-1),colors.HexColor('#EEF3F8')),('LEFTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
st+=[v]
st+=[P('Ce qui se passe',H),P('• Les démocrates ont remporté les élections de mi-mandat US ; les futures sur les indices US montent d\'environ 0,9 % ce matin.<br/>• Le pétrole reste cher (Brent ≈ 103 $) : le détroit d\'Ormuz est fermé et les USA ont frappé l\'île iranienne de Qeshm, mais des négociations via le Qatar continuent.<br/>• L\'inflation de la zone euro monte à 4,0 % (plus haut depuis 3 ans) : la BCE se rapproche d\'une hausse de taux en décembre.<br/>• Aux USA, ~70-85 % de chances d\'une hausse de taux de la Fed en décembre ; le taux à 10 ans est proche de 4,9 %.<br/>• En Suisse, le SMI a reculé de 0,4 % mardi (14 743 pts) ; le franc reste fort (1 USD ≈ 0,818 CHF).')]
st+=[P('News → impact sur les actions et ETF',H)]
rows=[['News (fait)','Secteurs / titres touchés','Sens (interprétation)','Certitude','Déjà dans les prix ?'],
['Victoire démocrate aux midterms (03.11)','Indices US larges (S&P 500, Nasdaq)','Hausse ce matin (futures +0,9 %)','Faible','En grande partie : réaction immédiate'],
['Inflation zone euro 4,0 %, sous-jacente 2,5 % (04.11)','Banques européennes (+), immobilier/utilities (−)','Hausse de taux BCE en déc. plus probable','Moyenne','Partiellement : hausse déjà attendue'],
['Fed : hausse en déc. pricée ~70-85 %, 10 ans ≈ 4,9 %','Tech/croissance US (−) si les taux montent encore','Pression si emploi fort vendredi','Moyenne','Oui en partie ; le 5 % sur le 10 ans est un seuil surveillé'],
['Frappes US sur Qeshm + diplomatie Qatar (02-03.11)','Pétrolières (Shell, TotalEnergies) ; compagnies aériennes (−)','Deal = pétrole en baisse ; escalade = hausse','Faible','Non : événement binaire, gros écarts possibles'],
['Résultats AMD (> attentes, +5 % après Bourse)','Semi-conducteurs (AMD, secteur puces IA)','Positif court terme','Moyenne','Oui : le saut a déjà eu lieu'],
['Franc fort (USD/CHF ≈ 0,818)','Actions US achetées en CHF ; exportateurs suisses','Risque de change sur les titres US','Moyenne','Oui']]
st+=[tbl(rows,[44*mm,38*mm,36*mm,17*mm,45*mm])]
st+=[P('Scénarios',H)]
rows=[['Titre','Déclencheur','Stop','Objectif','R/R','Nb actions / montant','Annulation'],
['<b>Aucun scénario valide aujourd\'hui</b>','—','—','—','—','—','Raison : risque binaire (NFP vendredi, Iran) et aucun niveau de prix daté et vérifié pour un titre éligible. Prochain réexamen : lundi 09.11, après les NFP.']]
st+=[tbl(rows,[30*mm,18*mm,14*mm,16*mm,12*mm,26*mm,64*mm])]
st+=[Spacer(1,3),P('<b>Exercice à blanc proposé :</b> sur le compte démo XTB, choisis une grande capitalisation (ex. ABB, qui a monté de 1,6 % mardi). Note son plus haut et son plus bas de la semaine sur le graphique journalier. Après les NFP, refais le calcul : nombre d\'actions = 10 CHF ÷ (prix d\'achat − stop). Si l\'objectif n\'est pas au moins 2 fois plus loin que le stop, on rejette.',S)]
st+=[P('Suivi des positions fictives',H),P('Aucune position ouverte (doc de cadre du 04.11.2026). Rien à suivre.')]
st+=[P('Apprendre en 2 minutes : « déjà dans les prix »',H),
P('La Bourse réagit à la <b>surprise</b>, pas à la nouvelle elle-même. Si tout le monde attend une hausse de taux de la Fed à 85 %, son annonce fera peu bouger les cours : elle est « déjà dans les prix ». C\'est l\'écart entre l\'attendu et le réel qui compte. Ainsi, vendredi, un bon chiffre de l\'emploi peut faire <b>baisser</b> les actions (s\'il renforce la hausse des taux).<br/><b>Analogie crypto :</b> « buy the rumor, sell the news ». En janvier 2024, l\'approbation des ETF Bitcoin était attendue par tous ; le BTC a d\'abord baissé juste après l\'annonce.<br/><b>À retenir :</b> avant d\'acheter sur une news, demande-toi « est-ce que les autres le savaient déjà ? ».')]
st+=[P('Agenda à risque (heures CET ; les USA sont passés à l\'heure d\'hiver le 01.11 : écart de 6 h avec New York)',H)]
rows=[['Date / heure CET','Événement','Pourquoi c\'est important'],
['Mer. 04.11, 14:15','Emploi privé ADP (US)','Avant-goût des NFP'],
['Mer. 04.11, 16:00','ISM services (US)','Croissance et prix dans les services'],
['Mer. 04.11, 16:30','Stocks de pétrole EIA','Mouvements sur les pétrolières'],
['Mer. 04.11, après la clôture US','Résultats Qualcomm, Uber, ARM, McDonald\'s','Gros titres US, effet secteur'],
['<b>Ven. 06.11, 14:30</b>','<b>Emploi US (NFP)</b>','<b>Décide en partie de la hausse Fed de décembre</b>'],
['Week-end 07-08.11','Risque Iran / Ormuz','Écart de cours possible à l\'ouverture de lundi'],
['Mar. 10.11, 14:30','Inflation US (CPI)','Deuxième grand test pour la Fed'],
['Mer. 11.11','Veterans Day (US)','Bourse US ouverte, marché obligataire fermé'],
['Ven. 13.11, 14:30','Prix à la production US (PPI)','Inflation en amont'],
['09.12 · 10.12, 09:30','Fed (décision) · BNS','Prochaines décisions de taux']]
st+=[tbl(rows,[38*mm,55*mm,87*mm])]
st+=[P('Sources (consultées le 04.11.2026)',H)]
src=[('TipRanks, Stock Market Today, 04.11.2026','https://www.tipranks.com/news/stock-market-today-nov-4-futures-rise-after-democrats-sweep-midterm-elections'),
('TraderFactor, Dollar Slips… JOLTS, ADP & ISM, 04.11.2026','https://traderfactor.com/dollar-slips-as-election-results-strong-jolts-take-focus/'),
('ING Think, Eurozone inflation brings ECB closer to December hike, 04.11.2026','https://think.ing.com/snaps/eurozone-inflation-brings-ecb-closer-to-december-rate-hike/'),
('Al Jazeera, US hits Qeshm Island… Iran war latest, 03.11.2026','https://www.aljazeera.com/news/2026/11/3/us-hits-qeshm-island-pezeshkian-signals-more-diplomacy-iran-war-latest'),
('ad-hoc-news, SMI closes 0.40 percent lower at 14,743.09, 03.11.2026','https://www.ad-hoc-news.de/boerse/news/marktberichte/smi-closes-0-40-percent-lower-at-14-743-09-points-before-us-midterm-vote/70452405'),
('Rio Times, Global economy briefing, 02.11.2026','https://www.riotimesonline.com/global-economy-briefing-november-2-2026'),
('LiteFinance, Weekly economic calendar 09-15.11.2026','https://litefinance.org/blog/analysts-opinions/weekly-economic-calendar-for-09112026-15112026'),
('FinanceCalendar, SNB Rate Decision December 2026','https://www.financecalendar.com/event/snb-rate-decision-december-2026/')]
for n,u in src: st.append(P(f'• {n} : <link href="{u}" color="blue">{u}</link>',S))
st+=[Spacer(1,3),P('Fait = chiffres sourcés ci-dessus. Interprétation = colonnes « sens », « certitude », « déjà dans les prix ». Chiffres de marché approximatifs, ils évoluent en séance.',S)]
def foot(c,d):
    c.saveState();c.setFont('DV',7.5);c.setFillColor(colors.grey)
    c.drawString(15*mm,9*mm,'Scénarios conditionnels, pas un conseil financier.');c.drawRightString(195*mm,9*mm,f'Page {d.page}');c.restoreState()
doc=SimpleDocTemplate('/home/claude/out/Briefing_marche_2026-11-04.pdf',pagesize=A4,leftMargin=15*mm,rightMargin=15*mm,topMargin=12*mm,bottomMargin=15*mm)
doc.build(st,onFirstPage=foot,onLaterPages=foot)
