# V7b: People list 1b, fact-check of dates

**Book:** John Andrew Morrow, *The Covenants of the Prophet Muhammad with the Christians of the World* (2013).
**Input:** `scratchpad/people/people_1b.md` (155 rows, chapters 3-7, pp. 110-201).
**Checked:** 2026-11-10.

## How the rows were checked

Every verdict rests on a page or record I actually opened. These are the sources:

- **Wikidata** entity records, retrieved through the API. I noted each claim's own reference (GND, BnF, Britannica and so on).
- **GND (Deutsche Nationalbibliothek)** authority records, read through `lobid.org/gnd/<id>.json`.
- **BnF** authority headings, from `data.bnf.fr/ark:/12148/cb<id>`.
- **TDV İslâm Ansiklopedisi** (`islamansiklopedisi.org.tr`), a peer-reviewed scholarly encyclopaedia. It gives AH/CE death dates in its headers.
- **Wikipedia, used only where marked:**
  - modern uncontroversial dates;
  - patriarch lists (the Church of the East list follows Wilmshurst);
  - three event dates: the abolition of the caliphate, the Toulon wintering, and the Fano printing;
  - Ja'far as a second source after TDV;
  - Berthold, Samuel of Ani and Bedir Khan.
- Single pages from **Store norske leksikon**, **Dizionario Biografico degli Italiani** (Treccani) and **WikiShia**.

**Sources I could not use:**

- Britannica returned 403.
- id.loc.gov (LoC) returned 403 behind Cloudflare.
- VIAF and the Iranica search are JavaScript-only.
- The session's web-search budget ran out partway through. After that I only opened known URLs and searched Wikidata and GND.

**Verdict rules:**

- **Minor difference:** ±1 year, an AH→CE conversion difference, or an approximate birth year.
- **Disputed among sources:** the standard references disagree, and the book follows one of the versions.
- **Inconsistent:** no source I checked supports the book's date, confirmed with at least two sources.
- **N/A:** the row gives no date.

## Summary counts (155 rows)

| Verdict | Rows |
|---|---|
| Consistent | 113 |
| Minor difference | 12 |
| Inconsistent | 11 (9 distinct people; Ibn Ishaq is counted twice, rows 3 and 121) |
| Disputed among sources | 5 |
| OCR issue | 4 |
| Unverified | 9 |
| N/A (no date given) | 1 |

## 1. Results table

