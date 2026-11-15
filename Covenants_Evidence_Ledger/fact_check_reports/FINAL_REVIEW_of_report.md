# Review of "Book Analysis Report: Timeline, Facts & Cross-Source Verification"

**Under review:** `scratchpad/report_export.md`, the report on J. A. Morrow, *The Covenants of the Prophet Muhammad with the Christians of the World* (2013).

**What the report was tested against:**
- the extraction files `Covenants_Evidence_Ledger/book_extraction/` (00–09);
- the book's OCR text `scratchpad/book/chunks/*.txt` (every book quotation below was re-read there);
- the fact-check reports `Covenants_Evidence_Ledger/fact_check_reports/` (V0–V7c, AUDIT_A, AUDIT_B, QA_extraction_checks).

No web sources were used.

**Conventions:**
- Page numbers are the book's printed pages.
- "Vx row Y" means the verdict row with that ID in that fact-check report.
- Every item gives the exact report text, the problem, the evidence, and the replacement wording.

**Overall judgement.** The report's core findings hold up against the evidence files, including the witness anachronisms, the 1517 Baghdad story, the 1630 date, the 975 decree, and the Thenaud and Burckhardt readings. But four kinds of fault would not survive a careful reader with the book open:
- A few statements put words in the book's mouth (items 1–2) or treat quotations as the author's own claims (item 21).
- The headline numbers and the "confirmed by audit" claims cannot be reproduced as written (items 7–8).
- Several "contradictions" and "not found" verdicts are overstated (items 9–12).
- The report repeatedly leaves out concessions the book itself makes, and the strongest evidence in the book's favour that the fact-check files contain (items 3, 13–20, 26–28).

Most fixes are small. Items 1–12 should be fixed before the report is shared.

---

## A. Statements that misrepresent the book (fix first)

### 1. The book never calls Hamidullah's reprint a "milestone"

**Report text:**
- Errors #6, "The book says" cell: "Hamidullah's 1956 reprint of the Najran text is a milestone in its recognition".
- Covenant-by-covenant, Najran row: "Hamidullah, whose 1956 reprint the book cites as a milestone, calls the Seert texts fabrications".

**Problem:**
- The word "milestone" is not in the book's discussion of Hamidullah. In the OCR it appears only twice: on p. 114, inside a quotation from Qureshi about the Treaty of Najran recorded in the Muslim sources, and on p. 65.
- What p. 138 actually says: "Although it was reprinted in 1956 in Muhammad Hamidullah's Majmuah al-watha'iq ... and in 2002 in Muhammad 'Amarah's al-Islam wa al-akhar, the work has not reached the wide audience that it merits."
- The real fault, as V3 row 4.58 frames it, is an omission: the book cites the reprint without saying that Hamidullah printed the texts as forgeries.
- V3 row 4.58 also says Hamidullah's verdict was read in his 5th edition, not the 1956 printing.
- Neither audit checked this item.

**Evidence:** OCR 04_ch3_ch4.txt lines 3873–3886 (p. 138); V3 row 4.58; V3 headline findings.

**Replace #6 with:**
- Book says: "The book cites Hamidullah's 1956 reprint of the Najran text (pp. xviii, 138), regretting only that the covenant 'has not reached the wide audience that it merits'".
- Sources show: "Hamidullah includes the Seert texts as a specimen of forgery and writes that 'there is not the slightest doubt' they are fabrications (5th edition). The book does not mention this."

**Replace the Najran-row sentence with:** "Hamidullah, whose reprint of the text the book cites without mentioning his verdict (p. 138), calls the Seert texts fabrications."

### 2. Errors #8 attributes to Arpee an argument the author makes in his own voice

**Report text:** "| 8 | Arpee's Persia covenant has no motive for forgery (quoting Arpee) | The quotation cuts Arpee's own aside "(though by modern criticism pronounced a forgery)" | p. 99 |"

**Problem:**
- On p. 99 the book quotes Arpee: the Persian text "reproduces a charter, purporting to be ... originally granted by Mohammed ... to the Monastery of St. Catherine". The ellipsis cuts the forgery aside. That quotation says nothing about motive.
- The motive argument is on pp. 102–103, in Morrow's own voice, and it is a different claim: that Arpee himself had no motive or means to forge the text.
- Arpee's aside refers to the underlying Sinai charter, not the Persian document.
- V3 rates this item "Minor difference (a substantive omission)". It was never audited.

**Evidence:** OCR 04_ch3_ch4.txt lines 1–12 (p. 99); 04_ch3_ch4.md §5 item 6 and the "Arguments for" row ("Arpee was a serious historian with no motive ... (p. 103)"); V3 row C3-7.

**Replace with:** "| 8 | Quoting Arpee, the Persia text 'reproduces a charter, purporting to be ... originally granted by Mohammed ... to the Monastery of St. Catherine' | The first ellipsis removes Arpee's aside that this Sinai charter was '(though by modern criticism pronounced a forgery)' (Arpee p. 355) | p. 99 |"

**Same fix in the Persia row of the covenant-by-covenant table.**
- Current: "The book's quotation of Arpee omits his remark that modern criticism called it 'a forgery'"
- Replace: "The book's quotation of Arpee (p. 99) cuts his aside that the Sinai charter the Persian text reproduces was '(though by modern criticism pronounced a forgery)'."

---

## B. Headline framing, chart and numbers

### 3. The lead paragraph overstates three points and gives nothing on the book's side

**Report text:** "No original survives, and each text first appears in dated evidence 250 to 1,300 years after the date it claims. Of about 1,550 checks against outside sources, 860 found the book consistent and 203 found it contradicted; the errors cluster in the evidence for authenticity. Most specialists treat the long covenant texts as later compositions, while a small group of scholars has defended them since 2016."

**Problems:**
- **(a) "No original survives."** The files support only "no original is known to survive" or "has been found" (V2a §4: "lost or missing"; V6a §4.4: "Even its defenders concede"). The book argues the Sinai original may lie in Topkapı (pp. 65, 69). It treats the St James Armenian scroll as possibly "the original" (p. 200: "Whether the copy ... is the original Prophet's oath, a copy thereof ... is immaterial"). That scroll has never been published or examined.
- **(b) "each text first appears in dated evidence".** This is not what the chart measures; see item 4. For Sinai (1512) and Armenians (1187) the dates are reports of a document, not appearances of the text. Najran's 878 is the text's own account of its discovery.
- **(c) "the errors cluster in the evidence for authenticity".** No fact-check file says this, and nothing counts it. In the report's own error tables, 14 of 101 items are in the "authenticity case" table, and dozens concern Chapter 15 history and life dates. V7a–c alone hold about 45 "Inconsistent" rows on life dates, and V6b about 30 on Chapter 15. The defensible claim is about importance, not distribution, and the Errors section already makes it ("The errors that matter most concern ...").
- **(d) Balance.** The lead gives only negatives. The fact-check's own neutral assessments name points for the book:
  - early Muslim sources preserve a real Najran treaty;
  - the prophetic-covenant genre is real;
  - Sinai's monks invoked a prophetic letter of protection before the Ottoman conquest.
  - Evidence: V6a §4.2 and §4.4; V0 §3.6; AUDIT_B B12, B13.
- **(e) "since 2016"** leaves out Morrow (2013), the author of the book under review. V0 §3.6 says "a small, active, mostly peer-reviewed group defending it since 2016".
- **(f) The counts** cannot be reproduced; see item 7.

**Replace the paragraph with** (keep the numbers only after the recount in item 7):

> John Andrew Morrow's book argues that six covenants protecting Christians were issued by the Prophet Muhammad. No original is known to survive, and the earliest dated evidence for each covenant (a copy, a printing, or a report of such a document) comes 250 to 1,300 years after the date it claims. Of 1,551 verdicts reached against outside sources, 860 found the book consistent and 203 found it contradicted, by other sources or by its own pages. The most consequential errors concern the evidence for authenticity: the witness lists, the dating of the documents and how sources are quoted. The fact-check also confirms points in the book's favour. Early Muslim sources record a real, shorter treaty with Najran, and the monks of Sinai were invoking a prophetic letter of protection before the Ottoman conquest of 1517. Most specialists whose verdicts could be opened treat the long covenant texts as later compositions. A small group of scholars, including Morrow, has defended them, in peer-reviewed venues since 2016.

### 4. The chart compares unlike evidence, and on the Assyrian bar this counts against the book

**Report text:**
- Line 221: "No original of any covenant survives, and each text first appears in dated evidence centuries after the date it claims."
- Line 225: "The gap is shortest for the Najran text, which by its own story was found in 878–79, and longest for the Persian and Assyrian texts."
- Chart data: Najran 631→878, Armenians 626→1187, Sinai 623→1512, World 625→1538, Persia 625→1881, Assyrian 625→1910.

**Problem.** The bars measure three different things:

| Covenant | Chart date | What that date actually is |
|---|---|---|
| Sinai | 1512 | Thenaud's report that the privilege was kept in the monastery mosque. The earliest dated copy of the text is 957 AH / 1550–51 (Moritz). The Mamluk decree of Qansuh al-Ghawri citing "letters of protection of the Prophet" is dated 911 or 921 AH (1505 or 1515), so it may be earlier than 1512 (V2a §2b, row E4; AUDIT_B B13). |
| Armenians | 1187 | Saladin's charter, which *refers to* pacts of the Prophet, 'Umar and 'Ali (V5 row T78, §4.2). The Armenian text itself is unpublished and undated. |
| Najran | 878 | The text's own account of its discovery. The witness that carries that account is a chronicle of the 10th–11th century (V6a §4.3 point 4; V3 §4B). |
| World | 1538 | A manuscript of a different recension: no date, scribe 'Ali. |
| Persia | 1881 | First printing. |
| Assyrian | 1910 | First printing. |

**The Assyrian bar breaks the rule used for Sinai and the Armenians.**
- The report itself says "A Church of the East claim to a prophetic charter is attested from the Abbasid period" (line 233).
- V5 §4.1: Bar Hebraeus (13th c.) and Assemani report a "diploma" obtained by Isho'yahb II with Said of Najran. "This shows the claim existed from at least the Abbasid period." V4 §4 adds that Mari and 'Amr report the same charter.
- V5 §4.1 and V6a §4.2 point 3: the Malech text belongs to the World-covenant family, attested from 1538.
- Scored the way Sinai and the Armenians are scored (first report of a document), the Assyrian gap would be about 650 years at most (Bar Hebraeus, 13th c.), not 1,285. Scored by its family (1538), it would be about 910.
- As drawn, the longest bar is the product of an inconsistent rule, and that rule works against the book.
- Caveat for fairness to the critics: V5 also says these reports do "not show that Malech's text is that charter". The same is true of Saladin's charter and the Armenian scroll. Whatever rule is chosen, it must be applied to every bar.

