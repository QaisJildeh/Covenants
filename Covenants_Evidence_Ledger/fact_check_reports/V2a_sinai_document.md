# V2a: The Sinai Achtiname as a document (Morrow 2013, Ch. 2 pp. 65–98; Ch. 8 Sinai texts I–VI)

Scope: the document itself. That covers its claimed date, scribe, witnesses, handprint and material; the removal of the original; Topkapı; the copies; the Fatimid–Ottoman decrees and fatwas; Napoleon's decree; the travellers; the critics; and the calendar. Out of scope (other agents): the monastery's general history, the mosque, Muhammad's alleged visit, and lifespans of people.

Method. Every verdict below rests on a page I opened, cited by URL in the row and listed in §7. Pages I could not open are marked **Unverified**, with what I tried. Wikipedia is used only as a lead or for uncontroversial dates, and is labelled "(Wikipedia)". Hijri↔Julian conversions were computed with the standard tabular (arithmetical) Islamic calendar and cross-checked against the Aladhan API.

Note: the session's web-search quota ran out partway through. All later work used direct fetches of known URLs and archive.org's own catalogue API. This mainly limited the search for Turkish-language press or museum material on Topkapı (§5, §6).

Book page = printed page. The extract files are `extract/03_ch2.md` and `extract/07_texts.md`.

---

## 0. Calendar check (used throughout)

Tabular Islamic calendar with civil epoch 1 Muharram 1 AH = Friday 16 July 622 (Julian); the astronomical epoch is 15 July. Dates are Julian unless marked "Greg." (proleptic Gregorian, +3 days in the 7th century).

| Hijri date | Tabular (civil) Julian | Proleptic Gregorian | Astronomical-epoch Julian |
|---|---|---|---|
| 1 Muharram 1 AH | Fri 16 Jul 622 | 19 Jul 622 | 15 Jul 622 |
| 3 Muharram 1 AH | 18 Jul 622 | 21 Jul 622 | – |
| 17 Muharram 1 AH | 1 Aug 622 | 4 Aug 622 | 31 Jul 622 |
| 1 Muharram 2 AH | 5 Jul 623 | 8 Jul 623 | 4 Jul 623 |
| **3 Muharram 2 AH** | **Thu 7 Jul 623** | **Thu 10 Jul 623** | 6 Jul 623 |
| 17 Ramadan 2 AH (Badr) | 13 Mar 624 | 16 Mar 624 | – |
| 2 AH runs | 5 Jul 623 – c. 22 Jun 624 | | |
| 1 Muharram 4 AH | 13 Jun 625 | | |
| 1 Muharram 5 AH | 2 Jun 626 | | |

