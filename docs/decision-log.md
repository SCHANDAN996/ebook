# फ़ैसलों का पूरा रिकॉर्ड (Decision Log)

## 2026-09-08: Geography तय — US only. यही वर्तमान निर्णय है।

**फ़ैसला: बाज़ार United States है। India वाला रास्ता बंद।**

यह कोई नया फ़ैसला नहीं, पहले से लिए गए फ़ैसले को लिखित करना है। नीचे "3. दूसरी
कोशिश" में niche इसी आधार पर चुना गया था — *"K-12 teachers के लिए AI prompt +
workflow system, US/Tier-1, $27"* — और उसके चारों सबूत अमेरिकी हैं: US में 40 लाख
K-12 teachers, Teachers Pay Teachers का $879M बाज़ार, "3 में से 2 अमेरिकी teacher"
वाला डाउनलोड आँकड़ा, और Facebook की 40+ महिला educator demographic. Cold-email
विश्लेषण भी सिर्फ़ अमेरिकी CAN-SPAM पर बना है।

इसके बावजूद `SALES-LAUNCH-PLAN.md` में दो अलग geography (International $ और India
₹) साथ-साथ खुली रह गई थीं, और उसी फ़ाइल में लिखा था *"पहले एक geography चुनें,
दोनों साथ नहीं।"* वह चुनाव अब यह है: **US.**

- Pricing: सिर्फ़ USD। ₹ वाला column hypothesis के तौर पर रहेगा, launch path में नहीं।
- Paid test: सिर्फ़ International hypothesis ($50 cap)। ₹2,000 वाला test नहीं चलेगा।
- `plan-b-thekedar-kit.md` India-only है और Plan B ही रहेगा — वह market research
  से नहीं निकला था, यह उसमें ख़ुद लिखा है।

**इसका सीधा नतीजा किताब पर:** किताब ब्रिटिश अंग्रेज़ी में लिखी जा चुकी थी —
`behaviour`, `maths`, `marking`, `timetable`, `judgement`, और पहले ही पन्ने पर
`Year 7 science`. एक अमेरिकी teacher के लिए यह तुरंत पकड़ में आता है। manuscript
और front-matter की 146 जगहें अमेरिकी अंग्रेज़ी में बदली गईं, `Year 7 / Year 5` को
`7th grade / 5th grade` किया गया, और safety page में **FERPA** तथा **COPPA** वाला
हिस्सा जोड़ा गया — अमेरिकी teacher student privacy का यही नाम खोजती है।

**एक पुराना दावा सुधारा जा रहा है:** 2026-09-07 की सूची कहती है कि PDF को
"browser-free exporter, clickable index, bookmarks और page numbers" दिए गए। यह
सही नहीं था। 2026-09-08 तक PDF में न bookmark थे, न page number, न cover, और
exporter headless Chromium ही है, browser-free नहीं। अब bookmarks (हर prompt का),
page numbers, running header, cover और complete edition में clickable index
सचमुच मौजूद हैं — exporter अब भी Chromium है।

**अभी भी बाकी:** `support_email` और `support_url` placeholder हैं, किसी अमेरिकी
teacher ने review नहीं किया (सभी 300 prompts `review_status: draft`), किताब में
लेखक का नाम नहीं है, और repo public है जबकि paid PDF उसी में committed है।

---

## 2026-09-07: समीक्षा के बाद सुधार - यही वर्तमान निर्णय है

नीचे का पुराना रिकॉर्ड ऐतिहासिक है। उसके market rankings, CTR/CPA, $41 AOV,
"zero risk", "no competition", "5 hours saved", "100 emails = proven demand"
और छोटे test की ₹40 लागत को सत्यापित तथ्य न मानें।
वर्तमान निर्णय [strategy.md](strategy.md) और [roadmap.md](roadmap.md) में हैं।

