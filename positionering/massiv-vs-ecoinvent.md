# Är en MASSIV+-nod "bara" ett cradle-to-gate-dataset?

*Analys av den ytliga likheten mellan MASSIV+:s nodmodell och processbaserad LCA (ecoinvent).*

---

## Utgångspunkt

Påståendet i dialogen var att MASSIV+:s nodansats är "precis som LCA - varje nod är som cradle-to-gate-data i exempelvis ecoinvent (fast bara med klimat då)". Intuitionen att det finns en skillnad är rätt. Ytlikheten är verklig, men det som *ser likadant ut* är en struktur - en DAG (riktad acyklisk graf, eller med cirkuläritetshanteringen en allmän riktad graf) där varje punkt summerar uppströmsbidrag plus egna aktiviteter. Att två system båda råkar vara grafer säger lika lite som att en organisationsbudget och ett elnät båda är grafer. Det intressanta är vad noderna *representerar*, vad som finns på kanterna, och vad som händer när man uppdaterar en nod.

---

## 1. Vad *är* en nod?

**Ecoinvent:** En nod är ett **unit process** - en beskrivning av en teknologi som producerar en **deklarerad enhet** av en viss produkt (1 kg varmvalsat stål, 1 MJ elektricitet från svensk nätmix, 1 tkm lastbilstransport). Den är definierad av sin *funktionella output*. Värdena är *intensiteter* - per kg, per MJ, per tkm. Processen är en idealiserad representation av en teknologi, ofta ett genomsnitt för en region och tidsperiod.

**MASSIV+:** En nod är en **organisatorisk enhet** - ett företag, en site, en produktionslinje. Den är definierad av sin *organisatoriska avgränsning* (vem äger vad, vilken juridisk person rapporterar). Värdena är *absoluta totaler* för en rapporteringsperiod (totalt Scope 1 i ton CO₂e under 2025, inte per kg produkt).

Det här är en reell skillnad. Det betyder att:

- Ecoinvent kan svara på frågan *"vad kostar 1 kg av den här produkten i utsläpp?"* men inte på frågan *"vad släppte det här bolaget ut förra året?"*
- MASSIV+ kan svara på *"vad släppte det här bolaget ut och hur fördelades det på dess kunder?"* men inte på *"vad är klimatavtrycket per kg av deras produkt X?"* (om inte noden bara gör en produkt).

---

## 2. Vad finns på kanterna?

**Ecoinvent:** Kanten är en **teknisk koefficient** - "för att producera 1 kg stål krävs 0,8 kg järnmalm". Det är en *norm* eller *recept*. Matrisen är A:s teknologikoefficientmatris i Leontief-mening.

**MASSIV+:** Kanten är en **allokeringsandel** av en faktisk leverans - "av nodens totala produktionsvolym gick 30 % till kund X". Det är inte ett recept, utan en bokföring av *vad som faktiskt hände* under rapporteringsperioden.

Den här skillnaden gör något viktigt: i ecoinvent är kedjan deterministisk och produktspecifik, medan i MASSIV+ är kedjan *verksamhetshistorisk och leverantörsspecifik*. Om du byter leverantör förändras din uppströms-siffra i MASSIV+ för att du nu hämtar från en annan nod med egna siffror. I ecoinvent förändras det bara om du väljer ett annat dataset.

---

## 3. Var kommer siffrorna ifrån - och vem äger dem?

**Ecoinvent:** En central organisation samlar, harmoniserar och publicerar datasets. Siffrorna är *tredjepartsproducerade representationer* av branscher, teknologier och regioner. De flesta användare använder samma stål-dataset oavsett vem deras faktiska stålleverantör är.

**MASSIV+:** Siffrorna är *självrapporterade av den faktiska leverantören* i en specifik affärsrelation. Det finns ingen central databas som svarar "vad släpper ett stålverk i genomsnitt ut"; det finns en specifik nod (SSAB Oxelösund, säg) som rapporterar sina faktiska totaler och allokerar dem till sina faktiska kunder.

Detta är den största praktiska skillnaden för användaren. En ecoinvent-kedja är en *modell av branschen*; en MASSIV+-kedja är en *bokföring av dina faktiska affärer*.

---

## 4. Tidsdimensionen

**Ecoinvent:** Datasets uppdateras sällan (versionssläpp varje eller vartannat år). En förändring i verkligheten (en leverantör går över till fossilfri el) syns i din kedja först när ecoinvent släpper en ny version och du väljer att uppdatera till den.

**MASSIV+:** Nodens värde är *per rapporteringsperiod*. När en leverantör byter till fossilfri el syns det direkt i deras egen rapportering - och därmed i din uppströms-siffra i nästa rapporteringscykel. Replacement rule är ett explicit designmoment: systemet är byggt för att ta emot uppdateringar löpande.

---

## 5. Attribution av osäkerhet

**Ecoinvent:** Har datakvalitetsindikatorer (pedigree-matris, lognormal-spridning per flöde) som hanterar osäkerhet *inom* ett dataset. Men när du använder ett dataset i en beräkning försvinner ursprunget; resultatet är en siffra.

**MASSIV+:** A/U-distinktionen är strukturell och propageras hela vägen genom kedjan. Du kan alltid säga "47 % av min uppströms-siffra är baserad på faktisk primärdata från den specifika leverantören, 53 % är okänt". Det är inte ett osäkerhetsspann - det är ett *epistemiskt* påstående om vad som är känt respektive inte känt.

