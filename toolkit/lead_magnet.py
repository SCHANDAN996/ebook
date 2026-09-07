#!/usr/bin/env python3
"""Free preview: 25 planning prompts and explicitly illustrative, fictional examples.
No API calls. No measured time-saving or cross-tool compatibility claim.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import html

import config
from steps.build import CSS, _md

TITLE = "25 AI Planning Prompts for Teachers"
SUBTITLE = "A free development preview: adapt, review and try one classroom task."
FOOTER_CTA = (
    "A larger Teacher AI Toolkit is in development, not yet validated for sale. "
    "These illustrative examples are not logged API executions or teacher-reviewed results. "
    "There is no guaranteed time saving or verified cross-tool compatibility. "
    "Share feedback through the project link below; never include student records."
)
SAFETY = config.DISCLAIMER

# ---------------------------------------------------------------------------
# 25 prompts. Har prompt mein role, context, constraint aur output format hai —
# ek-line wale prompts kaam nahi karte, aur teacher ko wahi farak dikhta hai.
# ---------------------------------------------------------------------------
PROMPTS = [
    # ---- Planning ----------------------------------------------------------
    ("Planning", "A full lesson plan from one standard", "K-2 · 3-5 · 6-8 · 9-12",
     "Supply standard text and lesson duration to create a plan for review.",
     """You are an experienced [GRADE] teacher planning a [MINUTES]-minute lesson on [TOPIC], aligned to [SUPPLIED STANDARD TEXT].

Write the full plan with these sections and nothing else:
1. Learning objective, in student-facing "I can" language
2. Warm-up (3-5 min) that surfaces prior knowledge
3. Mini-lesson with the exact steps I model, in order
4. Guided practice, including what I circulate and look for
5. Independent practice
6. Exit ticket — one question that would actually reveal who did not get it
7. The single most common misconception on this topic, and the exact question I ask to catch it

Keep every section short enough to read at a glance while teaching. No introduction, no summary."""),

    ("Planning", "A substitute plan for an unexpected absence", "All grades",
     "You are sick at 6am. This writes a plan a stranger can teach.",
     """Write a substitute teacher plan for [GRADE] [SUBJECT] for [NUMBER] periods.

Assume the sub knows nothing about my class and may not know the subject. The work must be meaningful, not busywork, and must need no preparation or special materials.

Include:
- A 3-line "what this class is like" note
- Minute-by-minute timing for each period
- Exactly what to write on the board
- The task itself, written out in full so it can be photocopied
- What to do if students finish early
- What to leave me a note about

Write it as one page the sub can follow top to bottom."""),

    ("Planning", "A week of bell ringers", "3-5 · 6-8 · 9-12",
     "Five warm-ups that spiral back to what they keep forgetting.",
     """Create 5 bell ringers (one per day) for [GRADE] [SUBJECT], each taking under 5 minutes.

