---
layout: default_banner
title: "MF-003 Verifierade utsläpp från utsläppshandelssystem"
parent: "Förslag"
nav_order: 3
forslag_id: MF-003
forslag_status: Utkast
forslag_mal: "0.2"
forslag_beror: "§2, §8"
forslag_forfattare: Birger Löfgren
forslag_diskussion: 
---

# MF-003 Verifierade utsläpp från utsläppshandelssystem

> **Status:** Utkast. Inte beslutat och ingår inte i standarden.
>
> Berör §2 och §8. Författare: Birger Löfgren.

## Problem

Specifikationen §2 kräver att alla noder räknar Scope 1 och 2 med standardens gemensamma emissionsfaktorer per bränsleslag och energibärare: "inga egna emissionsfaktorer tillåts för dessa komponenter". Introduktionen säger samtidigt att en aktör som rapporterar verifierade utsläpp under EU ETS kan använda dem direkt som Scope 1. Båda kan inte gälla.

En anläggning i EU ETS räknar sina utsläpp enligt övervakningsförordningen, kommissionens genomförandeförordning (EU) 2018/2066. Metoden bestäms i en övervakningsplan som myndigheten godkänner. Stora källor ska använda anläggningsspecifika värden, till exempel kolhalt och värmevärde från laboratorieanalys av det bränsle som faktiskt eldats, eller mäta utsläppen direkt i skorstenen. Utsläppen verifieras varje år av ett ackrediterat verifieringsorgan enligt genomförandeförordning (EU) 2018/2067, och de verifierade utsläppen per anläggning är offentliga.

Talen är noggrannare än en gemensam faktor per bränsleslag kan bli. Kolhalten i kol och restbränslen varierar mellan leveranser, och en gemensam faktor ger ett snitt. För processutsläpp räcker en faktor per bränsle inte alls. När kalksten bränns till cementklinker frigörs koldioxid ur själva råvaran, och i en masugn kommer kolet både från bränsle och reduktionsmedel. EU ETS räknar sådana utsläpp med en kolbalans över anläggningen.

Med dagens text får en ETS-anläggning två tal för samma utsläpp, ett verifierat och ett räknat med standardens faktorer, och det som går vidare i MASSIV+ är det mindre noggranna.

## Varför undantaget följer principen

Gemensamma faktorer finns för att ta bort godtycket i faktorvalet. Om varje nod väljer sina egna faktorer beror skillnaden mellan två noders Scope 1 på valen, inte på verksamheten, och talen går inte att jämföra (§2).

ETS-metoden är inte ett eget val. Den är föreskriven i förordning, lika för alla anläggningar i systemet, godkänd av en myndighet och granskad av tredje part varje år. En skillnad mellan två ETS-anläggningar beror därför på deras bränslen och processer. Det är den jämförbarhet gemensamma faktorer ska ge, med högre noggrannhet.

## Förslag

Fem tillägg till §2 och §8. Textändringen i specifikationen är inte skriven än.

1. **Verifierade utsläpp ersätter standardens faktorer.** För utsläppskällor som omfattas av en anläggnings tillstånd i EU ETS använder noden de verifierade utsläppen i stället för standardens faktorer.
2. **Övriga källor räknas som i dag.** Källor utanför anläggningens ETS-gräns, som fordon, uppvärmning av lokaler och gaser som ETS inte omfattar, räknas med standardens faktorer.
3. **Redovisning.** Noden anger hur stor del av sitt Scope 1 som bygger på verifierade ETS-utsläpp.
4. **Likvärdiga system.** Samma regel gäller system med föreskriven övervakningsmetod och årlig oberoende verifiering, till exempel UK ETS och det schweiziska systemet, som är länkat till EU:s. Vilka system som räknas förs i en förteckning som förvaltas tillsammans med emissionsfaktorerna.
5. **Coverage (§8).** Verifierade ETS-utsläpp är nodens eget Scope 1 och räknas som faktisk data, som allt annat Scope 1.

## Konsekvenser

Noder i och utanför ETS räknar med olika metoder. För vanliga bränslen som naturgas och diesel är skillnaden liten. För fasta bränslen, restbränslen och processutsläpp kan den vara stor, och där är ETS-talet det mer rättvisande.

Scope 2 påverkas inte direkt, eftersom ETS bara omfattar direkta utsläpp. Indirekt blir det bättre: en el- eller värmeproducent i ETS allokerar sitt verifierade Scope 1 till kunderna, och hos dem blir det Scope 2 med verifierad grund.

ETS räknar med kalenderår, och verifierade utsläpp finns först efter årets slut. En nod som rapporterar oftare än en gång om året kan använda övervakade men ännu inte verifierade värden och ersätta dem när verifieringen är klar.

ETS sätter emissionsfaktorn till noll för biomassa som uppfyller hållbarhetskriterierna. Hur det förhåller sig till standardens behandling av biogent kol beror på hur den frågan avgörs (se diskussionen om standardens omfång).

## Alternativ som övervägts

- Att noden får välja mellan verifierade utsläpp och standardens faktorer. Det tar tillbaka valet som gemensamma faktorer ska ta bort, eftersom noden kan välja det lägre talet.
- Att alla tredjepartsverifierade, anläggningsspecifika faktorer får användas, till exempel enligt ISO 14064-3. En sådan verifiering prövar att företagets egen metod är rätt tillämpad, men metoden är inte densamma mellan företag. Det ger noggrannhet men inte jämförbarhet.
- Att behålla standardens faktorer och redovisa ETS-talet bredvid. Det ger två tal för samma utsläpp, och det som propagerar är det sämre.

## Öppna frågor

- Ska eller får. Förslaget säger att verifierade utsläpp används. Finns det situationer där en ETS-anläggning har skäl att avstå?
- Vilka system räknas som likvärdiga, och vem avgör det?
- Anläggningar under ETS-tröskeln med processutsläpp, till exempel mindre kalk- eller glasverk, har varken ETS-tal eller en standardfaktor som täcker processen. Vad ska de använda?
- Ska verifierade tal från andra regelverk än utsläppshandel kunna räknas, om metoden är föreskriven och lika för alla?

## Beslut

Inte behandlat.