- The Aladhan converter (method "MATHEMATICAL") returns 3 Muharram 2 AH = Thursday **10-07-0623** (Gregorian). That is the same day as Julian 7 July 623. For Gregorian 4 Aug 622 (= Julian 1 Aug 622) it returns **17 Muharram 1 AH**. URLs: https://api.aladhan.com/v1/hToG/03-01-0002 ; https://api.aladhan.com/v1/gToH/04-08-0622
- **Why the date is uncertain.** (a) Tabular dates can differ from the observed crescent by 1–2 days. (b) Before 10 AH the Arabs may still have used intercalation (*nasīʾ*). The number and position of intercalary months between 1 and 10 AH are unknown, so commonly quoted dates "might be in error by one, two, three or even four lunar months" (Wikipedia, "Islamic calendar", https://en.wikipedia.org/wiki/Islamic_calendar). (c) The Hijri era itself was introduced under ʿUmar c. 17 AH/638 (Wikipedia, same page; some sources give 16 AH/637). So any document dated by "year 2 of the Hijra" is either backdated by its writer or later.
- **Bottom line.** "7 July 623" is the conventional Julian equivalent. The TDV İslâm Ansiklopedisi and the Met catalogue (see below) both give it. It is **not** a Gregorian date: the book says "of the Gregorian calendar" (p. 83). The true equivalent may be off by days or even months.

---

## 1. Verification table

Verdict key: **C** = Consistent; **MD** = Minor difference; **I** = Inconsistent; **D** = Disputed among sources; **U** = Unverified; **O** = Opinion.

### A. Date and calendar

| # | Book claim (page) | Verdict | What independent sources say | Source URLs |
|---|---|---|---|---|
| A1 | 3 Muharram 2 AH "corresponds to July 7th, 623 of the Gregorian calendar" (p. 83) | **MD** | Tabular civil date = Thu 7 Jul 623 **Julian** = 10 Jul 623 proleptic Gregorian. TDV "Ahidnâme" gives "3 Muharrem 2 (7 Temmuz 623)". The Met cat. 37 n. 1 says "This corresponds to July 7, 623". The "Gregorian" label is wrong. Uncertainty of days to months is explained in §0. | api.aladhan.com (above); https://islamansiklopedisi.org.tr/ahidname ; Met catalogue (archive.org, §7 #25) p. 64 |
| A2 | Era start "1 Muharram or July 16, 622 CE" (Peters, p. 85) | **C** | Civil epoch = Friday 16 Jul 622 (Julian). The astronomical epoch is 15 Jul. | Wikipedia "Islamic calendar"; own computation |
| A3 | Monastery statement: "In the second year of the Hegira, corresponding to AD 626" (p. 96) | **C** as a quotation; **I** as a conversion | The archived monastery page of 13 Nov 2013 reads exactly "corresponding to AD 626". The current page now says "corresponding to AD 623". 2 AH = Jul 623–Jun 624, and AD 626 falls in 4–5 AH. | https://web.archive.org/web/20131113095907/http://www.sinaimonastery.com/en/index.php?lid=68 ; https://sinaimonastery.com/index.php/en/history/mohammed |
| A4 | Sinai II/III (Arundale 1837; Géramb 1840, both from Mauchin): "3 Moharram, second year of the Hegira, and of J.C. the 1st of August, 622" (pp. 208, 210) | **C** as a quotation; **I** as a conversion | Both 1837 and 1840 texts print "1st of August, 622". In fact 1 Aug 622 = 17 Muharram **1** AH. The year is wrong by about one year, and the day does not match 3 Muharram either. | Arundale https://archive.org/details/illustrationsofj00arun ; Géramb https://archive.org/details/vol2pilgrimageto00gera ; Aladhan gToH |
| A5 | Monks' delegation "in 625 CE, namely, in the second to third year of the hijrah" (p. 70) | **I** (conversion) | 625 CE runs from about 3 AH (Jan–Jun) into 4 AH (from 13 Jun 625). It is not "second to third". The underlying claim (Hobbs 159) is **U** because Hobbs is lending-only. | own computation; Hobbs not openable (archive.org `mountsinai00hobb` is access-restricted) |
| A6 | Hobbs: written by ʿAli "in 623 CE" (p. 76) | **C** (conversion) / **U** (Hobbs text) | 3 Muharram 2 AH falls in July 623. | as A1 |
| A7 | Badr "March 13, 624 CE" (p. 83) | **C** | 17 Ramadan 2 AH = 13 Mar 624 Julian (tabular). | own computation |
| A8 | Abu Hurayrah "joined the Prophet in Medina in the year 7 AH (628/629)" (p. 83) | **C** | TDV (M. Yaşar Kandemir, DİA 10, 1994, pp. 160–167): converted early in year 7 (628) through Ṭufayl b. ʿAmr. He went to Medina in Muharram 7 (May 628) and joined the Prophet at Khaybar. | https://islamansiklopedisi.org.tr/ebu-hureyre |
| A9 | Abu Hurayrah "is also reported to have visited the Prophet in Mecca during the early years" (p. 83) | **U** | No source found. TDV records only the 7 AH conversion and migration. | as A8 |
| A10 | Abu al-Dardaʾ converted "after Battle of Badr in 624" (Mouton, p. 83) | **C** | TDV (A. Aydınlı, DİA 10, 1994, pp. 310–311): "reported to have become Muslim at the time of the Battle of Badr, as the last of the Ansar". | https://islamansiklopedisi.org.tr/ebud-derda |
| A11 | Alternative: Abu al-Dardaʾ converted "one year after the hijrah … 623 CE" (p. 83) | **U** | No source found. The TDV gives only the Badr report. | as A10 |
| A12 | Hijri calendar "only established in 637 by the Caliph ʿUmar" (Mouton, p. 84) | **MD** | Usually 17 AH/c. 638; some sources give 16 AH/637. Either way it postdates 2 AH. | Wikipedia "Islamic calendar" |
| A13 | Witness order "Abu Bakr, ʿUmar, ʿUthman, ʿAli, Muawiyyah fifth" is "suspicious" (p. 85) | **I** (wrong text for this chapter) | The Sinai witness lists printed in the book's own Ch. 8 (Sinai II, III, V, VI) begin with **ʿAli** and contain **no Muʿawiya**. The Pococke/Skrobucha list (I, IV) has no recognisable Muʿawiya either. The Abu Bakr…Muʿawiya order belongs to the 4 AH texts (Christians of the World/Najran), where Muʿawiya is scribe and witness. Muʿawiya became Muslim only at the conquest of Mecca (8 AH/630). | extract/07_texts.md §2 (Sinai I–VI); https://islamansiklopedisi.org.tr/muaviye-b-ebu-sufyan (İ. Aycan, DİA 30, 2020) |
| A14 | (Not claimed by the book; relevant to assessment.) Other Sinai witnesses who were not Muslims in Medina in Muharram 2 AH | — | **al-ʿAbbās b. ʿAbd al-Muṭṭalib**: fought with the Meccans at Badr (Ramadan 2 AH), was captured, and formally professed Islam c. Jan 630 (Wikipedia). **ʿAbd Allāh b. ʿAmr b. al-ʿĀṣ**: migrated to Medina after year 7 (TDV, Kandemir, DİA 1, 1988, pp. 85–86). Both appear in Sinai II/III/V/VI. | https://en.wikipedia.org/wiki/Al-Abbas_ibn_Abd_al-Muttalib ; https://islamansiklopedisi.org.tr/abdullah-b-amr-b-as |

### B. What the document says: scribe, place, witnesses, seal, material

| # | Book claim (page) | Verdict | What independent sources say | Source URLs |
|---|---|---|---|---|
| B1 | The Covenant says it was written by ʿAli, in the Mosque of the Prophet, on 3 Muharram 2 AH (pp. 70, 82, 97) | **C** (as the text's own claim) | Pococke 1743 vol. 1 p. 270: "written by … Ali … the Prophet marking it with his hand at the mosque of the Prophet … second year of the Hegira, the third day of the month Machorem". Burckhardt 1822 p. 547 has the same. The Met cat. 37 (p. 63) translates Shuqayr's Arabic: "written on parchment from Ṭāʾif by the hand of Ali ibn Abi Talib in the mosque of the Prophet". | https://archive.org/details/b30456307_0001 ; https://archive.org/details/b22017355 ; Met (§7 #25) |
| B2 | "The names of twenty-two witnesses" (Burckhardt, p. 82) | **C** | Burckhardt p. 547, verbatim. Lists vary by version: Pococke 16 (p. 270), Géramb 21, Arundale 22. Moritz's apparatus (1918, p. 7 notes) records witnesses **missing in the two dated 16th-c. copies**, so the list varied even then. | Burckhardt (above); Pococke (above); Moritz https://archive.org/details/beitrgezurgesc00moriuoft |
| B3 | Burckhardt: the document "states itself to have been written … in the mosque … at Medina", is "addressed … to all the Christians", and its note says the original "was lost" and this is "copied from a fourth successive copy" (pp. 68, 82) | **C** | Burckhardt pp. 546–547, verbatim. | https://archive.org/details/b22017355 |
| B4 | Handprint "attested to in all of the ancient sources"; Van Egmont & Heyman (fingerprint) are the "sole exception" (p. 75) | **MD** / partly **D** | A hand is reported by Thenaud 1512 ("signez de sa main, plongée en encre"), Affagart 1533/34 ("plongea sa main dedans l'ancre"), Monconys 1647 ("la figure de sa main"), Cantemir ("Palm of his hand"), Burckhardt ("extended hand") and Pococke's text ("marking it with his hand"). But Arundale 1837 has "marks of the Prophet's **fingers**". Chavanon's 1902 summary of Affagart says "l'empreinte des **doigts**". Skrobucha's "two fingers" (book p. 78) is **U**. So there is more than one exception. | Thenaud https://archive.org/details/levoyagedoutreme00then (pp. 72–73); Affagart https://archive.org/details/relationdeterres00affauoft (pp. 190–191 and intro); Monconys https://archive.org/details/voyageenegyptede00monc ; Arundale (A4) |
| B5 | Material: "leather from Ṭāʾif" (scribal note; author: *jild*), "consistent with early prophetic practice" (p. 97) | **D** | Versions differ. **Paper**: Thenaud ("papier"), Affagart ("pappier"), Monconys ("papier"). **Parchment**: Burckhardt; Met (HJS) "parchment from Ṭāʾif". **Gazelle skin**: Stanley 1856; Arundale 1837 ("Cufic characters upon the skin of a gazelle"). **Antelope's skin**: Géramb 1840. The Najran pact in the Chronicle of Seert is "sur une peau de bœuf". | sources in B4; Stanley https://archive.org/details/sinaipalestinein00stan_3 ; PO 13 https://archive.org/details/patrologiaorient13pariuoft p. 601 |
| B6 | "Sidney H. Griffith translated the word as 'parchment' (63)"; Griffith on the tray and green brocade (64); Griffith: confirmed "to … Abdul Hamid II in 1904" (64) (pp. 65, 97–98) | **I** (attribution) / **C** (content) | The Met *Byzantium and Islam* (2012) cat. no. 37, "Achtiname (Testament) of Muhammad", pp. 63–64, is signed **HJS = Hieromonk Justin of Sinai** (contributors list p. xvii). Griffith (SHG) signed cat. 35–36 on the same page. The content quoted by the book is in HJS's entry: tray and green brocade (n. 3: Nektarios 1980, p. 433); confirmations to Abdul Hamid II in 1904 (n. 4: Papamichalopoulos 1932, p. 216). | Met 2012 scan, https://archive.org/details/2012-byzantium-and-islam.-age-of-transition (PDF pp. 17, 84–85) |
| B7 | 1858 Turkish copy with the seal of the Sinai dependency of Canea, Crete, headed "Here is the reason for the writing of this document of eloquent language…" (p. 98) | **C** | Met cat. 37: "Egypt, Sinai, 1858; Ink on paper, bordered by green silk; 70.4 × 38.1 cm; Inscribed: In Turkish, in Arabic script … 'Here is the reason for the writing of this document of eloquent language…'; Provenance: The Sinai Metochion at Canea, Crete … (Turkish scroll no. 4)". | Met (as B6) |

### C. Removal of the original (Selim I in 1517, or later?)

| # | Book claim (page) | Verdict | What independent sources say | Source URLs |
|---|---|---|---|---|
| C1 | Hobbs: "When Ottoman troops occupied Sinai in 1517 … they sent the original firman to the palace of Sultan Selim I in Istanbul", replaced by a displayed copy (pp. 65–66) | **C** (indirect) | Ratliff 2008 p. 14–15 says nearly the same ("sent to the palace of the Sultan Salim I in Istanbul when Ottoman troops occupied Sinai in 1517 and replaced with a copy"), citing Hobbs 158–161. Hobbs himself is lending-only. | https://web.archive.org/web/20150213034339/http://www.saintcatherinefoundation.org/files/8013/2983/0724/Sinaiticus_2008-email.pdf |
| C2 | Monastery statement: in AD 1517 Selim I confirmed the prerogatives and took the original "to the royal treasury in Constantinople", giving "certified copies … each depicting the hand print" (p. 96) | **C** | Archived 2013 page, verbatim. The current page has the same 1517 sentence. | A3 URLs |
| C3 | Tomadakis (16): with Tsernotabey's help the monks met Selim in Cairo in 1517; Selim took the original to Constantinople, "where it must still exist in the archives" (pp. 67–68) | **U** (Tomadakis 1990 not online); substance partly corroborated | Moritz 1918 p. 5 n. quotes Khair Bey's decree of 927 AH (1520/21): "At the time when Sultan Selim was in Egypt (or in Cairo), these old documents were shown to him". Cantemir (1734, Bk III, note 50, which runs over pp. 168–169) frames the whole story as legend ("They say, though fabulously, that Mahomet…"). On **p. 168** it continues: "Long after, when Sultan Selim was in Egypt, the Abbot of Mount Sinai humbly came to him with Mahomet's true or forged Instrument, which the Emperor **purchased** of the Monks for four thousand Gold Crowns". Cantemir thus marks both the story as "fabulous" and the document as "true or forged". The name **Tsernotabey** was not found in any source I opened. Moritz: "Das Original selbst ist verschwunden" (the original itself has disappeared). | Moritz (B2 URL) pp. 5–6; Cantemir https://archive.org/details/dli.ministry.02708 (part 4) |
| C4 | Monconys (Le voyage 92): Selim took it (p. 67) | **C** | Monconys (visit 1647), IFAO ed. reproducing orig. pp. [91]–[92]: "Mahomet signa cette pancarte de la figure de sa main … laquelle Selin Empereur des Turcs leur osta, & l'emporta dans son thresor, aprés leur en avoir laissé une copie". No year is given. | https://archive.org/details/voyageenegyptede00monc |
| C5 | Pococke (148): Selim took it (p. 67) | **C** | Pococke 1743 vol. 1 p. 148: "in their hands to the time of Sultan Selim, who esteeming it too precious a treasure … took it from them, and granted them one under his own hand in the same terms". No year is given. Pococke's text of the Patent (ch. XIV, pp. 268–270) is "translated from the modern Greek". | C5 URL = B1 Pococke |
| C6 | Oumanetz (in Volkoff 128), Skrobucha (57) report 1517 (p. 67) | **U** | Not openable (Skrobucha is lending-only; Volkoff was not found). | — |
| C7 | "every authority has accepted 1517 as the year … (Ratfliff 14-15)" (p. 68) | **I** | Ratliff only reports the tradition and does not survey authorities. Moritz 1918 p. 5: "according to tradition it was taken by Sultan Selim **or his son, Sultan Suleiman**", and Moritz judged Süleyman the most probable remover (see C11). Monconys, Pococke, Burckhardt and Cantemir name Selim but give no year. The earliest explicit "1517" I found is Arundale 1837 (from Mauchin). | Ratliff (C1); Moritz (B2); Arundale (A4) |
| C8 | Atiya (xxix): "The story is circulated that Selim I … took the original … It is also said he gave the monks a certified copy" (p. 74) | **U** (Atiya 1955 is lending-only); substance **C** | Atiya's 1950 booklet: "The existing tradition is that the original charter was taken from the monastery by Sultan Selim I after the Ottoman Conquest of Egypt in 1517. The Sultan, however, gave the monks a copy of it and sanctioned its terms." | https://archive.org/details/dli.ministry.17394 (pp. 11–19 range) |
| C9 | Burckhardt: kept until Selim conquered Egypt; Selim added it to the relics in the imperial treasury and gave a copy "certified with his own cipher … kept in the Sinai convent at Cairo" (p. 81) | **C** | Burckhardt pp. 546–547, verbatim. He adds "I do not believe it to be an authentic document." | B3 URL |
| C10 | "when John Lewis Burckhardt visited the monastery in 1816, he had the opportunity to examine the copy … on display … in all probability … the one dated from 1800/01" (p. 68) | **I** | Burckhardt was at Sinai in spring 1816 (his chapter is headed "in the spring of 1816"). But the copy he says he saw was the one "kept in the Sinai convent **at Cairo**". He gives no date for it. Nothing in his text links it to 1800/01. | B3 URL |
| C11 | Author's hypothesis: if the original was still there in 1533–34, "it may have been taken by Sultan Sulayman the Magnificent" (p. 69) | **O**, already put forward by Moritz 1918 | Moritz pp. 5–6: the surviving copies were made in 957 AH (from Egypt) and 968 AH (from Constantinople), and Süleyman died only in 974 AH, "so ist es höchstwahrscheinlich, daß er es gewesen ist, der diese Urkunden aus dem Kloster hat entführen lassen" (it is most probable that he was the one who had these documents removed). On p. 17 Moritz adds that Süleyman or his representative may have become suspicious of it and "let it disappear". The book cites Moritz for the 16th-c. copies (p. 66) but not for this hypothesis. | B2 URL |
| C12 | Affagart (pilgrimage 1533–34) "certified" the "existence and presence of the original"; he "wrote that the original was still at the mosque" (p. 68) | **C** (translation) / **O** (characterisation) | Affagart (ed. Chavanon 1902, pp. 190–191): the Turks "ont édiffié dedans le monastère une mesquite … dedans laquelle sont les previlleiges que Mahommet donna au monastère. Les religieulx nous disrent…" The book's translation is accurate. But Affagart reports what the monks told him. He neither says he saw the document nor calls it the "original", and the book itself raises this doubt on p. 69. | Affagart URL (B4) |
| C13 | (Not in the book; in user scope.) Thenaud 1512 | — | Jean Thenaud left Angoulême 2 Jul 1511, reached Cairo 25 Mar 1512, and was at the monastery on the vigil of St John (23 June) [1512]. He writes: "Devant ceste église est une musquete de Mores … en laquelle sont les privilèges que Mahommet donna es caloyers, c'est assavoir immunité de tous tributz et devoirs; et sont signez de sa main, plongée en encre et assise sur ledict papier" (ed. Schefer 1884, pp. 72–73). This places a handprinted "privilege" in the mosque **five years before 1517**. | https://archive.org/details/levoyagedoutreme00then |
| C14 | Stanley: taken by Selim and "exchanged for a copy, which, however, no traveller has ever seen"; contract "drawn up on the skin of a gazelle" (pp. 67, 76) | **C** (quotation) | Stanley, *Sinai and Palestine* (1856), verbatim. Note that Burckhardt (1822) had claimed to see the certified copy in Cairo, which contradicts Stanley's statement. | https://archive.org/details/sinaipalestinein00stan_3 |
| C15 | Géramb: the Covenant "had been kept in the Convent of the Holy Transfiguration" (p. 65) | **C** | Géramb 1840 vol. 2 pp. 245–246: original "written in Cufic characters on antelope's skin … now in the Grand Signor's treasury … In 1517, after the conquest of Egypt, Selim I. demanded it, and left in its stead a copy written on parchment and certified by himself". | A4 Géramb URL |
| C16 | Original stored in the "Serrail" (Morison 105–106) / "Seraglio" (Van Egmont & Heyman 161) (p. 69) | **U** | Neither text was found in open full text on archive.org. | — |
| C17 | "the firman of Selim I has actually been located in the Turkish collection" (Atiya xxix) (pp. 74, 98) | **D / U** | Moritz 1918 p. 5: "Auch der Firman Sultan Selims, auf den sich Suleiman bezieht … ist gleichfalls aus dem Kloster verschwunden" (Selim's firman has also disappeared from the monastery). Atiya 1955 (per the book) says it was found later. I could open neither Atiya 1955 nor Schwarz 1970 (Ottoman sultans' documents of Sinai, Halle digitisation behind a bot-check). | B2 URL |
| C18 | Cantemir: exemption in force "till the time of Soliman II, Great-Uncle of the present Emperor, when the Turks began collecting the Haraj … by means of …Mustafa Pasha" (p. 72). The author identifies him as "Grand Vizier Merzifonlu Kara Mustapha Pasha, serving Sulayman II from 1663-1666" | **C** (quotation) / **I** (identification) | Cantemir 1734 (Bk III, n. 50; this part is on **p. 169**, matching the book's citation) names "**Kioprili ogli Mustafa Pasha**", i.e. Köprülüzâde Fâzıl Mustafa Paşa. He became grand vizier on 25 Oct 1689, took the seal at **Edirne/Adrianople** on 8 Nov 1689, and died in 1691. His cizye reform (ferman of Feb 1691) restored per-head collection. Süleyman II reigned 1687–1691. Merzifonlu Kara Mustafa **died in 1683**, before Süleyman II's accession. His posts in the 1660s (deputy/kaymakam, e.g. from 9 May 1666) were under Mehmed IV. | Cantemir (C3 URL); https://islamansiklopedisi.org.tr/kopruluzade-fazil-mustafa-pasa ; https://islamansiklopedisi.org.tr/suleyman-ii ; https://islamansiklopedisi.org.tr/merzifonlu-kara-mustafa-pasa |

### D. Copies at the monastery

| # | Book claim (page) | Verdict | What independent sources say | Source URLs |
|---|---|---|---|---|
| D1 | Six Arabic scroll copies: 1150 AH/1737-38, 1192 AH/1778, 1215 AH/1800-01, three undated (table p. 65; Atiya) | **U** (Atiya 1955 is lending-only; loc.gov returned 403); secondhand **C** | Morrow's own website (an advocacy source) describes the Library of Congress reel "Arabic Firmans 1–48": five Covenant copies dated "1737-1738, 1778, and 1800-1801" plus two undated, and "Scroll 77: Arabic Firmans 961, Addendum" with one more, making six. The Hijri conversions are correct: 1150 AH = May 1737–Apr 1738; 1192 = Jan 1778–Jan 1779; 1215 = May 1800–May 1801. | https://covenantsoftheprophet.org/2017/05/23/the-covenants-of-the-prophet-made-public/ |
| D2 | Codices 695/696 dated "1561 CE (same as 695)" and "1683-1684 CE" (table p. 65) | **C** (secondhand) | The same site says MS **696** = Arabic and Turkish, 1561, and MS **695** = two Arabic copies, 1683–84. This resolves the OCR alignment the extractor could not fix. | as D1 |
| D3 | Oldest copies date from Süleyman's reign; earliest is perhaps 1561 (pp. 66, 68) | **MD** | Moritz 1918 p. 5 knew dated copies of **957 AH (= Jan 1550–Jan 1551, "aus Ägypten")** and **968 AH (= Sep 1560–Sep 1561, "aus Konstantinopel")**, plus an undated copy made in Cairo. So the oldest **dated** copy known to scholarship is 1550/51, not 1561. The 1561 codex probably matches Moritz's 968 AH copy (not confirmed). | B2 URL |
| D4 | 43 Turkish translations (Atiya 80) (p. 66) | **C** (secondhand) | The LOC reel "Turkish Scrolls, Reel 1681" holds "43 copies … in Ottoman Turkish … from the 16th century to the 20th century" (as described on covenantsoftheprophet.org). The Met's 1858 copy is "Turkish scroll no. 4". | D1; Met (B6) |
| D5 | Plate: "Turkish language copy of the Achtiname … from 1638" (p. 222) | **U** | No independent catalogue entry found (Atiya and LOC not openable). 1638 = 1047/1048 AH. | — |
| D6 | Display copy "not dated" but "appears … to date from 1800/01"; "the one … on display … and which was copied by Moritz" (p. 97) | **I** (Moritz link) / **U** (display identity) | Moritz edited the text from **three** copies: the 957 AH and 968 AH copies and one undated Cairo copy (pp. 5–7). None is from 1800/01. No source I opened says which copy is displayed today. Mouton says only that a document with a handprint at its foot is still exhibited "dans l'entrée du monastère". | B2 URL; https://www.clio.fr/BIBLIOTHEQUE/pdf/pdf_le_sinai_medieval_entre_christianisme_et_islam.pdf |
| D7 | Scribal note: copied "from the copy that was copied from the copy written in the handwriting of … ʿAli" (p. 97) | **C** | Moritz p. 5 calls the surviving text "eine tertiäre Abschrift" (a third-generation copy), "in mehreren Exemplaren". Burckhardt's copy said "fourth successive copy". | B2, B3 URLs |
| D8 | All copies "identical in content, the only differences being the official seals, notes…" (pp. 68, 74) | **I** | Moritz's apparatus (pp. 6–8 notes) records textual variants among his three copies, including two witnesses missing from the two dated copies. | B2 URL |

### E. The decrees (Fatimid to Ottoman) and the fatwas

| # | Book claim (page) | Verdict | What independent sources say | Source URLs |
|---|---|---|---|---|
| E1 | Fatimid decrees "as early as 975, 1109, 1110, 1135, 1154, and 1156" (Atiya 26) (p. 71); "the earliest … passed by Fatimid Shiʿite jurists in 975" (p. 71); Pact "confirmed … as early as 975 CE" (p. 73) | **I** for 975, 1109, 1110; **C** for 1135, 1154, 1156 | Heidemann, Müller & Rāġib (*Annales islamologiques* 31, 1997, p. 1) say the monastery holds 81 medieval decrees: "**six remontent à la fin de l'époque fatimide (524/1130 à 553/1158)**". Their n. 2 states that Stern's and Ernst's editions "ont révélé les erreurs dont [l'inventaire d'Atiya] fourmille, de dates et même de dimensions". Stern's Sinai decrees as catalogued by the Princeton Geniza Project: doc. 3 Dhū l-Qaʿda 524 (Oct–Nov 1130); doc. 4 (Istanbul metochion) 3 Rajab 529 (19 Apr 1135); doc. 5 Bahrām (1135–37); doc. 6, 2 Jumādā II 530 (8 Mar 1136); doc. 7 Dhū l-Ḥijja 548 (Feb–Mar 1154); doc. 8 Rabīʿ II 551 (May–Jun 1156); doc. 9, 20 Muḥarram 553 (21 Feb 1158); doc. 10 (Cairo branch) Jumādā II 564 (Mar 1169). Atiya's own 1950 booklet: "the oldest document is dated 524 A.H./1130 A.D." Moritz 1918 p. 4: the series runs "vom Jahre 1134". **No source attests a 975 decree.** (Unconfirmed possibility: 365 AH = 975/76 and 503 AH = 1109/10 may be misread Hijri digits in Atiya's list.) | https://www.aai.uni-hamburg.de/voror/personen/heidemann/medien/heidemann-anislam-1997-sinai.pdf ; https://geniza.princeton.edu/en/documents/41382/ ; …/41383/ ; …/41384/ ; …/41387/ ; …/41388/ ; …/41389/ ; …/41423/ ; …/41438/ ; Atiya 1950 (C8 URL); Moritz (B2) |
| E2 | Al-Ḥāfiẓ's firman of 1134 orders the governor of ʿAqaba/Ayla to honour "the ancient agreements"; "these documents were already ancient" (pp. 79–80; Skrobucha 57–59; Justin 51) | **C** (as reported); **MD** (date) | Moritz p. 4: the oldest surviving document is a firman of al-Ḥāfiẓ (r. 526–544 AH = 1132–1149) ordering the governor of Aila-ʿAkaba to keep "die alten Verträge" (the old treaties). Hieromonk Justin (Met 2012, p. 51): "In 1134, Al-Hafiz … sent a decree to the governor of Ayla … These documents, considered old at the time, must already have existed for some centuries." Moritz found this firman in 1910 at the monastery's **Balat (Istanbul) metochion**. Heidemann n. 6 identifies the Balat document with Stern no. 4, dated 3 Rajab 529 = **19 Apr 1135**. So "1134" (Moritz) and "1135" (Stern; Atiya's list) probably refer to the same item. The firman speaks of "old treaties", **not explicitly** of a letter of the Prophet. | Moritz (B2); Met p. 51 (§7 #25); Heidemann (E1) |
| E3 | Ayyubid decrees 1195, 1199, 1201/02, 1210/11 (p. 71) | **MD / partly I** | Heidemann et al.: three Ayyubid decrees, 592/1195, 595/1199 and 609/1212-13, plus their own published decree of al-Malik al-ʿĀdil of 571/1176 (now in Berlin). Ratliff: an Ayyubid petition of 1212/13 to al-Kāmil. 1201/02 and 1210/11 are not attested there. | E1 Heidemann; Ratliff (C1) |
| E4 | Mamluk decrees 1259, 1260, 1272, 1268/69, 1280, 1516 (p. 71) | **U** (Ernst 1960 not accessible) | Heidemann et al.: 72 Mamluk decrees, edited by Ernst. Ratliff: a 1261 petition to Baybars (Stern 1966). Moritz p. 4: a decree of Qānṣūh al-Ghawrī of 6 Muḥarram 911 (or 921?) AH = 9 Jun 1505 or 20 Feb 1515. That decree is the **earliest Muslim document I found that explicitly names "Schutzschreiben des Propheten"** (letters of protection of the Prophet). | E1; Moritz (B2) |
| E5 | Ottoman decrees "from 1519 to 1818/19"; Ottomans "1517-1805" (pp. 70–71) | **C** (start) / **U** (end) | Moritz p. 4: firmans of Khair Bey of 926 AH (Dec 1519–Dec 1520) and 927 AH, and of Süleyman of 931 AH (1524/25). They refer to the prophetic letter and to "decrees of the (four) orthodox caliphs". End dates were not checked. | B2 URL |
| E6 | Latest edict "issued by Ottoman Sunni scholars in 1888" (p. 71); confirmations to Abdul Hamid II "in 1904" (p. 98) | **U** (1888); **C** (1904, but see B6 on attribution) | The Met cat. 37 (HJS) cites Papamichalopoulos 1932, p. 216 for 1904. Nothing was found for 1888. | Met (B6) |
| E7 | "166 decrees" by Ottoman viceroys; "1,742 Arabic and Turkish firmans … including 210 royal mandates … from twenty-one Ottoman sultans" (Atiya xxxi) (p. 71) | **U** | Atiya 1955 is not accessible. Atiya 1950 gives "more than 2000 pieces … from the twelfth to the nineteenth century". | C8 URL |
| E8 | Atiya (xviii): the covenant, "whether forged or authentic, was renewed by the successive Moslem potentates" (p. 71) | **C** (substance) | Atiya 1950: "the Covenant of the Prophet, whether authentic or forged, was in some way or other renewed". Note that Atiya himself keeps the authenticity question open. | C8 URL |
| E9 | Fatwas from the four Sunni rites (Atiya xxx) "as well as the Fatimid school" (p. 71) | **U** (four rites); **unsupported** (Fatimid school) | The Atiya passage quoted by the book names only the Maliki, Shafiʿi, Hanbali and Hanafi rites. I found no source for fatwas of a "Fatimid school". | — |
| E10 | Oldest Arabic document in the library "perhaps written in 1106" (Digbassanis 361) (p. 68) | **I** (for the decree series) / **U** (Digbassanis) | Atiya 1950: oldest 524/1130. Heidemann/Stern: 524/1130. Moritz: 1134/35. Digbassanis 1990 was not openable. He may mean a different kind of document. | E1 URLs |
| E11 | "542 years" of Muslim access to the original (975–1517) and "371" years of decrees from copies (1517–1888) (p. 71) | **O**, resting on an unattested premise | The arithmetic is right, but 975 is unattested (E1) and 1888 is unverified (E6). | — |

### F. Napoleon's decree

| # | Book claim (page) | Verdict | What independent sources say | Source URLs |
|---|---|---|---|---|
| F1 | Tomadakis: Napoleon "issued a special decree on 8 December, 1798" (p. 70) | **I** | *Correspondance de Napoléon Ier*, vol. 5 (1860), no. 3782 "ORDRE", pp. 219–220: "Quartier général, au Caire, **29 frimaire an VII (19 décembre 1798)**". Both archive.org scans agree, and the next document (no. 3783) carries the same date. 8 December would be 18 frimaire. | https://archive.org/details/correspondancede05napouoft ; https://archive.org/details/correspondancede05naporich |
| F2 | The decree "issued by Napoleon on 19 December 1798" (p. 70) | **C** | as F1 | as F1 |
| F3 | Contents: respect for "the Law of Moses, the Jewish Nation, and the educated inhabitants"; warring Bedouins may not seek asylum; freedom of worship; release from "tribute, taxes, or duty on any goods" (p. 70) | **C** | The decree's preamble cites the tradition of "notre conquête", "respect pour Moïse et la nation juive", and the convent being "habité par des hommes instruits et policés". Art. 1: Bedouins at war may not take refuge in the convent. Art. 2: freedom of worship. Art. 3: no annual duty or tribute "comme ils en ont été exemptés suivant les différents titres qu'ils en conservent". Art. 4: no customs on goods for the convent (incl. silks, satins, produce of Chios and Cyprus). Art. 6: no judicial fees. Art. 7: exemption from grain-export bans. Art. 8: no outside patriarch or bishop has authority over them. | as F1 |
| F4 | The decree "actually confirms the privileges that were granted by the Prophet"; Napoleon "endorsed its authenticity" (p. 70) | **O** (not supported by the text) | The decree does **not** mention Muhammad, the Achtiname or its authenticity. It refers only to "les différents titres qu'ils en conservent" (the various titles they keep). | as F1 |
| F5 | Napoleon helped rebuild the north wall that collapsed "in December, 1798" (Tomadakis) (p. 70) | **U** | Not found among the Sinai items in *Correspondance* vol. 5. Tomadakis was not openable. | — |
| F6 | Fazakerley saw the decree in 1811; *Le Figaro* 1986 article (p. 70) | **U** | Not checked (texts not located). | — |

### G. The critics and what they actually argue

| # | Book claim (page) | Verdict | What independent sources say | Source URLs |
|---|---|---|---|---|
| G1 | Burckhardt: no historian of Muhammad mentions Sinai; the privileges are "totally contrary to history"; "the former is a fable and the latter a forgery" (pp. 81–82) | **C** | Burckhardt pp. 546–547, verbatim. His key point is that the monks' story (given at the convent) is contradicted by the document itself (written at Medina, addressed to all Christians, original lost). | B3 URL |
| G2 | Moritz (via Skrobucha 58–59) disproved it on "date, style, and content": no duties imposed; Christians fix their own taxes; Sinai not named; clauses on women, military service and commerce irrelevant (pp. 78–79) | **C** (checked against Moritz directly; Skrobucha **U**) | Moritz pp. 13–15: genuine letters of protection impose duties, this one grants "die weitgehendsten Vorrechte … ohne irgendwelche Gegenleistung". "Keine muhammedanische Regierung" ever granted Christians self-assessment of tax. "Das Sinai-Kloster wird mit keinem Wort genannt." The Christian-women clause is "ganz unerklärlich", and the military exemption makes no sense for the monastery. | B2 URL |
| G3 | Skrobucha: "this document … may well have originated in Egypt" under al-Hakim (996–1020) (p. 79) | **C** (Moritz) | Moritz pp. 15–17. (a) Origin **outside the monastery**, in Egypt, because of the Egyptian measures *ardabb* and *qadaḥ*. (b) It uses "Sultan", an official title only from 334 AH/945, so it is "nicht vor rund 900". (c) The 1134/35 firman calls it "old", so 900–1000. (d) "perhaps" under al-Hakim (996–1020). Moritz does **not** say the monks forged it. He argues it was **not** made by a member of the monastery for its sole benefit. | B2 URL |
| G4 | Skrobucha: "not a very skilful" forgery, explained by "the Mohammedans' lack of critical sense … and their reverence" (p. 79) | **C** (Moritz) | Moritz p. 17: "Daß die Fälschung besonders geschickt ausgeführt sei, läßt sich nicht behaupten … Nur der Mangel der Muhammedaner an kritischem Sinn in religiösen Fragen sowie ihre Ehrfurcht vor den [Propheten] können diese Erscheinung erklären." | B2 URL |
| G5 | Moritz's "sic" markings suggest "shortcomings were somehow suspicious" (p. 83) | **C** (description) | Moritz's notes treat the forms as vulgar or medieval usage and use them as dating evidence (e.g. "falsche Schreibung … dem ungebildeten Schreiber allein geläufige vulgäre…", "ist mittelalterlich", p. 13). | B2 URL |
| G6 | Moritz's character: German imperial agent and Nazi collaborator; therefore "his scholarship can be dismissed … as propaganda" (pp. 79–80) | **O** (ad hominem; biography not checked) | Not checked; out of scope (other agents). Moritz's textual arguments (G2–G4) stand or fall on the evidence regardless of his politics. They were published in June 1918 by the Prussian Academy (*Abh.* 1918, Nr. 4). | B2 URL |
| G7 | Mouton (177): witnesses Abu Hurayrah and Abu al-Dardaʾ had not yet converted; the hijri calendar did not exist; derived from the 878 Najran letter forged "on the order of the Banu Makhlad" (pp. 82–86) | **U** (Mouton 1998 not online); partial corroboration | Ratliff n. 9: "Since the nineteenth century, scholars have questioned aspects of the document, particularly the list of witnesses; see Mouton, 177." Ratliff n. 11: the Najran letter "seems to have been produced by viziers of the Abbasid period, who were of Nestorian origin and wanted protection for their community" (citing Scher & Griveau 602 n. 1; Massignon 1963). Scher & Griveau (PO 13, p. 602 n. 1): the Najran pact "est certainement apocryphe. Il a été forgé par les chrétiens dans le but d'engager les musulmans à les épargner." The Chronicle of Seert dates the find to 265 AH (= 878–879), from "Habib le moine". Mouton's popular article (Clio) calls the visit story a legitimising "discours" developed "à partir du IXe siècle". | Ratliff (C1); PO 13 https://archive.org/details/patrologiaorient13pariuoft pp. 601–602; Clio (D6) |
| G8 | Ratliff (15): the document "bears close resemblance to … the letter of Muhammad addressed to the Christians of Najrān … discovered in 878 in a monastery in Iraq … preserved in the Chronicle of Séert"; it grants "protection against acts of violence…" (p. 81) | **C** | Verbatim, Ratliff 2008 p. 15. | C1 URL |
| G9 | "Ratliff alleges that Abd al-Masih … had both the linguistic skills and religious knowledge to forge the famous Patent" (p. 81) | **I** (misrepresents the source) / **O** | Ratliff discusses ʿAbd al-Masīḥ (pp. 16–17) in a separate section on Sinai's links with Christians under the Caliphate. She never connects him to the Achtiname. The book admits she does not "say it directly". | C1 URL |
| G10 | ʿAbd al-Masīḥ "martyred in the 860s"; manuscript "9th or 10th century" (p. 81) | **C** / **MD** | Ratliff: "the account and the manuscript [Sinai Ar. 542] are dated to the 9th century". n. 23: "Griffith argues that ʿAbd al-Masīḥ was martyred in the 860s." Four MSS survive, including a lost 10th-c. one and Sinai Ar. 396 (13th c.). | C1 URL |
| G11 | Hobbs: "several observers believe that monks … drafted the original firman … in about 1010 CE" (pp. 73, 75) | **U** | Hobbs is lending-only. The scholarly root of a c. 1000 date is Moritz (900–1000, perhaps al-Hakim), who did **not** attribute it to the monks (G3). | — |
| G12 | Evans (10): Achtiname "given the site in the first years of the Muslim advance across the Sinai Peninsula" (p. 73) | **C** | Met 2012 p. 10: "the Monastery of Saint Catherine at Sinai retains a copy of the *Achtiname*, a promise of protection in the name of the Prophet, given the site in the first years of the Muslim advance across the Sinai Peninsula (cat. no. 37)". | Met (§7 #25) |
| G13 | Hieromonk Justin (51): "These documents, considered old at the time, must have already existed for some centuries" (p. 79) | **C** | Met 2012 p. 51, verbatim (wording "must already have existed"). | Met |
| G14 | Hobbs's book: "Austin: University of Austin Press, 1995" (bibliography) | **MD** | Ratliff cites "Austin: University of Texas Press, 1995". | C1 URL |

### H. Topkapı claims in the book

| # | Book claim (page) | Verdict | What independent sources say | Source URLs |
|---|---|---|---|---|
| H1 | Topkapı's Chamber of Relics "is devoted to the holy artifacts that Selim I brought back from his conquest of Egypt in 1517". It holds the mantle, swords, the Muqawqis letter, beard hairs, soil, a tooth and footprints (p. 69) | **MD / partly I** | TDV "Mukaddes Emanetler" (N. Bozkurt, DİA 31, 2020, pp. 108–111): 605 items in the Sacred Relics department. "An important part" came during and **after** Selim's conquest of Egypt. Others were bought by officials, or sent from Medina by Fahreddin Paşa at the end of the Ottoman Hijaz. Letters held include those to Muqawqis (no. 21/174), al-Mundhir b. Sāwā (21/397), Musaylima (21/169) and al-Ḥārith b. Abī Shamir (21/674). The Muqawqis letter was found only in 1850 (the book's own p. 78), so it cannot be part of Selim's 1517 haul. The official palace page: the Has Oda became known as the Hırka-i Saâdet Dairesi "Yavuz Sultan Selim döneminde kutsal emanetlerin getirilmesinden sonra". | https://islamansiklopedisi.org.tr/mukaddes-emanetler ; https://www.millisaraylar.gov.tr/Lokasyon/2/topkapi-sarayi |
| H2 | The original Achtiname may "remain stored in some forgotten archive, perhaps in the Palace of Topkapi" (p. 69) | **U** / no supporting source | See §5. | §5 |
| H3 | It "eventually went missing from the Treasury in Istanbul"; perhaps destroyed by enemies of *ahl al-bayt* (p. 74) | **O** (speculation) | Moritz 1918 only says it disappeared, and suggests Süleyman or his agent may have had it disappear out of suspicion (G3/C11). | B2 URL |

---

## 2. Timeline comparisons where sources differ

### 2a. Removal of the original

| Source (date written) | Who removed it | When | Where it went | Notes |
|---|---|---|---|---|
| Thenaud (visit June 1512, ed. 1884) | — | — | In the monastery mosque in 1512 | Handprint on "papier". Pre-1517. |
| Affagart (visit 1533–34, ed. 1902) | Not removed; "Turks" offered money and monks refused | — | In the monastery mosque (per the monks) | Does not say he saw it, nor that it was the original. |
| Khair Bey decree, 927 AH = 1520/21 (via Moritz) | — | "when Sultan Selim was in Egypt/Cairo" | "old documents were shown to him" | Shown, not explicitly taken. |
| Monconys (visit 1647) | "Selin" | no year | "son thresor" | Copy left with the monks. |
| Cantemir (written c. 1714–16, publ. 1734), n. 50, p. 168 | Selim "purchased" it for 4,000 gold crowns | while in Egypt (= 1517) | — | Told as a story "They say, though fabulously"; the document is "true or forged". Selim's charter "Given at Cairo". Contrast Affagart, who says the monks **refused** Turkish offers of money. |
| Pococke (1743) | Sultan Selim | no year | — | Granted a copy "under his own hand". |
| Burckhardt (visit 1816, publ. 1822) | Selim I | "when [he] conquered Egypt" | imperial treasury, Constantinople | Certified copy seen **in Cairo**. |
| Arundale (1837), Géramb (1840), both from Mauchin | Selim | **1517** | "possession of the Sultan" / "Grand Signor's treasury" | Earliest explicit "1517" I found. |
| Stanley (1856) | Selim | no year | Constantinople | "if it ever existed". |
| Moritz (1918) | Tradition: Selim **or** Süleyman. Moritz: **Süleyman most probable** | before 974 AH/1566 | "Staatsarchiv von Konstantinopel" (tradition) | Based on copies dated 957 and 968 AH. |
| Atiya (1950) | Selim I | 1517 | — | "existing tradition". |
| TDV "Ahidnâme" (1988) | Yavuz Selim | at the conquest of Egypt | brought to Istanbul | Sent back an Arabic copy + Turkish translation + new ahidname. |
| Hobbs (1995) via Ratliff (2008) | Ottoman troops → Selim I's palace | 1517 | palace in Istanbul | |
| Monastery website (2013 and now) | Selim I | 1517 | royal treasury, Constantinople | Certified copies with handprint. |
| Met 2012 (HJS) | monks presented it to Selim | 1517 | — | tray, green brocade (Nektarios 1980). |
| **Morrow 2013** | Selim (most sources) or **Süleyman** (author's hypothesis) | 1517 or after 1533/34 | Topkapı / other palace? | Süleyman idea already in Moritz 1918. |

### 2b. Earliest attestation of a prophetic covenant for Sinai

| Date | Evidence | Explicitly prophetic? | Source |
|---|---|---|---|
| "from the 9th c." | Legend of the Prophet's visit as a legitimising discourse (Mouton) | legend, not a document | Clio (Mouton) |
| 524/1130 – 553/1158 | Fatimid decrees protecting the monks (Stern docs 3–9; Istanbul and Cairo items) | **No.** The al-Ḥāfiẓ firman speaks of "old treaties" | PGP; Heidemann 1997; Moritz p. 4; Justin (Met p. 51) |
| 911 or 921 AH (1505 or 1515) | Decree of Qānṣūh al-Ghawrī naming "Schutzschreiben des Propheten und Urkunden der Chalifen" | **Yes** (earliest explicit one I found) | Moritz p. 4 |
| June 1512 | Thenaud: privileges of Muhammad with handprint in the mosque | **Yes** (European eyewitness report) | Thenaud pp. 72–73 |
| 926–931 AH (1519–1525) | Khair Bey and Süleyman decrees referring to the Prophet's letter and the "orthodox caliphs'" decrees | **Yes** | Moritz pp. 4–5 |
| 1533–34 | Affagart (monks' account) | **Yes** | Affagart pp. 190–191 |
| **Book's claims**: 975 (Fatimid confirmation), 'Umar's reign (Champdor), 1403 treaty "allusion" | — | 975: not attested in Stern, Heidemann, Moritz or Atiya 1950. Champdor and 1403: not checked here | §1 E1 |

### 2c. Dating of the oldest surviving copies

| Source | Oldest dated copy | Other copies |
|---|---|---|
| Moritz 1918 | 957 AH = 1550/51 (made in Egypt) | 968 AH = 1560/61 (Constantinople); undated Cairo copy |
| Atiya 1955 / LOC (via Morrow's site) | Codex 696, 1561 (Arabic + Turkish) | Codex 695 (1683–84); scrolls 1737/38, 1778, 1800/01, undated; 43 Turkish copies 16th–20th c. |
| Book plate, Ch. 8 | "1638" Turkish copy (unverified) | — |
| Met 2012 | 1858 Turkish copy (Canea) | — |
| **Morrow 2013** | "1561 CE" (with the caveat that undated copies may be older); "from the rule of Süleyman" | display copy "appears … 1800/01" |

### 2d. Napoleon's decree

| Source | Date |
|---|---|
| *Correspondance de Napoléon Ier* vol. 5, no. 3782 | 29 frimaire an VII = **19 Dec 1798**, Cairo |
| Tomadakis (as quoted, p. 70) | 8 Dec 1798 (wrong) |
| Morrow (p. 70) | 19 Dec 1798 (correct) |

### 2e. Hijri-to-CE equivalents for the covenant's date

| Source | Equivalent given | Correct? |
|---|---|---|
| Mauchin → Arundale 1837 / Géramb 1840 | 1 Aug 622 | No (= 17 Muharram **1** AH) |
| Monastery website 2013 | AD 626 | No |
| Monastery website now | AD 623 | Yes |
| Hobbs (via book) | 623 | Yes |
| TDV 1988; Met 2012; Morrow p. 83 | 7 July 623 | Yes as Julian (Morrow wrongly calls it Gregorian) |
| Book p. 70 | 625 = "2nd–3rd year" | No (625 = 3rd–4th year) |

---

## 3. Discrepancies ranked by significance

1. **"Earliest" Fatimid confirmation in 975 (pp. 71, 73) is unsupported.** The specialist editions put the earliest Sinai decrees at 524/1130 (Stern; Heidemann et al. 1997; Atiya's own 1950 booklet), and Moritz 1918 at 1134/35. Heidemann et al. warn that Atiya's 1955 inventory "fourmille" with date errors. This matters because the book's "542 years of access to the original" and "one thousand years of scholarly consensus" arguments rest on 975. In addition, no Fatimid decree I could check mentions the Prophet explicitly. The earliest explicit official reference I found is late Mamluk (Qānṣūh al-Ghawrī, 1505 or 1515; Moritz p. 4).
2. **Witness anachronisms are real and broader than the two names the book discusses.** Abu Hurayra was a Muslim only from 7 AH, and Abu al-Dardaʾ from about Badr (both TDV). In addition, al-ʿAbbās fought for Mecca at Badr, after the covenant's own date (Wikipedia), and ʿAbd Allāh b. ʿAmr b. al-ʿĀṣ came to Medina after 7 AH (TDV). The book's counter-reports (an early Meccan visit by Abu Hurayra; Abu al-Dardaʾ's conversion in 623) have no source. Separately, the book's "suspicious order" argument (Abu Bakr… Muʿawiya, p. 85) applies to the 4 AH covenants, not to the Sinai lists, which start with ʿAli and lack Muʿawiya.
3. **Cantemir's vizier misidentified (p. 72).** Cantemir names Köprülüzâde (Fâzıl) Mustafa Paşa, grand vizier 1689–1691 under Süleyman II, whose 1691 cizye reform fits the episode exactly. The book substitutes Merzifonlu Kara Mustafa (d. 1683) and the dates 1663–1666 (TDV for all three facts).
4. **Misattribution of the Met 2012 catalogue entry (pp. 65, 97–98).** "Griffith 63–64" is cat. no. 37 by **Hieromonk Justin of Sinai** (HJS), not Sidney Griffith. This affects the tray/green brocade story, the "parchment" translation, the 1858 Canea copy and the 1904 Abdul Hamid II claim. The content is quoted accurately; the authority is wrong. It also means the "independent" confirmation is in fact the monastery's own librarian.
5. **Napoleon's decree: date and meaning (p. 70).** The date is 19 Dec 1798, not 8 Dec. More importantly, the text mentions neither the Prophet nor the Achtiname. Saying it "confirms the privileges … granted by the Prophet" and that Napoleon "endorsed its authenticity" is interpretation.
6. **Burckhardt (pp. 68, 81–82).** Burckhardt saw the Selim-certified copy **in the Sinai convent at Cairo**, not a display copy at the monastery. The link to the 1800/01 scroll is the author's assumption.
7. **The Süleyman hypothesis (p. 69) is presented as new, but Moritz 1918 made it**, from copies dated 957 and 968 AH. Moritz also reports that tradition said "Selim **or** Süleyman". The claim "every authority has accepted 1517" (p. 68, citing Ratliff) is therefore wrong. Ratliff only repeats the tradition, and the explicit year 1517 appears in print only from Arundale 1837 / Géramb 1840 among the sources I opened.
8. **Moritz's base text vs the "display copy of 1800/01" (p. 97).** Moritz edited from copies of 957 AH, 968 AH and an undated Cairo copy, not from an 1800/01 display copy. His apparatus also shows variants, including in the witness list, which contradicts "identical in content" (pp. 68, 74).
9. **Ratliff misrepresented (p. 81).** She never links ʿAbd al-Masīḥ to the Achtiname.
10. **Affagart overstated (p. 68).** He relays what the monks said and neither saw nor called it the original. On the other hand, **Thenaud (1512)**, whom the book does not use, independently reports the same handprinted privilege in the mosque five years before 1517. This helps date the document's existence to before the Ottoman conquest; it says nothing about its authenticity.
11. **Ayyubid dates 1201/02 and 1210/11** do not match the edited decrees (592/1195, 595/1199, 609/1212-13; plus 571/1176 in Berlin).
12. **Calendar slips.** "Gregorian" for a Julian date (p. 83). "625 CE = 2nd–3rd year" (p. 70). The monastery's own 2013 "AD 626", which the book reproduces without comment and the monastery has since corrected to 623. Mauchin's "1 August 622" in Ch. 8 texts II–III, which is a year off.
13. **Material and seal unanimity overstated (p. 75).** "All ancient sources" do not agree. Sources variously say paper, parchment, gazelle or antelope skin, or leather from Ṭāʾif, and hand or fingers.
14. **"Fatimid school" fatwas (p. 71)** have no support in the Atiya passage the book quotes.
15. Minor: "1134" vs "1135" for the al-Ḥāfiẓ firman (Moritz vs Stern; probably the same document). Hobbs's publisher is given as "University of Austin Press".

---

## 4. Scholarly assessment of authenticity (both sides)

**What the independent evidence establishes (common ground).**
- **Muslim protection.** From 524/1130 at the latest, Fatimid, Ayyubid, Mamluk and Ottoman authorities repeatedly issued decrees protecting the monastery: 81 medieval decrees survive (Heidemann et al. 1997), and many Ottoman ones. The 1130s al-Ḥāfiẓ firman already appeals to "old treaties" (Moritz p. 4; Justin, Met p. 51).
- **Explicit references to the Prophet.** Explicit reference to a *prophetic* letter appears in the late Mamluk decree of Qānṣūh al-Ghawrī (911/1505 or 921/1515) and in Ottoman decrees of 926–931 AH (Moritz pp. 4–5).
- **European reports.** Thenaud (1512) and Affagart (1533/34) report a handprinted privilege kept in the monastery's mosque.
- **Surviving copies.** All surviving copies are Ottoman-era or later. The oldest dated is 957 AH/1550 (Moritz). Specialists who discuss the text agree that the original is lost or missing.

**Case for authenticity, or for a copy of a lost genuine original.**
- **Who holds it.** The monastery holds it as tradition (website: delegation, handprint, Selim's certified copies), and so does Morrow (2013).
- **Morrow's strongest arguments:**
  - Late copies do not by themselves date a text, and the scribal notes describe a chain of copies.
  - Muslim rulers recognised the privilege continuously, across Sunni and Shiʿi dynasties.
  - The 1130s firman calls the agreements "old".
  - Genuine prophetic letters of protection to Christian and Jewish communities exist as a genre, e.g. Ayla and Maqnā.
  - Dates and witnesses may be later scribal additions to a genuine core.
- **Descriptive treatments.** Hieromonk Justin and Helen Evans (Met 2012) present the Achtiname descriptively as a document "dated to the second year of the hijra" or "given … in the first years of the Muslim advance", without discussing authenticity. These are monastery-affiliated or catalogue framings rather than critical arguments.
- **Qualified "recognition" (not authenticity).** Atiya (1950) expressly leaves the question open: "whether authentic or forged". Stanley (1856) thought the visit "not impossible".
- **Weakness of this side.** No specialist source I opened argues for a 7th-century date on documentary, palaeographic or linguistic grounds. The pro-authenticity case rests on tradition, on continuity of recognition (which proves acceptance, not origin), and on analogy.

**Case for a later composition.**
- **Burckhardt (1822).** No Muslim historian places Muhammad at Sinai, and the privileges (e.g. Muslims helping to rebuild churches) are "contrary to history". The document contradicts the monks' own story: it says it was written at Medina, is addressed to all Christians, and states that the original is lost. He calls the story "a fable" and the document "a forgery".
- **Moritz (1918), the fullest philological critique.**
  - Content: privileges without reciprocal duties, and tax self-assessment unparalleled in Muslim practice.
  - Sinai is not named, and clauses on Christian wives and military service do not fit a monastery.
  - Egyptian measures (*ardabb*, *qadaḥ*) point to an Egyptian origin.
  - The title "Sultan" became official only in 334/945.
  - Vulgar or medieval orthography.
  - Conclusion: composed **c. 900–1000, possibly under al-Ḥākim (996–1020), outside the monastery**, to protect Egyptian Christians and monks; "not particularly skilful".
- **Scher & Griveau (PO 13, 1919), on the sister document (the Najran pact of 878).** "Certainement apocryphe", forged by Christians to induce Muslims to spare them, with each Eastern Christian community keeping its own variant.
- **Mouton (1998, cited by Ratliff 2008 and by Morrow).**
  - Anachronistic witnesses (Abu Hurayra, Abu al-Dardaʾ).
  - A Hijri-year date written before the Hijri era existed (introduced under ʿUmar c. 637/638).
  - "Nothing original": derived from the 878 Najran letter, which Massignon attributed to Nestorian-origin Abbasid viziers (Banu Makhlad).
  - In his popular article, Mouton treats the Prophet's visit as a monastic legitimising discourse from the 9th century.
- **Ratliff (2008).** Reports the tradition and notes the close resemblance to the Najran letter and long-standing doubts about the witness list. She is cautious and does not accuse anyone.
- **TDV İslâm Ansiklopedisi ("Ahidnâme", M. Fayda, 1988), the standard Turkish Islamic reference.** "Bazı hıristiyanlar Hz. Peygamber'e nisbet edilen ahidnâmeler de uydurmuşlardır. Bunların en meşhuru … Saint Catherine Manastırı'nın ahidnâmesidir" ("Some Christians fabricated covenants attributed to the Prophet; the most famous is that of St Catherine's").
- **Additional internal evidence I checked.** The witness list includes people who were not Muslims in Medina in Muharram 2 AH: Abu Hurayra, Abu al-Dardaʾ, al-ʿAbbās and ʿAbd Allāh b. ʿAmr (A8, A10, A14).
- **Ottoman-era doubts.** Köprülüzâde Mustafa Paşa (1689–91) called the "whole Diploma" a forgery, though the Sinai monks kept their exemption (Cantemir p. 169). Cantemir himself calls the instrument "true or forged" and the origin story "fabulous" (p. 168). Moritz suggests Süleyman may have made the original disappear out of suspicion.

**Neutral summary.**
- The scholarly literature I could open (Burckhardt, Moritz, PO editors, Mouton via Ratliff, TDV) treats the Achtiname as a **later composition**. Proposed dates range from the 9th–10th century (Moritz; Mouton's derivation from the 878 Najran letter) to "some time before the 12th-century decrees".
- The monastery and Morrow regard it as a **copy of a lost genuine original**.
- What is securely documented is narrower:
  - a monastic tradition and a handprinted privilege attested by 1512;
  - centuries of Muslim protection, though explicitly tied to a prophetic letter only in late Mamluk and Ottoman decrees;
  - copies from 1550 on.
- None of this proves composition in 623. The internal anachronisms remain unanswered except by the hypothesis that dates and witnesses were added later, a hypothesis Morrow himself adopts (p. 85).

---

## 5. Topkapı: what can be sourced

- **No source I could open says that the Sinai Achtiname (original or copy) is held, catalogued or displayed at Topkapı Palace.**
  - The official Topkapı page of the Millî Saraylar (National Palaces) administration does not mention it. Topkapı has been attached to that administration since Presidential Decree no. 44 of 6 Sep 2019. The page describes the Has Oda / Mukaddes Emanetler Dairesi, called the Hırka-i Saâdet Dairesi after the relics were brought under Yavuz Sultan Selim (https://www.millisaraylar.gov.tr/Lokasyon/2/topkapi-sarayi).
  - The TDV articles "Mukaddes Emanetler" (2020) and "Mukaddes Emanetler Dairesi" (2020) do not mention it either. Their list of the Prophet's letters ("nâme-i saâdetler") in the collection names only four: to **al-Muqawqis** (inv. 21/174), **al-Mundhir b. Sāwā** (21/397), **Musaylima** (21/169) and **al-Ḥārith b. Abī Shamir** (21/674) (https://islamansiklopedisi.org.tr/mukaddes-emanetler ; https://islamansiklopedisi.org.tr/mukaddes-emanetler-dairesi).
  - Nor does the TDV "Hırka-i Saâdet" (1998) article.
- **The TDV "Ahidnâme" (1988) says only that Selim "brought it to Istanbul"** and sent a translated copy back. It says nothing about where the original is today.
- **Moritz (1918) says the original "has disappeared".** Tradition put it in the "Staatsarchiv von Konstantinopel".
- **Practical for a visitor.** The Sacred Relics rooms (Third Court) display the relics named above, including the letter to al-Muqawqis. There is no sourced basis for expecting to see a Sinai Achtiname there. The official page (as fetched 10 Nov 2026) gives the ticket office as 09:00–17:00 and says the palace is **closed on Tuesdays**; check before going.
- **Side note.** A Fatimid decree of the Sinai monastery (al-Ḥāfiẓ, Stern no. 4, 529/1135) was found by Moritz in 1910 at the monastery's **metochion in Balat, Istanbul** (Moritz p. 5 n.; Heidemann n. 6; PGP 41383). Its present location was not determined.
- **Not checked.** The Topkapı museum's own domain (topkapisarayi.gov.tr) did not resolve from this environment, and the web-search quota was exhausted. So I could not search Turkish press or the Topkapı library catalogue for "Sina ahidnamesi". An inquiry to the palace library (Topkapı Sarayı Müzesi Kütüphanesi) would be the way to settle it.

---

## 6. Items not checked, and why

- **Atiya, *The Arabic Manuscripts of Mount Sinai* (1955).** archive.org lending-only (download 401; search-inside unavailable). Its decree list (p. 26), the copy table (pp. 32–35, 80) and the quotes on pp. xviii, xxix–xxxi were checked only indirectly (Atiya 1950; Heidemann; LOC descriptions via Morrow's site).
- **Ernst (1960, Mamluk decrees) and Schwarz (1970, Ottoman decrees).** Digitised at ULB Halle, but behind a bot-check; not circumvented. So the Mamluk years (E4), the Ottoman end-dates (E5–E7) and Selim's firman (C17) are unverified.
- **Hobbs, *Mount Sinai* (1995) and Skrobucha, *Sinai* (1966).** archive.org lending-only. Skrobucha's summary was checked against Moritz directly; Hobbs only via Ratliff.
- **Mouton, "Les musulmans à Sainte-Catherine…" (1998).** No online copy found. Checked via Ratliff's notes, Mouton's Clio article and the PO 13 edition.
- **Stern, "A Fāṭimid decree of the year 524/1130" (BSOAS 1960) and *Fatimid Decrees* (1964).** Not openable. Used the Princeton Geniza Project records (which reproduce Stern's editions and dates) and Heidemann et al.
- **Tomadakis, Digbassanis, Manafis (eds.), *Sinai: Treasures* (1990); Nektarios 1980; Papamichalopoulos 1932.** Not found online.
- **Library of Congress item pages** (Sinai Arabic MSS 695/696, Arabic Firmans reels). HTTP 403 to both WebFetch and curl. Used Morrow's site's description (advocacy source; flagged).
- **Van Egmont & Heyman (1759), Morison (1704), M.L.M.D.C. *Jeux d'esprit* (1697), Fazakerley (1811 visit), *Le Figaro* 1986, Oumanetz/Volkoff, Davenport, Laborde's 1403 treaty, Champdor.** Not located in open full text within the time available.
- **Sanni (2015) review in *JMMA*.** Paywalled. Known only via Wikipedia (lead only).
- **Feridun Bey, *Münşeât-ı Selâtîn*.** Listed in the TDV bibliography, and Morrow's site says it contains the Arabic Sinai text. If so it would be a c. 1575 attestation. Not checked.
- **Moritz's personal and political biography.** Out of scope (other agents).
- **The Met's own website.** Returned HTTP 429. The catalogue was read from the full scan on archive.org, image pages viewed directly.
- **Web-search quota.** Exhausted partway through; later discovery was limited to direct URL fetches and archive.org's catalogue API.

---

## 7. Sources opened (every URL used)

**Calendar**
1. https://api.aladhan.com/v1/hToG/03-01-0002 ; https://api.aladhan.com/v1/gToH/04-08-0622 ; https://api.aladhan.com/v1/gToH/01-08-0622
2. https://en.wikipedia.org/wiki/Islamic_calendar (Wikipedia: epoch, ʿUmar c. 638, intercalation caveat)

**Monastery**
3. https://web.archive.org/web/20131113095907/http://www.sinaimonastery.com/en/index.php?lid=68 (2013: "AD 626")
4. https://web.archive.org/web/2013/http://www.sinaimonastery.com/en/index.php?lid=76 (2013 "Patent of Mohammed" page; snapshot 20131024112120)
5. https://sinaimonastery.com/index.php/en/history/mohammed (current: "AD 623"; read via WebFetch)

**Leads**
6. https://en.wikipedia.org/wiki/Ashtiname_of_Muhammad (lead only)
7. https://en.wikipedia.org/wiki/Al-Abbas_ibn_Abd_al-Muttalib (Wikipedia)

**Atiya, Ratliff, Moritz, Mouton**
8. Atiya, *The Monastery of St. Catherine in Mount Sinai* (Cairo 1950): https://archive.org/details/dli.ministry.17394 (text: …/download/dli.ministry.17394/ignca-s13569-rb_djvu.txt)
9. Ratliff, *Sinaiticus* 2008: https://web.archive.org/web/20150213034339/http://www.saintcatherinefoundation.org/files/8013/2983/0724/Sinaiticus_2008-email.pdf
10. Moritz, *Beiträge zur Geschichte des Sinaiklosters im Mittelalter* (Abh. Preuss. Akad. 1918, Nr. 4): https://archive.org/details/beitrgezurgesc00moriuoft
11. Mouton, "Le Sinaï médiéval, entre christianisme et islam" (Clio): https://www.clio.fr/BIBLIOTHEQUE/pdf/pdf_le_sinai_medieval_entre_christianisme_et_islam.pdf
12. Mouton publications list (EPHE): https://www.ephe.psl.eu/sites/default/files/2021-12/Publications%20Mouton.pdf

**The decrees**
13. Heidemann, Müller, Rāġib, *Annales islamologiques* 31 (1997): https://www.aai.uni-hamburg.de/voror/personen/heidemann/medien/heidemann-anislam-1997-sinai.pdf
14. Princeton Geniza Project, Sinai Fatimid decrees: https://geniza.princeton.edu/en/documents/41382/ , /41383/ , /41384/ , /41387/ , /41388/ , /41389/ , /41423/ , /41438/

**Napoleon**
15. *Correspondance de Napoléon Ier* vol. 5: https://archive.org/details/correspondancede05napouoft ; https://archive.org/details/correspondancede05naporich

**Travellers and early writers**
16. Affagart, *Relation de Terre Sainte* (ed. Chavanon 1902): https://archive.org/details/relationdeterres00affauoft
17. Thenaud, *Le voyage d'outremer* (ed. Schefer 1884): https://archive.org/details/levoyagedoutreme00then
18. Monconys, *Voyage en Égypte 1646–1647* (IFAO 1973): https://archive.org/details/voyageenegyptede00monc
19. Pococke, *A Description of the East* vol. 1 (1743): https://archive.org/details/b30456307_0001
20. Burckhardt, *Travels in Syria and the Holy Land* (1822): https://archive.org/details/b22017355
21. Stanley, *Sinai and Palestine* (1856): https://archive.org/details/sinaipalestinein00stan_3
22. Cantemir, *History of the Growth and Decay of the Othman Empire* (Eng. 1734; DLI scan): https://archive.org/details/dli.ministry.02708 (also the poor-OCR 1756 ed.: https://archive.org/details/bim_eighteenth-century_the-history-of-the-growt_dimitrie-cantemir-voivo_1756)
23. Géramb, *Pilgrimage to Jerusalem and Mount Sinai* vol. 2 (1840): https://archive.org/details/vol2pilgrimageto00gera
24. Arundale, *Illustrations of Jerusalem and Mount Sinai* (1837): https://archive.org/details/illustrationsofj00arun

**Catalogues and editions**
25. Evans & Ratliff (eds.), *Byzantium and Islam: Age of Transition* (Met 2012), scan: https://archive.org/details/2012-byzantium-and-islam.-age-of-transition (pp. xvii contributors; 10 Evans; 51 Justin; 63–64 cat. 37 by HJS)
26. *Patrologia Orientalis* 13 (Chronique de Séert II): https://archive.org/details/patrologiaorient13pariuoft (pp. 601–602)

**TDV İslâm Ansiklopedisi**
27. TDV articles:
    - https://islamansiklopedisi.org.tr/ahidname (M. Fayda, DİA 1, 1988, 535–536)
    - …/mukaddes-emanetler (N. Bozkurt, DİA 31, 2020, 108–111)
    - …/mukaddes-emanetler-dairesi (Bozkurt & Yavaş, DİA 31, 2020, 111–114)
    - …/hirka-i-saadet (N. Atasoy, DİA 17, 1998, 374–377)
    - …/ebu-hureyre (Kandemir, DİA 10, 1994)
    - …/ebud-derda (Aydınlı, DİA 10, 1994)
    - …/abdullah-b-amr-b-as (Kandemir, DİA 1, 1988)
    - …/muaviye-b-ebu-sufyan (Aycan, DİA 30, 2020)
    - …/suleyman-ii (Özcan, DİA 38, 2010)
    - …/kopruluzade-fazil-mustafa-pasa (Özcan, DİA 26, 2002)
    - …/merzifonlu-kara-mustafa-pasa (Özcan, DİA 29, 2004)
    - …/takvim (Akgür, DİA 39, 2010; no ʿUmar date found)

**Topkapı**
28. Millî Saraylar, Topkapı Sarayı: https://www.millisaraylar.gov.tr/Lokasyon/2/topkapi-sarayi
29. https://muze.gen.tr/muze-detay/topkapi (unofficial guide; opened, not relied on); https://muze.gov.tr/muze-detay?SectionId=TSM01&DistId=MRK (opened; no relevant text)

**Advocacy source**
30. covenantsoftheprophet.org (Morrow's site), LOC descriptions: https://covenantsoftheprophet.org/2017/05/23/the-covenants-of-the-prophet-made-public/

**Attempted, not usable:**
- loc.gov/item/00279388963-ms and 00279389153-ms (403)
- topkapisarayi.gov.tr (DNS failure)
- metmuseum.org publications page (429)
- opendata.uni-halle.de and relbib.de (bot-check)
- archive.org Atiya 1955 / Hobbs 1995 / Skrobucha 1966 (lending-only)
- libcat.wellesley.edu (403)
- research.kwaretech.com (no content)
