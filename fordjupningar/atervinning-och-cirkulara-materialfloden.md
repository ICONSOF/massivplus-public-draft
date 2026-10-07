---
layout: default_banner
title: "Återvinning och cirkulära materialflöden"
parent: "Fördjupningar"
nav_order: 12
---

# Återvinning och cirkulära materialflöden

> **Syfte:** Att visa hur MASSIV+ hanterar material som går tillbaka in i produktionen: skrot som köps tillbaka, restströmmar som säljs vidare och material som lämnas in för återvinning. Texten jämför med LCA-praxis och GHG Protocol och redovisar vad som är öppet.

Den här texten kan läsas fristående. Den förutsätter en grundläggande bild av hur MASSIV+ fungerar - läs [introduktionen](../introduktion.md) eller [specifikationen](../standard/specifikation.md) först om du inte är bekant med ramverket.

---

## I korthet

MASSIV+ hanterar återvinning med samma regler som alla andra affärer. Det ger fem följder.

1. Skrot som säljs är en leverans som vilken annan. Säljaren allokerar en andel av sina utsläpp till den som köper skrotet, och återvinnaren lägger till sina egna utsläpp för omsmältningen.
2. Återvunnet material får en lägre siffra därför att återvinningen släpper ut mindre än produktion ur malm. Enligt branschens egna siffror ger stål från skrot knappt en tredjedel av utsläppen från malm, och aluminium från skrot några procent. Ingen kredit behövs för att skillnaden ska synas.
3. Hur mycket skrotet bär beror på säljarens allokeringsnyckel. Med monetär nyckel bär det lite. Med massbaserad nyckel kan det återvunna materialet bära mer än primärt material. Standarden tar ännu inte ställning till vilken nyckel som passar.
4. Priset avgör riktningen. Får den som lämnar materialet betalt följer utsläppen med materialet. Betalar den för att bli av med det bär den behandlingens utsläpp, som vid avfallsförbränning.
5. Varje varv bär bara sina egna utsläpp. Utsläppen från tidigare varv är redan bokförda hos dem som köpte materialet då.

Sammantaget ligger MASSIV+ nära GHG Protocols rekommenderade metod för återvinning. Öppet är framför allt material som byter ägare utan betalning och vilken nyckel som passar för restströmmar.

## 1. Två betydelser av cirkulär

Ordet cirkulär används om två olika saker när det gäller MASSIV+.