**Replace line 221 with:** "No original of any covenant is known to survive, and for each covenant the earliest dated evidence (a copy, a printing, or a report of such a document) comes centuries after the date it claims."

**Add a note under the chart:**

> Claimed date = the date the text bears (Sinai 2 AH; World, Persia and Assyrian 4 AH). Morrow regards the 4 AH dates as later scribal additions (pp. 107, 167). The Najran text bears no date, so the book's "last year of the Prophet's life" is used. The Armenian text is unpublished, so the "626" of a tradition the book quotes is used (p. 191). The evidence points differ in kind:
> - Najran 878–79 is the text's own account of its discovery; the chronicle that carries it dates from the 10th–11th century.
> - Sinai 1512 (Thenaud) and Armenians 1187 (Saladin) are reports of a prophetic document, not copies. The earliest dated Sinai copy is 1550–51, and a Mamluk decree citing the Prophet's letters may date from 1505.
> - World 1538 is a manuscript of a different recension.
> - Persia 1881 and Assyrian 1910 are first printings. A Church of the East claim to a prophetic charter is reported much earlier (in medieval chronicles including Bar Hebraeus, 13th century), and the Assyrian text belongs to the World-covenant family attested from 1538.

**Replace line 225's sentence with:** "The gap is shortest for the Najran text, which by its own account was found in 878–79. It is longest for the Persian and Assyrian texts as printed (1881, 1910), though a Church of the East claim to such a charter is reported from the 13th century and the Assyrian text belongs to the World-covenant family attested from 1538."

### 5. Two date cells in "The six covenants" table contradict the chart and the rest of the report

**(a) Armenian.**
- Report text: "None given; placed in Patriarch Abraham I's term, given as 638–669 (p. 191)".
- Problem: the chart uses 626 as the Armenian claimed date. The book quotes "in 626" (Zeki al-Din, via the Belleville Armenian Church, p. 191) and "626/4H" and "early 630s" (Dadoyan, p. 200). Morrow himself places it "most likely in Medina, after his return" (p. 191).
- Evidence: OCR 06_ch6_ch7.txt lines 1405–1424 (p. 191); 06_ch6_ch7.md covenant profile, "Claimed date (CE)".
- Replace with: "None in a printed text. The book quotes traditions of 626 (Zeki al-Din, p. 191) and '626/4H' (Dadoyan, p. 200). Morrow places it in Patriarch Abraham I's term, given as 638–669, 'most likely in Medina' (p. 191)."

**(b) Assyrian.**
- Report text: "No year; "two years before" Mu'awiyyah's 630–632 service as scribe (p. 183)".
- Problem: the book's own printed text ends "in the 4th year of the Hegira in the city of Medina" (p. 314). The report says so itself in the covenant-by-covenant table (line 233) and in Errors #11.
- Replace with: "Printed text dated '4th year of the Hegira' (p. 314). Morrow dates it 'two years before' Mu'awiyyah's 630–632 service as scribe, i.e. about 628 (p. 183)."

### 6. "Every specialist verdict" turns a majority into unanimity; "Both sides agree" claims more than the book concedes

**Report text (line 180):** "Before 2013, every specialist verdict our agents could open treats the long covenant texts as later compositions, not 7th-century documents. Since 2016 a small group, chiefly Ahmed El-Wakil and Ibrahim Zein, has defended them in peer-reviewed venues. Both sides agree that no original survives; the dispute is over what the late copies prove."

**Problems:**
- V0 §3.6 limits the statement to the Sinai and Najran/Seert texts. It names Burckhardt, Ebers, Moritz, Scher and Hamidullah, and records Atiya (1950) as undecided.
- The report's own tables list Atiya as "Undecided" (Sinai row) and Roggema as holding a "genuine core" (Najran row).
- The World row names Salmasius, Renaudot and Hinckelmann as defenders. V4 §4 adds Twiss (1887: "haute ancienneté").
- For the Persia text the report itself found "No specialist verdict ... beyond Dadoyan's".
- Morrow does not agree that no original survives. He hopes the Sinai original "remains stored in some forgotten archive, perhaps in ... Topkapi" (p. 69), and says the Persian one "may simply have been misplaced or ... stolen" (p. 107).

**Evidence:** V0 §3.6; V2a §4; V3 §4B; V4 §4; book pp. 69, 107.

**Replace with:**

> Before 2013, the modern specialist verdicts our agents could open on the Sinai and Najran texts (Burckhardt, Ebers, Moritz, Scher, Hamidullah, Mouton) treat them as later compositions, not 7th-century documents. Atiya (1950) left the Sinai question open. Early-modern scholars were divided over the World covenant: Grotius and Prideaux rejected it, while Salmasius, Renaudot and Hinckelmann accepted it. Since 2016 a small group, chiefly Ahmed El-Wakil and Ibrahim Zein, has joined Morrow in defending the covenants in peer-reviewed journals and with an academic press. Both sides agree that no original has been found; the dispute is over what the late copies prove.

### 7. The verdict counts cannot be reproduced; two category labels misdescribe their contents; "one in eight" uses the wrong base

**Report text:**
- Line 238: "Most of the book's checkable statements hold up, but about one in eight is contradicted by reliable sources."
- The table rows, including "Sources disagree with one another | 101", "Contradicted by reliable sources | 203" and "No reliable source found | 142".
- Line 249: "Counts are verdict rows across the twelve fact-check reports, 1,551 in all".

**Problems:**
- **No file states the counting rule, and the figures do not reproduce.**
  - The scratchpad's `count_verdicts.py`, run on the current reports, gives 1,728 rows: Consistent 815, Minor 155, Disputed 99, Inconsistent 181, Unverified 128, Opinion 80. Another 270 rows are unclassified, including all 81 of V2a, whose verdicts are letter codes (C/MD/I/D/U/O).
  - Two other rules (first verdict term in a Verdict column, or bold verdicts only) gave 1,710 and 1,456 rows.
  - None gives 860 / 160 / 101 / 203 / 142 / 85 = 1,551.
- **The labels do not match the categories.**
  - The ledger classifier (`scratchpad/ledger_script.js`, lines 3–10) puts "partly / partially / mixed" verdicts in the same bin as "disputed". That bin is labelled "Sources disagree with one another", but "partly consistent" is a different finding.
  - The "unverified" bin includes "not checked", "n/a" and "no date", which is not the same as "No reliable source found".
  - The "Contradicted" bin includes rows where the book contradicts *itself* (e.g. V1a/V7 self-contradiction rows), not only outside sources.
- **"One in eight of the book's checkable statements".**
  - 203 / 1,551 = 13%, about one in 7.6, and that base includes opinions and unverified items, which are not checkable.
  - Among checkable verdicts (1,551 − 85 − 142 = 1,324), 203 is 15%, about one in 6.5.
- **"Twelve" reports** is right only if V0 is excluded, but line 388 says "Thirteen research agents".

**Replace:**
- Line 238, first sentence: "Most of the book's checkable statements hold up. About 13% of all verdict rows (203 of 1,551), or 15% once opinions and unverified items are set aside, found the book contradicted, by outside sources or by its own pages."
- Table labels:
  - "Disputed among sources, or only partly consistent | 101"
  - "Contradicted (by sources or by the book's own pages) | 203"
  - "Unverified (no source found, or not checked) | 142"
- Line 249: "Counts are verdict rows in the twelve fact-check reports that have verdict tables (V1a–V7c; V0 covers reception), 1,551 in all, classified by the first verdict word in each row; a claim checked in two reports counts twice."
- Before publishing, re-run the count with that stated rule and replace any figure that changes.

### 8. "Confirmed by the fact-check" and "re-checked by the audit" are claimed for more items than were checked

**Report text:**
- Line 238: "Each item below was confirmed by the fact-check, and the 26 most serious were re-checked by a second, independent audit."
- Line 384: "The 26 most serious findings were then re-checked by an independent audit: 23 were confirmed and 3 partly confirmed, and the corrections are reflected above."

**Problems:**
- **There were two audits, not one** (A1–A13 and B1–B13). The report's own line 389 says "Two further agents".
- **The 26 audited findings are not "the 26 most serious".** They include life dates (B10) and reviews (B11).
- **Coverage of tables 1–2.** Of the 29 items in Errors tables 1–2, these were never audited: #2, #6, #7, #8, #9, #13, #14, #25, #26, #27, #29. That includes the two worst problems in this review (items 1 and 2).
- **"Confirmed by the fact-check" is not true of every item:**
  - #42 rests on "Unverified" verdicts (V4 rows T92, T105, T128).
  - #72 contradicts V7a rows 15 and 98, which rate the book's dates "Consistent".
  - #8 and #18 are rated "Minor difference" (V3 row C3-7; V1b row T98).
- **"Corrections are reflected above"** holds for the three partial items (A5, A12, B13), but not for the caveats on A8, A9 and A13:
  - A13: the BnF has four 1630 records, and the absence of 1668 and 1888 editions is "unproven rather than disproved". See item 9.
  - B8: the ages are rounded (Watt), and Ibn Ishaq himself does not put Muhammad in the Fijar war. See item 26.
  - B6: the poisoner was the wife of a Nadir man. See item 33.

**Evidence:** AUDIT_A and AUDIT_B summary tables; V3, V1b, V4 and V7a rows as cited.

**Replace:**
- Line 238, last sentence: "Each item below is a finding of the fact-check reports. Twenty-six key findings (marked †) were re-checked from the primary sources by two independent audits."
- Mark † on #1 (Sinai part), #3, #4, #5, #10, #11, #12, #15–#24 and #28.
- Line 384: "Twenty-six key findings were then re-checked by two independent audits. 23 were confirmed (three of them with stated caveats) and 3 were partly confirmed. The corrections and caveats are reflected above." This sentence becomes true only after items 9, 26 and 33 are fixed.

---

## C. Verdicts stronger than the evidence

### 9. "Not found in any catalogue" for the 1630, 1668 and 1888 printings, filed under "Wrong dates"