They must spiral: Monday and Tuesday review [TOPIC THEY KEEP FORGETTING], Wednesday and Thursday preview [THIS WEEK'S TOPIC], Friday mixes both.

For each day give me: the question exactly as students will see it, the answer, and one sentence on what a wrong answer tells me."""),

    ("Planning", "Unit skeleton from an end goal", "6-8 · 9-12",
     "Work backwards from the assessment instead of forwards from day one.",
     """I am planning a [NUMBER]-week unit on [TOPIC] for [GRADE]. The unit ends with [FINAL ASSESSMENT].

Work backwards. Give me:
- The 4-6 things students must be able to do to succeed on that assessment
- Those skills sequenced across the weeks, with a reason for the order
- One checkpoint per week that tells me who is off track early
- The two lessons in this unit most likely to go wrong, and why

Table format, one row per week."""),

    ("Planning", "Turn a textbook chapter into a lesson", "6-8 · 9-12",
     "The book has the content. It does not have a lesson.",
     """Below is a passage I have permission to reproduce for [GRADE] [SUBJECT]. Turn it into a [MINUTES]-minute lesson that does not involve reading it aloud.

Give me: a hook that creates a question the text answers, the 3 ideas worth keeping (and what to cut), an activity that makes students use the ideas rather than restate them, and an exit ticket.

TEXT:
[PASTE THE SECTION HERE]"""),

    # ---- Report cards ------------------------------------------------------
    ("Report cards", "Batch report card drafts from fictional notes", "All grades",
     "Draft comments from supplied fictional observations; verify before adapting.",
     """I am writing report card comments for [GRADE] [SUBJECT].

Below is my class list as "Fictional student label | example grade | supplied evidence". For each student write a comment of [NUMBER] sentences that:
- opens with a specific strength, not a generic compliment
- names one concrete next step the student can act on
- is written to be read by a parent, warm but honest
- never compares one student to another

Vary the sentence openings — comments that all start the same way read as copy-paste.

CLASS LIST:
Student A | B+ | strong writer, rushes edits
Student B | C | participates, struggles with multi-step problems
[ADD FICTIONAL EXAMPLES ONLY]"""),

    ("Report cards", "Rewrite a blunt comment", "All grades",
     "You know what you mean. This makes it survivable for a parent.",
     """Rewrite the report card comment below so it is honest but not deflating for a parent to read.

Keep every fact. Do not soften it into meaninglessness — the parent must still understand there is a problem and what to do about it. Give me three versions: gentle, direct, and firm.

COMMENT:
[PASTE YOUR DRAFT]"""),

    ("Report cards", "A comment bank you can reuse all year", "All grades",
     "Build it once in January, use it every term after.",
     """Build a report card comment bank for [GRADE] [SUBJECT].

Give me 6 comments for each of these bands: excelling, secure, approaching, struggling, and inconsistent effort.

Each comment must have a blank [FICTIONAL LABEL] and one blank [SPECIFIC EXAMPLE] so I can drop in something real. Vary the openings across the bank. Group them under headings."""),

    # ---- Parent communication ---------------------------------------------
    ("Parent emails", "The email you have been putting off", "All grades",
     "A concern email that does not turn into a meeting about your tone.",
     """Write an email to a parent about a concern.

Concern: [WHAT IS HAPPENING]
What I have already tried: [WHAT YOU TRIED]
What I want from this email: [A MEETING / AWARENESS / SUPPORT AT HOME]

Rules: open with something genuine and specific about the child. State the concern in plain terms without jargon or diagnosis language. Describe behaviour, never character. End with one clear ask. Under 200 words. No emoji.

Then give me a shorter version for a parent who does not read long emails."""),

    ("Parent emails", "Positive notes home, ten at a time", "All grades",
     "Draft positive notes using only the observations supplied.",
     """Write 10 short positive notes home for [GRADE], one per student, based on the notes below.

Each must be 2-3 sentences, name something specific (not "a pleasure to teach"), and sound like a real person wrote it. Vary the structure so they do not read as a template.

STUDENTS:
Student A - fictional example: helped a new student find the room
Student B - fictional example: asked for help
[ADD FICTIONAL EXAMPLES ONLY]"""),

    ("Parent emails", "Conference prep one-pager", "All grades",
     "Ten minutes per family, and you have 24 families.",
     """I have parent conferences for [GRADE] [SUBJECT]. Each is [MINUTES] minutes.

From the notes below, build me a one-page card per student with: one strength with evidence, one growth area with evidence, one thing to ask the parent, and one thing the parent can do at home. Keep each card to what I can scan in 20 seconds.

NOTES:
[PASTE YOUR NOTES]"""),

    ("Parent emails", "Class newsletter from rough notes", "K-2 · 3-5",
     "Bullet points in, finished newsletter out.",
     """Turn these rough notes into a warm, scannable class newsletter for [GRADE] families for the week of [DATE].

Sections: what we learned, what is coming up, dates to remember, how to help at home. Keep it under 300 words, use headings, and write at a reading level any parent can follow.

NOTES:
[PASTE YOUR BULLET POINTS]"""),

    # ---- Differentiation ---------------------------------------------------
    ("Differentiation", "One task, three levels", "All grades",
     "Three entry points into the same lesson, with a shared learning objective.",
     """Take the task below for [GRADE] [SUBJECT] and give me three versions:

- Scaffolded: same thinking, more support (sentence starters, worked example, chunked steps)
- On-level: as written, tightened if needed
- Extension: same topic, genuinely harder thinking — not just more questions

All three must be able to run in the same room at the same time, and end with students able to share in one discussion.

TASK:
[PASTE YOUR TASK]"""),

    ("Differentiation", "Rewrite a text to a lower reading level", "3-5 · 6-8 · 9-12",
     "Keep the ideas. Lose the barrier.",
     """Rewrite the passage below for [GRADE] students reading roughly [NUMBER] years below grade level.

Keep every key idea and all subject vocabulary — define the vocabulary in place rather than removing it. Shorten sentences, make the structure obvious, and add a heading every few paragraphs.

Then list the 5 words a student may still get stuck on, with a student-friendly definition each.

PASSAGE:
[PASTE THE TEXT]"""),

    ("Differentiation", "Supports for multilingual learners", "All grades",
     "Access to the lesson, not a different lesson.",
     """For the [GRADE] [SUBJECT] lesson below, give me supports for students still developing English.

I need: the 6 words that will block comprehension with a plain definition and a visual I could sketch, sentence frames for the discussion, a way for a student to show understanding without writing a paragraph, and one thing I should say differently while teaching.

Do not simplify the content or lower the expectation — only the language load.

LESSON:
[PASTE YOUR PLAN]"""),

    ("Differentiation", "Real work for early finishers", "All grades",
     "Not a word search. Something that actually extends.",
     """Students finishing [TASK] early in [GRADE] [SUBJECT] need something that extends the same thinking, not filler.

Give me 5 options that: need no new instruction from me, take 5-15 minutes, use only what is already on their desk, and could be shared with the class in one sentence.

For each, say in one line what deeper thinking it demands."""),

    # ---- Assessment --------------------------------------------------------
    ("Assessment", "A quiz with an answer key and a diagnosis", "3-5 · 6-8 · 9-12",
     "Every wrong answer tells you something specific.",
     """Write a [NUMBER]-question quiz on [TOPIC] for [GRADE].

Mix recall, application, and one question that needs reasoning. For each question give me: the question, the answer, and — for each wrong option — what a student choosing it probably misunderstands.

Then tell me which 2 questions to look at first when I grade, to find out fastest who needs reteaching."""),

    ("Assessment", "A single-point rubric", "All grades",
     "One column of criteria. Faster to write, far faster to grade.",
     """Build a single-point rubric for [ASSIGNMENT] in [GRADE] [SUBJECT].

Format: a centre column stating what proficient looks like for each criterion, with blank columns either side for "needs work" and "exceeds" that I fill in per student. Use 4-5 criteria maximum, written in language a [GRADE] student can read and act on.

Then give me 3 feedback sentences per criterion that I can reuse."""),

    ("Assessment", "Exit tickets that actually sort the class", "All grades",
     "One question that separates 'got it' from 'nodded along'.",
     """Write 5 exit ticket questions for [TOPIC] in [GRADE] [SUBJECT].

Each must be answerable in under 3 minutes and must distinguish real understanding from surface repetition — a student who only copied the steps should get it wrong.

For each, tell me what a correct answer proves and what the most likely wrong answer tells me to reteach."""),

    ("Assessment", "Questions aimed at one misconception", "All grades",
     "You know exactly what they are getting wrong. Target it.",
     """My [GRADE] students are consistently making this mistake in [SUBJECT]: [DESCRIBE THE MISTAKE].

Give me 6 questions designed so that a student holding this misconception gets them wrong in a visible way, plus 2 where the misconception does not matter — so I can tell it apart from a general struggle.

Then give me the sequence of 3 questions I would ask one student, out loud, to walk them out of it."""),

    # ---- Worksheets & activities ------------------------------------------
    ("Worksheets", "A worksheet that ramps properly", "K-2 · 3-5 · 6-8",
     "Starts where they are, ends where you want them.",
     """Create a practice worksheet on [TOPIC] for [GRADE].

Structure it in four blocks: 2 warm-up items anyone can do, 5 core items building in difficulty, 2 items that combine this with [EARLIER TOPIC], and 1 challenge.

Include the answer key, and mark which single item is the "if they get this, they have it" question."""),

    ("Worksheets", "A station rotation from one topic", "K-2 · 3-5 · 6-8",
     "Four stations, four different ways in, one period.",
     """Design 4 stations on [TOPIC] for [GRADE], [MINUTES] minutes each.

Each station must use a different mode — one hands-on, one reading, one talking, one writing — and must work without me standing there.

For each: the instruction card exactly as students read it, materials (nothing I have to buy), and what I check when I walk past."""),

    # ---- Time & admin ------------------------------------------------------
    ("Time & admin", "The email to your admin", "All grades",
     "Professional, short, and it makes the ask clearly.",
     """Write an email to [ADMINISTRATOR ROLE] about [SITUATION].

I want: [WHAT YOU ACTUALLY WANT]. Tone: professional, brief, not apologetic and not confrontational. Lead with the ask, then the context, then what I have already done. Under 150 words.

Then a one-line version for a hallway conversation."""),

    ("Time & admin", "Behaviour reset script", "All grades",
     "What to say when it goes wrong, prepared in advance.",
     """A [GRADE] student is [DESCRIBE THE BEHAVIOUR]. I want to reset this without a power struggle and without an audience.

Give me: what I say in the moment (under 15 words), what I say to them one-to-one afterwards, and three things NOT to say and why.

Focus on the behaviour and the repair, not on the student's character. This is a classroom conversation, not a diagnosis."""),

    ("Time & admin", "Morning meeting for a whole week", "K-2 · 3-5",
     "Five days of openings, built around one thread.",
     """Plan 5 morning meetings for [GRADE], 10 minutes each, threaded around [THEME].

Each day: a greeting, a share prompt that a shy student can answer in one sentence, and a 2-minute activity. Build across the week so Friday connects back to Monday.

Keep the prompts about things students choose to share, never about home circumstances."""),
]

