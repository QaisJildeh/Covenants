# V1b: Verification of Morrow, *Covenants*, Chapter 1, second part (printed pp. 32–64)

Book: John Andrew Morrow, *The Covenants of the Prophet Muhammad with the Christians of the World* (Angelico Press / Sophia Perennis, 2013).
Input: `extract/02_ch1b.md` (timeline rows 1–195, §4 claims 1–194). The book's wording was re-checked in `book/chunks/02_ch1b.txt` wherever a verdict depends on it.

**Method.** Every verdict below rests on a page or full text that was actually opened, either by WebFetch or by curl download of the full text (archive.org `_djvu.txt`, PDF), and then read at the cited page. Search-engine snippets were used only to find pages. Wikipedia and Wikidata are labelled where they are used, and only as a lead or for uncontroversial dates or coordinates. Two parts were delegated, with the same rules and verdict scale, to helper agents whose tables were then checked and merged: **Part A** (Qur'an verses and hadith) and **Part B** (pre-Islamic and comparative background, post-prophetic, medieval, Ottoman and modern items). Their source files are `verify/_partA_quran_hadith.md` and `verify/_partB_later_history.md`.

**Verdict scale:** Consistent / Minor difference (AH→CE spans two CE years, spelling, OCR, rounding) / Inconsistent (what reliable sources say instead) / Disputed among sources (each version and who holds it) / Unverified (what was tried) / Opinion (not checkable).

**Calendar note.** One hijri year straddles two Julian years. 2 AH ≈ Jul 623–Jun 624; 4 AH ≈ Jun 625–May 626; 5 AH ≈ Jun 626–May 627; 6 AH ≈ May 627–Apr 628; 7 AH ≈ May 628–Apr 629; 8 AH ≈ May 629–Apr 630; 9 AH ≈ Apr 630–Apr 631; 10 AH ≈ Apr 631–Mar 632. These spans follow Watt's and Ibn Sa'd's translator's conversions quoted below: Hijra Sept 622; Badr ≈15 Mar 624; Muharram 7 AH = May 628; Farewell Pilgrimage = March 632 (xii/10); death 8 June 632.

### Source keys used in the tables (full list in §6)

| Key | Source (as opened) | URL |
|---|---|---|
| **G** | Ibn Ishaq, *The Life of Muhammad*, tr. A. Guillaume (OUP 1955), full text | https://archive.org/details/GuillaumeATheLifeOfMuhammad (text file: https://archive.org/download/GuillaumeATheLifeOfMuhammad/Guillaume%2C%20A%20-%20The%20Life%20of%20Muhammad_djvu.txt) |
| **W** | W. Montgomery Watt, *Muhammad at Medina* (Oxford 1956), full text | https://archive.org/details/muhammadatmedina029655mbp |
| **IS1** | Ibn Sa'd, *Kitab al-Tabaqat al-Kabir*, vol. I, tr. S. Moinul Haq (Karachi 1967) | https://archive.org/details/kitab-al-tabaqat-al-kabir-ibn-sad-s.-moinul-haq-h.-k.-ghazanfar-1 |
| **IS2** | Ibn Sa'd, *Kitab al-Tabaqat al-Kabir*, vol. II (maghazi), tr. Moinul Haq | https://archive.org/details/kitab-al-tabaqat-al-kabir-ibn-sad-s.-moinul-haq-h.-k.-ghazanfar-2 |
| **ISB** | Ibn Sa'd, tr. A. Bewley: vol. III *Companions of Badr*, vol. VI *Scholars of Kufa*, vol. VIII *Women of Madina* | https://archive.org/details/kitab-at-tabaqat-al-kabir |
| **T8 / T9** | *The History of al-Tabari*, vol. VIII (*Victory of Islam*, tr. Fishbein) / vol. IX (*Last Years of the Prophet*, tr. Poonawala), SUNY | https://archive.org/details/the-history-of-al-tabari |
| **BAL** | al-Baladhuri, *Futuh al-buldan*, tr. P. K. Hitti, *The Origins of the Islamic State* I (1916) | https://archive.org/details/originsofislamic01albauoft |
| **HAM** | M. Hamidullah, *The First Written Constitution in the World* (Lahore 1975) | https://archive.org/details/1975-the-first-written-constitution-in-the-world |
| **PO13** | *Histoire nestorienne (Chronique de Séert)*, ed./tr. A. Scher, *Patrologia Orientalis* 13 (1919), pp. 600–601 [280–281] | https://archive.org/details/patrologiaorient13pariuoft |
| **KIS** | M. J. Kister, "The Massacre of the Banu Qurayza: A re-examination of a tradition", *JSAI* 8 (1986) 61–96 (archived PDF) | http://web.archive.org/web/20250118072808/http://www.kister.huji.ac.il/sites/default/files/banu_qurayza.pdf |
| **BA** | Barakat Ahmad, *Muhammad and the Jews: A Re-Examination* (New Delhi 1979), full PDF | https://almuslih.org/wp-content/uploads/Library/Barakat,%20A%20-%20Muhammad%20and%20the%20Jews.pdf |
| **LEC1** | Hebrew University CRIS abstract of M. Lecker, *The "Constitution of Medina": Muhammad's First Legal Document* (Darwin 2004) | https://cris.huji.ac.il/en/publications/the-constitution-of-medina-muhammads-first-legal-document-2/ |
| **LEC2** | Publisher's description of Lecker, *The "Constitution of Medina"* (Gerlach Press 2024 ed.), bookseller page | https://www.theportobellobookshop.com/9783959941242 |
| **TOP** | M. S. Küçükaşçı, "İstanbul'daki Mukaddes Emanetler", *İstanbul Tarihi* (encyclopedic history, PDF) | https://istanbultarihi.ist/assets/uploads/pdf/istanbuldaki-mukaddes-emanetler-182.pdf |
| **BUK** | Sahih al-Bukhari, English text from the open hadith-api dataset (sunnah.com numbering; sunnah.com itself returned HTTP 403) | https://cdn.jsdelivr.net/gh/fawazahmed0/hadith-api@1/editions/eng-bukhari/7.json ; …/3043.json |
| **QA** | quran.com API v4 (verse texts; Saheeh Intl = id 20, Yusuf Ali = 22, Pickthall = 19; Ibn Kathir tafsir ids 169/14) (Part A) | https://api.quran.com/api/v4/verses/by_key/3:12?translations=20,22,19&fields=text_uthmani (and the same pattern for each verse) |
| **WD** | Wikidata (labelled; used only for uncontroversial dates and coordinates) | e.g. https://www.wikidata.org/wiki/Q716228 ; https://www.wikidata.org/wiki/Special:EntityData/Q35484.json |
| **CR** | Crossref metadata (via the crossref-search skill) | https://api.crossref.org/works/10.1163/9789004452909_005 |

---

## 1. Verification table

Row numbers are the extraction's timeline rows (T#) and §4 claim numbers (C#). Only rows that carry a checkable factual or date claim are listed. Rows 165–195 (deaths and reigns) are checked in block 1H. Rows marked "→ Part B" are in block 1G.

### 1A. Constitution of Medina and the early Medinan community

| # | Book claim (page) | Verdict | What independent sources say | Source URLs |
|---|---|---|---|---|
| T29 / C5 | The Constitution was prepared "to bring an end to the bitter in-fighting between the Arab war-lords of the tribe of Khazraj and their Jewish rivals" (p. 32) | **Inconsistent** (mis-describes the feud) | The pre-Hijra civil war was between the two Arab tribes **Aws and Khazraj**. It culminated in the battle of **Bu'ath** "shortly before the Hijrah", with Jewish clans fighting as allies on both sides: Qurayzah and al-Nadir with the Aws leader Hudayr, while Qaynuqa' were confederates of Khazraj. "No formal peace was made after Bu'ath … This was the uneasy position in Medina when negotiations with Muhammad commenced" (W pp. 157–158). Ibn Ishaq: "There were two parties: the B. Qaynuqa' and their adherents, allies of Khazraj; and al-Nadir and Qurayza and their adherents allies of Aus" (G p. 253). | W pp. 155–158; G p. 253 |
| T29 (dating) | Constitution undated in the book; "early Medina" | **Disputed among sources** (the book gives no date) | Ibn Ishaq places it near the start of the Medinan period without a date. Watt: "its place … is simply that called for by logic". Watt thinks the text is composite: early articles from the 'Aqabah pact or "shortly after the Hijrah", and "the document in its present form might belong to the period after the elimination of Qurayzah" (627) (W pp. 221, 227–228). Hamidullah: the first part dates to year 1 AH and the second (Jewish) part to after Badr, 2 AH, citing Abu Dawud (HAM pp. ~21–23). Lecker: "probably the first legal document of Muhammad and dates back to the first year after his hijra (622 CE)" (LEC2). See §2. | W; HAM; LEC2 |
| C7 | Clause "The Jews of Banu 'Awf are one community with the believers" (p. 32) | **Consistent** (quotation), but its reading is **Disputed** | Guillaume's text reads "The Jews of the B. 'Auf are one community with the believers (the Jews have their religion and the Muslims have theirs)" (G p. 233). Lecker argues that this common reading is mistaken: "Participating Jews instead received a guarantee of security (*amana*)", not *umma* status (LEC1). | G p. 233; LEC1 |
| C6, C11, C13 | Under the Constitution identity was no longer based on "family, tribe, kinship, or even religion"; Jews and Christians "belonged to the community of believers" (pp. 32–33) | **Opinion**, partly contradicted by the text | The document is organised clan by clan: "The B. 'Auf according to their present custom shall pay the bloodwit … The B. Sa'ida, the B. al-Harith …" (G p. 232). It says "the Jews have their religion and the Muslims have theirs" (G p. 233). It mentions no Christians. Watt: the three main Jewish tribes are probably **not** parties; "the Jews of B. 'Awf" are small Jewish groups attached to Arab clans (W p. 227). Lecker likewise holds that "most of Medina's Jewish tribes, including the large ones, did not join the document" (LEC1). | G pp. 231–233; W p. 227; LEC1 |
| C15 | "The payment of blood money … replaces the lex talionis" (pp. 34–35) | **Inconsistent** | Retaliation is retained: "Whosoever is convicted of killing a believer without good reason shall be subject to retaliation unless the next of kin is satisfied (with blood-money)". Bloodwit is paid "according to their present custom" (G p. 232). | G p. 232 |
| T30 | The Prophet "proclaimed Medina a haram or sacred place, thus barring all violence and weapons" (p. 35) | **Consistent** for *haram*. "barring all violence and weapons" is **Opinion** | "Yathrib shall be a sanctuary for the people of this document" (G p. 233). The same document regulates war, its costs and revenge for wounds, so it does not bar weapons. | G p. 233 |
| C19 | Non-Muslims "were not obliged to participate in the religious wars of the Muslims … rights without obligations"; when fighting together, "the cost of war was to be equally shared" (p. 35) | **Inconsistent** (overstated) | The Jews have explicit obligations: "The Jews shall contribute to the cost of war so long as they are fighting alongside the believers"; "The Jews must pay with the believers so long as war lasts"; "Each must help the other against anyone who attacks the people of this document"; "None of them shall go out to war save with the permission of Muhammad". On costs, "The Jews must bear their expenses and the Muslims their expenses" (G pp. 232–233). This is not "rights without obligations". | G pp. 232–233 |
| C18 | "The Qur'an and the Sunnah were enshrined as the sole basis for legislation" (p. 35) | **Minor difference / Opinion** | The text says only that disputes "must be referred to God and to Muhammad" (G pp. 232–233). Watt: "All that the Constitution explicitly states is that disputes are to be referred to Muhammad … his powers under the Constitution are so slight" (W p. 228). | G; W p. 228 |
| T31 | Brotherhood between Emigrants and Helpers (pp. 33, 35) | **Consistent** for the institution; the "rich with poor, black with white" pairing is **Opinion** | Ibn Ishaq heads the next section "Brotherhood between emigrants and helpers" (G p. 234). | G p. 234 |
| C21 | The Medinan state was founded "more than thirteen hundred years before" the UDHR (1948) (p. 35) | **Consistent** (arithmetic) | 622 + 1,300 = 1922, and 1948 is later. UDHR date: see Part B. | — |
| C28, C31–33 | The Prophet's letters "still exist in museums to this date"; 62 letters said sent, texts of 29 available; "over thirty-five" survive (pp. 33–34) | **Disputed among sources** | Four parchment "letters" (to al-Muqawqis, al-Mundhir b. Sawa, al-Harith b. Abi Shimr and Musaylima) are displayed in the Sacred Relics department of Topkapı (TOP). Their authenticity is contested. Wikipedia (lead only) cites Bolshakov, and Watt treats the story of the letters to the six rulers as theologically reshaped (W pp. 345–347). The 62/29 figures are attributed to Zeitlin and Dar Rah Haqq and were not checked. | TOP; W pp. 345–347; https://en.wikipedia.org/wiki/Al-Muqawqis (lead) |

### 1B. Meccan period and conversions

| # | Book claim (page) | Verdict | What independent sources say | Source URLs |
|---|---|---|---|---|
| T13–T15 / C48 | About twenty Christians from Abyssinia visit Muhammad in Mecca; Abu Jahl intercepts them; "it is said" they came from Najran; Q 28:52–55 "it is also said" revealed about them (Ibn Ishaq 179) (p. 37) | **Consistent** | The book's quotation matches the text word for word, including both hedges and "We have our religion and you have yours" (G p. 179). Ibn Kathir quotes the same Ibn Ishaq passage and adds al-Zuhri's view that the verses concern the Negus (Part A). | G p. 179; QA (Part A) |
| T16 | 'Addas, a young Christian from Nineveh enslaved at Ta'if, embraced Islam (p. 37) | **Consistent** | 'Addas says he is a Christian "from Nineveh" (G p. 193). | G p. 193 |
| T18 | "After a decade of persecution in Mecca" (p. 44) | **Minor difference** | Ibn Ishaq: at the Hijra the apostle "was fifty-three years of age, that being thirteen years after God called him" (G pp. 280–281). | G pp. 280–281 |
| T21–T24 / C41–43 | Salman: ex-Zoroastrian, served bishops and priests, sold by Kalb merchants to a Jew, then to a relative of the Banu Qurayzah; price 300 date palms and "1,600 silver coins"; gold "the size of a pigeon's egg"; Prophet planted the palms and none died (pp. 35–36) | **Consistent** with **minor differences** | Ibn Ishaq: Kalbite merchants sold him to a Jew at Wadi'l-Qura; "a cousin of his from B. Qurayza" bought him. Price: "three hundred palm-trees … and to pay forty okes of gold". Gold "as large as a hen's egg". "Not one of them died" (G pp. 95–98). The book's "1,600 silver coins" and "pigeon's egg" (from the InterIslam web text) differ from Guillaume's "forty okes of gold" and "hen's egg"; "nephew" vs "cousin". | G pp. 95–98 |
| T25–T26 / C46 | Ibn Sallam cries the *takbir* from a palm tree; aunt Khalida; hides in the Prophet's house; the Jews call him "our chief, and the son of our chief; our rabbi"; household and aunt follow (pp. 37–38) | **Consistent** | Word for word in G pp. 240–241. | G pp. 240–241 |
| C45 | Ibn Sallam's first words heard: "Spread peace … feed … pray at night … enter Paradise in peace" (p. 37) | **Consistent** | Tirmidhi 2485 (sahih); Ibn Majah 1334, 3251 (Part A). | Part A (hadith-api) |
| C47 | Qur'an 46:10 "presents him [Ibn Sallam] as a Jewish witness" (p. 38) | **Disputed among sources** | Bukhari 3812 and many early exegetes apply it to Ibn Sallam. Ibn Kathir (citing Masruq) says the verse is Meccan, predates his conversion and refers to witnesses in general. The Qur'an does not name him (Part A). | QA; BUK 3812 (Part A) |
| T27 | Safiyya's report: her father and uncle Abu Yasir visited the Prophet at Quba', returned weary; "Is he he?" … "I shall be his enemy as long as I live" (p. 38) | **Consistent** | G pp. 241–242. | G pp. 241–242 |
| T47 / C55–56 | Mukhayriq: learned rabbi rich in date palms; on the Sabbath of Uhud urged the Jews to help; killed; property to Muhammad; "Mukhayriq is the best of the Jews" (p. 38) | **Consistent** | G p. 241 (also p. 384). Baladhuri (from al-Waqidi) names him as of the Banu al-Nadir and lists his seven gardens as *sadaqa* land (BAL p. 34). | G pp. 241, 384; BAL p. 34 |
| T32–T33 | Hypocrites in the mosque "put out with some violence" (Ibn Ishaq 246); some rabbis falsely converted (p. 39) | **Consistent** | G p. 246, with a list of Jews "who hypocritically professed" Islam (G pp. 246–247). | G pp. 246–247 |
| C53 / C77 | Most Jews opposed Muhammad "due to the fact that he descended from Isma'il"; "racist reasons" (pp. 38, 41) | **Consistent with the Muslim tradition's attribution of motive**; as history it is **Opinion** | Ibn Ishaq: "About this time the Jewish rabbis showed hostility to the apostle in envy, hatred, and malice, because God had chosen His apostle from the Arabs" (G p. 239). The book's "Ishmael, not Isaac" and "racist" are its own glosses on this. Motives reported by one party cannot be checked independently. | G p. 239 |

### 1C. Badr and the three Jewish tribes

| # | Book claim (page) | Verdict | What independent sources say | Source URLs |
|---|---|---|---|---|
| T37 | Battle of Badr, 624 CE (p. 39) | **Consistent** | 17 Ramadan 2 AH. Watt: "The date given for the battle is the 17th, 19th, or 21st of Ramadan (ix) in the year 2 ( = 13, 15, or 17 March 624)" (W pp. 10–11). | W pp. 10–11 |
| T38 / C81 | "Just over 300 Muslims overwhelmed 900 enemy combatants" (p. 42) | **Consistent** | Muslims: "Thus the total number of Muslims … who were at Badr and were allotted a share in the booty was 314" (G p. 336). Meccans: the Prophet estimated "between nine hundred and a thousand" (G p. 295). | G pp. 295, 336 |
| T39–T40 / C58 | After Badr the Prophet assembled the Qaynuqa' in their market: "O Jews, beware lest God bring upon you the vengeance … become Muslims"; reply "if we fight you, you will find that we are real men!" (Ibn Ishaq 363) (p. 39) | **Consistent** | Word for word, G p. 363. | G p. 363 |
| T41 / C175 | Q 3:12–13 revealed in response (p. 39) | **Consistent** as an attribution to Ibn Ishaq. The occasion is **Disputed** | G p. 363. Guillaume's footnote cites "Sura 3. 10", a different verse numbering from the standard one; the quoted words are standard 3:12–13 (Part A). Al-Wahidi also gives an al-Kalbi report placing the verses after **Uhud**. Abu Dawud 3001 (the Ibn 'Abbas version) is graded weak (Part A). | G p. 363; Part A |
| T42 | Siege of Qaynuqa' "fourteen to fifteen days"; unconditional surrender (p. 39) | **Consistent** | Ibn Ishaq: "besieged them until they surrendered unconditionally", no duration (G p. 363). Ibn Sa'd: "mid-Shawwal, after the commencement of the twentieth month" (≈ April 624), "besieged them for fifteen days" (IS2 pp. 32–33). Watt: "after a siege of fifteen days" (W p. 209). | G p. 363; IS2 pp. 32–33; W p. 209 |
| T43 / C59 | Exiled, not killed; allowed to collect debts (Waqidi 89); went to Wadi al-Qura (p. 39) | **Consistent** | Ibn Sa'd: the Prophet "abandoned (the idea of) their killing and ordered them to be banished" (IS2 p. 33). Watt: "Three days were granted to them to collect money owing to them … they went to the Jewish colony at Wadi 'l-Qura, and after a month proceeded to 'Adhra'at in Syria" (W p. 209). Note that the "within his military rights to put them to the sword" clause (C59) is **Opinion**. | IS2 p. 33; W p. 209 |
| T44 | "Eventually, they settled permanently in **Defa** in Syria, to the west of Salkhad" (p. 39) | **Minor difference (probable OCR/typo)** | The sources name **Adhri'at / 'Adhra'at** (IS2 p. 33: "They went to Adhri'at where they lived for a short while"; W p. 209). Baladhuri places Adhri'at in the Hawran, near Busra (BAL, ch. on the conquest of Hawran, pp. 186–194). "Defa" is most likely a garbled "Der'a" (Daraa). Daraa (32.63 N, 36.11 E) does lie west of Salkhad (32.49 N, 36.71 E) (WD coordinates, labelled). The identification of Adhri'at with modern Der'a was not separately opened. Ibn Sa'd's "a short while" contradicts "settled permanently". | IS2 p. 33; W p. 209; BAL; WD Q238217, Q24343 |
| T45 / C67 | Ibn Ishaq's sequence (Qaynuqa' after Badr, Nadir after Uhud, Qurayza after the Trench) became the "orthodox" version (p. 40) | **Consistent** | Qaynuqa' "between Badr and Uhud" (G p. 363); "The deportation of the B. al-Nadir, A.H. 4" (after Uhud, G p. 437); Qurayza after the Trench (G pp. 461 ff.). | G pp. 363, 437, 461 |
| T46 / C66 | Muhammad al-Kalbi "(737–819 CE)" makes no mention of the Qaynuqa' incident; no conflict with the Jews before Uhud (Scholler 26–27) (p. 40) | **Attribution Unverified; dates Inconsistent** | The cited work is identified as Marco Schöller, "Sīra and Tafsīr: Muḥammad al-Kalbī on the Jews of Medina", in H. Motzki (ed.), *The Biography of Muḥammad* (Brill 2000), pp. 18–48 (CR). The Brill page returned HTTP 403, so the content was **not** read. **Dates:** Ibn Sa'd says Muhammad b. al-Sa'ib al-Kalbi "died in Kufa in 146 AH" (= 763 CE) (ISB vol. VI p. 345). The book's "737–819" are the dates of his **son**, Hisham b. al-Kalbi (WD Q716228, labelled: "Arab historian (737–819)"). Al-Wahidi preserves an al-Kalbi report dating the 3:12 episode after Uhud (Part A), which fits the claim in substance. | CR; ISB VI p. 345; WD Q716228; Part A |
| T49 | Before the 625 exile the Banu Nadir made "at least two attempts on the life of the Prophet, including an incident in which Muhammad was as close as a poisoned mouthful away from death" (p. 39) | **Inconsistent** (anachronism) | The Nadir plot of 4 AH in the sources is a rock to be dropped from a roof (G p. 437; IS2 pp. 68–69; BAL p. 34). The **poisoned-lamb** episode happened at **Khaybar in 7 AH**, after the conquest. The poisoner was Zaynab d. al-Harith, wife of Sallam b. Mishkam: "He took hold of the shoulder and chewed a morsel of it … spat it out" (G p. 516). It cannot precede the 625 exile. | G pp. 437, 516; IS2 pp. 68–69; BAL p. 34 |
| T50 | Exile of the Banu Nadir "in the year 625 CE" (p. 39) | **Consistent** (all sources opened agree on 4 AH / 625) | Ibn Ishaq: A.H. 4 (G p. 437). Ibn Sa'd: Rabi' I, "after the commencement of the thirty-seventh month" (IS2 p. 68). Watt: "August 625 (iii/4)" and "late August or early September 625" (W pp. 34, 210–211). Baladhuri: "This occurred in the year 4 of the Hegira"; also al-Zuhri: "six months after the battle of Uhud" (BAL pp. 34–35). | G p. 437; IS2 p. 68; W pp. 34, 210–211; BAL pp. 34–35 |
| T51 / C60 | 'Abd Allah ibn Ubayy, "chief of the hypocrites", "falsely promised two thousand reinforcements"; Nadir "roundly defeated"; given free passage; most to Khaybar, others to Syria (p. 39) | **Consistent**, with one **Minor difference** | Ibn Ubayy's message: "there are two thousand people of my tribe and other Arab tribes … with me" (IS2 p. 69). Ibn Ishaq: "they waited for the help they had promised, but they did nothing"; "Some went to Khaybar and others went to Syria" (G p. 437). The sources describe a siege of about 15 days ending in capitulation on terms (IS2 p. 70; BAL p. 34), not a battle, so "roundly defeated" overstates. | IS2 pp. 69–70; G p. 437; BAL p. 34 |
| T52 / C62 | Qurayza had two treaties with the Muslims, the Charter of Medina and a second one "signed at the time of the battle with the Banu Nadir" (Qureshi 261) (p. 40) | **Disputed among sources** | Watt: "the three main Jewish groups are not included in the document" (W p. 227). Lecker: the large Jewish tribes did not join the Constitution and instead had "looser non-belligerency treaties" (LEC1). Kister summarises the tradition that Qurayza "are said to have concluded a pact with the Prophet" (KIS p. 61). So a separate pact is attested, but Qurayza's membership of the Constitution is doubted. | W p. 227; LEC1; KIS p. 61 |
| T53–T55 / C61 | "In 627 CE" Qurayza negotiated with the besiegers; charged with treason; "besieged for twenty-five days" (p. 40) | **Consistent** | Kister: "April 627 A.D./Dhu l-Qa'da 5 A.H." (KIS p. 61). Watt: the siege of Medina "began on 31 March 627 (8/xi/5)" (W p. 36). Ibn Ishaq: "The apostle besieged them for twenty-five nights" (G p. 461). | KIS p. 61; W p. 36; G p. 461 |
| T56–T57 | Some Qurayza converted during the siege; the emissary offered a new agreement, or Judaism with *jizyah*; they "preferred to die than to pay taxes" (Waqidi 247) (p. 40) | **Unverified** | Al-Waqidi (Faizer tr.) was not available to open. Ibn Ishaq instead has Ka'b b. Asad propose three options to his own people: accept Muhammad, kill their families and fight, or attack on the Sabbath (G pp. 461–462). That is a different account. | G pp. 461–462 |
| T58 / C64 | They asked "to be judged by a member of the Arab tribe to which they were adherents"; the execution "had been decided by a judge appointed by the Jewish people, and who had ruled on the basis of the Torah" (p. 40) | **Disputed among sources** (the "Torah" basis is a modern interpretation) | Ibn Ishaq: the **Aws** pleaded for their allies; the **Prophet** proposed one of their own number and named Sa'd b. Mu'adh; the verdict is called "the judgement of Allah above the seven heavens" (G pp. 463–464; T8 p. 35). Bukhari 3043: "When the tribe of Bani Quraiza was ready to accept Sa'd's judgment …" (BUK). Kister: the Prophet "proposed to appoint as arbiter a man from Aus … Qurayza consented" (KIS p. 62). The Deuteronomy/Torah argument is Hamidullah's: "the arbitrator of their own choice who awarded exactly what Deuteronomy provided" (*Muslim Conduct of State* §497, quoted in KIS p. 64 n. 3). It is not in the early sources. Sa'd was a Muslim of the Aws, not a Jew. | G pp. 463–464; T8 p. 35; BUK 3043; KIS pp. 62, 64 |
| T59–T60 | Men "alleged to have been beheaded", women and children enslaved; "the seven hundred men of Qurayzah" (pp. 40–41) | **Consistent** (as the traditional account). The figure is **Disputed** | Ibn Ishaq: "There were 600 or 700 in all, though some put the figure as high as 800 or 900" (G p. 464; T8 p. 35). Kister collects figures of 400, 600, 700, 800 or 900 from many sources (KIS pp. 62, 89–90 nn.). | G p. 464; T8 p. 35; KIS |
| T61 / C65 | Historicity of the mass execution "has been called into question (Donner 73)"; clashes "may have been greatly exaggerated" (p. 40) | **Unverified** (Donner p. 73 not accessible) | Donner's *Muhammad and the Believers* (HUP 2010) could not be opened: the HUP page was empty and the JSTOR book requires a login. The scholarly dispute itself is documented: W. N. Arafat, *JRAS* 1976, denied the massacre; Kister 1986 rebutted him (KIS pp. 63–66). See §4. | KIS |
| T62–T63, T169 | Rayhana "married the Messenger of Allah and eventually embraced Islam. She died in 631 CE, shortly after the Prophet's Farewell Pilgrimage, a mere one year before his death" (p. 40) | Marriage: **Disputed among sources**. Death date: **Inconsistent** (calendar) | **Marriage:** Ibn Ishaq says she stayed "in his power" after refusing marriage (G p. 466). Ibn Sa'd gives both versions; al-Waqidi prefers manumission and marriage (ISB VIII pp. 92–93). **Death:** "She remained with him until she died on his return from the Hajj of Farewell" (ISB VIII p. 92). The Farewell Pilgrimage was "March 632 (xii/10)" and the Prophet died "8 June 632" (W pp. 79–80). So she died in **632**, about two to three months, not a year, before the Prophet. "631" can arise only from equating 10 AH with 631. | G p. 466; ISB VIII pp. 91–93; W pp. 79–80 |
| T65 / C68 | Khaybar "located 150 kilometers from Medina" (p. 40) | **Consistent** | The straight-line distance is about 140 km (Medina 24.47 N, 39.61 E; Khaybar 25.70 N, 39.29 E; WD coordinates, labelled; great-circle computation). The route distance is longer. | WD Q35484, Q27125 |
| T66 / T68 | "The Muslims marched on Khaybar, surrounded the city, and compelled the Jews to surrender" (p. 40), versus "the Jews of Khaybar surrendered without any significant fighting … a treaty was concluded by means of emissaries" (Scholler 39) (p. 41) | **Disputed among sources** | Ibn Ishaq: "The apostle seized the property piece by piece and conquered the forts one by one … The first to fall was the fort of Na'im", with single combats such as Marhab's (G pp. 511–513). The no-fighting version is the one the book attributes to Schöller's reading of al-Kalbi, which could not be opened. | G pp. 511–513 |
| T67 / C70 | Safiyya chose Islam, was freed and married, "her freedom being her dowry"; "seventeen year old" (pp. 40–41) | **Consistent** on manumission as dowry. Age **Unverified** | Ibn Sa'd: "She became Muslim and he set her free and married her and made her emancipation consist of her dower" (ISB VIII p. 85). Her age was not found in the texts opened. | ISB VIII p. 85 |
| T69 / C71–72 | Three versions of the Khaybar land settlement; the third (Fadak fell to Muhammad alone, left to the Jews for share-cropping) "most sound" (p. 41) | **Consistent** that Fadak was the Prophet's personal property; the ranking is **Opinion** | "Fadak was the personal property of the apostle because they had not driven horses or camels against it" (G p. 516). | G p. 516 |
| T70 | "Many traditions state that the Jews were only expelled from Khaybar by … 'Umar" (p. 41) | **Consistent** | Baladhuri (from Ibn Shihab): "'Umar ibn-al-Khattab investigated until he found it certain … that the Prophet had said, 'There can be no two religions at the same time in the Arabian peninsula.' Accordingly, he expelled the Jews of Khaibar" (BAL p. 48). | BAL p. 48 |
| T71 | "More than twenty Jewish tribes living in Medina" (Levy 158) (p. 41) | **Minor difference** | Watt: "The authentic Jewish tribes or clans are commonly said to be three … This is a simplification … As-Samhudi has a list of about a dozen clans in addition", besides groups "clearly of Arab extraction" (W p. 193). | W p. 193 |
| T72 | Neutral Jewish clans "were allowed to remain in Medina unmolested" (p. 42) | **Consistent** | Watt suggests the Constitution "in its final form was intended as a charter for the Jews remaining in Medina" (W p. 227). Barakat Ahmad: "the Jews were still in Medina in the ninth year of the Hijrah" (BA ch. on expulsions). | W p. 227; BA |
| C73–C74 | Barakat Ahmad's book "cast doubts on … Ibn Ishaq's account … colored by 'Abbasid ideas"; "As far as Ahmad is concerned, no Jews were executed or expelled from Medina during Muhammad's life" (p. 41) | First half **Consistent**; second half **Inconsistent** (misrepresents Ahmad) | Ahmad denies the **Qaynuqa'** expulsion: "the evidence seems to indicate that the B. Qaynuqa' were not expelled during the Apostle's lifetime". But he **accepts** the Nadir banishment: "Surat al-Hashr … deals with the banishment of the B. al-Nadir from Medina", and "After the banishment of the B. al-Nadir …". He also accepts that some Qurayza leaders were executed: "The leaders, Huyayy b. Akhtab, Ka'b b. Asad … were executed", their number would "not … exceed sixteen, or seventeen" (BA, chs. on Qaynuqa' and Qurayza). | BA |
| C (p. 41) | "More likely, it was Ibn Hisham … who was responsible for this more polemical perspective" (p. 41) | **Opinion**, which the evidence weakens | Guillaume's Introduction (the page the book cites as xvii; the passage lies between pp. xv and xxi of the scan) does say Ibn Hisham's text was "abbreviated, annotated, and sometimes altered". But the Qurayza account also survives in **al-Tabari's independent recension of Ibn Ishaq** (Salama b. al-Fadl, not Ibn Hisham): "They numbered 600 or 700—the largest estimate says they were between 800 and 900" (T8 p. 35). Kister notes that Abu 'Ubayd (d. 224 AH) records the same reports "almost identical with … Ibn Ishaq" through different chains (KIS p. 69). | G Introduction; T8 p. 35; KIS p. 69 |

