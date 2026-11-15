# V7c — People's dates in Morrow, *The Covenants of the Prophet Muhammad with the Christians of the World* (2013): Chapter 2 (Sinai) and Part III

**Input:** `people/people_batch2.md`. It has 196 rows, numbered 1–196 in file order:

- rows 1–65 come from extract `03_ch2`;
- rows 66–196 come from extract `08_ch13_ch17`.

Checked 10 Nov 2026.

**Method.** Every verdict rests on a page or API record that I opened in this session. Search-engine snippets were not used, and no WebSearch call was made. The sources:

- **TDV İslâm Ansiklopedisi.** Full article text was fetched and the birth, death and conversion passages were read.
- **GND authority records.** Each cited ID was re-fetched individually as `https://lobid.org/gnd/<id>.json`.
- **BnF authority and bibliographic records,** read through the BnF SRU API. They are cited by ark.
- **Wikidata entity JSON.** References are given for each date claim.
- **Primary texts,** fetched by me from archive.org and Gutenberg:
  - Arundale's *Illustrations*;
  - Walpole's *Travels* (1820), which contains Fazakerley's account;
  - Burckhardt's *Travels in Syria*;
  - *Patrologia Orientalis* 13 (Chronicle of Seert).
- **English, French and Hebrew Wikipedia, and English Wikisource,** used only where noted. These are labelled "Wikipedia-level".

The printed wording of disputed items was checked against the book's own page text in `book/pages` and `book/book.txt`.

**Grading.**
- **AH→CE overlap.** A Hijri year spans two CE years, so a one-year difference caused by that overlap is graded **Minor difference**.
- **Approximate dates.** A date marked "c." that lies within about 3 years of the reference is also **Minor difference**. Larger gaps are **Inconsistent**.
- **Before marking Inconsistent,** a second independent source was checked in every case.
- **Rows with two printings.** Where the book prints the same person twice and one printing is right and the other wrong, the row is graded **Inconsistent** and the reference column explains which printing is wrong.

**Access limits.**
- The Wikidata Query Service was rate-limited to 1 request/min, and the `wbgetentities` API returned HTTP 429. Wikidata was therefore read entity by entity through `Special:EntityData`.
- The Library of Congress and HathiTrust returned 403.
- No TDV entry was found for 'Abbas ibn 'Abd al-Muttalib, Hisham ibn al-'As, Sahl ibn Sa'd, al-Mu'tamid, al-Mutawakkil or Jaqmaq. Other sources were used for these.

**Deaths after publication (not errors).** Lewontin (2021), F. E. Peters (2020), Bernard Lewis (2018), Patricia Crone (2015), Qaradawi (2022), Robert Irwin (2024) and John Adair (2025). Juan Vernet died in 2011, *before* the book appeared; the book gives only "b. 1923".

URL shorthand used in the table:

| Shorthand | Expands to |
|---|---|
| TDV:slug | https://islamansiklopedisi.org.tr/slug |
| GND:id | https://lobid.org/gnd/id.json |
| BnF:cb… | https://catalogue.bnf.fr/ark:/12148/cb… |
| WD:Q… | https://www.wikidata.org/wiki/Q… (data read from Special:EntityData/Q….json) |

## 1. Row-by-row table