**Report text:**
- Timeline (line 94): "| 1630 | "Re-published four times during the first year" | p. 151 | **Not found** in any catalogue |"
- Timeline (line 98): "| 1668, 1888 | Further editions of the World covenant | p. 151 | **Not found** in catalogues; editions of 1645, 1660, 1661 and 1683–84 are omitted |"
- Errors #42: "No catalogue shows these editions; editions of 1645, 1660, 1661 and 1683–84 go unmentioned"

**Problems:**
- V4 searched only VD17 and GVK, and rates rows T92, T105 and T128 "Unverified", not Inconsistent.
- AUDIT_A A13: the BnF holds four 1630 records. They look like duplicates, but "metadata alone cannot exclude separate issues". The absence of 1668 and 1888 is "unproven rather than disproved".
- V4 row T105: Rycaut's *Present State of the Ottoman Empire* (1668) prints an English translation of the treaty, which "the book may mean". The report's own "Other books" table lists Rycaut 1668 as printing the covenant, and the book reprints that translation as World I (p. 229). The report therefore contradicts itself.
- The book's front matter (p. xv) speaks more carefully of three 1630 printings (copies at Harvard, "if the catalog entry is correct", and Marburg). Neither was checked.
- An unverified item does not belong in a table headed "Wrong dates and facts".

**Replace:**
- Timeline (line 94): "**Unconfirmed.** VD17 and GVK list one 1630 printing; the BnF's four 1630 records look like duplicates but may be separate issues. The book's own front matter (p. xv) names three 1630 printings (Harvard, Marburg), which were not checked."
- Timeline (line 98): "No separate 1668 or 1888 edition found (VD17, GVK, BnF; title searches are not conclusive). Rycaut's *Present State* (1668) does print an English translation, which the book reprints as World I (p. 229). Printings of 1645, 1660, 1661 and 1683–84 go unmentioned."
- #42: move it out of table 3, into a short "Unconfirmed claims" list or into table 2. Wording: "The 1630 edition was 're-published four times during the first year', and again in 1668 and 1888 | Not confirmed. VD17 and GVK list one 1630 printing; the BnF's four 1630 records appear to be duplicates. No separate 1668 or 1888 edition was found, though title searches are not conclusive, and Rycaut's 1668 *Present State* prints an English translation. Printings of 1645, 1660, 1661 and 1683–84 go unmentioned | pp. xv, 151".

### 10. Three "contradictions" in table 6 are not contradictions (delete them)

**#90.**
- Report text: "| 90 | Every authority accepts 1517 for the removal of the original (p. 68) | "Some scholars still suggest" 1517 (p. 73) |"
- Problem: p. 73 reads "some scholars still suggest that the Covenant ... *dates to* 1517 CE". That is about when the text was composed, not when the original was removed (OCR 03_ch2.txt lines 849–853; 03_ch2.md §7 item 24).
- Fix: delete. The real error ("every authority") is already covered in the 1517 timeline row.

**#94.**
- Report text: "| 94 | 4 AH = 626 CE (p. 158) | 4 AH = 625 CE (pp. 159–160) |"
- Problem: the "626th year" on p. 158 is inside a block quotation from Basnage de Beauval (OCR 05_ch5.txt lines 1894–1906), and the 625 comes from Twiss. Neither is Morrow's own conversion, and 4 AH runs from June 625 to May 626, so both years are correct.
- Fix: delete.

