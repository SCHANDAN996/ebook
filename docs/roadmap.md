# आगे का प्लान - परिणाम देखकर चरण बढ़ाएँ

यह लगभग 30 दिनों का कार्य-क्रम है, deadline या कमाई की गारंटी नहीं।
API खर्च, reviewer hiring, ads, customer messages और checkout activation के लिए
अलग स्वीकृति चाहिए। इस सुधार में इनमें से कोई कार्रवाई नहीं की गई है।

## 1. नींव और offline जाँच

- [x] अलग pilot/beta/full profiles।
- [x] वास्तविक workflow chaining और cache fingerprint।
- [x] Missing/refused/truncated outputs पर strict QC।
- [x] उदाहरणों पर सही labels और बेहतर privacy instructions।
- [x] Offline regression tests और PDF generation।
- [ ] बजट स्वीकृति के बाद छोटा live API smoke test।
- [ ] अपने PC पर install/build करके environment compatibility जाँचना।

आगे बढ़ने की शर्त: live pilot भी पूरा हो; catalog, exact inputs, output records और
token usage मिलें। यह teacher validation का विकल्प नहीं है।

## 2. ग्राहक की समस्या चुनना - लगभग दिन 4–7

लगभग 10 target teachers से बातचीत करें:
- आखिरी बार कौन-सा planning/admin task कठिन लगा?
- अभी किस tool या template से करते हैं?
- AI draft में सबसे ज्यादा क्या ठीक करना पड़ता है?
- उनके school में कौन-से AI services approved हैं?
- किस उपयोगी परिणाम के लिए वे पैसे देने पर विचार करेंगे?

किसी बच्चे का record, नाम, IEP या identifiable example न माँगें।
एक grade band/task चुनें। Interviews के बिना नया niche या दूसरी product line शुरू न करें।

## 3. छोटा beta product - लगभग दिन 8–14

- 30 prompts और 3 जुड़े workflows।
- Exact fictional inputs, पूरे outputs और editable teaching artifacts।
- Answer keys और supplied standard text का reviewer verification।
- Quick-start और troubleshooting।
- लगभग 2–3 qualified teachers से समीक्षा का प्रयास; paid hiring केवल स्वीकृत budget पर।

आगे बढ़ने की शर्त: हर output पर वास्तविक approval record; कोई गंभीर
accuracy/privacy issue बाकी नहीं। Reviewer disagree करे तो correction और re-review करें।

## 4. वास्तविक उपयोग - लगभग दिन 15–20

लगभग 10 volunteers से एक सप्ताह इस्तेमाल कराएँ। दर्ज करें:
- कौन-सा task पूरा किया?
- कितनी editing लगी?
- AI response सहित कुल task time कितना था?
- अगले दिन/अगले सप्ताह दोबारा इस्तेमाल हुआ या नहीं?
- वर्तमान free tools से बेहतर क्या था?
- उस समय stated price पर खरीदना चाहेंगे या नहीं?

सिर्फ पसंद आने, downloads या email संख्या को paid demand न मानें।
समय-बचत के दावे सिर्फ दर्ज किए गए परिणाम और उनकी सीमाओं के साथ दें।

## 5. बिक्री का छोटा परीक्षण - लगभग दिन 21–25

पहले user choices चाहिए:
- Product segment, deliverables और price।
- वास्तविक support email।
- Seller/payment onboarding और applicable accounting review।
- स्पष्ट refund/delivery policy।
- Consent-based email और data retention व्यवस्था।

फिर landing page, checkout, download delivery और tracking implement/test करें।
Payment success से पहले delivery न दें; webhook signature, duplicate event handling,
failed payment, duplicate purchase और refund paths जाँचें।
पहले test mode; live transaction/activation केवल स्वीकृति पर।

शुरुआती 5–10 genuine buyers उपयोगी signal हैं, scalability का प्रमाण नहीं।

## 6. सीमित ads - लगभग दिन 26–30 या बाद में

Product और delivery ठीक होने के बाद ही:
- 2–3 honest screen demos।
- एक clear audience और offer।
- अधिकतम स्वीकार्य नुकसान पहले तय।
- Purchase cost, refunds और contribution margin मापना।
- खराब परिणाम पर कारण जाँचें; budget स्वतः न बढ़ाएँ।

## अभी अगले तीन काम

1. इस branch के बदलाव review/merge करना।
2. Support email और target teacher segment तय करना।
3. छोटा live pilot चलाने से पहले API/provider budget की स्पष्ट स्वीकृति लेना।

कोई भी चरण सिर्फ calendar पूरा होने से पास नहीं होगा।
