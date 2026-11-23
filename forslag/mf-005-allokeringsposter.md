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

> **Status:** Utkast, 2026-10-30, språket förenklat 2026-11-21. Ingår inte i standarden. Berör §4 och §6. Författare: Birger Löfgren. Diskussion: [#63](https://github.com/ICONSOF/massivplus-public-draft/discussions/63).
>
> Förslaget anger vad som ska följa med när en nod lämnar en allokering till en annan organisation. När posten bokförs och hur rättelser hanteras anges i [MF-006](mf-006-periodregel.md). Förslaget kan bedömas för sig.

En nod lämnar Actual och Unknown till nästa nod, som bokför dem som A och U ([§4](../standard/specifikation.md#4-allokeringsformel---matematisk-definition)). Specifikationen säger inte hur den uppgiften ska se ut. Utan gemensamma krav går det inte att veta vilken mängd som gäller vilken affär, period och version, eller att undvika att samma mängd bokförs två gånger.

Förslaget kallar uppgiften en allokeringspost och anger vad den ska innehålla.

## Förslag till standardtext

### §4: lägg till Allokeringspost

En allokering mellan organisationer ska kunna dokumenteras som en post. Posten ska innehålla eller tydligt hänvisa till:

| Uppgift | Krav |
|---|---|
| Parter | Utfärdande organisation, som ansvarar för posten, och mottagande organisation |
| Identitet | En referens som är unik hos utfärdaren |
| Period och omfattning | Rapporteringsperiod och vilka affärer eller leveranser posten gäller, till exempel en order, en leverans eller en grupp leveranser |
| Mängd | Actual och Unknown var för sig, med enhet |
| Nodkoppling | Det som behövs för att knyta posten till avsändarens nod och till mottagarens egna noder |
| Version | Postens version, om den är preliminär, slutlig eller rättad enligt [MF-006](mf-006-periodregel.md), och vilken tidigare post den ersätter |
| Metod | Allokeringsregel, beräkningsversion och standardversion |
| Granskning | Om posten är granskad, av vem och med vilken säkerhet ([MF-009](mf-009-faktorer-och-faktisk-data.md)) |

Nodkopplingen kan göras med gemensamma referenser, till exempel ordernummer, som var och en knyter till sina egna noder. Ingen behöver lämna ut sitt interna nodnätverk. Innehåller ett meddelande flera poster ska de gå att skilja åt. En totalsumma ska gå att skilja från posterna den består av, så att den inte bokförs en gång till.

Avsändaren ska kunna stämma av posten mot sin utgående allokering, och mottagaren mot sitt ingående A och U. Delar mottagaren en post mellan egna noder dokumenteras regeln, och delarna ska summera till postens Actual och Unknown. En sådan uppdelning ska gå att skilja från en uppdelning som avsändaren själv har gjort.

Posten ändrar inte allokeringsregeln. §3-4 gäller för nodens hela T, med samma andel för faktisk och okänd del.

Posten får överföras på vilket sätt som helst, om identitet, innehåll och versioner bevaras. Standarden föreskriver inget protokoll eller någon plattform.

### §6: lägg till Versioner och ersättning

En ny version av en post ersätter den tidigare versionen i beräkningen, och historiken sparas. Importeras samma version igen ändras ingenting.

När en deklaration gäller inköp som mottagaren tidigare har bokfört som U, tas det tidigare underlaget bort. Deklarationens Actual och Unknown bokförs i stället för samma inköp. Deklarationens Unknown läggs inte ovanpå mottagarens tidigare underlag. Rättelser hanteras enligt periodregeln i [MF-006](mf-006-periodregel.md).

En kvittens visar att posten har tagits emot. Avsändarens allokering och massbalans (bevarandeprincipen, om [MF-008](mf-008-namnbyte.md) antas) enligt §5 gäller även om mottagaren aldrig hämtar posten eller inte använder MASSIV+.

## Exempel

Stålverket deklarerar 12 ton CO2e Actual och 3 ton Unknown till Grossisten för en grupp inköp under perioden. Talen är påhittade.

| Hos Stålverket | Posten | Hos Grossisten |
|---|---|---|
| 12 Actual och 3 Unknown utgående | Parter, referens, period, omfattning, version, mängd och metod | 12 A och 3 U ingående |
| Kopplad till egen avsändande nod | Referenser som båda kan stämma av mot | Kopplad till egna inköp och noder |

Bolagen kan ha olika interna nodindelningar. Det gemensamma är postens identitet, omfattning och mängd. Avstämningen visar att samma mängd har tagits emot, men avgör inte om allokeringsnyckeln eller nodindelningen är lämplig. Det är samma sak som i [bokföringsanalogin](../fordjupningar/bokforingsanalogin.md): en utgående post hos den ena är en ingående post hos den andra.

Hade Grossisten tidigare 20 ton U för samma inköp tas de bort, och 12 A och 3 U bokförs i stället. Det nya underlaget är 15 ton. Rättar Stålverket sedan posten till 11 Actual och 2 Unknown ersätter den nya versionen den gamla. Båda versionerna finns kvar i historiken, men bara den senaste räknas.

Utsläppen finns kvar i Stålverkets egen redovisning och ingår som uppströmsutsläpp i senare led. Summan av alla bolags tal i kedjan är därför inget mått på de totala utsläppen.

## Vem ser vad

Leverantören vet vilka egna noder som ligger bakom posten. Kunden vet vem som ansvarar för posten, vad den gäller och hur den ska stämmas av.

Grossisten kan be om separata poster för två grupper av inköp. Leverantören knyter dem till sina noder, och Grossisten knyter samma referenser till sina. Ingen får därmed se den andras övriga nätverk.

Lämnar leverantören bara en gemensam post kan Grossisten själv fördela den internt. Den fördelningen är Grossistens egen och visar inte att leverantören har lämnat separata deklarationer.

## Flera poster till samma kund

En kund kan köpa flera kvaliteter under samma period, och då räcker inte alltid en post per kund. §5 tillåter redan allokering per leverans och kvalitet. Förslaget kräver att posten anger vad den gäller, men inte en post för varje leverans. Flera leveranser kan ingå i samma post om omfattningen är tydlig.

Hur fint mottagaren kan fördela beror på dess egna data. Lägger mottagaren allt i en gemensam nod jämnas skillnaderna ut igen. En detaljerad post garanterar alltså inte att detaljerna följer med genom kedjan.

## Teknisk infrastruktur

Specifikationen nämner data spaces som en teknisk vision men specificerar ingen infrastruktur. Ett dataspace kan hantera identitet, behörighet och överföring. Posten beskriver vad som måste bevaras i en sådan överföring, och samma krav gäller om posten skickas som fil, via en portal eller via ett API.

Att ett meddelande har kommit fram räcker inte. Mottagaren måste också kunna hantera period, omfattning, mängd, intern koppling och versioner. Därför fungerar reglerna innan någon gemensam infrastruktur är beslutad, och standarden kan börja användas av ett bolag i taget. En framtida profil för data spaces kan beskriva hur kraven uppfylls.

## Förhållande till andra förslag

- Separata poster kan ge underlag för finare noder enligt MF-004 och för referensen till D enligt [MF-002](mf-002-utspadning.md). Att en post kan identifieras säger däremot inget om vilken referens som är rätt.
- Utgående Actual och Unknown räcker inte för att kunden ska kunna räkna om avsändarens D, eftersom avsändarens egna utsläpp ingår i Actual. MF-005 förutsätter inte att D införs.
- MF-006 anger när posten bokförs och när den är slutlig.

## Alternativ och konsekvenser

- Ett gemensamt tekniskt protokoll i standarden. Skulle underlätta automatisering men binda standarden till ett tekniskt val.
- Bara en totalsumma mellan bolagen. Lämnar period, omfattning och ersättning oklara.

Förslaget väljer gemensamma krav på innehållet, som flera tekniska lösningar kan uppfylla. Det kräver arbete med referenser, versioner och intern koppling. Befintliga order-, leverans- och fakturareferenser kan användas. Ett tekniskt schema återstår att utforma.

## Beslut

Inte behandlat. Förslaget avser tillägg till §4 och §6 och kräver separat beslut.