**#100.**
- Report text: "| 100 | The monastery mosque was officially closed in 1986 (p. 20) | It was restored in 1986, on the same page (p. 20) |"
- Problem: a building can be closed and restored in the same year (for example, closed for restoration). The two statements come from different cited sources (Mouton and 'Abd al-Malik; *Arabic News*). V2b row B15 rates the closure "Unverified".
- Fix: delete. The timeline row on line 124 already records the point.

### 11. Other table-6 rows misstate one side of the pair

**#96.**
- Report text: "| 96 | The Najran covenant is the oldest (ch. 14) | The Persian covenant may predate all others (ch. 16) |"
- Problem: p. 331 calls Najran "the oldest such charter", attested in the 9th century, i.e. the oldest surviving attestation. p. 353's "perhaps ... predates all of the others" is a hedged guess about the lost original. These are two different senses of "oldest".
- Replace with: "| 96 | Najran is 'the oldest such charter', attested in the 9th century (p. 331) | The Persian covenant 'perhaps ... predates all of the others' (p. 353), a guess about the lost original |", or delete.

**#91.**
- Report text: "| 91 | The last Ottoman confirmation is 1805 (p. 70) | 1818/19 (p. 71), 1888 (p. 71) and 1904 (p. 98) |"
- Problem: p. 70 gives the Ottoman period of rule, "(1517–1805 CE)", not a last decree. The 1904 is inside a quotation from Griffith.
- Replace with: "| 91 | Ottoman decrees ran 'from 1519 to 1818/19' (p. 71) | The latest edict was issued 'in 1888' (p. 71); quoting Griffith, confirmations ran to 1904 (p. 98) |"

**#88.**
- Report text: "| 88 | The Sinai covenant dates to 7 July 623 (p. 83) | AD 626, quoting the monastery (p. 96); 1 August 622 in two printed versions (pp. 208, 210) |"
- Problem: the right-hand dates are in a quotation from the monastery and in the Arundale and Géramb texts the book reprints (V2a row A4). They are not Morrow's own statements.
- Replace with: "| 88 | The book converts the date to 7 July 623 (p. 83) | It prints, without comment, the monastery's 'AD 626' (p. 96) and two versions dated '1st of August, 622' (pp. 208, 210) |"

**#89.**
- Report text: "| 89 | The Sinai witnesses are genuine companions (pp. 82–83) |"
- Problem: on pp. 82–83 the book argues that witnesses such as Abu Hurayra *could* have been present; it does not assert that they were.
- Replace with: "| 89 | Abu Hurayra and Abu al-Darda' could really have been witnesses (pp. 82–83) | 'In all probability ... the dates, the name of the scribe, and those of the witnesses were added at a later time' (p. 85) |"

**#93**, and the Najran witness cell on line 138.
- Report text: "32 (p. 115), "over thirty" (p. 118), 30 (p. 138); the printed list has 27 entries (p. 300)"
- Problem: on p. 118, "over thirty" is a general remark that witness numbers "increased exponentially over time from a couple to over thirty" (OCR 04_ch3_ch4.txt lines 1888–1891). It is not a count for Najran. The book's 32 matches Scher's edition (31 witnesses plus the scribe; V3 row C4-39). Its own English list has 27 entries and drops three of Scher's names.
- Replace in both places with: "32 (p. 115, matching Scher's edition: 31 witnesses plus the scribe) and 30 (p. 138); the book's own printed list has 27 entries and omits three of Scher's names (p. 300)".

**#101.**
- Problem: the front matter (p. xvii) says "six", names five typed texts, then describes the 1538 copy, which a reader could count as the sixth.
- Replace with: "It names five texts; the sixth covenant discussed, the Armenian, is not printed", or delete.

### 12. #72 takes one side where the fact-check reports disagree

**Report text:** "| 72 | Ibn Ishaq | 704–761/770 | d. 767 or 768 | pp. 112, 188 |"

**Problem:**
- V7a rows 15 and 98 rate the same dates "Consistent". EI2 records death dates "as early as 144/761-2" and as late as 153/770, so "the book's range spans the attested extremes".
- V7b rates them Inconsistent but did not consult EI2.
- A user who checks EI2 will find 761.

**Fix:** delete the row. If it stays: "| 72 | Ibn Ishaq | 704–761/770 | Most sources give d. 150/767 or 151/768; EI2 records variants from 144/761–2 to 153/770, so the range is defensible but leaves out the standard date | pp. 3, 6, 7, 112, 188 |".

---

## D. The book's own concessions, and the strongest evidence for its side, left out

### 13. Errors #1 answers the book's weakest explanation and leaves out its main one

**Report text:** "| 1 | Impossible witnesses can be explained by later additions to the lists, by re-issue of the covenants, or by dictation in the Year of Delegations (630–31) | No list fits any single date in the Prophet's life. ..."

**Problem:**
- "No list fits any single date" rebuts the re-issue and Year-of-Delegations explanations. It does not rebut later addition.
- Later addition is the explanation the book itself favours:
  - p. 85: "In all probability ... both the dates, the name of the scribe, and those of the witnesses were added at a later time".
  - p. 174: the signatories were "attached posthumously".
  - p. 353: "appended ... centuries after the fact".
- That is a major concession, and the report uses it against the book in #89 while ignoring it here.
- The pages for the Year-of-Delegations (p. 327) and re-issue (p. 328) arguments are not cited.

**Evidence:** OCR pp. 85, 174, 327–328, 353; V6a §4.1 and §4.3 point 1.

**Replace the "book says" cell with:** "The impossible witnesses are explained as later additions ('in all probability ... the dates, the name of the scribe, and those of the witnesses were added at a later time', p. 85; 'appended ... centuries after the fact', p. 353), as the result of repeated re-issue (pp. 85, 328), or by a single dictation in the Year of Delegations, 630–31 (p. 327)".

**Append to the sources cell:** "Neither re-issue nor a single dictation fits these lists. The later-addition explanation, which the book itself favours, concedes that the lists, dates and scribes are not original, so the body of each text has to be dated on other evidence."

**Pages:** "pp. 85, 115, 147, 174, 205–217, 236, 300, 327–328, 353".

### 14. Errors #11 and the Assyrian row present points the book itself makes as findings against it, and overstate the specialists

**Report text:**
- #11: "The Assyrian covenant dates from about 628 and is an independent witness | Its own colophon reads "4th year of the Hegira". It calls itself a translation, and its scribe, date and witness order match the World covenant printed in 1630".
- Covenant row: "It calls itself a translation and matches the World covenant family."
- Covenant row: "Specialists (Brock, Wilmshurst, Wood, Reynolds) reject a 7th-century origin; no specialist was found defending this text".

**Problems:**
- The book itself says, on p. 178, that the document "commences with the words: 'The translation of the holy messenger's treaty'" (OCR 06_ch6_ch7.txt lines 153–160).
- On p. 177 the book allows that the Assyrians "had simply adopted the document that was originally directed to the Monastery of Saint Catherine. This remains within the realm of possibility." So "independent witness" overstates the book.
- The 4 AH colophon is printed in the book (p. 314).
- Of the four named specialists, only Reynolds addresses this text. Brock (GEDSH) and Wilmshurst reject the tradition that Isho'yahb II dealt with Muhammad. Wood addresses the related Seert Najran treaty (V5 §4.1, points 2–3).

**Replace:**
- #11, "book says": "The Assyrian covenant dates from 'two years before' Mu'awiya's 630–632 service as scribe, i.e. about 628 (p. 183). The book treats it as a separate charter, while allowing that the Assyrians may have adopted the Sinai text (p. 177)."
- #11, "sources show": "The book's own printed text ends '4th year of the Hegira' (p. 314), i.e. 625–26. Its scribe, date formula and witness order match the World covenant printed in 1630, a comparison the book does not make. (The book notes that the text opens 'The translation of the holy messenger's treaty', p. 178.)"
- Covenant row, last column: "Reynolds dates the text to the 17th century. Brock and Wilmshurst reject the tradition that Isho'yahb II dealt with Muhammad, and Wood and Scher reject the related Seert Najran treaty. No specialist was found defending this text."

### 15. Covenant-by-covenant, World row: the book's own concession is left out, and Hamza is credited to Prideaux

**Report text:**
- "Dated 4 AH; found by Scaliger c. 1627–28; BnF MS Arabe 214 (1538) is "no question" its source; reprinted many times"
- "Mu'awiya (Muslim from c. 630) as scribe and Hamza (killed 625) as a witness have been flagged as anachronisms since Prideaux (1698)"
- "The BnF record ties Arabe 214 to Vansleb's purchases in Egypt in the 1660s–70s"

**Problems:**
- The book says the scribe and date "are almost certainly Umayyad additions" (p. 167; OCR 05_ch5.txt lines 2804–2806; V4 §4).
- Prideaux flagged only Mu'awiya. The Hamza point is the fact-checkers' own inference (V0 §3.2).
- The BnF record says "Acheté par Vansleb en Orient" ("bought in the East"), not in Egypt (AUDIT_A A10).

**Replace:**
- Claims cell: "Text dated 4 AH, but Morrow calls the scribe (Mu'awiya) and the date 'almost certainly Umayyad additions' (p. 167). Found by Scaliger c. 1627–28. BnF MS Arabe 214 (1538) is 'no question' its source (p. 145), later 'to be determined' (p. 176). Reprinted many times."
- Evidence cell: "... The BnF record says Arabe 214 was 'bought in the East' by Vansleb (travels 1663–64 and 1671–73), so its link to Sionita is unproven. Prideaux (1698) objected that Mu'awiya, named as scribe in 4 AH, was then fighting the Prophet. The list also names Hamza, killed in 625. Morrow treats scribe and date as later additions."

### 16. Persia: the book's verdict is understated, its strongest claims are left out, and the 1881 find is credited only against the critic

**Report text:**
- Six-covenants table: "Open: authenticity "cannot be disproved" (p. 107)"
- Covenant row: "Dated 4 AH; known only from Arpee's 1946 English text; original missing; "cannot be disproved""
- Covenant row: "This refutes the critic Dadoyan's claim that the source does not contain it."

**Problems:**
- The book's words are "neither can it be disproved".
- The book leans towards authenticity. On p. 103 it says "we have documented evidence that it was being adhered to and emulated in the 8th century and that ... Imam Ja'far al-Sadiq has authenticated it". V3 §4A finds that the 8th-century evidence does not mention this document.
- The 1881 Ter-Hovhaneants print also corrects the *book*. Morrow says the text survives "only in English translation" (p. 99) and suggests it "may actually be included in another Armenian history" (p. 102; V3 headline finding 1).
- The report credits the find only against the critic, which is fair to the book but incomplete.
- The book's own 4 AH concession (the date was "probably included by a scribe", p. 107) belongs in the claims cell.

**Replace:**
- Six-covenants verdict cell: "Leans to authentic: 'neither can it be disproved' (p. 107); claims 8th-century adherence and Ja'far al-Sadiq's authentication (p. 103)".
- Covenant row, claims cell: "Text dated 4 AH, a date Morrow thinks a scribe added (p. 107). Survives 'only in English translation' (p. 99). Adhered to in the 8th century and authenticated by Ja'far al-Sadiq (p. 103). 'Neither can it be disproved' (p. 107)."
- Covenant row, evidence cell: "... prints an Armenian copy dated 4 AH. This refutes both Dadoyan's claim that the source does not contain it and the book's statements that the text survives only in English (p. 99) and may be in another history (p. 102). The 8th-century evidence the book cites does not mention this document. ..." Then apply item 2's fix to the Arpee sentence.

### 17. Najran row: the scholars' positions are characterised beyond what the sources support

**Report text:** "Later Christian composition: Scher, Cahen, Hamidullah, Wood. Christian-written but with a genuine core: Roggema. Authentic: El-Wakil"

**Problems:**
- Roggema says the text was "certainly penned by Christians, but should not be dismissed as an absolute forgery". That is not "a genuine core", and it is known only from a Google Books snippet (V3 §4B).
- Cahen's remark is an aside that does not name Najran (V3 row 4.32).
- Zein and El-Wakil (2020) are sympathetic but concede the witness problems (V3 §4B; V0 §3.4: "Pro, but hedged").
- Morrow belongs in the "Authentic" list.

**Replace with:** "Later Christian composition: Scher, Hamidullah, Wood; also Cahen, in an aside on 'the Edict of the Prophet to the Christians'. Christian-written but 'not ... an absolute forgery': Roggema (seen in a snippet only). Sympathetic but conceding the witness problems: Zein and El-Wakil (2020). Authentic: El-Wakil (2016), Morrow."

### 18. Sinai row: the book's concession and the limits of the Topkapı check are left out

**Report text:**
- "A witness, Abu Hurayra, became Muslim only around 7 AH."
- "... and no source checked places the Sinai original there"
- "Authentic: the monastery's tradition, Morrow, El-Wakil."

**Problems:**
- The book concedes the list was "in all probability" added later (p. 85).
- Topkapı's own website could not be reached (AUDIT_A A9: "Confirmed as far as checkable").
- No Sinai-specific statement by El-Wakil is in the files.

**Replace:**
- "A witness, Abu Hurayra, became Muslim only around 7 AH; Morrow concedes the list was 'in all probability' added later (p. 85)."
- "... and no source checked places the Sinai original there (Topkapı's own website could not be reached)."
- "Authentic: the monastery's tradition, Morrow; El-Wakil (on the covenants generally)."

### 19. Armenian row: the book is misquoted, and Saladin and Thomson are overstated

**Report text:**
- "Given to Patriarch Abraham I (638–669), who "had two full years" with the Prophet". The Timeline (line 70) and #13 use the same paraphrase.
- "Saladin's 1187 charter is genuine and is the earliest datable trace of the claim"
- "Sanjian ("fabricated"), Thomson and Azarya treat the charters as later"

**Problems:**
- The book's words (p. 191) are: "Since he was Patriarch from 638 to 669 CE, he had two full years in order to obtain a firman or covenant from the Prophet Muhammad". The 638–669 dates are quoted from Krikorian, via Hagopian. The same paragraph also quotes a tradition dating the visit to 626.
- Saladin's charter: Sanjian says it "has all the earmarks of being authentic" (V5 row T78). The report states it as fact.
- Thomson deals with the Armenian chroniclers' pact about "the land of Armenia", not the Jerusalem charters (V5 §4.2).

**Replace:**
- Claims cell: "Given to Patriarch Abraham I, whose term the book gives as 638–669 (after Krikorian) and who, it says, 'had two full years in order to obtain a firman or covenant from the Prophet' (p. 191). The book also quotes a tradition dating the visit to 626."
- Evidence cell: "... Saladin's 1187 charter, which Sanjian judges to have 'all the earmarks of being authentic', refers to pacts of the Prophet, 'Umar and 'Ali, and is the earliest datable trace of the claim."
- Scholars cell: "Sanjian ('must have been fabricated') and Azarya treat the Jerusalem charters as later; Thomson explains the Armenian chroniclers' prophetic pact (about Armenia) as a later attribution. No peer-reviewed defender of a 7th-century origin was found."
- Timeline line 70 and #13: quote the book's words as above. The verdict "Impossible" is fair for the arithmetic as printed.

### 20. The "Points in the book's favour" paragraph leaves out the strongest pro-authenticity evidence the files contain

**Report text (line 217):** "Points in the book's favour also stand. Moritz, a sceptic, records that a late Mamluk decree (Qansuh al-Ghawri, r. 1501–1516) already cites letters of protection of the Prophet, and Thenaud saw a handprinted privilege at the monastery in 1512. ..."

**Problems:**
- "Thenaud saw": Thenaud reports that the mosque holds the privileges (V2a row C13 and §4: "reports"). The report treats Affagart's similar account more strictly ("He relays what the monks told him").
- "The earlier Fatimid decrees": Moritz cites one Fatimid decree (AUDIT_B B13).
- The decree's date (911 or 921 AH = 1505 or 1515) is known and should be given.
- These points from the files are missing:
  - the genre is real (Ayla, Maqna; V6a §4.2 point 1);
  - the 1538 manuscript shows the World text circulating about 90 years before Scaliger (V4 §4; the book argues this on p. 145);
  - Bar Hebraeus independently reports a Najran/Isho'yahb diploma with a parallel tax structure (V3 §4B; V4 §4; V5 §4.1);
  - Saladin's 1187 charter refers to the Prophet's pact and is accepted as authentic by Sanjian (V5 §4.2);
  - Moritz thought an Ottoman removal of an "original" "möglich, sogar wahrscheinlich" (V6a §4.2 point 2);
  - El-Wakil argues it is "highly unlikely" that different communities forged the same wording (V0 §3.4; V6a §4.2 point 3);
  - even sceptics such as Döllinger and Gieseler accepted that Muhammad gave some Arabian Christians letters of protection (V4 §4).

**Replace with:**

> Points in the book's favour also stand. Thenaud reported in 1512 that the monastery mosque held the Prophet's privileges with his handprint, as the book itself argues (pp. 19, 192). Moritz, a sceptic, records a decree of Qansuh al-Ghawri (911 or 921 AH, i.e. 1505 or 1515) that already cites "letters of protection of the Prophet", and he thought an Ottoman removal of an "original" "possible, even probable". So some claimed prophetic letter was in use before the Ottoman conquest; the earliest (Fatimid) decree refers only to "the old treaties". Written prophetic agreements with non-Muslim communities are a real genre (Ayla, Maqna). Hamidullah accepts that a short treaty with Najran existed, and even 19th-century sceptics such as Döllinger and Gieseler accepted that Muhammad gave some Arabian Christians letters of protection. The World text was circulating by 1538, about 90 years before Scaliger (p. 145). Bar Hebraeus reports a diploma for the Church of the East with terms parallel to the Seert text, and Saladin's 1187 charter to the Armenians, accepted as authentic even by Sanjian, already refers to a pact of the Prophet. El-Wakil argues that different communities are "highly unlikely" to have forged the same wording independently. None of this dates the surviving texts to the 7th century, and the monastery maintains the traditional account.

---

## E. Quotations from the book's sources presented as the author's own claims

### 21. Rows that credit Morrow with statements he quotes from someone else

In each row below, the book is quoting or relaying a named source. The report should say so; the correction may still stand against the source the book relies on.

**#44, and Timeline line 106.**
- Report text: "Badr Khan's massacres were in 1845 and 1847; he was rewarded in Crete in 1856"
- Problem: 1845 comes from Surma, and 1847 from Stafford, Browne and Yelda, all quoted (V5 rows T33–T37). V5 rates Yelda's 1847 "Consistent with the cited article", with the date itself disputed. The book does not say he was "rewarded in Crete". It says the Ottomans "used his skills to crush a rebellion of Cretan Greeks in 1856. As a reward ... he was allowed to move to Damascus" (OCR 06_ch6_ch7.txt lines 572–576).
- Replace #44 with: "| 44 | Following Surma (1845) and Stafford, Browne and Yelda (1847), the book dates the massacres to 1845 or 1847; it says Badr Khan crushed a Cretan Greek rebellion in 1856 and was rewarded with a move to Damascus | The massacres were in 1843 (Tiyari) and October 1846 (Tkhuma); 1847 is his defeat. He was pardoned in 1857 and moved to Damascus in 1868. No source opened has him crushing a Cretan revolt; the great revolt of 1866–69 came after he left the island | pp. 181–182 |"
- Timeline line 106: "**Wrong in the sources the book quotes** (Surma 1845; Stafford, Browne, Yelda 1847). The massacres were in 1843 and 1846, and 1847 is Badr Khan's defeat. Two sources the book cites (Yohannan; Theodore) give 1843."

**#47.**
- Report text: "Abbas I relocated over 150,000 Armenians to New Julfa in 1606 and built a new cathedral | The deportation was in October–November 1604 and involved more than 300,000 people (Iranica)."
- Problem: the book says "according to American and European accounts" (OCR 04_ch3_ch4.txt lines 31–33). Iranica's 300,000–400,000 is the *total* deported; about 10,000 settled in New Julfa (V3 row 3.32). Set against that, 150,000 is an *over*statement for New Julfa, not an understatement.
- Replace with: "'According to American and European accounts', Abbas I relocated over 150,000 Armenians to New Julfa in 1606 | The deportation was in October–November 1604, and New Julfa was built from 1605 (one 1974 study says 1606). Iranica gives 300,000–400,000 deported in all, of whom about 10,000 settled in New Julfa, so 150,000 fits neither figure. Abbas I planned a cathedral in 1614 but dropped it; Vank Cathedral was built 1653–64 under Abbas II."

**#54.**
- Problem: the children-sold claim and the 50,000 are quoted from Boase, and "about half a million" from Chejne. On the same page the book itself gives "a total of 300,000", which V6b row T168 rates Consistent. V6b row T167 rates the 50,000 as traced to a contemporary source (Aznar Cardona) with no modern confirmation, not as contradicted.
- Replace with: "| 54 | Quoting Boase: Morisco children over seven were sold as slaves, and over 50,000 'died resisting'. Castile expelled its Moriscos in 1614. Quoting Chejne, 'about half a million' left, beside the book's own 'total of 300,000' | No edict sold children over seven. The order was Valencia 1609; Andalusia, Castile, Aragon and Catalonia 1610; Murcia 1613–14. The 50,000 goes back to Aznar Cardona (1612), who says they 'died miserably'; there is no modern count. Standard totals are 272,000–300,000, matching the book's 300,000 rather than the half-million | p. 345 |"

**#58.**
- Problem: the translation is marked "(qtd. Isseroff)" on p. 337.
- Fix: begin the row "Quoting Isseroff's translation of al-Tabari: ...".

**#62.**
- Problem: the book is quoting Brockopp. A 2013 quotation is being measured against a 2023 figure, and Lebanon has had no census since 1932 (V6b row C81).
- Replace with: "| 62 | Quoting Brockopp: Lebanon is 'still almost half Christian' | No census since 1932; a 2023 US State Department estimate gives about 30.5% of citizens; figures from around 2013 were not checked | p. 334 |"

**#40.**
- Problem: the 17th-century bells come from a quotation of *Arabic News* (p. 18). The book says "temporarily abandoned" (p. 23). V2b row A10 rates this "Inconsistent / Disputed". Bauden (2025) records that most monks took refuge at al-Tur in 1482.
- Replace the "book says" cell with: "Quoting *Arabic News*: the bells date from the 17th century. Jebel Musa was identified as Sinai only in the 15th century, and the monastery was 'temporarily abandoned' by 1479."
- Append to the sources cell: "though in 1482 most monks took refuge at al-Tur after Bedouin attacks (Bauden 2025)".

**#10.**
- Problem: this is Malech's account, quoted by the book (AUDIT_B, line 49: "the book quotes Malech accurately ... which p. 178 endorses").
- Replace the "book says" cell with: "Quoting Malech, the book reports that in 1517 Selim I took the Assyrian covenant from Patriarch 'Shimon the fourth' at Baghdad (p. 177), and finds this 'perfect chronological sense' (p. 178)".

**#30.**
- Problem: the page is wrong (p. 58, PDF 83, not p. 60; OCR 02_ch1b.txt lines 2586–2655). The "less than five thousand" is cited to Karabell, and V1b row T128 says it is true of the first force (3,500–4,000).
- Replace with: "| 30 | Muslims entered Sinai in 634; Egypt fell to 'less than five thousand soldiers' (after Karabell) | 'Amr crossed into Sinai in December 639 (al-Baladhuri: 640). His first force of 3,500–4,000 was reinforced to about 12,000–15,500 before Egypt fell | p. 58 |"

---

## F. Other misstatements of the book's wording

### 22. Rows where the "book says" cell does not match the page

**#56.**
- Report text: "the Battle of the Masts was fought under 'Umar"
- Problem: the book says Mu'awiya, "While governor of Syria under the Caliph 'Umar ... organized a navy ... which resulted in the defeat of the Byzantine navy at the Battle of the Masts in 655 CE" (OCR 08_ch13_ch17.txt lines 1403–1409). The 655 date is correct (V6b row T116).
- Replace with: "'Umar visited Jerusalem in 659; Mu'awiya built his navy 'while governor of Syria under the Caliph 'Umar' | 'Umar died in 644. He refused Mu'awiya a naval expedition (al-Baladhuri); the first came under 'Uthman, and the battle (c. 655, as the book says) fell in 'Uthman's reign".

**#61.**
- Report text: "Muslim Granada lasted more than 700 years"
- Problem: the book says "the Emirate came to an end after more than seven hundred years" (p. 342; OCR lines 1611–1615). Rephrased as "Muslim Granada", the statement becomes roughly true (c. 713–1492). V6b row T134 rates the book's actual sentence a "Minor difference (conflation)".
- Replace with: "'Abd al-Rahman I was the last Umayyad caliph; the Emirate of Granada ended 'after more than seven hundred years' | Marwan II was the last Umayyad caliph. The Nasrid emirate lasted 1238–1492; seven centuries fits Muslim rule in Iberia, not the emirate."

**#49.**
- Report text: "Qur'an 5:29 forbids violating the rites of Allah"
- Problem: p. 25 says Shi'ites respect "the signs of Allah (Qur'an 22:32; 40:81; 5:29; 31:32)" (OCR 01_front_ch1a.txt lines 3900–3902). The book does not say 5:29 forbids anything.
- Replace with: "| 49 | Cites Qur'an 22:32, 40:81, 5:29 and 31:32 for respecting 'the signs of Allah' | 5:29 is the Cain and Abel verse; 5:2 ('do not violate the signs/rites of Allah') is probably meant | p. 25 |"

