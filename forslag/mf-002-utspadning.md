---
layout: default_banner
title: "MF-002 Utspädning i genomströmningsnoder"
parent: "Förslag"
nav_order: 2
forslag_id: MF-002
forslag_status: Utkast
forslag_mal: "0.2"
forslag_beror: "§1, §3, §8"
forslag_forfattare: Birger Löfgren
---

# MF-002 Utspädning i genomströmningsnoder

> **Status:** Utkast. Inte beslutat och ingår inte i standarden. Diskuteras i [#49](https://github.com/ICONSOF/massivplus-public-draft/discussions/49).
>
> Berör §1, §3 och §8. Författare: Birger Löfgren.

## Problem

En grossist köper 100 ton av en vara från en leverantör med låga utsläpp, med en börda på 40 ton CO2e, och 100 ton av samma vara från en annan leverantör, med 200 ton CO2e. Den egna Scope 1+2 är 5 ton. Kund X köper varan från den första leverantören och kund Y resten.

Räknas hela lagret som en nod får båda kunderna 122,5 ton. X har köpt varan med låga utsläpp men får samma tal som Y. Delas noden efter inflöde får X 42,5 ton och Y 202,5 ton. Båda uppfyller specifikationens krav på allokering, och summan är densamma. Skillnaden ligger i hur noden är avgränsad.

Coverage ser inte den här skillnaden. En nod kan ha bara faktisk data och ändå radera all differentiering som kom in uppströms.

## Förslag

Utkast till tillägg:

- **Granularitetskrav.** En nod avgränsas på den finaste nivå där inköp per leverantör, försäljning per kund och egen energianvändning alla går att observera.
- **Individuation.** En nod avgränsas av en fysisk enhet vars utsläpp går att mäta för sig, eller av en motpart. Gods som passerar noden används som allokeringsinformation inom den, inte som grund för avgränsningen.
- **Redovisad granularitet.** Noden redovisar vid sidan av Coverage hur fint den är avgränsad, och vad som satte gränsen.

Textändringen i specifikationen är inte skriven än.

## Konsekvenser

Granularitetskravet är det enda tillägget som kostar något för den som rapporterar. Det gör utspädning till en brist där data medger en finare avgränsning, och lämnar den som en redovisad följd av datan där den inte gör det.

## Alternativ som övervägts

En separat spårningsmekanism vid sidan av noderna. Den behövs inte, eftersom en finare avgränsning gör samma arbete.

## Öppna frågor

- Hur kravet tillämpas där flöden blandas fysiskt, som i ett el- eller fjärrvärmenät.
- Om måttet ska heta utspädning eller något annat.

## Beslut

Inte behandlat.