| # | Name | Book's dates (page) | Verdict | Reference dates | Source URL(s) |
|---|---|---|---|---|---|
| 1 | Marie-Joseph de Géramb | 1772–1848 (p. 65) | **Consistent** | 17 Apr 1772 – 15 Mar 1848 (BnF); GND 1772–1848 | https://catalogue.bnf.fr/ark:/12148/cb107464927 ; https://lobid.org/gnd/117536334.json |
| 2 | Aziz S. Atiya | 1898–1988 (pp. 66, 71, 74) | **Consistent** | GND 1898–1988; Wikidata 5 Jul 1898 – 24 Sep 1988 (citing BnF) | https://lobid.org/gnd/128054093.json ; https://www.wikidata.org/wiki/Q733934 |
| 3 | Sulayman the Magnificent | r. 1520–1566 (pp. 66, 68, 69) | **Consistent** | Sultan 1520–1566, d. 974/1566 (TDV); GND "regierte 1520-1566" | https://islamansiklopedisi.org.tr/suleyman-i ; https://lobid.org/gnd/118619993.json |
| 4 | Homer | "8th century BCE" (p. 66) | **Consistent** | This is the conventional dating only. Wikidata: born 9th c. BCE (citing BnF), death 8th c. BCE (citing GND) | https://www.wikidata.org/wiki/Q6691 |
| 5 | Richard C. Lewontin | b. 1929 (p. 66) | **Consistent** | GND 1929–2021 | https://lobid.org/gnd/12215293X.json |
| 6 | Balthasar de Monconys | 1611–1665 (p. 67) | **Disputed among sources** | Death 28 Apr 1665 is agreed. Birth: BnF 1608 and GND 1 Mar 1608 (both current records). Wikidata holds both 1611 (older catalogue imports: ULAN, RKD, Open Library etc.) and 1 Mar 1608 (Dictionnaire historique de Lyon) | https://catalogue.bnf.fr/ark:/12148/cb13333954v ; https://lobid.org/gnd/120669501.json ; https://www.wikidata.org/wiki/Q2262911 |
| 7 | Richard Pococke | 1704–1765 (pp. 67, 69) | **Consistent** | 19 Nov 1704 – 25 Sep 1765 (GND); BnF 1704–1765 | https://lobid.org/gnd/11768757X.json ; https://catalogue.bnf.fr/ark:/12148/cb12462693b |
| 8 | Dean Arthur (Penrhyn) Stanley | 1815–1881 (pp. 67, 76) | **Consistent** | 13 Dec 1815 – 18 Jul 1881 (GND) | https://lobid.org/gnd/117211931.json |
| 9 | Greffin Affagart | c. 1490 or 1495 – c. 1557; pilgrimage 1533–34 (pp. 68, 69) | **Consistent** | fr.wikipedia: "né vers 1490 ou 1495, décédé vers 1557"; *Relation* written 1533/1534. Wikidata has the same, citing fr.wikipedia. Wikipedia-level only; no GND or BnF authority record exists | https://fr.wikipedia.org/wiki/Greffin_Affagart ; https://www.wikidata.org/wiki/Q3116171 |
| 10 | J. L. Burckhardt | 1784–1817; visited 1816; died aged 32 (pp. 68, 81, 82) | **Consistent** | 25 Nov 1784 – 15 Oct 1817 (GND; BnF), so he died aged 32. His *Travels in Syria* contains a "Journal of a Tour in the Peninsula of Mount Sinai, in the Spring of 1816" | https://lobid.org/gnd/118702203.json ; https://catalogue.bnf.fr/ark:/12148/cb12434306m ; https://www.gutenberg.org/cache/epub/8884/pg8884.txt |
| 11 | Imam 'Ali | d. 661 (pp. 68–97) | **Consistent** | d. 40/661; caliph 656–661 (TDV); GND 600–661 | https://islamansiklopedisi.org.tr/ali ; https://lobid.org/gnd/118846582.json |
| 12 | Sultan Selim I | r. 1512–1520 (p. 69) | **Consistent** | Sultan 1512–1520, d. 926/1520 (TDV); GND "regierte ab 1512", d. 1520 | https://islamansiklopedisi.org.tr/selim-i ; https://lobid.org/gnd/122789148.json |
| 13 | Ibn Sa'd | d. 845 (pp. 69, 77) | **Consistent** | d. 230/845 (TDV); GND 784–845 | https://islamansiklopedisi.org.tr/ibn-sad ; https://lobid.org/gnd/119181118.json |
| 14 | Napoleon I | 1769–1821 (p. 70) | **Consistent** | 15 Aug 1769 – 5 May 1821 (GND) | https://lobid.org/gnd/118586408.json |
| 15 | Fatimids | r. 901–1171 (p. 70) | **Inconsistent** | 909–1171 (TDV: "909-1171 yılları arasında"; Wikidata 909–1171). The start date is 8 years too early | https://islamansiklopedisi.org.tr/fatimiler ; https://www.wikidata.org/wiki/Q160307 |
| 16 | Ayyubids | r. 1174–1249 (p. 70) | **Disputed among sources** (definitional) | Usual dating is 1171 (Wikidata; TDV: dynasty 1171–1462 counting all branches). The book's end points match real events in TDV: Nur al-Din d. 569/1174, which made Saladin independent; al-Salih Ayyub d. 23 Nov 1249. But Turan Shah became sultan on 1 Feb 1250, so Ayyubid rule in Egypt ran to 1250 | https://islamansiklopedisi.org.tr/eyyubiler ; https://www.wikidata.org/wiki/Q180114 |
| 17 | Mamluks | "12501517" (p. 70) | **OCR issue** | Reads as 1250–1517, which matches Wikidata 1250–1517 | https://www.wikidata.org/wiki/Q282428 |
| 18 | Ottomans (in Egypt) | 1517–1805 (p. 70) | **Disputed among sources** (definitional) | The conquest of 1517 is correct (TDV Selim I). Muhammad Ali was appointed governor on 3 Jul 1805 (TDV). The Egypt eyalet formally lasted until 1867 (Wikidata, from enwiki). So 1805 is the start of Muhammad Ali's rule, not the end of Ottoman sovereignty | https://islamansiklopedisi.org.tr/kavalali-mehmed-ali-pasa ; https://www.wikidata.org/wiki/Q491507 |
| 19 | Demetrius Cantemir | 1673–1723 (p. 72) | **Consistent** | 26 Oct 1673 – 21 Aug 1723 (GND). Wikidata also has 1674 (EB-11) and an older death year of 1726 | https://lobid.org/gnd/118518879.json ; https://www.wikidata.org/wiki/Q159933 |
| 20 | Merzifonlu Kara Mustafa Pasha | "served Sulayman II from 1663-1666" (p. 72) | **Inconsistent** | b. 1044/1634-35, d. 1095/1683 (TDV). Career (TDV): kapudan pasha 1661–1666; acting grand vizier (kaymakam) during the 1663 Uyvar campaign and again from 9 May 1666; grand vizier from 5 Nov 1676. All of this was under **Mehmed IV** (r. 1648–1687, TDV). Suleiman II reigned 1687–1691, after Kara Mustafa's death. The years fit his career; the sultan is wrong | https://islamansiklopedisi.org.tr/merzifonlu-kara-mustafa-pasa ; https://islamansiklopedisi.org.tr/mehmed-iv ; https://lobid.org/gnd/118585975.json |
| 21 | Mu'awiya ibn Abi Sufyan | d. 680 (p. 72); 602–680 (p. 85) | **Consistent** | b. 602 or 603 in Mecca, d. 60/680 (TDV); BnF 603?–680; GND 605–680 | https://islamansiklopedisi.org.tr/muaviye-b-ebu-sufyan ; https://catalogue.bnf.fr/ark:/12148/cb13555700m ; https://lobid.org/gnd/119217481.json |
| 22 | Caliph 'Umar ibn al-Khattab | r. 634–644; 579–644 (pp. 73, 76, 84, 85, 97) | **Disputed among sources** (birth) | Reign 634–644 and d. 23/644 (TDV) are correct. Birth estimates vary: TDV, about 13 years after the Year of the Elephant (≈583) or 4 years before the Great Fijar; BnF 581?; GND 568; Wikidata c. 586 (Britannica). **No source checked gives 579** | https://islamansiklopedisi.org.tr/omer ; https://catalogue.bnf.fr/ark:/12148/cb11939742h ; https://lobid.org/gnd/118822810.json ; https://www.wikidata.org/wiki/Q8467 |
| 23 | Francis Arundale | 1807–1853; "voyage to Sinai in 1831" (p. 74) | **Inconsistent** (voyage year) | Life dates are correct: 9 Aug 1807 – 9 Sep 1853 (Wikidata, citing RKD and Benezit). The trip date is not. Arundale's own *Illustrations of Jerusalem and Mount Sinai* (1837) says the caravan left Cairo for Sinai on "the 29th of August, 1833". Wikipedia (after the DNB): he went to Egypt with Hay in 1831 and toured the Holy Land in 1833 | https://www.wikidata.org/wiki/Q5480030 ; https://archive.org/download/illustrationsofj00arun/illustrationsofj00arun_djvu.txt ; https://en.wikipedia.org/wiki/Francis_Arundale |
| 24 | Caliph al-Hakim | r. 996–1021 (author); 996–1020 (Skrobucha quote) (pp. 75, 79) | **Consistent** | Caliph 996–1021, d. 411/1021 (TDV); Wikidata 19 Oct 996 – Feb 1021. The quoted 1020 is a one-year slip | https://islamansiklopedisi.org.tr/hakim-biemrillah ; https://www.wikidata.org/wiki/Q342137 |
| 25 | al-Afdal | "the Fatimid Caliph al-Afdal", "al-Hakim's successor", reigning c. 1106 (p. 75) | **Inconsistent** (title/succession) | al-Afdal Shahanshah was a vizier and army commander, not a caliph: d. 515/1121 (TDV); vizier 1094–1121 (Wikidata). The caliph in 1106 was al-Amir (r. 1101–1130, TDV). Al-Hakim's successor was al-Zahir (r. 1021–1036, Wikidata). The book itself calls al-Afdal "a powerful chancellor" (p. 75, from Skrobucha). The year 1106 does fall within his vizierate | https://islamansiklopedisi.org.tr/efdal-b-bedr-el-cemali ; https://islamansiklopedisi.org.tr/amir-biahkamillah ; https://www.wikidata.org/wiki/Q1740272 |
| 26 | al-Hafiz | 1132–49; firman 1134 (p. 79) | **Consistent** | Regent from Oct 1130, caliph from 1132, d. 1149 (enwiki); TDV "1131-1149", d. 544/1149 | https://en.wikipedia.org/wiki/Al-Hafiz_li-Din_Allah ; https://islamansiklopedisi.org.tr/hafiz-lidinillah |
| 27 | Mamluk Sultan Jakmak (Jaqmaq) | 1438–53; acted 1442 (p. 79) | **Consistent** | Reigned 9 Sep 1438 – 1 Feb 1453 (enwiki); Wikidata: Mamluk sultan 1438–1453 | https://en.wikipedia.org/wiki/Sayf_ad-Din_Jaqmaq ; https://www.wikidata.org/wiki/Q647942 |
| 28 | Leo Frobenius | 1873–1973 (p. 79) | **Inconsistent** | 29 Jun 1873 – 9 Aug 1938 (GND; Wikidata citing BnF, Britannica, Brockhaus). The death year is 35 years off | https://lobid.org/gnd/11869376X.json ; https://www.wikidata.org/wiki/Q60570 |
| 29 | Stephen (Suleyman) Schwartz | b. 1948 (p. 80) | **Consistent** | b. 9 Sep 1948 (GND; Wikidata citing BnF; the Wikidata item is now labelled "Lulu Schwartz") | https://lobid.org/gnd/124471684.json ; https://www.wikidata.org/wiki/Q7610618 |
| 30 | 'Abd al-Masih al-Najrani (Qays/Rabi' al-Ghassani) | "martyred in the 860s" (Griffith) (p. 81) | **Unverified** | Confirmed only to the century: Wikipedia says he "died in the 9th century". Griffith's article (*Le Muséon* 98, 1985) has no online abstract, so the 860s could not be checked | https://en.wikipedia.org/wiki/Qays_al-Ghassani ; https://doi.org/10.2143/mus.98.3.2011489 |
| 31 | Abu Hurayrah | 603–681; "joined the Prophet in Medina in 7 AH (628/629)" (p. 83) | **Inconsistent** (death) | Arrival is correct: he went to Medina in Muharram 7 AH (May 628) (TDV). Death: 58/678 aged about 78, also reported as 57/677 or 59/679 (TDV); GND 602–679; BnF 601?–677?; Wikidata 676–679. **No source gives 681** | https://islamansiklopedisi.org.tr/ebu-hureyre ; https://lobid.org/gnd/118966863.json ; https://catalogue.bnf.fr/ark:/12148/cb16245619f |
| 32 | Abu al-Darda' | converted "after Badr in 624" (Mouton) or "one year after the hijrah, 623" (p. 83) | **Disputed among sources** | TDV: he is said to have become Muslim "during the Battle of Badr, the last of the Ansar" to do so. Badr was in Ramadan 2 AH (Mar 624), which supports 624. No source checked supports 623 | https://islamansiklopedisi.org.tr/ebud-derda |
| 33 | Tabari | d. 923 (p. 77) | **Consistent** | d. 310/923 (TDV); GND 839–923 | https://islamansiklopedisi.org.tr/taberi-muhammed-b-cerir ; https://lobid.org/gnd/118620436.json |
| 34 | Wahb ibn Munabbih | 655–732 (p. 78) | **Consistent** | b. 34/654-55; d. Muharram 114 / Mar 732 (TDV; variants 110, 113, 116 AH); BnF 654–732; GND 654–728 | https://islamansiklopedisi.org.tr/vehb-b-munebbih ; https://lobid.org/gnd/113168195.json |
| 35 | Ibn 'Abbas | 619–687 (p. 78) | **Consistent** | b. about 3 years before the Hijra; d. 68/687-88 (TDV); GND 619–687 | https://islamansiklopedisi.org.tr/abdullah-b-abbas ; https://lobid.org/gnd/118925857.json |
| 36 | Ka'b al-Ahbar | d. 652 (p. 78) | **Consistent** | d. 32/652-53 [?] (TDV) | https://islamansiklopedisi.org.tr/kab-el-ahbar |
| 37 | al-Saffah | "between 750-754" (p. 78) | **Consistent** | First Abbasid caliph 750–754, d. 136/754 (TDV) | https://islamansiklopedisi.org.tr/ebul-abbas-es-seffah |
| 38 | Ibn Qutaybah | 828–885 (p. 84) | **Inconsistent** (death) | b. 213/828, d. 276/889 (TDV); GND 828–889; BnF 828–889 | https://islamansiklopedisi.org.tr/ibn-kuteybe ; https://lobid.org/gnd/119526409.json ; https://catalogue.bnf.fr/ark:/12148/cb12551842q |
| 39 | Hudhayfa ibn al-Yaman | d. 656 (p. 84) | **Consistent** | d. 36/656 (TDV) | https://islamansiklopedisi.org.tr/huzeyfe-b-yeman |
| 40 | F. E. Peters | b. 1927 (p. 84) | **Consistent** | 23 Jun 1927 – 30 Apr 2020 (GND) | https://lobid.org/gnd/132849968.json |
| 41 | Hashim Amir 'Ali | 1903–1987 (p. 85) | **Consistent** | GND: b. 1903, no death date. Wikidata: 8 May 1903 – 1987, citing enwiki (the death year is Wikipedia-level only) | https://lobid.org/gnd/1146266405.json ; https://www.wikidata.org/wiki/Q5678998 |
| 42 | "Prince Leoni" Caetani | 1869–1935 (p. 85) | **Consistent** | GND 1869–1935; Wikidata 12 Sep 1869 – 25 Dec 1935 (BnF) | https://lobid.org/gnd/118853597.json |
| 43 | Henri Lammens | 1862–1937 (p. 85) | **Consistent** | 1 Jul 1862 – 24 Apr 1937 (BnF); GND 1862–1937 | https://catalogue.bnf.fr/ark:/12148/cb12314182k ; https://lobid.org/gnd/135656117.json |
| 44 | Abraha | raids "in 552 CE" (p. 85) | **Consistent** (date) | Wikipedia: "The second inscription of Abraha, dated 552, mentions military campaigns in central Arabia" (Murayghan, Ry 506). The inscription describes central Arabia (Haliban), not specifically "near Mecca". Wikipedia-level | https://en.wikipedia.org/wiki/Abraha |
| 45 | Ahmad ibn Hanbal | 780–855 (p. 85) | **Consistent** | b. Rabi' I 164/780, d. 241/855 (TDV); GND 780–855 | https://islamansiklopedisi.org.tr/ahmed-b-hanbel ; https://lobid.org/gnd/118885855.json |
| 46 | 'Umar ibn 'Abd al-'Aziz | r. 717–720 (p. 86) | **Consistent** | Caliph 717–720, d. 101/720 (TDV); GND 682–720 | https://islamansiklopedisi.org.tr/omer-b-abdulaziz ; https://lobid.org/gnd/118589938.json |
| 47 | Sa'id ibn Makhlad | d. 889 (p. 86) | **Consistent** | d. 889 (Wikidata, citing al-A'lam); enwiki: "died c. 889", born a Nestorian Christian, "years active 878–885" | https://www.wikidata.org/wiki/Q7395440 ; https://en.wikipedia.org/wiki/Sa%27id_ibn_Makhlad |
| 48 | al-Mu'tamid | "nominal Caliph 878-885 CE"; "(r. 877; 878-879 CE)" (p. 86) | **Inconsistent** | Reigned 16 Jun 870 – Oct 892 (Wikidata). Enwiki: "al-Mu'tamid (r. 870–892)". The book's figures belong to his viziers: 877 and 878/9 are al-Hasan ibn Makhlad's two vizierates; 878–885 are Sa'id ibn Makhlad's "years active" (both enwiki) | https://www.wikidata.org/wiki/Q284721 ; https://en.wikipedia.org/wiki/Al-Hasan_ibn_Makhlad_al-Jarrah ; https://en.wikipedia.org/wiki/Sa%27id_ibn_Makhlad |
| 49 | al-Hasan ibn Makhlad ibn al-Jarrah | d. c. 882 (p. 86) | **Consistent** | "probably died in 882"; vizier Aug–Sep 877 and Jul–Aug 878 (enwiki, citing Sourdel, EI2 "Ibn Makhlad") | https://en.wikipedia.org/wiki/Al-Hasan_ibn_Makhlad_al-Jarrah ; https://www.wikidata.org/wiki/Q4702481 |
| 50 | Caliph al-Mutawakkil | r. 847–861 (p. 86) | **Consistent** | GND 822–861, "regierte ab 847"; Wikidata caliph 10 Aug 847 – Dec 861 | https://lobid.org/gnd/121169863.json ; https://www.wikidata.org/wiki/Q220789 |
| 51 | Arthur Jeffery | 1892–1959 (p. 88) | **Consistent** | 18 Oct 1892 – 2 Aug 1959 (GND) | https://lobid.org/gnd/1024481352.json |
| 52 | Léon de Laborde | 1807–1869 (p. 88) | **Consistent** | 12 Jun 1807 – 25 Mar 1869 (GND) | https://lobid.org/gnd/116638044.json |
| 53 | Muhammad Hamidullah | 1908–2002 (p. 94) | **Consistent** | 19 Feb 1908 – 17 Dec 2002 (GND); TDV 1908–2002 | https://lobid.org/gnd/10360572X.json ; https://islamansiklopedisi.org.tr/muhammed-hamidullah |
| 54 | al-Biruni | 937–1048 (p. 94) | **Inconsistent** (birth) | b. 3 Dhu l-Hijja 362 / 4 Sep 973 (TDV); GND 973–1048; BnF 973–1050. "937" looks like a transposition of 973. The death year is itself disputed: 440/1048 is the old standard (GND), but TDV says he was alive in 443/1051 and suggests 453/1061; BnF has 1050 | https://islamansiklopedisi.org.tr/biruni ; https://lobid.org/gnd/118511327.json ; https://catalogue.bnf.fr/ark:/12148/cb120695932 |
| 55 | Jamal al-Din al-Afghani | 1837–1897 (p. 94) | **Minor difference** | b. Sha'ban 1254 / Nov 1838 (TDV: sources agree on this), d. 1897; GND 1838–1897 | https://islamansiklopedisi.org.tr/efgani-cemaleddin ; https://lobid.org/gnd/118500902.json |
| 56 | Muhammad 'Abduh | 1849–1905 (p. 94) | **Consistent** | TDV 1849–1905; GND 1849–1905 | https://islamansiklopedisi.org.tr/muhammed-abduh ; https://lobid.org/gnd/118643584.json |
| 57 | Rashid Rida | 1865–1935 (p. 94) | **Consistent** | TDV 1865–1935; GND 23 Sep 1865 – 22 Aug 1935 | https://islamansiklopedisi.org.tr/resid-riza ; https://lobid.org/gnd/11888753X.json |
| 58 | Sultan Abdul Hamid II | "in 1904" (p. 98) | **Consistent** | Sultan 1876–1909 (TDV; GND: deposed 1909), so 1904 falls within his reign. Griffith's claim that he confirmed the Testament was not checked | https://islamansiklopedisi.org.tr/abdulhamid-ii ; https://lobid.org/gnd/118646435.json |
| 59 | (J. N.) Fazakerley | visit "in 1811" (p. 70) | **Consistent** | His "Journey from Cairo to Mount Sinai" (in Walpole, *Travels*, 1820) begins "We left Cairo on the thirty-first of January, 1811". The same account mentions a convent document "from Buonaparte". Fazakerley lived 1787–1852 (Wikidata) | https://archive.org/download/travelsinvarious00walp/travelsinvarious00walp_djvu.txt ; https://www.wikidata.org/wiki/Q6250416 |
| 60 | monk Habib | found the Najran text "in 878/879 CE" (p. 77) | **Consistent** | Chronicle of Seert (Scher, PO 13): "copie … faite sur un registre qui fut retrouvé en 265 à Rirmantha chez Habib le moine". 265 AH = Aug 878 – Aug 879 | https://archive.org/download/patrologiaorient13pariuoft/patrologiaorient13pariuoft_djvu.txt |
| 61 | "Barthlmy" (Étienne Barthélemy) | discovery "in 1850" (p. 78) | **Disputed among sources** | Wikipedia (Seal of Muhammad) quotes EI2: the parchment "was found in a monastery at Akhmim in 1850". A footnote on the same page quotes another source: "discovered in 1858 by Monsieur Etienne Barthelemy". The book's "near Saide" also differs from Akhmim | https://en.wikipedia.org/wiki/Seal_of_Muhammad |
| 62 | Tsernotabey | acted "in 1517" (pp. 67–68) | **Unverified** | No authority record or independent account found. The 1517 conquest itself is correct (TDV Selim I) | https://islamansiklopedisi.org.tr/selim-i |
| 63 | M.L.M.D.C. | book published 1697 (pp. 74–75) | **Consistent** | BnF: *Jeux d'esprit et de mémoire*, Cologne, Frédéric Le Jeune, **1697** (an earlier edition is dated 1694). Author: Jean Brodeau, marquis de Châtres (1632?–1712), i.e. "M. L. M. D. C." | https://catalogue.bnf.fr/ark:/12148/cb302289205 ; https://catalogue.bnf.fr/ark:/12148/cb33441791m |
| 64 | Sulayman II / "Soliman II" | Kara Mustafa served him "from 1663-1666" (p. 72) | **Inconsistent** | Suleiman II: b. 1642, reigned 1687–1691 (TDV; GND; Wikidata 8 Nov 1687 – 22 Jun 1691). Mehmed IV was sultan 1648–1687 (TDV). GND notes that older European works sometimes count Suleiman the Magnificent as "Suleiman II", but he reigned 1520–1566, which also rules out 1663–66 | https://islamansiklopedisi.org.tr/suleyman-ii ; https://islamansiklopedisi.org.tr/mehmed-iv ; https://lobid.org/gnd/122838068.json |
| 65 | The Prophet Muhammad (ch. 2) | death 19 years before 651 (= 632); covenant 3 Muharram 2 AH = 7 Jul 623; migration "September 622" (pp. 66, 83, 85) | **Consistent** | GND 570–632. Hijra (TDV): left Mecca on the night of 26 Safar / 9 Sep 622, reached Quba on 20 Sep 622, entered Medina on 24 Sep 622. Calendar check: BnF says 'Umar fixed the Hijri epoch at 16 Jul 622; adding 354 days gives 1 Muharram 2 AH = 5 Jul 623, so 3 Muharram 2 AH = 7 Jul 623 (tabular calendar, my arithmetic). The "552 birth" of "a few Western historians" was not checked | https://lobid.org/gnd/118583158.json ; https://islamansiklopedisi.org.tr/hicret ; https://catalogue.bnf.fr/ark:/12148/cb11939742h |
| 66 | 'Ali ibn Abi Talib | d. 661; r. 656–661 (pp. 323, 351, 370) | **Consistent** | d. 40/661, caliph 656–661 (TDV) | https://islamansiklopedisi.org.tr/ali |
| 67 | Abu Bakr | c. 573–634 (p. 323; "c. 573634" OCR at p. 335) | **Consistent** | b. about 3 years after the Year of the Elephant; d. 22 Jumada II 13 / 23 Aug 634, aged 63 (TDV); GND and BnF 573–634 | https://islamansiklopedisi.org.tr/ebu-bekir ; https://lobid.org/gnd/118859323.json ; https://catalogue.bnf.fr/ark:/12148/cb15598577g |
| 68 | 'Umar ibn al-Khattab | 579–644 (pp. 323, 334, 335, 338) | **Disputed among sources** (birth) | Same sources as row 22: TDV ≈583, BnF 581?, GND 568, Wikidata c. 586; no source gives 579. d. 23/644 is correct | https://islamansiklopedisi.org.tr/omer ; https://lobid.org/gnd/118822810.json |
| 69 | 'Uthman ibn 'Affan | 577–656 (p. 323) | **Disputed among sources** (birth) | d. 35/656 (TDV) is correct. Birth: "six years after the Year of the Elephant", at Ta'if (TDV); GND 574; Wikidata 574/575; BnF 570?. 577 is close to TDV but no source gives it | https://islamansiklopedisi.org.tr/osman ; https://lobid.org/gnd/119073765.json ; https://catalogue.bnf.fr/ark:/12148/cb15061698j |
| 70 | Abu al-Darda' | d. 652 (pp. 323, 325) | **Consistent** | d. 32/652 in Damascus; some reports say 31/651 (TDV) | https://islamansiklopedisi.org.tr/ebud-derda |
| 71 | Abu Hurayrah | 603–681 (p. 323) | **Inconsistent** (death) | Same as row 31: d. 58/678 (TDV; also 57 or 59 AH); GND 679; BnF 677? | https://islamansiklopedisi.org.tr/ebu-hureyre ; https://lobid.org/gnd/118966863.json |
| 72 | "Abu Hudayfah ibn al-Yaman" | d. 656 (p. 323) | **Consistent** (date; name garbled) | Hudhayfa ibn al-Yaman, whose kunya is Abu 'Abd Allah, d. 36/656 (TDV). "Abu Hudhayfa" is the kunya of a different man (row 91). On p. 84 the book names him correctly as "Hudayfah ibn al-Yaman" | https://islamansiklopedisi.org.tr/huzeyfe-b-yeman |
| 73 | 'Abd Allah ibn Mas'ud | d. c. 650 (p. 323) | **Minor difference** | d. 32/652-53 (TDV); GND d. 653 | https://islamansiklopedisi.org.tr/abdullah-b-mesud ; https://lobid.org/gnd/118897470.json |
| 74 | 'Abbas ibn 'Abd al-Muttalib | d. 652/653 (p. 323) | **Consistent** | Wikidata d. 653 (preferred: 15 Feb 653); enwiki c. 566 – c. 653 | https://www.wikidata.org/wiki/Q293599 ; https://en.wikipedia.org/wiki/Al-Abbas_ibn_Abd_al-Muttalib |
| 75 | Hassan ibn Thabit | d. 674 (p. 323) | **Disputed among sources** | TDV: sources give 40 (660), 50 (670) or 54 (674); if the report that he lived 120 years is right, about 60 (680), which is the date in TDV's heading. GND 563–660; Wikidata 674 (OpenITI). The book uses one of the reported dates | https://islamansiklopedisi.org.tr/hassan-b-sabit ; https://lobid.org/gnd/119000962.json |
| 76 | Zubayr ibn al-'Awwam | 594–656 (p. 323) | **Consistent** | d. 36/656 (TDV). Wikidata b. 594 (it.wikipedia), d. 4 Dec 656. TDV gives no birth year | https://islamansiklopedisi.org.tr/zubeyr-b-avvam ; https://www.wikidata.org/wiki/Q293565 |
| 77 | Talhah ibn 'Ubaydullah | d. 656 (p. 323) | **Consistent** | d. 36/656 (TDV) | https://islamansiklopedisi.org.tr/talha-b-ubeydullah |
| 78 | Sa'd ibn Mu'adh | d. 627 (p. 324) | **Consistent** | d. 5/627 (TDV) | https://islamansiklopedisi.org.tr/sad-b-muaz |
| 79 | Nafi ibn al-Harith | d. 670; "the Prophet Muhammad's physician" (p. 324) | **Disputed among sources** (and the identity is confused) | TDV: the physician was his father, al-Harith ibn Kalada. Sources say al-Harith died in 50/670, but TDV prefers the report that he died on the same day as Abu Bakr (23 Aug 634). Nafi' was the physician's son and a Companion (TDV). Current English Wikipedia makes Nafi the physician and gives "died 13 AH / 634–635"; Wikidata still has d. 670. So "670" is a disputed date taken over from the father | https://islamansiklopedisi.org.tr/haris-b-kelede ; https://en.wikipedia.org/wiki/Nafi_ibn_al-Harith ; https://www.wikidata.org/wiki/Q8064535 |
| 80 | Zayd ibn Thabit | c. 610 – c. 660 (pp. 324, 325) | **Inconsistent** (death) | b. 11 years before the Hijra (611) (TDV): correct. d. 45, 51 or 55 AH, with 45/665 most often preferred (TDV); GND 611–666; Wikidata 665 (preferred). Only English Wikipedia gives 660 | https://islamansiklopedisi.org.tr/zeyd-b-sabit ; https://lobid.org/gnd/118981331.json ; https://www.wikidata.org/wiki/Q144302 |
| 81 | Khuzaymah ibn Thabit | d. 657 (p. 324) | **Consistent** | d. 37/657 at Siffin (TDV) | https://islamansiklopedisi.org.tr/huzeyme-b-sabit |
| 82 | 'Abd Allah ibn 'Amr ibn al-'As | d. 684 (p. 324) | **Consistent** | d. 65/684-85 (TDV heading; reported variants 63, 65, 68, 69 AH) | https://islamansiklopedisi.org.tr/abdullah-b-amr-b-as |
| 83 | 'Ammar ibn Yasir | c. 570 – c. 657 (pp. 324, 326) | **Disputed among sources** (birth) | d. 37/657 at Siffin "about 93 years old" (TDV), which implies b. c. 564. Wikidata gives 570 without a reference. GND d. 657. Death year is correct | https://islamansiklopedisi.org.tr/ammar-b-yasir ; https://lobid.org/gnd/128433701.json |
| 84 | Yasir ibn 'Amir al-'Ansi | converted "between 610 and 613" (p. 324) | **Consistent** | Converted at Dar al-Arqam, led by his son 'Ammar; tortured to death by Abu Jahl, "probably 615" (TDV) | https://islamansiklopedisi.org.tr/yasir-b-amir |
| 85 | Abu Dharr | d. 652 (p. 325) | **Consistent** | d. 32/653 (TDV heading; 32 AH = Aug 652 – Jul 653) | https://islamansiklopedisi.org.tr/ebu-zer-el-gifari |
| 86 | al-Bara' ibn Malik | d. 640 (p. 325) | **Minor difference** | Killed at Tustar; d. 20/641 (TDV). Wikidata 641. 20 AH began on 21 Dec 640 | https://islamansiklopedisi.org.tr/bera-b-malik |
| 87 | Anas ibn Malik | c. 612 – 709 or 712 (p. 325) | **Consistent** | b. 10 years before the Hijra (612); d. 93/711-12 aged 103; other reported years 90/709, 91/710, 92/711, 95/714 (TDV) | https://islamansiklopedisi.org.tr/enes-b-malik |
| 88 | Hamzah | 568–625 (p. 325) | **Minor difference** | b. 569 or 570; d. 3/625 at Uhud (TDV). Wikidata 568 (ru.wikipedia) | https://islamansiklopedisi.org.tr/hamza ; https://www.wikidata.org/wiki/Q770033 |
| 89 | Sahl ibn Sa'd | (709) (p. 325) | **Minor difference** | d. 91 AH (enwiki), which is Nov 709 – Oct 710; Wikidata 710 (citing al-A'lam) | https://en.wikipedia.org/wiki/Sahl_ibn_Sa%27d ; https://www.wikidata.org/wiki/Q7399677 |
| 90 | Sahl ibn Hunayf | d. c. 658 (p. 325) | **Consistent** | d. 38/658-59 (TDV) | https://islamansiklopedisi.org.tr/sehl-b-huneyf |
| 91 | Abu Hudhayfa ibn 'Utba | d. 633 (p. 325) | **Consistent** | d. 12/633 (TDV) | https://islamansiklopedisi.org.tr/ebu-huzeyfe |
| 92 | Tamim al-Dari | d. 661 (p. 325) | **Consistent** | d. 40/661 (TDV); GND d. 660 | https://islamansiklopedisi.org.tr/temim-ed-dari ; https://lobid.org/gnd/118926942.json |
| 93 | 'Amr ibn al-'As | c. 592–664 (p. 326) | **Disputed among sources** (birth) | d. 43/664 (TDV) is correct. Birth: GND "ca. 570" (alternative ca. 575); Wikidata 570 (from GND), c. 573 (enwiki). TDV implies c. 603, since he is said to have been only 11–12 years older than his son, who was born c. 615. **No source checked gives 592** | https://islamansiklopedisi.org.tr/amr-b-as ; https://lobid.org/gnd/129982091.json ; https://www.wikidata.org/wiki/Q314781 |
| 94 | 'Abd Allah ibn 'Umar | c. 614–693 (p. 326) | **Minor difference** | b. "in the third year of prophethood" (TDV, ≈612/613); d. 73/693 (TDV). Wikidata c. 610 | https://islamansiklopedisi.org.tr/abdullah-b-omer-b-hattab ; https://www.wikidata.org/wiki/Q2046261 |
| 95 | Abu Hanifah | 699–767 (p. 326) | **Consistent** | b. 80/699, d. 150/767 (TDV); GND 699–767 | https://islamansiklopedisi.org.tr/ebu-hanife ; https://lobid.org/gnd/11899204X.json |
| 96 | 'Asim ibn Thabit | "died at Badr (624 CE)" (p. 326) | **Inconsistent** | He fought at Badr, where he killed 'Uqba ibn Abi Mu'ayt, but he was killed at **al-Raji'** in 4/625 (TDV). Wikidata d. 625 | https://islamansiklopedisi.org.tr/asim-b-sabit ; https://www.wikidata.org/wiki/Q6812181 |
| 97 | Sa'd ibn al-Rabi' | died at Uhud (625) (p. 326) | **Consistent** | d. 3/625 at Uhud (TDV) | https://islamansiklopedisi.org.tr/sad-b-rebi |
| 98 | 'Amir ibn Rabi'ah | "returned to Medina in 615 CE" (p. 326) | **Inconsistent** | TDV: he emigrated to Abyssinia twice and went to **Medina** as soon as he learned of the Prophet's Hijra (622). The first emigrants left in 615, and some later returned to **Mecca** (TDV *Hicret* dates that return to 620). No one could "return to Medina" in 615 | https://islamansiklopedisi.org.tr/amir-b-rebia ; https://islamansiklopedisi.org.tr/hicret |
| 99 | Hisham ibn al-'As | "died 635 CE at the Battle of Yarmuk" (p. 326) | **Inconsistent** | Yarmuk was fought in 15/636 (TDV). 13/634 was Ajnadayn (TDV). The book seems to follow Wikipedia ("Battle of Yarmouk in the year 13 AH (635 CE)"), which matches neither date | https://islamansiklopedisi.org.tr/yermuk-savasi ; https://islamansiklopedisi.org.tr/ecnadeyn-savasi ; https://en.wikipedia.org/wiki/Hisham_ibn_al-As |
| 100 | Ja'far ibn Abi Talib | d. 629 (p. 326) | **Consistent** | d. 8/629 at Mu'ta (TDV) | https://islamansiklopedisi.org.tr/cafer-b-ebu-talib |
| 101 | Usamah ibn Zayd | 615–673 (p. 326) | **Minor difference** | b. 8 years before the Hijra (614); d. 54/674 (TDV; 54 AH = Dec 673 – Dec 674) | https://islamansiklopedisi.org.tr/usame-b-zeyd |
| 102 | Zayd ibn Arqam | d. 685 (p. 327) | **Minor difference** | d. 66 (686) or 68 (688) in Kufa (TDV). 66 AH runs Aug 685 – Jul 686. Wikidata 687 (al-A'lam) | https://islamansiklopedisi.org.tr/zeyd-b-erkam |
| 103 | Jubayr ibn Mut'im | converted after Hudaybiyya (628) (p. 327) | **Consistent** | TDV: gave up his hostility after Hudaybiyya and became Muslim in 628; another report says he converted at the conquest of Mecca | https://islamansiklopedisi.org.tr/cubeyr-b-mutim |
| 104 | Juan Vernet | b. 1923 (p. 333) | **Consistent** | 31 Jul 1923 – 23 Jul 2011 (BnF); GND 1923–2011. He died before the book appeared | https://catalogue.bnf.fr/ark:/12148/cb12849415z ; https://lobid.org/gnd/1017412391.json |
| 105 | (George F.) Nafziger | b. 1949 (p. 334) | **Consistent** | b. 1 Mar 1949 (GND) | https://lobid.org/gnd/124265839.json |
| 106 | John Eric Adair | b. 1934 (p. 334) | **Consistent** | b. 18 May 1934 (GND); Wikidata d. 1 Nov 2025 | https://lobid.org/gnd/124297234.json ; https://www.wikidata.org/wiki/Q3180864 |
| 107 | Sir John Bagot Glubb | 1897–1986 (p. 334) | **Consistent** | 16 Apr 1897 – 17 Mar 1986 (GND) | https://lobid.org/gnd/118695479.json |
| 108 | (Fred) Donner | b. 1945 (p. 334) | **Consistent** | GND b. 1945; Wikidata 30 Sep 1945 | https://lobid.org/gnd/141164719.json |
| 109 | John bar Penkaye | 7th century (p. 335) | **Consistent** (weak) | Wikidata: floruit 7th century (no reference). The GND record has no dates. Wikidata-level only | https://www.wikidata.org/wiki/Q330890 |
| 110 | Bishop of Adiabene (unnamed) | writing 650–660 (p. 335) | **Unverified** | No person is named, so there is nothing to look up. Fortescue, the book's source, was not opened | — |
| 111 | Abu Yusuf | d. 798 (p. 335) | **Consistent** | d. 182/798 (TDV); GND 731–798 | https://islamansiklopedisi.org.tr/ebu-yusuf ; https://lobid.org/gnd/118925873.json |
| 112 | Mu'awiya | 602–680; "king" in Jerusalem 659 (pp. 335, 340) | **Disputed among sources** (659) | Life dates are correct (row 21). Jerusalem: he received oaths of allegiance there "the first in late 660 or early 661 and the second in July 661" (enwiki, citing modern scholarship). The book's 659 comes from Crone & Cook | https://en.wikipedia.org/wiki/Mu%27awiya_I ; https://islamansiklopedisi.org.tr/muaviye-b-ebu-sufyan |
| 113 | 'Abd al-'Aziz ibn Marwan | d. 705; "The Caliph" (p. 336) | **Consistent** (date) | d. 86/705 at Hulwan. He was governor of Egypt for over 20 years and son of the caliph Marwan, **not a caliph** (TDV) | https://islamansiklopedisi.org.tr/abdulaziz-b-mervan |
| 114 | al-Turtushi | 1059–1127 (pp. 336–339) | **Minor difference** | b. 26 Jumada I 451 / 10 Jul 1059; d. 520/1126 (TDV; GND "451/1059 – 520/1126"). 520 AH ended on 15 Jan 1127 | https://islamansiklopedisi.org.tr/turtusi ; https://lobid.org/gnd/119220989.json |
| 115 | Zaid Shakir | b. 1956 (p. 337) | **Consistent** | b. 24 May 1956 (Wikidata, citing enwiki; Wikipedia-level) | https://www.wikidata.org/wiki/Q8064787 |
| 116 | Yusuf al-Qaradawi | b. 1956 (p. 337); b. 1926 (p. 372) | **Inconsistent** (p. 337) | b. 9 Sep 1926, d. 26 Sep 2022 (Wikidata); GND 1926–2022. p. 372 is right; p. 337 is wrong | https://lobid.org/gnd/123493390.json ; https://www.wikidata.org/wiki/Q64129 |
| 117 | M. J. de Goeje | 1836–1909 (p. 337) | **Consistent** | 13 Aug 1836 – 13 May 1909 (GND) | https://lobid.org/gnd/116703636.json |
| 118 | Leone Caetani | 1869–1935 (p. 337) | **Consistent** | GND 1869–1935 | https://lobid.org/gnd/118853597.json |
| 119 | A. S. Tritton | 1881–1973 (p. 337) | **Consistent** | 25 Feb 1881 – 8 Nov 1973 (GND) | https://lobid.org/gnd/17242691X.json |
| 120 | Robert Spencer | b. 1962 (p. 337) | **Consistent** | b. 27 Feb 1962 (enwiki). GND has "Spencer, Robert, b. 1962", but the record has no description to confirm it is the same man | https://en.wikipedia.org/wiki/Robert_Spencer_(author) ; https://lobid.org/gnd/137209347.json |
| 121 | Imam al-Tabari | 838–923 (pp. 337–339) | **Minor difference** | b. end of 224 / start of 225 AH (839) (TDV); GND and BnF 839–923; Wikidata's earliest possible date is 838 | https://islamansiklopedisi.org.tr/taberi-muhammed-b-cerir ; https://lobid.org/gnd/118620436.json ; https://catalogue.bnf.fr/ark:/12148/cb11925884j |
| 122 | Caliph 'Umar II | r. 717–720 (p. 338) | **Consistent** | 717–720 (TDV) | https://islamansiklopedisi.org.tr/omer-b-abdulaziz |
| 123 | Ami Isseroff | d. 2011 (p. 338) | **Unverified** | Checked GND, Wikidata and English and Hebrew Wikipedia. None has a biography with a death date; Wikipedia only cites him as an author | — |
| 124 | (Addai) Scher | 1867–1915 (p. 339) | **Consistent** | GND 1867–1915; Wikidata 3 Mar 1867 – 21 Jun 1915 | https://lobid.org/gnd/123927013.json |
| 125 | The Prophet Muhammad | 570–642 (p. 339); 570–632 (p. 354) | **Inconsistent** (p. 339) | GND 570–632; Wikidata 570/571 – 8 Jun 632. p. 354 is right; p. 339 is 10 years off | https://lobid.org/gnd/118583158.json ; https://www.wikidata.org/wiki/Q9458 |
| 126 | Khalid ibn al-Walid | 592–642 (p. 339) | **Inconsistent** (birth) | b. 35–39 years before the Hijra (583–587), d. 21/642 (TDV); BnF "058.–0642"; Wikidata 586. Death year is correct | https://islamansiklopedisi.org.tr/halid-b-velid ; https://catalogue.bnf.fr/ark:/12148/cb135409718 |
| 127 | John of Damascus | c. 645 or 676–749 (p. 340); d. 749/764 (p. 371) | **Disputed among sources** (birth); "764" unsupported | TDV: proposed birth years 640, 645 and 679; most scholars accept 675; Nasrallah 655–660; Sahas 655. Death "generally accepted as 749". GND 675–749; Wikidata 675 – 4 Dec 749. **No source checked gives 764** | https://islamansiklopedisi.org.tr/yuhanna-ed-dimaski ; https://lobid.org/gnd/118557971.json ; https://www.wikidata.org/wiki/Q51884 |
| 128 | Yazid I | r. 680–683 (p. 340) | **Consistent** | Caliph 680–683, d. 64/683 (TDV) | https://islamansiklopedisi.org.tr/yezid-i |
| 129 | al-'Aziz | r. 975–996 (p. 340) | **Consistent** | 975–996 (TDV) | https://islamansiklopedisi.org.tr/aziz-billah |
| 130 | 'Abd al-Malik ibn Marwan | r. 685–705 (p. 340) | **Consistent** | 685–705 (TDV) | https://islamansiklopedisi.org.tr/abdulmelik-b-mervan |
| 131 | Tiberius Sempronius Gracchus | Sardinia 177 BCE (p. 341) | **Consistent** | "After his first consulship in 177 BC, he was assigned to Sardinia" (enwiki) | https://en.wikipedia.org/wiki/Tiberius_Sempronius_Gracchus_(consul_177_BC) |
| 132 | Charlemagne | 782 (p. 341) | **Consistent** | Massacre of Verden: October 782, 4,500 Saxons (enwiki). GND 747–814 | https://en.wikipedia.org/wiki/Massacre_of_Verden ; https://lobid.org/gnd/118560034.json |
| 133 | 'Abd al-Rahman III | r. 912–961; caliphate 929 (p. 342) | **Consistent** | 912–961 (TDV). GND: emir 912–929, caliph 929–961 | https://islamansiklopedisi.org.tr/abdurrahman-iii ; https://lobid.org/gnd/118978098.json |
| 134 | 'Abd al-Rahman I | Emirate 756 (p. 342) | **Consistent** (date) | Founded the Umayyad state of al-Andalus, emir 756–788 (TDV; GND). The book's label "the last Caliph of the Umayyads" is wrong: he was never a caliph | https://islamansiklopedisi.org.tr/abdurrahman-i ; https://lobid.org/gnd/121026019.json |
| 135 | Bayezid II | r. 1481–1512 (p. 342) | **Consistent** | 1481–1512 (TDV) | https://islamansiklopedisi.org.tr/bayezid-ii |
| 136 | Boabdil | 1459–1533 (p. 343) | **Consistent** | Wikidata Q312763: c. 1459 – 1533 (citing enwiki). Enwiki: born 1460, died 1533, "Multiple dates … are suggested in different sources". The GND record has no dates. Wikipedia-level. Warning: Wikidata Q1377360 carries az-Zaghal's dates (1444–1494) | https://www.wikidata.org/wiki/Q312763 ; https://en.wikipedia.org/wiki/Boabdil |
| 137 | Fernando (Ferdinand II) | 1452–1516 (p. 343) | **Consistent** | GND 1452–1516 | https://lobid.org/gnd/118686712.json |
| 138 | Isabela (Isabella I) | 1451–1504 (p. 343) | **Consistent** | GND 1451–1504 | https://lobid.org/gnd/11863982X.json |
| 139 | Cardinal Cisneros | 1436–1517 (p. 343) | **Consistent** | GND 1436 – 8 Nov 1517 | https://lobid.org/gnd/118712152.json |
| 140 | al-Maqqari | 1578–1632 (p. 344) | **Disputed among sources** (birth) | d. 1041/1632 (TDV; BnF Jan 1632; GND) is correct. Birth estimates: TDV "990 (1582) or a few years later"; BnF 1577?; GND 1591; Wikidata 1578 (SNAC) | https://islamansiklopedisi.org.tr/makkari-ahmed-b-muhammed ; https://catalogue.bnf.fr/ark:/12148/cb15001876j ; https://lobid.org/gnd/118969579.json |
| 141 | Charles V | 1500–1558 (p. 344) | **Consistent** | 24 Feb 1500 – 21 Sep 1558 (GND) | https://lobid.org/gnd/118560093.json |
| 142 | Philip II | 1527–1598 (p. 344) | **Consistent** | 21 May 1527 – 13 Sep 1598 (GND) | https://lobid.org/gnd/118593862.json |
| 143 | Don Juan de Austria | 1547–1578 (p. 344) | **Consistent** | 24 Feb 1547 – 1 Oct 1578 (GND) | https://lobid.org/gnd/118713299.json |
| 144 | Mehmed II | r. 1444–1446, 1451–1481 (pp. 345, 349) | **Consistent** | TDV and GND: "1444-1446 sowie 1451-1481" | https://islamansiklopedisi.org.tr/mehmed-ii ; https://lobid.org/gnd/118583166.json |
| 145 | Karen Armstrong | b. 1944 (p. 346) | **Consistent** | b. 14 Nov 1944 (GND) | https://lobid.org/gnd/119304791.json |
| 146 | Louis XII | 1462–1515 (p. 347) | **Consistent** | 27 Jun 1462 – 1 Jan 1515 (GND) | https://lobid.org/gnd/118780735.json |
| 147 | Selim II | r. 1566–1574 (p. 347) | **Consistent** | 1566–1574 (TDV; GND) | https://islamansiklopedisi.org.tr/selim-ii ; https://lobid.org/gnd/138054231.json |
| 148 | Sir Charles Eliot | 1801–1875 (p. 347) | **Inconsistent** (wrong person) | *Turkey in Europe* (1900) is by Sir Charles Norton Edgcumbe Eliot, 8 Jan 1862 – 16 Mar 1931 (enwiki; GND gives 1864–1931). The book's 1801–1875 are the dates of Admiral Sir Charles **Elliot** (GND 1801–1875; Wikidata 15 Aug 1801 – 9 Sep 1875) | https://en.wikipedia.org/wiki/Charles_Eliot_(diplomat) ; https://lobid.org/gnd/119127032.json ; https://lobid.org/gnd/122894928.json ; https://www.wikidata.org/wiki/Q184780 |
| 149 | Albert Howe Lybyer | 1876–1949 (p. 347) | **Consistent** | GND 1876–1949. Wikidata also has an unreferenced 1879 | https://lobid.org/gnd/173251455.json |
| 150 | Selim I ("the Grim") | r. 1512–1520 (p. 348) | **Consistent** | 1512–1520 (TDV) | https://islamansiklopedisi.org.tr/selim-i |
| 151 | Patriarch Theoleptus (I) | 1513–1522 (p. 348) | **Consistent** | Patriarch from mid-1513 to Dec 1522 (enwiki) | https://en.wikipedia.org/wiki/Theoleptus_I_of_Constantinople |
| 152 | Antonio Rincon | Belgrade 1532 (p. 349) | **Consistent** (year) | "Rincon was again sent to the Ottoman court in March 1532" (enwiki); GND: d. 1541, ambassador 1538–1541. The Belgrade location is not confirmed | https://en.wikipedia.org/wiki/Antonio_Rincon ; https://lobid.org/gnd/1418140368.json |
| 153 | Jean Bodin | 1530–1596 (p. 349) | **Consistent** | GND 1529–1596; Wikidata 1530 (LIBRIS, SNL) – 1596 (BnF) | https://lobid.org/gnd/118512307.json ; https://www.wikidata.org/wiki/Q190944 |
| 154 | Muhammad Hamidullah | 1908–2002 (pp. 349, 355, 368) | **Consistent** | Same as row 53 | https://lobid.org/gnd/10360572X.json |
| 155 | Kemal Atatürk | 1881–1938 (p. 349) | **Consistent** | 19 May 1881 – 10 Nov 1938 (GND) | https://lobid.org/gnd/118650793.json |
| 156 | Juan Perón | 1895–1974 (p. 354) | **Consistent** | 8 Oct 1895 – 1 Jul 1974 (GND) | https://lobid.org/gnd/118739999.json |
| 157 | Ibn Sa'd | 784–845 (pp. 354, 355) | **Disputed among sources** (birth) | d. 230/845 (TDV) is correct. Birth: GND 784; Wikidata 784 (GND, BnF, AlKindi); TDV 160/777 (citing al-Dhahabi) | https://islamansiklopedisi.org.tr/ibn-sad ; https://lobid.org/gnd/119181118.json |
| 158 | Baladhuri | d. c. 892 (p. 355) | **Consistent** | d. 279/892-93 (TDV); GND d. 892 | https://islamansiklopedisi.org.tr/belazuri ; https://lobid.org/gnd/119312360.json |
| 159 | Gibbon | 1737–1794 (p. 355) | **Consistent** | GND 1737–1794 | https://lobid.org/gnd/118717286.json |
| 160 | Bar Hebraeus | 1226–1286 (p. 355) | **Consistent** | GND 1226–1286; TDV b. 622/1225, d. 685/1286 | https://lobid.org/gnd/118652508.json ; https://islamansiklopedisi.org.tr/ibnul-ibri |
| 161 | Ibn Qayyim al-Jawziyyah | "1292/93-1286" (p. 355) | **Inconsistent** | b. 7 Safar 691 / 29 Jan 1292, d. 751/1350 (TDV); GND 4 Feb 1292 – 1 Sep 1350; BnF 29 Jan 1292 – 26 Sep 1350. The printed death date is before the birth date. "1286" is Bar Hebraeus' death year, printed just before on the same page | https://islamansiklopedisi.org.tr/ibn-kayyim-el-cevziyye ; https://lobid.org/gnd/118983547.json ; https://catalogue.bnf.fr/ark:/12148/cb12538862m |
| 162 | al-Mutawakkil | "only ruled from 847 to 861" (p. 355) | **Consistent** | Same as row 50 | https://lobid.org/gnd/121169863.json |
| 163 | Bassam Tibi | b. 1944 (p. 356) | **Consistent** | GND b. 1944; Wikidata 4 Apr 1944 | https://lobid.org/gnd/119541815.json |
| 164 | Jonathan A. C. Brown | b. 1977 (p. 360) | **Consistent** | GND b. 1977 | https://lobid.org/gnd/13366953X.json |
| 165 | Robert Graham Irwin | b. 1946 (p. 360) | **Consistent** | 23 Aug 1946 – 28 Jun 2024 (GND) | https://lobid.org/gnd/132238136.json |
| 166 | Seyyed Hossein Nasr | b. 1933 (pp. 360, 361) | **Consistent** | GND b. 1933; Wikidata 7 Apr 1933 | https://lobid.org/gnd/119382008.json |
| 167 | Muhammad Kurd 'Ali | 1876–1953 (p. 361) | **Consistent** | GND 1876–1953; TDV 1876–1953 | https://lobid.org/gnd/118906852.json ; https://islamansiklopedisi.org.tr/muhammed-kurd-ali |
| 168 | Jalal Al-e Ahmad | 1923–1969 (p. 361) | **Consistent** | 2 Dec 1923 – 9 Sep 1969 (GND) | https://lobid.org/gnd/119282690.json |
| 169 | René Guénon | 1886–1951 (p. 361) | **Consistent** | 15 Nov 1886 – 7 Jan 1951 (GND). Only the name is OCR-garbled | https://lobid.org/gnd/118936433.json |
| 170 | Muhammad Asad | 1900–1992 (p. 361) | **Consistent** | 2 Jul 1900 – 20 Feb 1992 (GND) | https://lobid.org/gnd/119060116.json |
| 171 | Sayyid Qutb | 1906–1966 (p. 361) | **Consistent** | GND 1906–1966; TDV 1906–1966 | https://lobid.org/gnd/118881957.json ; https://islamansiklopedisi.org.tr/seyyid-kutub |
| 172 | Maryam Jameelah | 1934–2012 (p. 361) | **Consistent** | 23 May 1934 – 31 Oct 2012 (GND) | https://lobid.org/gnd/1024812677.json |
| 173 | Hamid Algar | b. 1940 (p. 361) | **Consistent** | GND b. 1940 | https://lobid.org/gnd/1037005228.json |
| 174 | Abdul Latif Tibawi | 1910–1981 (p. 361) | **Consistent** | GND 1910–1981 | https://lobid.org/gnd/1074724208.json |
| 175 | Ziauddin Sardar | b. 1951 (p. 361) | **Consistent** | GND b. 1951 | https://lobid.org/gnd/124092748.json |
| 176 | Fazlur Rahman Malik | 1919–1988 (p. 361) | **Consistent** | GND 1919–1988; TDV 1919–1988 | https://lobid.org/gnd/121034143.json ; https://islamansiklopedisi.org.tr/fazlurrahman |
| 177 | Muhsin Mahdi | 1926–2007 (p. 361) | **Consistent** | 21 Jun 1926 – 9 Jul 2007 (GND) | https://lobid.org/gnd/102669728X.json |
| 178 | Bernard Lewis | b. 1916 (p. 361) | **Consistent** | 31 May 1916 – 19 May 2018 (GND) | https://lobid.org/gnd/118897225.json |
| 179 | John Edward Wansbrough | 1928–2002 (p. 361) | **Consistent** | 19 Feb 1928 – 10 Jun 2002 (GND) | https://lobid.org/gnd/1068887567.json |
| 180 | Richard L. Thompson | 1947–2008 (p. 361) | **Consistent** | 4 Feb 1947 – 18 Sep 2008 (GND) | https://lobid.org/gnd/1049230051.json |
| 181 | Arthur Pillsbury Dodge | 1849–1915 (p. 361) | **Consistent** | Library-catalogue heading "Dodge, Arthur Pillsbury, 1849-1915" on *Whence? Why? Whither?* (1907), archive.org metadata | https://archive.org/metadata/whencewhywhither00dodg |
| 182 | Anton F. Haddad | translation published 1902 (p. 362) | **Consistent** | Wikisource: Anton Haddad (1862–1924), translator of *The Oath of the Prophet Mohammed to the Followers of the Nazarene* (1902) | https://en.wikisource.org/wiki/Author:Anton_Haddad |
| 183 | Gabriel Sionita | 1577–1648 (p. 366) | **Consistent** | GND 1577–1648 | https://lobid.org/gnd/104043857.json |
| 184 | Johann Georg Nissel | 1621–1662 (p. 366) | **Consistent** | d. 1662 (GND; BnF via Wikidata). Birth: 1621 (Wikidata, citing Early Modern Letters Online) or 1623 (ECARTICO); GND gives no birth year | https://lobid.org/gnd/121226646.json ; https://www.wikidata.org/wiki/Q55125772 |
| 185 | Wendell Phillips | 1950 expedition (p. 366) | **Unverified** (event) | Life dates fit: 25 Sep 1921 – 4 Dec 1975 (BnF); GND 1921–1975, with the note that he founded the American Foundation for the Study of Man in 1949. The year of the Sinai expedition itself was not confirmed (not in English Wikipedia; the LoC collection page returned 403) | https://catalogue.bnf.fr/ark:/12148/cb12186433s ; https://lobid.org/gnd/1161143521.json |
| 186 | Adrien Guibert | *Dictionnaire* 1850 (p. 367) | **Consistent** | BnF: *Dictionnaire géographique et statistique*, Paris, J. Renouard, **1850** (later editions 1855 and 1863). GND/Wikidata have an Adrien Guibert 1805–1843 (unreferenced); if he is the same man, the 1850 edition was posthumous | https://catalogue.bnf.fr/ark:/12148/cb30554196c ; https://lobid.org/gnd/1384156402.json |
| 187 | M. J. Zohrab | 1822 (p. 367) | **Unverified** | The 1822 *Journal asiatique* notice was not located in the volumes I could open. A "docteur Zohrab" co-edited Armenian fables with J. Saint-Martin in 1826 (JA publications list), so an Armenian scholar of that name was active in Paris then | https://archive.org/download/journalasiatiqu42fragoog/journalasiatiqu42fragoog_djvu.txt |
| 188 | Gregory (first name unknown) | 1822 (p. 367) | **Unverified** | The *Bulletin des sciences* (1822) notice was not located | — |
| 189 | M. Nallino | 1899 (p. 367) | **Consistent** | The 12th International Congress of Orientalists met in Rome in 1899 (enwiki). C. A. Nallino lived 1872–1938 (GND) | https://en.wikipedia.org/wiki/International_Congress_of_Orientalists ; https://lobid.org/gnd/116894261.json |
| 190 | Patricia Crone | b. 1945 (p. 368) | **Consistent** | GND 1945–2015 | https://lobid.org/gnd/131444778.json |
| 191 | Gerd R. Puin | b. 1940 (p. 368) | **Consistent** | GND b. 1940 | https://lobid.org/gnd/170032167.json |
| 192 | al-Hajjaj ibn Yusuf | "end of the first century of the hijrah" (p. 369) | **Consistent** | d. 95/714 (TDV); GND 661–714 | https://islamansiklopedisi.org.tr/haccac-b-yusuf-es-sekafi ; https://lobid.org/gnd/119312026.json |
| 193 | Muhammad ibn Sirin | 653–728 (pp. 370, 329) | **Consistent** | b. 34/654, also reported as 31/651 or 33/653; d. 110/729 (TDV; 110 AH = Apr 728 – Apr 729). GND 653 – 14 Jan 729; BnF 654–728 | https://islamansiklopedisi.org.tr/ibn-sirin ; https://lobid.org/gnd/110642457.json ; https://catalogue.bnf.fr/ark:/12148/cb12482780p |
| 194 | Imam 'Ali Zayn al-'Abidin | d. 712 (p. 370) | **Consistent** | d. Rabi' I 94 / Dec 712, the majority view (TDV); GND 658–710 | https://islamansiklopedisi.org.tr/zeynelabidin ; https://lobid.org/gnd/118914006.json |
| 195 | Patriarch Timothy I | 727/8–823 (p. 371) | **Consistent** | GND 728–823 | https://lobid.org/gnd/115603344.json |
| 196 | Muhammad ibn 'Abd al-Wahhab | "17031792" (p. 372) | **OCR issue** | Reads as 1703–1792: b. 1115/1703, d. 1206/1792 (TDV); GND and BnF 1703–1792 | https://islamansiklopedisi.org.tr/muhammed-b-abdulvehhab ; https://lobid.org/gnd/119152169.json |

**Verdict counts (196 rows):**

| Verdict | Rows |
|---|---|
| Consistent | 141 |
| Minor difference | 10 |
| Inconsistent | 20 |
| Disputed among sources | 16 |
| Unverified | 7 |
| OCR issue | 2 |

## 2. Inconsistent and Disputed rows, most significant first

**Inconsistent (20)**

1. **Row 125 – the Prophet "570-642 CE" (p. 339).** He died in 632 (GND, Wikidata). The book itself prints 570–632 on p. 354 and dates his death 19 years before 651 on p. 85.
2. **Rows 31/71 – Abu Hurayrah "603-681" (pp. 83, 323).** He died in 58/678; the variants are 677 and 679 (TDV, GND, BnF). No source gives 681. He reached Medina only in Muharram 7 AH, which is 5 years after the Sinai date.
3. **Row 48 – al-Mu'tamid "nominal Caliph 878-885" and "(r. 877; 878-879)" (p. 86).** He reigned 870–892. The book's figures are the dates of his viziers al-Hasan and Sa'id ibn Makhlad. These are the very men Mouton's forgery thesis rests on.
4. **Row 161 – Ibn Qayyim "1292/93-1286" (p. 355).** The death date is printed before the birth date. Correct: 1292–1350.
5. **Row 116 – Qaradawi "b. 1956" (p. 337).** Correct: 1926, as the book itself gives on p. 372.
6. **Row 96 – 'Asim ibn Thabit "died at Badr (624)".** He was killed at al-Raji' in 4/625. The error affects the book's identification of the witness "Ibn 'Asir".
7. **Row 98 – 'Amir ibn Rabi'ah "returned to Medina in 615".** The 615 emigrants returned to Mecca. Medina before 622 is impossible.
8. **Rows 20/64 – Kara Mustafa "served Sulayman II from 1663-1666".** In those years he served Mehmed IV, as kapudan pasha and acting grand vizier. Suleiman II reigned 1687–1691, after Kara Mustafa died in 1683.
9. **Row 54 – al-Biruni "937".** Correct: b. 973 (TDV, GND, BnF).
10. **Row 148 – "Sir Charles Eliot (1801-1875)".** These are the dates of Admiral Charles Elliot. The author of *Turkey in Europe* lived 1862–1931.
11. **Row 28 – Leo Frobenius "1873-1973".** He died in 1938.
12. **Row 15 – Fatimids from "901".** Correct: 909.
13. **Row 38 – Ibn Qutaybah "828-885".** He died in 276/889 (TDV, GND, BnF).
14. **Row 126 – Khalid ibn al-Walid "592".** Correct: b. 583–587 (TDV); Wikidata 586.
15. **Row 25 – al-Afdal called "the Fatimid Caliph" and al-Hakim's successor.** He was vizier 1094–1121. The caliph in 1106 was al-Amir, and al-Hakim's successor was al-Zahir.
16. **Row 23 – Arundale's Sinai voyage "1831".** By his own account he left Cairo for Sinai on 29 Aug 1833.
17. **Row 99 – Hisham ibn al-'As "died 635 at Yarmuk".** Yarmuk was in 15/636; 13/634 was Ajnadayn.
18. **Row 80 – Zayd ibn Thabit "d. c. 660".** Reported years are 45, 51 or 55 AH (665+); only English Wikipedia gives 660.

**Disputed among sources (16)**

1. **Rows 22/68 – 'Umar b. 579.** Sources give 568 (GND), 581? (BnF), ≈583 (TDV) and c. 586 (Wikidata/Britannica). None gives 579.
2. **Row 127 – John of Damascus "c. 645 or 676" and "d. 749/764".** TDV lists 640, 645, 655–660, 675 (the majority) and 679 for the birth, and 749 for the death. No source supports 764.
3. **Row 79 – Nafi ibn al-Harith "d. 670, the Prophet's physician".** The physician was his father al-Harith ibn Kalada, who died either 13/634 (TDV's preference) or 50/670. The son's death is given as 634–635 by current English Wikipedia.
4. **Row 93 – 'Amr ibn al-'As "c. 592".** GND ca. 570/575; Wikipedia c. 573; TDV implies c. 603. No source gives 592.
5. **Row 69 – 'Uthman b. 577.** TDV: six years after the Year of the Elephant (≈576); GND 574; BnF 570?.
6. **Row 75 – Hassan ibn Thabit d. 674.** Reported dates are 660, 670, 674 and c. 680 (TDV); GND 660.
7. **Row 32 – Abu al-Darda' converted 623 or 624.** TDV supports 624 (at Badr). No source checked supports 623.
8. **Row 112 – Mu'awiya "king in Jerusalem 659".** Wikipedia: late 660/early 661 and July 661.
9. **Row 140 – al-Maqqari b. 1578.** Sources give 1577? (BnF), 1582 or later (TDV) and 1591 (GND).
10. **Row 6 – Monconys b. 1611.** BnF and GND now give 1608.
11. **Row 83 – 'Ammar b. c. 570.** TDV's "about 93 at Siffin" implies c. 564.
12. **Row 157 – Ibn Sa'd b. 784.** GND, BnF and Wikidata give 784; TDV gives 777.
13. **Row 61 – Barthélemy's find "1850".** The EI2 quotation gives 1850; another source quoted on the same Wikipedia page gives 1858. The place is also given as Akhmim, not "near Saide".
14. **Row 16 – Ayyubids 1174–1249.** The usual dating is 1171–1250. The book's end points are events, not dynastic limits.
15. **Row 18 – Ottomans 1517–1805.** 1805 is Muhammad Ali's appointment. The eyalet formally lasted until 1867.

## 3. Places where the book contradicts itself about the same person

| Person | Conflicting printings | Which is right |
|---|---|---|
| The Prophet Muhammad | 570–642 (p. 339) vs 570–632 (p. 354); p. 85 dates his death 19 years before 651, i.e. 632 | 632 |
| Yusuf al-Qaradawi | b. 1956 (p. 337) vs b. 1926 (p. 372) | 1926 |
| John of Damascus | "c. 645 or 676–749" (p. 340) vs "d. 749/764" (p. 371) | Death is 749 per all checked sources; 764 is unsupported |
| Ibn Qayyim al-Jawziyyah | "1292/93–1286" (p. 355) contradicts itself (death before birth) | 1292–1350; 1286 is Bar Hebraeus' death year, printed immediately before |
| al-Mu'tamid | "nominal Caliph 878–885" and "(r. 877; 878–879)", in adjacent sentences on p. 86 | Neither: he reigned 870–892 |
| al-Afdal | "the Fatimid Caliph al-Afdal", al-Hakim's successor (p. 75, Hobbs passage) vs "Shahan Shah al-Afdal, a powerful chancellor of the Fatimid Empire" (p. 75, from Skrobucha) | Chancellor/vizier |
| al-Hakim | r. 996–1021 (author) vs AD 996–1020 (Skrobucha quotation) | 1021 (TDV); the quote is a minor slip |
| Hudhayfa ibn al-Yaman | "Hudayfah ibn al-Yaman (d. 656)" (p. 84) vs "Abu Hudayfah ibn al-Yaman (d. 656)" (p. 323) | Same date; the kunya on p. 323 is wrong |
| Abu al-Darda' | conversion "after Badr in 624" vs "one year after the hijrah … 623" (p. 83) | The book reports two versions without choosing; TDV supports 624 |
| Ja'far ibn Abi Talib | "d. 629 CE" vs "died during the early years of the hijrah" (p. 326) | 8 AH (629) is not the "early years" |

Checked and found consistent across their repetitions:

- 'Ali (d. 661);
- 'Umar (r. 634–644 / 579–644);
- Mu'awiya (d. 680 / 602–680);
- Ibn Sa'd (d. 845 / 784–845);
- Selim I;
- Hamidullah;
- 'Umar II;
- al-Mutawakkil;
- Abu Hurayrah (603–681 on both pages, consistently wrong);
- Caetani;
- Arundale ("1831" on p. 74 and also on p. 11, consistently wrong).

## 4. Witnesses whose reference dates conflict with a covenant's claimed date of issue

The covenant dates are the book's own:

| Covenant | Claimed date |
|---|---|
| Sinai | 3 Muharram 2 AH ≈ 7 Jul 623 |
| Christians of the World ("CW") | 4 AH ≈ Jun 625 – Jun 626 |
| Najran | 9–10 AH ≈ Apr 630 – Mar 632 |

The witness lists are as the book gives them: Sinai on pp. 323–324 (and p. 74 for Mu'awiya); the "second group" on pp. 324–327, which covers CW 1630, CW 1538, Najran, Assyria and one further text.

| Witness (row) | Covenant | Conflict | Source |
|---|---|---|---|
| Abu Hurayrah (31, 71) | Sinai | Converted and came to Medina in Muharram 7 AH (May 628), about 5 years after 2 AH. The book admits this (p. 323) | TDV ebu-hureyre |
| Mu'awiya (21, 112) | Sinai (fifth witness, p. 74); CW 1630 | Converted with his father during the conquest of Mecca (8/630). That is after both 2 AH and 4 AH. It is not a problem for Najran | TDV muaviye-b-ebu-sufyan |
| Abu al-Darda' (32, 70) | Sinai | Converted at the time of Badr (Ramadan 2 AH ≈ Mar 624), about 8 months after 3 Muharram 2 AH | TDV ebud-derda |
| 'Abbas ibn 'Abd al-Muttalib (74) | Sinai | Fought for the Quraysh at Badr and was captured; he did not emigrate to Medina; formal conversion is perhaps Jan 630. In Muharram 2 AH he was a non-Muslim (at least openly) in Mecca | enwiki Abbas ibn Abd al-Muttalib |
| 'Abd Allah ibn 'Amr ibn al-'As (82) | Sinai (penultimate witness); also on three second-group texts | Born c. 615. Converted before his father, but went to Medina only after 7 AH. His father converted on 1 Safar 8 / 31 May 629. So he was absent in 2 AH and 4 AH | TDV abdullah-b-amr-b-as ; TDV amr-b-as |
| Hamzah (88) | Second group (on two texts) | Killed at Uhud, 3/625. That is before 4 AH and before 9–10 AH, so it is a conflict whichever two texts carry him. The book admits this | TDV hamza |
| Ja'far ibn Abi Talib (100) | Second group (on four of five texts) | In Abyssinia until he joined the Prophet at Khaybar (7/628); killed at Mu'ta (8/629). Conflicts with CW (4 AH) and with Najran (9–10 AH) | TDV cafer-b-ebu-talib |
| Sa'd ibn Mu'adh (78) | All second-group manuscripts, including Najran | d. 5/627, before 9–10 AH. No conflict with Sinai or CW. The book notes the problem | TDV sad-b-muaz |
| Sa'd ibn al-Rabi' (97), proposed by the book for "Ibn Rabiah" | Second group | d. 3/625 at Uhud, before CW and Najran | TDV sad-b-rebi |
| 'Asim ibn Thabit (96), proposed for "Ibn 'Asir" | Second group | d. 4/625 at al-Raji': borderline for CW (same year) and a conflict for Najran. The book's "died at Badr 624" would make it worse | TDV asim-b-sabit |
| Jubayr ibn Mut'im (103), proposed for "Ibn Jubayr" | Second group | Converted 628 (or at the conquest of Mecca), after CW's 4 AH | TDV cubeyr-b-mutim |
| Tamim al-Dari (92), proposed for "Sahl ibn Tamim" | Second group | Converted 9 (630) or 10 (631) AH, after CW's 4 AH; acceptable for Najran | TDV temim-ed-dari |
| Abu Dharr (85) | All second-group texts | Emigrated to Medina after Uhud (3/625) or after the Trench (5/627). On the second report he was not in Medina in 4 AH. This is a possible conflict with CW only | TDV ebu-zer-el-gifari |

No date conflict was found for the other dated witnesses:

- 'Ali, Abu Bakr, 'Umar, 'Uthman;
- Ibn Mas'ud, Zubayr, Talhah;
- Hassan ibn Thabit (converted 622, TDV);
- Zayd ibn Thabit (aged about 12 in 623), Khuzaymah, 'Ammar;
- al-Bara' ibn Malik, Abu Hudhayfa ibn 'Utba, Hisham ibn al-'As;
- Sahl ibn Hunayf, Usamah, Zayd ibn Arqam.

## 5. Unverified rows and why

| Row | Person | Claim | What was tried and why it stays unverified |
|---|---|---|---|
| 30 | 'Abd al-Masih al-Najrani | "martyred in the 860s" (attributed to Griffith) | Wikipedia confirms only "9th century". Griffith's 1985 *Le Muséon* article (doi 10.2143/mus.98.3.2011489) has no abstract online |
| 62 | Tsernotabey | acted in 1517 | No authority record, encyclopedia entry or independent account was found. Only the 1517 conquest is confirmed |
| 110 | Bishop of Adiabene | writing 650–660 | The person is unnamed. Fortescue's text was not opened |
| 123 | Ami Isseroff | d. 2011 | GND, Wikidata, and English and Hebrew Wikipedia (search API) have no biography |
| 185 | Wendell Phillips | 1950 Sinai expedition | His life (1921–1975) is confirmed. The expedition year is not mentioned on the pages I could open; the LoC collection page and HathiTrust returned 403 |
| 187 | M. J. Zohrab | 1822 *Journal asiatique* notice | The 1822 volume was not among the archive.org scans I opened. A "docteur Zohrab" is attested in Paris in 1825–26 |
| 188 | "Gregory" | 1822 *Bulletin des sciences* edition | Not located |

Claims inside otherwise verified rows that I did **not** check:

- the "552 CE" birth year for the Prophet attributed to "a few Western historians" (row 65);
- Griffith's statement that Abdul Hamid II confirmed the Testament in 1904 (row 58; the date only falls within his reign);
- that Rincon's 1532 visit was at Belgrade (row 152);
- that Abraha's 552 campaign was "near Mecca" (row 44; the inscription refers to central Arabia).