### 1D. Campaigns and numbers

| # | Book claim (page) | Verdict | What independent sources say | Source URLs |
|---|---|---|---|---|
| T122 / C82–83 | The Prophet took part in **30** raids/expeditions and sent **61** forays (lists, pp. 42–43) | **Inconsistent** with the classical totals (counts vary by compiler) | Ibn Ishaq: "The apostle took part personally in twenty-seven (T. six) raids", fought in nine; "expeditions and raiding parties … were thirty-eight (T. thirty-five)" (G pp. 659–660). Ibn Sa'd (from Musa b. 'Uqba): 27 *ghazwas* and **47** *sariyyas*, fighting in nine (IS2 p. 2). The book's lists contain duplicates (see extraction §7 item 15) and match none of these totals. | G pp. 659–660; IS2 p. 2 |
| T123 / C85 | "Muhammad spent no more than 89 days in battle" (p. 43) | **Unverified** | The book gives no source. No classical or modern source giving "89 days" was found; web searches were exhausted. | — |
| T124 / C86 | Arabia brought under Islamic rule "at the cost of approximately one thousand casualties" (p. 43) | **Unverified**, with internal tension | No source was found. On the traditional figures alone, the Qurayza execution (400–900 men; KIS pp. 62, 89–90) would account for most of a 1,000 total. Add the Meccan dead at Badr ("the total number of Quraysh slain at Badr as given to us is 50", G p. 338), the Muslim dead at Uhud (total given G p. 403) and so on. The figure is therefore plausible only if the Qurayza tradition is rejected, which the book does tentatively. | KIS; G pp. 338, 403 |
| T121 | "the Army of Usamah … the final expedition ordered by the Messenger of Allah" (p. 43) | **Consistent** | "The sending of Usama b. Zayd to Palestine" is the last expedition, ordered in his final illness (G p. 652). | G p. 652 |
| C84 | Most raids were "short actions … with little to no bloodshed" (p. 43) | **Opinion** (broadly compatible) | Ibn Ishaq: he "actually fought in nine" of 27 (G p. 660); Ibn Sa'd, the same (IS2 p. 2). | G p. 660; IS2 p. 2 |
| C92 | Saying "Both I smile and I fight" (Ibn Taymiyya via Hamidullah) (p. 43) | **Disputed among sources** | Ibn Taymiyya cites «أنا الضحوك القتال» as the Prophet's words. His modern editor: "we did not find the hadith", only an Ibn 'Abbas report that this is the Prophet's name "in the Torah" (Part A). | https://shamela.ws/book/305/80 (Part A) |