# Editorial examples, not execution evidence. Exact fictional inputs are shown.
EXAMPLE_INPUTS = {
    "Batch report card drafts from fictional notes":
        "Write two sentences per fictional learner using only these supplied notes. "
        "Do not infer gender or add observations. Student A: strong writer, rushes edits. "
        "Student B: participates, struggles with multi-step problems.",
    "One task, three levels":
        "Create three versions of this Grade 4 math task: compare 1/2 and 3/4 and "
        "explain which is larger. Keep the same fraction-comparison objective. "
        "Include a shared discussion question and an answer key.",
    "The email you have been putting off":
        "Draft an email using this fictional scenario only: Student A asks questions "
        "during discussions. Three practice assignments are missing. I supplied paper "
        "copies and gave reminders. Ask the family for a short conversation to learn "
        "whether there are barriers. Do not invent reasons or pronouns.",
}
SAMPLES = {
    "Batch report card drafts from fictional notes":
        "**Student A**\n\nStudent A shows strength in writing. A useful next step "
        "is to allow time for checking and revising each draft.\n\n"
        "**Student B**\n\nStudent B participates in class. A useful next step "
        "is to write down and check each stage of a multi-step problem.\n\n"
        "**Teacher check:** Replace general wording with verified classroom evidence "
        "locally; do not add evidence that was never observed.",
    "One task, three levels":
        "**Supported task**\n\nDraw two equal-sized rectangles. Split each into four "
        "equal parts. Shade two parts in the first and three in the second. "
        "Complete: 1/2 = __/4. Therefore __ is larger because __.\n\n"
        "**Independent task**\n\nCompare 1/2 and 3/4. Draw a model or use equivalent "
        "fractions to explain your answer in two sentences.\n\n"
        "**Extension task**\n\nFind a fraction strictly between 1/2 and 3/4. "
        "Show why it belongs between them using equivalent fractions.\n\n"
        "**Shared discussion**\n\nWhy must the wholes be the same size when we compare?\n\n"
        "**Answer key**\n\n1/2 = 2/4, so 3/4 is larger. One extension answer "
        "is 5/8 because 1/2 = 4/8 and 3/4 = 6/8. "
        "Check equal-sized wholes and equal partitions.",
    "The email you have been putting off":
        "**Subject: Checking in about practice assignments**\n\n"
        "Hello,\n\nStudent A asks questions during class discussions. "
        "I wanted to check in because three practice assignments are missing. "
        "I have provided paper copies and reminders.\n\n"
        "Could we arrange a short conversation to understand whether any barriers "
        "are making these assignments difficult to complete? We can agree on a manageable "
        "next step together.\n\nThank you.\n\n"
        "**Teacher check:** This is fictional. Confirm every observation before "
        "adapting it locally, and add contact details outside the AI tool.",
}