Den första är beräkningsmässig. Två noder säljer till varandra, så att den enas utsläppsvärde beror på den andras. [Specifikationens avsnitt 7](../standard/specifikation.md#7-cirkulära-flöden) låter verktyget lösa det, antingen genom att räkna ut värdena för alla noder i loopen samtidigt, som två ekvationer med två okända (det specifikationen kallar matrisinversion), eller genom att använda föregående periods värde. Användaren behöver inte göra något.

Den andra är cirkulär ekonomi: skrot, återvunnet material och sekundärråvara som går tillbaka in i ny produktion. Det är den betydelsen den här texten handlar om.

De två hänger ihop. När en tillverkare köper tillbaka skrot från samma kunder som den säljer till uppstår exakt det ömsesidiga leveransförhållande som specifikationens avsnitt 7 hanterar. Cirkulär ekonomi ger alltså upphov till beräkningsmässig cirkularitet, och den delen är redan löst. Det som återstår är frågan om hur utsläppen ska fördelas längs loopen.

## 2. Skrotloopen steg för steg

Ta ett verktygsbolag som säljer skärverktyg till en mekanisk verkstad och köper tillbaka de förbrukade verktygen och spånen som skrot. Mönstret är detsamma för stålskrot till en ljusbågsugn, en elektrisk ugn som smälter skrot, för aluminiumskrot till ett omsmältningsverk eller för plastspill som säljs tillbaka till en råvaruleverantör.

Steg ett: verktygsbolaget levererar verktyg och allokerar en andel av sin totala utsläppsmassa T till verkstaden med sin dokumenterade allokeringsnyckel, den regel som fördelar utsläppen mellan kunderna, till exempel efter intäkt eller vikt. Andelen hamnar i verkstadens uppströmsvärde.

Steg två: verkstaden säljer skrotet till verktygsbolaget. I den affären är verkstaden leverantör. Den allokerar en andel av sin egen T, där verktygsbolagets tidigare allokering ingår, till verktygsbolaget med sin nyckel.

Steg tre: verktygsbolaget smälter om skrotet eller återvinner det kemiskt. Det återvunna materialet bär den andel som verkstaden allokerat plus verktygsbolagets egna Scope 1 och 2 för återvinningsprocessen. Om återvinningen ger lägre utsläpp än primär produktion får det återvunna materialet en lägre siffra, eftersom de uppmätta utsläppen är lägre. Hur stor skillnaden är tas upp i nästa avsnitt.

## 3. Återvunnet mot primärt material

Att framställa material av skrot ger betydligt lägre utsläpp än att framställa det ur malm. Metallen i skrotet behöver inte utvinnas ur malm en gång till, och därmed faller de mest energikrävande stegen bort.

Branschens egna siffror visar storleksordningen. Stål från malm tillverkas i masugn, där järnet utvinns med koks, och stål från skrot i ljusbågsugn.

| Material | Från malm | Från skrot | Källa |
|---|---|---|---|
| Stål, ton CO₂ per ton råstål, 2022 | 2,33 (masugn) | 0,68 (ljusbågsugn) | [worldsteel](https://worldsteel.org/wp-content/uploads/Sustainability-indicators-report-2023.pdf) |
| Aluminium, ton CO₂e per ton, 2022 | 15,1 | 0,52 | [International Aluminium Institute](https://aluminium.org.au/wp-content/uploads/2024/10/IAI-Factsheet-Claim-3_GHG-Saving_external.pdf) |

I båda jämförelserna går skrotet in utan börda, och bara omsmältningen räknas. IAI påpekar därför själva att talet för omsmältning inte ska läsas som klimatavtrycket för återvunnet aluminium. Talen är också globala genomsnitt, och elen väger tungt: för primäraluminium producerat i Europa anger samma faktablad 6,7 ton, European Aluminiums tal för 2015.

I MASSIV+ syns skillnaden utan någon kredit. Den som köper material av en återvinnare får återvinnarens faktiska utsläpp i sitt uppströmsvärde, i stället för en primärproducents. Ett stålverk som smälter skrot har ingen masugn i sitt Scope 1, och det lägre talet följer med till varje led nedströms.

Ett stålverks tal i MASSIV+ blir ändå inte detsamma som branschens siffror, av tre skäl. Elen räknas med faktorn för det elområde verket ligger i, så ett verk med ren el hamnar långt under det globala snittet. Uppströms ingår allt som verkets leverantörer allokerar, vilket är bredare än branschens systemgräns. Och skrotet bär den andel som säljaren allokerar till det, inte noll (avsnitt 4). Det som består är storleksordningen på skillnaden, eftersom den kommer av själva processen.

Det är en fysisk minskning, och den är den viktigaste effekten av återvinning. Det som sänker summan av utsläppen i systemet är att omsmältning ersätter primär produktion. Det förutsätter att det återvunna materialet ersätter primärt material och inte kommer till utöver det. Om det sker är en fråga om marknaden som helhet, och den kan en redovisningsstandard inte besvara. Hur utsläppen sedan fördelas mellan den som säljer skrotet och den som köper det ändrar inte summan, men det kan påverka hur mycket av fördelen köparen ser. Det är ämnet för nästa avsnitt.

## 4. Säljarens nyckel avgör hur mycket skrotet bär

Skrotet är ett av säljarens utflöden, och säljaren fördelar sin utsläppsmassa över utflödena med den nyckel den valt för hela noden ([specifikationen, avsnitt 3](../standard/specifikation.md#3-allokering---att-fördela-utsläpp-till-mottagare)). Det är den nyckeln som avgör hur mycket skrotet bär. Undviken börda, en kredit för den primärproduktion som återvinningen antas ersätta, ingår inte, eftersom MASSIV+ inte ger krediter (avsnitt 7).

> En verkstad har under perioden en total utsläppsmassa på 1 000 ton CO₂e. Den säljer bearbetade detaljer för 99 miljoner kronor och stålskrot för 1 miljon till ett stålverk med ljusbågsugn. Detaljerna väger 400 ton och skrotet 100 ton.
>
> Med monetär nyckel bär skrotet 1 procent av verkstadens utsläppsmassa, 10 ton. Med massbaserad nyckel bär det 20 procent, 200 ton.
>
> Stålverkets egna utsläpp för att smälta om de 100 tonnen, med el och övriga insatsvaror, sätts till 68 ton, världsgenomsnittet för skrotbaserat stål. Till det kommer verkstadens andel. Det återvunna stålet bär 78 ton med monetär nyckel hos verkstaden och 268 ton med massbaserad. Samma mängd stål via masugn hade enligt världsgenomsnittet gett omkring 233 ton.
>
> I båda fallen sjunker verkstadens övriga kunders andel med lika mycket som skrotet tar på sig, så verkstadens summa är densamma.
>
> Exemplet kombinerar branschens genomsnitt med MASSIV+:s fördelning. Det visar storleksordningar, inte vad två verkliga verk skulle rapportera.

Med monetär nyckel syns återvinningens fördel hos den som köper det återvunna stålet, 78 mot 233 ton. Skrotet bär en liten börda eftersom det har ett lågt värde i förhållande till verkstadens övriga försäljning, och resultatet hamnar nära cut-off, en vanlig metod i LCA där återvunnet material inte bär någon börda från sitt tidigare liv (avsnitt 8). Med massbaserad nyckel bär det återvunna stålet mer än primärt stål, 268 mot 233 ton, trots att omsmältningen gav mindre än en tredjedel av masugnsvägens utsläpp. Verkstadens fabriksutsläpp flyttas då till en restprodukt med lågt värde, och nyckeln döljer den fysiska fördelen i det tal köparen ser, utan att ändra något i systemets summa.

Standarden tar ännu inte ställning till vilken nyckel som passar noder med stora restströmmar av lågt värde, och frågan behöver utredas.

## 5. Priset avgör riktningen

I MASSIV+ bestäms riktningen av vem som betalar, inte av vart materialet rör sig. Den som betalar är kund, den som får betalt är leverantör, och utsläppsdata går från leverantör till kund. Samma regel ger tre fall för material som går till återvinning.

Positivt pris. Den som lämnar materialet får betalt och är leverantör. Utsläppen går med materialet till återvinnaren, som i avsnitt 2. Det är det vanliga fallet för metallskrot.

Negativt pris. Den som lämnar materialet betalar för att bli av med det. Återvinnaren säljer då en behandlingstjänst, och riktningen vänds: återvinnaren är leverantör, den som lämnar materialet är kund, och behandlingens utsläpp allokeras till den som lämnade materialet. Det är samma resonemang som för [avfallsförbränning](avfallsforbranning-och-allokering.md). Återvinnaren har då två utflöden, behandlingstjänsten och den sekundärråvara den säljer vidare, och fördelar sin utsläppsmassa mellan dem med sin nyckel. Material som pendlar mellan positivt och negativt pris med marknaden byter riktning med priset.

Pris noll. Ingen betalning sker, och därmed saknas den affärsrelation som MASSIV+ bygger på. Standarden har redan listat detta som ett öppet gränsfall, vederlagsfria strömmar (se [metodologiska risker](metodologiska-risker.md#koordinatens-gränsfall)). Ett förslag är att en leverantörsrelation finns så snart det finns ett dokumenterat överlämningsavtal, oavsett pris, med den som lämnar materialet som leverantör. Hur stor börda flödet bär avgörs då av leverantörens nyckel. Med monetär nyckel bär ett flöde till priset noll ingenting, vilket sammanfaller med cut-off. Med massbaserad nyckel bär det börda i proportion till vikten. Förslaget bör prövas i pilot innan det skrivs in i specifikationen.

## 6. Material från privatpersoner

När en privatperson lämnar in en uttjänt produkt till återvinning kommer materialet från någon som inte är en nod. Specifikationen behandlar en privatkonsument som en sänka: när produkten såldes till konsumenten terminerade kedjan, och den ackumulerade bördan löstes upp på produkten i det ledet ([specifikationen, avsnitt 5](../standard/specifikation.md#från-affärsrelation-b2b-till-produktinformation-b2c)). Ett hushåll har inget eget Scope 1 och 2 att allokera.

Materialet går därför in i kedjan igen utan börda från sitt tidigare liv och bär bara insamlarens och återvinnarens egna utsläpp. Det följer av hur sänkan är definierad, men står inte uttryckligen i specifikationen och bör skrivas ut där.

Skillnaden mot skrot från ett företag är att ett företag som inte är nod ändå har utsläpp som kan allokeras. Skrot från en sådan leverantör bokförs därför som okänt uppströmsvärde, U, kvantifierat med bästa tillgängliga metod, exempelvis inköpsbelopp eller vikt, och konverteras till faktiskt värde, A, när leverantören börjar rapportera.

## 7. Vad MASSIV+ visar, och vad som hör hemma i andra instrument

MASSIV+ visar de utsläpp som faktiskt uppstått, fördelade per affärsrelation. För cirkulära flöden får det fyra följder.

Varje varv bär bara sina egna utsläpp. Ta en stålbalk. Utsläppen från när den tillverkades bokfördes när balken köptes, och följde med huset till den som ägde det. När huset flera decennier senare rivs och balken säljs som skrot, bär skrotet en andel av rivningsfirmans utsläpp, och stålverket lägger till sina utsläpp för omsmältningen. Utsläppen från den första tillverkningen följer inte med, eftersom de redan är bokförda hos husets ägare. Ett material som gått fem varv bär bara det senaste varvets utsläpp, på samma sätt som den femte ägaren till en begagnad bil inte betalar fem nybilspriser.

Siffrorna innehåller bara bokförda utsläpp. Återvinning ger ingen kredit, och det finns ingen motsvarighet till modul D i EN 15804, där EPD:er redovisar nyttan av återvinning bortom produktens systemgräns, eller till de krediter som EU:s miljöavtrycksmetod PEF fördelar med sin Circular Footprint Formula. Det är samma hållning som standarden har till klimatkompensation (se [köpt energi och Scope 2](kompensation-och-faktiska-floden.md)), och den sammanfaller med GHG Protocols rekommenderade metod (avsnitt 8).

Incitamentet finns ändå, och på båda sidor. Den som köper återvunnet material får ett lågt uppströmsvärde när återvinningen ger lägre utsläpp än primär produktion och säljarens nyckel inte lägger en stor del av fabriksutsläppen på skrotet (avsnitt 3 och 4). Den som säljer skrot flyttar en del av sin utsläppsmassa från sina huvudprodukter till skrotköparen, så att säljarens övriga kunder ser en något lägre siffra.

Återvinningsbarhet som produktegenskap ligger utanför. Att en produkt kan återvinnas till en viss andel är en uppgift för ett digitalt produktpass eller en EPD. MASSIV+ ser återvinningen när affären faktiskt äger rum.

En praktisk konsekvens gäller återköpsprogram. Skrot som köps från många små verkstäder som inte är noder bokförs som U. Ett återköpsprogram som växer snabbt kan därför sänka köparens Coverage, andelen faktisk data, tills skrotleverantörerna ansluter. Det är samma mekanism som för vilken leverantör som helst som inte rapporterar, och siffran blir bättre när leverantörerna ansluter och replacement rule, regeln att faktisk data ersätter det okända värdet, byter U mot A.

## 8. Jämförelse med LCA-praxis och GHG Protocol

Skrotflödet i avsnitt 2 motsvarar det ISO 14044, standarden för livscykelanalys, behandlar under allokering vid återanvändning och återvinning (avsnitt 4.3.4.3): ett material lämnar ett produktsystem och används i ett annat, och frågan är hur bördan ska delas mellan dem. Standarden skiljer på två fall (4.3.4.3.3). Behåller materialet sina inneboende egenskaper, som när metallskrot smälts om till likvärdig kvalitet, gäller en procedur för sluten loop: allokering behövs inte, eftersom det återvunna materialet ersätter primärt material. Ändras egenskaperna gäller en procedur för öppen loop, och då ska allokeringen om möjligt grundas i första hand på fysiska egenskaper, exempelvis massa, i andra hand på ekonomiskt värde och i tredje hand på antalet efterföljande användningar (4.3.4.3.4).

I praktiken har det gett två huvudspår. Med cut-off bär det återvunna materialet ingen börda från sitt tidigare liv, bara återvinningsprocessen. Med undviken börda (avoided burden) får den som skickar material till återvinning en kredit för den primärproduktion materialet antas ersätta. Metallindustrin har argumenterat för det senare med hänvisning till ISO 14044: metaller kan smältas om till likvärdig kvalitet och ersätter därmed primär metall, vilket är situationen som proceduren för sluten loop beskriver. Positionen finns i [metallindustrins gemensamma deklaration om återvinning](https://doi.org/10.1065/lca2006.11.283) och utvecklas för aluminium av [European Aluminium](https://european-aluminium.eu/wp-content/uploads/2022/10/2013-09-23-aluminium-recycling-in-lca.pdf).

GHG Protocol behandlar återvinning i en egen ruta i Scope 3-standarden och mer utförligt i den tekniska vägledningen för kategori 5, avfall från den egna verksamheten. Den rekommenderade metoden heter recycled content-metoden, som GHG Protocols produktstandard också kallar cut-off-metoden. Utsläppen från själva återvinningen redovisas av den som köper det återvunna materialet, i kategori 1 eller 2. Den som skickar material till återvinning redovisar i kategori 5 de steg i materialåtervinningen som inte redan ingår i det återvunna materialets emissionsfaktor, och får ta med transporten dit. Undvikna utsläpp får inte dras av från inventeringen men får redovisas separat.

För material som behåller sina egenskaper tillåter vägledningen också closed loop approximation. Metoden drar av den primärproduktion som återvinningen antas ersätta. Produktstandarden anger att den motsvarar metallindustrins ansats och proceduren för sluten loop i ISO 14044.

Kapitel 8 i Scope 3-standarden, om allokering, har en regel som också gäller här. Avfall utan marknadsvärde ska inte tilldelas några utsläpp. Blir avfallet säljbart behandlas det som vilken annan produkt som helst och kan tilldelas en andel av anläggningens utsläpp.

| | GHG Protocol | MASSIV+ |
|---|---|---|
| Återvinningsprocessens utsläpp | Hos köparen av det återvunna materialet | Hos återvinnaren, allokerat till köparen av det återvunna materialet |
| Kredit för undviken primärproduktion | Ingen med recycled content-metoden. Closed loop approximation drar av ersatt primärproduktion. Övriga undvikna utsläpp redovisas separat | Ingen |
| Material utan marknadsvärde | Tilldelas inga utsläpp | Tilldelas inget med monetär nyckel. Om det alls finns en leverantörsrelation är ett öppet gränsfall (avsnitt 5) |
| Säljbart skrot | Behandlas som en produkt och kan tilldelas utsläpp | Bär den andel säljarens nyckel ger |
| Insamling och sortering | Hos den som skickar materialet, om stegen inte ingår i det återvunna materialets emissionsfaktor | Följer priset: hos den som lämnar materialet vid negativt pris, hos köparen av det återvunna materialet vid positivt pris |

MASSIV+ ligger alltså nära GHG Protocols rekommenderade metod. Skillnaden är hur gränsen dras. I GHG Protocol avgörs den av vad som ingår i den emissionsfaktor köparen använder. I MASSIV+ avgörs den av vem som betalar vem, samma logik som gör att MASSIV+ inte behöver någon särskild undantagsregel för avfallsförbränning. MASSIV+ har heller ingen motsvarighet till closed loop approximation, eftersom den metoden räknar in primärproduktion som antas ha ersatts och inte bara de utsläpp som faktiskt uppstått.

## 9. Vad som är avgjort och vad som är öppet

Följande följer direkt av standarden som den står:

- En materialloop är en följd av vanliga affärer, och loopar mellan samma parter löses på verktygsnivå.
- Återvunnet material får en lägre siffra genom återvinnarens lägre faktiska utsläpp, och återvinning ger ingen kredit.
- Säljarens nyckel avgör hur stor börda skrotet bär, och nyckeln gäller hela noden.
- Priset avgör riktningen, och negativt pris ger samma behandling som avfallsförbränning.

Följande är öppet eller föreslaget:

- Vederlagsfria strömmar. Förslaget att ett dokumenterat överlämningsavtal räcker för en leverantörsrelation bör prövas i pilot.
- Material från privatpersoner. Att det går in utan börda följer av sänkdefinitionen men behöver skrivas ut i specifikationen.
- Nyckeln för restströmmar. Standarden tar inte ställning än, och frågan behöver utredas. En närliggande fråga är om noder med stora restströmmar ska kunna dela upp sig så att restströmmen får en egen nyckel.

---

## Källor

- GHG Protocol, *Corporate Value Chain (Scope 3) Accounting and Reporting Standard* (2011), box 5.6 "Accounting for emissions from recycling" och kapitel 8 om allokering. [PDF](https://ghgprotocol.org/sites/default/files/standards/Corporate-Value-Chain-Accounting-Reporing-Standard_041613.pdf)
- GHG Protocol, *Product Life Cycle Accounting and Reporting Standard* (2011), avsnitt 9.3.6 om recycled content-metoden (cut-off) och closed loop approximation, och 9.3.7 om valet mellan dem. [PDF](https://ghgprotocol.org/sites/default/files/standards/Product-Life-Cycle-Accounting-Reporting-Standard_041613.pdf)
- GHG Protocol, *Technical Guidance for Calculating Scope 3 Emissions*, kapitel 5 (kategori 5), avsnittet "Accounting for emissions from recycling". [PDF](https://ghgprotocol.org/sites/default/files/2022-12/Ch5_GHGP_Tech.pdf)
- ISO 14044:2006, *Environmental management - Life cycle assessment - Requirements and guidelines*, avsnitt 4.3.4.3 om allokering vid återanvändning och återvinning: 4.3.4.3.3 om procedurerna för sluten och öppen loop, 4.3.4.3.4 om ordningen för allokeringsgrund.
- Atherton, J., *Declaration by the metals industry on recycling principles*, International Journal of Life Cycle Assessment 12(1), 59-60 (2007). Stödd av stål- och metallindustrins branschorganisationer. [DOI](https://doi.org/10.1065/lca2006.11.283)
- European Aluminium, *Aluminium recycling in LCA* (2013), om substitutionsmetoden och varför aluminium kan behandlas som sluten loop. [PDF](https://european-aluminium.eu/wp-content/uploads/2022/10/2013-09-23-aluminium-recycling-in-lca.pdf)
- worldsteel, *Sustainability indicators 2023 report*, utsläppsintensitet per produktionsväg 2021-2022. [PDF](https://worldsteel.org/wp-content/uploads/Sustainability-indicators-report-2023.pdf)
- International Aluminium Institute, *Recycling aluminium saves greenhouse gas emissions by over 90%* (faktablad 2024), 2022 års tal för primär och omsmält aluminium. [PDF](https://aluminium.org.au/wp-content/uploads/2024/10/IAI-Factsheet-Claim-3_GHG-Saving_external.pdf)
- EN 15804:2012+A2:2019, *Sustainability of construction works - Environmental product declarations*, modul D.
- Europeiska kommissionens rekommendation (EU) 2021/2279 om användning av metoder för miljöavtryck (PEF), med Circular Footprint Formula. [EUR-Lex](https://eur-lex.europa.eu/eli/reco/2021/2279/oj)