- Default pilot अब 5 prompts + 1 workflow है; beta/full caches अलग हैं।
- QC missing outputs/workflows को असफल करता है।
- Workflow steps अब वास्तविक पूर्व output पर निर्भर हैं।
- Cache input/model fingerprints और output provenance रखता है।
- पुराने lead-magnet samples को verified API outputs कहना उचित नहीं था।
  उनकी जगह स्पष्ट fictional editorial examples दिए गए हैं।
- Student initials को anonymization बताना हटाया; privacy और factual checks बढ़ाए।
- PDF को browser-free exporter, clickable index, bookmarks और page numbers दिए।
- बड़ा paid product, real teacher review, live API test और sales funnel अभी बाकी हैं।
- कोई API खर्च, ad launch, customer outreach या checkout activation नहीं किया गया।

---

## ऐतिहासिक रिकॉर्ड - वर्तमान execution instructions नहीं

यह दस्तावेज़ बताता है कि **अब तक क्या-क्या तय हुआ और क्यों** — शुरुआत से आज तक।
कुछ महीने बाद जब याद न रहे कि फ़लाँ फ़ैसला क्यों लिया था, तो यही फ़ाइल खोलिए।

---

## 1. मूल सवाल

> "Facebook ads से ebook बेचकर कमाई करनी है। कौन सा niche सबसे सही है —
> जिसमें **लागत कम**, **CTR ज़्यादा**, **कमाई ज़्यादा**, **user base बड़ा** हो?
> Content पूरा AI से बनवाना है।"

---

## 2. पहली कोशिश — और वो क्यों रद्द हुई

पहली बार `android-apps` repo देखकर niche चुना गया था: **ठेकेदार / Contractor Kit**
(क्योंकि वहाँ Mistri Calculator, Jameen Napi जैसे apps पहले से थे)।

**यह ग़लत तरीक़ा था।** सवाल था "मार्केट में क्या चल रहा है" — न कि "मैं पहले से
क्या कर रहा हूँ"। मौजूदा काम को देखकर निष्कर्ष निकालना मार्केट रिसर्च नहीं है।

वो योजना [`plan-b-thekedar-kit.md`](plan-b-thekedar-kit.md) में रख दी गई है।
अपने आप में ख़राब नहीं है — India-only, कम बजट वाला रास्ता चाहिए तो काम आएगी।

**सीख:** मौजूदा काम से शुरू करने पर वही निकलता है जो आप पहले से कर रहे हैं,
न कि वो जो बाज़ार माँग रहा है।

---

## 3. दूसरी कोशिश — सिर्फ़ मार्केट डेटा से

### जो niche रद्द किए — डेटा के साथ

| Niche | डेटा | रद्द क्यों |
|---|---|---|
| **Health / Weight loss** | सबसे ज़्यादा CTR — **3.02%** | Meta की सबसे सख़्त policy। 2026 में before/after का ban अब "implied transformation" तक। Q1 2026 में supplements के **64% accounts review** हुए (+41% QoQ) |
| **Make money / Trading** | सबसे ज़्यादा माँग | **38 देशों में advertiser verification अनिवार्य**। एक strike = पूरा ad account गया |
| **Personal finance** | सबसे ऊँचा CPM ($15–22) | वही verification की दीवार |
| **AI productivity (global)** | सबसे तेज़ बढ़ता (+29.38% YoY) | कोई बढ़त नहीं, US CPM 10x, और AI-slop saturation सबसे ज़्यादा वहीं — **30%+ नए titles पर AI disclosure** |
| **Notion / Canva templates** | Etsy पर top-selling, 70–90% margin | यह Etsy/Pinterest का खेल है, paid ads का नहीं |
| **Parenting** | बड़ा audience, कम competition | Paid conversion बहुत कमज़ोर — parents मुफ़्त content पर रुक जाते हैं |
| **AI for realtors / HR** | ticket बड़ा ($49–199) | वो LinkedIn पर हैं, Meta पर ठंडी audience। **यह Product #2 है, #1 नहीं** |

### जो चुना: **AI for Teachers**

