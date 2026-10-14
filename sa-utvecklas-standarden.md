---
layout: default_banner
title: "Så utvecklas standarden"
parent: "Bidra"
nav_order: 1
---

# Så utvecklas standarden

MASSIV+ utvecklas öppet. Vem som helst kan läsa, fråga och föreslå ändringar. För att den som räknar efter standarden ska veta vilken text som gäller ändras den normativa kärnan bara genom släppta versioner, som beslutas på ett releasemöte.

## Två lager

| Lager | Innehåll | Hur det ändras |
|---|---|---|
| **Normativt** | [Specifikationen](standard/specifikation.md) | Bara genom släppta versioner. Mellan två versioner är texten låst. |
| **Icke-normativt** | Introduktion, positionering, fördjupningar | Löpande, när något behöver förklaras bättre. |

En rättelse av språk, stavning eller en trasig länk i specifikationen får göras mellan versionerna, så länge innebörden inte ändras. Är det tveksamt räknas ändringen som normativ.

## Fördjupningar och förslag

En [fördjupning](fordjupningar/) förklarar standarden som den är och anger vilken version den förklarar. Ett [förslag](forslag/) vill ändra standarden. Förslagen har löpnummer och en status:

| Status | Betyder |
|---|---|
| Utkast | Författaren arbetar fortfarande. Kommentarer välkomna. |
| Under diskussion | Öppet för synpunkter i en tråd i Discussions. |
| Beredd | Har en konkret textändring och tas upp på nästa releasemöte. |
| Antagen | Ingår i specifikationen från en angiven version. |
| Avvisad | Med motivering. Förslaget ligger kvar. |
| Parkerad | Inte moget. Kan tas upp igen. |

## Från fråga till version

```
Discussions  ->  Förslag  ->  Textändring (pull request)  ->  Releasemöte  ->  Ny version
```

De flesta frågor besvaras med en hänvisning till specifikationen eller en fördjupning. Ett förslag skrivs när svaret är att standarden behöver ändras. [Mallen](forslag/mall.md) visar vad ett förslag innehåller.

## Enkelt för vem

Standarden ska framför allt fungera: massbalansen ska hålla, och signalen från en leverantör med bra data ska inte spädas ut på vägen. Det som blir komplicerat när den tillämpas är i första hand något som verktygen ska stödja, inte ett skäl att förenkla bort principen. Vad som faktiskt är svårt tar piloterna reda på, och det underlaget avgör om ett förslag ska förenkla standarden eller om svårigheten ska lösas i verktygen.

## Releasemötet

Versioner släpps när det finns ett dokumenterat behov. För att beslutstidpunkten ska vara förutsägbar finns ett releasemöte varje månad. Nästa möte är {{ site.massiv.nasta_releasemote }}. Mötet går igenom de förslag som är beredda och beslutar för vart och ett om det ska antas, avvisas eller parkeras, och vilken versionsklass en antagen ändring har. Besluten tas i konsensus och motiveringen skrivs in i förslaget. Finns inga beredda förslag släpps ingen version. Det som antas blir en ny version, redovisad i [ändringsloggen](standard/andringslogg.md).

Tills vidare fattas besluten av ett provisoriskt tekniskt råd ur MASSIV+-projektets kärnteam, vars ledamöter deltar i personlig kapacitet. När föreningen finns utser styrelsen rådet efter en öppen nominering.

## Versionsklasser

| Klass | Vad den omfattar |
|---|---|
| Förtydligande eller rättelse | Förklarar ett befintligt krav, eller rättar språk och hänvisningar. Ändrar inte hur någon räknar. |
| Mindre revision | Kompatibel precisering eller tillägg. Metodlogiken bevaras. |
| Större revision | Påverkar metodens innebörd, resultaten, jämförbarheten eller utbytet mellan implementationer. |

Under 0.x, som är pilotfasen, kan större revisioner diskuteras öppet utan formell remiss. Från version 1.0 remitteras större revisioner öppet innan de beslutas.