Ecoinvent har ingen motsvarighet. Där *är* allting siffror; osäkerheten är en spridning kring siffran, inte en flagga på att siffran saknar empirisk grund.

---

## 6. Allokeringsproblemet

Båda ramverken måste allokera när en process har flera outputs. Skillnaden:

**Ecoinvent** löser detta metodologiskt en gång för alla: antingen substitution/systemexpansion, allokering efter fysisk egenskap, eller efter ekonomiskt värde - beroende på systemmodell (cut-off, APOS, consequential). Valet är *inbyggt i datasetet*.

**MASSIV+** lämnar valet till noden själv (mass, energi, kvantitet, monetärt) med krav på konsistens. Det är - som den kritiska granskningen redan påpekar - en svaghet: utan normativ vägledning blir allokeringen en strategisk variabel.

---

## 7. Den kategoriska punkten: vad mäter man?

Här finns den djupaste skillnaden:

> **Ecoinvent beskriver en teknologi. MASSIV+ beskriver en verksamhet.**

Ett ecoinvent-dataset för "stål, varmvalsat, europeisk marknadsmix" representerar en *abstraktion* - en syntes av flera producenter, normaliserad till en funktionell enhet. Det har ingen juridisk person, ingen balansräkning, inga kunder.

En MASSIV+-nod för SSAB Oxelösund är en *specifik juridisk enhet* med faktiska kunder, faktisk total volym, och en bokföringsrelation som matchar affärsrelationer. Det är därför internhandel inte är ett specialfall - det är bara en annan nodgräns. Det är också därför konfidentialitet är ett designkrav (i ecoinvent finns det inga kunder att dölja data för; i MASSIV+ finns det kunder som inte ska kunna räkna ut leverantörens marginaler).

---

## Analogi: ecoinvent ≈ nationalräkenskaper, MASSIV+ ≈ balansräkning

Det kan vara värt att använda dubbel bokföring som analogi. Frågan "är inte MASSIV+:s noder samma sak som ecoinvents datasets?" liknar frågan "är inte balansräkningen samma sak som SCB:s nationalräkenskaper?" Båda är finansiella objekt i en nätverksstruktur, båda måste vara konsistenta, båda aggregeras uppåt. Men:

- **Nationalräkenskaperna** (≈ ecoinvent) beskriver *branscher och sektorer* genom aggregering och modellering. De svarar på frågor om struktur och genomsnitt.
- **Balansräkningen** (≈ MASSIV+) beskriver *ett specifikt bolag* genom bokföring av faktiska transaktioner. Den svarar på frågor om just det bolaget.

Den som säger att de är "samma sak" har rätt i att de båda handlar om pengar och har en nätverksstruktur. Men de används till helt olika saker, av helt olika anledningar, och att försöka använda den ena där den andra behövs är en kategoriförväxling.

---

## Vad är då genuint nytt i MASSIV+?

Nodstrukturen i sig är välkänd; det nya - eller åtminstone ovanligt i kombination - är:

1. **Organisationsenheten som bärare** (inte produkten) kombinerat med **propagering** i en kedja - ecoinvent har produkter i en kedja, GHG Protocol har organisationer utan kedjepropagering.
2. **Självrapportering från faktiska parter** som ersättning för centralt modellerade datasets - systemet är federativt snarare än kuraterat.
3. **Strukturell A/U-separation** som propageras hela vägen, inte bara som lokala datakvalitetsflaggor.
4. **Replacement rule** som gör systemet inkrementellt förbättringsbart utan rekonstruktion.

Ingen av dessa för sig är revolutionerande. Kombinationen - och framför allt det medvetna valet att byta centralt objekt från produkt till organisationsenhet - är det som gör MASSIV+ till något annat än "ecoinvent med bara klimat".

---

## Sammanfattande jämförelse

| Dimension | Ecoinvent (processbaserad LCA) | MASSIV+ |
|---|---|---|
| **Vad noden representerar** | Teknologi (unit process) | Organisatorisk enhet (juridisk eller operativ) |
| **Värdets enhet** | Intensitet per deklarerad enhet | Absolut total per rapporteringsperiod |
| **Kantens innebörd** | Teknisk koefficient (recept) | Allokeringsandel av faktisk leverans |
| **Datakälla** | Centralt kuraterad databas | Självrapportering från faktisk leverantör |
| **Specificitet** | Branschgenomsnitt eller teknikrepresentation | Specifik leverantör i specifik affärsrelation |
| **Uppdateringsfrekvens** | Versionssläpp (1-2 år) | Per rapporteringsperiod |
| **Osäkerhetshantering** | Pedigree-matris, lognormal-spridning | A/U-separation propagerad genom kedjan |
| **Allokeringsval** | Inbyggt i datasetmodellen (cut-off/APOS/consequential) | Lämnat till noden, med konsistenskrav |
| **Konfidentialitet** | Inte ett designkrav (inga kunder) | Designkrav (skydd mot inköpsanalys) |
| **Frågor systemet svarar på** | "Vad kostar 1 kg av produkt X i utsläpp?" | "Vad släppte bolaget ut, och hur fördelades det på kunder?" |
| **Frågor systemet *inte* svarar på** | "Vad släppte det här bolaget ut förra året?" | "Vad är klimatavtrycket per kg av produkt X?" |

---

*Källa: MASSIV+ teknisk beskrivning, april 2026 · Birger Löfgren*