### 1E. Treaties, letters and delegations (2–10 AH)

| # | Book claim (page) | Verdict | What independent sources say | Source URLs |
|---|---|---|---|---|
| T35–T36 / C96 | Treaty with the Banu Damrah, 2 AH: non-aggression, later widened (pp. 44–45) | **Consistent** | Raid of Waddan/al-Abwa', Safar "at the beginning of the twelfth month" after the Hijra (= Safar 2 AH): "The B. Damra there made peace with him through their leader Makhshi b. 'Amr al-Damri" (G pp. 280–281). Ibn Sa'd: neither side would fight the other, and Damra would not help his enemies; "He wrote a document for the two parties" (IS2 p. 5). The widened text (Hamidullah, *Muslim Conduct*) was not opened. | G pp. 280–281; IS2 p. 5 |
| T73 / D6 | Treaty of Ashja', 5 AH, dictated to 'Ali; "pledge concluded by Na'ym ibn Mas'ud al-Ashja'i", valid "so long as the Mountain of Uhud remains standing and the sea wets the shells"; clan embraced Islam in 5 AH (p. 45) | **Consistent** (minor wording) | Ibn Sa'd: "This is an agreement made by Nu'aym Ibn Mas'ud Ibn Rukhaylah al-Ashja'i … as long as Uhud remains at its place and the ocean water drenches **wool**. 'Ali had scribed it". Deputation of Ashja' "in the year of the Battle of the Ditch" (5 AH), 100 men; "He made peace with them … Then they embraced Islim" (IS1 pp. 324, 362). Wool vs shells is a translation variant. | IS1 pp. 324, 362 |
| T74 | "According to the Chronicle of Seert, the Arabs commenced their conquests in the year **5 AH** … (627/28 CE)" (p. 45) | **Inconsistent** (minor; conversion error) | The Chronicle uses no hijri year. It says: "En la dix-huitième année d'Héraclius … année en laquelle régna Ardašir fils de Široi … les Arabes commencèrent leurs conquêtes, et l'Islam devint puissant" (PO13 p. 600 [280]). Scher's notes equate the 18th year of Heraclius with 627/8 and date Ardashir's accession after September 628. **5 AH = June 626–May 627**; 627/28 corresponds to 6–7 AH. | PO13 pp. 600–601 [280–281] |
| T75–T76 / C99 | Najran's Christians, "headed by Sayyid Ghassani", brought presents, offered to fight under his banner; Prophet gave them a covenant; 'Umar made a second (p. 45) | **Consistent** as an attribution to the Chronicle | "Les habitants de Najran conduits par le Seyyid Ghassâni, le chrétien, allèrent le trouver, lui apportant leurs présents … ils s'engagèrent … à combattre sous ses bannières … Il accepta leurs présents et leur écrivit un pacte et un édit. 'Omar ben el-Khattâb en fit un autre durant son califat" (PO13 p. 601 [281]). The Chronicle adds that its copy came from a register "retrouvé en 265 [AH = 878–879] … chez Habib le moine" (PO13 p. 601), i.e. a late transmission. Historicity was not assessed here. | PO13 p. 601 |
| T77 / D8 | Treaty of Saint Catherine "in the year 6 AH (628 CE)", dictated "to Mughirah" (Qureshi 155) (p. 45) | **Unverified** (left to the Sinai-covenant check) | No critical edition of the Sinai *Achtiname* was opened in this part. Ratliff (Sinaiticus 2008) describes the document and its removal to Selim I's palace in 1517 but gives no hijri date in the text read. Note the internal tension: 6 AH ends in April 628, while the book's own Chronicle-based argument (p. 45) puts the Najran covenant earlier. | scratchpad copy of Ratliff, *Sinaiticus* 2008 (not re-fetched) |
| T78–T79 / C101 | Letter to Hawdhah b. 'Ali of Yamamah via Sulayt (Salit) b. 'Amr al-'Amiri; Hawdhah offered to follow if given a share of power; the Prophet declined, "he did make an ally, but one who unfortunately died shortly after" (pp. 45–46) | Facts **Consistent**; "made an ally" **Inconsistent** | Ibn Sa'd: Salit b. 'Amr carried the letter. Hawdhah replied "I am the poet of my people and their preacher … share with me a part of your affairs, so that I may follow you". The Prophet said: "If he had asked for the flowing of water, I would not have given him; **may he perish!**" Hawdhah died after the conquest of Mecca (IS1 p. 309). That is not an alliance. | IS1 p. 309 |
| T80–T81 / D10 | Letter to the Negus al-Asham b. Abjar; reply: "I have sent you my son Arha" (Ibn Ishaq 657–658) (pp. 46–47) | **Consistent** | G pp. 657–658: "…al-Asham b. Abjar … I have sent to you my son Arha". Ibn Sa'd dates the dispatch, carried by 'Amr b. Umayya al-Damri, to **Muharram 7 AH (May 628)** (IS1 pp. 304–305). The Prophet's letter (G p. 657) says "my **nephew** Ja'far"; the book's Qureshi text says "my cousin" (minor). | G pp. 657–658; IS1 pp. 304–305 |
| T82 / C191 | "Leave the Abyssinians in peace, so long as they do not take the offensive" (Abu Dawud, Nasa'i) (p. 47) | **Minor difference** | Abu Dawud 4302 and Nasa'i 3176 (both *hasan*): "Let the Abyssinians alone as long as they let you alone, and let the Turks alone …". The book omits the Turks clause; in Nasa'i the saying comes at the Trench (Part A). | Part A (hadith-api) |
| T83 / D11 | Letter to Heraclius "probably sent in 627 CE" (p. 47) | **Disputed among sources** | **Traditional:** Ibn Sa'd: after Hudaybiya (Dhu'l-Hijja 6 AH), six envoys "set out, in one day, and this was in Muharram, 7 H. (May, A.C. 628)". Dihya delivered it via the governor of Busra to Heraclius "at Emessa, as he was going on foot from Constantinople to Iliya" after defeating the Persians (IS1 pp. 304–306). Bukhari 7: Heraclius received Abu Sufyan "at Ilya (Jerusalem)" "at the time when Allah's Messenger had truce with Abu Sufyan" (BUK 7), i.e. after March 628. Watt dates the Holy Rood's restoration to Jerusalem to March 630 (W p. 114). **Revisionist:** Watt argues "the sending of some of the envoys was prior to al-Hudaybiyah. The mission of Dihyah to Bostra must have been in the summer of 627" (W p. 345). The book's "627" matches Watt's reconstruction, not the Muslim sources. | IS1 pp. 304–306; BUK 7; W pp. 113–114, 345 |
| T84 / C103 | Heraclius, "initially inclined to embrace Islam", was pressured by "ecclesiastic advisors"; mobilised near Damascus; "After conquering the cities of Lakhm and Judham, he intended to invade Medina" (p. 47) | **Minor difference** (advisers) and **Inconsistent** (Lakhm, Judham) | Ibn Sa'd: Heraclius addressed "the Roman grandees in a church at Emessa"; they "ran away like wild asses"; he then said he had only been testing them (IS1 p. 306). Lakhm and Judham were **Arab tribes** allied to Byzantium, not cities. Baladhuri: the Prophet marched to Tabuk "for the invasion of those of the Greeks, 'Amilah, Lakhm, Judham and others whom he learnt had assembled against him" (BAL p. 92). | IS1 p. 306; BAL p. 92 |
| T85 / C180 | Message from Tabuk to Heraclius quoting the jizyah verse (Bahnasawy 13–14) (p. 47) | Verse **Consistent** (= Q 9:29, Part A). The letter itself is **Unverified** | Not found in Ibn Ishaq's Tabuk narrative (G pp. 602–609). | QA (Part A); G pp. 602–609 |
| T88–T89 / C109 | Letter to al-Muqawqis carried by "Hatib ibn Abu Balta'a **al-Khami**"; placed in an ivory casket; reply: the prophet "would be born in Syria"; two maids, clothing, a steed; the letter "is preserved in a library in Egypt" (p. 48) | Narrative **Consistent** (al-Khami ≈ al-Lakhmi). Location **Inconsistent** | Ibn Sa'd: "Hatib Ibn Abi Balta'ah al-**Lakhmi** … to al-Muqawqis … placing it in a vessel of ivory … I thought he would rise in Syria … two slave-girls … a mantle and a mule", "and he did not embrace Islam" (IS1 pp. 307). **Location:** the parchment presented as this letter is displayed in the Sacred Relics department of **Topkapı Palace, Istanbul**: "Hz. Peygamber'in … Mısır Genel Valisi Mukavkıs'a … gönderdiği İslam'a davet mektupları Mukaddes Emanetler Dairesi'nde sergilenmektedir" (TOP). Wikipedia (lead only), citing Tahsin Öz 1953, adds that it was found in Akhmim, Egypt, and brought to Istanbul under Abdülmecid I. Its authenticity is disputed. | IS1 p. 307; TOP; https://en.wikipedia.org/wiki/Al-Muqawqis (lead) |
| T90 / C110 / C192 | Letter to Chosroes; "the new Persian Emperor" tore it up; "Even so, O Lord, tear from him his kingdom" (pp. 48–49) | Tearing **Consistent**; "new emperor" **Disputed**; wording **Minor difference** | Ibn Sa'd: 'Abd Allah b. Hudhafa delivered it; Kisra "tore it"; the Prophet said "O Allah: Tear (break) his kingdom". Kisra was then killed by his son Shirawayh, which Ibn Sa'd dates to 10 Jumada I 7 AH (IS1 pp. 306–307; similar G pp. 658–659). The traditional recipient is therefore Khosrow II Parwiz, not a "new" emperor. Watt: "In February 628 … the Persian emperor was assassinated" (W p. 114), i.e. **before** the May 628 dispatch. Watt also doubts "whether any envoy went to the court of the Persian emperor" (W p. 346). Part A: the book's English follows H. G. Wells, who names the recipient Kavadh (628). | IS1 pp. 306–307; G pp. 658–659; W pp. 114, 346; Part A |
| T91 | "Within ten short years … the Muslims conquered Persia" (p. 49) | **Minor difference / approximate** (not fully checked) | Ibn Sa'd's own story has the Sasanian governor of Yemen, Badhan, convert in 7 AH (IS1 p. 307). The conquest of Iran proper was not checked here. Part B was not tasked with it. | IS1 p. 307 |
| T92–T93 / C112–113 | Letter to "the King of Bahrayn" Mundhir b. Sawa al-Tamimi; "the Persian inhabitants of the **island nation**"; conditions; Abu Hurayra sent to collect taxes (pp. 49–50) | Narrative **Consistent**. "Island nation" and "Persian inhabitants" **Inconsistent** | Ibn Sa'd: after al-Ji'irrana (end of 8 AH) the Prophet sent al-'Ala' al-Hadrami "to al-Mundhir Ibn Sawa al-'Abdi who was in al-Bahrayn". Mundhir read the letter "before the people of **Hajar**"; "In my country there are Magians, and Jews also"; Abu Hurayra was sent with al-'Ala' (IS1 pp. 310–311). Baladhuri: "The land of al-Bahrain formed a part of the Persian kingdom. In its **desert** lived a great many Arabs from the tribes of 'Abd-al-Kais, Bakr ibn-Wa'il and Tamim"; al-Mundhir ruled the Arabs "in the name of the Persians" and was of Tamim (b. Darim), so "al-Tamimi" is fine (BAL pp. 120–121). Watt: "Most of the Arabs of al-Bahrayn belonged to the tribe of 'Abd al-Qays … Moreover the population included Persians, Christians, and Jews" (W pp. 131–132). Seventh-century al-Bahrayn was the eastern Arabian mainland (Hajar), with a mainly Arab population. | IS1 pp. 310–311; BAL pp. 120–121; W pp. 131–132 |
| T94 / C115 | Letter to the kings of Oman, "written by Ubbay b. Kab", delivered by 'Amr b. al-'As to the sons of Julunda, "Junayfir" and 'Abd; both embraced Islam after debate (p. 50) | **Consistent**, with **Minor difference** (name). Scribe **Unverified** | Ibn Sa'd: 'Amr b. al-'As was sent "in (the month of) Dhu al-Qa'dah, 8 H. to **Jayfar** and 'Abd sons of al-Julanda … Jayfar was their ruler". After some days "He and his brother accepted Islam" (IS1 pp. 309–310). "Junayfir" is a corruption of Jayfar. Ubayy b. Ka'b as scribe is not stated in the Ibn Sa'd passage read. | IS1 pp. 309–310 |
| T95–T96 | "Around the year 628 CE" letter to al-Harith (b. Abi Shimr), ruler of the Ghassanids, carried by "Mubarak Shuja' ibn Wahab al-Asadi"; al-Harith, "ruler of Damascus", furious: "Who dares dispossess me of my country? I will fight him"; "the Prophet sent his forces to conquer the region of Ghassan" (p. 51) | Letter **Consistent**. "Sent his forces to conquer" **Inconsistent** | Ibn Sa'd: Shuja' b. Wahb al-Asadi, one of the six envoys of Muharram 7 AH (May 628), found al-Harith "at Ghutah of Damascus". Al-Harith said "Whoever disputes with me about my country I shall march against him". Caesar told him **not** to march. Al-Harith "died in the year of Victory" (8 AH) (IS1 pp. 307–308). No source read reports a Muslim conquest of Ghassan in the Prophet's lifetime. Watt: Ghassan "showed no signs of accepting Islam" (W p. 114). The name prefix "Mubarak" is not in Ibn Sa'd. | IS1 pp. 307–308; W p. 114 |
| T97–T99 | Dumat al-Jandal "had initially antagonized the Muslims by stopping traffic to Medina and threatening to invade"; 700 men under 'Abd al-Rahman b. 'Awf; three days; al-Asbagh, Christian leader of Kalb, converted; others paid *jizyah*; Tamadhir married to 'Abd al-Rahman (pp. 51–52) | **Consistent**, with a **Minor difference** (two expeditions merged) | 'Abd al-Rahman's expedition, **Sha'ban 6 AH**: "He stayed there for three days … al-Asbagh Ibn 'Amr al-Kalbi, who was a Christian joined the fold of Islam … He who promised to pay al-Jizyah remained in his old faith. 'Abd al-Rahman married Tumadir" (IS2 p. 110). The traffic harassment and threat to Medina belong to the Prophet's own **ghazwa of Rabi' I 5 AH** with 1,000 men: "they treated cruelly the camel-riders … and intended to attack al-Madinah" (IS2 p. 76). The figure of 700 is not in the Ibn Sa'd passage. | IS2 pp. 76, 110 |
| C117 | Dumat = al-Jawf, "five hundred miles from Medina", "some seven days by caravan south of Damascus", southern end of Wadi Sirhan (p. 51) | **Minor difference** | Ibn Sa'd: "on the border of Syria at five days' journey from Damascus and fifteen or sixteen days' journey from al-Madinah" (IS2 p. 76). The straight-line distance Medina–Dumat is about 594 km (369 mi), and Damascus–Dumat about 533 km (WD coordinates, labelled; computed). "500 miles" overstates the straight line. | IS2 p. 76; WD Q35484, Q2719371, Q3766 |
| T98 / C118 / C193 | The exhortation to 'Abd al-Rahman: "Fight everyone in the way of Allah **[who attacked you or betrayed you]** and kill those who disbelieve … nor kill children" (Ibn Ishaq 672) (p. 52) | **Minor difference** (an interpolation inside the quotation) | Guillaume: "fight everyone in the way of God and kill those who disbelieve in God. Do not be deceitful with the spoil; do not be treacherous, nor mutilate, nor kill children. This is God's ordinance and the practice of his prophet among you" (G p. 672). The bracketed clause is **not** in Guillaume. It is the author's insertion and narrows the command's meaning. | G p. 672 |
| T100–T101 / C119 | "Several years later" Khalid captured Ukaydir, "Christian prince of Dumat", whose brother was killed. Ukaydir had to (1) embrace Islam, (2) make peace, (3) collect tribute from Dumat, Tabuk, Aylah and Tayma'. Ransom of 2,000 camels, 800 sheep, 400 coats of armour, 400 lances. Treaty sealed with the Prophet's thumb-print (Waqidi 505). Book also calls Ukaydir "the successor of al-Asbagh" (p. 52) | Date, capture and ransom **Consistent** (sheep vs cattle minor). Conversion **Disputed**. "Successor of al-Asbagh" **Inconsistent**. Tribute clause **Unverified** | Ibn Sa'd: Khalid with 420 horsemen, **Rajab 9 AH**; "Ukaydir belonged to the Kindah … and he was a Christian"; his brother Hassan was killed. Peace was made "for two thousand camels, eight hundred heads of cattle, four hundred coats of mail and four hundred spears". The Prophet "concluded peace with him on the condition of the payment of al-Jizyah … He placed his thumb impression on it" (IS2 pp. 205–206). Ibn Ishaq: "a man of Kinda … he was a Christian", spared "on condition that he paid the poll tax" (G pp. 607–608; T9 pp. 58–59). **But** the document text in al-Waqidi/Ibn Sa'd and Baladhuri says Ukaydir "accepted Islam and forsook the objects of worship and idols" (IS1 p. 342; BAL p. 95). Ukaydir was of **Kinda**, not of Kalb, so "successor of al-Asbagh" has no support. | IS2 pp. 205–206; G pp. 607–608; T9 pp. 58–59; IS1 p. 342; BAL p. 95 |
| T103 | "Soon … Ukaydir broke his word and the covenant" (p. 53) | **Consistent** | Baladhuri: "no sooner had the Prophet been dead, than Ukaidir stopped the payment of the sadakah, violated the covenant"; Khalid later killed him on Abu Bakr's orders (BAL p. 96). | BAL p. 96 |
| T104 / C121 | "In the year 8 AH (630 CE)" the 'Abd al-Qays (branch of Rabi'ah, in Bahrayn, "included some Christians") sent "a fourteen member delegation, headed by Jarud ibn Amr, who professed the Christian faith" (p. 53) | **Disputed among sources**. "Headed by Jarud" **Inconsistent** | Ibn Sa'd: "Twenty persons came to him under the leadership of '**Abd Allah Ibn 'Awf al-Ashajj**; and among them were al-Jarud … Their arrival was in the year of the Victory" (8 AH). "Al-Jarud was a Christian … He embraced Islam" (IS1 pp. 370–371). Ibn Ishaq has al-Jarud b. 'Amr come with the 'Abd al-Qays deputation among the deputations of 9–10 AH (G pp. 635–636). The number 14 (or 13) is a separate tradition not opened here. 8 AH spans May 629–Apr 630. | IS1 pp. 370–371; G pp. 635–636 |
| T105 | "In approximately the same period" (8 AH) treaties with Christian and Jewish leaders of al-Aqabah, Maqnah, Adhruh and al-Jarbah (quoted, "(12)") (p. 53) | **Minor difference** (date) | These treaties were concluded during the **Tabuk** campaign, **9 AH**: "When the apostle reached Tabuk Yuhanna b. Ru'ba governor of Ayla came … The people of Jarba' and Adhruh also came and paid the poll tax" (G p. 607; T9 p. 58; BAL pp. 92–93). Ibn Sa'd: "The people of Maqna were Jews … the people of Jarba and Adhruh were also Jews" (IS1 p. 345); Yuhanna of Ayla wore "a cross of gold" (IS1 p. 344). | G p. 607; T9 p. 58; BAL pp. 92–93; IS1 pp. 344–345 |
| T107 / D20–D20a / C122–124 | Treaty of Maqnah, 9 AH, with "the Jews of the Banu Janbah, Banu Habibah or Banu Haninah"; one-fourth of dates, fish catch and women's spinning; exempted from jizyah and forced labour (pp. 53–54) | **Consistent** | Ibn Sa'd: "to Banu Janbah, the Jews of Maqna … near Aylah … one-fourth of the yield of your date palms, and one-fourth of your game from the rivers, and one-fourth of what your women spin … exempt from jizyah and forced labour" (IS1 pp. 327–328). Baladhuri: "to the banu-Habibah and the inhabitants of Makna … Written by 'Ali-ibn-abu-Talib in the year 9" (BAL pp. 93–94). | IS1 pp. 327–328; BAL pp. 93–94 |
| T108 / D21 | People of Adhruh: 100 dinars "on every Rajab" (p. 54) | **Consistent** | "In every Rajab they will pay one hundred dinars pure and of full weight" (IS1 p. 344; BAL p. 92). | IS1 p. 344; BAL p. 92 |
| T109 / D22 / C126 | Letter to Yuhanna b. Ru'ba: give Harmala three *wasqs* of barley; clothe Zayd; threat to take the young captive and slay the elders (p. 54) | **Consistent** | "Provide Zayd with good clothes … make your young ones captive and shall slay your elders … Pay three wasaq of barley to Harmalah" (IS1 pp. 328–329). | IS1 pp. 328–329 |
| T110 | "Not only did Yuhannah b. Ru'bah respond, he came in person to **Medina** … treated him as a guest … provided him with a cloak" (p. 54) | Place **Inconsistent**; cloak **Consistent** | Ibn Ishaq: "When the apostle reached **Tabuk** Yuhanna b. Ru'ba governor of Ayla came and made a treaty with him" (G p. 607). The same in al-Tabari (T9 p. 58) and Baladhuri: "During his stay at Tabuk, there came to him Yuhanna" (BAL p. 92). Ibn Sa'd says only that he "came before the Prophet", with no place named, and that the Prophet "covered him with a Yamanite sheet and ordered him to stay with Bilal" (IS1 pp. 343–344). | G p. 607; T9 p. 58; BAL p. 92; IS1 pp. 343–344 |
| T111 | Aylah: one dinar per adult; board and lodging for passing Muslim forces (p. 55) | **Consistent** | "To pay on every adult in his land one dinar per annum making it 300 dinars in all … provide with board and lodging whomsoever of the Moslems may pass by them" (BAL p. 92; IS1 p. 344: "three hundred dinars per annum … three hundred persons"). | BAL p. 92; IS1 p. 344 |
| T112 | Tabalah: converted, status quo kept, collected one dinar per person from People of the Book (Qureshi 184) (p. 55) | **Unverified** | Not located in the texts opened. | — |
| T113–T116 / D25 / C128–130 | "In the **tenth** year of the hijrah, the **Christian** kings of Himyar notified the Prophet … they had rejected polytheism … and accepted Islam"; letter to the kings of Himyar (Ibn Ishaq 643–644): poll tax one dinar; zakat scale; messengers led by Mu'adh b. Jabal (pp. 55–56) | Letter text **Consistent**. Year **Inconsistent/Disputed**. "Christian" **unsupported** | Ibn Ishaq: "**On his return from Tabuk** a messenger brought a letter from the kings of Himyar with their acceptance of Islam"; the letter says "Your messenger reached me on my return from the land of the Byzantines". Zakat and poll-tax terms and the five messengers are as quoted (G pp. 642–644). Al-Tabari puts the Himyar letter under **year 9** (T9 pp. 73–75). Neither source calls the kings Christian; al-Tabari's text speaks of "their abandonment of polytheism" and mentions Jews and Christians only as third parties (T9 pp. 73–75). They report "abandonment of polytheism" (G p. 643), and the letter addresses Jews and Christians as third parties. | G pp. 642–644; T9 pp. 73–75 |
| T117–T118 / C133 | 10 AH, Yemeni delegation of "fifteen to twenty" led by Surad b. 'Abd Allah; siege of Jurash about a month; feigned withdrawal; only combatants killed; others levied one dinar a year as *jizyah* (Qureshi 175) (p. 56) | Date and siege **Consistent**. Size **Minor difference**. *Jizyah* outcome **Inconsistent** | Al-Tabari: "In this year [10 AH], the deputation of al-Azd headed by Surad b. 'Abdallah came, and they were ten odd" (T9 p. 88). Ibn Sa'd: "about thirteen to nineteen" (IS1 pp. 397–398). Siege "for about a month … withdrew as far as … Shakar … killed a large number of them" (G p. 642; IS1 p. 398). Outcome: "The deputation of Jurash came to the apostle and **accepted Islam** and he gave them a special reserve" (G p. 642; IS1 p. 398: "embraced Islam"). No *jizyah* is mentioned. | T9 p. 88; IS1 pp. 397–398; G p. 642 |
| T119–T120 / D28 / C135–136 | 10 AH: "complete submission of the Christians of Najran"; after the Banu al-Harith submitted, covenant/letter to 'Amr b. Hazm (Ibn Ishaq 647–648), including "for every **one** camel, two sheep; and for every twenty camels, four sheep" (pp. 57–58) | Date **Consistent**. "Christians of Najran" **Minor difference**. Camel rate **Inconsistent** (misquotation) | Khalid was sent "in the month of Rabi'u'l-Akhir or Jumada'l-Ula in the year 10 to the B. al-Harith b. Ka'b in Najran"; "the men accepted Islam" (G pp. 645–646). Ibn Ishaq speaks of the Banu al-Harith's Islam, not of "Christians". Guillaume's text of the letter reads "for every **ten** camels two sheep; and for every twenty camels four sheep" (G p. 647). The book's "one camel" is a transcription error, and it explains the "inconsistency" with the Himyar letter that the extraction flagged (§7 item 6). Other clauses ("the greater hajj … the lesser hajj is the 'umra", prayer times, ban on appeals "to tribes and families", "a golden dinar or its equivalent in clothes") are **Consistent** (G pp. 647–648). | G pp. 645–648 |
| C181–C182 | Qur'an 5:1 and "[7:44]" in the 'Amr b. Hazm letter (p. 57) | 5:1 **Consistent**; 7:44 **Minor difference** | The Arabic of the letter has «ألا لعنة الله على الظالمين», which is the wording of **11:18**. The English matches Pickthall 7:44 (Part A). | QA (Part A) |
| C132 / C20 (Mu'adh) | Instructions to Mu'adh (Bukhari; Malik) (p. 56) | **Minor difference** | "Make things easy" was said to Mu'adh **and Abu Musa** (Bukhari 3038, 4341). "You are going to People of the Book …" is Consistent (Bukhari 1458, 4347). "Make your character good …" is a separate chainless Muwatta report, graded *da'if* (Part A). | Part A |
| D27 | Document on *sadaqah* "in the possession of Imam Muhammad al-Baqir" (Waqidi 531) (p. 56) | **Unverified** | Al-Waqidi not available. | — |

### 1F. Qur'an citations and hadith elsewhere in the section (from Part A, re-checked for consistency)

| # | Book claim (page) | Verdict | What the source says | Source URLs |
|---|---|---|---|---|
| C171–172 | 3:19 and 5:3 (*al-Islam*) (p. 33) | **Consistent** (text). The linguistic argument against Donner is **Opinion** | The definite article is present. Translators differ (Pickthall 3:19: "the Surrender"). | QA 3:19, 5:3 |
| C176–178 | 2:256; 10:99; 49:13 (p. 44) | **Consistent** | Saheeh Intl / Yusuf Ali wording. | QA |
| C179 | 3:64 in the Heraclius and Muqawqis letters (pp. 47–48) | **Consistent** (verse) | — | QA |
| C183 | 29:46 (p. 59) | **Consistent**; the ellipsis drops a qualifier | The omitted words: "except in a way that is best, except for those who commit injustice among them". | QA |
| C184 | 5:48 (p. 59) | **Consistent** | Pickthall. | QA |
| C185 / C158 | 49:14 applied to the Sinai Bedouin (p. 62) | Verse **Consistent**; application **Opinion** | Al-Wahidi: revealed about Banu Asad Bedouin in Medina. | altafsir.com (Part A) |
| C186 | 3:113–115 epigraph (p. 64) | **Consistent** | Yusuf Ali. | QA |
| C12 / C187 | Fatimah theft, "rhetorical question" (p. 33) | **Minor difference** | Bukhari 3475, 6788: a sworn statement, "By Allah, if Fatima … stole, I would cut off her hand". | hadith-api (Part A) |
| C38 / C188 | Jesus "would break the crosses" (p. 34) | **Consistent** | Bukhari 2222, 3448. | hadith-api (Part A) |

### 1G. Ancient, Byzantine, post-prophetic, medieval, Ottoman and modern items (Part B)

These rows were checked by the Part B helper under the same rules. Its full table is `verify/_partB_later_history.md`, with every URL opened. The rows below are condensed. I spot-checked three of them against the texts themselves, and each matched the helper's quotation: al-Baladhuri on 'Umar II and St John's church (BAL pp. 191–192: "When 'Umar ibn-'Abd-al-'Aziz became caliph … 'Shall we destroy our mosque …?'"), Butler's "12 December, 639 A.D." for 'Amr's crossing, and the ICTJ report's "Black Saturday … between 56 and 70 civilians in East Beirut were summarily executed; the fate of 300 others who were kidnapped remains unknown".

| # | Book claim (page) | Verdict | What independent sources say | Source URLs |
|---|---|---|---|---|
| T1 / C1 | Athenian democracy (5th c. BCE): citizens were free adult males "natives of Athens **or Sparta**"; "the majority of peasants (>50% of the population)" excluded (p. 32) | Date **Consistent**; the rest **Inconsistent** | Sparta was a separate, non-democratic state. Athenian citizenship required citizen birth on both sides after 451/0 (*Ath. Pol.* 26.4, 42.1). Solon gave the poorest class (thetes) "a place in the Assembly and in the juries" (*Ath. Pol.* 7.3). "In 403, two thirds of all Athenians were still owners of land" (FHW). Peasants were citizens; women, children, slaves and metics were the excluded groups. | https://www.gutenberg.org/cache/epub/26095/pg26095.txt ; https://www.fhw.gr/chronos/05/en/politics/321assembly.html ; https://www.fhw.gr/chronos/04/en/politics/411poli_solon.html ; https://www.fhw.gr/chronos/05/en/economy/100landownership.html |
| T2 / C3 | Roman Republic 509–27 BCE; plebeians "could not rule, elect rulers or make use of land"; the assembly was "representatives of military units" (p. 32) | Dates **Consistent**; claims **Inconsistent** (true at most of the early Republic) | Smith, *Dictionary* s.v. "Plebs": plebeians were free landowners and voted in the comitia centuriata. The consulship was opened by the rogations of 367; "L. Sextius Lateranus was the first plebeian consul" (366). After the Hortensian law (287) "the distinction between patricians and plebeians now ceased". | https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Plebs.html ; https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Lex_Licinia.html |
| T3 | "Flavius Renatus Vegeitus", end of 4th c.: "If you want peace, prepare yourself for war" (p. 44) | Quote **Consistent** (paraphrase); name **Minor difference**; date **Disputed** | The manuscript has "Flavi Vegeti Renati"; *Epitoma* 3 praef.: "qui desiderat pacem, praeparet bellum". The date (383–450) is debated: Theodosius I (Barnes 1979) or Valentinian III (Seeck, Goffart). | https://www.thelatinlibrary.com/vegetius3.html ; https://en.wikipedia.org/wiki/Vegetius (lead) |
| T4 | Ghassanids "possibly" Christian in the 4th century (Goddard 15) (p. 51) | **Disputed** (hedged) | The scholarship reported via Wikipedia (Shahid 2004, Wood 2023) puts their conversion in the 6th century under al-Harith b. Jabala. No opened source supports the 4th century. | https://en.wikipedia.org/wiki/Christianity_in_pre-Islamic_Arabia (lead) |
| T5 | Harith b. Jabala made phylarch, 6th c. (p. 51) | **Consistent** | Procopius, *Wars* I.17.47: Justinian "bestowed upon him the dignity of king" (Dewing: 531; Wikipedia: 529). | https://www.gutenberg.org/cache/epub/16764/pg16764.txt |
| T6 | Mundhir b. Harith granted "King of the Arabs" by **Heraclius** (Shoup 12) (p. 51) | **Inconsistent** | Al-Mundhir (r. 569–582) "received a royal diadem from Tiberius II in 580", was arrested in 580 and exiled to Sicily in 582 (syriaca.org; König 2019). Heraclius reigned 610–641. | https://syriaca.org/johnofephesus/persons/5124 ; https://ojs.ub.uni-konstanz.de/transmed/index.php/tmh/article/download/14/134/146 |
| T9 | Najran Christians turned Nestorian "when they came within the Persian sphere in 575" (Betts 5) (p. 37) | **Disputed** | GEDSH (Van Rompay): Persians conquered South Arabia in 572; the Syriac sources show Najran as non-Chalcedonian (Miaphysite). No opened source supports a Nestorian turn. | https://gedsh.bethmardutho.org/Himyar |
| T87 / C107 | "In AD 632 … Heraclius had ordered the baptism of all Jews" (Armour 27) (p. 48) | **Consistent** (minor dating dispute) | *Encyclopaedia Judaica* (Sharf): 632 decree, "enforced only in Carthage". Maximus, *Ep.* 8: baptisms at Pentecost 632. Van der Horst 2009: the order was issued c. 630, after the recapture of Jerusalem. | https://www.encyclopedia.com/religion/encyclopedias-almanacs-transcripts-and-maps/heracliusdeg ; https://andrewjacobs.org/translations/maximos.html ; https://almuslih.org/wp-content/uploads/2024/11/Van-der-Horst-P-About-the-doctrina-Jacobi.pdf |
| T127 | Muslim forces under 'Amr entered Sinai "in 634 CE" (quoting Crone & Cook 120) (p. 58) | **Inconsistent** with the standard chronology (the *Hagarism* page itself was **Unverified**) | 'Amr crossed at al-'Arish on 12 Dec 639 (Butler 1902, p. 198; LoC Country Study). Baladhuri gives AH 19 = 640 (BAL p. 335). In 634 'Amr was fighting in southern Palestine (Dathin; BAL pp. 166–167). | https://archive.org/details/arabconquestofeg00butl ; https://countrystudies.us/egypt/15.htm ; BAL |
| T128 / C143 | Egypt fell "to an army of less than five thousand soldiers" (Karabell 28) (p. 58) | **Inconsistent** (true only of the first force) | 3,500–4,000 at the start, reinforced by about 12,000 (Butler p. 226); 8,000–12,000 by June 640 (LoC). | Butler; https://countrystudies.us/egypt/15.htm |
| T129 | "Later Arab chroniclers even claimed" that the Copts aided the Arabs (Karabell 28) (p. 58) | **Disputed** (correctly framed as a claim) | LoC: Copts were "neutral or … actively supported the Arabs". Butler calls the welcome-as-deliverers story a "time-honoured fallacy" (p. 357). | Butler; https://countrystudies.us/egypt/15.htm |
| T132 | 711 entry into Spain "at the request of the oppressed Jews" (p. 60) | Date **Consistent**; agency **Inconsistent** | The tradition names Count Julian of Ceuta and Witiza's faction (EB1911). The *Jewish Encyclopedia* says Jews helped after the landing. Simon (1983) calls Jewish collaboration in 711 "one of the most persistent myths of modern historiography". | https://en.wikisource.org/wiki/Page:EB1911_-_Volume_25.djvu/561 ; https://www.jewishencyclopedia.com/articles/1494-andalusia ; https://escholarship.org/content/qt17h688pf/qt17h688pf.pdf |
| T133 | "The overwhelming majority of the Catholic population of the Iberian Peninsula eventually embraced Islam" (p. 59) | **Disputed** / overstated | Stroumsa 2016: the figures are "very conjectural", and Bulliet's conversion curve is contested. The Christian north was never under Muslim rule. | https://journals.uco.es/mediterranea/article/download/5171/4865/5471 |
| T134–T135 / C35 | 'Abd al-Malik (r. 685–705) built the Dome of the Rock, Arabised the administration and removed the cross from coins (Foss 136) (p. 34) | **Consistent** ("symbol of Muslim superiority" is interpretation) | Dome inscription dated AH 72 (691/2) (Wikipedia, lead). The Ashmolean confirms the abolition of figural coinage; Islamic Awareness describes the modified cross-on-steps. | https://ashmolean.web.ox.ac.uk/node/179036 ; https://islamic-awareness.org/history/islam/coins/dinar3 ; https://en.wikipedia.org/wiki/Dome_of_the_Rock (lead) |
| T136 | Standing Caliph coins "issued between 694/95 and 692/697 CE" (p. 34) | **Minor difference** (garbled range) | Dinars AH 74–77 = 693–696/7 (Museum of Islamic Art, Doha; Islamic Awareness; Ashmolean specimen 696–697). Copper from about 690 (Goodwin, RNS 2018). | https://collections.qm.org.qa/objects/standing-caliph-dinar-g10517 ; https://numismatics.org.uk/2018/04/29/now-available-the-standing-caliph-coinage/ |
| C40 | The Standing Caliph coins "were the last to depict a human image" (p. 34) | **Inconsistent** as a general statement | True of Umayyad imperial coinage after the AH 77 reform. Later Islamic figural coins exist, e.g. Artuqid copper dirhams with a seated ruler (Harvard Art Museums 57040) and with busts (LACMA 116623). | https://harvardartmuseums.org/collections/object/57040 ; https://collections.lacma.org/object/116623 |
| C36, C39 | Coin 89A figure "said by Foss and Hoyland to be the Prophet Muhammad himself" (p. 34) | **Overstated** (Foss); **Unverified** (Hoyland) | The book's own Foss quotation is a question ("Could this be the image of the Prophet himself?") about coin 89c, not 89A. Hoyland, *History Compass* 5/2 (2007) 581–602, is closed access (CR: DOI 10.1111/j.1478-0542.2007.00395.x). Museums identify the figure as the caliph (Doha; Ashmolean: "represents the Umayyad caliph, 'Abd al-Malik"). | https://ashmolean.web.ox.ac.uk/node/179036 ; https://collections.qm.org.qa/objects/standing-caliph-dinar-g10517 |
| C37–C38 | The reverse is a "broken cross" (author's conclusion) (p. 34) | **Opinion** | Ashmolean: "a standard on steps". Islamic Awareness: a cross-on-steps with the transverse bar removed. | as above |
| T137 | Walid I (r. 705–715) confiscated a church; "his successor" ordered it returned "even if it entailed the destruction of the mosque" (Haya 5) (p. 62) | Reign **Consistent**; story **Inconsistent** in detail | Baladhuri: it was **'Umar II** (r. 717–720), not Walid's successor Sulayman, who ordered the added part returned. The Damascenes objected, and the Christians accepted the churches of al-Ghutah in exchange. St John's was never returned (BAL pp. 191–192). | BAL pp. 191–192 ; https://ora.ox.ac.uk/objects/uuid:427a98b0-73f4-4079-900f-f40599b3e013/files/m6a9774dd739b45636853c54812de1496 (Sahner 2017) |
| T138 | Yazid II (r. 720–724) "persecuted Christians and destroyed their icons throughout the Caliphate" (Irwin 23) (p. 62) | Reign **Consistent**; scope **Disputed / overstated** | Sahner 2017: the edict of 104/723 (Vasiliev: 721) "was probably in force for a year or less", "was not implemented widely" and was revoked by Hisham. | Sahner 2017 (URL above) |
| T145 | Saladin took Jerusalem in 1187; clemency and pilgrims' freedom of movement (Hobbs 226) (p. 61) | Date **Consistent**; clemency partial (**Minor**) | 2 Oct 1187. A ransom was required, and about 15,000 who could not pay were enslaved (Wikipedia, lead). | https://en.wikipedia.org/wiki/Siege_of_Jerusalem_(1187) (lead) |
| T146–T147 | Selim I (r. 1512–1520); Sinai under the Ottomans 1517; firman to Patriarch Joachim of Alexandria in 1517 (p. 61) | **Consistent** (the firman as Patriarchate tradition; no primary text located) | Ridaniya 22 Jan 1517 (Wikipedia, lead). OrthodoxWiki: "In 1517, the Sultan Selim I issued a Firman to Patr. Joachim". The Patriarchate site confirms the privileges under Selim without a year. | https://orthodoxwiki.org/Joachim_I_of_Alexandria ; https://www.patriarchateofalexandria.com/patriarch/joachim-i-pany-1487-1567/?lang=en |
| T190 | Joachim c. 1448–1567 (p. 61) | **Consistent** with tradition | "Born about 1448"; patriarch 1486/7–1567; "died aged 119" (the Patriarchate's traditional figure). | same |
| T149 | Affagart, *Relation de Terre Sainte* (1533–1534) (p. 61) | **Consistent** ("15349" is OCR) | Chavanon ed. 1902, title "(1533-1534)". | https://archive.org/details/relationdeterres00affauoft |
| T150–T151 | Each new sultan instructed the pasha of Egypt (Hobbs 160); the pasha renewed protections yearly (Ratliff 15) (p. 61) | **Consistent** (page **Minor**) | Ratliff, *Sinaiticus* 2008, p. **14**, citing Hobbs 160. | https://web.archive.org/web/20150213034339id_/http://www.saintcatherinefoundation.org/files/8013/2983/0724/Sinaiticus_2008-email.pdf |
| T153–T154 / C153 | Cantemir read a Turkish translation of Selim's Arabic charter at Adrianople; Tindal's English, "Given at Cairi" (Cantemir 168–169) (p. 61) | Quotation **Consistent**; context **omitted** | Tindal 1734, Pt I, Bk III, n. 50, pp. 168–169: "I read at Adrianople"; "exempted … from their annual Tribute"; "Given at Cairi, &c." ("Cairi" is Tindal's spelling). The book omits that Cantemir calls the Sinai story "fabulous", quotes from memory, calls it "Mahomet's true or forged Instrument" bought by Selim for "four thousand Gold Crowns", and reports that Köprülü Mustafa Pasha "made no scruple to charge the whole Diploma with forgery". | https://archive.org/details/dli.ministry.02708 ; https://archive.org/details/thehistoryofthegrowthanddecaydcantemir_201912 |
| T192–T193 | Cantemir 1673–1723; N. Tindal 1687–1774, vicar of Great Waltham (p. 61) | **Consistent** | DNB "Tindal, Nicholas (1687–1774)"; 1734 title page. | https://en.wikisource.org/wiki/Page:Dictionary_of_National_Biography_volume_56.djvu/411 |
| T155 | Monks lived "in symbiosis with the Bedouins" for more than 1,300 years (Soskice 116) (p. 62) | **Opinion / Unverified** | Not checked against Soskice. | — |
| T157 | UDHR 1948 (p. 35) | **Consistent** | Proclaimed 10 Dec 1948. | https://www.un.org/en/about-us/universal-declaration-of-human-rights |
| T159 | Lebanese Civil War 1975–1990 (p. 63) | **Consistent** | ICTJ 2013: "the 1975–1990 war". | https://www.ictj.org/sites/default/files/ICTJ-Report-Lebanon-Mapping-2013-EN_0.pdf |
| T160 | The Phalange "slit the throats of three hundred Muslims at road-blocks on **Black Friday** in 1975" (Dalrymple 226) (p. 63) | Name **Inconsistent**; number **Disputed** | "Black Saturday", **6 December 1975**. ICTJ: 56–70 executed and 300 kidnapped, fate unknown. Wikipedia (lead) gives 150–200 killed. The perpetrators (Kataeb) and the checkpoints are correct. Whether the slip is Dalrymple's or Morrow's was not checked. | ICTJ (above) ; https://en.wikipedia.org/wiki/Black_Saturday_(1975) (lead) |
| T161 | Tel al-Za'tar massacre "a year later" (1976) (p. 63) | **Consistent** (simplified attribution) | ICTJ: attack from 22 June 1976, led by the PNL militia, with the Kataeb joining after 27 June; the camp fell on 12 Aug 1976. | ICTJ |
| T164 / C149 | Esposito: Muslims "conquered Byzantium" and were welcomed by sects persecuted by "'official' Christianity, that is, Catholicism" (p. 60) | Quotation **Unverified**; wording imprecise (**Opinion**) | The Arabs conquered Byzantine provinces, not Byzantium itself, and the persecuting church was the imperial Chalcedonian church. | — |
| §3 | "John L. Esposito (b. 1940)" (pp. 47, 61) vs "John F. Esposito" (p. 60) | Birth year **Consistent**; "F." **Minor** (typo) | John Louis Esposito, b. 19 May 1940 (Wikipedia, lead); Open Library: "John L. Esposito". | https://en.wikipedia.org/wiki/John_Esposito (lead) ; https://openlibrary.org/search/authors.json?q=John%20L.%20Esposito |
| T156 | Shah Waliullah Dehlvi, 18th-century India (p. 58) | **Consistent** | 1703–1762 (Wikipedia, lead). | https://en.wikipedia.org/wiki/Shah_Waliullah_Dehlawi (lead) |

### 1H. Deaths and reigns used as timeline events (rows 165–195)

Only the dates that matter as events, or that clash with sources opened above, were checked in depth. The rest were checked against Wikidata (labelled) or left to the lifespan agent.

| # | Book date (page) | Verdict | What sources say | Source URLs |
|---|---|---|---|---|
| T166 | 'Abd Allah b. Sallam **d. 630 CE** (p. 36) | **Inconsistent** | Ibn Sa'd reports Ibn Salam speaking "on the day when 'Uthman was killed" (35 AH/656 CE) (ISB III p. 59). Wikidata (labelled) gives d. 663, i.e. 43 AH. | ISB III p. 59; WD Q307686 |
| T169 | Rayhana d. 631 (p. 40) | **Inconsistent (calendar)** | Died on the return from the Farewell Hajj, March 632 (see T62–T63). | ISB VIII p. 92; W |
| T184 | Muhammad al-Kalbi **737–819** (p. 40) | **Inconsistent** (father and son conflated) | Muhammad b. al-Sa'ib al-Kalbi d. Kufa **146 AH (763)** (ISB VI p. 345). 737–819 are his son Hisham's dates (WD Q716228, labelled). | ISB VI p. 345; WD Q716228 |
| T182 | Ibn Ishaq **704–761/770** (pp. 37–40) | **Minor difference / Disputed** | Guillaume: "born in Medina about A.H. 85" (≈704) and "died in 150 (or perhaps 151)" (≈767–768) (G Introduction, pp. xiii–xiv). Wikidata (labelled): 704–768. The "761/770" endpoints are not supported by Guillaume. | G pp. xiii–xiv; WD Q334847 |
| T187 | Ibn Hisham d. 833 (p. 41) | **Consistent / Disputed** | "Died at Fustat in Egypt in 218 or 213" AH = 833 or 828 (G Introduction, p. xli). Wikidata (labelled): 828. | G p. xli; WD Q461096 |
| T183 | al-Waqidi 748–822 (p. 41) | **Minor difference** | Wikidata (labelled): 747–823 (130–207 AH). | WD Q285255 |
| T167 | Mukhayriq killed at Uhud | **Consistent** | G p. 241. | G |
| T168 | Hawdhah died "shortly after" | **Consistent** | Died after the Prophet's return from the conquest of Mecca, 8 AH (IS1 p. 309). | IS1 p. 309 |
| T170 / T126 | Prophet 570–632 | **Consistent** (death) | Died "8 June 632" (W pp. 79–80). The birth year is traditional (c. 570) and was not checked. | W pp. 79–80 |
| T171 | 'Umar 579–644 | Death **Consistent**; birth **not checked** | "Stabbed on Wednesday 26 Dhu al-Hijja 23 AH" (= Nov 644) (ISB III p. 284). | ISB III p. 284 |
| T172 | Khalid b. al-Walid 592–642 | Death **Consistent**; birth differs | Wikidata (labelled): 586–642. | WD Q26918 |
| T173 | 'Abd al-Rahman b. 'Awf d. 652 | **Consistent** | "Died in 32 AH when he was seventy-five" (ISB III p. 102). 32 AH = 652/3. | ISB III p. 102 |
| T174 | 'Ali d. 661 / r. 656–661 | **Consistent** | "Died on Saturday night 20 Ramadan 40 AH" (= Jan 661) (ISB III p. 25). | ISB III p. 25 |
| T165 | Salman d. 654 | **Disputed** | Wikidata (labelled): d. 657. Traditional death years range from 33 to 36 AH. Left to the lifespan agent. | WD Q557378 |
| T175, T177 | 'Amr b. al-'As d. 664; Abu Hurayra 603–681 | **Not checked here** (Wikidata label search failed; left to the lifespan agent) | — | — |
| T176 | Qays 'Abd al-Rashid 575–661 | **Opinion/legend** | Wikidata describes him as a "legendary founding father of the Pashtun people" and gives these same dates (labelled); legendary dates are not historical evidence. | WD Q7265861 |
| T178–T179 | Muhammad b. Abi Bakr 631–658; Malik al-Ashtar d. 658 | **Consistent** (Wikidata, labelled) | 631–658; d. 658. | WD Q1112754, Q1108678 |
| T180 | Heraclius r. 610–641 | **Consistent** | Wikidata (labelled): "Byzantine emperor from 610 to 641". | WD Q41852 |
| T181 | 'Abd al-Malik r. 685–705, "fifth Umayyad caliph" | **Consistent** | Wikidata (labelled): "Umayyad caliph from 685 to 705". | WD Q36788 |
| T185–T186 | Zayn al-'Abidin d. 712; al-Baqir 676–733 | **Minor difference** | Wikidata (labelled): d. 713; 677–733. | WD Q314978, Q311153 |
| T188–T195 | Saladin 1138–1193; Selim I r. 1512–1520; Joachim c. 1448–1567; Affagart d. c. 1557; Cantemir 1673–1723; Tindal 1687–1774; Walid I r. 705–715; Yazid II r. 720–724 | → Part B (block 1G) | Wikidata (labelled): Saladin 1138–1193; Cantemir 1673–1723; Walid I d. 715; Yazid II d. 724. | WD Q8581, Q159933, Q284003, Q314791 |

---

## 2. Timeline comparison: events where the sources give different dates

"Muslim tradition" means the early Arabic sources as opened: Ibn Ishaq (Guillaume), Ibn Sa'd (al-Waqidi's school), al-Tabari and al-Baladhuri. "Modern" means Watt, Kister, Lecker and Hamidullah, plus the Part B sources. A dash means no date was found in that source.

| Event | Book (page) | Ibn Ishaq / al-Tabari | Ibn Sa'd (al-Waqidi school) / al-Baladhuri | Modern historians | Comment |
|---|---|---|---|---|---|
| Constitution of Medina | undated, "early Medina" (p. 32) | Placed at the start of the Medinan period, undated (G pp. 231–233) | — | Watt: composite; core soon after the Hijra (622), present form possibly after Qurayza (627) (W pp. 227–228). Hamidullah: part 1 in 1 AH, Jewish part after Badr, 2 AH (HAM). Lecker: first year after the Hijra, 622 (LEC2) | The dating is genuinely open; the book takes no position. |
| Badr | 624 (p. 39) | 17 Ramadan 2 AH | Same | Watt: 13, 15 or 17 March 624 (W pp. 10–11) | Agreement. |
| Qaynuqa' siege and exile | after Badr, 624; siege 14–15 days (p. 39) | "Between Badr and Uhud", no duration (G p. 363) | Mid-Shawwal 2 AH (≈ Apr 624), 15 days; went to Adhri'at (IS2 pp. 32–33) | Watt: after Badr, 15 days, Wadi'l-Qura then 'Adhra'at (W p. 209). Barakat Ahmad: **no expulsion** in the Prophet's lifetime (BA). Al-Kalbi (per Schöller, unopened): no Qaynuqa' episode | The book's date fits the tradition. The revisionist alternatives are as the book reports, except for its summary of Ahmad. |
| Banu al-Nadir exile | 625 (p. 39) | A.H. 4, after Uhud (G p. 437) | Rabi' I, 37th month = Rabi' I 4 AH (IS2 p. 68). Baladhuri: year 4; al-Zuhri "six months after Uhud" (BAL pp. 34–35) | Watt: late Aug/early Sept 625 (W pp. 34, 210–211). Barakat Ahmad accepts the banishment (BA) | Agreement on 625. |
| Poisoning attempt on the Prophet | before the 625 exile (p. 39) | After the conquest of **Khaybar**, 7 AH (G p. 516) | — | — | **Book anachronistic.** |
| Trench and Qurayza | 627; siege 25 days (p. 40) | Trench "Shawwal, A.H. 5" (G p. 450); Qurayza besieged 25 nights (G p. 461) | — | Watt: the siege of Medina began 31 Mar 627 (8/xi/5) (W p. 36). Kister: Qurayza April 627 / Dhu'l-Qa'da 5 AH (KIS p. 61) | Agreement on 627. Watt's month differs from Ibn Ishaq's (Dhu'l-Qa'da vs Shawwal). |
| Number executed (Qurayza) | "seven hundred", doubted (p. 41) | 600–700, "some put the figure as high as 800 or 900" (G p. 464; T8 p. 35) | Ibn Sa'd: 600–700 (per KIS) | Kister collects 400 to 900 (KIS pp. 62, 89–90). Barakat Ahmad: leaders only, ≤16–17 (BA). Arafat 1976: denial (per KIS) | Disputed. |
| Rayhana's death | 631, "one year before his death" (p. 40) | — | "until she died on his return from the Hajj of Farewell" (ISB VIII p. 92) | Farewell Pilgrimage March 632; Prophet d. 8 June 632 (W pp. 79–80) | **Book: 631. Sources imply spring 632.** |
| 'Abd al-Rahman b. 'Awf to Dumat al-Jandal | undated; motive taken from the 5 AH raid (pp. 51–52) | Dumat raid by the Prophet, A.H. 5 (G p. 449) | Prophet's ghazwa: Rabi' I 5 AH (IS2 p. 76). 'Abd al-Rahman: Sha'ban 6 AH (IS2 p. 110) | — | The book merges two expeditions. |
| Letters to the rulers (Negus, Heraclius, Chosroes, Muqawqis, Ghassan, Yamamah) | Heraclius "probably 627"; Ghassan "around 628" (pp. 47, 51) | "Between al-Hudaybiyah and his death" (per W p. 346) | Six envoys "in Muharram, 7 H. (May, A.C. 628)" (IS1 pp. 304–305). Bukhari 7: Heraclius at Jerusalem during the Hudaybiya truce | Watt: Dihya's mission to Bostra "must have been in the summer of 627"; the Muqawqis's slave-girls were in Medina soon after Jan 627 (W p. 345). Watt places the Holy Rood in Jerusalem in March 630 (W p. 114) | The book's 627 for Heraclius follows Watt's revision, not the Muslim sources. |
| Chosroes' death (after tearing the letter) | "new Persian Emperor" (p. 48) | Shirawayh killed his father after the letter (G pp. 658–659) | 10 Jumada I 7 AH (translator: 13 Sept 628) (IS1 p. 307) | Watt: Khosrow II assassinated **Feb 628**, before the May 628 dispatch (W p. 114) | The traditional chronology is internally strained. |
| Chronicle of Seert: start of the Arab conquests | "5 AH" (627/28) (p. 45) | — | — | Chronicle: 18th year of Heraclius, the year of Ardashir son of Shiroi; Scher: 627/8, Ardashir after Sept 628 (PO13 p. 600) | 5 AH = 626/7, so the book's conversion is off by about a year. |
| Oman letter | undated (p. 50) | — | Dhu'l-Qa'da 8 AH (IS1 p. 309) | Watt: the envoys to 'Uman, al-Bahrayn and the Yemen "were known not to have been sent until after Hunayn" (W p. 347) | — |
| Bahrayn letter | undated (p. 49) | — | After al-Ji'irrana, end of 8 AH (IS1 p. 310). Baladhuri: "beginning of the year 8" (BAL p. 120) | Watt: after Hunayn (W p. 347) | Minor disagreement within the tradition. |
| 'Abd al-Qays deputation | 8 AH / 630; 14 men led by al-Jarud (p. 53) | Al-Jarud among the deputations of 9–10 AH (G pp. 635–636) | Year of the Conquest (8 AH); 20 men led by al-Ashajj, al-Jarud among them (IS1 pp. 370–371) | — | Disputed; "led by al-Jarud" is unsupported. |
| Ukaydir captured | "several years" after 6 AH (p. 52) | During Tabuk, 9 AH (G pp. 607–608; T9 pp. 58–59) | Rajab 9 AH (IS2 p. 205) | — | Consistent. |
| Treaties of Ayla, Maqna, Adhruh, Jarba' | "approximately the same period" as 8 AH (p. 53); Maqna 9 AH (p. 53) | At Tabuk, 9 AH (G p. 607; T9 p. 58) | Maqna document "written by 'Ali … in the year 9" (BAL p. 94) | — | The book's 8 AH framing is off by a year. |
| Yuhanna of Ayla's visit | came "to Medina" (p. 54) | At **Tabuk** (G p. 607; T9 p. 58) | Baladhuri: "During his stay at Tabuk" (BAL p. 92). Ibn Sa'd: no place given (IS1 p. 343) | — | Book inconsistent on the place. |
| Himyar kings' letter | "tenth year" (p. 55) | "On his return from Tabuk" (G p. 642). Al-Tabari: under **year 9** (T9 p. 73) | — | — | Book: 10 AH. Sources: late 9 AH. |
| Surad and the siege of Jurash | 10 AH (p. 56) | Al-Tabari: year 10 (T9 p. 88) | Undated (IS1 pp. 397–398) | — | Consistent. |
| Banu al-Harith of Najran submit; 'Amr b. Hazm letter | 10 AH (p. 57) | Rabi' II or Jumada I, 10 AH (G p. 645) | — | — | Consistent. |
| Treaty of Saint Catherine | 6 AH / 628 (p. 45) | — | — | not checked here (see §5) | — |
| 'Amr's march into Sinai and Egypt | 634 (p. 58) | — | Baladhuri: AH 19 = 640 (BAL p. 335, Part B) | Butler: 12 Dec 639; LoC: Dec 639 (Part B) | **Book inconsistent.** |
| Heraclius's forced-baptism decree | 632 (p. 48) | — | — | EJ: 632 (enforced at Carthage); van der Horst: 630 (Part B) | Minor. |
| Al-Mundhir crowned "King of the Arabs" | by Heraclius (p. 51) | — | — | Tiberius II, 580 (syriaca.org; König 2019) (Part B) | **Book inconsistent.** |
| Standing Caliph coinage | "694/95 and 692/697" (p. 34) | — | — | AH 74–77 = 693–696/7 (Doha, Ashmolean, Islamic Awareness); copper c. 690 (Goodwin) (Part B) | Garbled range in the book. |
| Yazid II's iconoclastic edict | (reign 720–724) (p. 62) | — | — | Vasiliev: 721; Sahner: 723 (Part B) | — |
| "Black Friday" | 1975 (p. 63) | — | — | Black **Saturday**, 6 Dec 1975 (ICTJ) (Part B) | Name wrong. |
| Deaths: 'Abd Allah b. Sallam | 630 (p. 36) | — | Alive at 'Uthman's murder, 656 (ISB III p. 59) | Wikidata: 663 | **Book inconsistent.** |
| Deaths: Muhammad al-Kalbi | 737–819 (p. 40) | — | d. 146 AH / 763 (ISB VI p. 345) | 737–819 = Hisham b. al-Kalbi (WD Q716228) | **Father and son conflated.** |
| Ibn Ishaq | 704–761/770 (pp. 37–40) | b. c. 85 AH (704), d. 150/151 (767/8) (G pp. xiii–xiv) | — | Wikidata: 704–768 | Minor. |

---

## 3. Discrepancies ranked by significance (most serious first)

"Significance" means how much the error affects the book's argument in this section, not only how large the factual gap is.

1. **Barakat Ahmad misrepresented (p. 41).** The book: "As far as Ahmad is concerned, no Jews were executed or expelled from Medina during Muhammad's life." Ahmad (1979) in fact accepts the banishment of the Banu al-Nadir ("Surat al-Hashr … deals with the banishment of the B. al-Nadir from Medina") and the execution of Qurayza leaders, whose number would "not … exceed sixteen, or seventeen". He denies only the Qaynuqa' expulsion during the Prophet's lifetime (BA). This matters because the book uses revisionist scholarship to weaken the Qurayza tradition.
2. **Anachronism in the case against the Banu al-Nadir (p. 39).** The "poisoned mouthful" happened at Khaybar in 7 AH, after the conquest. The poisoner was Zaynab d. al-Harith (G p. 516). The 4 AH Nadir plot in every source opened is a rock to be dropped (G p. 437; IS2 pp. 68–69; BAL p. 34). The error inflates the justification offered for the exile.
3. **The Constitution of Medina is misdescribed in several particulars (pp. 32–35):**
   - The conflict it ended was Aws vs Khazraj, ending at Bu'ath, with Jewish clans on both sides (W pp. 157–158; G p. 253), not "Khazraj and their Jewish rivals".
   - It **keeps** retaliation alongside blood-money (G p. 232); blood-money does not "replace the lex talionis".
   - It imposes explicit war-cost and mutual-defence obligations on the Jews (G pp. 232–233), so it is not "rights without obligations".
   - It does not mention Christians.
   - Leading scholars hold that the three main Jewish tribes were **not** parties (W p. 227; Lecker, LEC1), and Lecker reads the Jews' status as *amana* (security), not *umma* (LEC1).

   These points undercut the book's central claim of a pluralist "one and indivisible" citizenry.
4. **The Qurayza arbiter is presented as "a judge appointed by the Jewish people … [who] ruled on the basis of the Torah" (p. 40).** In Ibn Ishaq the Aws interceded and the Prophet proposed Sa'd b. Mu'adh, a Muslim of the Aws, whom the parties accepted. The verdict is called "the judgement of Allah" (G pp. 463–464; T8 p. 35; Bukhari 3043; KIS p. 62). The Deuteronomy/Torah reading is Hamidullah's modern interpretation (*Muslim Conduct of State* §497, quoted in KIS p. 64 n. 3). The book states it as fact.
5. **An interpolated clause inside a quotation (p. 52).** "Fight everyone in the way of Allah **[who attacked you or betrayed you]** …", cited to Ibn Ishaq 672. Guillaume p. 672 has no such qualification: "fight everyone in the way of God and kill those who disbelieve in God". The square brackets mark an editorial addition, but it reverses the scope of the command and is not flagged as the author's.
6. **Campaign statistics are unsourced or contradicted (pp. 42–43).** "30" led and "61" sent do not match Ibn Ishaq (27 and 38; al-Tabari 26 and 35) or Ibn Sa'd (27 and 47) (G pp. 659–660; IS2 p. 2), and the lists contain duplicates. "No more than 89 days in battle" and "approximately one thousand casualties" have no source. The traditional Qurayza figures alone (400–900) would make up most of the casualty total (KIS).
7. **The early conquests (pp. 58–61):**
   - 'Amr entered Sinai in Dec 639/640, not "634" (Butler; BAL; Part B).
   - Egypt did not fall to "less than five thousand"; reinforcements took the army to about 12,000–15,500 (Part B).
   - The 711 invasion of Spain was not "at the request of the oppressed Jews": the received tradition names Count Julian and Witiza's faction, and Simon (1983) calls Jewish collaboration a "persistent myth".
   - "Overwhelming majority of the Catholic population … embraced Islam" is a contested estimate.
8. **The Prophet's letters (pp. 45–51):**
   - The Muqawqis parchment is in **Topkapı**, Istanbul (TOP), not "a library in Egypt".
   - Hawdhah of Yamamah was **not** "an ally". Ibn Sa'd has the Prophet say "may he perish!" (IS1 p. 309).
   - Al-Harith of Ghassan was not conquered. Caesar restrained him, and he died in 8 AH (IS1 pp. 307–308).
   - Heraclius did not "conquer the cities of Lakhm and Judham". These were Arab tribes allied to Byzantium (BAL p. 92).
   - Al-Bahrayn was the eastern Arabian mainland (Hajar), mostly Arab, not a Persian "island nation" (IS1 pp. 310–311; BAL p. 120; W pp. 131–132).
   - The 627 date for the Heraclius letter is a scholarly minority dating (Watt), not "traditional" (see §2).
9. **Treaties and deputations (pp. 52–56):**
   - Yuhanna of Ayla met the Prophet at **Tabuk**, not Medina (G p. 607; T9 p. 58; BAL p. 92).
   - The Himyar letter dates to late **9 AH**, after Tabuk, not the "tenth year" (G p. 642; T9 p. 73), and the sources do not call the kings Christian.
   - Jurash **converted**; no *jizyah* is recorded (G p. 642; IS1 p. 398).
   - Ukaydir was of Kinda, not "the successor of al-Asbagh" of Kalb (G p. 607; IS2 p. 205). Whether he converted or paid *jizyah* is disputed between the narrative (*jizyah*: Ibn Ishaq, Ibn Sa'd) and the document text (conversion: al-Waqidi, Baladhuri).
   - The 'Abd al-Qays deputation was led by al-Ashajj, not al-Jarud (IS1 pp. 370–371).
10. **Al-Mundhir b. al-Harith was crowned by Tiberius II in 580, not Heraclius (p. 51)** (Part B: syriaca.org; König 2019).
11. **Person dates that collide with events:**
    - 'Abd Allah b. Sallam "d. 630" (p. 36): he was alive at 'Uthman's murder in 656 (ISB III p. 59); Wikidata gives 663.
    - "Muhammad al-Kalbi (737–819)" (p. 40): these are his son Hisham's dates. Muhammad b. al-Sa'ib al-Kalbi died in 146 AH/763 (ISB VI p. 345).
    - Rayhana "d. 631 … one year before his death" (p. 40): she died on the return from the Farewell Hajj, spring 632 (ISB VIII p. 92; W pp. 79–80).
12. **The Chronicle of Seert is given a hijri date it does not contain (p. 45).** The Chronicle's own dating, "the 18th year of Heraclius / the year of Ardashir son of Shiroi", equals 627/8–628. The book's "5 AH" (626/7) is a conversion error (PO13 p. 600).
13. **Comparative-politics claims are inaccurate (p. 32).** Athenian citizenship never included "natives of … Sparta". Poor Athenian farmers (thetes) were citizens. Roman plebeians voted, owned land and from 367/366 BCE could hold the consulship (Part B).
14. **Coins (p. 34).** The issue dates are garbled. "The last to depict a human image" is false for Islamic coinage in general; Artuqid figural coins exist. "Said by Foss and Hoyland to be the Prophet" overstates Foss, whom the book quotes only as asking a question about a different coin (89c); Hoyland was not accessible (Part B).
15. **Umayyad and modern items (pp. 62–63).** The church restitution story concerns 'Umar II, not Walid's successor, and the church was never returned (BAL pp. 191–192). Yazid II's edict was short-lived and patchily applied (Sahner 2017). "Black Friday 1975" was Black **Saturday**, 6 Dec 1975, and the "300 killed" is disputed: ICTJ gives 56–70 executed and 300 missing.
16. **A misquotation of the 'Amr b. Hazm letter (p. 57).** "For every **one** camel, two sheep" should read "for every **ten** camels two sheep" (G p. 647). This removes the apparent clash with the Himyar letter noted in the extraction (§7 item 6).
17. **Selective quotation of Cantemir (p. 61).** The Tindal text is accurately quoted. But Cantemir calls the Sinai story "fabulous", speaks of "Mahomet's true or forged Instrument", and reports Köprülü Mustafa Pasha's charge of forgery. The book omits all of this (Part B).
18. **Minor items:**
    - "Defa" for Adhri'at/Der'a (p. 39); "Junayfir" for Jayfar (p. 50); "al-Khami" for al-Lakhmi (p. 48); "John F." for John L. Esposito (p. 60); "Flavius Renatus Vegeitus" (p. 44).
    - "A decade" of Meccan persecution: Ibn Ishaq says 13 years (p. 44).
    - "Five hundred miles" to Dumat: the straight line is about 370 miles, and Ibn Sa'd gives 15–16 days' journey (p. 51).
    - Ratliff p. 14, not p. 15 (p. 61).
    - Salman's price in Guillaume is 40 okes of gold and the nugget the size of a hen's egg, not 1,600 silver coins and a pigeon's egg (p. 36).
    - The Fatimah hadith is an oath, not a "rhetorical question" (p. 33).
    - The Abyssinians hadith drops its Turks clause (p. 47).
    - The Chosroes curse is in H. G. Wells's wording (p. 49).
    - The Mu'adh instructions were addressed to Mu'adh and Abu Musa jointly (p. 56).
    - The "[7:44]" in the 'Amr b. Hazm letter matches the Arabic of 11:18 better (p. 57) (Part A).

---

## 4. Assessment of the author's main arguments in this section

### 4.1 "The Constitution of Medina created a tolerant, pluralistic state of Muslims, Jews, Christians and pagans, 'one and indivisible regardless of religion'" (pp. 32–35)

**For the author.**
- The document is widely accepted as authentic and early. Watt uses it "as a source for the ideas underlying the Islamic state in the early formative years" (W p. 228). Lecker calls it "probably the first legal document of Muhammad" from the first year after the Hijra (LEC2).
- It does include Jewish groups among "the people of this document". It guarantees "the Jews have their religion and the Muslims have theirs" (G p. 233). It binds both sides to mutual defence (G p. 233).
- Watt takes "the people of this document" to cover "both Jews and Muslims" (W p. 228).
- Hamidullah presents it as "the first written constitution in the world" (HAM).
- Donner, whom the author attacks, also reads the early community as confessionally mixed (Bouali's review: "L'hétérogénéité confessionnelle est … un … trait saillant du mouvement des Croyants"; https://journals.openedition.org/assr/25460). On this point Morrow and Donner agree more than the book admits.

**Against or qualifying.**
- The text is organised by Arab clans, each paying blood-money "according to their present custom". It keeps retaliation and refers disputes to "God and … Muhammad" (G pp. 232–233). Tribe remains the organising unit, against the book's "no longer … tribe, kinship".
- It never mentions Christians. "Pagans" appear only as parties restricted from protecting Quraysh (G p. 232).
- On the most-cited clause, Lecker argues that the Jews received *amana* (security), not *umma* status, and that "most of Medina's Jewish tribes, including the large ones, did not join the document" (LEC1). Watt reaches a similar conclusion on the three main tribes and thinks the extant text may postdate Qurayza (W p. 227). If so, the document cannot show that the Qaynuqa', Nadir and Qurayza were full members of a pluralist polity that they then betrayed. This is a tension in the book's own narrative (pp. 39–40).
- The comparison with Athens and Rome rests on factual errors about both (Part B).
- **Balance:** "pluralist" and "tolerant" are defensible as descriptions of a confederal security pact with religious autonomy for the Jewish parties. "One and indivisible regardless of religion", "rights without obligations" and the inclusion of Christians are not supported by the text.

### 4.2 Rejection of Donner's "Believers" thesis (pp. 33–34)

**Donner's thesis (as summarised in reviews).** The early movement of "Believers" (*mu'minun*) was ecumenical and admitted pious Jews and Christians. *Muslim* became a confessional label later. The decisive shift came under 'Abd al-Malik (685–705): "Khalifat Allah", anti-Trinitarian inscriptions on the Dome of the Rock, and a sharper prophetology (Bouali, *ASSR* 164, 2013). Schubel calls the ecumenical claim "more controversial" than Donner's religious reading of Muhammad (https://www.ajis.org/index.php/ajiss/article/view/1244).

**Morrow's counter-arguments, assessed.**
1. *Definite al-Islam in 3:19 and 5:3.* The definite article is there (Part A). But translators render it both as a proper name and as "the Surrender" (Pickthall). The grammar alone does not settle whether a 7th-century speaker meant a confessional boundary. **Opinion.**
2. *The Prophet's surviving letters "in museums" use "Islam" and "Muslims".* This is the weakest plank. The physical letters in Topkapı exist (TOP), but their authenticity is disputed (Wikipedia lead citing Bolshakov; https://en.wikipedia.org/wiki/Al-Muqawqis). Watt, who accepts most of Ibn Sa'd's treaty material, judges that the six-envoys story "cannot be accepted as it stands" and was reshaped "because of the theological interest" (W pp. 345–346). Letters transmitted in 9th-century compilations cannot by themselves serve as 7th-century proof against a thesis that dates confessional vocabulary to the later 7th century.
3. *Morrow concedes a hardening under 'Abd al-Malik* (Dome, Arabisation, coin reform; p. 34). Part B confirms these facts. This concession comes close to Donner's own chronology of a turning point.
4. *Crone and Cook.* The *Hagarism* p. 120 statement could not be checked (Part B).

**Balance:** The book's rejection is argued from theology and from contested documents rather than from the epigraphic and papyrological evidence that Donner's debate turns on. The reviews opened show the thesis is debated, not refuted.

### 4.3 The Jewish tribes: mercy in exile, doubt about the Qurayza executions, Ibn Hisham as the source of polemic (pp. 39–42)

- The traditional sequence and details are reported accurately in most places (Ibn Ishaq, Ibn Sa'd; §1C), apart from the anachronistic "poisoned mouthful" and the "Torah judge".
- **On historicity**, the scholarship is split. Arafat (1976) and Barakat Ahmad (1979) argued for denial or minimisation. Kister (1986) rebutted Arafat at length, showing that early jurists (al-Shafi'i, Abu 'Ubayd, al-Mawardi) treated the episode as legal precedent and that its reports come through several independent chains (KIS pp. 63–69). Watt and the Western biographers Kister lists accepted it, often with moral criticism (KIS p. 63 n. 2).
- The book's "increasingly, the evidence suggests that we cannot [believe it]" is not borne out by the sources opened. It is a **minority revisionist position**, and the book misstates what Ahmad himself concluded (§3 item 1).
- **The Ibn Hisham hypothesis** is undermined by al-Tabari's independent Salama recension of Ibn Ishaq, which carries the same numbers (T8 p. 35), and by the parallel transmission in Abu 'Ubayd (KIS p. 69) and Bukhari 3043.
- The appeal to 7th-century norms (Armstrong; p. 41) is a moral argument, not a factual one. **Opinion.**

### 4.4 "The Prophet used the threat of force rather than violence; Arabia was unified at about 1,000 casualties" (pp. 42–44)

- The sources support the view that most expeditions involved little fighting. Ibn Ishaq and Ibn Sa'd both say he fought in only 9 of 27 campaigns (G p. 660; IS2 p. 2).
- The **numbers** the book adds (30/61 expeditions, 89 days, about 1,000 casualties) have no source and do not match the classical totals (§1D).
- The book's quotation of Ibn Ishaq 672 adds a defensive qualifier that is not in the source (§3 item 5).
- **Balance:** the qualitative claim is arguable; the quantitative claims are unsupported.

### 4.5 "A consistent policy: convert, or ally and pay tax; no compulsion" (pp. 44–57)

- Broadly **supported by the treaty texts** that survive in the early compilations: Ayla, Adhruh, Maqna and Jarba' (IS1 pp. 327–345; BAL pp. 92–94). The Himyar and 'Amr b. Hazm letters both state that a Jew or Christian "who holds fast to his religion … is not to be turned from it", subject to a dinar's poll tax (G pp. 643, 648).
- **Qualifications:**
  - Several cases the book cites as alliances were not. Hawdhah was refused and cursed; al-Harith of Ghassan stayed hostile.
  - Jurash's outcome was conversion, not *jizyah*.
  - The Ukaydir sources disagree on conversion versus *jizyah*.
  - The early treaties survive only in later compilations. Watt regards the Ibn Sa'd treaty material as broadly authentic (W p. 345), but individual documents vary in reliability.

### 4.6 Christian and Jewish welcome for the conquests; Ottoman protection of Sinai (pp. 58–62)

- The Coptic welcome is a contested tradition: the Library of Congress country study accepts it, while Butler calls it a "fallacy".
- The Jewish role in 711 is a "persistent myth" according to Simon (1983).
- Mass Iberian conversion is a conjectural estimate (Stroumsa 2016).
- The Ottoman documents and the yearly renewals by the pasha are attested (Ratliff p. 14; Cantemir/Tindal).
- The book omits that its own Ottoman witness, Cantemir, called the Prophet's Sinai charter possibly forged (Part B). That omission bears directly on the book's larger project, which is the authenticity of the covenants.

---

## 5. Items not checked, and why

| Item (page) | Reason |
|---|---|
| Donner's own pages (58, 71, 73, 194–224) | *Muhammad and the Believers* not accessible: the HUP page returned no content and JSTOR requires a login. The thesis was taken from two reviews. |
| Schöller's chapter (al-Kalbi; Scholler 26–30, 38–39) | Identified via Crossref (Brill 2000, pp. 18–48), but brill.com returned HTTP 403. The attribution is unverified; only al-Kalbi's dates were checked. |
| Al-Waqidi, *Kitab al-Maghazi* (Faizer tr.): pp. 89, 91, 247, 348, 505, 531 | No open full text found; covered indirectly through Ibn Sa'd, who transmits al-Waqidi. |
| Qureshi's treaty and letter texts (pp. 34–41, 117–18, 153–288) and Hamidullah, *Muslim Conduct of State* (pp. 157, 629–30) | Not opened. Treaty contents were checked against Ibn Sa'd, Ibn Ishaq and Baladhuri instead. |
| Treaty of Saint Catherine "6 AH", scribe "Mughirah" (p. 45) | Left to the Sinai-covenant verification; no critical edition opened here. |
| 62 letters / 29 texts (Zeitlin; Dar Rah Haqq) (p. 34) | Not opened. |
| Tabala (p. 55); "Letter to the Jews" (p. 53); Tabuk message to Heraclius (p. 47); Ubayy b. Ka'b as scribe of the Oman letter (p. 50); 700 men with 'Abd al-Rahman (p. 51); Ukaydir's tribute clause (p. 52); Safiyya's age 17 (p. 40); the 14-member 'Abd al-Qays version (p. 53) | Not found in the texts opened, and web-search budget exhausted. |
| "89 days in battle"; "1,000 casualties" (p. 43) | No source found; the book gives none. |
| Persia conquered "within ten short years" (p. 49) | Not assigned to either part; not checked. |
| Quoted modern authors: Peters 201, Armstrong 2000, Mattson 149, O'Shea 15, Nafziger & Walton, Karabell, Fletcher, Emhardt & Lamsa, Wigram, Binns/Michael the Syrian, Cahen, Hobbs 226, Galey, Tomadakis, Mouton, Champdor, Soskice, Irwin, Haya, Shboul, Jordac/Zaydan (Imam 'Ali's letters), Zayn al-'Abidin's *Risalat al-huquq*, al-Rikabi, Khomeini 42, Mamdani 172, Dalrymple 226, Bangash, Khan 1, Esposito 71/82/83 | These are attributions or opinions. The quotation accuracy of these modern works was not checked (most are not openly available). Where a quotation contains a checkable fact (Black Saturday, Sinai 634, Spain 711, Mundhir), the fact was checked. |
| *Hagarism* p. 120; Hoyland 2007 | Closed access or unauthorised copies only (Part B). |
| Death dates of 'Amr b. al-'As and Abu Hurayra; 'Umar's birth year; Salman d. 654 | Wikidata label search failed or sources vary; left to the lifespan agent. |
| A substantive scholarly critique of Donner (e.g. a full review by Crone) | Web-search budget was exhausted, and Tablet and Wiley pages returned 403. |

**Access limits.** Britannica returned HTTP 403 to both WebFetch and curl. Sunnah.com sat behind a Cloudflare challenge, so hadith were read from the hadith-api mirror. Brill, Wiley, Iranica, UNESCO, the Met and Archnet were blocked or rate-limited. The session's shared web-search budget ran out in the last phase, so later items were checked only by fetching known URLs and full texts already downloaded. No verdict rests on a search snippet.

---

## 6. Sources (every URL opened)

### 6.1 Opened directly for this part (main thread)

Full texts (archive.org; downloaded and read at the cited pages):
- https://archive.org/details/GuillaumeATheLifeOfMuhammad — text: https://archive.org/download/GuillaumeATheLifeOfMuhammad/Guillaume%2C%20A%20-%20The%20Life%20of%20Muhammad_djvu.txt
- https://archive.org/details/muhammadatmedina029655mbp — text: https://archive.org/download/muhammadatmedina029655mbp/muhammadatmedina029655mbp_djvu.txt
- https://archive.org/details/kitab-al-tabaqat-al-kabir-ibn-sad-s.-moinul-haq-h.-k.-ghazanfar-1 (vol. I text)
- https://archive.org/details/kitab-al-tabaqat-al-kabir-ibn-sad-s.-moinul-haq-h.-k.-ghazanfar-2 (vol. II text)
- https://archive.org/details/kitab-at-tabaqat-al-kabir (Bewley vols I, II, III, VI, VIII texts)
- https://archive.org/details/the-history-of-al-tabari (Tabari_Volume_07/08/09 djvu texts)
- https://archive.org/details/originsofislamic01albauoft (Hitti, Baladhuri I)
- https://archive.org/details/1975-the-first-written-constitution-in-the-world (Hamidullah)
- https://archive.org/details/patrologiaorient13pariuoft and https://archive.org/details/patrologiaorien13pari (PO 13, Chronicle of Seert)
- archive.org metadata and advanced-search API calls used to locate the above (https://archive.org/advancedsearch.php?… ; https://archive.org/metadata/…/files)

Articles, books and pages:
- http://web.archive.org/web/20250118072808/http://www.kister.huji.ac.il/sites/default/files/banu_qurayza.pdf (Kister 1986), located via https://archive.org/wayback/available?url=kister.huji.ac.il/sites/default/files/banu_qurayza.pdf
- https://almuslih.org/wp-content/uploads/Library/Barakat,%20A%20-%20Muhammad%20and%20the%20Jews.pdf (Barakat Ahmad 1979)
- https://cris.huji.ac.il/en/publications/the-constitution-of-medina-muhammads-first-legal-document-2/ (Lecker abstract)
- https://www.theportobellobookshop.com/9783959941242 (Lecker 2024, publisher's description)
- https://istanbultarihi.ist/assets/uploads/pdf/istanbuldaki-mukaddes-emanetler-182.pdf (Küçükaşçı, Topkapı relics)
- https://en.wikipedia.org/wiki/Al-Muqawqis (lead only)
- https://journals.openedition.org/assr/25460 (Bouali, review of Donner)
- https://www.ajis.org/index.php/ajiss/article/view/1244 (Schubel, review of Donner)
- https://cdn.jsdelivr.net/gh/fawazahmed0/hadith-api@1/editions/eng-bukhari/7.json ; https://cdn.jsdelivr.net/gh/fawazahmed0/hadith-api@1/editions/eng-bukhari/3043.json
- Crossref API (via skill): https://api.crossref.org/works/10.1163/9789004452909_005 (Schöller 2000) and searches for Hoyland 2007 (10.1111/j.1478-0542.2007.00395.x), El-Cheikh 1999 (10.2307/1596083), and Donner reviews (10.35632/ajis.v28i3.1244; 10.4000/assr.25460; 10.1093/jaarel/lfr024)
- Wikidata (labelled): https://www.wikidata.org/w/api.php (wbsearchentities); https://query.wikidata.org/sparql (dates for Q557378, Q307686, Q26918, Q1647771, Q7265861, Q1112754, Q1108678, Q41852, Q36788, Q285255, Q314978, Q311153, Q461096, Q284003, Q314791, Q334847, Q716228, Q8581, Q159933, Q494660); https://www.wikidata.org/wiki/Special:EntityData/Q35484.json, …/Q27125.json, …/Q3766.json, …/Q2719371.json, …/Q238217.json, …/Q24343.json (coordinates); https://www.wikidata.org/wiki/Q716228
- https://en.wikipedia.org/api/rest_v1/page/summary/Hisham_ibn_al-Kalbi (lead only)

Attempted and failed (no verdict rests on these): https://brill.com/view/book/edcoll/9789004452909/B9789004452909_s005.xml (403); https://www.hup.harvard.edu/books/9780674064140 (empty); https://www.tabletmag.com/sections/news/articles/among-the-believers (403); https://www.britannica.com/biography/Hisham-ibn-al-Kalbi (403); https://www.britannica.com/place/Bahrain/History (blocked stub); https://www.islamic-awareness.org/history/islam/letters/muqawqis (404); https://readings.com.au/product/9783959941242/… (403); https://kister.huji.ac.il/sites/default/files/banu_qurayza.pdf (HTML error page; archived copy used).

Texts already in the scratchpad from earlier agents that were re-read here: `scratchpad/po13/po13.txt` (identical to the PO 13 archive.org text above, confirmed by byte comparison) and `scratchpad/ratliff/s.txt` (Ratliff, *Sinaiticus* 2008; Part B opened the public URL).

### 6.2 Opened by the Part A helper (Qur'an and hadith), copied from `verify/_partA_quran_hadith.md`

**quran.com API**
- https://api.quran.com/api/v4/resources/translations
- https://api.quran.com/api/v4/resources/tafsirs
- https://api.quran.com/api/v4/verses/by_key/{key}?translations=20,22,19&fields=text_uthmani for each key: 3:19, 5:3, 28:52, 28:53, 28:54, 28:55, 46:10, 3:12, 3:13, 2:256, 10:99, 49:13, 3:64, 9:29, 5:1, 7:44, 11:18, 29:46, 5:48, 49:14, 3:113, 3:114, 3:115
- https://api.quran.com/api/v4/quran/verses/imlaei (full text, searched for لعنة الله على)
- https://api.quran.com/api/v4/tafsirs/169/by_ayah/46:10
- https://api.quran.com/api/v4/tafsirs/169/by_ayah/28:52
- https://api.quran.com/api/v4/tafsirs/169/by_ayah/3:12
- https://api.quran.com/api/v4/tafsirs/169/by_ayah/49:14
- https://api.quran.com/api/v4/tafsirs/169/by_ayah/9:29
- https://api.quran.com/api/v4/tafsirs/14/by_ayah/28:52
- https://api.quran.com/api/v4/tafsirs/14/by_ayah/28:53
- https://api.quran.com/api/v4/tafsirs/14/by_ayah/28:54
- https://api.quran.com/api/v4/tafsirs/14/by_ayah/28:55

**altafsir.com (al-Wahidi, Asbab al-Nuzul, tr. Guezzou)**
- https://www.altafsir.com/Tafasir.asp?tMadhNo=0&tTafsirNo=86&tSoraNo=3&tAyahNo=12&tDisplay=yes&UserProfile=0&LanguageId=2
- https://www.altafsir.com/Tafasir.asp?tMadhNo=0&tTafsirNo=86&tSoraNo=49&tAyahNo=14&tDisplay=yes&UserProfile=0&LanguageId=2
- https://www.altafsir.com/Tafasir.asp?tMadhNo=0&tTafsirNo=86&tSoraNo=28&tAyahNo=52&tDisplay=yes&UserProfile=0&LanguageId=2 (no Wahidi entry)
- https://www.altafsir.com/Tafasir.asp?tMadhNo=0&tTafsirNo=86&tSoraNo=46&tAyahNo=10&tDisplay=yes&UserProfile=0&LanguageId=2 (no Wahidi entry)

**Hadith (hadith-api dataset; base https://cdn.jsdelivr.net/gh/fawazahmed0/hadith-api@1/editions/)**
- eng-bukhari/3475.json, eng-bukhari/6788.json, ara-bukhari/3475.json
- https://raw.githubusercontent.com/fawazahmed0/hadith-api/1/editions/eng-bukhari/2222.json ; eng-bukhari/3448.json
- eng-abudawud/4302.json, ara-abudawud/4302.json, eng-nasai/3176.json, ara-nasai/3176.json
- eng-bukhari/64.json, ara-bukhari/64.json, eng-bukhari/2939.json, eng-bukhari/4424.json
- eng-bukhari/3038.json, ara-bukhari/3038.json, eng-bukhari/4341.json, eng-bukhari/4344.json, eng-bukhari/6124.json
- eng-bukhari/1458.json, eng-bukhari/1496.json, eng-bukhari/4347.json
- eng-malik.min.json, ara-malik/1633.json
- eng-tirmidhi/2485.json, ara-tirmidhi/2485.json, eng-ibnmajah/1334.json, eng-ibnmajah/3251.json
- eng-bukhari/3812.json, ara-bukhari/3812.json
- eng-abudawud/3001.json
- eng-muslim.min.json, ara-muslim/4521.json

**Other**
- https://sunnah.com/bukhari:3475 (curl: Cloudflare challenge; WebFetch: HTTP 403)
- https://sunnah.com/abudawud:4302 (WebFetch: HTTP 403)
- https://shamela.ws/book/305/80 (Ibn Taymiyya, *al-Siyasa al-sharʿiyya*, ed. ʿAtaʾat al-ʿIlm, p. 22, with editor's footnote)
- https://ar.wikisource.org/wiki/البداية_والنهاية/الجزء_الرابع/بعثه_إلى_كسرى_ملك_الفرس
- https://outline-of-history.mindvessel.net/300-seven-centuries-in-asia/304-first-message-from-islam.html
- https://hadithunlocked.com/suyuti/47/106 (Suyuti, *Jamʿ al-jawamiʿ* §492-5b, letter to ʿAmr b. Hazm, Arabic)
- https://seerah.gtaf.org/books/1/chapters/29/a-deputation-to-abyssinia-ethiopia/

### 6.3 Opened by the Part B helper (background and later history), copied from `verify/_partB_later_history.md`

Ancient background
- https://www.fhw.gr/chronos/05/en/politics/321assembly.html
- https://www.fhw.gr/chronos/04/en/politics/411poli_solon.html
- https://www.fhw.gr/chronos/05/en/economy/100landownership.html
- https://www.gutenberg.org/cache/epub/26095/pg26095.txt (Aristotle, *Athenian Constitution*, trans. Kenyon)
- https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Lex_Licinia.html
- https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Plebs.html
- https://en.wikipedia.org/wiki/Roman_Republic (labelled lead)
- https://www.thelatinlibrary.com/vegetius3.html
- https://en.wikipedia.org/wiki/Vegetius (lead)
- https://api.crossref.org/works?query.bibliographic=The+Date+of+Vegetius+Barnes+Phoenix ; https://api.crossref.org/works/10.14264/106601

Ghassanids / Najran
- https://en.wikipedia.org/wiki/Ghassanids (lead)
- https://en.wikipedia.org/wiki/Christianity_in_pre-Islamic_Arabia (lead)
- https://syriaca.org/johnofephesus/persons/5124
- https://ojs.ub.uni-konstanz.de/transmed/index.php/tmh/article/download/14/134/146 (König 2019)
- https://www.gutenberg.org/cache/epub/16764/pg16764.txt (Procopius, *Wars* I–II, trans. Dewing)
- https://gedsh.bethmardutho.org/Himyar

Heraclius
- https://www.encyclopedia.com/religion/encyclopedias-almanacs-transcripts-and-maps/heracliusdeg
- https://www.jewishvirtuallibrary.org/heraclius
- https://andrewjacobs.org/translations/doctrina.html
- https://andrewjacobs.org/translations/maximos.html
- https://almuslih.org/wp-content/uploads/2024/11/Van-der-Horst-P-About-the-doctrina-Jacobi.pdf
- (opened but not relevant: https://www.jewishencyclopedia.com/articles/7591-heraclius, an article on heretics)

Egypt / Spain / Iberia
- https://archive.org/download/arabconquestofeg00butl/arabconquestofeg00butl_djvu.txt (Butler 1902)
- https://countrystudies.us/egypt/15.htm
- https://archive.org/download/originsofislamic01albauoft/originsofislamic01albauoft_djvu.txt (Hitti, *Origins of the Islamic State* I, 1916; I downloaded the archive.org copy myself and checked it against scratchpad/hitti/hitti1.txt)
- https://www.jewishencyclopedia.com/articles/1494-andalusia
- https://escholarship.org/content/qt17h688pf/qt17h688pf.pdf (Simon 1983)
- https://en.wikisource.org/wiki/Page:EB1911_-_Volume_25.djvu/561
- https://journals.uco.es/mediterranea/article/download/5171/4865/5471 (Stroumsa 2016)
- (opened, not used: https://discovery.ucl.ac.uk/10167594/1/04%2BFenwick%2BFinal%2Bonline%2Bversion%2BMarch%2B22%2B2023.pdf; https://ddd.uab.cat/pub/medievalia/medievalia_a1982n3/medievalia_a1982n3p168.pdf, a scanned image with no text)

'Abd al-Malik / coins
- https://en.wikipedia.org/wiki/Abd_al-Malik_ibn_Marwan (lead)
- https://en.wikipedia.org/wiki/Dome_of_the_Rock (lead)
- https://collections.qm.org.qa/objects/standing-caliph-dinar-g10517
- https://numismatics.org.uk/2018/04/29/now-available-the-standing-caliph-coinage/
- https://ashmolean.web.ox.ac.uk/node/179036
- https://islamic-awareness.org/history/islam/coins/dinar3
- https://harvardartmuseums.org/collections/object/57040
- https://collections.lacma.org/object/116623
- https://api.crossref.org/works?query.bibliographic=Hoyland+Writing+the+biography+of+the+Prophet+Muhammad+problems+and+solutions+History+Compass
- https://api.openalex.org/works/doi:10.1111/j.1478-0542.2007.00395.x
- https://www.cambridge.org/core/services/aop-cambridge-core/content/view/S1047759400004244
- https://research.ucc.ie/en/publications/the-7th-c-islamic-coinages-of-syria-and-egypt-in-their-historical/
- https://api.openalex.org/works/W2275606035

Umayyads (Walid I, Yazid II)
- https://ora.ox.ac.uk/objects/uuid:427a98b0-73f4-4079-900f-f40599b3e013/files/m6a9774dd739b45636853c54812de1496 (Sahner 2017)
- https://api.crossref.org/works?query.bibliographic=Vasiliev+The+Iconoclastic+Edict+of+the+Caliph+Yazid+II+A.D.+721
- Hitti (above), pp. 191–192

Saladin / Ottomans / Sinai
- https://en.wikipedia.org/wiki/Siege_of_Jerusalem_(1187) (lead)
- https://en.wikipedia.org/wiki/Selim_I (lead)
- https://www.patriarchateofalexandria.com/patriarch/joachim-i-pany-1487-1567/?lang=en
- https://orthodoxwiki.org/Joachim_I_of_Alexandria
- https://archive.org/metadata/dli.ministry.02708 and its part-4 djvu text (Tindal 1734, pp. 168–169), via https://archive.org/details/dli.ministry.02708
- https://archive.org/download/thehistoryofthegrowthanddecaydcantemir_201912/The_History_of_the_Growth_and_Decay_D_Cantemir_djvu.txt (1734–35 edition)
- https://archive.org/download/bim_eighteenth-century_the-history-of-the-growt_dimitrie-cantemir-voivo_1756/bim_eighteenth-century_the-history-of-the-growt_dimitrie-cantemir-voivo_1756_djvu.txt (1756 edition; OCR poor)
- https://en.wikipedia.org/wiki/Dimitrie_Cantemir (lead)
- https://en.wikisource.org/wiki/Page:Dictionary_of_National_Biography_volume_56.djvu/411
- https://archive.org/download/relationdeterres00affauoft/relationdeterres00affauoft_djvu.txt (Affagart, ed. Chavanon 1902)
- https://web.archive.org/web/20150213034339id_/http://www.saintcatherinefoundation.org/files/8013/2983/0724/Sinaiticus_2008-email.pdf (Ratliff 2008)

Modern
- https://www.un.org/en/about-us/universal-declaration-of-human-rights
- https://www.ictj.org/sites/default/files/ICTJ-Report-Lebanon-Mapping-2013-EN_0.pdf
- https://en.wikipedia.org/wiki/Black_Saturday_(1975) (lead)
- https://en.wikipedia.org/wiki/John_Esposito (lead)
- https://openlibrary.org/search/authors.json?q=John%20L.%20Esposito
- https://en.wikipedia.org/wiki/Shah_Waliullah_Dehlawi (lead)

Attempted but failed (no verdict rests on these): britannica.com (Vegetius, plebeian, Licinian-Sextian laws: 403); iranicaonline.org/articles/ghassanids (403/Cloudflare); compass.onlinelibrary.wiley.com Hoyland 2007 (403); academia.edu/3303289 (403); stoa.org Demos (refused); whc.unesco.org/en/list/954 (403); metmuseum.org essays (429); archnet.org (429); al-qantara.revistas.csic.es (TLS); gedsh.bethmardutho.org/Najran (403); dev.gedsh (TLS); espace.library.uq.edu.au (403); smarthistory.org (403); acmcu.georgetown.edu (404); id.loc.gov (403); sciencespo.fr mass-violence page (404).
