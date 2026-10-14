---
layout: default_banner
title: "MF-001 Lagerhantering"
parent: "Förslag"
nav_order: 1
forslag_id: MF-001
forslag_status: Utkast
forslag_mal: "0.2"
forslag_beror: "§5, §6"
forslag_forfattare: Birger Löfgren
---

# MF-001 Lagerhantering

## Problem

En nod fördelar periodens hela utsläppsmassa på periodens leveranser, enligt massbalansen i specifikationen §5. Ett bolag som köper komponenter ett år och säljer de färdiga produkterna året efter får komponenternas utsläpp i sin börda det första året. De fördelas då på det årets kunder, alltså på fel kunder. Kunderna året efter får i stället det årets inköp.

- Är lagret stabilt jämnar det ut sig.
- När lagret byggs upp blir talen för höga, och när det töms blir de för låga.
- I det extrema fallet sker alla inköp ena året och all försäljning det andra. Då finns inga leveranser att fördela på det första året, och specifikationen säger inte vad som gäller.

Specifikationen §6 är dessutom otydlig om tidsförskjutningen.

## Förslag

Ett lagerkonto för utsläpp, som i ekonomisk redovisning. Utsläppen från inköpta varor ligger kvar i lager tills varorna säljs eller förbrukas. Det följer [bokföringsanalogin](../fordjupningar/bokforingsanalogin.md), och lagervärderingen finns redan i bolagens bokföring.

Kapitalvaror är samma fråga med längre tidsförskjutning. Utgångspunkten är att följa GHG Protocol (Scope 3 Standard, box 5.4), som bokför hela utsläppet det år kapitalvaran köps och inte skriver av det.

Textändringen i specifikationen är inte skriven än.

## Konsekvenser

Ska beskrivas: vad som läggs in och tas ut ur lagerkontot, värderingsprincip, kopplingen till faktisk och okänd data och till Coverage.

## Alternativ som övervägts

- Att behålla periodlogiken och jämna ut med glidande medelvärde.
- Att bara kräva lagerkonto när lagret ändras mycket.

## Öppna frågor

- Hur förenklingen för små noder ska se ut. Det är kärnfrågan i förslaget.
- Om investeringar ska hanteras här eller i ett eget förslag.

## Beslut

Inte behandlat.
