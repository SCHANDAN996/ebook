# ebook — Teacher AI Toolkit

Ek digital product ko market research se leke bikne-layak PDF tak le jaane ka
poora kaam: **rannneeti, gaNit, aur wo script jo product khud banati hai.**

**Product:** *The Teacher AI Toolkit* — K-12 teachers ke liye 300 copy-paste AI
prompts + 12 multi-step workflows. Front-end $27, target AOV $41.

**Sabse badi baat:** har prompt ke saath uska **ASLI output** chhapta hai. Amazon
par $2.99–9.99 wali prompt-list books mein sirf prompt ki list hoti hai. Wahi ek
farak product ko alag karta hai — aur wahi unke liye haath se karna namumkin hai.

---

## Repo mein kya hai

| Path | Kya hai |
|---|---|
| [`docs/strategy.md`](docs/strategy.md) | **Yahan se shuru karo.** Poora market research — niche kyun chuna, unit economics, campaign settings, 5 ready ad scripts, Meta policy ke jaal, 14-din ka plan |
| [`docs/decision-log.md`](docs/decision-log.md) | **फ़ैसलों का पूरा रिकॉर्ड (देवनागरी में)** — अब तक क्या-क्या तय हुआ और क्यों, कौन से niche रद्द हुए, पैसा कहाँ लगेगा, अभी की स्थिति और बाक़ी काम |
| [`docs/plan-b-thekedar-kit.md`](docs/plan-b-thekedar-kit.md) | Ek alag, India-only, kam budget wala plan. Side mein rakha hua |
| [`deliverables/lead-magnet.pdf`](deliverables/lead-magnet.pdf) | **Muft lead magnet — banaa hua PDF.** 25 prompts, 3 ke saath asli output. Seedha baant sakte ho |
| [`toolkit/`](toolkit/) | Product banane wali pipeline. Detail: [`toolkit/README.md`](toolkit/README.md) |

---

## Kis kram mein chalna hai

### Kadam 0 — Muft validation (₹0)

Paisa lagane se **pehle** demand check karo.

```bash
cd toolkit
pip install -r requirements.txt
python3 lead_magnet.py          # koi API call nahi, koi kharcha nahi
```

`build/lead-magnet.pdf` banta hai. **Ya seedha
[`deliverables/lead-magnet.pdf`](deliverables/lead-magnet.pdf) uthao — wahi file
pehle se repo mein padi hai**, kuch chalane ki zaroorat hi nahi.

25 prompts, 3 ke saath asli sample output. Ye teacher wale Facebook groups mein
muft baanto, badle mein email lo.

- 3 din mein **100+ email** → maang asli hai, aage badho
- **20 se kam** → angle galat hai. **~₹14,000 bach gaye**

### Kadam 1 — Product banao (~₹1,530)

```bash
export ANTHROPIC_API_KEY=sk-ant-...

python3 run.py estimate     # kitna lagega, pehle dekho
python3 run.py catalog      # 300 prompts + 12 workflows
python3 run.py outputs      # sabko chala kar ASLI output (Batch API, 50% sasta)
python3 run.py build        # HTML + PDF + QC
```

> **Pehli baar poora 300 mat chalao.** `config.py` mein kisi ek section ka
> `count` **5** kar do, `python3 run.py all -y` chalao (~₹40). Sab theek dikhe,
> tabhi poora chalao.

### Kadam 2 — Ads (~₹12,500 test)

Settings, targeting, creatives, kill rules — sab
[`docs/strategy.md`](docs/strategy.md) mein hain.

---

## Paisa kahan lagega

| Cheez | Kharcha | Zaroori? |
|---|---|---|
| Free validation | **₹0** | ✅ sabse pehle |
| Product banana (Anthropic API) | ~₹1,530 | ✅ |
| Landing page | ₹0 (khud banao) | ✅ |
| Payment gateway (Lemon Squeezy) | ₹0 upfront, ~5% per sale | ✅ |
| Facebook ads test (7 din) | ~₹12,500 | ✅ |
| Teacher UGC video | ₹4,000–13,000 | ❌ baad mein |

---

## Naya product banana

Poori pipeline niche-agnostic hai. `toolkit/config.py` mein sirf `PRODUCT`,
`SECTIONS` aur `WORKFLOW_BRIEF` badlo (aur `steps/catalog.py` ka system prompt) —
"AI for Realtors" ya "AI for HR" ban jaayega.

**Pehla product 4 din, doosra 1 din.** Ye factory hai, ek product nahi.