K-12 teachers के लिए AI prompt + workflow system, US/Tier-1, **$27**।

**चारों शर्तों पर:**

| शर्त | डेटा |
|---|---|
| User base | 40 लाख K-12 + 17 लाख college teachers सिर्फ़ US में |
| कमाई | $27 → **$41 AOV**, margin 95%+ |
| CTR | **2.74%** — दूसरा सबसे ज़्यादा, सबसे तेज़ बढ़ता (+29.38% YoY) |
| लागत | Content 100% AI, कोई inventory, **Meta की restricted category नहीं** |

**असली वजह — चार:**

1. **यह audience पहले से PDF ख़रीदती है, सबूत के साथ।**
   Teachers Pay Teachers = **$879 million (₹7,300 करोड़) सालाना**, 40 लाख educators,
   1 billion+ downloads, **3 में से 2 अमेरिकी teacher** ने पिछले साल resource
   download किया। *बाक़ी हर niche में यह व्यवहार पहले बनाना पड़ता है।*

2. **Facebook की सबसे अच्छी demographic यही है।**
   रिसर्च: *"ज़्यादातर educators महिलाएँ हैं, आधे से ज़्यादा 40 से ऊपर।"*
   बाक़ी सब advertiser Instagram पर 25-साल वालों के लिए लड़ रहे हैं।

3. **दर्द अभी, इस वक़्त है।** 60% teachers पहले से AI इस्तेमाल कर रहे हैं और
   44% prep time बचा रहे हैं — पर बेतरतीब तरीक़े से। AI in Education market:
   $6.4B (2025) → $79.6B (2034), CAGR 31.35%.

4. **यहाँ AI content slop नहीं है — वही product है।** Product ही AI prompts है।
   और हर prompt चलाकर उसका असली output दिखाया जा सकता है।

---

## 4. एक सोच जो ग़लत निकली — और सुधारी गई

पहले माना था: **"zero competition = अच्छा"**।

**मार्केट डेटा इसके उलट कहता है:**

> *"जिन ebook niches में rising Google Trends interest और **5-15 competitors** हैं,
> वो हमेशा **zero-competition** वालों से बेहतर perform करते हैं। एक औसत ebook
> भूखी audience में, एक शानदार ebook से ज़्यादा बिकेगी जो saturated niche में हो।"*

**Zero competition का मतलब अक्सर "कोई बाज़ार ही नहीं" होता है।**

AI-for-Teachers में बिल्कुल सही मात्रा में competition है — Amazon पर $2.99–9.99
की books, TpT पर bundles। **पर एक भी Meta ads funnel नहीं चला रहा।** सब Amazon
search पर लड़ रहे हैं। यही खाली जगह है।

---

## 5. Product के फ़ैसले

### Offer stack

| परत | दाम | उम्मीद |
|---|---|---|
| **Front-end** — 300 prompts + 12 workflows | **$27** | 100% |
| **Order bump** — 80 parent emails | +$17 | 30-45% लेंगे |
| **Upsell** — पूरा system + video + updates | +$67 | 10-20% लेंगे |

**AOV = $27 + $5.95 + $8.04 = $41 प्रति ख़रीदार** (≈ ₹3,600)

**$27 क्यों, $97 नहीं?** डेटा: *"Teachers अपने ही पैसे ख़र्च कर रहे हैं और ज़्यादा
चुनिंदा हो रहे हैं; कम दाम वाले, ज़्यादा value वाले resources अच्छा perform कर
रहे हैं।"* **यह volume का खेल है, दाम का नहीं।**

### सबसे बड़ा फ़र्क़: हर prompt के साथ उसका असली output

Amazon की सारी books में सिर्फ़ **prompt की सूची** है। इस product में हर prompt के
नीचे उसका **असली output** छपेगा।

तीन फ़ायदे एक साथ:
1. ख़रीदार को तुरंत दिखता है कि क्या मिलेगा → refund घटता है
2. "AI ने लिखा है" वाला शक ख़त्म
3. Ad creative इसी के अंदर से निकल आता है

