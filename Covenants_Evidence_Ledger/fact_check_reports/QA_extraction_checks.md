# Quality checks on the book extraction

These checks test whether the nine extraction files faithfully record what the book says. They were run by script against the PDF's own text layer, independently of the agents that wrote the extractions.

| Check | Method | Result |
|---|---|---|
| Years land on the cited page | Every 3–4 digit year in each timeline row's "Date as printed" cell was searched for on the PDF page(s) the row cites | 689 of 694 years found (99.3%) |
| Printed page and PDF page agree | Every "p. M [PDF N]" pair was tested against the page map (p. 1 = PDF 24; the scan repeats pp. 32–33 at PDF 55–58; from p. 34, PDF = p. + 25) | 3,171 pairs, 0 mismatches |
| Quotations are verbatim | Every quoted passage of 25+ characters was searched for, after normalising case, accents, hyphenation and punctuation, on the cited page(s) and the page either side | 2,568 of 2,871 found verbatim (89.4%) |

**What the misses were.** The five unmatched years were: one passage that starts on the page before the one cited (the 1403 treaty, PDF 113 rather than 114); one session number written out in words in the book ("five hundred and fourteenth"); and three rows where the "date" is a description such as "undated (before 1630)". For quotations, the unmatched 10.6% were sampled by hand. Every sampled miss was caused by the scan's text layer, not by a misquotation: doubled letters ("tthe losing … wworld"), words split across the two print columns, or brackets the agent normalised ("[w]hen" written as "When").

**Page map anomaly.** The PDF repeats printed pages 32–33 (PDF 55–56 and 57–58 are the same pages). One chunk label was wrong as a result (PDF 56 is p. 33, not p. 31); the extracting agent caught it and cited the correct page.

**Table images.** Two tables the text layer scrambled were read from page images instead: the list of Sinai copies on p. 65 (PDF 90) and the witness tables in Appendix I (PDF 402–406).
