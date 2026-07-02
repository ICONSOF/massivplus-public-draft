---
layout: default_banner
title: "Koordinatbytet"
parent: "Fördjupningar"
nav_order: 8
---

# Koordinatbytet: MASSIV+ följer affären, inte flödet

> **Poäng:** Den grundläggande skillnaden mellan MASSIV+ och livscykeltraditionen ligger i en enda punkt: vad ett utsläpp knyts till när det bokförs. Livscykelanalys (LCA) knyter det till materialets fysiska väg genom en produkts livscykel; MASSIV+ knyter det till affärsrelationen mellan köpare och säljare. Det är ett byte av grundkoordinat - inte en bättre eller sämre LCA, och inte en skillnad i vilken sorts påstående metoden gör (attributionell LCA och MASSIV+ beskriver båda vad som hänt).

Den här texten kan läsas fristående. Den förutsätter en grundläggande bild av hur MASSIV+ fungerar - läs [introduktionen](../introduktion.md) först om du inte är bekant med ramverket. För hur MASSIV+ förhåller sig till de enskilda produktstandarderna, se [produktstandarder](../positionering/jamforelse/produktstandarder.md); för den ytliga likheten med processbaserad LCA, se [MASSIV+ vs processbaserad LCA](../positionering/massiv-vs-ecoinvent.md).

---

## 1. Tre sätt att avgöra vart ett utsläpp hör

All utsläppsredovisning måste svara på en riktningsfråga: när ett utsläpp uppstår, vart hör det - i vems bok ska det hamna?

Ta en lastbil som förbränner diesel för att leverera stål. Utsläppet är ett och detsamma, men det finns tre olika sätt att avgöra vart det hör: till *materialet* och dess fysiska väg genom tillverkningen, till den *organisation* som äger lastbilen, eller till den *affär* där någon köpte transporten. Vilken av dessa man utgår från är det vi kallar en **koordinat** - grundregeln som bestämmer i vilken riktning ett utsläpp bokförs. Bilden är densamma som på en karta: samma punkt kan anges i olika koordinatsystem, och på samma sätt kan samma utsläpp knytas till olika saker beroende på vilken koordinat man valt.

Tre koordinater används i praktiken:

| Koordinat | Riktningen ges av | Exempel |
|---|---|---|
| **Fysiskt flöde** | Materialets eller energins fysiska väg genom produktions- och konsumtionssystemet | Produkt-LCA (ISO 14040/44, ISO 14067), EPD, PACT/Pathfinder, Catena-X |
| **Ägande / kontroll** | Vilken juridisk enhet som äger eller styr aktiviteten | GHG Protocol scope-gräns, organisatorisk LCA |
| **Affärsrelation** | Vem som är kund respektive leverantör (avtalet, betalningen) | MASSIV+ |

De två första koordinaterna sammanfaller ofta i praktiken, och båda är flödesförankrade i meningen att de utgår från den fysiska aktiviteten och följer den. Den tredje utgår från något annat: den affär som faktiskt inträffade mellan två organisationer. MASSIV+ gör affärsrelationen till *primär* riktningsdefinition, och är såvitt känt ensam om det bland de organisationsnära ramverken.

---

## 2. Brottet är koordinaten, inte hållningen

Både LCA och MASSIV+ beskriver vad som hänt; ingen av dem förutsäger. En vanlig kontrast säger annat - att LCA handlar om orsak och verkan (kausal) eller om framtiden (prognostisk), medan MASSIV+ bara är deskriptivt - men den håller inte. Den vanligaste formen av LCA, den attributionella - som fördelar ut ett systems befintliga utsläpp på det som produceras - är själv beskrivande: den redovisar de miljöeffekter som kan *tillskrivas* ett system över dess livscykel, och LCA-litteraturen kallar den uttryckligen för "accounting", "book-keeping" och "descriptive". Det är samma bokföringshållning som MASSIV+ bygger på.

Skillnaden ligger i stället i vad boken indexeras mot:

> Brottet går genom det utsläppet knyts till: den funktionella enheten (den bestämda produktmängd allt räknas per) i LCA, affärsrelationen i MASSIV+. Sättet att veta delar de två: båda beskriver vad som hänt, ingen påstår orsak eller framtid.

Attributionell LCA tillskriver längs leveranskedjan plus användning och slutskede - alltså längs den fysiska livscykeln. Även när logiken är bokföring förs den bokföringen i en flödes- och produktkoordinat. MASSIV+ för samma typ av deskriptiv bokföring, men i en relationskoordinat: affären mellan två parter. Det är där brottet ligger - i koordinaten, inte i hållningen.

---

## 3. Varför livscykelansatsen inte kan lägga affären som primär riktning

