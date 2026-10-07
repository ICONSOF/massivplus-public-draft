---
layout: default_banner
title: "Återvinning och cirkulära materialflöden"
parent: "Fördjupningar"
nav_order: 12
---

# Återvinning och cirkulära materialflöden

> **Syfte:** Att visa hur MASSIV+ hanterar material som går tillbaka in i produktionen: skrot som köps tillbaka från kunder, restströmmar som säljs vidare och material som lämnas in för återvinning. Texten visar att en materialloop i MASSIV+ är en följd av vanliga affärer, att det är säljarens allokeringsnyckel och priset på materialet som avgör hur utsläppen fördelas, och hur det förhåller sig till GHG Protocol och till LCA-praxis. Den redovisar också vilka delar som ännu är öppna.

Den här texten kan läsas fristående. Den förutsätter en grundläggande bild av hur MASSIV+ fungerar - läs [introduktionen](../introduktion.md) eller [specifikationen](../standard/specifikation.md) först om du inte är bekant med ramverket.

---

## 1. Två betydelser av cirkulär

Ordet cirkulär används om två olika saker när det gäller MASSIV+.

Den första är beräkningsmässig. Två noder säljer till varandra, så att den enas utsläppsvärde beror på den andras och tvärtom. Räknar man en nod i taget går det inte att veta var man ska börja: A kan inte räknas klart förrän B är klar, och B inte förrän A är klar. [Specifikationens avsnitt 7](../standard/specifikation.md#7-cirkulära-flöden) tillåter två lösningar. Den ena är att räkna ut värdena för alla noder i loopen samtidigt. Med två noder är det samma sak som att lösa två ekvationer med två okända, och med fler noder blir det ett större ekvationssystem av samma slag. Specifikationen kallar det matrisinversion, och tekniken används sedan länge i LCA-verktyg. Den andra lösningen är att bryta loopen genom att använda den andra nodens värde från föregående rapporteringsperiod. Valet mellan dem lämnas till verktyget, och användaren behöver inte göra något.

Den andra är cirkulär ekonomi: skrot, återvunnet material och sekundärråvara som går tillbaka in i ny produktion. Det är den betydelsen den här texten handlar om.

De två hänger ihop. När en tillverkare köper tillbaka skrot från samma kunder som den säljer till uppstår exakt det ömsesidiga leveransförhållande som avsnitt 7 hanterar. Cirkulär ekonomi ger alltså upphov till beräkningsmässig cirkularitet, och den delen är redan löst. Det som återstår är frågan om hur utsläppen ska fördelas längs loopen.

## 2. Skrotloopen steg för steg

Ta ett verktygsbolag som säljer skärverktyg till en mekanisk verkstad och köper tillbaka de förbrukade verktygen och spånen som skrot. Mönstret är detsamma för stålskrot till en ljusbågsugn, aluminiumskrot till ett omsmältningsverk eller plastspill som säljs tillbaka till en råvaruleverantör.

Steg ett: verktygsbolaget levererar verktyg och allokerar en andel av sin totala utsläppsmassa T till verkstaden med sin dokumenterade nyckel. Andelen hamnar i verkstadens uppströmsvärde.

Steg två: verkstaden säljer skrotet till verktygsbolaget. I den affären är verkstaden leverantör. Den allokerar en andel av sin egen T, där verktygsbolagets tidigare allokering ingår, till verktygsbolaget med sin nyckel.

Steg tre: verktygsbolaget smälter om skrotet eller återvinner det kemiskt. Det återvunna materialet bär den andel som verkstaden allokerat plus verktygsbolagets egna Scope 1 och 2 för återvinningsprocessen. Om återvinningen kräver mindre energi än primär produktion får det återvunna materialet en lägre siffra, eftersom de uppmätta utsläppen är lägre. Ingen kredit behöver läggas på för att det ska synas.

## 3. Säljarens nyckel avgör hur mycket skrotet bär

Steg två är det ISO 14044 kallar allokering vid öppen loop (avsnitt 4.3.4.3): ett material lämnar ett produktsystem och används i ett annat, och frågan är hur bördan ska delas mellan dem. LCA-praxis har två huvudsvar. Med cut-off bär det återvunna materialet ingen börda från sitt tidigare liv, bara återvinningsprocessen. Med undviken börda (avoided burden) får den som skickar material till återvinning en kredit för den primärproduktion materialet antas ersätta.

MASSIV+ föreskriver inget av dem. Skrotet är ett av säljarens utflöden, och säljaren fördelar sin utsläppsmassa över utflödena med den nyckel den valt för hela noden ([specifikationen, avsnitt 3](../standard/specifikation.md#3-allokering---att-fördela-utsläpp-till-mottagare)). Nyckeln gör arbetet, och valet av nyckel får stor betydelse.

> Verkstaden har under perioden en total utsläppsmassa på 1 000 ton CO₂e. Den säljer bearbetade detaljer för 99 miljoner kronor och skrot för 1 miljon. Detaljerna väger 400 ton och skrotet 100 ton.
>
> Med monetär nyckel bär skrotet 1 procent av utsläppsmassan, 10 ton. Med massbaserad nyckel bär det 20 procent, 200 ton.
>
> Verktygsbolagets omsmältning av de 100 tonnen ger 30 ton i egna Scope 1 och 2 (illustrativt). Det återvunna materialet bär alltså 40 ton med monetär nyckel hos verkstaden och 230 ton med massbaserad nyckel. I båda fallen sjunker verkstadens övriga kunders andel med lika mycket som skrotet tar på sig, så summan är densamma.

Med monetär nyckel hamnar MASSIV+ nära cut-off: skrotet bär en liten börda eftersom det har ett lågt värde i förhållande till säljarens övriga försäljning. Med massbaserad nyckel flyttas en stor del av verkstadens fabriksutsläpp till den som köper skrotet, trots att skrotet är en restprodukt med lågt värde. Det kan vara ett skäl för vägledning att peka på monetär nyckel för noder med stora restströmmar av lågt värde, utan att göra den normativ. ISO 14044 nämner fysiska egenskaper före ekonomiskt värde som grund för allokering vid återvinning, så en sådan vägledning skulle avvika från ISO-standardens ordning och behöver motiveras.

## 4. Priset avgör riktningen

I MASSIV+ bestäms riktningen av vem som betalar, inte av vart materialet rör sig. Den som betalar är kund, den som får betalt är leverantör, och utsläppsdata går från leverantör till kund. Samma regel ger tre fall för material som går till återvinning.

Positivt pris. Den som lämnar materialet får betalt och är leverantör. Utsläppen går med materialet till återvinnaren, som i avsnitt 2. Det är det vanliga fallet för metallskrot.

Negativt pris. Den som lämnar materialet betalar för att bli av med det. Återvinnaren säljer då en behandlingstjänst, och riktningen vänds: återvinnaren är leverantör, den som lämnar materialet är kund, och behandlingens utsläpp allokeras till den som lämnade materialet. Det är samma resonemang som för [avfallsförbränning](avfallsforbranning-och-allokering.md). Återvinnaren har då två utflöden, behandlingstjänsten och den sekundärråvara den säljer vidare, och fördelar sin utsläppsmassa mellan dem med sin nyckel. Material som pendlar mellan positivt och negativt pris med marknaden byter alltså riktning med priset.

Pris noll. Ingen betalning sker, och därmed saknas den affärsrelation som MASSIV+ bygger på. Standarden har redan listat detta som ett öppet gränsfall, vederlagsfria strömmar (se [metodologiska risker](metodologiska-risker.md#koordinatens-gränsfall)). Ett förslag är att en leverantörsrelation finns så snart det finns ett dokumenterat överlämningsavtal, oavsett pris, med den som lämnar materialet som leverantör. Hur stor börda flödet bär avgörs då av leverantörens nyckel. Med monetär nyckel bär ett flöde till priset noll ingenting, vilket sammanfaller med cut-off. Med massbaserad nyckel bär det börda i proportion till vikten. Förslaget bör prövas i pilot innan det skrivs in i specifikationen.

## 5. Material från privatpersoner

När en privatperson lämnar in en uttjänt produkt till återvinning kommer materialet från någon som inte är en nod. Specifikationen behandlar en privatkonsument som en sänka: när produkten såldes till konsumenten terminerade kedjan, och den ackumulerade bördan löstes upp på produkten i det ledet ([specifikationen, avsnitt 5](../standard/specifikation.md#från-affärsrelation-b2b-till-produktinformation-b2c)). Ett hushåll har inget eget Scope 1 och 2 att allokera.

Materialet går därför in i kedjan igen utan börda från sitt tidigare liv och bär bara insamlarens och återvinnarens egna utsläpp. Det följer av hur sänkan är definierad, men står inte uttryckligen i specifikationen och bör skrivas ut där.

Skillnaden mot skrot från ett företag är att ett företag som inte är nod ändå har utsläpp som kan allokeras. Skrot från en sådan leverantör bokförs därför som okänt uppströmsvärde, U, kvantifierat med bästa tillgängliga metod, exempelvis spend eller vikt, och konverteras till faktiskt värde, A, när leverantören börjar rapportera.

## 6. Vad MASSIV+ visar, och vad som hör hemma i andra instrument

MASSIV+ visar de utsläpp som faktiskt uppstått under perioden, fördelade per affärsrelation. För cirkulära flöden får det fyra följder.

Varje period står för sig. Skrot som säljs i år bär säljarens andel av årets utsläppsmassa. Utsläppen från när verktyget en gång tillverkades följer inte med, eftersom de redan har bokförts och allokerats i den period de uppstod.

Siffrorna innehåller bara bokförda utsläpp. Återvinning ger ingen kredit, och det finns ingen motsvarighet till modul D i EN 15804, där EPD:er redovisar nyttan av återvinning bortom produktens systemgräns, eller till de krediter som EU:s miljöavtrycksmetod PEF fördelar med sin Circular Footprint Formula. Det är samma hållning som standarden har till klimatkompensation (se [köpt energi och Scope 2](kompensation-och-faktiska-floden.md)), och den sammanfaller med GHG Protocol (avsnitt 7).

Incitamentet finns ändå, och på båda sidor. Den som köper återvunnet material får ett lågt uppströmsvärde när återvinningen kräver mindre energi än primär produktion. Den som säljer skrot flyttar en del av sin utsläppsmassa från sina huvudprodukter till skrotköparen, så att säljarens övriga kunder ser en något lägre siffra. Båda effekterna är verkliga och går att spåra till en affär.

Återvinningsbarhet som produktegenskap ligger utanför. Att en produkt kan återvinnas till en viss andel är en uppgift för ett digitalt produktpass eller en EPD. MASSIV+ ser återvinningen när affären faktiskt äger rum.

En praktisk konsekvens gäller återköpsprogram. Skrot som köps från många små verkstäder som inte är noder bokförs som U. Ett återköpsprogram som växer snabbt kan därför sänka köparens Coverage, andelen faktisk data, tills skrotleverantörerna ansluter. Det är samma mekanism som för vilken leverantör som helst som inte rapporterar, och siffran blir bättre när leverantörerna ansluter och replacement rule ersätter U med A.

## 7. Jämförelse med GHG Protocol

GHG Protocols Scope 3-standard har en egen regel för återvinning (box 5.6 i Corporate Value Chain Standard). Utsläppen från själva återvinningsprocessen redovisas av den som köper det återvunna materialet, i kategori 1 eller 2. Den som skickar material till återvinning redovisar i kategori 5 bara utsläppen från att samla in och ta tillvara materialet, inte från återvinningen. Undvikna utsläpp får inte dras av från inventeringen men får redovisas separat.

MASSIV+ landar på samma ställe i två av tre avseenden och avviker i det tredje.

| | GHG Protocol (box 5.6) | MASSIV+ |
|---|---|---|
| Återvinningsprocessens utsläpp | Hos köparen av återvunnet material | Hos återvinnaren, allokerat till köparen av återvunnet material |
| Kredit för undviken primärproduktion | Ingen i inventeringen, får redovisas separat | Ingen |
| Insamling och transport till återvinning | Alltid hos den som skickar materialet | Följer priset: hos den som lämnar materialet vid negativt pris, hos köparen av det återvunna materialet vid positivt pris |
| Börda från säljarens övriga verksamhet | Ingen, skrotet är fritt | Den andel säljarens nyckel ger, liten med monetär nyckel |

Avvikelsen följer av att MASSIV+ låter affären ge riktningen. GHG Protocol lägger insamlingen hos den som skickar materialet oavsett pris. I MASSIV+ beror det på vem som betalar vem: får den som lämnar materialet betalt är insamlaren en leverantör till nästa led, och dess utsläpp följer materialet nedströms. Det är samma logik som gör att MASSIV+ inte behöver någon särskild undantagsregel för avfallsförbränning.

## 8. Vad som är avgjort och vad som är öppet

Följande följer direkt av standarden som den står:

- En materialloop är en följd av vanliga affärer, och loopar mellan samma parter löses på verktygsnivå.
- Säljarens nyckel avgör hur stor börda skrotet bär, och nyckeln gäller hela noden.
- Priset avgör riktningen, och negativt pris ger samma behandling som avfallsförbränning.
- Återvinning ger ingen kredit i de propagerade siffrorna.

Följande är öppet eller föreslaget:

- Vederlagsfria strömmar. Förslaget att ett dokumenterat överlämningsavtal räcker för en leverantörsrelation bör prövas i pilot.
- Material från privatpersoner. Att det går in utan börda följer av sänkdefinitionen men behöver skrivas ut i specifikationen.
- Nyckeln för restströmmar. Om vägledningen ska peka på monetär nyckel, och hur det motiveras mot ISO 14044:s ordning, är inte avgjort. En närliggande fråga är om noder med stora restströmmar ska kunna partitionera sig så att restströmmen får en egen nyckel.

---

## Källor

- GHG Protocol, *Corporate Value Chain (Scope 3) Accounting and Reporting Standard* (2011), box 5.6 "Accounting for emissions from recycling". [PDF](https://ghgprotocol.org/sites/default/files/standards/Corporate-Value-Chain-Accounting-Reporing-Standard_041613.pdf)
- ISO 14044:2006, *Environmental management - Life cycle assessment - Requirements and guidelines*, avsnitt 4.3.4.3 om allokering vid återanvändning och återvinning.
- EN 15804:2012+A2:2019, *Sustainability of construction works - Environmental product declarations*, modul D.
- Europeiska kommissionens rekommendation (EU) 2021/2279 om användning av metoder för miljöavtryck (PEF), med Circular Footprint Formula. [EUR-Lex](https://eur-lex.europa.eu/eli/reco/2021/2279/oj)