def render() -> str:
    groups: dict[str, list] = {}
    for group, title, bands, use, prompt in PROMPTS:
        groups.setdefault(group, []).append((title, bands, use, prompt))

    parts = [
        "<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1'>",
        f"<title>{html.escape(TITLE)}</title><style>{CSS}</style></head><body>",
        f"<div class='cover'><h1>{html.escape(TITLE)}</h1>",
        f"<p class='sub'>{html.escape(SUBTITLE)}</p>",
        "<p class='promise'>Includes three editorial examples using fictional data. "
        "These are illustrations, not recorded API outputs or validated classroom results.</p></div>",
        "<h2 id='quick-start'>Start with one task</h2>",
        "<p>Choose one prompt. Fill in task details using fictional or non-identifying material. "
        "Use only an authorized AI service. Check the result and correct it before use. "
        "Record whether it helped; no fixed time saving is promised.</p>",
        "<p>For chained workflows, paste the previous reviewed output into the next step. "
        "Do not assume a new chat remembers another conversation.</p>",
        "<h2 id='contents'>Contents</h2>",
        "<p>" + " | ".join(f"<a href='#group-{i}'>{html.escape(group)}</a>"
                          for i, group in enumerate(groups)) + "</p>",
        f"<div class='note'><strong>Before you start.</strong> {html.escape(SAFETY)}</div>",
    ]

    n = 0
    for group_index, (group, items) in enumerate(groups.items()):
        parts.append(f"<h2 class='section' id='group-{group_index}'>{html.escape(group)}</h2>")
        parts.append(f"<p class='sectionnote'>{len(items)} prompts</p>")
        for title, bands, use, prompt in items:
            n += 1
            prompt += ("\n\nUse only supplied facts and fictional examples. Do not infer identity, "
                       "pronouns, achievements or diagnoses. If key evidence is missing, ask "
                       "instead of inventing it. Review all results before classroom use.")
            parts += [
                "<div class='card'>",
                f"<h3>{n}. {html.escape(title)}</h3>",
                f"<p class='meta'><span>{html.escape(bands)}</span></p>",
                f"<p class='use'>{html.escape(use)}</p>",
                "<p class='label'>The prompt</p>",
                f"<div class='prompt'>{html.escape(prompt)}</div>",
            ]
            if title in SAMPLES:
                parts.append("<div class='output'><p class='label'>Fictional example input</p>")
                parts.append(f"<div class='prompt'>{html.escape(EXAMPLE_INPUTS[title])}</div>")
                parts.append("<p class='label'>Illustrative draft - not a recorded API execution</p>")
                parts.append(_md(SAMPLES[title]))
                parts.append("</div>")
            parts.append("</div>")

    parts += [
        "<h2 class='section' id='next'>Project status and feedback</h2>",
        f"<div class='note'>{html.escape(FOOTER_CTA)}</div>",
        f"<footer><p><a href='{config.PRODUCT['support_url']}'>Project feedback</a>"
        " - do not include any student information.</p></footer></body></html>",
    ]
    return "\n".join(parts)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output-dir", type=Path, default=config.ROOT / "build" / "lead-magnet")
    ap.add_argument("--html-only", action="store_true")
    args = ap.parse_args(argv)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    source = render()
    out_html = args.output_dir / "lead-magnet.html"
    out_html.write_text(source, encoding="utf-8")
    if not args.html_only:
        from steps.pdf_export import export_pdf
        export_pdf(source, args.output_dir / "lead-magnet.pdf", TITLE,
                   "Free development preview - fictional examples; review before use")
    print(f"{len(PROMPTS)} prompts; {len(SAMPLES)} illustrative examples. No API calls.")
    print(f"Files: {args.output_dir}")


if __name__ == "__main__":
    main()
