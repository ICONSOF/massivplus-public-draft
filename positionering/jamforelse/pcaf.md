# MASSIV+ och PCAF

> Del av [Jämförelse med andra ramverk](../jamforelse-med-andra-ramverk.md) - översiktstabell och sammanfattande positionering finns där. Ny här? Läs [introduktionen](../../introduktion.md) först.

PCAF är finanssektorns standard för financed emissions. Den representerar en egen kategori i landskapet: en portföljallokeringsmetod som behöver kunddata MASSIV+ kan leverera.

---

## MASSIV+ vs. PCAF

PCAF (Partnership for Carbon Accounting Financials) är finanssektorns standard för att mäta utsläpp kopplade till lån, investeringar och försäkringar. Tredje utgåvan (december 2025) täcker tio tillgångsklasser - bland dem listed equity och corporate bonds, business loans och unlisted equity, project finance, commercial real estate, mortgages, motor vehicle loans, sovereign debt, samt nya tillägg som securitizations och use-of-proceeds-strukturer. Standarden fördelar låntagarens eller investeringsobjektets utsläpp till finansiella aktörer proportionellt mot deras finansieringsandel via en *attribution factor* - outstanding amount dividerat med total equity + debt för onoterade bolag, eller med EVIC (Enterprise Value Including Cash) för noterade. Resulterande "financed emissions" är vad finansiella aktörer rapporterar som sin Scope 3 kategori 15.

Sedan 2025-rapporter krävs att finansiella aktörer rapporterar låntagarens Scope 1, Scope 2 *och* Scope 3 - genomgående för alla sektorer. PCAF har ett eget data quality score (1-5): score 1 är tredjepartsverifierade rapporterade utsläpp, score 2 är oberverifierade rapporterade utsläpp, score 3 är primärdata på fysisk aktivitetsnivå, och score 4-5 är sektor- eller spend-baserade EEIO-schabloner. PCAF erkänner explicit att scope 3-datakvaliteten "varierar kraftigt per sektor och datakälla". I praktiken landar de flesta bank-PCAF-värden idag på score 4-5.

MASSIV+ adresserar exakt det data-gap PCAF kämpar med. Standarden producerar verifierbar primärdata med Coverage-mått hos låntagaren eller investeringsobjektet, vilket banken kan använda direkt som indata till sin PCAF-beräkning. En oberverifierad MASSIV+-deklaration motsvarar konceptuellt PCAF score 2 (unverified reported emissions); med tredjepartsverifiering nås score 1. PCAF tillhandahåller *attribution-metoden* (hur banken fördelar kundens utsläpp till sin portfölj); MASSIV+ tillhandahåller *kunddatan* (vad kundens utsläpp är, med transparent datakvalitet). De är komplementära - PCAF förblir bankens standard för portföljallokering, medan MASSIV+ kan höja datakvaliteten på de underliggande emissionsvärdena från EEIO-schabloner (PCAF score 4-5) till primärdata-grundade rapporter (score 1-2).

| Dimension | PCAF | MASSIV+ |
|---|---|---|
| Centralt objekt | Finansiell portfölj | Värdekedjenod |
| Räckvidd | 10 tillgångsklasser (lån, investeringar, försäkringar) | Värdekedjenoder (alla branscher och organisationsstorlekar) |
| Allokeringsmetod | Attribution factor (finansieringsandel) | Massbalans + allokeringsregel per nod |
| Datakällor | Kundens egna data, fallback till EEIO/spend-baserade schabloner | Standardiserad Scope 1+2 + propagering nedifrån |
| Datakvalitetsmått | PCAF data quality score (1-5) | Coverage = A/(A+U) |
| Relation | PCAF är bankens portföljmetod | MASSIV+-data kan vara primärinput till PCAF (höjer score 4-5 till 1-2) |