| # | Name | Book's dates (page) | Verdict | Reference dates | Source URL(s) |
|---|---|---|---|---|---|
| 1 | Kemal Ataturk | 1881-1938 CE (p. 110) | **Consistent** | b. 19 May 1881, d. 10 Nov 1938 (GND; BnF 1881-1938). Life dates fine, BUT the same sentence says he abolished the Caliphate in 1922: the sultanate was abolished 1 Nov 1922, the caliphate on 3 Mar 1924 (Wikipedia, 'Abolition of the Caliphate'). | https://lobid.org/gnd/118650793.json<br>https://data.bnf.fr/ark:/12148/cb12055367s<br>https://www.wikidata.org/wiki/Q5152<br>https://en.wikipedia.org/wiki/Abolition_of_the_Ottoman_Caliphate |
| 2 | Wilhem [sic] von Pressel | 'circa 1876' observation (p. 111) | **Consistent** | Wilhelm Pressel, 28 Oct 1821 - 16 May 1902; GND: 1872 director-general of the Ottoman railways, originator of the Baghdad Railway. c. 1876 falls within his life. | https://lobid.org/gnd/13923473X.json<br>https://www.wikidata.org/wiki/Q2807815 |
| 3 | Ibn Ishaq | 704-761/770 CE (p. 112) | **Inconsistent** | Birth 704 OK (GND 704; BnF 704?; TDV gives 80/699 after al-Dhahabi). Death: 151/768 (TDV; GND 768) or 150/767 (TDV variant; BnF 767?); TDV also lists minority variants 153/770 and 154/771. '761' is not attested in any source checked; the book omits the standard 767/768. | https://islamansiklopedisi.org.tr/ibn-ishak<br>https://lobid.org/gnd/118976850.json<br>https://data.bnf.fr/ark:/12148/cb12172761p<br>https://www.wikidata.org/wiki/Q334847 |
| 4 | 'Umar | r. 634-644 CE (p. 114) | **Consistent** | Second caliph 634-644, d. 23/644 (TDV; GND 'Zweiter Kalif (634-644)'). | https://islamansiklopedisi.org.tr/omer<br>https://lobid.org/gnd/118822810.json<br>https://www.wikidata.org/wiki/Q8467 |
| 5 | al-Hadi (Yahya b. al-Husayn), first Zaydi imam of Yemen | r. 897-911 CE (p. 114) | **Consistent** | Received allegiance at Sa'da 6 Safar 284 / 15 Mar 897; d. 298/911 (TDV). Wikidata: imam 897-911. | https://islamansiklopedisi.org.tr/hadi-ilelhak-yahya-b-huseyin<br>https://www.wikidata.org/wiki/Q2745413 |
| 6 | Yusuf ibn Ya'qub ibn al-Mujawir | 13th century CE (p. 114) | **Consistent** | d. after 630/1233 (TDV); GND 1204-1291. | https://islamansiklopedisi.org.tr/ibnul-mucavir<br>https://lobid.org/gnd/1089716648.json<br>https://www.wikidata.org/wiki/Q6534479 |
| 7 | Philip Khuri Hitti | 1886-1978 CE (p. 114) | **Consistent** | 22 Jun 1886 - 24 Dec 1978 (BnF 1886-1978; GND 1886-1978). | https://data.bnf.fr/ark:/12148/cb12183272d<br>https://lobid.org/gnd/11886369X.json<br>https://www.wikidata.org/wiki/Q554718 |
| 8 | 'Abd Allah ibn Abi Bakr | 1st half of 7th c. CE (p. 114) | **Consistent** | d. 11/632-33 (TDV). | https://islamansiklopedisi.org.tr/abdullah-b-ebu-bekir<br>https://www.wikidata.org/wiki/Q4666109 |
| 9 | Abu Hurayrah | 603-681 CE (p. 115) | **Inconsistent** | Death: 58/678 at about 78; also reported 57/677 or 59/679 (TDV). BnF 601?-677?; GND 602-679. No source gives 681. Birth c. 601-603 is fine. | https://islamansiklopedisi.org.tr/ebu-hureyre<br>https://data.bnf.fr/ark:/12148/cb16245619f<br>https://lobid.org/gnd/118966863.json<br>https://www.wikidata.org/wiki/Q69326 |
| 10 | Mu'awiyah ibn Abi Sufyan | 602-680 CE (p. 115); d. 680 (p. 116, twice) | **Consistent** | b. 602 or 603 in Mecca, d. 60/680 (TDV); BnF 603?-680; GND 605-680. | https://islamansiklopedisi.org.tr/muaviye-b-ebu-sufyan<br>https://data.bnf.fr/ark:/12148/cb13555700m<br>https://lobid.org/gnd/119217481.json<br>https://www.wikidata.org/wiki/Q181154 |
| 11 | Ja'far ibn Abi Talib | exile 616 CE; return 626 CE (p. 116) | **Inconsistent** | Exile 616 OK (Wikipedia: joined the second emigration in 616). Return: he came back from Abyssinia and reached the Prophet at Khaybar just after its conquest (TDV), and Khaybar was in year 7/628 (TDV 'Hayber'); Wikipedia: left Abyssinia summer 628. Return was 628, not 626. d. 8/629 (TDV). | https://islamansiklopedisi.org.tr/cafer-b-ebu-talib<br>https://islamansiklopedisi.org.tr/hayber<br>https://en.wikipedia.org/wiki/Ja%27far_ibn_Abi_Talib |
| 12 | al-Nawawi | 1234-1278 CE (p. 116) | **Minor difference** | b. 631/1234 (TDV); d. 676/1277 (TDV; BnF 1233-1277). GND 1233-1278. 676 AH runs Jun 1277-May 1278, so 1278 is a conversion-level difference. | https://islamansiklopedisi.org.tr/nevevi<br>https://data.bnf.fr/ark:/12148/cb11917471c<br>https://lobid.org/gnd/119158523.json |
| 13 | Fakhr al-Din al-Razi | 1149-1209 CE (p. 118) | **Minor difference** | b. 25 Ramadan 543 / 6 Feb 1149 (TDV; 544 also reported); d. 606/1210 (TDV); BnF 1150-1210; GND 1149-1210. 606 AH spans 1209-1210. | https://islamansiklopedisi.org.tr/fahreddin-er-razi<br>https://data.bnf.fr/ark:/12148/cb12086410z<br>https://lobid.org/gnd/118749390.json |
| 14 | Claude Cahen | 1909-1991 CE (p. 119) | **Consistent** | 26 Feb 1909 - 18 Nov 1991 (GND; BnF). | https://lobid.org/gnd/12238704X.json<br>https://data.bnf.fr/ark:/12148/cb118947771 |
| 15 | Louis Massignon | 1883-1962 CE (p. 119) | **Consistent** | 25 Jul 1883 - 31 Oct 1962 (GND; BnF). | https://lobid.org/gnd/118782460.json<br>https://data.bnf.fr/ark:/12148/cb11914994p |
| 16 | Ibn Sa'd | d. 845 CE (p. 120) | **Consistent** | d. 230/845 (TDV); GND 784-845; BnF 784?-845. | https://islamansiklopedisi.org.tr/ibn-sad<br>https://lobid.org/gnd/119181118.json<br>https://data.bnf.fr/ark:/12148/cb13539440k |
| 17 | Baladhuri | d. c. 892 CE (p. 120) | **Consistent** | d. 279/892-93 (TDV); GND d. 892; BnF 08..-0892. | https://islamansiklopedisi.org.tr/belazuri<br>https://lobid.org/gnd/119312360.json<br>https://data.bnf.fr/ark:/12148/cb12987833h |
| 18 | Moshe Gil | b. 1921 CE (p. 120) | **Consistent** | b. 8 Feb 1921 (Wikidata); GND 1921-2014; BnF 1921-2014 (he died in 2014, after the book appeared). | https://lobid.org/gnd/138330840.json<br>https://data.bnf.fr/ark:/12148/cb122531313<br>https://www.wikidata.org/wiki/Q2904684 |
| 19 | Imam 'Ali al-Rida | 765-818 CE (p. 122) | **Disputed among sources** | Death 203/818 agreed (TDV; BnF). Birth: TDV 'most probably 153/770', with 148/765 or 151/768 also reported; BnF 765?-818 (= book); GND 770-817; Wikidata 770. Book follows the 148/765 version. | https://islamansiklopedisi.org.tr/ali-er-riza<br>https://data.bnf.fr/ark:/12148/cb16956831h<br>https://lobid.org/gnd/102415293.json |
| 20 | Muhammad al-Shaybani | 749/50-805 CE (p. 124) | **Consistent** | b. 132/749-50 at Wasit, d. 189/805 (TDV); GND 749-805; BnF 750?-804?. | https://islamansiklopedisi.org.tr/seybani-muhammed-b-hasan<br>https://lobid.org/gnd/119171716.json<br>https://data.bnf.fr/ark:/12148/cb12990402n |
| 21 | Muhammad ibn Ahmad al-Sarakhsi | d. c. 1096 CE (p. 124) | **Disputed among sources** | TDV: biographical works generally give 483/1090-91; some say vaguely 'around [4]90' or 'around 500'. GND d. 1090; BnF 1009-1090; Wikidata 1090 (TDV) / 1097 / 1096 (deprecated). Book follows the minority 'c. 490/1096-97' version. | https://islamansiklopedisi.org.tr/serahsi-semsuleimme<br>https://lobid.org/gnd/119336588.json<br>https://data.bnf.fr/ark:/12148/cb10715274w<br>https://www.wikidata.org/wiki/Q579171 |
| 22 | Abu Hanifah | 699-767 CE (p. 124) | **Consistent** | b. 80/699 Kufa, d. 150/767 (TDV); GND and BnF 699-767. | https://islamansiklopedisi.org.tr/ebu-hanife<br>https://lobid.org/gnd/11899204X.json<br>https://data.bnf.fr/ark:/12148/cb14559823n |
| 23 | Abu Yusuf | d. 798 CE (p. 124) | **Consistent** | d. 182/798 (TDV); GND and BnF 731-798. | https://islamansiklopedisi.org.tr/ebu-yusuf<br>https://lobid.org/gnd/118925873.json<br>https://data.bnf.fr/ark:/12148/cb11166383h |
| 24 | 'Allamah Majlisi (Muhammad Baqir) | 1616-1689 CE (p. 124) | **Inconsistent** | b. 1037/1627 in Isfahan; d. 1110/1698-99 or 1111/1699-1700 (TDV). GND 1627-1698; Wikidata c. 1627-1698/1700. Both ends about 11 years too early. | https://islamansiklopedisi.org.tr/meclisi-muhammed-bakir<br>https://lobid.org/gnd/119147459.json<br>https://www.wikidata.org/wiki/Q755939 |
| 25 | 'Abdul 'Ahad Dawud (David Benjamin Keldani) | 1867-c. 1940 CE (p. 124) | **Consistent** | 1867-1940 (GND: born Digala, Urmia; former priest who became Muslim); Wikidata death 'circa' 1940. | https://lobid.org/gnd/124465420.json<br>https://www.wikidata.org/wiki/Q719343 |
| 26 | Ahmed Deedat | 1918-2005 CE (p. 124) | **Consistent** | 1 Jul 1918 - 8 Aug 2005 (GND; BnF 1918-2005). | https://lobid.org/gnd/1033452173.json<br>https://data.bnf.fr/ark:/12148/cb125744077 |
| 27 | Abraham Isaac Katsh | c. 1908-1998 CE (p. 124) | **Consistent** | 10 Aug 1908 - 21 Jul 1998 (Wikidata, citing BnF/GND); BnF 1908-1998. | https://data.bnf.fr/ark:/12148/cb158257254<br>https://www.wikidata.org/wiki/Q30053249 |
| 28 | Leopold Weiss (Muhammad Asad) | 1900-1992 CE (p. 125) | **Consistent** | 2 Jul 1900 - 20 Feb 1992 (GND; BnF 1900-1992). | https://lobid.org/gnd/119060116.json<br>https://data.bnf.fr/ark:/12148/cb12586449v |
| 29 | Lev Nussimbaum ('Nussi mbaum', OCR of name) | 1905-1942 CE (p. 125) | **Consistent** | 20 Oct 1905 - 27 Aug 1942 (GND, as 'Essad Bey'; BnF 1905-1942). | https://lobid.org/gnd/119131609.json<br>https://data.bnf.fr/ark:/12148/cb12466084p |
| 30 | Maryam Jameelah | 1934-2012 CE (p. 125) | **Consistent** | 23 May 1934 - 31 Oct 2012 (GND). | https://lobid.org/gnd/1024812677.json<br>https://www.wikidata.org/wiki/Q3696204 |
| 31 | Michael Wolfe | b. 1945 CE (p. 125) | **Consistent** | b. 3 Apr 1945 (GND 1059445603: 'converted to Islam and took the name Abdul Majid'). | https://lobid.org/gnd/1059445603.json |
| 32 | Samuel L. Lewis | 1896-1971 CE (p. 125) | **Consistent** | 18 Oct 1896 - 15 Jan 1971 (GND). | https://lobid.org/gnd/1164196057.json |
| 33 | Tali Fahima | b. 1976 (p. 125) | **Consistent** | b. 8 Feb 1976 (Wikidata, whose only reference is Arabic Wikipedia; Wikipedia-level source, modern uncontroversial date). | https://www.wikidata.org/wiki/Q2916037 |
| 34 | Mark W. Walton (date placement ambiguous) | b. 1949 CE (p. 128) | **Consistent** | GND: Walton, Mark W., b. 1949; Nafziger, George F., b. 1 Mar 1949. The date is right for either co-author. | https://lobid.org/gnd/1146626010.json<br>https://lobid.org/gnd/124265839.json |
| 35 | Karen Armstrong | b. 1944 (p. 128) | **Consistent** | b. 14 Nov 1944 (GND). | https://lobid.org/gnd/119304791.json |
| 36 | Muhammad Taqi Majlisi | 'in the 17th century' (p. 128) | **Consistent** | d. 1070/1659 (TDV). | https://islamansiklopedisi.org.tr/meclisi-muhammed-taki |
| 37 | Fred Donner | b. 1945 (p. 128) | **Consistent** | b. 1945 (GND); 30 Sep 1945 (Wikidata). | https://lobid.org/gnd/141164719.json<br>https://www.wikidata.org/wiki/Q680793 |
| 38 | Abu Dharr al-Ghifari | d. 652 CE (p. 129) | **Consistent** | d. Dhu l-Hijja 32 / Jul 653 at al-Rabadha (TDV); BnF d. 652. 32 AH spans 652-653. | https://islamansiklopedisi.org.tr/ebu-zer-el-gifari<br>https://data.bnf.fr/ark:/12148/cb12273901s<br>https://www.wikidata.org/wiki/Q1029610 |
| 39 | John ibn Hawai (Jawn b. Huway) | martyred at Karbala 680 CE (p. 129) | **Consistent** | Martyred on 'Ashura 61/680 at Karbala (WikiShia, a Shi'i reference wiki; not peer-reviewed). | https://en.wikishia.net/view/Jawn_b._Huway |
| 40 | Khalid ibn al-Walid | 592-642 CE (p. 134) | **Inconsistent** | Death 21/642 OK (TDV; GND 642). Birth: '35-39 years before the Hijra (583-587)' (TDV); Wikidata 586. No reliable source found for 592. Birth is approximate, so this is a low-significance error. | https://islamansiklopedisi.org.tr/halid-b-velid<br>https://lobid.org/gnd/118896083.json<br>https://www.wikidata.org/wiki/Q26918 |
| 41 | Jean de Thevenot | '(!633-1667 CE)' (p. 135) | **OCR issue** | Reads 1633-1667: 16 Jun 1633 - 28 Nov 1667 (GND; BnF 1633-1667). Travels 1655-1663 fall within his life. | https://lobid.org/gnd/121201708.json<br>https://data.bnf.fr/ark:/12148/cb11926390b |
| 42 | Muhammad Hamidullah | reprinted the covenant in 1956 (p. 138) | **Consistent** | 19 Feb 1908 - 17 Dec 2002 (GND; BnF), so 1956 falls in his lifetime (the edition date itself was not checked). | https://lobid.org/gnd/10360572X.json<br>https://data.bnf.fr/ark:/12148/cb120009676 |
| 43 | Muhammad 'Amarah | reprinted the covenant in 2002 (p. 138) | **Consistent** | 8 Dec 1931 - 2020 (GND; BnF 1931-2020). | https://lobid.org/gnd/124614531.json<br>https://data.bnf.fr/ark:/12148/cb15550355v |
| 44 | Pacifique de Provins (Pacificus Scaliger) | 1588-1648 CE; d. 1648; born 1588 (pp. 139-152) | **Consistent** | BnF heading 'Pacifique de Provins (capucin, 1588-1648)'; Wikidata 1588 - May 1648. | https://data.bnf.fr/ark:/12148/cb10742253t<br>https://www.wikidata.org/wiki/Q3360218 |
| 45 | Berthold (founder of the Carmelites) | died in 1188 (p. 139) | **Inconsistent** | d. c. 1195: Store norske leksikon 'Dod 1195 (approximate year of death)'; Wikipedia 'died 1195' (founded the Mount Carmel hermit colony in 1185); Wikidata 1195 (SNL, fr.wiki) or 1198 (hu.wiki). | https://snl.no/Berthold_av_Calabria<br>https://en.wikipedia.org/wiki/Berthold_of_Calabria<br>https://www.wikidata.org/wiki/Q828129 |
| 46 | Sir Paul Ricaut (Rycaut) | 1629-1700 CE (pp. 140-161) | **Minor difference** | BnF 1628-1700; GND 1628-1700; Wikidata also has b. 23 Dec 1629 (unreferenced) and d. 16 Nov 1700 (BnF). | https://data.bnf.fr/ark:/12148/cb12636782n<br>https://lobid.org/gnd/118894803.json<br>https://www.wikidata.org/wiki/Q3372144 |
| 47 | Sultan Ibrahim I | ruled 1640-1648 CE (p. 141) | **Consistent** | GND: took the throne Feb 1640 after Murad IV; deposed Aug 1648; 1615-1648. | https://lobid.org/gnd/129287660.json<br>https://www.wikidata.org/wiki/Q168776 |
| 48 | Sultan Murad IV | r. 1623-1640 CE (p. 142) | **Consistent** | Ottoman sultan 1623-1640, d. 1049/1640; b. 27 Jul 1612 (TDV); BnF 1612-1640. | https://islamansiklopedisi.org.tr/murad-iv<br>https://lobid.org/gnd/118585797.json<br>https://data.bnf.fr/ark:/12148/cb16945226t |
| 49 | Gabriel Sionita | 1577-1648 CE (pp. 142-145) | **Consistent** | BnF 1577-1648; GND 1577-1648. | https://data.bnf.fr/ark:/12148/cb106355968<br>https://lobid.org/gnd/104043857.json |
| 50 | Eusebe Renaudot | 1646-1720 CE (p. 145); '16461720' (OCR, p. 153) | **Consistent** | 20 Jul 1646 - Sep 1720 (GND; BnF 1646-1720). The p. 153 form is an OCR join. | https://lobid.org/gnd/11908760X.json<br>https://data.bnf.fr/ark:/12148/cb119976242 |
| 51 | Johann Michael Vansleb (Wansleben) | 1635-1676 CE (p. 145) | **Inconsistent** | b. 1 Nov 1635, d. 12 Jun 1679 (GND); BnF 'Johann Michael Wansleben (1635-1679)'. Death year is wrong by 3 years. | https://lobid.org/gnd/124386474.json<br>https://data.bnf.fr/ark:/12148/cb107038605<br>https://www.wikidata.org/wiki/Q3180611 |
| 52 | Johann Georg Nissel | 1621-1662 (p. 146) | **Consistent** | d. 1662 (GND; BnF '16..-1662'); b. 1621 (Wikidata citing Early Modern Letters Online) or 1623 (Wikidata citing ECARTICO). | https://lobid.org/gnd/121226646.json<br>https://data.bnf.fr/ark:/12148/cb11997022q<br>https://www.wikidata.org/wiki/Q55125772 |
| 53 | Mu'awiyah ibn Abi Sufyan (ch. 5) | d. 680 CE; embraced Islam before the conquest of Mecca, 8 AH/630 CE (p. 147) | **Consistent** | d. 60/680; became Muslim with his father 'during the conquest' (of Mecca, 8/630), then served as the Prophet's scribe (TDV). (TDV says 'during', the book 'before'. Same year.) | https://islamansiklopedisi.org.tr/muaviye-b-ebu-sufyan<br>https://www.wikidata.org/wiki/Q181154 |
| 54 | Imam 'Ali | d. 661 CE (pp. 147, 160) | **Consistent** | d. 40/661; caliph 656-661 (TDV); BnF 596?-661; GND 600-661. | https://islamansiklopedisi.org.tr/ali<br>https://data.bnf.fr/ark:/12148/cb13518682d<br>https://lobid.org/gnd/118846582.json |
| 55 | al-Mada'ini | d. 225/840 (p. 147) | **Consistent** | TDV: 'according to most sources 225 (840)'; variants: Ibn al-Nadim 215/830; al-Raba'i and al-Yafi'i Dhu l-Qa'da 224/Sep 839; al-Tabari 228/843; Ibn Taghribirdi 231/845-46. GND and Wikidata use 843. | https://islamansiklopedisi.org.tr/medaini<br>https://lobid.org/gnd/1051901189.json |
| 56 | Selim I | r. 1512-1520 CE (pp. 147-148) | **Consistent** | Ottoman sultan 1512-1520, d. 926/1520 (TDV); GND 'regierte ab 1512', d. 1520. | https://islamansiklopedisi.org.tr/selim-i<br>https://lobid.org/gnd/122789148.json |
| 57 | Sulayman the Magnificent | r. 1520-1566 CE (pp. 148, 175) | **Consistent** | Sultan 1520-1566, d. 974/1566; b. 6 Nov 1494 (TDV); GND 'regierte 1520-1566'. | https://islamansiklopedisi.org.tr/suleyman-i<br>https://lobid.org/gnd/118619993.json |
| 58 | Francis I of France | r. 1515-1547 CE (pp. 145-149) | **Consistent** | King from 1515, d. 31 Mar 1547 (GND); Wikidata King of France 1515 - 31 Mar 1547. | https://lobid.org/gnd/118534947.json<br>https://www.wikidata.org/wiki/Q129857 |
| 59 | Henri II | r. 1547-1559 CE (p. 149) | **Consistent** | King from 1547, d. 10 Jul 1559 (GND); Wikidata 1547-1559. | https://lobid.org/gnd/118548166.json<br>https://www.wikidata.org/wiki/Q132545 |
| 60 | Guillaume Postel | 1510-1581 CE (p. 149) | **Consistent** | 25 Mar 1510 - 6 Sep 1581 (GND; BnF). | https://lobid.org/gnd/118793004.json<br>https://data.bnf.fr/ark:/12148/cb12078540f |
| 61 | Jean Bodin | 1530-1596 CE (p. 149) | **Consistent** | BnF 1530-1596; GND 1529-1596. | https://data.bnf.fr/ark:/12148/cb119999518<br>https://lobid.org/gnd/118512307.json |
| 62 | Sultan Ahmed I | r. 1603-1617 CE (p. 149) | **Consistent** | Sultan 1603-1617, d. 1026/1617 (TDV); GND 1590-1617, 'ab 1603 Sultan'. | https://islamansiklopedisi.org.tr/ahmed-i<br>https://lobid.org/gnd/11850116X.json |
| 63 | Henri IV | r. 1589-1610 CE (pp. 149, 150) | **Consistent** | Wikidata: King of France 2 Aug 1589 - 14 May 1610; GND d. 14 May 1610. | https://www.wikidata.org/wiki/Q936976<br>https://lobid.org/gnd/118548174.json |
| 64 | Francois Savary de Breves | 1560-1627 CE (pp. 143-150) | **Minor difference** | BnF '1560-1628' (Wikidata, citing BnF: d. 22 Apr 1628); GND 1560-1628. Death year one year off. | https://data.bnf.fr/ark:/12148/cb13010901m<br>https://lobid.org/gnd/124447163.json<br>https://www.wikidata.org/wiki/Q527333 |
| 65 | Andre Du Ryer | c. 1580-1660 CE ('15801660', OCR, p. 150) | **Disputed among sources** | GND 1580-1660 (= book); BnF '15..-1688?'; Wikidata 1580-1660 (GND) and d. 1688 (LIBRIS). | https://lobid.org/gnd/128963220.json<br>https://data.bnf.fr/ark:/12148/cb12507577z<br>https://www.wikidata.org/wiki/Q2847689 |
| 66 | Claudius Salmasius (Claude de Saumaise) | d. 1653 (p. 150); '1588 or 1596-1653' (p. 152) | **Minor difference** | b. 15 Apr 1588, d. 3 Sep 1653 (GND; BnF 1588-1653). No source checked gives 1596, so the alternative birth year is unsupported. | https://lobid.org/gnd/119114119.json<br>https://data.bnf.fr/ark:/12148/cb12003602h |
| 67 | Abraham Hinckelmann | 1652-1695 CE ('16521695', OCR) | **OCR issue** | 2 May 1652 - 11 Feb 1695 (GND). | https://lobid.org/gnd/11689704X.json<br>https://www.wikidata.org/wiki/Q85503 |
| 68 | Francois Ravaillac | 1578-1610 CE (p. 150) | **Consistent** | BnF 1578?-1610; GND 1578 - executed 27 May 1610. | https://data.bnf.fr/ark:/12148/cb12130888p<br>https://lobid.org/gnd/118904299.json |
| 69 | Layard ('Henri Layard') | 1817-1894 CE (pp. 151-156) | **Consistent** | Austen Henry Layard, 5 Mar 1817 - 5 Jul 1894 (GND; BnF). | https://lobid.org/gnd/118570390.json<br>https://data.bnf.fr/ark:/12148/cb124515254 |
| 70 | Gregory Bar Hebraeus | 1226-1286 CE; 13th c. (p. 151) | **Consistent** | d. 685/1286 (TDV); BnF and GND 1226-1286. | https://islamansiklopedisi.org.tr/ibnul-ibri<br>https://data.bnf.fr/ark:/12148/cb12024654d<br>https://lobid.org/gnd/118652508.json |
| 71 | Edward Rehatsek | 1819-1891 CE (pp. 141, 151) | **Consistent** | 3 Jul 1819 - 11 Dec 1891 (GND). | https://lobid.org/gnd/141743999.json |
| 72 | Matthaei Amrus ('Amr ibn Matta) | 'lived in the 14th century' (p. 152) | **Consistent** | Wikipedia and Wikidata: '14th-century Syriac Christian author'; Wikipedia says his work is discussed by Ibn Kabar (d. 1324). Only Wikipedia-level sources found, no peer-reviewed confirmation. | https://en.wikipedia.org/wiki/Amr_ibn_Matta<br>https://www.wikidata.org/wiki/Q22935918 |
| 73 | The Prophet Muhammad | 570-632 CE (p. 152) | **Consistent** | GND 570-632; BnF '057.-0632'; Wikidata c. 570/571 - 8 Jun 632. | https://lobid.org/gnd/118583158.json<br>https://data.bnf.fr/ark:/12148/cb12085994z<br>https://www.wikidata.org/wiki/Q9458 |
| 74 | Jacobo Nagy de Harsany (Harsanyi Nagy Jakab) | b. 1615 CE (pp. 152-153) | **Consistent** | BnF 'Jakab Harsanyi Nagy (1615-1677?)'; Wikidata 1615-1676. | https://data.bnf.fr/ark:/12148/cb12917900c<br>https://www.wikidata.org/wiki/Q20480593 |
| 75 | Pierre Bayle | 1647-1706 CE (pp. 153, 156) | **Consistent** | 18 Nov 1647 - 28 Dec 1706 (GND; BnF). | https://lobid.org/gnd/11850777X.json<br>https://data.bnf.fr/ark:/12148/cb119867257 |
| 76 | Pedro de Madrazo | 1816-1898 CE (p. 153) | **Consistent** | b. 11 Oct 1816; d. Aug 1898 (GND 30 Aug; Wikidata 20 Aug, citing the Diccionario Biografico Espanol). | https://lobid.org/gnd/116655305.json<br>https://www.wikidata.org/wiki/Q3898728 |
| 77 | James Thayer Addison | 1887-1953 CE (p. 153) | **Consistent** | GND 1887-1953. | https://lobid.org/gnd/1074684699.json |
| 78 | Simon Bolivar | 1783-1830 CE (p. 155) | **Consistent** | 24 Jul 1783 - 17 Dec 1830 (GND; BnF). | https://lobid.org/gnd/118513052.json<br>https://data.bnf.fr/ark:/12148/cb118926507 |
| 79 | Jose Marti | 1853-1895 CE (p. 155) | **Consistent** | 28 Jan 1853 - 19 May 1895 (GND; BnF). | https://lobid.org/gnd/118578235.json<br>https://data.bnf.fr/ark:/12148/cb120206475 |
| 80 | Johann Heinrich Hottinger | 1620-1667 CE (p. 156) | **Consistent** | 10 Mar 1620 - 5 Jun 1667 (GND; BnF). | https://lobid.org/gnd/104286547.json<br>https://data.bnf.fr/ark:/12148/cb17733052x |
| 81 | Hugo Grotius | 1583-1645 CE (p. 156) | **Consistent** | 10 Apr 1583 - 28 Aug 1645 (GND; BnF). | https://lobid.org/gnd/118542702.json<br>https://data.bnf.fr/ark:/12148/cb119854851 |
| 82 | Gisbertus Voetius | 1589-1676 CE (p. 156) | **Consistent** | 3 Mar 1589 - 1 Nov 1676 (GND; BnF). | https://lobid.org/gnd/11890261X.json<br>https://data.bnf.fr/ark:/12148/cb130137473 |
| 83 | Johannes Hoornbeek | 1617-1666 CE (p. 156) | **Consistent** | 4 Nov 1617 - 1 Sep 1666 (GND; BnF). | https://lobid.org/gnd/123625505.json<br>https://data.bnf.fr/ark:/12148/cb14329024t |
| 84 | Dean Humphrey Prideaux | 1648-1724 CE (p. 156) | **Consistent** | GND 1648-1724; BnF 1648-1724. | https://lobid.org/gnd/124436579.json<br>https://data.bnf.fr/ark:/12148/cb122243438 |
| 85 | Ignaz von Dollinger | 1799-1890 CE (p. 156) | **Consistent** | 28 Feb 1799 - 10 Jan 1890 (GND; BnF). | https://lobid.org/gnd/118526243.json<br>https://data.bnf.fr/ark:/12148/cb12159364w |
| 86 | Johann Lorenz von Mosheim | 1693-1755 CE (p. 156) | **Consistent** | 9 Oct 1693 - 9 Sep 1755 (GND; BnF 1693-1755). Wikidata also records 1694, citing Britannica. | https://lobid.org/gnd/118737147.json<br>https://data.bnf.fr/ark:/12148/cb13541523j<br>https://www.wikidata.org/wiki/Q65260 |
| 87 | Abu Dawud | d. 889 CE (p. 157) | **Consistent** | d. 275/889 (TDV); GND 817-889. | https://islamansiklopedisi.org.tr/ebu-davud-es-sicistani<br>https://lobid.org/gnd/119462575.json |
| 88 | al-Tabari | d. 923 CE (p. 157) | **Consistent** | d. 310/923 (TDV); GND 839-923; BnF 839?-923. | https://islamansiklopedisi.org.tr/taberi-muhammed-b-cerir<br>https://lobid.org/gnd/118620436.json<br>https://data.bnf.fr/ark:/12148/cb11925884j |
| 89 | Johann Karl Ludwig Gieseler | 1792-1854 CE (p. 158) | **Consistent** | 3 Mar 1792 - 8 Jul 1854 (GND; BnF). | https://lobid.org/gnd/100286097.json<br>https://data.bnf.fr/ark:/12148/cb10651159d |
| 90 | Henri Basnage de Beauval | 1657-1710 CE (pp. 158-159) | **Disputed among sources** | BnF heading 1657-1710 (= book); GND 1656-1710; Wikidata 7 Aug 1656 - Apr 1710, citing BnF. | https://data.bnf.fr/ark:/12148/cb11983683d<br>https://lobid.org/gnd/12053827X.json<br>https://www.wikidata.org/wiki/Q3130625 |
| 91 | Sir Travers Twiss | 1809-1897 CE ('18091897', OCR) (p. 159) | **OCR issue** | 19 Mar 1809 - 14 Jan 1897 (GND; BnF 1809-1897). | https://lobid.org/gnd/128768800.json<br>https://data.bnf.fr/ark:/12148/cb12314495r |
| 92 | Murad III | 1546-1595; 'time of Murad III, in 1587/1588' (pp. 149, 159) | **Consistent** | Sultan 1574-1595, d. 1003/1595 (TDV); BnF and GND 1546-1595. | https://islamansiklopedisi.org.tr/murad-iii<br>https://data.bnf.fr/ark:/12148/cb16926407x<br>https://lobid.org/gnd/119524767.json |
| 93 | Queen Elizabeth of England | 1533-1603 CE (p. 159) | **Consistent** | 7 Sep 1533 - 24 Mar 1603 (GND; BnF). | https://lobid.org/gnd/118529870.json<br>https://data.bnf.fr/ark:/12148/cb12026274d |
| 94 | Giovanni Paolo Marana | 1642-1693 CE (p. 160) | **Consistent** | BnF 1642?-1693; GND 1642-1693. | https://data.bnf.fr/ark:/12148/cb12207211p<br>https://lobid.org/gnd/119080370.json |
| 95 | Yeshu'yab II (Ishoyahb II) | 'at the time of the Arab conquest' (pp. 139, 151-156) | **Consistent** | Patriarch 628-645 (Wikipedia list); GND 'active 628-646'. | https://en.wikipedia.org/wiki/List_of_patriarchs_of_the_Church_of_the_East<br>https://lobid.org/gnd/1011380900.json |
| 96 | Sieur Foret (Jean de La Foret) | 1536 (p. 145) | **Consistent** | First French ambassador to the Porte 1534-1537; d. 1537 (Wikidata). | https://www.wikidata.org/wiki/Q926393 |
| 97 | Barbarossa (Hayreddin) | wintered in Toulon 1543-1544 CE (p. 148) | **Consistent** | Ottoman wintering in Toulon: winter 1543-44 (Wikipedia); Barbarossa d. 953/1546 (TDV); BnF 1476?-1546. | https://en.wikipedia.org/wiki/Ottoman_wintering_in_Toulon<br>https://islamansiklopedisi.org.tr/barbaros-hayreddin-pasa<br>https://data.bnf.fr/ark:/12148/cb12653029z |
| 98 | Pope Julius II | patron of the 1514 Fano printing (p. 150) | **Minor difference** | Pope 1503 - d. 21 Feb 1513 (GND 1443-1513; BnF; Wikidata). He was dead before 1514. Wikipedia: some sources credit the Fano Arabic press to Julius II, and others think the book was printed in Venice. 'Patron of the press' is possible, 'patron of the 1514 printing' is not. | https://lobid.org/gnd/118714090.json<br>https://data.bnf.fr/ark:/12148/cb119549219<br>https://www.wikidata.org/wiki/Q80516<br>https://en.wikipedia.org/wiki/Kitab_Salat_as-Sawai |
| 99 | Paganino and Alessandro Paganini | 1537/1538 (p. 149) | **Consistent** | Paganino d. 1538 (BnF '14..-1538'); Alessandro active 1509-1538 (GND). | https://data.bnf.fr/ark:/12148/cb135362947<br>https://lobid.org/gnd/1037599683.json |
| 100 | Girgis al-Ifrangi | 1538 (1254 of the Martyrs) (pp. 144, 175) | **Unverified** | Known only from the manuscript (BnF MS Arabe 214). No authority record found in Wikidata or GND. | (none found; see section 4) |
| 101 | Mansur ibn Sulayman Sahyun al-Ramadi | reading mark 1620 CE (p. 145) | **Unverified** | Known only from a reader's note in the manuscript. No authority record found. | (none found; see section 4) |
| 102 | Butrus ibn Diyab al-Halabi | reading mark 1673 CE (p. 145) | **Unverified** | Known only from a reader's note in the manuscript. No authority record found. | (none found; see section 4) |
| 103 | Pope Gregory XV | met Scaliger in 1623 (p. 141) | **Consistent** | Pope 9 Feb 1621 - d. 8 Jul 1623 (GND; Wikidata), so the meeting must be before July 1623. | https://lobid.org/gnd/118697404.json<br>https://www.wikidata.org/wiki/Q132692 |
| 104 | Francois Hotman (de 'Mar-fontaine') | c. 1629-1630 (pp. 142, 152) | **Consistent** | GND 126581290X: Francois Hotman, seigneur de Mortefontaine/Marfontaine, 1576-1636; 'conseiller clerc au Parlement' from 1597. Not the jurisconsult Francois Hotman (Wikidata Q561737). | https://lobid.org/gnd/126581290X.json<br>https://www.wikidata.org/wiki/Q139002127 |
| 105 | Antoine Vitray (Vitre) | 1630 (pp. 146, 149) | **Consistent** | BnF 1587?-1674; GND 1595-1674. | https://data.bnf.fr/ark:/12148/cb12353896s<br>https://lobid.org/gnd/104174978.json |
| 106 | Louis XIII | 1630 (p. 149) | **Consistent** | King of France 1610-1643 (Wikidata); GND 1601-1643. | https://www.wikidata.org/wiki/Q737533<br>https://lobid.org/gnd/11872942X.json |
| 107 | Valerianus Oserole | 1659 CE (p. 151) | **Unverified** | Known only from notes in a copy of Sionita's edition. No authority record found. | (none found; see section 4) |
| 108 | Ibrahim Muteferrika | founded the Ottoman press in 1726 (p. 148) | **Minor difference** | TDV: his treatise Vesiletu't-tibaa was written in 1726, and the ferman authorising the press was issued in early July 1727; d. 1160/1747. BnF 1670?-1747?. | https://islamansiklopedisi.org.tr/ibrahim-muteferrika<br>https://data.bnf.fr/ark:/12148/cb135457232 |
| 109 | Lefebvre de Villebrune | 1795 (pp. 144, 154-155) | **Consistent** | Jean-Baptiste Lefebvre de Villebrune, 1732 - 7 Oct 1809 (BnF; GND). | https://data.bnf.fr/ark:/12148/cb135464344<br>https://lobid.org/gnd/104237813.json |
| 110 | Citizen Gregoire; Mr. Legrand | 1795 (p. 155) | **Consistent** | Henri Gregoire 1750-1831 (BnF; GND); Wikidata: member of the Council of Five Hundred from Oct 1795. 'Mr. Legrand' could not be identified, so his part is unverified. | https://data.bnf.fr/ark:/12148/cb119058290<br>https://lobid.org/gnd/118718657.json<br>https://www.wikidata.org/wiki/Q561218 |
| 111 | M. Grassi (Alfio) | 1826 (pp. 153, 155) | **Minor difference** | Alfio Grassi 1766-1827 (BnF; GND). Dizionario Biografico degli Italiani: 'Charte turque ... I-II, Paris 1825'. A later printing dated 1826 was not checked. | https://www.treccani.it/enciclopedia/alfio-grassi_(Dizionario-Biografico)/<br>https://data.bnf.fr/ark:/12148/cb102720442<br>https://lobid.org/gnd/100487033.json |
| 112 | Alexandre de Miltitz | 1838 (p. 153) | **Consistent** | Alexander von Miltitz 1785-1843 (GND). | https://lobid.org/gnd/11704704X.json<br>https://www.wikidata.org/wiki/Q94893343 |
| 113 | Edward A. Van Dyke (Van Dyck) | 1881 (p. 154) | **Unverified** | GND record 'Van Dyck, Edward Abbott' has no dates; Wikidata item has no dates. VIAF and LoC pages could not be read (JavaScript or blocked). | https://lobid.org/gnd/1052800505.json<br>https://www.wikidata.org/wiki/Q111473359 |
| 114 | Baron de Slane | catalogue 1883-1895 (p. 144) | **Consistent** | William McGuckin de Slane, 1801-1878 (BnF; GND). Wikipedia's bibliography dates the BnF Catalogue des manuscrits arabes to 1883-1895, so it was published after his death. The book's dates are publication dates. | https://data.bnf.fr/ark:/12148/cb11913736q<br>https://lobid.org/gnd/117633860.json<br>https://en.wikipedia.org/wiki/William_McGuckin_de_Slane |
| 115 | M.J. Guillaume (James Guillaume) | 'writing in the early 20th century' (p. 155) | **Consistent** | 16 Feb 1844 - 20 Nov 1916 (GND; BnF), so early-20th-century work is possible. The publication dates of the Proces-verbaux were not checked. | https://lobid.org/gnd/116921625.json<br>https://data.bnf.fr/ark:/12148/cb125196815 |
| 116 | Jesus of Nazareth | 7-2 BCE to 30-36 CE (p. 184) | **Consistent** | Wikidata: b. c. 6-4 BC (preferred), 7 BC (Handbook of Biblical Chronology), 2 BC (Meier); d. 30 or 33. GND: 'ca. 1. Jh. v. Chr. bis 30'. The book's range covers the scholarly range. | https://www.wikidata.org/wiki/Q302<br>https://lobid.org/gnd/118557513.json |
| 117 | Salman the Persian | d. 654 CE (p. 178) | **Disputed among sources** | TDV: died at al-Mada'in at the end of 35 or start of 36 (656), 'though earlier or later dates are also given'; Wikidata 657 (Islamic encyclopaedic dictionary). 654 was not found in any source checked. | https://islamansiklopedisi.org.tr/selman-i-farisi<br>https://www.wikidata.org/wiki/Q557378 |
| 118 | Mu'awiyah ibn Abi Sufyan (ch. 6) | 602-680 CE; Islam 8 AH/630; scribe 630-632 (pp. 178, 183) | **Consistent** | As row 10/53: b. 602 or 603, d. 60/680; converted at the conquest of Mecca and then acted as the Prophet's scribe (TDV). | https://islamansiklopedisi.org.tr/muaviye-b-ebu-sufyan<br>https://www.wikidata.org/wiki/Q181154 |
| 119 | Prophet Muhammad | d. 632 implied (p. 183) | **Consistent** | As row 73 (GND 570-632; BnF '057.-0632'). | https://lobid.org/gnd/118583158.json<br>https://data.bnf.fr/ark:/12148/cb12085994z |
| 120 | al-Baladhuri | d. c. 892 CE (p. 183) | **Consistent** | As row 17: d. 279/892-93 (TDV). | https://islamansiklopedisi.org.tr/belazuri<br>https://lobid.org/gnd/119312360.json |
| 121 | Ibn Ishaq | '704-761/70 CE' (p. 188) | **Inconsistent** | As row 3: d. 150/767 or 151/768 (TDV; GND 768; BnF 767?); 770 is only a minority variant; 761 is unattested. | https://islamansiklopedisi.org.tr/ibn-ishak<br>https://lobid.org/gnd/118976850.json<br>https://data.bnf.fr/ark:/12148/cb12172761p |
| 122 | Al-Waqidi | '747823 CE' (p. 188) | **OCR issue** | Reads 747-823: d. 207/823 (TDV); GND and BnF 747-823. | https://islamansiklopedisi.org.tr/vakidi<br>https://lobid.org/gnd/102372179.json<br>https://data.bnf.fr/ark:/12148/cb15506017w |
| 123 | Ibn Hisham | d. 834 (p. 188) | **Minor difference** | TDV: d. 13 Rabi' II 218 / 8 May 833 (some sources 213/828). BnF '07..-0834?'; GND 767-834. 218 AH spans 833-834. | https://islamansiklopedisi.org.tr/ibn-hisam<br>https://data.bnf.fr/ark:/12148/cb11956088k<br>https://lobid.org/gnd/11855526X.json |
| 124 | Alfred Guillaume | 1888-1966 CE (p. 188) | **Minor difference** | b. 8 Nov 1888; d. 30 Nov 1965 (GND); BnF 1888-1965. Death year one year off. | https://lobid.org/gnd/1031157255.json<br>https://data.bnf.fr/ark:/12148/cb124240026 |
| 125 | Mehmet II | r. 1444-1446 and 1451-1481 CE (p. 187) | **Consistent** | Sultan 1444-1446, 1451-1481; d. 886/1481 (TDV); GND same. | https://islamansiklopedisi.org.tr/mehmed-ii<br>https://lobid.org/gnd/118583166.json |
| 126 | Selim I (ch. 6) | r. 1512-1520 CE; fl. 1517 (pp. 177-178) | **Consistent** | As row 56. | https://islamansiklopedisi.org.tr/selim-i |
| 127 | 'Shimon the fourth', patriarch | fl. 1517 (p. 177) | **Inconsistent** | Shemon IV was patriarch c. 1450 (or 1437) to 1497. In 1517 the patriarch was Shemon VI (1504-1538): Wikipedia list; Wikidata Shemon VI, citing Wilmshurst, Ecclesiastical Organisation of the Church of the East 1318-1913. Numbering of the Shemon patriarchs varies between lists, so this may be a numbering problem rather than a wrong person. | https://en.wikipedia.org/wiki/List_of_patriarchs_of_the_Church_of_the_East<br>https://www.wikidata.org/wiki/Q108169726 |
| 128 | Surma D'Bait Mar Shimun | 1883-1975 CE (pp. 179, 181) | **Consistent** | BnF 'Surma d'Bet Mar Shimoun (1883-1975)'; Wikidata 27 Jan 1883 - 7 Dec 1975. | https://data.bnf.fr/ark:/12148/cb155678105<br>https://www.wikidata.org/wiki/Q7646448 |
| 129 | Mar Shimun XXI Benyamin | (1887-1918 CE) (p. 181) | **Consistent** | Life dates: b. 1887 (Wikidata, from de.wiki; 1885 also recorded), d. 3 Mar 1918. He was patriarch 1 Mar 1903 - 3 Mar 1918, so the printed dates are life dates, not reign dates. | https://www.wikidata.org/wiki/Q968845 |
| 130 | Theodore D'Mar Shimun | 1906-2001 CE (p. 181) | **Unverified** | Not found in Wikidata, GND or Wikipedia (direct title). The VIAF autosuggest returned nothing usable. | (none found; see section 4) |
| 131 | Bedir (Badr) Khan Beg | c. 1800-1868 CE; leader 'around 1820'; died Damascus 1868 (pp. 181-182) | **Minor difference** | Wikipedia: b. 1803; Mir of Botan 1821-1847; moved to Damascus June 1868 and 'died a year after' (1869). Wikidata 1806-1869 (unreferenced). Death is one year off; birth is approximate. | https://en.wikipedia.org/wiki/Bedir_Khan_Beg<br>https://www.wikidata.org/wiki/Q735665 |
| 132 | Earl Percy | fl. 1899 (visit) (pp. 179, 181) | **Consistent** | Henry Algernon George Percy, Earl Percy, 1871-1909 (GND; Wikidata 21 Jan 1871 - 30 Dec 1909). | https://lobid.org/gnd/138134979.json<br>https://www.wikidata.org/wiki/Q5726862 |
| 133 | Philip Jenkins | b. 1952 (p. 184) | **Consistent** | GND b. 1952; Wikidata 3 Apr 1952. | https://lobid.org/gnd/131843524.json<br>https://www.wikidata.org/wiki/Q2086251 |
| 134 | Karen Armstrong (ch. 6) | b. 1944 (p. 186) | **Consistent** | As row 35 (GND b. 14 Nov 1944). | https://lobid.org/gnd/119304791.json |
| 135 | Frederic [Frederick] Jones Bliss | fl. 1912 (p. 188) | **Consistent** | 22 Jan 1859 - 1937 (GND). | https://lobid.org/gnd/142607304.json<br>https://www.wikidata.org/wiki/Q1452925 |
| 136 | Shaykh 'Abd al-'Aziz al-Shaykh | fl. March 2012 (p. 185) | **Consistent** | Grand Mufti 14 May 1999 - 23 Sep 2025; b. 30 Nov 1943 (Wikipedia; modern, uncontroversial). | https://en.wikipedia.org/wiki/Abdul-Aziz_ibn_Abdullah_Al_ash-Sheikh |
| 137 | Ahmad al-Hasani al-Baghdadi | fl. 2012 (p. 185) | **Unverified** | Not found in Wikidata, GND or Wikipedia (direct titles tried). | (none found; see section 4) |
| 138 | Essvo Yabh (Ishoyahb), Nestorian patriarch | 'toward the end of the seventh' (p. 180) | **Inconsistent** | If 'seventh century' is meant: Ishoyahb II 628-645 and Ishoyahb III 649-659 (Wikipedia list; GND Ishoyahb II active 628-646; Wikidata Ishoyahb III d. 659). The late-7th-century patriarchs were Yohannan I and Hnanisho I. No Ishoyahb held office at the end of the 7th century. (If 'seventh year' of the Hijra was meant, 628 fits the start of Ishoyahb II.) | https://en.wikipedia.org/wiki/List_of_patriarchs_of_the_Church_of_the_East<br>https://lobid.org/gnd/1011380900.json<br>https://www.wikidata.org/wiki/Q554286 |
| 139 | Abraham I, Armenian Patriarch of Jerusalem | 638-669 (p. 191) | **Consistent** | Wikipedia list of Armenian patriarchs of Jerusalem: Abraham I (638-669); a traditional list, Wikipedia-level source. The reported visit to the Prophet 'in 626' comes before this office (see section 3). | https://en.wikipedia.org/wiki/List_of_Armenian_Patriarchs_of_Jerusalem |
| 140 | 'Umar ibn al-Khattab | Caliph 634-644; conqueror of Jerusalem 638; firman 15 AH (pp. 193, 200) | **Consistent** | Caliph 634-644; went to Jerusalem and made the treaty in 17/638 (TDV). The firman's 15 AH (636) is earlier than the capitulation (see section 3). | https://islamansiklopedisi.org.tr/omer |
| 141 | Sophronios | fl. 15 AH (pp. 193-194) | **Consistent** | Patriarch of Jerusalem 634-638, d. 11 Mar 638 (Wikidata); BnF '055.?-0639'; GND 560-638. | https://www.wikidata.org/wiki/Q317773<br>https://data.bnf.fr/ark:/12148/cb120308844<br>https://lobid.org/gnd/118615696.json |
| 142 | 'Ali ibn Abi Talib | caliph 656-661; '626/4H'; decree 660 CE; Safar 40 AH (pp. 194-200) | **Consistent** | Caliph 656-661, d. 40/661 (TDV). By standard conversion Safar 40 AH falls in 660 and 4 AH = 625-626, so the book's dates agree with each other. | https://islamansiklopedisi.org.tr/ali |
| 143 | Cyril Lucaris | 1572-1638 CE (p. 192) | **Consistent** | GND 1572-1638; BnF 1571-1638; Wikidata 13 Nov 1572 - 27 Jun 1638. | https://lobid.org/gnd/133504255.json<br>https://data.bnf.fr/ark:/12148/cb12086376m<br>https://www.wikidata.org/wiki/Q440558 |
| 144 | Murad IV (ch. 6) | '1630-1634' period (p. 192) | **Consistent** | Inside his 1623-1640 reign (TDV). | https://islamansiklopedisi.org.tr/murad-iv |
| 145 | Jean Thenaud | fl. 1512 (p. 192) | **Consistent** | GND: born between 1474 and 1484, last mentioned 1542; BnF '14..-154.'. | https://lobid.org/gnd/120904624.json<br>https://data.bnf.fr/ark:/12148/cb12182601r |
| 146 | Father Jerome (Girolamo) Golubovich | book published 1921 (p. 191) | **Consistent** | 7 Feb 1865 - 9 Jan 1941 (BnF; GND), so 1921 falls in his lifetime (publication year not checked separately). | https://data.bnf.fr/ark:/12148/cb11202316b<br>https://lobid.org/gnd/174163533.json |
| 147 | Caliph Muktafi II (al-Muqtafi) | fl. 1138 CE (p. 198) | **Consistent** | Abbasid caliph 1136-1160, d. 555/1160 (TDV). | https://islamansiklopedisi.org.tr/muktefi-liemrillah<br>https://www.wikidata.org/wiki/Q293617 |
| 148 | Salah al-Din al-Ayyubi | c. 1138-1193 CE; Jerusalem 1187 (pp. 199-200) | **Consistent** | BnF 1138-1193; GND 1137-1193; d. 589/1193 (TDV). | https://data.bnf.fr/ark:/12148/cb119722308<br>https://lobid.org/gnd/118604988.json<br>https://islamansiklopedisi.org.tr/selahaddin-i-eyyubi |
| 149 | Samuel (of Ani) | wrote 'in the 13th century' (p. 200) | **Inconsistent** | 12th-century historian and priest (Wikipedia); GND d. 1179; Wikidata c. 1105 - c. 1185 / d. 1179. | https://en.wikipedia.org/wiki/Samuel_Anetsi<br>https://lobid.org/gnd/100960332.json<br>https://www.wikidata.org/wiki/Q3036364 |
| 150 | Gregor Campan | fl. 1767 (p. 194) | **Unverified** | No authority record found (Wikidata search). Known only from the Avdall 1870 account. | (none found; see section 4) |
| 151 | Joakim Gregor Bagratuni | fl. 1804 (p. 194) | **Unverified** | No authority record found. | (none found; see section 4) |
| 152 | Johannes Avdall | fl. 1869-1870 (p. 194) | **Consistent** | BnF 'Jean Avdaliants (1803-1870)'; Wikidata d. 11 Jul 1870. | https://data.bnf.fr/ark:/12148/cb16195070d<br>https://www.wikidata.org/wiki/Q15961845 |
| 153 | Henry Torrens | fl. before 1869 (p. 194) | **Consistent** | Henry Whitelock Torrens, 20 May 1806 - 17 Aug 1852 (Wikidata, citing Find a Grave); GND 1806-1852. | https://lobid.org/gnd/105548521X.json<br>https://www.wikidata.org/wiki/Q5730097 |
| 154 | al-Husayn ibn 'Ali, Sharif of Mecca | 1854-1931 CE; edict 1917 (p. 201) | **Minor difference** | BnF 'Husayn ibn Ali (roi du Hijaz, 1853-1931)'; Wikidata b. c. 1853 (citing BnF, GND, LoC), d. 4 Jun 1931. Birth one year off. | https://data.bnf.fr/ark:/12148/cb15598932m<br>https://www.wikidata.org/wiki/Q128906 |
| 155 | Albert Yelda | no dates ('former') (pp. 182, 190) | **N/A (no date given)** | No date to check. Wikipedia: Albert Edward Ismail Yelda, b. 1959, later Iraq's ambassador to the Vatican. | https://en.wikipedia.org/wiki/Albert_Yelda |

## 2. Inconsistent and Disputed rows, most significant first

### Inconsistent

1. **Row 24, 'Allamah Majlisi (Muhammad Baqir), "1616-1689".** The real dates are b. 1037/1627 and d. 1110/1698-99 or 1111/1699-1700 (TDV; GND 1627-1698). Both ends are about 11 years early. The book may have mixed him up with his father's generation.
2. **Row 149, Samuel of Ani, "wrote in the 13th century".** He was a 12th-century historian: GND d. 1179; Wikidata c. 1105-c. 1185; Wikipedia. The book is a century late.
3. **Row 11, Ja'far ibn Abi Talib, "return 626".** He returned from Abyssinia at the conquest of Khaybar, 7/628 (TDV "Ca'fer b. Ebu Talib" and "Hayber"). Wikipedia gives summer 628.
4. **Row 9, Abu Hurayrah, "603-681".** He died in 58/678, with 57/677 or 59/679 also reported (TDV). BnF gives d. 677? and GND d. 679. No source gives 681.
5. **Row 127, "Shimon the fourth", patriarch in 1517.** Shemon IV died in 1497. The patriarch in 1517 was Shemon VI (1504-1538), per the Wikipedia list and Wikidata citing Wilmshurst. The lists number the Shemon patriarchs differently, so this may be a numbering mismatch.
6. **Row 51, Johann Michael Vansleb, "1635-1676".** He died on 12 Jun 1679 (GND; BnF heading 1635-1679).
7. **Row 45, Berthold, "died in 1188".** He died c. 1195 (Store norske leksikon; Wikipedia). Wikidata gives 1195 or 1198.
8. **Rows 3 and 121, Ibn Ishaq, "704-761/770".** The standard death date is 150/767 or 151/768 (TDV; GND 768; BnF 767?). TDV lists 153/770 and 154/771 only as minority variants. 761 is not attested in any source checked.
9. **Row 138, Essvo Yabh (Ishoyahb), "toward the end of the seventh [century]".** No Ishoyahb was patriarch then. Ishoyahb II served 628-645/646 and Ishoyahb III 649-659 (Wikipedia list; GND; Wikidata). If the book meant the seventh year of the Hijra, 628 fits Ishoyahb II.
10. **Row 40, Khalid ibn al-Walid, born "592".** TDV gives c. 583-587 ("35-39 years before the Hijra") and Wikidata 586. His death in 642 is correct. This is low significance because the birth year is approximate anyway.

**Other dating errors in these rows that are not life or reign dates:**

- **Row 1.** Atatürk "abolished the Caliphate in 1922": the sultanate was abolished on 1 Nov 1922 and the caliphate on 3 Mar 1924 (Wikipedia "Abolition of the Caliphate"). This is the most visible event-date error in the batch, though Atatürk's own dates (1881-1938) are correct.
- **Row 98.** Julius II is called "patron of the 1514 Fano printing", but he died on 21 Feb 1513 (GND, BnF, Wikidata). At most he founded or patronised the press.

### Disputed among sources (the book follows one version)

1. **Row 117, Salman the Persian, "d. 654".** TDV gives 35-36/656 and says other dates exist. Wikidata gives 657. I found 654 in no source, so this is close to Inconsistent.
2. **Row 21, al-Sarakhsi, "d. c. 1096".** The usual date is 483/1090-91 (TDV; GND; BnF). Some biographies say "around [4]90", and the book follows that minority version.
3. **Row 19, 'Ali al-Rida, born "765".** BnF gives 765? and TDV lists 148/765 as one variant. But TDV, GND and Wikidata prefer 153/770. His death in 203/818 is agreed.
4. **Row 65, André Du Ryer, "c. 1580-1660".** GND gives 1580-1660, but BnF gives "15..-1688?".
5. **Row 90, Henri Basnage de Beauval, "1657-1710".** BnF gives 1657-1710, but GND and Wikidata give a 1656 birth.

**Minor differences, for completeness:**

| Row | Person | Book | Sources |
|---|---|---|---|
| 12 | al-Nawawi | d. 1278 | d. 676/1277 |
| 13 | al-Razi | d. 1209 | d. 606/1210 |
| 46 | Rycaut | b. 1629 | BnF/GND 1628 |
| 64 | Savary de Brèves | d. 1627 | d. 22 Apr 1628 |
| 66 | Salmasius | alternative birth 1596 | unsupported; 1588 is correct |
| 98 | Julius II | patron in 1514 | d. 1513 (see above) |
| 108 | Müteferrika | press founded 1726 | ferman July 1727; treatise 1726 |
| 111 | Grassi | Charte turque 1826 | Paris 1825 (DBI) |
| 123 | Ibn Hisham | d. 834 | 218/833; BnF/GND say 834 |
| 124 | Alfred Guillaume | d. 1966 | d. 30 Nov 1965 |
| 131 | Bedir Khan | d. 1868 | d. 1869 (Wikipedia/Wikidata) |
| 154 | Husayn ibn 'Ali | b. 1854 | BnF/Wikidata 1853 |

## 3. Does the book contradict itself about the same person?

**Dates:** no direct contradiction found. Every person who appears in several rows gets the same life or reign dates each time:

- Mu'awiyah: pp. 115, 116, 147, 178, 183
- Ibn Ishaq: p. 112 "761/770" and p. 188 "761/70", the same dates abbreviated
- al-Baladhuri: pp. 120, 183
- 'Umar: pp. 114, 193
- 'Ali: pp. 147, 160, 194-200
- Selim I: pp. 147-148, 177
- Karen Armstrong: pp. 128, 186
- Muhammad: pp. 152, 183
- Pacifique de Provins: pp. 139-152
- Henri IV: pp. 149, 150
- Sulayman: pp. 148, 175
- Renaudot: p. 145 and p. 153, the latter only an OCR join
- Murad IV: "r. 1623-1640" on p. 142 and the "1630-1634" period on p. 192. These do not conflict; the second is a sub-period.

**Hedges and small wording differences:**

- **Salmasius.** The book gives "d. 1653" on p. 150 and "1588 or 1596-1653" on p. 152. The death year agrees; the second page adds an unsupported alternative birth year.

**Chronological tensions inside the book's own narrative (flag for the user):**

- **'Umar.** On p. 193 he is the "conqueror of Jerusalem in 638" (TDV agrees: 17/638). Yet his firman to Sophronios is dated 20 Rabi' al-Awwal 15 AH, about 636, roughly two years before the capitulation the book itself dates to 638.
- **Abraham I, Armenian Patriarch of Jerusalem.** On p. 191 he is "Patriarch from 638 to 669", but he is also said to have visited the Prophet "in 626" to obtain privileges. The visit falls 12 years before his patriarchate, and the Prophet died in 632 (BnF, GND).
- **Mu'awiyah.** On p. 115 he "might not yet have been a Muslim" when he witnessed the Najran covenant. On pp. 147 and 183 he "embraced Islam before the conquest of Mecca (8 AH/630)" and was the Prophet's scribe 630-632. Whether these clash depends on the date the book assigns to the Najran covenant, which is not in this list.
- **Baron de Slane.** Row 114 gives "catalogue 1883-1895", but de Slane died in 1878 (BnF, GND). These are the posthumous publication dates, not years he was working.

## 4. Unverified rows and why

The session's web-search budget ran out partway through. After that I tried only Wikidata search (wbsearchentities), GND search (lobid), VIAF autosuggest and direct Wikipedia titles.

- **Rows 100, 101, 102 and 107 (Girgis al-Ifrangi, Mansur ibn Sulayman Sahyun al-Ramadi, Butrus ibn Diyab al-Halabi, Valerianus Oserole).** These are copyists and readers known only from notes in the manuscript or printed copy. I found no authority record in Wikidata or GND. The dates come from the book's reading of the manuscript and can only be checked against the manuscript itself (BnF MS Arabe 214 and the copy of Sionita's edition).
- **Row 113 (Edward A. Van Dyck).** The GND record (1052800505) and the Wikidata item (Q111473359) exist but carry no dates. The 1881 date is the year of his consular report, which I did not open.
- **Row 130 (Theodore D'Mar Shimun, "1906-2001").** Not found in Wikidata, GND or Wikipedia (direct title). VIAF autosuggest gave nothing usable.
- **Row 137 (Ahmad al-Hasani al-Baghdadi, fl. 2012).** Not found in Wikidata or Wikipedia under any spelling I tried. The 2012 edict is unverified.
- **Rows 150 and 151 (Gregor Campan, fl. 1767; Joakim Gregor Bagratuni, fl. 1804).** No Wikidata or GND record. Both are known only through Avdall's 1870 article in the Journal of the Asiatic Society of Bengal, which I did not open.
- **Also partly unverified (counted as Consistent):**
  - Row 110: "Mr. Legrand" could not be identified; Grégoire's part is fine.
  - Rows 42, 115 and 146: the publication years (Hamidullah's 1956 edition, Guillaume's Procès-verbaux, Golubovich's 1921 book) were only checked against the authors' lifespans.
- **Row 155 (Albert Yelda)** is marked N/A because the book gives no date.
