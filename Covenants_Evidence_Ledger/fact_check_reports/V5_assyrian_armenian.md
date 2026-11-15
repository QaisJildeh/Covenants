# V5: Checking Morrow (2013), Chapter 6 (Assyrian Christians) and Chapter 7 (Armenian Christians of Jerusalem) against independent sources

**Book:** John Andrew Morrow, *The Covenants of the Prophet Muhammad with the Christians of the World* (2013), pp. 177–204.

**Input:** the extraction `scratchpad/extract/06_ch6_ch7.md`. IDs used below:
- **T** = row of its timeline table (§2);
- **C** = item in its factual-claims list (§4).

The book's wording was checked against `book/chunks/06_ch6_ch7.txt`. The Assyrian covenant text was checked at PDF pp. 338–347 of `07_texts_ch8_ch12.txt`.

**Method**
- Every verdict rests on a page that was opened, either by me or by one of four sub-checks whose working files are listed below. Search snippets were not used as evidence.
- Full texts came from archive.org, read as djvu text with page images where pagination mattered. Other sources were GEDSH online, Encyclopaedia Iranica, open-access journals, and Wayback snapshots.
- Wikipedia is used only as a lead, or for uncontroversial dates, and is labelled where used.
- **Calendar.** AH→CE conversions use the tabular Islamic calendar (epoch 16 July 622, Julian), cross-checked with the Aladhan API. Treat them as ±2 days.
- **Before marking an item Inconsistent,** I checked for OCR misreadings (several against the book's page images) and calendar spans, and looked for a second source.

**Working files.** Full detail and extra quotations are in these files, all in `/tmp/claude-1000/-home-cool-Documents-Turkey-Trip/7546f7f6-5b83-4cbe-bfaf-72579fbd2e97/scratchpad/verify/parts/`:
- `A_assyrian_sources.md`: Ch. 6 sources;
- `B_ottoman_kurdish.md`: Ottoman, Kurdish and Church-of-the-East chronology, and the digressions;
- `C_islamic_chronology.md`: early-Islamic chronology, 'Umar, 'Ali, Muktafi;
- `D_armenian_golubovich.md`: Armenian material, Golubovich, Thenaud, Avdall, Thomson, the Sharif.

**Verdict legend**
- **Consistent**: independent sources agree.
- **Minor difference**: a spelling slip, an AH/CE span, a wrong page, or a small overstatement.
- **Inconsistent**: reliable sources say otherwise; the row says what they say.
- **Disputed**: sources disagree with each other; the row gives each version.
- **Unverified**: no reliable source could be opened; the row says what was tried.
- **Opinion**: not checkable as fact.

---

## 1. Verification table

### 1a. Timeline rows, Chapter 6 (T1–T60)

| # | Book claim (page) | Verdict | What independent sources say | Source URLs |
|---|---|---|---|---|
| T1 | Jesus "7-2 BCE to 30-36 CE" (p. 184) | Not checked | This is a lifespan and is left to the lifespan agent. | — |
| T2 | Mu'awiya "602-680" (p. 183) | Not checked | Lifespan; left to the lifespan agent. | — |
| T3 | Mu'awiya embraced Islam before the conquest of Mecca, "8 AH or 630", per "most Islamic sources" (p. 183) | **Consistent** | Al-Baladhuri (tr. Murgotten II pp. 272–273): "When Mu'awiyah accepted Islam in the year of the Conquest, he also acted as scribe for Muhammad." Britannica: he did not become a Muslim until Muhammad had conquered Mecca. Ibn Ishaq dates the conquest to 20 Ramadan 8 AH, about 11 Jan 630 (tabular). | https://archive.org/details/originsoftheisla032520mbp ; https://web.archive.org/web/20261027002919/https://www.britannica.com/biography/Muawiyah-I ; https://archive.org/details/GuillaumeATheLifeOfMuhammad (p. 566) |
| T4 | Mu'awiya was the Prophet's scribe "from the year 630 to the year 632" (p. 183) | **Consistent** ("two years" is rounded) | Baladhuri (above); Britannica: "made a scribe in his service". The Prophet died in 632 (Kennedy 2007). That leaves about 2.4 years. | as T3 ; https://archive.org/details/the-great-arab-conquests-how-the-spread-of-islam-changed-the-world-we-live-in-pdf-room |
| T5 | The Assyrian covenant "dates from two years before" 630–632 (p. 183) | **Inconsistent** | The colophon of the very text the book uses dates it otherwise. The English (Malech 1910, p. 230; reprinted in the book at p. 314) reads: "written by Moavijah Ben Sofian ... in the 4th year of the Hegira in the city of Medina". The Persian (Malech p. 222, page image) reads «روز دوشنبه آخر ماه چهارم از سال چهارم از هجرت», "Monday, end of the 4th month of the 4th year of the Hijra". 4 AH = 13 Jun 625 – 1 Jun 626; Rabi' II 4 AH ≈ Sept–Oct 625. That is 4–5 years before 630, not two. | https://archive.org/details/historyofsyriann00male (pp. 222, 230); https://api.aladhan.com/v1/hToG/01-01-0004 |
| T6 | Many delegations met the Prophet "during his final two years" (p. 178) | **Consistent** | Ibn Ishaq/Guillaume pp. 627–628: "THE YEAR OF THE DEPUTATIONS, A.H. 9" (= Apr 630 – Apr 631). | https://archive.org/details/GuillaumeATheLifeOfMuhammad |
| T7 | Salman "d. 654" (p. 178) | Not checked | Lifespan. | — |
| T8 | Salman translated al-Fatiha into Persian with the Prophet's permission (p. 178, Hamidullah) | **Minor difference**: the book states a reported tradition as fact | Tahmasebian & Gould, *IJMES* 56.1 (2024): Salman "is reported to have produced" a translation, a tradition transmitted by al-Sarakhsi (11th c.) from Abu Hanifa. | https://www.cambridge.org/core/product/82977225F39FC98BED07F5B375ABB13C/core-reader |
| T9 | Siemon-Netto: the Prophet "in the 7th century issued a Firman" for the Assyrians (p. 190) | **Consistent** with the cited article | *Christianity Today* (UPI), 1 Aug 2004, quoted accurately. | https://www.christianitytoday.com/ct/2004/augustweb-only/8-2-52.0.html |
| T10 | Emhardt & Lamsa: a decree "written by Ali" was given to "Nestorian Patriarch Essvo Yabh toward the end of the seventh" [century] (p. 180) | Quote **Consistent** (the word "special" is dropped). The date is **Inconsistent** | E&L pp. 75–76 is verbatim. The catholicos meant, Isho'yahb II, reigned 628–645 (GEDSH), and Muhammad died in 632, so "end of the seventh [century]" is impossible. E&L name 'Ali as scribe; Malech names Mu'awiya. | https://archive.org/details/oldestchristianp0000will ; https://gedsh.bethmardutho.org/Ishoyahb-II-of-Gdala |
| T11 | Percy: the firman was originally accorded by Mahomet to "Ishy Yau, the then Patriarch of the East, residing at Bagdad", through "Said the Christian Prince of Najran" (Bar Hebraeus via Assemani) (p. 179) | Quote **Consistent**. "Residing at Baghdad" is **Inconsistent** | Percy (Royal Institution *Notices* XVI, pp. 645–646) is verbatim. GEDSH: Isho'yahb II (628–45) sat at **Seleucia-Ctesiphon** and withdrew to Karka in Beth Garmai when the Arabs took it in 637/8. Baghdad was founded in **762**, and catholicoi resided there only from c. 780 (GEDSH "Baghdad"; Wilmshurst pp. 473–474). Bar Hebraeus (*Chron. Eccl.* III cols. 115–118) and Assemani (*BO* III/1 p. 108) do report a "diploma" obtained with Said of Najran. | https://archive.org/details/noticesofproceed1618roya ; https://gedsh.bethmardutho.org/Ishoyahb-II-of-Gdala ; https://gedsh.bethmardutho.org/Baghdad ; https://archive.org/details/the-martyred-church ; https://archive.org/details/BarHebraeusChroniconEcclesiasticumVol.3 ; https://archive.org/details/bub_gb_dqIBok_FOLEC |
| T12 | Wigram, *The Assyrians* **33**: under "Omar the Khalif" the Assyrian Church had millet status, exemption from military service, could repair but not build churches, and so on (p. 180) | **Minor difference**: the text is accurate but the page is wrong | Wigram, *The Assyrians and their Neighbours* (1929), **pp. 76–77**, nearly verbatim (page image checked). Wigram does not link these terms to a covenant of the Prophet. | https://archive.org/details/assyrianstheirne0000wigr |
| T13 | After the conquest of Mecca the Prophet had all pictures in the Ka'ba erased except Jesus and Mary (Ibn Ishaq 552). Per Waqidi and Azraqi, he covered the icon with his hand and spared Abraham's picture; another tradition erases Abraham (pp. 187–188) | The Ibn Ishaq part is **Consistent**. The Abraham detail is **Inconsistent / Unverified** | Guillaume p. 552 has the sentence verbatim, but inside a bracketed passage that Guillaume restores from al-Azraqi. It is not in Ibn Hisham. King's study of Azraqi has the hand over the image of Mary/Jesus, and has Abraham's picture *condemned* ("divining with arrows"). Ibn Hisham's note 806 also erases Abraham. No opened source spares Abraham. Waqidi (Faizer tr. p. 411) was not opened. King also shows Azraqi carries conflicting reports (all pictures wiped vs. Jesus–Mary spared). | https://archive.org/details/GuillaumeATheLifeOfMuhammad ; https://dergipark.org.tr/tr/download/article-file/581221 |
| T14 | The Ka'ba images survived until the Umayyad destruction of the Ka'ba in 683 (p. 188, King 219–220) | **Consistent** | King (Turkish tr., pp. 175–176): in 64/683 the Umayyads besieging Ibn al-Zubayr bombarded and burned the Ka'ba, the "final destruction" of the paintings. | https://dergipark.org.tr/tr/download/article-file/581221 |
| T15 | Before 711 the Jews of al-Andalus invited the North African Muslims to liberate them (p. 189, Levy 169) | **Disputed**; the specialist view is against | Roth, *Jews, Visigoths and Muslims in Medieval Spain* (1994) pp. 73–74: "There is no evidence whatever" for a Jewish conspiracy to bring about the invasion. The "betrayal" story is a later Christian legend. Levy p. 169 was not accessible. | https://archive.org/details/jvam_20240413 |
| T16 | Jews aided the Arabs in capturing Byzantine cities (p. 189, Armour 27) | **Unverified** | Lewis, *The Jews of Islam*, was searched and has nothing on armed aid. Armour was not accessible. | https://archive.org/details/the-jews-of-islam |
| T17 | The Franks sacked Constantinople in 1204 (p. 187) | **Consistent** | *Encyclopedia of the Ottoman Empire* (EOE): the Latins took the city in 1204 (Fourth Crusade). | https://archive.org/details/encyclopedia-of-the-ottoman-empire |
| T18 | Into the 13th c. Eastern Christians called themselves Nasraye (p. 184, Jenkins 7) | **Consistent** with Jenkins | Jenkins 2008 p. 7. | https://archive.org/details/the-lost-history-of-christianity |
| T19 | Mamluks "(1250-1517)" (p. 188) | **Consistent** | EOE "Mamluk Empire": 1250 to the Ottoman conquest of 1516–17. | https://archive.org/details/encyclopedia-of-the-ottoman-empire (p. 348) |
| T20 | Mehmet II "r.1444-1446 and 1451-1481" (p. 187) | **Consistent** | EOE p. 243. | same |
| T21 | 1453: Hagia Sophia converted to a mosque (p. 187) | **Consistent** | EOE p. 243. | same |
| T22 | Selim I "r. 1512-1520" (p. 177) | **Consistent** | EOE "Selim I"; Iranica: acceded 1512, died 21 Sept 1520. | same ; https://www.iranicaonline.org/articles/ottoman-persian-relations-i-under-sultan-selim-i-and-shah-esmail-i/ |
| T23 | "In 1517 Sultan Selim came from Constantinople to Baghdad". Patriarch "Shimon the fourth" showed him the covenant; Selim kept the original in the Constantinople treasury and gave him a signed copy, "still extant" (p. 177; restated p. 180) | Quote **Consistent** with Malech p. 221. The event is **Inconsistent** on three counts | (a) **Selim never went to Baghdad.** It was Safavid from 1508 until the Ottomans took it in **1534** (Iranica "Iraq iv"). Selim's 1514–18 route (Chaldiran, Tabriz, Marj Dabiq, Cairo, Damascus) never touched it (Iranica; EOE). (b) **The patriarch in 1517 was Shem'on VI (1504–38).** Shem'on IV Basidi died in 1497 (Wilmshurst; Baum & Winkler). Malech's own list (p. 314) gives "Shimon VI, 1504-1538". (c) **No patriarch had lived at Baghdad since Makkikha II (1257–65)** (Wilmshurst). Malech gives no source for the anecdote. | https://archive.org/details/historyofsyriann00male (pp. 221, 314); https://www.iranicaonline.org/articles/iraq-iv-safavid-period/ ; https://archive.org/details/the-martyred-church ; https://archive.org/details/the-church-of-the-east-a-concise-history |
| T24 | The Sinai covenant shared "the same fate" (Selim, 1517) (p. 177) | **Consistent as tradition**; undocumented as an event | Atiya (1950) p. 51: "The existing tradition is that the original charter was taken ... by Sultan Selim I". Moritz (1918) p. 5: by tradition Selim *or Suleiman*; Selim's supposed visit to Sinai "sicher erfunden" (certainly invented). Golubovich: "Selim's firman" is first mentioned in 1638. | https://archive.org/details/dli.ministry.17394 ; https://archive.org/details/beitrgezurgesc00moriuoft ; https://archive.org/details/golubovichbibliotecabi4 |
| T25 | 1517 was the culmination of Selim's wars "first in Persia, and then in Palestine and Egypt", leaving an empire of "nearly one billion acres" (p. 178) | Sequence **Consistent**. Area **Inconsistent** | Chaldiran 1514, Marj Dabiq 1516, Raydaniyya and Cairo 1517 (Iranica; EOE). EOE "Selim I": the empire grew "from 341,100 square miles in 1512 to 576,900 square miles in 1520", about **369 million acres**, not a billion. The book's figure matches the May 2012 Wikipedia wording ("almost 1 billion acres"); that is a probable origin, not a proven one. | https://archive.org/details/encyclopedia-of-the-ottoman-empire (p. 511); https://en.wikipedia.org/w/index.php?oldid=495375422&action=raw (lead) |
| T26 | Persian-speaking professors judged the language "consistent with that used in 17th-century Persia" (p. 178) | **Unverified** (the colleagues are unnamed) | No published linguistic analysis was found. Reynolds (2014) also dates the Assyrian covenant to the 17th century (see §4). | http://web.archive.org/web/20151030230243/http://www.firstthings.com/article/2014/02/briefly-noted |
| T27 | A hypothetical Safavid "Shi'ite recension" (p. 178) | **Opinion** | The Persian text uses the Shi'i-style formula «صلى الله عليه وآله» ("and his family") and «علی ابن ابی طالب علیه السلام» (Malech pp. 222, 227, page images). That is consistent with an Iranian Shi'i milieu but does not date the text. | https://archive.org/details/historyofsyriann00male |
| T28 | Persian prose writers could use the archaic style "into the early twentieth century" (p. 178) | **Unverified** (vague) | Not checked. | — |
| T29 | The document "has been preserved among the Christians for many centuries" (Malech) (p. 177) | **Consistent** with Malech p. 221 | Verbatim. | https://archive.org/details/historyofsyriann00male |
| T30 | Browne: "About 170 years ago, part of the people living in the (Mosul) plains broke away from the Patriarch (the Mar Shimun) and formed the Chaldean Church" (p. 181) | Quote **Consistent**, but the parentheses are the book's own. Date: **Minor difference**. "(the Mar Shimun)": **Inconsistent** | Browne (1936–37) has no "(Mosul)" or "(the Mar Shimun)". Counting back gives c. 1766. GEDSH dates the Chaldean lines to 1553, 1681 and 1830, but also notes that by 1767 about 100 of Alqosh's 500 families were Catholic. The Mosul-plain Christians belonged to the Eliya-line patriarchs (Alqosh/Rabban Hormizd), not to Mar Shimun of Qudshanis (Wilmshurst p. 474). | http://web.archive.org/web/20260305093811/https://www.atour.com/history/1900/20030922a.html ; https://gedsh.bethmardutho.org/Chaldean-Catholic-Church ; https://gedsh.bethmardutho.org/Alqosh ; https://archive.org/details/the-martyred-church |
| T31 | Bedir Khan born "c. 1800" (p. 182) | Not checked | Lifespan. For the lifespan agent: sources give 1802 or 1803. | — |
| T32 | Bedir Khan became "the first leader of the Emirate of Botan" around 1820 (p. 182) | **Inconsistent** ("first") | Iranica: the "**last** ruler of the principality of Cizre-Botan", an old Kurdish principality. Aboona: in the 1830s he was still assistant to Mir Saif al-Din. Wikipedia (lead, citing Jongerden 2012) gives his rule as 1821–47. | https://www.iranicaonline.org/articles/bedir-khan-badr-khan-d/ ; https://archive.org/details/HirmisAboonaAssyriansKurdsAndOttomansIntercommunalRelationsOnThePeripheryOfTheOttomanEmpire |
| T33 | Surma: the firman and knife were preserved "to the time of Bedru Khan Beg (1845)", then stolen, not destroyed; Bedr Khan cursed Nurullah Beg (p. 181) | Quote **Consistent** ("requite" for Surma's "require"). The year 1845 is **Inconsistent** | Surma (1920, ch. IX) says this and dates the war "some seventy-five years ago". The documented Badr Khan/Nurullah massacres were in **1843** (Tiyari) and **October 1846** (Tkhuma). No massacre is recorded for 1845 (Wilmshurst pp. 373–374; GEDSH "Hakkari" "1843–46"; Layard 1849). | http://web.archive.org/web/20070404200218/http://www.aina.org:80/books/acc/acc.htm ; https://gedsh.bethmardutho.org/Hakkari ; https://archive.org/details/the-martyred-church ; https://archive.org/details/remainswithaccount00laya |
| T34 | Wigram: preserved until the middle of the 19th c.; it "perished in the 'Massacres of Bedr Khan Beg'" (p. 181) | **Consistent** | Wigram 1910 p. 310, verbatim; it calls the object "a document, purporting to be the grant". The period matches 1843–46. | https://archive.org/details/introductiontohi0000wawi ; https://gedsh.bethmardutho.org/Hakkari |
| T35 | Stafford 95: a catastrophic massacre in 1847 destroyed the firman (p. 181) | Substance **Consistent**, with one omission. The 1847 massacre date is **Inconsistent** | Stafford (AINA e-text pp. 83–84): "Until Badr Khans massacres ... in 1847, a firman had been preserved by the Patriarch ... the gift either of the Prophet Mohammed himself **or of the Khalif Omar**". The book omits the 'Umar alternative, and Stafford does not say "destroyed". **1847 is the year the Ottomans defeated Badr Khan**; the massacres were 1843 and 1846. p. 95 of the 1935/2006 print is unverified. | https://archive.org/details/the-tragedy-of-the-assyrians ; https://archive.org/details/the-martyred-church ; https://dergipark.org.tr/en/download/article-file/4224379 |
| T36 | Browne: in 1847 the Wali of Mosul organised "a political massacre"; Bedir Khan with Turkish troops attacked; the firman was destroyed (p. 181) | Quote mostly **Consistent**. The 1847 date is **Inconsistent**. The Mosul role is **partly supported** (for 1843) | Browne: "until the year 1847, when the Wali of Mosul ... Instigated by him, and helped by Turkish troops ... Bedir Khan Beg attacked ... the firman of Mohammed was destroyed". The phrase "organized ... a political massacre" is not in the online transcription, which is defective there. Ottoman complicity in **1843** is documented: Kurds asked permission of the governors of Mosul and 'Amadiya and "it was willingly given" (Wilmshurst); Canning to Aberdeen, 17 Aug 1843 (Aboona). | Browne (Wayback, as T30); https://archive.org/details/the-martyred-church ; Aboona (as T32) |
| T37 | Yelda: the firman "disappeared without a trace" in 1847 (p. 182) | **Consistent** with the cited article. The date itself is **Disputed** | CT 2004: "The Firman disappeared without trace in 1847, Yelda told United Press International". Other sources: Yohannan 1916 p. 78, "preserved till **1843**"; Theodore d'Mar Shimun's own book, family in Mosul by 27 July 1843. | CT (as T9); https://archive.org/details/deathanationore00yohagoog ; https://marshimun.com/wp-content/uploads/2025/11/The-History-of-the-Patriarchal-Succession-of-the-dMar-Shimun-Family-Updated-Version.pdf |
| T38 | Bedir Khan was defeated by the Ottomans in 1847 and exiled to Crete; the massacres were ended by the Turks under British and French pressure (p. 182) | **Consistent**; the French role is a **Minor difference** | 1847 defeat: Wilmshurst; EOE "Kurds"; Akpınar 2025. Exile to Crete (Kandiye): Iranica; Akpınar. British pressure (Canning) is well documented. No specific French démarche was found in the sources opened. | https://www.iranicaonline.org/articles/bedir-khan-badr-khan-d/ ; https://dergipark.org.tr/en/download/article-file/4224379 ; https://archive.org/details/encyclopedia-of-the-ottoman-empire |
| T39 | The patriarchal family had to flee in the mid-19th c. (p. 182) | **Consistent** | Shem'on XVII Abraham fled to Mosul in 1843 and stayed nearly four years (Wilmshurst p. 374; Aboona ch. 12). | https://archive.org/details/the-martyred-church ; Aboona |
| T40 | At Dizan the satchel with decree and dagger was left behind in a Kurdish attack, stolen and taken to Bedr Khan (Theodore) (p. 181) | **Consistent** with Theodore's text. The incident is not independently attested | Theodore's book (updated PDF p. 24) is verbatim. It is printed straight after a reprint of Surma's chapter, so it is not independent of Surma, and it dates these events to 1843. Canning (1843, via Aboona): Bedr Khan "had destroyed and plundered Diz". | Theodore PDF (as T37); Aboona |
| T41 | Hormizd overheard Bedr Khan's son in an Istanbul coffeehouse; a great-grandson spoke in Cyprus (p. 181) | **Consistent** with Theodore; otherwise **Unverified** | This is oral family testimony with no independent check. | Theodore PDF |
| T42 | "In 1856" the Ottomans used Bedir Khan to crush Cretan Greek rebels and rewarded him with a move to Damascus (p. 182) | **Inconsistent** | Akpınar 2025 (citing Doğan 2010 and Kardam 2011): pardoned in **1857** with pasha rank; to Istanbul 1861 or 1863; to **Damascus 1868**. No opened source has him crushing a Cretan revolt; the Great Cretan Revolt (1866–69) came after he left Crete. Wikipedia (lead): he mediated between Christians and Muslims on Crete. | https://dergipark.org.tr/en/download/article-file/4224379 ; https://en.wikipedia.org/w/index.php?title=Bedir_Khan_Beg&action=raw (lead) |
| T43 | Died in Damascus "in 1868"; "forty to ninety sons", 22 confirmed (p. 182) | Death year **Disputed**. Sons: **Minor difference** | Iranica: died 1868 (headword "d. 1867"); Akpınar/Doğan: 1869. Iranica: "as many as ninety or ninety-nine **children**", with "twenty-one sons and twenty-one daughters" alive at his death. Akpınar: 21 sons. | Iranica (as T38); Akpınar |
| T44 | Emhardt & Lamsa: the document was treasured by the family "until the end of the last [19th] century" and "is now said to be in the Ottoman Museum" (p. 180) | Quote **Consistent**. The claim is **Unverified** and partly contradicted | E&L pp. 75–76 verbatim. Most other sources date the loss to 1843–47. The Topkapı list of the Prophet's letters (Küçükaşcı, *A History of Istanbul*) includes no covenant with Christians. | https://archive.org/details/oldestchristianp0000will ; https://istanbultarihi.ist/546-sacred-relics-in-istanbul |
| T45 | Percy: "When the Turkish troops occupied the village at the time of my visit in 1899, this was the only article which they ... carry away". The author says the date "seems off by nearly half a century" (pp. 181–182) | Quote **Consistent**. The book's reading is **Inconsistent** | Percy p. 645 is verbatim, and his summer 1899 journey is confirmed (*Highlands of Asiatic Turkey*, 1901). Percy's object is the **Jelu (Mar Zaia) handkerchief "covered with Arabic writing"**, not the patriarchal parchment firman. Surma and Wigram (1910 p. 310 n.) also keep the two apart. There is no half-century conflict: they are two different relics. | https://archive.org/details/noticesofproceed1618roya ; https://archive.org/details/highlandsasiati00percgoog ; Surma (as T33); https://archive.org/details/introductiontohi0000wawi |
| T46 | The covenant remained common knowledge "well into the 19th century" (p. 190) | **Opinion** | — | — |
| T47 | A Mollah of Julamerk read the document annually in public (Surma) (p. 179) | **Consistent** with Surma | Surma ch. IX. Not independently attested. | Surma (as T33) |
| T48 | 1912: Bliss on shrines shared by Muslims, Christians and others (pp. 188–189) | **Consistent** | Bliss, *The Religions of Modern Syria and Palestine* (1912) pp. 27–28, wording matches. 1912 is the date of publication. | https://archive.org/details/religionsofmode00blis |
| T49 | Early 20th c.: Muslims asked Christians to parade relics against an epidemic (p. 189) | **Consistent** with Jenkins | Jenkins p. 205 (citing Hasluck). | https://archive.org/details/the-lost-history-of-christianity |
| T50 | 1915: Turkish troops and Kurdish tribes slaughtered the Christians of Jilu; survivors fled to Salmas. The author takes Yelda's "before they set out to kill 30,000 Christians" to mean 1915 (p. 182) | 1915 events **Consistent**. Reading Yelda as 1915 is **Inconsistent** with the cited source | GEDSH "Hakkari": the Jilu men withdrew to Persia in 1915, and 25,000 reached Salmas by end Sept 1915. Gaunt (2006) pp. 143–144: Ottoman–Kurdish attacks from June 1915, and the Mar Zaya church in Jilu "destroyed together with all its priceless contents". **But the cited article says "The massacre of 30,000 Christians in 1847 was succeeded by another in 1896. In 1915 ... 250,000 Assyrians"**, and attributes the destruction belief to "Assyrians", not Yelda. | https://gedsh.bethmardutho.org/Hakkari ; https://archive.org/details/massacres-resistance-protectors-muslim-christian-relations-in-eastern-anatolia-d ; CT (as T9) |
| T51 | The covenant was destroyed "at some later point" than 1845/47 but before 1915 (p. 182) | **Opinion**, unsupported | This inference rests on merging the two relics (T45) and on misdating Yelda's massacre (T50). | as T45, T50 |
| T52 | 1935: Hagia Sophia turned into a museum (p. 187) | **Minor difference** | Council of Ministers decree of **24 Nov 1934**; opened as a museum on **1 Feb 1935** (Akan 2020; EOE "1934"). | https://dergipark.org.tr/en/download/article-file/1184889 ; EOE |
| T53 | 1990s: Muslims visited the Virgin of Seidnaya (p. 189) | **Consistent** with Jenkins | Jenkins p. 205 (citing Dalrymple). | Jenkins |
| T54 | "End of the twentieth century": Canada recognised Quebec as a nation; Spain recognised Catalonia, Galicia and the Basque Country as autonomous (p. 184) | Quebec **Inconsistent**. Spain **Consistent** | House of Commons motion "the Québécois form a nation within a united Canada", adopted **27 Nov 2006**. Spain: Basque and Catalan statutes of 18 Dec 1979; Galicia, 6 Apr 1981. | https://www.noscommunes.ca/Content/House/391/Journals/087/Journal087.PDF ; https://boe.es/boe/dias/1979/12/22 ; https://www.boe.es/eli/es/lo/1981/04/06/1 |
| T55 | March 2001: the Taliban destroyed the Bamiyan Buddhas, inspired by Salafism (p. 184) | Date **Consistent**; "Salafism" is **Opinion** | UNAMA: destroyed "by the Taliban regime in March 2001". | https://unama.unmissions.org/en/node/61683 |
| T56 | Early 21st c.: Sufi centres in Qom destroyed and turned into parking lots (p. 185) | **Consistent** (one centre, 2006) | IPS 2007: the Gonabadi hosseiniyeh in Qom was bulldozed and "converted into a parking lot". RFE/RL: demolished in 2006. | https://www.ipsnews.net/?p=26822 ; https://www.rferl.org/a/1495342.html |
| T57 | March 2012: the Saudi Grand Mufti ruled "All churches in the Arabian Peninsula must be destroyed" (p. 185) | **Consistent as reported** (secondhand) | USDOS 2012 IRF report: "reportedly stated that all churches in the Arabian Peninsula should be demolished". The Kuwaiti MP who asked the question later said he meant a ban on new churches (The World). | https://www.justice.gov/eoir/vll/country/DOS_IRF/2012/Saudi%20Arabia.pdf ; https://theworld.org/stories/2012-03-16/saudi-mufti-says-destroy-all-churches-arabian-peninsula ; https://www.christiantoday.com/news/destroy-all-churches-says-saudi-arabian-islamic-leader |
| T58 | 2012: Ahmad al-Hasani al-Baghdadi's edict against Iraqi Christians (p. 185) | **Consistent as reported** (Dec 2012) | Worthy News, 21 Dec 2012. The AsiaNews original returned 403. | https://www.worthynews.com/12042-fatwa-threatens-iraqi-christians |
| T59 | The lethal attacks on churches in Iraq violated the Prophet's will (Siemon-Netto) (p. 190) | **Consistent** with the cited article | CT 2004: "The lethal attacks on five churches in Iraq violated the stated will of the prophet Muhammad". | CT (as T9) |
| T60 | "Assyrian tradition relates" that a Hanbali plot in Baghdad led to a church being burned with 500 people inside (Yohannan 98–99) (p. 180) | **Minor difference** (framing) | Yohannan pp. 98–99 tells it as a dated chronicle event under the caliph al-Qadir (991–1031), with a footnote to Bar Hebraeus. The church was **Jacobite**, and the story is not presented as "Assyrian tradition". | https://archive.org/details/deathanationore00yohagoog |

### 1b. Timeline rows, Chapter 7 and the Part II divider (T61–T98)

| # | Book claim (page) | Verdict | What independent sources say | Source URLs |
|---|---|---|---|---|
| T61 | "Zeki al-Din": Abraham, the first Armenian patriarch, went to Muhammad "in 626" (p. 191, via the Belleville Armenian Church site) | Quote **Consistent**. Zeki al-Din **Unverified**. The event is **Inconsistent** with chronology | The archived Belleville page (content "used by permission of The Mother See") has the sentence verbatim. No Arab historian "Zeki al-Din" could be identified. In 626 (4 AH) Muhammad lived in Medina; Mecca was taken only in Dec 629/Jan 630. Abraham's tenure on the traditional roster begins in 638. | http://web.archive.org/web/20130313125607/http://bellevillearmenianchurch.org:80/armtoday11.htm ; https://archive.org/details/Sanjian1965ACSOD |
| T62 | Dadoyan: 'Ali made a similar arrangement "626/4H" (p. 200) | **Minor difference** (4 AH = 625/626). The tradition is anachronistic | Sanjian 1965 n. 2 and 1981 p. 429: the charter 'Ali "is alleged to have granted ... in 4 A.H. [= A.D. 625]". 'Ali became caliph only in 656. | https://archive.org/details/Sanjian1965ACSOD ; https://arar.sci.am//Content/381972/424-448.pdf |
| T63 | Azadian: Patriarch Abraham went to Mecca in the 7th century to obtain privileges from the Prophet (p. 191) | Quote **Consistent**. Historicity **Disputed** (specialists reject it) | The sentence is in Azadian's *Mirror-Spectator* opinion column (29 May 2011); the book calls this "Armenian historians". Sanjian calls the charter "apocryphal"; Azarya: "Scholars doubt the authenticity". | http://web.archive.org/web/20260421094726/https://mirrorspectator.com/2011/05/29/jerusalem-in-limbo/ ; https://archive.org/details/Sanjian1965ACSOD ; https://archive.org/details/azarya1984aqjbackground |
| T64 | Krikorian, via Hagopian: Abraham (638–669) "had trekked all the way to Mecca" (p. 191) | **Minor difference** (attribution) | The words are Hagopian's own, in his review of Krikorian's book (*Armenian Reporter*, 14 May 2011). | http://web.archive.org/web/20110530032136/http://www.reporter.am:80/go/article/2011-05-14-jerusalem-armenian-story-finally-being-told |
| T65 | Dadoyan: the "Prophet's Oath" was granted to a deputation from Jerusalem "in Medinah ... during early 630s, if not earlier" (p. 200) | **Consistent** (snippets only; p. 60 not seen) | Google Books snippets of Dadoyan (2011) confirm the section. Place: Medina (Dadoyan) vs. Mecca (Sanjian's summary, Azadian, Hagopian). | https://www.google.com/books/feeds/volumes?q=%22Prophet%27s+Oath%22+%22Medinah%22+%22Armenian+Patriarch%22+Dadoyan |
| T66 | The covenant was most likely obtained in Medina (p. 191) | **Opinion** | — | — |
| T67 | Abraham I patriarch "638–669"; "he had two full years in order to obtain a firman ... from the Prophet" (p. 191) | Dates **Consistent** with the traditional roster. "Two full years": **Inconsistent** | Sanjian 1965 pp. 96–97: the roster "begins with the reign of Abraham who, upon the Arab conquest of Jerusalem in 638, allegedly received a charter from the Caliph Umar". A tenure beginning in 638 starts six years after the Prophet died (632). The title "patriarch" is generally dated from **1311** (Sanjian; Azarya, "more likely"). | https://archive.org/details/Sanjian1965ACSOD ; https://archive.org/details/azarya1984aqjbackground |
| T68 | 'Umar caliph "634-644" (p. 200) | **Consistent** | Kennedy 2007: "Umar (634-44)". | https://archive.org/details/the-great-arab-conquests-how-the-spread-of-islam-changed-the-world-we-live-in-pdf-room |
| T69 | 'Umar, "the Conqueror of Jerusalem in 638" (p. 193) | **Disputed**; 638 is the conventional date | Versions run from 634/5 to 638; see §2. 638: Baladhuri "year 17", El-Awaisi "Muharram 17/Feb 638". 637: Kaegi, and Mango & Scott ("by Dec. 637"). 636/637: Tabari/Sayf "year 15", Michael the Syrian. 634/5: Theophanes. | https://archive.org/details/originsofislamic00balarich ; https://dergipark.org.tr/download/article-file/294102 ; https://archive.org/details/walter-e.-kaegi-byzantium-and-the-early-islamic-conquests-1992 ; https://archive.org/details/chronicle-of-theophanes-the-confessor ; https://archive.org/details/the-history-of-al-tabari ; https://archive.org/details/MichelLeSyrien2 |
| T70 | The Achtiname of 'Umar to Sophronios is dated "20th of Rabi' al-Awwal of the 15th year of the hijrah" (pp. 193–194; no CE date given) | The date matches the document. As history it is **Inconsistent** | 20 Rabi' I 15 AH ≈ **2 May 636** (Julian). That is before Yarmuk (20 Aug 636, Kaegi) and before every surrender date in the Muslim sources and in modern estimates (637–638). The Greek Patriarchate's site itself glosses it "(636)". El-Awaisi (2000), analysing the Patriarchate's MS 552, judges the text Ottoman-era, "either forged or at least concocted" (see §4). | https://api.aladhan.com/v1/hToG/20-03-0015 ; https://dergipark.org.tr/download/article-file/294102 ; https://web.archive.org/web/20130806041255/http://www.jerusalem-patriarchate.info/en/axtinames.htm |
| T71 | 'Ali caliph "656-661" (p. 200) | **Consistent** | Kennedy; Tabari XVII ('Ali killed Ramadan 40 = Jan 661). | Kennedy ; Tabari |
| T72 | The Covenant of 'Ali is dated "Safar, 40th year of the hijrah" (p. 195) | **Consistent** | Avdall 1870 p. 60ff. has it, with the gloss "June, July, 660". Tabular: Safar 40 = 16 Jun – 14 Jul 660. | https://archive.org/details/journalofasiatic39asia ; https://api.aladhan.com/v1/hToG/01-02-0040 |
| T73 | "660 CE, just one year prior to his martyrdom" (p. 194) | **Minor difference** | 'Ali was killed 17–21 Ramadan 40 (24–28 Jan 661), about 6–7 months after Safar 40 (Tabari XVII p. 213). "A year before" is Avdall's rounding. | Tabari ; Avdall |
| T74 | 'Ali's martyrdom one year after 660 (p. 194) | **Consistent** (as a year) | January 661. | Tabari |
| T75 | "The treatises of Muawiyah and Ibn Maslamah were 'reconfirmations' of the ... 'Prophet's Oath'" (p. 200, Dadoyan) | The treaties are **Consistent**; "reconfirmations" is an **Armenian view** | Sebeos (tr. Thomson): T'eodoros Rshtuni's treaty with Mu'awiya, 652/653. Baladhuri (Hitti pp. 314–315): Habib b. Maslama's treaty with Dabil (Dvin). Neither treaty mentions a covenant of the Prophet. | https://archive.org/details/armenian-history-attributed-to-sebeos-liverpool-university-press-translated-text ; https://archive.org/details/originsofislamic01albauoft |
| T76 | The Umayyads "'renewed'" the Oath in 703 and 719 (p. 200) | **Consistent** as a report of Armenian opinion. The events are **Unverified** | A Dadoyan snippet frames this as "as it was often said". The book later turns it into her own finding (p. 200). | https://www.google.com/books/feeds/volumes?q=%22renewed%22+%22Prophet%27s+Oath%22+%22703+and+719%22 |
| T77 | 1138: Caliph Muktafi II's Charter of Protection to the Nestorian Church, following "the precedent of the imams" and the Orthodox Caliphs (p. 198) | **Consistent** (date and wording). The author's gloss is **Opinion** | Mingana, *BJRL* 10 (1926) 127–133, text p. 132. It is an **investiture diploma for Catholicos 'Abdisho' III**, and it does **not** mention any covenant of the Prophet. AH 533 began 8 Sep 1138. The bibliography's "1925" is a minor slip; the article appeared in Jan 1926. | https://archive.org/details/bulletinofjohnry1011unse |
| T78 | 1187: Salah al-Din entered Jerusalem and granted the Armenians special protections; his oath is "accepted as authentic" (pp. 199–200) | **Consistent** | Lane-Poole (1898) p. 230: capitulation signed Friday 2 Oct 1187 (27 Rajab 583). Sanjian (1965, pp. 170–171) says Saladin's charter "has all the earmarks of being authentic" and that it cites earlier pacts of the Prophet, 'Umar and 'Ali. | https://archive.org/details/saladinandfallk03lanegoog ; https://archive.org/details/Sanjian1965ACSOD |
| T79 | Samuel of Ani wrote "in the 13th century" (p. 200) | **Inconsistent** (minor) | Thomson (1986) p. 842: "writing at the end of the twelfth century". | https://archive.org/details/thomsonmuhammadislamarmlit |
| T80 | The Sinai covenant "had been endorsed by religious authorities at regular intervals over the previous five hundred years" ("five centuries of fatwas") (p. 192) | **Inconsistent** (overstated) | The extant Sinai decrees begin in **1130** (Atiya) or **1134** (Moritz), about 385 years before 1517. They are rulers' decrees, not fatwas. Explicit references to a "protection letter of the Prophet" appear only in late Mamluk decrees (Moritz pp. 4–5). | https://archive.org/details/dli.ministry.17394 ; https://archive.org/details/beitrgezurgesc00moriuoft |
| T81 | 1512: Jean Thenaud saw at St Catherine's a mosque holding Muhammad's privileges to the monks, "signed by his palm-print" (Thenaud 72) (pp. 192–193) | **Consistent** (the edition date in the bibliography is wrong) | Schefer's edition p. 72: "privilèges que Mahommet donna es caloyers ... immunité de tous tributz ... signez de sa main, plongée en encre". The edition is Paris: Leroux, **1884**, not 1874. The journey of 1511–12 is confirmed. | https://archive.org/details/levoyagedoutreme00then |
| T82 | "The original is reported to have been taken to Istanbul by Selim I in 1517" (p. 192) | **Consistent as tradition** | Atiya p. 51; Moritz p. 5 (Selim or Suleiman). | as T24 |
| T83 | Golubovich: the "Pact of Muhammad" appeared around 1569 (p. 192) | **Consistent**, with a clarification | 1569 is the date of an **Ottoman Turkish translation** (Nov 1569), registered in 1638; Golubovich infers "prima del 1569 non si aveva traccia alcuna" (no trace before 1569). Thenaud (1512) and Mamluk decrees refute that inference. | https://archive.org/details/golubovichbibliotecabi4 |
| T84 | The Pact predates the Ottoman conquest of Sinai (p. 193) | **Consistent** as to existence; it does not bear on authenticity | Thenaud 1512; Qansuh al-Ghuri's decree (1505 or 1515) cites the Prophet's letter (Moritz). Moritz still judges the charter a medieval forgery. | Thenaud ; Moritz |
| T85 | Golubovich dates most forgeries to 1630–1634 under Murad IV (p. 192) | **Consistent** | Golubovich: the 'Umar firman "apparve la prima volta nel 1630" (first appeared in 1630) and was condemned by Murad IV's firman of 1040/1630; the "three gates" detail dates it to "il periodo 1629-1634". He gives Murad IV's reign as 1623–40. | https://archive.org/details/golubovichbibliotecabi4 |
| T86 | "(1333)" in Golubovich's title (p. 191) | **Consistent** | The title includes 1333, the year Golubovich gives for the Franciscans' legal possession of the Holy Places. | https://openlibrary.org/works/OL42220000W ; Golubovich |
| T87 | The Covenant of 'Ali translated into Armenian by Gregor Campan in 1767, then by Saragian (p. 194) | **Consistent** | Avdall p. 60: "Gregor Campan, on the 15th January 1767, in Astrachan". | https://archive.org/details/journalofasiatic39asia |
| T88 | Authenticated by Joakim Gregor Bagratuni in 1804 (p. 194) | **Consistent** | Avdall p. 60. | same |
| T89 | 1869: Avdall's Cufic copy, lent to Henry Torrens, Vice-President of the Asiatic Society, was lost (p. 194) | **Consistent** | The paper is marked "[Received 23rd September, 1869.]"; Avdall's statement is verbatim. | same |
| T90 | Avdall's translation published in *JASB* 1870 (p. 194) | **Consistent** | *JASB* 39 pt. 1 (1870) pp. 60–64. | same |
| T91 | "In 1917" the Sharif of Mecca issued an edict to all Muslims to protect "the entire Armenian, Jacobite, community" (p. 201) | **Inconsistent** (date and addressees) | The document published by the Armenian National Institute (image: «١٨ رجب ١٣٣٦») is dated **18 Rajab 1336 = 29 Apr 1918** and is addressed to **Prince Faisal and 'Abd al-'Aziz al-Jarba**. Earlier Sharifian manifestos of 1916 and 1917 exist (Margaryan 2005, abstract), so "1917" may conflate them. | https://www.armenian-genocide.org/Affirmation.4/current_category.1/affirmation_detail.html ; https://www.armenian-genocide.org/uploads/Affirmation/4.jpg ; https://arar.sci.am/dlibra/publication/125102/edition/113617/content |
| T92 | Golubovich's book "published in 1921" (p. 191) | **Minor difference** (a 1921 edition was not seen directly) | OpenLibrary/Harvard: "2. ed., aumentata", Firenze 1922, reprinted from *Biblioteca bio-bibliografica* IV (Quaracchi 1923). A 1921 first edition fits the *RB* 1921 review. | https://openlibrary.org/works/OL42220000W |
| T93 | Confirmations "continued into the 20th century" (p. 201) | **Consistent** in substance | Ottoman confirmations of 1734, 1810 and 1813 (Golubovich; Sanjian pp. 189–190). The Sharif's letter is 1918 (T91). | Golubovich ; Sanjian 1965 |
| T94 | Shi'ite rule in post-1979 Iran (p. 198) | **Consistent** (but see C182) | — | https://www.iranicaonline.org/articles/buyids/ (for C182) |
| T95 | A hypothetical forger "over a thousand years ago" (p. 202) | **Opinion** | — | — |
| T96 | The scroll is in the St James Library (pp. 191, 201) | **Unverified**; location **Disputed** | Narkiss (1979) is access-restricted. Sanjian (1965 n. 2) cites Savalaneanc' (1931): the original is **not** in the Patriarchate archives, only a copy. Sassounian (2018, via ANCA): "the original decree cannot be located ... a yellowish copy exists in the ... Mardigian Museum". | https://archive.org/details/armenianarttreas0000unse (restricted) ; https://archive.org/details/Sanjian1965ACSOD ; https://anca.org/?p=64014 |
| T97 | The Firman of 'Umar (captioned "with the Armenian Christians") is in the St James Library, and a "handwritten Arabic copy is kept at the National Library in Paris" (p. 193) | **Inconsistent** (two documents conflated). The Paris copy is **Unverified** | The text printed is the **Greek Orthodox** Achtiname to Sophronios, taken from the Greek Patriarchate's website; that site's note about a Paris copy ("Saint Germain des Pres, No. 100") concerns the Greek version. The **Armenian** 'Umar charter is a different text, addressed to the Armenian patriarch (Sanjian 1965 n. 2). | https://web.archive.org/web/20130806041255/http://www.jerusalem-patriarchate.info/en/axtinames.htm ; https://archive.org/details/Sanjian1965ACSOD |
| T98 | Part II epigraph, Qur'an 3:3–4 (p. 204) | **Consistent** | The verse text matches (Sahih International). | https://api.alquran.cloud/v1/ayah/3:3/en.sahih |

### 1c. Factual claims (§4 of the extraction) not already covered above

Claims whose substance is a T row above are not repeated. Groups of pure opinion are listed together at the end.

| # | Book claim (page) | Verdict | What independent sources say | Source URLs |
|---|---|---|---|---|
| C1 | The Najran covenant was unknown to Muslims until rediscovered "almost one hundred years ago"; the Assyrian covenant "has long been known" to the Muslims of upper Mesopotamia (p. 177) | First part: **Minor difference**. Second part: **Unverified** | The Chronicle of Seert's Najran covenant was published by Scher in *Patrologia Orientalis* 13 (1919). Wood (2013, p. 244) says it was "apparently discovered in 878 by a monk named Habib". The only evidence of Muslim knowledge in Hakkari is Surma's and Wigram's testimony. | https://archive.org/details/patrologiaorient13pariuoft ; https://archive.org/details/oapen-20.500.12657-33852 |
| C2 | The original was "allegedly composed in the Persian language" (Brevick 114) (p. 177) | Book exists; **p. 114 Unverified** | Brevick, *Books Were Opened*, exists (archive.org item, access-restricted). Malech p. 221 says "written in the Persian language". **But** the Persian text itself opens «ترجمه عهدنامه» ("Translation of the covenant") (Malech p. 227). | https://archive.org/details/bwb_S0-ADX-247 ; https://archive.org/details/historyofsyriann00male |
| C3–C7 | Malech's title, account and 1517 anecdote (p. 177) | Quotes **Consistent** | Malech pp. 221 and 227, verbatim. Malech calls Said's tribe "the Najarai" and says his ch. "is taken from the writings of Shimon Assemani and Bar Hebraeus". Those sources name the bishop **Isho/'Isa**, not "Jahb Alahah". For the historicity of 1517, see T23. | https://archive.org/details/historyofsyriann00male ; https://archive.org/details/BarHebraeusChroniconEcclesiasticumVol.3 ; https://archive.org/details/patrologiaorient13pariuoft (p. 605) |
| C8 | "Jahb Alahah may be a corruption of Abu Haritha" (p. 177) | **Opinion** | The Seert and Bar Hebraeus sources give the bishop as Isho/'Isa (see C3–C7). | as above |
| C9 | "Some scholars": the Assyrians may have appropriated the covenant addressed to "all Christians" (p. 177) | **Opinion**, but supported by evidence the book does not cite | Malech's text shares its colophon (Mu'awiya; Monday, end of the 4th month, 4 AH; Medina) and most of its witness list with the "Testament/Covenant with the Christians of the World" printed by Sionita (Paris 1630, p. 16, page image). Its Persian preamble addresses all Christians, east and west (Malech p. 227). | https://digital.slub-dresden.de/id308498003 ; https://archive.org/details/BIUSante_07231x02 ; https://archive.org/details/historyofsyriann00male |
| C11 | "Of all the Caliphs, Selim I was ... the most relentless" relic-seeker (p. 178) | **Disputed** (the caliph title). Relic-collecting **partly Consistent**. Superlative **Opinion** | EOE "Abbasid Caliphate": the story of the caliphate passing to Selim in 1517 first appears in **17th-century** court histories, and "No contemporary accounts recorded such a transfer". Küçükaşcı: after 1517 Selim "personally sealed the sacred relics" sent to Istanbul. | https://archive.org/details/encyclopedia-of-the-ottoman-empire (pp. 3–4) ; https://istanbultarihi.ist/546-sacred-relics-in-istanbul |
| C12, C15, C16 | 1517 was "the ideal time" to present charters; Selim's scholars were not surprised by the Persian; a fake would have been destroyed (p. 178) | **Opinion**, resting on a false premise | All three assume that Selim met the patriarch in Baghdad (refuted at T23). | — |
| C13 | Traditions in Muslim and Bukhari show the Prophet could speak Persian (p. 178) | **Minor difference** (overstated) | Bukhari 3070–3072 (chapter "Whoever spoke in Persian") record single words ("kikh kikh", "sur"), not command of the language. | https://sunnah.com/bukhari:3072 ; https://sunnah.com/bukhari:3070 |
| C14 | Salman was proficient in Persian, Aramaic, "possibly Greek" (p. 178) | **Unverified** (plausible) | Ibn Ishaq's account (Guillaume pp. 95–98) places him with clerics in Syria, Mosul and Nisibis, but states no language skills. | https://archive.org/details/GuillaumeATheLifeOfMuhammad |
| C17 | The document begins "The translation of the holy messenger's treaty, peace be upon him and his family" (p. 178) | **Consistent** | Malech p. 227, Persian, page image: «ترجمه عهدنامه حضرت رسول صلى الله عليه وآله». | https://archive.org/details/historyofsyriann00male |
| C19 | Persian-speaking professors saw no sign of forgery (p. 178) | **Unverified** | The colleagues are unnamed. | — |
| C20 | "It has not yet been established whether the version in Malech's text was transcribed in modern or ancient times" (p. 178) | **Opinion**; there is evidence pointing to modern | The preamble before the witness list (Malech p. 222, page image) reads, as I read it: «حکم صورت امضای خلفاء و صحابه کبار که در روزنامه‌های خارجه نقل می‌شود», "the copy of the signatures of the caliphs and great Companions, which is reproduced in foreign *rūznāmas* [newspapers/journals]". *Rūznāma* in the sense "newspaper" is modern (19th c.), and the phrase implies the list was copied from published (European) sources. **This is my reading of the page image and should be confirmed by a Persianist.** | https://archive.org/details/historyofsyriann00male (p. 222 = page image n247) |
| C21 | The English translation is "not perfectly accurate", especially the witness list (p. 178) | **Consistent** | The English omits 'Uthman and 'Ali, garbles names ("Ebar Ibn Jaamir" = 'Ammar b. Yasir), and adds "in the city of Medina", which is not in the Persian colophon. | https://archive.org/details/historyofsyriann00male |
| C22 | The Persian covenant has **27** witnesses (p. 179) | **Inconsistent** | Malech's English list has **31** names; the Persian list (p. 222, counted from the image) has **33**, or 32 if "Abu Hudhayfa ibn 'Usayr" is one name. The book's own transliteration (p. 314) has 33. | https://archive.org/details/historyofsyriann00male |
| C23 | "Muttawatir", the highest hadith grade, means passed down by many narrators (p. 179) | **Minor difference** (spelling "mutawatir"); definition **Consistent** | "A Mutawatir hadith is one which is reported by such a large number of people that they cannot be expected to agree upon a lie". It is a category by number of transmitters, conventionally yielding certainty. | https://www.islamic-awareness.org/hadith/ulum/asb3.html |
| C24–C28 | Wigram 310, Browne and Surma quotations on the firman, knife and Muslim respect (p. 179) | **Consistent** | Verbatim, with small slips. Wigram has "a firman **from** the prophet"; the book has "of". | Wigram 1910 ; Browne ; Surma (URLs at T30, T33, T34) |
| C29–C31 | Percy on the Jelu handkerchief and the Ishy Yau/Said tradition; terms included church building "as they pleased" with Arab help (p. 179) | Quotes **Consistent**. Percy's church clause is **Minor difference** against Bar Hebraeus | Bar Hebraeus cols. 115–118 has help in **restoring collapsed** churches ("collapsae ecclesiae aedificium instaurare"), taxes of 4 zuzas for the poor and 12 for merchants and the rich, and no compulsion to go to war. Percy's "erect churches as they pleased" overstates this. For "residing at Baghdad", see T11. | https://archive.org/details/noticesofproceed1618roya ; https://archive.org/details/BarHebraeusChroniconEcclesiasticumVol.3 |
| C32–C35 | Surma: gold letters on parchment, written "circle wise" around a handprint; the knife; the Mollah of Julamerk (p. 179) | **Consistent** with Surma | Surma ch. IX. | Surma (as T33) |
| C38 | "The rights confirmed by 'Umar are clearly the very same granted in the Covenant" (p. 180) | **Opinion**, contradicted on one point | Wigram's 'Umar terms forbid **new** churches without permission (1929 pp. 76–77). The Malech text requires Muslim neighbours to **help build** churches (p. 229). | Wigram 1929 ; Malech |
| C39 | Wigram, *The Assyrians* 33 (p. 180) | **Minor difference** (page) | pp. 76–77 (see T12). | https://archive.org/details/assyrianstheirne0000wigr |
| C40–C41 | Stafford 95: a copy of the firman was preserved by the Patriarch; millet rights (p. 180) | Substance **Consistent**; omission | Stafford attributes it to "either the Prophet ... or the Khalif Omar"; the book drops the 'Umar option (see T35). | https://archive.org/details/the-tragedy-of-the-assyrians |
| C42 | "This treasured relic was stored in the great church of Mar Zaia in Jilu ... some twenty ... villages" (p. 180) | **Inconsistent**: the book merges two relics. Village count **Consistent** | Surma separates the Mar Zeia **silk kerchief** (lost when Oramar Kurds plundered the church) from the patriarchal **parchment** firman "kept among the treasures of the Patriarchate". Wigram 1910 p. 310 n. calls the Jilu item "a similar firman". Gaunt (Table 1, p. 21): the Jilu diocese had **21** villages. | Surma ; Wigram 1910 ; https://archive.org/details/massacres-resistance-protectors-muslim-christian-relations-in-eastern-anatolia-d |
| C43 | When the patent was raised, Muslims dropped their weapons (p. 180) | **Consistent** with Malech p. 228, whom the book does not cite here | Malech says this of the covenant in general, not of the Jilu relic. | https://archive.org/details/historyofsyriann00male |
| C44, C46 | The original "has yet to be located" in Istanbul; neither covenant is in the "Turkish museum" catalogue (pp. 180–181) | **Consistent** (limited check) | The Topkapı relics survey lists the Prophet's letters to al-Muqawqis, al-Mundhir, al-Harith and Musaylima, but **no covenant with Christians**. The full Topkapı catalogue was not checked. | https://istanbultarihi.ist/546-sacred-relics-in-istanbul |
| C45 | Emhardt & Lamsa 75–76 (p. 180) | **Consistent** (one word dropped) | See T10. | https://archive.org/details/oldestchristianp0000will |
| C47 | The owners make no mention of any transfer to Istanbul (p. 181) | **Consistent** (argument from silence) | Neither Surma nor Theodore mentions Selim or 1517. | Surma ; Theodore |
| C48 | Surma was the sister of "Mar Shimun XXI Benyamin" (p. 181) | **Minor difference** (numbering) | Wilmshurst: "Shem'on XIX Benjamin (1903–18)" in the older numbering; XXI is a later revision. Surma's preface: "sister of his two successors, Benyamin and Paulus". | https://archive.org/details/the-martyred-church ; Surma |
| C56, C57 | The covenant may survive in private hands or have been confiscated by the Young Turks (p. 182) | **Opinion** | Gaunt: the Mar Zaya church in Jilu was destroyed in 1915 "with all its priceless contents". That bears on the kerchief, not on the patriarchal firman. | Gaunt (pp. 143–144) |
| C58 | Yelda: "later destroyed by the Turkish rulers before they set out to kill 30,000 Christians" (p. 182) | **Inconsistent** with the cited source | CT 2004: "**Assyrians believe** that the then-Turkish rulers destroyed this document before setting out to kill 30,000 Christians", and "The massacre of 30,000 Christians in **1847**". The word "later" is not in the article. | https://www.christianitytoday.com/ct/2004/augustweb-only/8-2-52.0.html |
| C59 | 1915 events in Jilu and the flight to Salmas (p. 182) | **Consistent** | See T50. | GEDSH "Hakkari" ; Gaunt |
| C60 | The 1915 perpetrators "could not have been Muslims" but "secular revolutionaries" (p. 182) | **Opinion**; its factual premise is **Disputed** | Gaunt pp. 63–64: the official Ottoman **jihad** fatwa of Nov 1914, and a Kurdish perpetrator's letter about "the Great Jihad". Kurdish tribal irregulars took part. GEDSH "Sayfo": the massacres were "orchestrated by high Ottoman officials", notably Talaat Pasha. | Gaunt ; https://gedsh.bethmardutho.org/Sayfo |
| C61 | Bedir Khan was the first leader of Botan; his state included Bahdinan (p. 182) | "First": **Inconsistent**. Bahdinan: **Unverified/Disputed** | Iranica says "last ruler" (see T32). Aboona: Bahdinan was a separate emirate, occupied by Ottoman forces in 1842. | Iranica ; Aboona |
| C62 | European powers spread discontent; Christians were seen as a "fifth column" (p. 182) | **Opinion** (partly reflects documented perceptions) | GEDSH "Hakkari": the government regarded the Christians as "a disloyal non-Muslim element". | https://gedsh.bethmardutho.org/Hakkari |
| C63, C67 | Emhardt & Lamsa 82, 83, 88 (p. 182) | **Consistent** | Verbatim or close. | https://archive.org/details/oldestchristianp0000will |
| C64 | Bedir Khan set out to exterminate the Christians to create a homogeneous Kurdish homeland (p. 182) | **Disputed** / Opinion | The motives given differ: EOE (missionary-emboldened Christians), Wilmshurst (revenge for the 1842 'Amadiya affair), Aboona (Ottoman policy), GEDSH (intra-Kurdish wars). | EOE ; Wilmshurst ; Aboona ; GEDSH Hakkari |
| C65 | 40–90 sons, 22 confirmed (p. 182) | **Minor difference** | See T43: 21 sons; the larger figures count children. | Iranica ; Akpınar |
| C68 | Percy: the Muslims' change of attitude was "due not to religious antagonism but to jealousy of their superior wealth" (pp. 182–183) | **Consistent** | Percy p. 645, verbatim. | https://archive.org/details/noticesofproceed1618roya |
| C70 | "The vast majority of scholars who have written about the Assyrian Christians treat the Covenant ... as a historical fact" (p. 183) | **Inconsistent** | Wigram reports it as "Assyrian tradition", "purporting to be the grant". Stafford says "according to tradition", and offers 'Umar as an alternative. Wilmshurst calls the 878 Najran "treaty" "a forgery". Reynolds (2014): "Forged by Christians". El-Wakil, who defends the covenants, describes the "accepted understanding that these are forgeries" (2016 abstract) and says they were "regarded as forgeries by both Muslim and non-Muslim academics" (2017). | Wigram 1910 ; Stafford ; https://archive.org/details/the-martyred-church ; Reynolds (as T26) ; https://academic.oup.com/jis/article-lookup/doi/10.1093/jis/etw027 ; https://elmi.hbku.edu.qa/en/studentTheses/searching-for-the-covenants-identifying-authentic-documents-of-th/ |
| C71 | Wigram: "The claim of a special position ... can hardly be substantiated under present conditions" (p. 183) | **Consistent** | Wigram 1910 p. 310. | https://archive.org/details/introductiontohi0000wawi |
| C73 | Some Sunni scholars place Mu'awiya's conversion earlier (p. 183) | **Consistent** | Dangor (*Encyclopedia of Islam and the Muslim World*): "Some sources suggest that Mu'awiya accepted Islam before the conquest ... but concealed it". | https://www.encyclopedia.com/religion/encyclopedias-almanacs-transcripts-and-maps/muawiya-680 |
| C74 | Al-Baladhuri: 17 literate Qurayshis; the literate women included Hafsah, 'A'ishah and Umm Kulthum (p. 183) | **Minor difference** | Baladhuri (Murgotten II pp. 271–272) has 17 literate men and the names given. But **'A'ishah "could read the Koran but could not write"**. | https://archive.org/details/originsoftheisla032520mbp |
| C75 | The Prophet sent "his adopted son, Zayd" to learn Hebrew and Syriac (p. 183) | **Inconsistent** (wrong person) | The reports concern **Zayd b. Thabit** (Bukhari 7195; Tirmidhi 2715, "learning Syriac"). The adopted son was Zayd b. Haritha. | https://sunnah.com/bukhari:7195 ; https://sunnah.com/tirmidhi:2715 |
| C76 | At least 45 scribes (Azami 10) (p. 183) | **Consistent** | Azami p. 10. | https://archive.org/details/StudiesInHadithMethodologyAndLiterature |
| C77–C109 | The item-by-item quotations of the covenant (pp. 183–190) | **Consistent** with Malech pp. 228–230, with modernisations | I compared the full text. The "item" numbers are Morrow's own; Malech does not number clauses. Modernisations: "Mohammedans"→"Muslims", "Beth Almal"→"bayt al-mal", "denar"→"dinar", "turn Moslems"→"become Muslims". The book inserts "the members of" (C82). | https://archive.org/details/historyofsyriann00male |
| C79 | Jenkins on Nasraye and rabban (p. 184) | **Consistent** | Jenkins p. 7. | Jenkins |
| C83 | The Prophet was dealing with "what previously was a vassal kingdom of the Byzantines" (p. 184) | **Inconsistent** | The Church of the East's heartland (Seleucia-Ctesiphon, Beth Garmai, Adiabene) was in the **Sasanian Persian** empire. Isho'yahb II was sent to Heraclius by the Persian queen Boran (GEDSH; Percy p. 645). Wigram (1929) compares the 'Umar terms with those "received under the Persian". | https://gedsh.bethmardutho.org/Ishoyahb-II-of-Gdala ; https://archive.org/details/noticesofproceed1618roya |
| C92, C95–C97 | Definition of bayt al-mal; quotations from Armour, Betts and Humphreys (pp. 186) | **Not checked** | Those sources were not accessed. | — |
| C98 | The Qur'an's gender-inclusive phrasing (3:195; 4:124; 16:97; 33:35; 40:40) is "totally unique" (p. 187) | The verses are **Consistent**; "unique" is **Opinion** | Each verse uses "male or female" or "men ... women" (Sahih International). | https://api.alquran.cloud/v1/ayah/33:35/en.sahih (and 3:195, 4:124, 16:97, 40:40) |
| C110 | Muhammad ended female infanticide (p. 189) | **Partly Consistent** / Opinion | Q 81:8–9 condemns it. That the practice "ended" was not verified. | https://quran.com/81/8-9 |
| C115–C122 | Modern-religious-policy claims (pp. 184–185) | See T55–T58. C117: **Minor difference**. C118: **Minor difference**. C120: **Consistent**. C119: **Unverified** | **C117:** Malaysia bans Shia worship as "deviant"; arrests are followed by "rehabilitation", not long prison terms (USDOS 2014). **C118:** Saudi Arabia closed about 70 husseiniyas, many reopened, and Isma'ilis were "reportedly" not obstructed (USDOS 2012). **C120:** church construction is not allowed (USDOS 2012). **C119:** too general to check. | https://www.ecoi.net/en/document/313262 ; https://www.justice.gov/eoir/vll/country/DOS_IRF/2012/Saudi%20Arabia.pdf |
| C123 | "Many, if not most" militant Muslim movements are controlled by US, British, French and Israeli services (p. 185) | **Opinion** (asserted as fact, with no evidence given) | — | — |
| C124, C125 | Mehmet II protected Constantinople's treasures (Lunde 85) and left the icons in place beside calligraphy (p. 187) | C124 **Unverified**. C125 **Minor difference** | EOE: under Mehmed II "the bell, relics, crosses, icons ... were removed", and icons on the qibla side were plastered. Most figural mosaics remained until the whitewashing of 1607–09. Lunde was not accessed. | https://archive.org/details/encyclopedia-of-the-ottoman-empire (pp. 243–244) |
| C126–C130 | The Ka'ba pictures (p. 188) | See T13, T14 | C129 (Guillaume's note "Apparently I.H. has cut out what I.I. wrote") is **Consistent**: p. 552 n. 3, verbatim. | https://archive.org/details/GuillaumeATheLifeOfMuhammad |
| C132, C133 | The Damascus shrine list (Walker via Jenkins 217–218); Bliss's examples (pp. 188–189) | **Consistent** | Jenkins pp. 217–218; Bliss pp. 27–28. | Jenkins ; Bliss |
| C134 | The Jews of al-Andalus invited the Muslims (p. 189) | **Disputed** | See T15. | Roth |
| C135, C136 | Spanish Catholics loathed their Germanic overlords; Muslims seen as saviours (Ahmad Thomson 88) (p. 189) | **Opinion / Unverified** | Not checked. | — |
| C137 | The Qur'an enjoins respect for "the signs of Allah": 22:32; 40:81; 5:29; 31:32 (p. 189) | **Minor difference** | 22:32 ("honors the symbols of Allah"), 40:81 and 31:32 fit. **5:29 does not**: it is Abel's speech about bearing sin. 5:2 ("do not violate the rites of Allah") would fit, so 5:29 may be a typo. | https://api.alquran.cloud/v1/ayah/5:29/en.sahih ; https://api.alquran.cloud/v1/ayah/5:2/en.sahih ; https://api.alquran.cloud/v1/ayah/22:32/en.sahih |
| C138, C139 | The Prophet "sent word to the Byzantines, who rebuked his offers"; a "buffer zone" strategy (p. 191) | **Opinion** (C139). C138 rests on the tradition of the letter to Heraclius, **not checked** | sunnah.com returned 403 to WebFetch for this page. | — |
| C140–C142 | The scroll's title (Narkiss 11, fig. 2); "little circulation"; 327 x 21.5 cm, paper on silk (p. 191) | C140 and C142 **Unverified**. C141 **Opinion** (plausible) | Narkiss is access-restricted, and no other source gives the dimensions. Sassounian (2018) calls the decree "rarely-known". | https://archive.org/details/armenianarttreas0000unse (restricted) ; https://anca.org/?p=64014 |
| C146 | "Abraham I appears in the full light of history" (p. 191) | **Inconsistent** (overstated) | Sanjian (1965 p. 97): "We have no information on the Armenian incumbents before Abraham". Abraham is known from the later roster and from charters Sanjian calls "apocryphal". | https://archive.org/details/Sanjian1965ACSOD |
| C147 | Many leaders came to the Prophet in Medina after Mecca (p. 191) | **Consistent** | See T6. | Guillaume |
| C148, C149 | Golubovich's title and aim (p. 191) | **Minor difference** ("Greo" = "greco"). Aim **Consistent** | Part II heading: "falsi firmani posseduti dai Greci" (false firmans held by the Greeks). | https://archive.org/details/golubovichbibliotecabi4 ; https://openlibrary.org/works/OL42220000W |
| C150 | *Revue Biblique* reviewer: "a fraud built like a war machine" (pp. 191–192) | **Unverified** | *RB* 30 (1921) is not online (archive.org gap; Gallica and HathiTrust blocked). | — |
| C151 | Golubovich: the Sinai Pact, the 'Umar treaty and Selim's firman are fakes (p. 192) | **Consistent** | Article titles "Il falso «Patto» di Maometto" and "Il falso Firmano di Omar"; "pseudo firmani di Selim I (1517)". | Golubovich |
| C152 | The authors named: Lucaris, "Father Lambrinos", Théophane "his procureur", archdeacon Grégoire "former Jew" who "sold the pot to the roses" (p. 192) | **Minor difference**; "Lambrinos" **Unverified** | Golubovich Art. XII names Murad IV, Cyril Lucaris, Patriarch Teofane, and "Gregorio Filareto, ex ebreo, arcidiacono". In 1635 Gregorio "svelò" ("revealed") the matter, which fits the French idiom *découvrir le pot aux roses* ("to let out the secret"). No "Lambrinos" is in the text, and Theophanes was Patriarch, not a "procureur". | Golubovich |
| C154 | Hagopian: the Greeks as well as the Latins tried to expropriate Armenian property (p. 192) | **Consistent** | Hagopian 2011. | Hagopian (as T64) |
| C153, C156 | The reviewer's conspiracy is "far-fetched"; if Golubovich were right the sites would revert to Muslims (p. 192) | **Opinion** | — | — |
| C158 | Golubovich judged the Armenian covenant fake (p. 193) | **Minor difference** | He calls the Armenian versions of the 'Umar and Selim firmans "identici rescritti falsi" ("identical false rescripts"). Of the Prophet's covenant he notes only that the Armenians "pretendono di possedere anch'essi un simile autografo" ("claim to possess a similar autograph too"). | Golubovich |
| C160–C165 | The text of the Achtiname (Sophronios, "Patriarch of the Imperial Nation", "three gates", the list of sects including Franks, a 1⅓-drachma pilgrim tax) (pp. 193–194) | **Consistent** as a description of the Greek Patriarchate's text | El-Awaisi (2000) analyses the same features and treats them as evidence of an Ottoman-era date (see §4). | https://dergipark.org.tr/download/article-file/294102 |
| C166 | Source "(Jerusalem Patriarchate)" (p. 194) | **Consistent** | Archived 2013 page "axtinames". | https://web.archive.org/web/20130806041255/http://www.jerusalem-patriarchate.info/en/axtinames.htm |
| C167 | Sophronios is historical; "There were literally hundreds of patriarchs in Jerusalem at the time" (p. 194) | First part **Consistent**. Second part **Inconsistent** | Sophronios was patriarch from early 634 until his death on 11 Mar 639 (Mango & Scott; the Greek Patriarchate gives 634–638). It was **one see with one incumbent**: Theophanes' annual lists name a single bishop of Jerusalem. | https://archive.org/details/chronicle-of-theophanes-the-confessor ; https://en.jerusalem-patriarchate.info/?p=37562 |
| C168 | The original 'Umar firman bore the print of the Prophet's hand (p. 194) | **Unverified** | El-Awaisi's description of MS 552 mentions no handprint. | El-Awaisi |
| C170 | Title "Covenant of 'Ali, Fourth Caliph, of Baghdad" (p. 194) | **Consistent** with Avdall's title. The title is **anachronistic** | 'Ali ruled from **Kufa** (Tabari XVII). Baghdad was founded in 145/762 (Tabari XXVIII n. 730). | https://archive.org/details/the-history-of-al-tabari ; Avdall |
| C172, C173 | Scribe "Hashim, the son of Athap, the son of Valas"; "Kharanthala"; "the son of Saha" (p. 195) | **Minor difference**; "Kharanthala" **Unverified** | Avdall has "son of **Sahan**", and footnotes the odd names "So in the Armenian text". | Avdall |
| C174–C176 | Clauses of the Covenant of 'Ali (p. 196) | **Consistent**, with **omissions** | The book's text skips "The priests should not be deprived of their holy calling. The Christians should not be converted" (eye-skip), and skips "Their property should not be meddled with when they build Churches". | Avdall |
| C177 | "I have entered into a Covenant of patriarchs, of prophets, which was brought down from heaven by an angel"; on p. 198 the author treats an angel-delivered covenant as a Shi'ite trait | **Inconsistent** (transcription omission; the argument rests on it) | Avdall: "...a Covenant of patriarchs, of prophets and of all holy men ... **And the word of God to the holy prophets, which was brought down from heaven by the angel**, enjoins obedience". What the angel brings is revelation to the prophets, not 'Ali's covenant. | https://archive.org/details/journalofasiatic39asia |
| C179–C181, C184 | Kufic script fits 'Ali; Christians aided 'Ali; disloyal Muslims = Mu'awiya; Sunni acceptance of inspiration (pp. 197–198) | **Opinion** | — | — |
| C182 | Shi'ites are "a mere ten percent" and ruled only under the Idrisids, Fatimids, Safavids and post-1979 Iran (p. 198) | **Minor difference** | Pew 2009: "10-13%". The list omits the **Buyids**, who entered Baghdad in 945 (Iranica). Classing the Idrisids as Shi'ite is debatable. | https://www.pewresearch.org/religion/2009/10/07/mapping-the-global-muslim-population/ ; https://www.iranicaonline.org/articles/buyids/ |
| C183 | Shi'ites see their Imams as inspired by angels and regard the Umayyads as apostates (p. 198) | **Not checked** (doctrinal generalisation) | — | — |
| C185, C186 | The Muktafi II charter; Mingana's quotations (pp. 198–199) | **Consistent**, with one trimmed quotation | Mingana pp. 127–128 has "It is not the Kur'an that was the cause of **some cases of** persecution of Christians **in early times**"; the book drops the qualifiers. | https://archive.org/details/bulletinofjohnry1011unse |
| C187, C188 | Salah al-Din, "a notorious nasibi", granted the Armenians protection; "most authorities" treat his edict as genuine (p. 199) | Protection and authenticity **Consistent** (only two specialists located). "Nasibi" is **Opinion** | Sanjian: "has all the earmarks of being authentic". Mkrtumyan 2025 (abstract) studies its Arabic versions. | Sanjian 1965 ; https://armenianstudies.aspu.am/index.php/armenianstudies/article/view/180 |
| C189 | Sanjian speaks only of firmans "attributed to" the Prophet, 'Umar and 'Ali (p. 199) | Narkiss **Unverified**. Sanjian's view is **misrepresented** | Sanjian 1965 p. 169: the edicts from 'Umar, the Prophet and 'Ali are "**equally unauthentic** ... must have been fabricated to support rival claims to the dominical sanctuaries, have **no historical foundation**". Bazmavep 1981 repeats this. | https://archive.org/details/Sanjian1965ACSOD ; https://arar.sci.am//Content/381972/424-448.pdf |
| C190, C191 | Dadoyan's "alleged 'Prophet's Oath'"; the core of the oaths was protection in return for submission and taxes (pp. 199–200) | **Consistent** (snippets) | p. 60 and the word "alleged" were not seen. | Dadoyan snippets (as T65) |
| C192 | Samuel of Ani, Mxit'ar of Ani, Kirakos and Juanser "all confirm that 'Muhammad himself made a pact with the Armenians'" (Thomson 842) (p. 200) | Quote **Consistent**; its use is **misrepresented** | Thomson p. 842 reports the claim and immediately explains it: "it is not particularly surprising that Muhammad himself was credited with an arrangement only worked out under his successors". The pact concerns "the land of Armenia", not Jerusalem. | https://archive.org/details/thomsonmuhammadislamarmlit |
| C193 | Samuel's tax list: "...But from the priests, nobles and cavalry he ordered tax to be taken" (p. 200) | **Inconsistent**: the misquotation reverses the meaning | Thomson p. 843: "he ordered **no** tax to be taken". The book's page image (PDF p. 225) was checked, so this is not OCR. | Thomson |
| C194, C195 | Thomson on the Armenians' imprecise understanding of Islam (858); the "credited with an arrangement" quotation (842) | **Consistent** | Both verbatim or close. | Thomson |
| C196 | The 1917 edict text (p. 201) | **Inconsistent** (date and addressees) | See T91. The text matches the 1918 letter ("the Jacobite Armenian community"; *'iqāl*, "rope"). | ANI (as T91) |
| C197 | Mingana: "the praiseworthy keynote of tolerance that runs through [the Firman]" (p. 201) | **Minor difference** | Mingana p. 128 wrote this of the **1138 charter**, not of any firman. | Mingana |
| C198 | Takfiris and Wahhabis as "apostates"; Saudi Arabia a "State player"; opposition to "their Western backers" (pp. 201–202) | **Opinion** | — | — |
| C199, C201 | Qur'an 28:41–42 and 3:3–4 (pp. 201, 204) | **Consistent** | The verse texts match. | https://api.alquran.cloud/v1/ayah/28:41/en.sahih |
| C200 | The Patriarchate "has always been careful to speak of the firman *attributed to* the Prophet" (p. 201) | **Disputed** | The Mother See text (via Belleville) states the grant as fact. "Attributed" is Sanjian's wording in an exhibition catalogue (Narkiss, not opened). | Belleville (as T61) |
| Other opinion items | C10, C36, C37, C66, C69, C81, C111, C131, C179–C181 and the author's argument lists in §§5–6 of the extraction | **Opinion** | Not checkable as fact. | — |

---

## 2. Timeline comparison: events where sources differ

| Event | Book (page) | Version A (who) | Version B (who) | Version C and notes (who) |
|---|---|---|---|---|
| **Date of the "Assyrian" covenant** | "two years before" 630–632 (p. 183) | **4 AH, Medina** (13 Jun 625 – 1 Jun 626): Malech's English, p. 230 (= book p. 314) | **Monday, end of the 4th month, 4 AH** (≈ Sept–Oct 625): Malech's Persian, p. 222 | Same colophon in Sionita, Paris 1630, p. 16: "die Lunae ultima mensis quarti, anni quarti Hegirae, in Medina" |
| **Catholicos to whom the grant is ascribed** | "Ishy Yau ... residing at Bagdad" (Percy); "Essvo Yabh, end of the seventh [century]" (E&L) (pp. 179–180) | **Isho'yahb II, 628–645, at Seleucia-Ctesiphon until 637/8, then Karka**: GEDSH; Wilmshurst | **Envoys reached Medina after Muhammad's death and dealt with Abu Bakr**: Chronicle of Seert (PO 13 pp. 619–620) | Baghdad founded 762; the catholicos moved there c. 773–80 (GEDSH; Wilmshurst) |
| **Patriarch who met Selim in 1517** | "Shimon the fourth", at Baghdad (p. 177) | **Shem'on VI (1504–38)**: Wilmshurst; Baum & Winkler; **Malech himself, p. 314** | Shem'on IV Basidi **died 1497** (Wilmshurst) | **Baghdad was Safavid 1508–1534** (Iranica); Selim never went there |
| **Hakkari massacres and loss of the patriarchal firman** | 1845 (Surma); 1847 (Stafford, Browne, Yelda); mid-19th c. (Wigram); 1899 (Percy, misapplied); "before 1915" (author) (pp. 181–182) | **1843** (Tiyari) and **Oct 1846** (Tkhuma): Wilmshurst; GEDSH "Hakkari"; Layard 1849. Yohannan p. 78: "preserved till 1843". Theodore's own book: family in Mosul 27 July 1843 | **1847**: the year of Badr Khan's *defeat* by the Ottomans (Wilmshurst; Aboona; Akpınar) | **1899**: refers to a *different* relic, the Jelu kerchief (Percy; Surma; Wigram). **1847** is also the date the Yelda article gives for the "30,000" massacre (CT 2004) |
| **Badr Khan's later life** | 1856 Crete reward → Damascus; died 1868 (p. 182) | **1857** pardon → Istanbul **1861/1863** → Damascus **1868** → died **1869**: Akpınar 2025 (Doğan; Kardam) | Died **1868**: Iranica (headword "d. 1867") | No source opened confirms that he suppressed a Cretan revolt |
| **Chaldean break from the "Mar Shimun"** | "About 170 years" before 1936/37, i.e. c. 1766 (Browne) | **1553** (Sulaqa), **1681** (Amid), **1830** (Yohannan Hormez): GEDSH | **1767**: about 100 of 500 Alqosh families Catholic (GEDSH "Alqosh") | That line was the Eliya patriarchate of Alqosh/Mosul, not Mar Shimun (Wilmshurst) |
| **Surrender of Jerusalem to 'Umar** | 638 (p. 193) | **634/5** (AM 6127, after a two-year siege): Theophanes | **636/637** (year 15): al-Tabari/Sayf; Michael the Syrian (AG 948, AH 15) | **637** (by Dec 637): Kaegi; Mango & Scott. **637 or 638**: Kennedy. **638** (year 17; Muharram 17 = Feb 638): al-Baladhuri; El-Awaisi. The Achtiname's own date (20 Rabi' I 15 AH ≈ 2 May 636) precedes Yarmuk (Aug 636) and all of these |
| **Sophronios's patriarchate** | (none given) | Early 634 – 11 Mar 639: Mango & Scott | 634–638: Greek Patriarchate | — |
| **Abraham's visit to Muhammad** | 626 (Zeki al-Din, Belleville); 7th c. (Azadian); within 638–669 with "two full years" (author) (p. 191) | **626, Mecca**: Mother See text; Sassounian 2018 | **"early 630s, if not earlier", Medina**: Dadoyan (Armenian tradition) | The Prophet lived in Medina 622–632, Mecca fell in Dec 629/Jan 630, he died in 632, and the roster dates Abraham from 638 (Sanjian) |
| **Armenian see as a "patriarchate"** | From Abraham, 638 (p. 191) | **638**: Armenian roster/tradition | **1311** (Sargis): Sanjian; Azarya ("more likely"); the Mother See dates independence to 1311 | **11th c.**: "some" sources, per Azarya |
| **'Ali's charter to the Armenians** | 626/4H (Dadoyan); Safar 40 AH = 660 (Avdall; author) (pp. 194, 200) | **AH 4 = AD 625**, to Abraham with 40 clerics: Sanjian (citing Savalaneanc') | **Safar 40 AH = 16 Jun – 14 Jul 660**: Avdall 1870 | 'Ali became caliph in 656 and died c. 24–28 Jan 661 (6–7 months after Safar 40) |
| **First appearance of the Sinai "Pact"** | Golubovich c. 1569; the author counters with 1512 and "five centuries of fatwas" (p. 192) | **1569** (Ottoman Turkish translation; registered 1638): Golubovich | **1512**: Thenaud p. 72 | **c. 1505/1515**: Qansuh al-Ghuri decree citing the Prophet's letter (Moritz). Oldest extant Sinai decree **1130/1134** ("old covenants" only): Atiya; Moritz |
| **Greek forged firmans** | 1630–1634 (p. 192) | **1629–1634** ('Umar firman, "three gates"): Golubovich | **1630**: 'Umar firman first appears and is condemned (Golubovich) | **1638**: the Prophet's rescript registered (Golubovich). Ottoman rejections of 1690 and 1810 (Sanjian) |
| **Sharif Husayn's decree** | 1917 (p. 201) | **18 Rajab 1336 = 29 Apr 1918**: document image (ANI) | **Manifestos of 26 Jul 1916 and Mar 1917**: Margaryan 2005 (abstract) | The text the book quotes matches the 1918 letter |
| **Hagia Sophia becomes a museum** | 1935 (p. 187) | Decree **24 Nov 1934** (Akan 2020; EOE) | Opened **1 Feb 1935** (Akan 2020) | — |
| **Quebec recognised as a nation** | "end of the twentieth century" (p. 184) | **27 Nov 2006** (House of Commons Journals) | — | Spanish statutes of 1979 and 1981 are correct |
| **Samuel of Ani's chronicle** | 13th c. (p. 200) | End of the 12th c. (Thomson p. 842) | — | — |

---

## 3. Discrepancies ranked by significance (most serious first)

1. **The 1517 Selim–Baghdad–"Shimon IV" story (p. 177, restated p. 180; used p. 178 as "perfect chronological sense") is impossible on three counts.** The book repeats it from Malech p. 221, who gives no source.
   - Baghdad was Safavid from 1508 to 1534, and Selim never went there (Iranica "Iraq iv"; EOE).
   - The patriarch in 1517 was Shem'on VI. Shem'on IV died in 1497, and Malech's own list on p. 314 says so.
   - No Church-of-the-East patriarch had lived at Baghdad since 1265 (Wilmshurst).

   The book's whole explanation of why the original is "in Istanbul" rests on this anecdote.
2. **The covenant's own date contradicts the book's chronology (p. 183; T5, W1).**
   - The text the book reprints (p. 314) is dated 4 AH (625/626) at Medina, so it is not "two years before" 630–632.
   - At that date the listed witnesses include Hamza (killed at Uhud, Shawwal 3 AH), 'Uthman b. Maz'un (d. 3 AH), Ja'far b. Abi Talib (in Abyssinia until 7 AH), Ibn 'Abbas (aged about 6), and the scribe Mu'awiya (converted 8 AH). Sources: Guillaume pp. 375ff., 391, 526; Baladhuri.
   - The book's three explanations address only Mu'awiya.
3. **The Assyrian text is not an independent witness (pp. 177–183).** Malech's Persian text calls itself a "translation" (p. 227).
   - Its colophon (Mu'awiya; Monday, end of the 4th month, 4 AH) and its witness list match the "Covenant with the Christians of the World" printed by Sionita in Paris in 1630.
   - Dated copies of that text family go back to 1538 (BnF Arabe 214, which de Slane calls "une des nombreuses rédactions de ce document apocryphe").
   - Its tax scale parallels the 9th-century Chronicle of Seert treaty, which Wood and Scher judge a fabrication.
   - The book raises "appropriation" only as a possibility (p. 177) and never makes this comparison.
4. **Two relics are merged (pp. 180–182; C42, T45, T51).** Surma, Wigram and Percy describe two objects: a silk kerchief "with Arabic writing" at Mar Zaia, Jilu, and a gold-lettered parchment firman kept by the Patriarchate. The book's "half-century" problem with Percy's 1899 date, and its scenario that the firman survived until 1915, both come from treating them as one.
5. **Yelda's source is misread (p. 182; T50, C58).** The cited *Christianity Today* article dates the massacre of "30,000 Christians" to **1847**, gives 1915 separately (250,000 Assyrians), attributes the destruction belief to "Assyrians", and has no "later". The book's 1915 identification is contradicted by its own source.
6. **Armenian specialists are misrepresented (pp. 199–200).**
   - Sanjian is cited only for "attributed", but he calls the Prophet's, 'Umar's and 'Ali's edicts to the Armenians "equally unauthentic ... fabricated ... no historical foundation".
   - Thomson is cited as confirming a pact, but he explains it as a later attribution.
   - Dadoyan's report of Armenian opinion (the 703/719 "renewals") is turned into her own recognition.
   - Samuel of Ani is misquoted in a way that reverses the tax clause: "ordered tax to be taken" for "ordered **no** tax" (C193; checked against the page image).
7. **The Covenant of 'Ali is transcribed with an omission that carries an argument (pp. 196, 198; C177).** Dropped words make the covenant itself "brought down from heaven by an angel". The author then cites this as a Shi'ite trait that a Christian forger could not have invented. In Avdall's text, what the angel brings is God's word to the prophets.
8. **The Armenian chronology is impossible (p. 191; T61, T67).**
   - A patriarchate of 638–669 cannot leave "two full years" with a Prophet who died in 632.
   - A 626 visit to Mecca is impossible, since Muhammad lived in Medina and Mecca fell in 629/630.
   - "Zeki al-Din" cannot be identified.
   - The title "patriarch" is generally dated from 1311.
9. **The 'Umar documents are conflated and the date is unexamined (pp. 192–194; T70, T97).**
   - The text printed under an "Armenian" caption is the Greek Orthodox Achtiname to Sophronios, taken from the Greek Patriarchate's website, along with its note about a Paris copy.
   - Its date (20 Rabi' I 15 AH ≈ 2 May 636) precedes Yarmuk and every surrender date.
   - El-Awaisi judges it an Ottoman-era text; Ottoman tribunals rejected the Greek 'Umar charter in 1630, 1690 and 1810.
   - Golubovich listed this very treaty among the forgeries, so citing it against him (p. 193) assumes what is disputed.
10. **Badr Khan and the Hakkari massacres are misdated (pp. 181–182).**
    - The massacres were in 1843 and 1846, not 1845 or 1847. 1847 is the year Badr Khan was defeated.
    - He was the last emir of an old principality, not its "first leader".
    - The "1856 Crete reward and move to Damascus" is wrong: he was pardoned in 1857 and moved to Damascus in 1868.
    - The 1843 date, which appears in sources the book cites (Yohannan p. 78; Theodore), is never mentioned.
11. **The Sharif's decree is misdated (p. 201).** It is dated 18 Rajab 1336 = 29 Apr 1918, not 1917, and it is addressed to Faisal and al-Jarba, not to "all Muslims".
12. **Other false or overstated statements:**
    - "Literally hundreds of patriarchs in Jerusalem at the time" (p. 194): there was one.
    - The Assyrian Christians as "a vassal kingdom of the Byzantines" (p. 184): the Church of the East lived under Sasanian Persia.
    - "Five centuries of fatwas" for Sinai (p. 192): rulers' decrees, attested from 1130/1134.
    - "The vast majority of scholars ... treat the Covenant ... as a historical fact" (p. 183): even the defenders of the covenants describe the accepted view as forgery.
    - "Ishy Yau ... residing at Baghdad" and "Essvo Yabh ... end of the seventh [century]" are passed on without comment (pp. 179–180).
13. **Medium and low slips.**
    - The empire was "nearly one billion acres" (p. 178); the true figure is about 369 million.
    - Quebec was recognised as a nation in 2006, not at the end of the 20th century (p. 184).
    - The "adopted son Zayd" should be Zayd b. Thabit (p. 183).
    - The book says Waqidi and Azraqi spared Abraham's picture; the opened sources erase it (p. 188).
    - Wigram's *The Assyrians* is cited at p. 33; the passage is on pp. 76–77.
    - Stafford's "or the Khalif Omar" is omitted.
    - Browne's quotation has parenthetical insertions printed as his, including the wrong "(the Mar Shimun)".
    - The witness count is 27 in the book, against 31 or 33 in the sources.
    - Samuel of Ani is placed in the 13th century; it should be the end of the 12th.
    - Thenaud's edition is given as 1874; it is 1884.
    - "Father Lambrinos" is not found in Golubovich.
    - Hagia Sophia: the museum decree was 1934, the opening 1935.
    - "Mar Shimun XXI" uses the revised numbering; the older numbering is XIX.
    - Mingana's "keynote of tolerance" sentence is moved to "the Firman".
    - Qur'an "5:29" should probably be 5:2.

---

## 4. Scholarly assessment of authenticity (both sides, with citations)

The two covenants in these chapters have to be judged separately. Each has its own textual history and its own specialist literature. In both cases the literature located splits the same way. Specialists on the Church of the East and on Armenian Jerusalem treat the documents as later productions. The defence of authenticity comes mainly from Morrow and from a small group of scholars around the "Covenants" project (El-Wakil, Zein, Considine). Their work is on the covenant corpus as a whole, mostly Sinai and Najran.

### 4.1 The "Covenant with the Assyrian Christians" (Ch. 6)

**What the text is.** The only text the book uses is the one printed by Malech (1910): Persian at pp. 222–227, English at pp. 228–230.
- **It calls itself a translation.** The Persian opens «ترجمه عهدنامه حضرت رسول صلى الله عليه وآله», "Translation of the covenant of the Holy Messenger ..." (p. 227).
- **Its colophon.** Mu'awiya b. Abi Sufyan wrote it at the Prophet's dictation on "Monday, the end of the fourth month of the fourth year of the Hijra" (p. 222).
- **The same colophon is in a printed text of 1630.** Gabriel Sionita's Paris edition, *Testamentum et pactiones initae inter Mohamedem et Christianae fidei cultores* (Vitray), p. 16, reads: "Secretarius autem fuit Moauia ben-abi-Sofian ... die Lunae ultima mensis quarti, anni quarti Hegirae, in Medina".
- **The witness lists match.** Sionita's list shares most names with Malech's, including distinctive ones: Hamza b. 'Abd al-Muttalib, 'Uthman b. Maz'un, Daud b. Jubayr, Abu al-'Aliya, Hashim b. 'Asiya, Ka'b b. Ka'b and Ja'far b. Abi Talib.
- **The clauses match.** Sionita has the same three-days-of-hospitality and no-shelter-for-enemies clauses (Latin p. 14).
- **The opening matches too.** The Persian preamble on p. 227 addresses the whole Christian nation "in the regions of the world, east ... and west", the address of the "Covenant with the Christians of the World".

So the "Assyrian" covenant is a Persian recension of the widely copied Testament/"Covenant with the Christians of the World". Sources: page images of Malech, https://archive.org/details/historyofsyriann00male ; the 1630 edition, https://digital.slub-dresden.de/id308498003 and https://archive.org/details/BIUSante_07231x02.

**Dated copies of this text family:**
- the earliest dated copy is BnF Arabe 214, dated 1538. De Slane's BnF catalogue (1883–95, p. 54, no. 214) describes it as "Copie de la charte accordée par Mahomet ... à tous les chrétiens, avec les signatures d'environ une trentaine des Compagnons. C'est une des nombreuses rédactions de ce document apocryphe" (https://archive.org/details/cataloguearabes00bibluoft);
- Quaresmius had an Arabic copy around 1616 from the Armenian bishop of Jerusalem, who said the autograph was in the imperial treasury at Constantinople (Golubovich, *Biblioteca* IV pp. 90–91, https://archive.org/details/golubovichbibliotecabi4). The claim that the original is in Constantinople thus attaches to this text family a century before Malech;
- Sionita printed it in Paris in 1630.

**Evidence and arguments against authenticity (or for a late date)**
1. **Internal chronology** (see §3 no. 2). The 4 AH date is incompatible with five of the named witnesses and with the scribe's conversion. The book addresses only the scribe, and misstates the date.
2. **Specialists on the Church of the East.**
   - *GEDSH* (S. P. Brock, "Isho'yahb II of Gdala"): "Although late sources claim he corresponded with Muḥammad and met ʿUmar, in fact he appears to have left Seleucia-Ctesiphon when the city was taken by the Arabs in 637/8 and withdrawn to Karka in Beth Garmai" (https://gedsh.bethmardutho.org/Ishoyahb-II-of-Gdala).
   - Wilmshurst, *The Martyred Church* (2011), pp. 102–103, 150: Isho'yahb's approach came after Muhammad's death. The 'Umar charter is "more likely ... a later Christian invention", and the Najran treaty "found" in 878 is "a forgery" (https://archive.org/details/the-martyred-church).
   - Philip Wood, *The Chronicle of Seert* (OUP 2013, open access), pp. 244–246, on the related Najran treaty. That treaty has the same scribe, Mu'awiya, an overlapping witness list, and a tax scale of 4 dirhams for commoners and 12 for "landowners, merchants, or owners of mines". The Malech text has 1 and 12 dinars, the 12 falling on "merchants and people who own mines of gold and silver". Wood: "The letter is extremely lengthy and repetitive, far too much so to be anything other than an invention. It was composed by an author who was familiar with the accounts of the Life of Muhammad, such as that composed by Ibn Ishaq in the 780s". He calls it part of "the Abbasid-era rewriting of the past", a "lengthy document, apparently discovered in 878 by a monk named Habib" (https://archive.org/details/oapen-20.500.12657-33852).
   - Wood restates this in *Al-Masaq* 33.2 (2021), abstract: an "ʿAbbāsid-era re-imagination" asserting rights "rooted in alleged historical precedents" (https://scholars.aku.edu/en/publications/the-treaty-between-mu%E1%B8%A5ammad-and-the-christians-of-najr%C4%81n-in-the-c/).
   - The Chronicle's editor, Addai Scher (*PO* 13, 1919, p. 623 n. 1), calls this covenant and the 'Umar edict "deux faux" (two forgeries) (https://archive.org/details/patrologiaorient13pariuoft).
3. **Islamic-studies review.** Gabriel Said Reynolds (Notre Dame), *First Things*, Feb. 2014: "Forged by Christians intent on proving to their Muslim overlords that the Prophet himself had guaranteed their well-being ... The 'covenant of the Prophet with Assyrian Christians' dates to the seventeenth century (and is in an Islamic Persian script that did not exist in Muhammad's day)" (http://web.archive.org/web/20151030230243/http://www.firstthings.com/article/2014/02/briefly-noted). The 17th-century dating matches the judgement of the book's own Persian-speaking colleagues (p. 178).
4. **The Assyrian sources themselves hedge.**
   - Wigram (1910, p. 310) reports "Assyrian tradition" and "a document, *purporting to be* the grant", and says the claim of special position "can hardly be substantiated".
   - Stafford attributes the firman to "either the Prophet ... or the Khalif Omar".
   - Surma's and Theodore's family accounts never mention Selim or Istanbul.
   - Physical descriptions vary: a silk kerchief "with Arabic writing" (Percy; Surma) and a gold-on-parchment spiral around a handprint (Surma). Neither fits a Persian text that calls itself a translation. So the 19th-century testimony to a revered relic does not authenticate Malech's text.
5. **A possible modern marker in the Persian text** (my reading of Malech p. 222, needing confirmation by a Persianist). The text says the signatures of the caliphs and Companions are those "reproduced in foreign *rūznāmas*", which suggests the list was copied from published sources.
6. **What the field regards as the default view.**
   - Ahmed El-Wakil, the leading academic defender, writes that Morrow argued "against the accepted understanding that these are forgeries" (*JIS* 27.3, 2016, abstract: https://academic.oup.com/jis/article-lookup/doi/10.1093/jis/etw027).
   - His thesis abstract says they "have until very recently been regarded as forgeries by both Muslim and non-Muslim academics" (https://elmi.hbku.edu.qa/en/studentTheses/searching-for-the-covenants-identifying-authentic-documents-of-th/).

**Evidence and arguments for authenticity (or at least an early claim)**
1. **Morrow's arguments** (pp. 177–183):
   - a Persian original should not prompt a priori dismissal;
   - informal judgements of Persian-speaking colleagues;
   - Selim would have destroyed a fake (premise false; §3 no. 1);
   - Muslim respect for the Mar Shimun family;
   - three possible explanations for Mu'awiya.

   None is independent documentary evidence for a 7th-century origin.
2. **The claim of a prophetic charter is old in the Church of the East.**
   - The Chronicle of Seert (compiled from the 9th century on) has the Najran treaty and an account of Isho'yahb II's envoys.
   - Bar Hebraeus (13th c., *Chron. Eccl.* III cols. 115–118) and Assemani (*BO* III/1 p. 108) report a "diploma" obtained by Isho'yahb with Said of Najran.
   - Tritton (1930, p. 139) cites Bar Hebraeus's account of "the agreement made by 'Ishoyahbh with the Arabs" as evidence for early tax terms without questioning it (https://archive.org/details/caliphsandtheirn029590mbp).

   This shows the claim existed from at least the Abbasid period. It does not show that Malech's text is that charter.
3. **Scholarship sympathetic to the covenants.**
   - El-Wakil (2016): "categorical dismissal of the covenants as forgeries is no longer tenable".
   - El-Wakil (2017): the covenants "are indeed genuine and authentic documents that were issued by the Prophet", though "in some instances tampered with". His main argument is that it is "highly implausible that different and disparate religious communities would have forged similarly worded documents".
   - Zein and El-Wakil, *The Covenants of the Prophet Muḥammad* (Routledge 2022), ch. 4 "The Prophet's covenants with other Christian communities" (pp. 143–189). It was not accessible, so its verdict on the Persian text is unknown (https://eld.bl.uk/catalog/020780086).
   - As Monferrer-Sala summarises Morrow's own later work, this school holds that "many later copies adapt a foundational treaty – the Naǧrān Covenant preserved in the Chronicle of Seert". On that model the Persian text is a derivative, not an autograph.
4. **Reviews of the 2013 book and its sequel.**
   - Amar Sellam (*AJISS* 32:2, 2015, pp. 116–118) is favourable ("groundbreaking"; "an admirable case of a persuasive arguer"), with no engagement with the evidence (https://www.ajis.org/index.php/ajiss/article/view/977).
   - Amidu Sanni (*JMMA* 35:4, 2015) could not be opened (403).
   - Juan Pedro Monferrer-Sala, a Christian-Arabic specialist, reviewed Morrow's 2025 sequel (*Mediterranea* 11, 2026, pp. 403–408). He judges that the work "conflates textual reception with historical origin: late Gharšūnī or Ottoman copies are treated as if they could decisively illuminate seventh-century practice". Its argument is "more persuasive as advocacy than as a decisive demonstration of authenticity" (https://journals.uco.es/mediterranea/article/view/18755).

**Net assessment.** The evidence located supports the following:
- a Church of the East claim to a prophetic or early-caliphal charter from at least the 9th–13th centuries;
- a revered "firman" relic in the Mar Shimun household until 1843–47.

Malech's text cannot be a 7th-century document as it stands. Its colophon and witness list are chronologically impossible, it calls itself a translation, and it belongs to the "Christians of the World" family attested in dated copies from 1538 and in print from 1630. No specialist source located defends this particular text; the pro-authenticity literature defends a hypothetical Najran-treaty core, not this recension.

### 4.2 The Armenian covenant(s) of Jerusalem (Ch. 7)

**Against authenticity**
- **Avedis K. Sanjian** (UCLA), *The Armenian Communities in Syria under Ottoman Dominion* (1965), p. 169 and n. 2, and *Bazmavep* (1981), pp. 427–429. The edicts the Armenian patriarch "is alleged to have received not only from Caliph Umar I but also from the Prophet Muhammad and the orthodox Caliph Ali ... must have been fabricated to support rival claims to the dominical sanctuaries, have no historical foundation". He notes the copy of the Prophet's charter is witnessed by "the future Caliph Umar", and that 'Ali's is dated AH 4 (https://archive.org/details/Sanjian1965ACSOD ; https://arar.sci.am//Content/381972/424-448.pdf).
- **Robert W. Thomson** (Oxford), "Muhammad and the Origin of Islam in Armenian Literary Tradition" (1986), p. 842. The chroniclers' claim (Samuel of Ani, end of the 12th c.; Mxit'ar of Ani; Kirakos; Juanšer) is unsurprising because "Muhammad himself was credited with an arrangement only worked out under his successors". The real arrangements were Rshtuni's treaty with Mu'awiya of 652/3 (Sebeos) and Habib b. Maslama's treaty with Dvin (Baladhuri). The chroniclers' pact concerns "the land of Armenia", not Jerusalem (https://archive.org/details/thomsonmuhammadislamarmlit).
- **Victor Azarya** (1984, pp. 58–60): "Scholars doubt the authenticity of these documents, which could have been fabricated to support rival claims". The title "patriarch" most likely dates from 1311 (https://archive.org/details/azarya1984aqjbackground).
- **Seta Dadoyan** (2011) treats the "Prophet's Oath" as Armenian tradition or "legend" ("alleged"). Only snippets were seen.
- **The 'Umar texts.** El-Awaisi (2000) analysed the Greek Patriarchate's MS 552, the text the book prints. His reasons for an Ottoman date:
  - Ottoman vocabulary;
  - "Franks";
  - sects not present in 638;
  - 'Uthman as a witness;
  - the pilgrim levy.

  He concludes "either forged or at least concocted" (https://dergipark.org.tr/download/article-file/294102). Ottoman tribunals rejected the Greek 'Umar charter in 1630, 1690 and 1810 (Golubovich; Sanjian p. 190).
- **Golubovich** (1921/1923). He is a partisan Franciscan source, but his documentation is specific:
  - the Greek 'Umar and related firmans first appear in 1630, during the 1629–34 litigation;
  - the Prophet's rescript is first registered in 1638, from a 1569 Turkish translation;
  - the Armenian copies are "identici rescritti falsi".
- **Moritz** (1918), on the related Sinai charter: a medieval forgery, accepted as genuine "über ein halbes Jahrtausend" ("for over half a millennium") (https://archive.org/details/beitrgezurgesc00moriuoft).
- **Internal anachronisms:**
  - "Patriarch" Abraham from 638 receives a charter from a Prophet who died in 632;
  - a 626 visit to Mecca;
  - 'Ali's charter dated AH 4, or titled "Fourth Caliph, of Baghdad" (Baghdad founded 762).

**For authenticity, or at least an early claim**
- **Saladin's charter of 1187** is accepted as genuine even by Sanjian ("has all the earmarks of being authentic"). It refers to pacts of the Prophet, 'Umar and 'Ali, so the Armenian claim existed by 1187. Mkrtumyan (2025, abstract) studies its Arabic versions (https://armenianstudies.aspu.am/index.php/armenianstudies/article/view/180).
- **Ottoman confirmations.** Selim I's charter of 1517 to Patriarch Sargis, and rulings of 1734, 1810 and 1813, accepted Armenian documents. These were legal and political decisions in the Holy Places dispute, not historical authentications (Golubovich; Sanjian).
- **Mkrtumyan** (*Religions* 12(2):138, 2021; abstract only) argues from Matenadaran copies that such covenants were recognised by Muslim authorities. This concerns reception, not 7th-century origin.
- **Morrow's case** (pp. 191–202) rests on "covenantal continuity", conformity with the Qur'an, and the Shi'ite features of the 'Ali covenant. One of those features depends on words dropped from Avdall's text (§3 no. 7).
- **Against Golubovich's dating, Morrow is partly right.** Thenaud (1512) and late-Mamluk decrees show the Sinai text existed before the Ottoman conquest. That answers Golubovich's "no trace before 1569", but not the authenticity question.

**Net assessment.** The specialists on Armenian Jerusalem who were opened (Sanjian, Azarya, Thomson, and Dadoyan in framing) treat the Prophet's, 'Umar's and 'Ali's charters to the Armenians as later productions tied to the Holy Places rivalry. They treat Saladin's 1187 charter as genuine, and it is the earliest datable witness to the Armenian claim. No peer-reviewed specialist was found who defends a 7th-century origin for the Armenian documents. The book presents these specialists as more open than their own texts are.

---

## 5. Items not checked, and why

- **Lifespans** (T1, T2, T7, T31, and the "People with dates" table) were left to the lifespan agent, as instructed. Incidental findings are passed on in T31 and T43.
- **Brevick, *Books Were Opened*, p. 114** (C2): the archive.org copy is access-restricted, Google Books returned a quota error, and HathiTrust returned 403. Only the book's existence is verified.
- ***Revue Biblique* 30 (1921) pp. 636–638** (C150, the reviewer's quotations): the volume is not on archive.org, and Gallica and HathiTrust were blocked. Golubovich's own text corroborates the substance.
- **Narkiss (ed.), *Armenian Art Treasures of Jerusalem* (1979)** (C140, C142, C189: scroll size, material, Sanjian's catalogue wording): access-restricted.
- **Dadoyan 2011, p. 60**: Google Books snippets only; the word "alleged" was not seen.
- **Stafford p. 95; Theodore "p. 3[?]"; Wigram pagination of other editions**: only other editions or e-texts were available. Their texts were checked; the cited page numbers were not.
- **Browne's phrase "organized ... a political massacre"**: the online transcription is defective at that sentence.
- **Waqidi (Faizer tr. p. 411); Azraqi (Wüstenfeld p. 111); Zeitlin p. 131; Hamidullah *Introduction* p. 210; Chejne p. 59; Levy p. 169; Armour pp. 27, 32; Betts; Humphreys; Lunde p. 85; Ahmad Thomson p. 88**: not accessible. Primary sources were checked where possible (Guillaume, King on Azraqi, Baladhuri, hadith).
- **Not opened** (paywalled, refused, or 403): EI²/EI³ entries ("Mu'awiya", "al-Kuds", "Dhimma", "Badr Khan", "Khalifa"), Britannica (except one Wayback copy), Mark R. Cohen (*JSAI* 1999), Levy-Rubin (2011), Busse, Gil, Donner, Sahas. Nothing in the verdicts rests on them.
- **Zein & El-Wakil (2022), ch. 4 on "other Christian communities"**: not accessible, so their verdict on the Persian and Armenian texts is unknown.
- **Sanni's review** (*JMMA* 2015): 403. **Themelios review** of the 2025 sequel: 403.
- **"Zeki al-Din"; "Kharanthala"; the BnF copy of the 'Umar firman; the handprint on its original; "Father Lambrinos"**: no identification found in any source opened.
- **The Persian readings** (colophon; the "foreign *rūznāmas*" phrase): these are my readings of page images and should be confirmed by a Persian specialist.
- **C138** (letter to Heraclius): sunnah.com refused WebFetch for that page. **C92, C95–C97, C135–C136, C183**: not checked; definitional, or the sources were not accessible.
- **Umayyad "renewals" of 703 and 719; Bahdinan in Badr Khan's state; French pressure in 1847; Bedir Khan's Cretan role**: no source found that confirms them.

---

## 6. Sources list (every URL opened; ✗ = failed or not usable)

Opened by me directly:
- https://archive.org/details/historyofsyriann00male (djvu text; page images n247, n252 via /page/nNNN_w900.jpg; page_numbers.json)
- https://digital.slub-dresden.de/id308498003 (METS via https://digital.slub-dresden.de/oai/?verb=GetRecord&metadataPrefix=mets&identifier=oai:de:slub-dresden:db:id-308498003 ; page images .../jpegs/00000018–22.tif.medium.jpg)
- https://archive.org/details/cataloguearabes00bibluoft (de Slane, djvu text)
- https://archive.org/details/noticesofproceed1618roya (Percy, djvu text)
- https://archive.org/details/oapen-20.500.12657-33852 (Wood 2013, djvu text 453481_djvu.txt)
- https://gedsh.bethmardutho.org/Ishoyahb-II-of-Gdala
- https://scholars.aku.edu/en/publications/the-treaty-between-mu%E1%B8%A5ammad-and-the-christians-of-najr%C4%81n-in-the-c/
- http://web.archive.org/web/20151030230243/http://www.firstthings.com/article/2014/02/briefly-noted (Reynolds). Also opened: the 20140403093734 snapshot (paywalled stub) and https://www.firstthings.com/article/2014/02/briefly-noted (now a 2019 page). Wayback availability and CDX APIs used.
- https://www.frontpagemag.com/?p=28854 (lead to Reynolds only)
- https://academic.oup.com/jis/article-lookup/doi/10.1093/jis/etw027 (abstract)
- https://elmi.hbku.edu.qa/en/studentTheses/searching-for-the-covenants-identifying-authentic-documents-of-th/
- https://eld.bl.uk/catalog/020780086
- https://journals.uco.es/mediterranea/article/view/18755 ; PDF https://journals.uco.es/mediterranea/article/download/18755/17486/60103 (doi.org/10.21071/mijtk.v11i.18755 redirect)
- https://www.ajis.org/index.php/ajiss/article/view/977 (via https://doi.org/10.35632/ajis.v32i2.977)
- https://religions.dicid.org/index.php/religions/article/download/32/37/108 (Toure review of Zein & El-Wakil; not relevant)
- https://www.islamic-awareness.org/hadith/ulum/asb3.html
- https://api.alquran.cloud/v1/ayah/{3:195, 4:124, 16:97, 33:35, 40:40, 3:3, 3:4, 22:32, 40:81, 5:29, 5:2, 31:32, 28:41, 28:42, 29:46}/en.sahih
- Crossref API (search, match, works 10.1093/jis/etw027, 10.4324/9781003008989-5)
- archive.org advancedsearch and metadata API (searches)
- https://academic.oup.com/book/26826 (TOC not readable)
- https://www.taylorfrancis.com/chapters/mono/10.4324/9781003008989-5/... (no abstract)
- ✗ Failed: https://www.britannica.com/topic/Hadith (403) ; https://library.oapen.org/handle/20.500.12657/33852 (bot wall) ; https://directory.doabooks.org/handle/20.500.12854/26146 (connection reset) ; https://www.tandfonline.com/doi/full/10.1080/13602004.2015.1112122 (403) ; https://www.kriso.ee/cgi-bin/shop/9781003008989_pe.html (403) ; https://www.thegospelcoalition.org/themelios/review/muhammad-and-the-christians-commemorating-the-covenants-of-the-prophet/ (403) ; https://sunnah.com/bukhari:7 (403) ; Google Books API (429 quota)

Opened by the sub-checks (detail and failures in the part files, §5 or §6 of each):
- **Part A:**
  - https://archive.org/details/historyofsyriann00male
  - https://archive.org/details/noticesofproceed1618roya
  - https://archive.org/details/highlandsasiati00percgoog
  - https://archive.org/details/bub_gb_dqIBok_FOLEC
  - https://archive.org/details/BarHebraeusChroniconEcclesiasticumVol.3
  - https://archive.org/details/patrologiaorient13pariuoft
  - https://gedsh.bethmardutho.org/Baghdad
  - https://gedsh.bethmardutho.org/Hakkari
  - https://gedsh.bethmardutho.org/Chaldean-Catholic-Church
  - https://archive.org/details/introductiontohi0000wawi
  - https://archive.org/details/assyrianstheirne0000wigr
  - https://archive.org/details/the-tragedy-of-the-assyrians
  - http://web.archive.org/web/20260305093811/https://www.atour.com/history/1900/20030922a.html
  - http://web.archive.org/web/20070404200218/http://www.aina.org:80/books/acc/acc.htm
  - https://marshimun.com/wp-content/uploads/2025/11/The-History-of-the-Patriarchal-Succession-of-the-dMar-Shimun-Family-Updated-Version.pdf
  - https://archive.org/details/oldestchristianp0000will
  - https://archive.org/details/deathanationore00yohagoog
  - https://www.christianitytoday.com/ct/2004/augustweb-only/8-2-52.0.html
  - https://archive.org/details/bwb_S0-ADX-247
  - https://archive.org/details/BIUSante_07231x02
  - https://en.wikipedia.org/wiki/Jilu (lead)
  - https://en.wikipedia.org/wiki/Shimun_XIX_Benyamin (lead)
- **Part B:**
  - https://archive.org/details/encyclopedia-of-the-ottoman-empire
  - https://www.iranicaonline.org/articles/ottoman-persian-relations-i-under-sultan-selim-i-and-shah-esmail-i/
  - https://www.iranicaonline.org/articles/iraq-iv-safavid-period/
  - https://www.iranicaonline.org/articles/bedir-khan-badr-khan-d/
  - https://istanbultarihi.ist/546-sacred-relics-in-istanbul
  - https://gedsh.bethmardutho.org/Hakkari
  - https://gedsh.bethmardutho.org/Sayfo
  - https://gedsh.bethmardutho.org/Alqosh
  - https://gedsh.bethmardutho.org/Church-of-the-East
  - https://archive.org/details/the-martyred-church
  - https://archive.org/details/the-church-of-the-east-a-concise-history
  - https://archive.org/details/HirmisAboonaAssyriansKurdsAndOttomansIntercommunalRelationsOnThePeripheryOfTheOttomanEmpire
  - https://archive.org/details/massacres-resistance-protectors-muslim-christian-relations-in-eastern-anatolia-d
  - https://archive.org/details/remainswithaccount00laya
  - https://dergipark.org.tr/en/download/article-file/4224379
  - https://www.inlibra.com/document/download/pdf/uuid/8734ea7a-109e-3bc5-8f37-dbdfff4d304b
  - https://archive.org/details/the-lost-history-of-christianity
  - https://archive.org/details/religionsofmode00blis
  - https://dergipark.org.tr/tr/download/article-file/581221
  - https://archive.org/details/the-life-of-muhammad-ibn-ishaq-tr.-a-guillaume
  - https://dergipark.org.tr/en/download/article-file/1184889
  - https://www.noscommunes.ca/Content/House/391/Journals/086/Journal086.PDF
  - https://www.noscommunes.ca/Content/House/391/Journals/087/Journal087.PDF
  - https://boe.es/boe/dias/1979/12/22
  - https://www.boe.es/eli/es/lo/1981/04/06/1
  - https://unama.unmissions.org/en/node/61683
  - https://www.rferl.org/a/1495342.html
  - https://www.ipsnews.net/?p=26822
  - https://theworld.org/stories/2012-03-16/saudi-mufti-says-destroy-all-churches-arabian-peninsula
  - https://www.christiantoday.com/news/destroy-all-churches-says-saudi-arabian-islamic-leader
  - https://www.justice.gov/eoir/vll/country/DOS_IRF/2012/Saudi%20Arabia.pdf
  - https://www.worthynews.com/12042-fatwa-threatens-iraqi-christians
  - https://www.ecoi.net/en/document/313262
  - https://archive.org/details/jvam_20240413
  - https://archive.org/details/the-jews-of-islam
  - https://quran.com/81/8-9
  - https://archive.org/details/dli.ministry.17394
  - https://en.wikipedia.org/w/index.php?oldid=495375422&action=raw (lead)
  - https://en.wikipedia.org/w/index.php?title=Bedir_Khan_Beg&action=raw (lead)
- **Part C:**
  - https://archive.org/details/originsoftheisla032520mbp
  - https://archive.org/details/originsofislamic00balarich
  - https://web.archive.org/web/20261027002919/https://www.britannica.com/biography/Muawiyah-I
  - https://www.encyclopedia.com/religion/encyclopedias-almanacs-transcripts-and-maps/muawiya-680
  - https://archive.org/details/GuillaumeATheLifeOfMuhammad
  - https://archive.org/details/StudiesInHadithMethodologyAndLiterature
  - https://archive.org/details/the-history-of-al-tabari
  - https://archive.org/details/chronicle-of-theophanes-the-confessor
  - https://archive.org/details/walter-e.-kaegi-byzantium-and-the-early-islamic-conquests-1992
  - https://archive.org/details/the-great-arab-conquests-how-the-spread-of-islam-changed-the-world-we-live-in-pdf-room
  - https://archive.org/details/bulletinofjohnry1011unse
  - https://archive.org/details/MichelLeSyrien2
  - https://archive.org/details/saladinandfallk03lanegoog
  - https://archive.org/details/caliphsandtheirn029590mbp
  - https://dergipark.org.tr/download/article-file/294102
  - https://www.cambridge.org/core/product/82977225F39FC98BED07F5B375ABB13C/core-reader
  - https://sunnah.com/bukhari:3070
  - https://sunnah.com/bukhari:3071
  - https://sunnah.com/bukhari:3072
  - https://sunnah.com/bukhari:7195
  - https://sunnah.com/tirmidhi:2715
  - https://en.jerusalem-patriarchate.info/?p=37562
  - https://www.pewresearch.org/religion/2009/10/07/mapping-the-global-muslim-population/
  - https://www.iranicaonline.org/articles/buyids/
  - https://api.aladhan.com/v1/hToG/20-03-0015
  - https://api.aladhan.com/v1/hToG/01-02-0040
  - https://api.aladhan.com/v1/hToG/01-01-0004
  - https://api.aladhan.com/v1/hToG/27-07-0583
  - https://api.aladhan.com/v1/hToG/01-01-0533
  - https://en.wikipedia.org/wiki/Uthman_ibn_Maz%27un (date only)
  - https://en.wikipedia.org/wiki/Abd_Allah_ibn_Abbas (date only)
  - https://en.wikipedia.org/wiki/Umar%27s_Assurance (lead)
- **Part D:**
  - https://archive.org/details/golubovichbibliotecabi4
  - https://openlibrary.org/works/OL42220000W
  - https://archive.org/details/levoyagedoutreme00then
  - https://archive.org/details/dli.ministry.17394
  - https://archive.org/details/beitrgezurgesc00moriuoft
  - https://archive.org/details/journalofasiatic39asia
  - https://arar.sci.am//Content/381972/424-448.pdf
  - https://archive.org/details/Sanjian1965ACSOD
  - https://archive.org/details/thomsonmuhammadislamarmlit
  - https://archive.org/details/armenian-history-attributed-to-sebeos-liverpool-university-press-translated-text
  - https://archive.org/details/originsofislamic01albauoft
  - https://archive.org/details/azarya1984aqjbackground
  - Google Books feed snippets (Dadoyan)
  - https://www.armenian-genocide.org/Affirmation.4/current_category.1/affirmation_detail.html
  - https://www.armenian-genocide.org/uploads/Affirmation/4.jpg
  - https://arar.sci.am/dlibra/publication/125102/edition/113617/content
  - http://web.archive.org/web/20260421094726/https://mirrorspectator.com/2011/05/29/jerusalem-in-limbo/
  - http://web.archive.org/web/20110530032136/http://www.reporter.am:80/go/article/2011-05-14-jerusalem-armenian-story-finally-being-told
  - http://web.archive.org/web/20130313125607/http://bellevillearmenianchurch.org:80/armtoday11.htm
  - https://web.archive.org/web/20130806041255/http://www.jerusalem-patriarchate.info/en/axtinames.htm
  - https://anca.org/?p=64014
  - https://armenianweekly.com/2018/09/14/prophet-muhammads-rarely-known-decree/
  - https://armenianstudies.aspu.am/index.php/armenianstudies/article/view/180
  - https://api.crossref.org/works/10.3390/rel12020138
  - https://dl.tufts.edu/concern/pdfs/0p096p16p
  - Wikipedia leads: List of Armenian patriarchs of Jerusalem; Conquest of Mecca; Umar; Ali; Samuel of Ani
- **Failures:** listed in each part file. Main ones:
  - Narkiss 1979 (restricted);
  - *Revue Biblique* 1921 via Gallica and HathiTrust (Cloudflare);
  - Iranica "Armenia and Iran" (403);
  - MDPI (403);
  - EI²/Brill (paywall);
  - GEDSH Qudshanis and Jilu (403);
  - AsiaNews, state.gov, FDD, CBC, UNESCO (403);
  - Amnesty (certificate error);
  - Jwaideh and Donner (restricted).