**#24.**
- Report text: "'Dr. Addison' gave a detailed defence of the World covenant, listed beside James Thayer Addison (1887–1953) | The cited article concerns Lancelot Addison (d. 1703), who called the treaty one of Muhammad's "artifices" and reported an Arabist's view that Scaliger forged it"
- Problem: the book itself quotes both the "artifices" passage and the Arabist's opinion (pp. 154, 157), and calls Addison's views "evidently incorrect" (p. 154). As worded, the row implies the book hid them. The real faults are calling this a "detailed defense" and never naming Lancelot (AUDIT_A A12, "partly confirmed").
- Replace the sources cell with: "The cited article (*General Dictionary*, 1734) concerns Lancelot Addison (d. 1703), whom the book never names. His view that the treaty was one of Muhammad's 'artifices', and an Arabist's opinion that Scaliger forged it, both of which the book quotes (pp. 154, 157), are not a defence of authenticity."

**#21.**
- Problem: the book cites Sanjian's captions in Narkiss (not checked; the audit notes they "may well say 'attributed'"). "Fabricated" comes from Sanjian's own 1965 monograph.
- Replace the sources cell with: "In his own monograph (*The Armenian Communities in Syria*, 1965, p. 169) Sanjian writes that these edicts 'must have been fabricated' and 'have no historical foundation'. The book cites only his captions in Narkiss, which were not checked."

**#2.**
- Problem: the book's hedge "To my knowledge" (p. 359) is dropped. Also, the Khaybar letter is itself Jewish, so it disproves "the only" but not "not by Christians".
- Replace the "book says" cell with: "'To my knowledge, the only prophetic letter of protection which was forged ... was produced, not by Christians, but by Jews' (the Cairo Geniza letter)".
- Append to the sources cell: "Specialists (Scher, Hamidullah, Moritz, Mouton) have judged Christian-held covenants forged."

