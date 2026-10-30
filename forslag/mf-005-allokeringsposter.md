---
layout: default_banner
title: "MF-005 Allokeringsposter mellan organisationer"
parent: "Förslag"
nav_order: 5
forslag_id: MF-005
forslag_status: Utkast
forslag_mal: "0.2"
forslag_beror: "§4, §6"
forslag_forfattare: Birger Löfgren
forslag_diskussion: https://github.com/ICONSOF/massivplus-public-draft/discussions/63
---

# MF-005 Allokeringsposter mellan organisationer

> **Status:** Utkast, 2026-10-30. Ingår inte i standarden. Berör §4 och §6. Författare: Birger Löfgren. Diskussion: [#63](https://github.com/ICONSOF/massivplus-public-draft/discussions/63).
>
> [MF-004](mf-004-nodindelning.md) behandlar interna beräkningsenheter och [MF-002](mf-002-utspadning.md) fördelningsmåttet D. Detta förslag preciserar informationsinnehållet när en beräknad allokering lämnas till nästa organisation. Det kan bedömas separat från de två andra.

Enligt [specifikationens §4](../standard/specifikation.md) lämnar en nod Actual, ett belopp med faktisk grund, och Unknown, ett numeriskt underlag för den okända delen, till nästa nod. Hos mottagaren bokförs dessa som A respektive U. En allokeringspost är här den identifierbara uppgift som beskriver denna tilldelning mellan organisationerna.

## Förslag till standardtext

### §4: lägg till Gemensam allokeringspost

En allokering mellan organisationer ska kunna dokumenteras som en gemensamt identifierbar post. Posten ska innehålla eller entydigt hänvisa till:

| Uppgift | Minimikrav |
|---|---|
| Parter | Ansvarig utfärdande organisation och mottagande organisation |
| Identitet | En postreferens som är unik inom utfärdarens referenssystem |
| Period och omfattning | Rapporteringsperiod samt vilka affärer eller leveranser posten omfattar, exempelvis en order, en leverans eller en definierad grupp |
| Belopp | Actual och Unknown var för sig med utsläppsenhet |
| Nodkoppling | Underlag för entydig hänföring till avsändande nod och mottagarens egna beräkningsnoder |
| Version | Postens version och hänvisning till eventuell tidigare version eller post som den ersätter |
| Metod | Tillämpad allokeringsregel samt beräknings- och standardversion |

Nodkopplingen får upprätthållas genom gemensamma externa referenser som parterna kopplar till sina egna noder. Mottagaren ansvarar för sin interna hänföring. Hela motpartens interna nodnätverk behöver inte lämnas ut. Om ett meddelande innehåller flera separata allokeringsposter ska de vara identifierbara var för sig. Ett sammanfattande totalbelopp ska kunna särskiljas från de poster som ingår i det så att det inte bokförs en gång till.

Avsändaren ska kunna stämma av postens belopp mot sin utgående allokering. När mottagaren använder posten ska den kunna stämmas av mot mottagarens ingående A respektive U. Om mottagaren delar en post mellan egna noder ska hänföringsregeln dokumenteras och delarna summera till postens Actual respektive Unknown. Uppdelningen ska kunna skiljas från en finare uppdelning som avsändaren själv har deklarerat.

Om fördelningen görs genom en intern beräkningsnod gäller §3-4 för hela nodens T med samma Share för faktisk och okänd del. Posthanteringen inför inget undantag från allokeringsregeln.

Överföringssättet får väljas fritt om postens identitet, innehåll och versionssamband bevaras. Denna regel föreskriver inget visst protokoll eller någon särskild plattform.

### §6: lägg till Versions- och ersättningshantering

En ny version av en allokeringspost ska ersätta den tidigare versionens bidrag i beräkningen, med historiken bevarad. En upprepad överföring eller import av samma postversion ska inte ge ytterligare utsläppsbelopp.

När en mottagen deklaration överlappar ett tidigare U-underlag ska det överlappande underlaget tas bort. Deklarationens Actual och eventuella kvarvarande Unknown ska därefter bokföras för samma omfattning. Den deklarerade okända delen får inte läggas ovanpå mottagarens tidigare underlag för samma inköp. Rättelser och uppdaterad propagering ska versionshanteras enligt standardens periodregler.

En kvittens anger att posten har mottagits eller behandlats. Avsändarens allokering och lokala massbalans enligt §5 ska upprätthållas även när mottagaren inte hämtar posten eller använder MASSIV+. Kvittens är därför inget villkor för att avsändaren ska redovisa sitt utgående flöde.

## Varför behövs en gemensam post?

§4 definierar redan hur Actual och Unknown beräknas och blir A respektive U i nästa nod. §6 kräver att bättre data ersätter tidigare U. För att detta ska fungera i ett praktiskt informationsutbyte behöver organisationerna kunna identifiera vilket belopp som avser vilken affär, period och version.

Detta stöder MASSIV+:s syfte att kunna börja med tillgänglig data och förbättra underlaget successivt. Ett företag ska kunna använda standarden utan att först installera en viss infrastruktur eller få insyn i alla leverantörers interna beräkningar. Samtidigt behöver den data som faktiskt utbyts vara tillräckligt entydig för bokföring och senare rättelser.

Förslaget preciserar innehållet och hanteringen. Ett maskinläsbart schema, identitetsformat, säkerhetsprofil eller kommunikationsprotokoll kan senare bygga på dessa krav.

## Bokföringsanalogin som utgångspunkt

[Bokföringsanalogin](../fordjupningar/bokforingsanalogin.md) beskriver hur en utgående mängd hos en part motsvarar en ingående mängd hos en annan. Anta att Ovako deklarerar 12 ton CO2e Actual och 3 ton Unknown till Helens för en definierad grupp inköp under perioden. Talen är påhittade.

| Hos Ovako | Gemensam post | Hos Helens |
|---|---|---|
| 12 Actual och 3 Unknown utgående | Parter, referens, period, omfattning, version, belopp och metod | 12 A och 3 U ingående |
| Koppling till egen avsändande nod | Referenser som kan stämmas av | Koppling till egna inköp och mottagande noder |

Bolagen får ha olika interna nodindelningar. Det gemensamma är postens identitet, omfattning och belopp. Avstämningen visar att samma mängd har tagits emot; den väljer inte allokeringsnyckel eller avgör om den interna nodindelningen är lämplig.

Analogin gäller avstämning av en överförd uppgift. Utsläppen ligger kvar i utsläppskällans egen redovisning och kan ingå som uppströmsutsläpp i flera senare led. Summan av alla bolags utsläppstal i kedjan blir därför inget mått på nya fysiska utsläpp. Förslaget inför heller inget avdrag av de egna utsläppen när en allokering skickas vidare.

## Vem ser vad?

Leverantören behöver veta vilka egna noder och beräkningar som ligger bakom den post den utfärdar. Kunden behöver veta vilken ansvarig organisation som lämnar posten, vad den omfattar och hur den kan hänföras och stämmas av i kundens egen beräkning.

Helens kan exempelvis be om separata poster för två grupper av inköp. Leverantören kan knyta dem till sina avsändande noder internt. Helens kan knyta samma externa referenser till sina egna noder och till berörda leveranser till kunder. Referenserna ger ingen automatisk rätt till hela leverantörens eller kundens övriga nätverk.

Om leverantören endast lämnar en gemensam post kan Helens dokumentera en intern fördelning. Den fördelningen är Helens eget beräkningsunderlag. Den visar inte att leverantören har lämnat separata deklarationer för varje del.

## En kundrelation kan innehålla flera leveransgrupper

Ett kundbolag kan köpa flera kvaliteter eller göra olika inköp under samma period. En post per kund är därför inte alltid tillräcklig för det beslut som ska följas upp. §5 tillåter redan finkornighet per leverans och kvalitet.

Förslaget kräver att en post anger vad den omfattar, men kräver inte en post för varje fysisk leverans. Flera leveranser kan sammanföras när omfattningen är tydlig och nivån är användbar för mottagaren. Om fler delposter överförs ska de vara urskiljbara. En enda totalsumma kan inte samtidigt beskrivas som flera separata leverantörsdeklarationer.

Mottagarens egna data avgör vilken lokal hänföring som är möjlig. Kända leveranskopplingar och fördelningar efter dokumenterad nyckel behöver skiljas åt. Om mottagaren väljer en gemensam nod kan den nodens fortsatta allokering åter jämna ut skillnaderna. Postens detaljnivå garanterar därför inte att samma upplösning bevaras genom hela kedjan.

## Rättelser, återimport och bättre leverantörsdata

Anta att Helens tidigare har 20 ton U för de inköp som omfattas av posten med 12 Actual och 3 Unknown. När deklarationen används tas det tidigare 20-tonsbidraget bort. Därefter bokförs 12 A och 3 U. Nytt totalunderlag för omfattningen är 15. Det är varken 35 eller 32 ton. Ändringen av totalunderlaget är tillåten eftersom bättre information ersätter det gamla underlaget.

Om samma post hämtas igen ändras ingen mängd. Om utfärdaren senare rättar posten till 11 Actual och 2 Unknown ersätter den nya versionen bidraget 12 och 3. Båda versionerna finns i historiken, medan enbart den tillämpliga versionen ingår i beräkningen. Delvisa rättelser kräver att den ersatta omfattningen kan identifieras.

Detta är en precisering av §6:s replacement rule. Förslaget kräver inte att gamla rapporteringsperioder ändras tyst; period, metod och version ska följa standardens regler för uppdatering och fortsatt propagering.

## Förhållandet till dataspace-ansatsen

Specifikationens syftesavsnitt nämner en teknisk vision för peer-to-peer-datadelning med data spaces, samtidigt som infrastrukturen ännu inte är specificerad. Ett dataspace kan ge stöd för deltagaridentitet, tillträde, avtal och kontrollerad överföring mellan självständiga organisationer.

Den föreslagna allokeringsposten beskriver vad som behöver bevaras genom en sådan överföring. Dataspace-deltagarens identitet, den tekniska anslutningens adress och MASSIV+-nodens identitet fyller olika funktioner. Ett bolag kan ha flera interna beräkningsnoder eller flera tekniska anslutningar. Antalen behöver inte sammanfalla.

En lyckad dataöverföring visar att ett meddelande kommit fram. För att mottagaren ska bokföra rätt behöver även postens period, omfattning, belopp, interna hänföring och ersättningssamband hanteras. Dessa krav gäller också när överföringen sker som fil, via portal eller API, ett programmerbart gränssnitt.

Förslaget gör därför beräknings- och informationsreglerna användbara före ett beslut om gemensam teknisk infrastruktur. En framtida dataspace-profil kan precisera hur kraven uppfylls. Standarden kan därmed tillämpas unilateralt och med stegvis anslutning i enlighet med sitt befintliga syfte.

## Förhållandet till D och nodindelningen

Poster med separata belopp kan ge underlag för finare interna beräkningar enligt MF-004. De kan också bidra till en referensfördelning för D enligt MF-002 när kopplingen till mottagarrelationerna finns. Att en post är identifierbar räcker däremot inte för att avgöra vilken referens som är relevant.

Om D redovisas behöver det följa med en beskrivning av mätområde, referens och mottagarnivå enligt det förslaget. Utgående Actual och Unknown räcker inte ensamma för att kunden ska kunna räkna om avsändarens D, eftersom områdets egna utsläpp då ingår i Actual. MF-005 förutsätter inget beslut om att D ska införas.

## Alternativ och praktiska konsekvenser

Ett gemensamt tekniskt protokoll direkt i kärnstandarden skulle kunna underlätta automatisering men samtidigt knyta metodens införande till ett visst tekniskt val. Enbart ett totalbelopp mellan bolag lämnar i stället period, omfattning och ersättning oklara. Förslaget väljer gemensamma innehållskrav som kan bäras av flera tekniska lösningar.

Minimikraven innebär arbete med referenser, versionshistorik och lokal hänföring. Befintliga order-, leverans- och fakturareferenser kan användas när de tillsammans identifierar rätt omfattning. De behöver inte göras identiska med den interna nodindelningen. Ett separat tekniskt schema återstår att utforma och kan granskas mot de föreslagna innehållskraven.

## Beslut

Inte behandlat. Förslaget avser tillägg till §4 och §6 och kräver separat beslut.