और यह उनके लिए हाथ से करना नामुमकिन है — पर एक script के लिए आसान।

---

## 6. गणित

**वास्तविक (realistic):**
```
CPM $15 → CTR 2.5% → CPC $0.60 → LP conversion 4% → CPA $15
AOV $41 → ROAS 2.7x  ✅
```

**निराशाजनक (pessimistic):**
```
CPM $22 → CTR 1.5% → CPC $1.47 → LP conversion 2% → CPA $73.50
AOV $41 → ROAS 0.56x  ❌  (offer या landing page बदलनी पड़ेगी)
```

इसीलिए test budget **$140 (₹12,500)** है — सिर्फ़ यह पता करने के लिए कि आप किस
हालत में हैं।

---

## 7. पैसे के फ़ैसले

| चीज़ | ख़र्चा | ज़रूरी? |
|---|---|---|
| **मुफ़्त validation** | **₹0** | ✅ सबसे पहले |
| Product बनाना (Anthropic API) | ~₹1,530 | ✅ |
| Landing page | ₹0 (ख़ुद बनाएँगे) | ✅ |
| Payment gateway (Lemon Squeezy) | ₹0 upfront, ~5% per sale | ✅ |
| Facebook ads test (7 दिन) | ~₹12,500 | ✅ |
| Teacher UGC video | ₹4,000–13,000 | ❌ बाद में |

**क्रम तय हुआ — पहले मुफ़्त वाला कदम:**

Teacher वाले Facebook groups में मुफ़्त lead magnet बाँटो, email गिनो।
- 3 दिन में **100+ email** → माँग असली है, ₹1,530 लगाओ
- **20 से कम** → angle ग़लत है, **₹14,000 बच गए**

**Batch API का फ़ैसला:** 300 sample outputs latency-sensitive नहीं हैं, इसलिए
Message Batches API — **50% छूट**। इसी एक फ़ैसले से ~₹1,500 बचे।

---

## 8. बनाने के तकनीकी फ़ैसले

| फ़ैसला | वजह |
|---|---|
| **Python** | Pipeline है, Flutter app code नहीं |
| **Batch API** | 50% सस्ता, और ये requests को तुरंत जवाब नहीं चाहिए |
| **15-15 के chunk** | 60 prompts एक request में `max_tokens` से बाहर निकलकर **चुपचाप कट जाते** — पता भी न चलता कि book अधूरी है |
| **हर कदम resume होता है** | 300 prompts के job में ज़रूरी है, luxury नहीं। Batch id disk पर — दोबारा पैसा नहीं लगता |
| **`custom_id` से match** | Batch results किसी भी क्रम में आते हैं, position से कभी match मत करो |
| **`steps/keys.py` अलग** | Book बनाने के लिए Anthropic SDK की ज़रूरत नहीं होनी चाहिए |
| **PDF step non-fatal** | पहले browser न मिलने पर पूरा build crash हो जाता था, जबकि HTML बन चुका था |
| **Lead magnet हाथ से लिखा** | कोई API call नहीं = मुफ़्त validation सच में मुफ़्त |

---

## 8क. Cold email का फ़ैसला

**सवाल:** क्या cold email से promote कर सकते हैं?

**फ़ैसला: नहीं — teachers को सीधा नहीं। बाद में स्कूलों को, हाँ।**

| वजह | आँकड़ा |
|---|---|
| B2C cold email की बिक्री दर | **0.215%** = एक बिक्री पर **464 ईमेल** |
| $27 के product पर | घाटे का सौदा |
| Teachers के ईमेल | K-12 districts के सबसे सख़्त फ़िल्टर के पीछे |
| 2026 के नियम | spam complaints 0.3% से ज़्यादा = **सीधा rejection**, spam folder भी नहीं |
| नया domain | 4-6 हफ़्ते सिर्फ़ 5-10 ईमेल/दिन, वरना domain जल जाता है |