**#7.**
- Problem: the book does quote Ibn Ishaq's doubt ("God knows whether that was so"). The fault is that the ellipsis removes "from Abyssinia" and the book then concludes the contact was clear (V3).
- Replace the sources cell with: "Ibn Ishaq (Guillaume p. 179) says the twenty Christians came 'from Abyssinia', giving Najran only as a report he doubts. The book quotes the doubt, but its ellipsis removes 'from Abyssinia', and it gives the visit a date Ibn Ishaq does not."

**#9.**
- Problem: the epigraph keeps Scher's two reasons (the copies differ between communities; the language is faulty), and the book answers them (pp. 109–110). The ellipsis removes only his reference (Cheikho, *Al-Machriq* 1909), which nobody opened (V3 §5).
- Replace with: "Scher's note (PO 13, p. 602 n. 1) gives two reasons: the copies differ between communities, and the language is faulty. The book's epigraph quotes both and the book answers them (pp. 109–110). Its ellipsis removes only Scher's reference (Cheikho, *Al-Machriq*, 1909). The note is brief, but it is not without argument."

**#4.**
- Problem: the book's actual argument is left out. It reads the reader's mark "Gabriyal Sahyun al-Ziftawi" as Gabriel Sionita (p. 145). V4 rates that identification "Disputed / unsupported", since al-Ziftawi points to Zifta in Egypt.
- Replace the sources cell with: "The BnF record says it was 'bought in the East' by Vansleb (travels 1663–64 and 1671–73). The book's identification rests on a reader's mark of 'Gabriyal Sahyun al-Ziftawi', which it reads as Sionita; the name more likely points to Zifta in Egypt. By the book's own transcription, the 1538 text differs from the 1630 print in scribe, date and witnesses, and the book later calls the relation one that 'remains to be determined' (p. 176)."

### 23. The Armenian verdict quotation drops its conditional

**Report text:** "| "Genuine, as I believe both it and the other covenants ... most likely are" (p. 202) |"

**Problem:** the book reads "if the document is indeed genuine, as I believe both it and the other covenants presented in this book most likely are" (OCR 06_ch6_ch7.txt lines 2207–2210). The same paragraph considers that it could be the work of "a misguided, but well-intentioned, Christian". Capitalising "Genuine" and dropping "if" changes the sense.

**Replace with:** "Likely genuine: 'if the document is indeed genuine, as I believe both it and the other covenants presented in this book most likely are' (p. 202); the book also considers that it may be the work of 'a misguided, but well-intentioned, Christian'".

### 24. Other key facts, "Witness lists": the book argues the opposite of what the row implies

**Report text:** "| Witness lists | Morrow calls a list of 32 Companions on a prophetic treaty "anomalous" and a "possible addition" | p. 115 |"

**Problem:** on p. 115 the book grants the anomaly, but argues that forgers "would have been running a huge risk", that "what initially appears to be a major error may actually act as confirmation of the Covenant's authenticity", and that the covenants "were designed to be anomalous" (OCR 04_ch3_ch4.txt lines 1601–1636).

**Replace with:** "Morrow grants that 32 witnesses are 'anomalous' for a prophetic treaty and may be an 'addition', but argues that forgers would not have risked such a list, so the apparent errors 'may actually act as confirmation of the Covenant's authenticity' (p. 115)".

### 25. Other key facts: four rows need precision

**Najran evidence.**
- Report text: "Morrow concedes the covenant "appears to be completely absent in the classical Islamic sources" and that "most scholars dismiss it as dubious""
- Problem: the next sentence is the author's reply: "However, when viewed in a broader context, such a position seems eminently reactionary and intransigent" (AUDIT_B B12).
- Fix: append ", but calls that position 'eminently reactionary and intransigent' (p. 112)".

**Constitution of Medina.**
- Report text: "Dated 622 (after Ibn Ishaq)"
- Problem: the translation comes from Ibn Ishaq. The dating "622–624" is attributed to Esposito, and the book allows it "may even date from a later period" (p. 28; 01_front_ch1a.md rows 75, 78, 79).
- Replace with: "Presented as made on arrival in 622; dated 622–624 after Esposito, possibly later (p. 28); text from Ibn Ishaq".

**Prophet's campaigns.**
- Report text: "30 expeditions led and 61 sent"
- Problem: the book prints lists, not totals. The figures are counts of those lists, which contain duplicates (V1b row T122; 02_ch1b.md §7 item 15).
- Replace with: "Lists about 30 expeditions led and 61 sent (counted from its lists, which contain duplicates; no totals given)".
- Same fix in Errors #34. Also change "have no source" to "are given without a source ('It is estimated', p. 43)".

**Where the Sinai original is / Sinai archive.**
- Problem 1: the book's alternative, that the original was taken later under Süleyman (p. 69, after Mouton; AUDIT_A A8), is left out.
- Problem 2: "Selim I's own firman survives" is Atiya's statement, quoted on p. 74. Moritz says Selim's firman had disappeared (V2a row C17).
- Fix: add "or perhaps later under Süleyman (p. 69)" and "Selim I's own firman, Atiya reports, 'has actually been located'".

**Assyrian witnesses (six-covenants table).**
- Report text: "27 (p. 179)"
- Problem: the book also says 32 (p. 370), and Malech prints 31 names in English and 33 in Persian (V6a row 1D-3).
- Replace with: "27 (p. 179); 32 (p. 370); Malech prints 31 (English) and 33 (Persian) names".

---

## G. Timeline section

### 26. "Twenty-five years of silence" (Timeline line 46, Errors #12) overstates the sources and leaves out the book's concession

**Report text:**
- Timeline: "**Contradicted.** Ibn Ishaq, Ibn Sa'd and al-Tabari place him in Mecca at about 20, 25 and 35. No early source records a Sinai visit"
- #12: "Ibn Ishaq, Ibn Sa'd and al-Tabari place him in Mecca at about 20 (the Fijar war), 25 (his marriage) and 35 (rebuilding the Ka'ba)."