Livscykelanalysens bärande enhet är den funktionella enheten - den bestämda mängd produkt eller tjänst som allt räknas per, till exempel 1 kg stål eller 1 kWh el. Systemgränsen dras kring produktens väg från vagga till grav (eller vagga till grind, alltså fram till fabriksporten), och allt som beräknas hänger på den vägen - oavsett vilka juridiska personer eller affärer den passerar. Det är inbyggt: PACT/Pathfinder definierar till exempel sina livscykelsteg (materialanskaffning, produktion, distribution) och räknar per deklarerad enhet i kg CO₂e. Riktningen är materialets.

Konsekvensen är att en LCA-ansats inte kan lägga affärsrelationen som grundkoordinat utan att upphöra att vara LCA. Den har redan bundit sig vid flödesriktningen. Koordinatbytet blir därför strukturellt nödvändigt så snart noden - den organisatoriska enheten - görs till bärare i stället för produkten: en organisation har kunder och leverantörer som sin naturliga topologi, en funktionell enhet har det inte.

---

## 4. Vad som gör koordinatbytet möjligt

Mekanismen som möjliggör affärskoordinaten är MASSIV+:s grundarkitektur: varje nod beräknar sitt eget Scope 1+2 och skickar det vidare (propagerar det) till sina kunder enligt principen *"ditt Scope 1+2 är mitt Scope 3"*. Eftersom varje nod är självständigt ansvarig för sin egen direktmätning behöver systemet aldrig spåra ett fysiskt flöde genom hela kedjan för att veta var ett utsläpp hör hemma. Det räcker att varje nod känner sina egna affärsrelationer.

I en klassisk livscykelansats är hela poängen den motsatta: att följa materialet eller energin genom dess livscykel för att bygga upp det kumulativa avtrycket. Där måste flödeskedjan rekonstrueras. I MASSIV+ är kedjan emergent ur lokala affärsrelationer snarare än något som måste spåras centralt - vilket också är skälet till att ingen central överblick över hela nätverket krävs.

---

## 5. De två ställen där relationen redan tränger in i LCA-traditionen

Livscykeltraditionen är inte helt stängd mot relationella objekt. Den släpper in dem på två ställen. Att pröva tesen mot dessa två gränsfall gör den skarpare snarare än svagare, eftersom den står kvar även efter prövningen.

**Konsekventiell LCA med kontraktsvillkor.** Konsekventiell LCA är den form som i stället modellerar vad ett beslut leder till på marknaden - vilka utsläpp som tillkommer eller uteblir om efterfrågan ändras. Vissa forskare begränsar den marknadsmodellen genom att uttryckligen beakta befintliga leveranskontrakt och planerade framtida leverantörer. Det är relationella objekt inne i LCA-traditionen själv. Skillnaden är att konsekventiell LCA gör det prognostiskt och hypotetiskt - en generisk marginalkedja (den produktion på marknaden som en ökad efterfrågan antas dra in) - medan MASSIV+ gör det deskriptivt och faktiskt: den affär som inträffade.

**Avfallsbehandling via marknadsvärdet.** LCA-metodiken löser negativt marknadsvärde (en gate fee för avfall) genom att låta alla behandlingssteg fram till dess att avfallet når nollmarknadsvärde tillhöra det system som genererade avfallet, eftersom ett avfall i sig inte kan bära någon behandlingsbörda. Här används marknadsvärdet - priset, nollvärdesgränsen - som operativ skiljelinje för var ansvaret går från generator till behandlare. Det är alltså en transaktions- och värdekoordinat som avgör riktningen, inte en ren fysisk-flödeskoordinat. MASSIV+ når samma slutsats men gör värdekoordinaten primär och generell i stället för ett specialfall som bara aktiveras när en process ger flera produkter samtidigt (multifunktionalitet). (Se [avfallsförbränning och allokering](avfallsforbranning-och-allokering.md).)

MASSIV+ är därför distinkt på ett precist och avgränsat sätt: genom att kombinera en attributionell, deskriptiv hållning med en relationskoordinat, och genom att göra värde- och relationskoordinaten generell i stället för en undantagsregel. Relationen är alltså en bärande princip i MASSIV+, medan den i LCA-traditionen förblir ett undantag. Traditionen hanterar dessa fall redan; skillnaden ligger i om relationen är regel eller undantag.

---

## 6. Organisatorisk LCA - det skenbara motexemplet

Den närmast till hands liggande invändningen är att organisationsnivå-LCA redan finns. UNEP/SETAC:s *Guidance on Organizational Life Cycle Assessment* (2015, som vilar på ISO/TS 14072) analyserar hela organisationen i stället för en enskild produkt.

