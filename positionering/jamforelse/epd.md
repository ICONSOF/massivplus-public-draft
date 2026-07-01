---
layout: default
title: "EPD / ISO 14025"
parent: "Jämförelse med andra ramverk"
grand_parent: "Positionering"
nav_order: 9
---

# MASSIV+ och EPD / ISO 14025

> Del av [Jämförelse med andra ramverk](../jamforelse-med-andra-ramverk.md) - översiktstabell och sammanfattande positionering finns där. Den gemensamma ingången för produktstandarderna finns i [den generella relationen](produktstandarder.md#den-generella-relationen). Ny här? Läs [introduktionen](../../introduktion.md) först.

En EPD (Environmental Product Declaration) är en typ III-miljödeklaration enligt ISO 14025 - ett tredjepartsverifierat dokument som redovisar en produkts miljöpåverkan baserat på LCA. ISO 14025 kräver att beräkningarna görs enligt ISO 14040/14044 och att produktkategorispecifika regler (PCR) specificerar beräkningsmetodik: systemgränser, cut-off-kriterier, allokeringsregler och datakvalitetskrav. Sektoriella tillämpningar som EN 15804 (byggprodukter) lägger ytterligare krav ovanpå detta. EN 15804+A2 har därutöver krav på datakvalitetsbedömning och dokumentation av primärdataandel; andra PCR varierar i hur explicit de behandlar detta. Distinktionen *primärdata vs sekundärdata* är alltså etablerad i EPD-systemet, men hanteras som metadata bredvid ett enskilt rapporterat värde per produkt. EPD-systemet är metodologiskt föreskrivande för *beräkningarna* - men det EPD saknar är definitionen av hur utsläpp ska fördelas och propageras längs en värdekedja. Det är precis vad MASSIV+ tillhandahåller.

Båda är B2B-verktyg, men fyller olika funktioner. En EPD *deklarerar* vad en produkt presterar vid ett givet tillfälle och används i upphandling och leverantörsdialog. MASSIV+ skapar ett *operativt flödessystem* där kunder löpande kan se hur stor andel av inkommande utsläpp som är faktabaserade och därigenom rikta krav och incitament mot rätt leverantörer. En leverantör med publicerad EPD har per definition genomfört en verifierad LCA - det är precis den primärdata som gör Coverage-värdet högt i MASSIV+. EPD är input; MASSIV+ är systemet som gör inputens kvalitet synlig längs hela kedjan.

**Räcker det inte med EPDer?**

En vanlig invändning är att MASSIV+ inte behövs eftersom organisationer redan arbetar med att samla in EPDer från sina leverantörer. Argumentet bygger på en missuppfattning: EPDer är värdefull indata, men utgör inget värdekedjesystem. Fem begränsningar gör en ren EPD-strategi otillräcklig:

- **Täckning.** EPDer finns för en bråkdel av en typisk leverantörsbas - framförallt inom bygg där EN 15804 driver fram dem, marginellt i andra sektorer. En EPD-strategi har inget svar för den stora delen av leverantörsspenden där ingen EPD finns.
- **Bakar in det okända i ett samlat värde.** EPD adresserar datakvalitet via metadata (DQR enligt EN 15804, primärdataandelar) och fallback till sekundärdatabaser, men kombinerar detta i ett enskilt rapporterat värde per produkt. MASSIV+:s U/A-distinktion håller i stället okänt och faktiskt strukturellt åtskilt **på värdenivå**, så att andelen kan följas, propageras separat nedströms, och stegvis konverteras till primärdata utan att modellen behöver räknas om.
- **Ingen koherens mellan EPDer.** Olika EPDer använder olika emissionsfaktorer, systemgränser och PCR. Att samla 40 EPDer ger 40 punktdeklarationer, inte en koherent värdekedjebild - och inget strukturellt skydd mot gränsöverlapp eller över-allokering mellan dem.
- **Statisk vs operativ.** En EPD är en ögonblicksbild giltig 3-5 år; MASSIV+ är ett operativt flödessystem där värden uppdateras löpande.
- **Produkttal, inte allokerad motpartsrelation.** En produktspecifik EPD namnger sin utfärdare - den leverantören kan du redan idag välja bort eller premiera. Det EPD-strategin ändå inte ger, hur många deklarationer som än samlas in, är din egen affärs allokerade andel: ett tal bokfört av en namngiven motpart mot just dig och massbalanserat så att samma utsläpp inte kan bokföras mot någon annan. En EPD svarar på "vad bär den här produkten"; MASSIV+ svarar på "vad släppte den här noden ut och hur fördelades det på mig som kund". (Notera att branschgenomsnittliga EPDer inte namnger någon enskild producent alls.)

Den operativa karaktären har en konkret styrningskonsekvens som EPD-strategin saknar. Eftersom Coverage och utsläppsvärden uppdateras löpande kan organisationen sätta **KPI:er för kontinuerlig utsläppsminskning** - år för år eller kvartalsvis om man vill - både för den egna verksamheten och som krav eller incitament mot leverantörer. När en leverantör förbättrar sin primärdata syns effekten omedelbart i mottagarnas nästa rapporteringscykel utan att tidigare rapporter behöver räknas om. Det förvandlar utsläppsdata från en årlig rapporteringsbörda till ett operativt styrinstrument.

EPD och MASSIV+ är därför komplementära och fyller olika funktioner. En leverantör med publicerad EPD bidrar med idealisk primärdata till sin nod, men mottagaren behöver ändå ett system för att hantera leverantörer utan EPD, garantera massbalans, och göra datakvaliteten synlig och styrbar nedströms. Det är vad MASSIV+ tillhandahåller.

| Dimension | EPD / ISO 14025 | MASSIV+ |
|---|---|---|
| Systemtyp | Deklarationsformat | Propageringssystem |
| Miljöpåverkan | Multipla kategorier | Enbart klimat (CO₂e) |
| Verifiering | Tredjepartsverifierad, obligatorisk | Ej specificerat |
| B2B-funktion | Deklarera produktens miljöprestanda | Göra datakvalitet synlig och handlingsbar |
| Relation | EPD-data är idealisk primärindata i MASSIV+-nod | Komplementärt |