**Problems:**
- Ibn Ishaq dates the Fijar war by the Prophet's age but does not say he fought in it. His participation comes from Ibn Hisham's note (aged 14–15) and from Ibn Sa'd (aged 20). Watt warns that the ages are "multiples of five" and approximate (AUDIT_B B8, which this report does not apply).
- Fijar was fought near Mecca, not in it.
- "No early source records a Sinai visit": V2b §4 excepts the Night Journey narration (al-Nasa'i 450), which the book cites on p. 21.
- The book itself mentions the Fijar reports (pp. 6, 12). It says many Muslims would reject the Sinai accounts, "perhaps rightfully so", and calls the Sinai stay a "creative reconstruction" (p. 12; OCR 01_front_ch1a.txt lines 2587–2649).
- "c. 585–610" is the report's own conversion of the book's ages 15–40.

**Replace the timeline cell with:** "**Contradicted.** The record is thin and the ages are rounded, but the early sira places him at the Fijar war and the Hilf al-fudul (about 20; Ibn Sa'd, Ibn Hisham), at his marriage (25) and at the rebuilding of the Ka'ba (35). The book mentions Fijar but calls it 'spurious' without a source (p. 6), and concedes that Muslims may reject the Sinai accounts, 'perhaps rightfully so' (p. 12). No Islamic historical source examined records a physical visit to Sinai; one hadith (al-Nasa'i 450, cited on p. 21) places a prayer there during the Night Journey."

**Replace the #12 sources cell with:** "The early sira places him at the Fijar war and the Hilf al-fudul at about 20 (Ibn Sa'd quotes him: 'I attended it with my uncles and shot arrows'; Ibn Hisham gives 14–15), at his marriage at 25, and at the rebuilding of the Ka'ba at 35. The record is thin and its ages are round numbers (Watt), but it is not silent, and no early source mentions Sinai."

### 27. Timeline rows rated "Matches" or "confirmed" where the fact-check says otherwise

**Line 104, Burckhardt 1816.**
- Report text: "Matches; he saw the copy at the monastery's Cairo house"
- Problem: V2a row C10 is "**I**" (Inconsistent). The book says he examined "the copy ... on display", "in all probability" the 1800/01 copy (p. 68), but the copy he saw was kept at the Cairo house. His words were "I do not believe it to be an authentic document" (V2a row C9). "Calls it a forgery" is the book's paraphrase.
- Replace with: "**Partly.** He was at Sinai in spring 1816 and judged it inauthentic ('I do not believe it to be an authentic document'). But the copy he saw was kept at the monastery's Cairo house, not the display copy the book names (p. 68)."

**Line 59, Tabuk.**
- Report text: "| 9 AH (630) | Tabuk; treaties with Ayla, Maqna and Adhruh | pp. 52–53 | Matches."
- Problem: p. 53 places these treaties "in approximately the same period" as 8 AH and dates only Maqna to 9 AH. V1b row T105 rates this "Minor difference", and V1b §2 says "the book's 8 AH framing is off by a year". The Yuhanna-at-Medina claim is on p. 54.
- Replace with: "| 'approximately the same period' as 8 AH (630); Maqna 9 AH | Treaties with Ayla, Maqna, Adhruh and Jarba' | pp. 53–54 | **Minor difference.** The sources place all four at Tabuk, 9 AH (autumn 630). Yuhanna of Ayla met the Prophet at Tabuk, not Medina (p. 54) |"

**Line 91, 1561 codex.**
- Report text: "Matches 968 AH"
- Problem: V2a row D3 says it "probably matches", not confirmed, and the 1561 date is known only secondhand.
- Replace with: "Probably Moritz's copy of 968 AH (1560/61), not confirmed. Moritz also records an older dated copy of 957 AH (1550/51). The book allows that undated copies may be older (p. 66)."

**Line 123, 1956 and 2002 reprints.**
- Report text: "Reprints confirmed."
- Problem: V1a row 78 rates 1956 "partly verified". 2002 is unconfirmed: V3 row 4.59 found printings of 2001, 2004 and 2012.
- Replace with: "Both reprints exist; the 1956 date is partly verified, and the 2002 date unconfirmed (printings of 2001, 2004 and 2012 found)."

**Line 55, Banu Qurayzah.**
- Report text: "Matches. But the judge, Sa'd ibn Mu'adh, was named by the Prophet, not "appointed by the Jewish people""
- Problem: V1b row T58 rates this "Disputed among sources". Qurayza consented to Sa'd (Ibn Ishaq; Kister; Bukhari 3043).
- Replace with: "Date and 25-day siege match. The book's 'judge appointed by the Jewish people' is disputed: in Ibn Ishaq the Prophet proposed Sa'd ibn Mu'adh, a Muslim of the Aws, and Qurayza consented."

**Line 49, Constitution of Medina.**
- Report text: "to a composite text finished after 627 (Watt)"
- Problem: Watt says only that the present form "might belong to the period after the elimination of Qurayzah" (V1a row 53; V1b row T29). The book itself sets out this range on p. 28.
- Replace with: "Hijra matches. The Constitution's date is disputed, as the book itself notes (p. 28). Lecker dates it to 622; Watt thinks it composite, with its present form possibly after Qurayza (627)."

### 28. Line 82 (Sinai original, 1517) gives one side, and a key dated item is missing

**Report text:** "**Disputed.** Tradition names "Selim or Süleyman" (Moritz, 1918). Among the sources checked, the year 1517 first appears explicitly in Arundale (1837)"

**Problem:**
- V2a row C3: Khair Bey's decree of 927 AH (1520/21) says that while Selim was in Egypt "these old documents were shown to him".
- AUDIT_A A8: Burckhardt and Cantemir tie the removal to Selim's conquest. Arundale's source (Mauchin) was not checked. The book itself raises Süleyman (p. 69).
- The timeline keeps the negative 975 row but has no row for the book's Mamluk decrees (p. 71) or for Moritz's 911/921 AH decree. That decree is the earliest Muslim document found to name the Prophet's letter (V2a §2b; AUDIT_B B13).

**Replace with:** "**Disputed.** A decree of 1520/21 says the old documents were shown to Selim in Egypt, and Burckhardt and Cantemir tie the removal to his conquest. But tradition names 'Selim or Süleyman' (Moritz, 1918), and the book itself raises Süleyman (p. 69). The numeral 1517 first appears, among sources checked, in Arundale (1837), citing Mauchin (not checked)."

**Add after the 975 row:** "| 1259–1516 | Mamluk decrees confirming the monks' privileges | p. 71 | The book's list is unverified (Ernst's edition was not accessible). Moritz (1918) records a decree of Qansuh al-Ghawri of 911 or 921 AH (1505 or 1515) that names 'letters of protection of the Prophet', the earliest Muslim document found to do so |"

### 29. Wrong pages, and dates the book does not print

- **Line 67, "634 | Muslims enter Sinai | p. 60":** the page is p. 58 (PDF 83; OCR 02_ch1b.txt lines 2586–2655). The same fix applies to #30 (item 21).
- **Line 58, "pp. 113, 183":** the 630 / 8 AH Najran delegation is on p. 112 (V3 row 4.13). Change to "pp. 112, 183".
- **Line 125, "11 Aug 2013":**
  - The book prints no launch date; that is the web-post date (V1a row 82).
  - Change the date cell to "2013 (the book gives no date; the online post is dated 11 Aug 2013)".
- **Line 122, "(1948 in the front matter) | pp. 99, xviii":** p. 103 also gives 1948, which is how #92 cites it. Change to "(1948 on pp. 103 and xviii) | pp. 99, 103, xviii".
- **Line 69, "(635–638)":**
  - V5 row T69 and §2 give 634/5 (Theophanes) to 638.
  - Change to "(634/5–638)".
- **Line 37, intro:**
  - Report text: "the 69 below are the ones the book's argument rests on ... Dates are as the book prints them".
  - Problem: several rows have nothing to do with the argument (1916, 1922, Stanley). Several dates are the report's own conversions (c. 585–610; 15 AH (636); 9 AH (630); 11 Aug 2013).
  - Replace with: "The 69 below are a selection: the main events of the book's chronology and the dates tested most closely. Dates are as the book prints them; CE equivalents are added where the book gives none." The counts 1,336 and 69 are correct.

### 30. Smaller timeline refinements

- **Line 50 (7 July 623):**
  - The book calls 7 July 623 a date "of the Gregorian calendar" (p. 83). V2a row A1 says that label is wrong.
  - Replace with: "**Minor error.** The book calls 7 July 623 Gregorian; it is the Julian date (10 July Gregorian). Early hijri dates may be off, and the hijri era was adopted c. 637–638."
- **Line 54 (Ja'far):**
  - The book itself places the return at Khaybar (V3 row 4.6).
  - Replace with: "**Wrong year.** He did return at Khaybar, as the book says, but that was 7 AH / 628; the book dates Khaybar to 629 (p. 105)."
- **Line 57 (Khaybar):**
  - The 629 is the author's own date, in a passage about Sunni reports of a ban on mut'a.
  - Replace the event with: "Conquest of Khaybar dated 629 (in a passage on Sunni reports of a ban on mut'a)".
- **Line 60 (Najran 10 AH):**
  - Append: "(the book follows Qureshi, pp. 113–114; the sources do date Khalid's and 'Ali's Najran missions to 10 AH)".
- **Line 76 (975):**
  - Append: "The book's source (Atiya 1955, p. 26) could not be opened; Heidemann et al. say that hand-list has many date errors."
- **Line 89 (Affagart):**
  - Append: "; the book itself notes this (p. 69)".
- **Line 92 (Scaliger):**
  - Only his travel dates are attested.
  - Replace with: "His travel dates broadly fit (in Aleppo from c. 1626, back in France by 1629); no source dates the acquisition itself."
- **Line 93 (1630 edition):**
  - Replace "Matches the title page" with "Matches: the title page names Vitray; the Latin version is Sionita's".
- **Line 95 (1638):**
  - The book itself says Fabricius "apparently only included the Latin translation" (p. xv; V4 row T95).
  - Replace with: "Matches: Fabricius, Rostock 1638, Latin only, as the book says (p. xv). The 1638 Turkish copy on the cover could not be checked."
- **Line 103 (Napoleon):**
  - For balance, append: "It exempts the monks 'according to the various titles they keep' (Art. 3)" (V2a row F4).
- **Line 105 (Arundale):**
  - Replace with: "**Wrong.** He went to Egypt in 1831 but reached Sinai in August 1833" (V7a row 50; V2b row D7).
- **Line 119 (Sharif):**
  - Append: "(earlier Sharifian manifestos of 1916 and 1917 exist; the text quoted is the 1918 letter)" (V5 row T91).

---

## H. Literature and reviews

### 31. "Other books and studies" table

- **El-Wakil 2016.**
  - Report text: "Dismissing them as forgeries is "no longer tenable""
  - Problem: this drops "categorical". The abstract says "categorical dismissal of the covenants as forgeries is no longer tenable" (V0 §3.4), a weaker claim.
  - Replace with: "'Categorical dismissal of the covenants as forgeries is no longer tenable'".
- **Zein & El-Wakil 2022.**
  - Problem: "forgery claim 'no longer tenable'" comes from the publisher's description, which was all that was read (V0 §3.4).
  - Fix: add "(publisher's description)".
- **Morrow 2021.**
  - Problem: the "Main evidence" cell lists only a concession.
  - Replace with: "Manuscript filiation: proposes the 'Rylands' text as a 'missing link' between the Seert Najran text and the 1630 Testamentum, while dating it 'an Ottoman-issued document' of the 16th or 17th century".
- **Scher 1919.**
  - Report text: "Text surfaced only in 878–79 CE by its own account"
  - Problem: that is not Scher's argument.
  - Replace with: "Each Eastern Christian community keeps a different copy; 'incorrect' language; cites *Al-Machriq* (1909)" (V3 §4B; PO 13 p. 602 n. 1).
- **Hamidullah, "1956 ff."**
  - Problem: the verdict was read in his 5th edition (V3 row 4.58).
  - Fix: "1956 (text); verdict as read in the 5th ed."
- **Rycaut, "Accepts".**
  - Problem: Rycaut reports that "very good Authors" take it for real, in order to argue that Muhammad broke it (V4 row C125).
  - Replace with: "Reports it as taken for real 'by very good Authors'".
- **Burckhardt, "Forgery (Sinai)".**
  - Fix: "Not authentic ('I do not believe it to be an authentic document')" (V2a row C9).
- **Add the main pro argument as a row:** "| El-Wakil, *Religions* 10:9 | 2019 | Authentic (protection clause) | 'highly unlikely for different non-Muslim communities to have forged this Prophetic statement' |" (V0 §3.4).

### 32. The Reviews table is uneven in what it records

- **Monferrer-Sala.**
  - Report text: "Unpersuaded"
  - Problem: V0 §2.3 gives "Verdict: mixed. He praises the breadth but is not persuaded on authenticity." V0's table says "Unpersuaded".
  - Replace with: "Mixed: praises its breadth; unpersuaded on authenticity".
- **Valkenberg.**
  - Problem: the note leaves out that he grants "a multiple attestation (tawātur in hadith science) of such covenants" (V0 §2.3).
  - Fix: add that phrase.
- **Sanni.**
  - Problem: V0 rates him critical/mixed, and his quotations reached the fact-check via the Pfander Center, an evangelical advocacy site (V0 R7).
  - Fix: "Critical/mixed | Not opened; known only through quotations on an advocacy website".
- **Reynolds.**
  - Fix: add "short 'Briefly Noted' notice (magazine)" (V0 §4).
- **Sellam.**
  - Problem: the conflict-of-interest note rests on an interview. A link the user can check is printed in the book itself: Sellam's back-cover endorsement (01_front_ch1a.md §3 item 5; OCR 01_front_ch1a.txt line 164) and his name in the printed list of Initiative signatories (OCR line 1310).
  - Fix: "His endorsement is printed on the book's back cover and he signed the Covenants Initiative; Morrow thanks him for help with translations".
- **Optional, for symmetry:** the critics' affiliations could be stated as neutrally as the supporters' (e.g. Reynolds, Catholic magazine *First Things*), or both dropped.

---

## I. Remaining items in Errors tables 1–5

### 33. Small refinements

- **#3.**
  - Report text: "Every edition of the Sinai archive starts at 1130 (Stern; Heidemann et al.; Atiya 1950)"
  - Problem: Atiya 1950 is a survey, not an edition; Moritz gives 1134. Fairness point: three of the book's other Fatimid dates (1135, 1154, 1156) match Stern (AUDIT_A A1; V2a row E1).
  - Replace with: "No source checked attests a Sinai decree from 975: Stern, Heidemann et al. (1997) and Atiya (1950) put the oldest at 524/1130, and Moritz at 1134. The book's other Fatimid dates (1135, 1154, 1156) do match Stern. Its source for 975, Atiya's 1955 hand-list, could not be opened."
- **#5:** append "The fourth month is Rabi' al-Akhir, so the book's month is roughly right; the error is the day."
- **#14:** replace with "*Tawatur*, in wording or meaning, requires mass transmission at every level of a chain, and *musnad* and *muttasil* describe a connected chain. The covenants list witnesses, but no chain links them to the surviving copies" (V6a §1C, §4.3 point 2).
- **#16:** append "The book quotes Burckhardt through Manley and 'Abdel-Hakim, and the misreading may come from them (AUDIT_A A7)."
- **#18:** clarity only. Append "Square brackets conventionally mark an insertion, but the words are not identified as the author's gloss and they narrow the command" (AUDIT_B B7).
- **#19:** append audit B6's nuance: "The poisoner, Zaynab bint al-Harith, was the wife of a Nadir man; the link to the Nadir is real, the chronology is not."
- **#22:** append "The quoted words themselves are accurate (AUDIT_A A4)."
- **#28:** replace with "The decree (19 Dec 1798) protects the monks and keeps their exemptions 'according to the various titles they keep' (Art. 3), but names neither the Prophet nor any covenant."
- **#37:** append "(the parchment's authenticity is itself debated)" (V1b row C28).
- **#38:**
  - Report text: "no source supports a Jewish invitation"
  - Problem: this overstates V1b row T132.
  - Replace with: "the received tradition names Count Julian; the *Jewish Encyclopedia* has Jews helping only after the landing, and Simon (1983) calls Jewish collaboration in 711 'one of the most persistent myths'".
- **#41:** see item 30 (Arundale went to Egypt in 1831).
- **#46:** append the 1916 and 1917 manifestos note (item 30).
- **#48:** "about 369 million acres in 1520" (V5 row T25).
- **#53:** Mármol's figure is "more than 400" women and children killed, and the 4,500 enslaved came from Galera and nearby places. V6b row T142 found the first quotation's substance in Wiegers.
  - Replace with: "Neither sentence is in Wiegers (1994), though the first agrees with him in substance. At Galera, Mármol records more than 2,400 fighting men and more than 400 women and children killed, and 4,500 enslaved from Galera and nearby places."
- **#59:** pages "pp. 333, 341". Add "(the book cites 2:62 correctly on p. 374)" (V6b row C115).
- **#67:** "The cited author lived 1868–1949 (BnF); 1932–1989 are the dates of a different man, Safdar Husain Najafi."
- **#73, #81, #82** (precision):
  - #73: "12th century (d. 1179 per GND; c. 1185 per other references)".
  - #81: "973–1048 or later".
  - #82: "1862–1931 (GND: 1864–1931)".

---

## J. Method, limits, sources, provisions

### 34. "How this was done, and its limits"

- **Line 387: "a hand check of the rest found only scan errors"**
  - The QA file says the misses were sampled.
  - Replace with: "a hand check of a sample of the rest found only scan errors, not misquotation".
- **Line 387: "All 3,171 page citations are consistent"**
  - Replace with: "All 3,171 printed-page/PDF-page pairs agree with the page map".
- **Line 387: "2,568 of 2,871 quotations match word for word"**
  - Add "(after normalising case, accents and punctuation)".
- **Line 388: "Thirteen research agents ... Every verdict had to rest on a page the agent opened, not a search snippet. Wikipedia was used only for uncontroversial dates"**
  - Twelve reports carry verdicts; V0 surveyed reception; several reports used helper sub-agents.
  - Some rows rest on Google Books or Open Library "search-inside" excerpts, labelled as such (V3 rows 3.5, 3.32, 3.34; Roggema).
  - The reports say Wikipedia was used "as a lead or for uncontroversial dates".
  - Replace with: "Twelve fact-check reports (V1a–V7c) checked the claims by chapter and topic, and a thirteenth (V0) surveyed the reception and wider scholarship; several used helper sub-agents. Verdicts rest on pages the agents opened; a few rest on 'search-inside' excerpts, labelled as weaker. Wikipedia was used only as a lead or for uncontroversial dates, and labelled."
- **Line 393: "the paywalled *Encyclopaedia of Islam*" (listed as not opened)**
  - The report itself cites EI2 (#64), and V3 and V7a read EI2 articles through an archive.org copy and Brill abstract pages. Only AUDIT_B skipped EI2.
  - Replace with: "Brill's online EI2 was paywalled; EI2 articles were read from an archive.org copy and abstract pages, and the audit used TDV instead."
  - Also add Boase, the source behind #54, which V6b could not open.

### 35. "Sources" list

- **Line 403: "These are the main sources the fact-check opened and relied on."**
  - Several entries were seen only as an abstract or a publisher page (V0 §3.4, V3, V5):
    - El-Wakil 2016: abstract.
    - Wood 2021: abstract.
    - Zein & El-Wakil 2022: publisher's description.
    - Iranica: read through Wayback snapshots.
  - Mark these, e.g. "(abstract only)".
  - The Zein & El-Wakil text actually used is the article in *Al-Shajarah* 25:2 (2020); add it.
  - Every URL listed does appear in at least one report.

### 36. Provisions paragraph (line 176)

- **Report text:** "and Muslim help to repair churches"
- **Problem:** Sinai I only forbids hindering repairs, and Sinai V says help is "not [to] be withheld" (07_texts.md, Sinai items 11 and 13). The Persia statement in the same paragraph is right.
- **Replace with:** "and Muslim help with, or no hindrance to, church repairs".

### 37. Sinai copies sentence (line 145)

- **Report text:** "The earliest dated copy the book lists is from 1561 CE, about 940 years after the claimed date of issue."
- **Problem:** the book adds that "one cannot state with certainty that the earliest copy dates to 1561 ... Some of the undated covenants may actually be older" (p. 66). Moritz records a copy of 1550/51.
- **Fix:** append "The book cautions that undated copies may be older (p. 66). Moritz (1918) records a copy dated 957 AH (1550/51)."

---

## No change needed (checked and sound)

- **About the book table.**
  - Title, publisher and imprint; author born 1971 (LC heading on the copyright page).
  - Both ISBNs as printed on the copyright page (the hardback ISBN is not confirmed externally, V0 §1.1, but the table says "from the copyright page").
  - LC class, LCCN and Dewey; the 1638 Turkish cover copy; covenantsoftheprophet.com.
  - xx + 441 pages (About the Author is p. 441). The PDF has 468 pages and its OCR layer dates from May 2022 (pdfinfo: ABBYY FineReader, 19 May 2022).
- **Structure paragraph and the discussion/text page table.** All chapter page ranges match the contents (01_front_ch1a.md §3 items 10–11). "No separate text chapter" for the Armenians is right.
- **"About the copy analysed".** The page map (p. 1 = PDF 24; pp. 32–33 repeated at PDF 55–58; from p. 34, PDF = p. + 25) matches QA_extraction_checks.md and the OCR markers.
- **Timeline rows.** 570, 582, 595, 610, 619, 624, 625, 4 AH World ("Mistranslated" is fair), "probably" 627, 632, 15 AH, 40 AH, 685–705, 711, 265 AH, 897, 996–1021, 1106, 1187, 783 AH, 1512, 1517 Assyrian (matches AUDIT_B B1), 1538, 1655, 1663–66, 1690, 1737–38/1778/1800–01, 1743, 1795, 19 Dec 1798, 1858, 1881, 1888, 1902, 1910, 1915, 1916, 1917, 1919, 1922, 1986, 2013 closure. Also correct: the counts of 1,336 dated items and 69 rows.
- **Six-covenants table.**
  - Sinai: date, scribe, witnesses, source, verdict quotation (p. 98).
  - Najran: scribe (p. 300), source (p. 109), "last year" dating (p. 118), verdict (p. 138).
  - World: date, scribe, 36/30 witnesses, sources, verdict (pp. 167, 175).
  - Assyrian: scribe, source, verdict (pp. 177, 190).
  - Armenian: scroll description.
- **Sinai copies table.** Every row matches p. 65 and V2a rows D1–D2; also the 1858 Canea copy and Atiya's 43 Turkish translations.
- **Other key facts.** Mosque and minbar; early life including 582/595; "twenty-five years of silence" as the book's argument; archive figures; 975–1888 confirmations and fatwas; printing claims (p. 151); 1795 committee; Covenants Initiative.
- **Other books table.** Early Muslim sources (the cell includes the religious guarantees AUDIT_B B12 asked for); Sionita; Pococke; Moritz (B13 correction applied); Mouton; the monastery website; Wood; Prideaux (the 1698 edition opened; first edition 1697).
- **Reviews table.** Castleton, Walsh, Mehraj ud Din, Hussain.
- **Covenant-by-covenant, apart from items 4 and 14–19.**
  - Sinai: decrees from 1130, copies of 1550/51 and 1560/61, Abu Hurayra, Moritz "Selim or Süleyman", the TDV four letters (A9).
  - World: 1630 date reading, Vitray, 36 witnesses (A11).
  - Najran: the short treaty's terms; Sa'd ibn Mu'adh with Mu'awiya.
  - Assyrian: 1517, Baghdad and Shem'on VI (B1); 4 AH colophon, Hamza and Ja'far (B2).
  - Armenian: the 'Umar firman as the Greek Orthodox document; Sharif's decree 18 Rajab 1336 = 29 April 1918 (B4).
  - The chart caption's balance sentence ("A gap does not by itself prove forgery...").
- **Errors tables, apart from the items above.** #13, #15, #17 (optionally add the book's hedge "While not entirely convincing", p. 41), #20, #23, #25, #26, #27, #29, #31, #32, #33, #35, #36, #39, #43, #45, #50, #51, #52, #55, #57, #60, #63–66, #68–71, #74–80, #83–87, #92, #95, #97–99.
- **Methods facts that hold.** 468-page PDF; nine sections; 689 of 694 years; 2,568 of 2,871 quotations; two tables read from page images; two audits; 26 findings re-checked, 23 confirmed and 3 partly confirmed. The Limits bullets on Atiya 1955, Ernst, Schwarz, Skrobucha, Hobbs, Mouton 1998, Sanni and Hussain, the search quota, AI reading of Arabic/Persian/Armenian, and "No reliable source found means unverified" are all accurate.