Det avgörande är att organisatorisk LCA (O-LCA) bytte *aggregeringsnivå* - vilken nivå data slås ihop på, från enskild produkt till hel organisation - men inte *koordinatsystem*. Den inkluderar uttryckligen inte bara organisationens egna anläggningar utan också uppströms- och nedströmsaktiviteter - alltså livscykelansatsen behållen. Riktningen ges fortfarande av aktivitetens väg genom värdekedjan, och gränsen mellan direkt och indirekt dras på ägande och kontroll. I praktiken körs O-LCA som en uppskalad produkt-LCA med systemgräns vagga till grind.

Slutsatsen stärker tesen: man har redan provat att flytta LCA till organisationsnivå, och flödeskoordinatens allokeringsproblematik kvarstår, eftersom riktningen fortfarande ges av aktivitetens plats i flödet. Att aggregeringsnivån i sig inte löste det visar att källan var koordinaten, inte nivån.

---

## 7. E-liability - det seriösa gränsfallet

Ett ramverk ärver inte självklart flödeskoordinaten och förtjänar därför särskild behandling: E-liability (en föreslagen redovisningsmetod där varje företag bär ett utsläpps-skuldsaldo som förs över vid varje köp) och E-ledgers (Kaplan & Ramanna). Det är transaktionsbaserat och överför utsläpp vid varje motpartstransaktion, påfallande likt MASSIV+:s propagering. E-liability är alltså inte ett rent livscykelarv.

Skillnaden ligger i en annan dimension. E-liability spårar *produkter* (vagga till grind per vara). Eftersom utsläppen måste fördelas (allokeras) ner på varje såld produktenhet kommer det fysiska orsakssambandet in bakvägen just i det fördelningssteget. MASSIV+:s organisationsnivå undviker det: frågan är aldrig "vilken produkt orsakade vilket utsläpp", bara "vilka är nodens kunder". Skillnaden mot E-liability är alltså inte flöde mot affär i samma renhet som mot LCA, utan produkt mot organisation - och det är produktnivån som drar tillbaka in ett flödesliknande allokeringssteg. Tesen överlever därmed mötet med sitt starkaste gränsfall. (Hur MASSIV+ ändå når produktupplösning där den behövs behandlas i [produktnivå-invändningen](produktniva-invandningen.md).)

---

## 8. Vad koordinatbytet eliminerar - och vad det inte gör

Flödeskoordinaten drar med sig en klass av problem som affärskoordinaten formulerar bort:

- **Allokering vid samproduktion och avfall.** I flödeskoordinaten kräver fall där material och affär divergerar särskilda undantagsregler. I affärskoordinaten faller riktningen ut direkt ur vem som köpte behandlingen.
- **Krav på att rekonstruera kedjan.** Flödesansatser kräver spårning av materialet genom livscykeln; affärskoordinaten kräver bara lokal kännedom om egna kunder och leverantörer.
- **Funktionell enhet som tvång.** LCA binder allt till en funktionell eller deklarerad enhet; noden behöver ingen sådan, vilket gör tidig adoption möjlig utan fullständig produktspårbarhet.

Koordinatbytet löser dock inte allt. MASSIV+ ärver inte flödesproblematiken, men har sina egna öppna frågor: val av allokeringsnyckel när en nod har flera kunder, nodgranularitet och jämförbarhet, samt cirkulära flöden. Brottet eliminerar en klass av problem (riktning och flöde) men upphäver inte fördelningsfrågan i sig. Dessa öppna frågor behandlas i [metodologiska risker](metodologiska-risker.md).

---

## 9. Kärnformulering

> Livscykelanalysen följer materialet; MASSIV+ följer affären. Det är ett byte av grundkoordinat, inte en förbättrad LCA. Att organisatorisk LCA redan finns - och ändå bär samma allokeringsproblematik - visar att det var flödeskoordinaten, inte aggregeringsnivån, som bar problemet.

---

## Referenser

- ISO 14040:2006 och ISO 14044:2006, *Environmental management - Life cycle assessment - Principles and framework / Requirements and guidelines* (med ändringar 2020). De normativa grundstandarderna för LCA.
- S. Hellweg & L. Milà i Canals, "Emerging approaches, challenges and opportunities in life cycle assessment", *Science* 344 (2014), 1109-1113.
- UNEP/SETAC Life Cycle Initiative, *Guidance on Organizational Life Cycle Assessment* (2015).
- J. Martínez-Blanco, A. Inaba & M. Finkbeiner, "Organizational LCA: the new member of the LCA family", *Int. J. LCA* (2015).
- WBCSD, *PACT/Pathfinder Framework* - livscykelsteg och deklarerad enhet.
- R. Kaplan & K. Ramanna m.fl., *A Proto-Standard for Carbon Accounting and Auditing using the E-Liability Method* (2025), samt E-ledgers Institute.