**क़ानूनी तौर पर** अमेरिका में वैध है (CAN-SPAM, consent की ज़रूरत नहीं), पर 6 शर्तें
हैं और एक भी छूटने पर **प्रति ईमेल $51,744 तक** जुर्माना। कनाडा (CASL) और
यूरोप/UK (GDPR) में बिल्कुल मत भेजिए।

**पर एक रूप काम करता है:** teacher को $27 का PDF नहीं — **स्कूल को 40 licence**।
वो B2B है: reply rate 3–5%, एक सौदा $500–2,000 का। **यह बाद का क़दम है** — पहले
20-30 असली ख़रीदार चाहिए जिनकी बात ईमेल में लिखी जा सके।

**और सबसे बड़ी बात:** lead magnet से आने वाले ईमेल **cold नहीं, warm** हैं —
10-50 गुना बेहतर चलते हैं, ₹0 ख़र्च, कोई क़ानूनी झंझट नहीं। वही असली रास्ता है।

पूरा विश्लेषण: [`channels-cold-email.md`](channels-cold-email.md)

---

## 9. अभी की स्थिति

### ✅ हो चुका

- [x] पूरी मार्केट रिसर्च और रणनीति — [`strategy.md`](strategy.md)
- [x] Build pipeline (7 फ़ाइलें) — [`../toolkit/`](../toolkit/)
- [x] मुफ़्त lead magnet — [`../deliverables/lead-magnet.pdf`](../deliverables/lead-magnet.pdf)
- [x] Pipeline नक़ली डेटा से पूरी तरह test — QC ने plant किए हुए 18 missing और
      8 छोटे outputs पकड़ लिए, 341-page PDF बना
- [x] अलग repository — `SCHANDAN996/ebook`

### ⬜ बाक़ी

- [ ] `toolkit/config.py` में `support_email` बदलना (अभी `CHANGE_ME@example.com`)
- [ ] Lead magnet teacher Facebook groups में बाँटना — **यही अगला कदम है**
- [ ] Pinterest पर resources डालना (₹0, teachers वहाँ ढूँढती हैं)
- [ ] Landing page (email capture)
- [ ] 100+ email मिलें तो: `python3 run.py all` (~₹1,530)
- [ ] Lemon Squeezy पर checkout + order bump + upsell
- [ ] Meta Pixel + Conversions API
- [ ] 5 creatives, फिर ads
- [ ] *(बाद में)* TpT पर listing
- [ ] *(20-30 बिक्री के बाद)* स्कूलों को B2B cold email

---

## 10. ईमानदार चेतावनियाँ

1. **Pipeline सिर्फ़ नक़ली डेटा से test हुई है।** असली API call एक भी नहीं हुई —
   क्योंकि वो आपका पैसा है। पहली बार चलाते वक़्त किसी एक section का `count` **5**
   कर दीजिए (~₹40), सब ठीक दिखे तभी पूरा 300 चलाइए।

2. **आप teacher नहीं हैं।** सबसे असरदार ad format "मैं teacher हूँ" वाला UGC है।
   **झूठ मत बोलिए** — Meta पर misrepresentation policy का उल्लंघन भी है, और
   teachers 10 सेकंड में पकड़ लेंगी। रास्ता: screen-demo ads, फिर असली teacher
   UGC creator hire कीजिए।

3. **Seasonality असली है।** Jul–Sep peak (back to school), January दूसरा peak,
   June मुर्दा। यह फ़ैसला **September 2026** में लिया गया — यानी peak के अंदर।

4. **पहला funnel fail हो सकता है।** $140 सीखने की फ़ीस है। ज़्यादातर लोग पहला
   fail होने पर छोड़ देते हैं — असली नाकामी वही है।

5. **यह script product बनाती है, verify नहीं करती।** बेचने से पहले कुछ prompts
   ख़ुद ChatGPT/Gemini पर चलाकर देखिए।
