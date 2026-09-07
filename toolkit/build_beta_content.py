"""Build the hand-curated Phase 3 beta content pack.

The beta deliberately covers every chapter before the remaining 270 prompts are
written. Generated Markdown stays deterministic so editorial changes are reviewable.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "book"


@dataclass(frozen=True)
class Prompt:
    id: str
    folder: str
    subtopic: str
    title: str
    use: str
    inputs: tuple[str, ...]
    deliverable: str
    sections: str
    test_case: str
    grades: str = "3-12"
    subjects: str = "Any"
    sample: bool = False


PROMPTS = (
    Prompt("LP-001", "01-lesson-planning", "complete-lessons", "Build a complete evidence-led lesson", "You need a teachable lesson, not a loose list of activities.", ("GRADE_BAND: learner age or grade", "SUBJECT_AND_TOPIC: exact content", "DURATION_MINUTES: total time", "LEARNING_STANDARD_OR_OBJECTIVE: paste verbatim", "AVAILABLE_MATERIALS: include constraints", "LEARNER_CONTEXT: relevant strengths and needs; no names"), "Create a classroom-ready lesson whose assessment directly measures the supplied objective.", "Return: objective in student-friendly language; timed agenda; teacher moves; student actions; checks for understanding; independent evidence; exit ticket with answer guide; likely misconception and response; materials and preparation.", "Grade 6 science; photosynthesis; 50 minutes; students model matter and energy; board, paper, colored pencils; mixed reading levels.", "3-8", "Science", True),
    Prompt("LP-002", "01-lesson-planning", "backward-unit-planning", "Plan a unit backward from mastery", "You have an end goal and need a coherent learning sequence.", ("GRADE_BAND", "SUBJECT_AND_UNIT", "NUMBER_AND_LENGTH_OF_LESSONS", "FINAL_MASTERY_EXPECTATION", "REQUIRED_STANDARDS", "KNOWN_PRIOR_KNOWLEDGE", "AVAILABLE_RESOURCES"), "Design a backward-planned unit in which every lesson builds toward final mastery.", "Return: unpacked mastery criteria; final assessment; prerequisite map; lesson sequence table; formative checkpoints; reteaching triggers; extension path; resource list; alignment self-check.", "Grade 8 mathematics; linear equations; 8 lessons of 45 minutes; solve and justify one-variable equations; students know integer operations.", "6-12", "Mathematics"),
    Prompt("LP-003", "01-lesson-planning", "standards-and-objectives", "Turn a standard into measurable objectives", "A standard is too broad to teach or assess in one lesson.", ("GRADE_BAND", "SUBJECT", "STANDARD_TEXT: paste exactly", "LESSON_COUNT", "CONTEXT_OR_UNIT"), "Unpack the supplied standard without changing its meaning.", "Return: key nouns and verbs; prerequisite skills; 3-6 measurable objectives; student-friendly 'I can' statements; success criteria; one aligned evidence task per objective; ambiguity questions. Quote the supplied standard exactly before analysis.", "Grade 5 ELA; standard supplied by teacher; 4 lessons; informational text unit.", "K-12", "Any"),
    Prompt("LP-004", "01-lesson-planning", "warm-ups-and-exit-tickets", "Create a matched warm-up and exit ticket", "You want to expose prior knowledge and measure growth in one lesson.", ("GRADE_BAND", "SUBJECT_AND_TOPIC", "OBJECTIVE", "WARM_UP_MINUTES", "EXIT_TICKET_MINUTES", "KNOWN_MISCONCEPTION"), "Create two brief tasks aligned to the same learning target.", "Return: warm-up instructions and answer guide; what each response reveals; bridge into instruction; exit-ticket question and answer guide; 3 response categories (secure/developing/not yet); next-day action for each category.", "Grade 7 science; food webs; explain indirect ecosystem effects; 5 minutes each; students think only directly connected organisms are affected.", "3-12", "Any", True),
    Prompt("LP-005", "01-lesson-planning", "substitute-and-emergency-plans", "Create a no-surprises substitute lesson", "A substitute teacher needs a safe, self-contained plan with minimal preparation.", ("GRADE_BAND", "SUBJECT_AND_TOPIC", "DURATION_MINUTES", "MATERIALS_ALREADY_IN_ROOM", "STUDENT_ROUTINES", "ACCESSIBILITY_NEEDS: non-identifying", "PROHIBITED_ACTIVITIES_OR_RESOURCES"), "Write a substitute plan that another adult can run without guessing.", "Return: one-page overview; minute-by-minute plan; exact directions to read aloud; attendance and safety notes as placeholders; independent task; early-finisher option; answer key; collection procedure; contingency if technology fails. Never invent school procedures.", "Grade 4 social studies; map skills; 55 minutes; atlases and paper; no devices; established pair-share routine.", "K-12", "Any"),
    Prompt("WA-001", "02-worksheets-activities", "practice-worksheets", "Build a focused practice worksheet", "Students need purposeful practice rather than repetitive filler.", ("GRADE_BAND", "SUBJECT_AND_SKILL", "LEARNING_OBJECTIVE", "NUMBER_OF_ITEMS", "DIFFICULTY_RANGE", "ALLOWED_FORMATS", "ACCOMMODATIONS"), "Create a printable worksheet with a deliberate progression and usable answer key.", "Return: title and directions; brief model; items grouped as foundation/application/reasoning; workspace cues; one misconception diagnostic; optional challenge; complete answer key with short explanations; alignment check.", "Grade 6 mathematics; ratio tables; 12 items; easy to moderate; black-and-white printing; larger spacing.", "3-12", "Any", True),
    Prompt("WA-002", "02-worksheets-activities", "learning-stations", "Design four learning stations", "You need varied practice modes with manageable rotations.", ("GRADE_BAND", "SUBJECT_AND_TOPIC", "OBJECTIVE", "CLASS_SIZE", "TOTAL_TIME", "MATERIALS", "ROOM_OR_NOISE_CONSTRAINTS"), "Design four distinct stations that can run simultaneously.", "Return for each station: mode; materials per group; student-facing instruction card; expected product; teacher look-fors; misconception; brief answer guide. Also return groups, rotation timing, transition signal and setup checklist.", "Grade 7 science; ripple effects in ecosystems; 32 students; 48 minutes; paper, dominoes, whiteboards; one quiet station.", "3-12", "Any", True),
    Prompt("WA-003", "02-worksheets-activities", "collaborative-tasks", "Create an accountable group task", "You want collaboration where every learner must think and contribute.", ("GRADE_BAND", "SUBJECT_AND_TOPIC", "OBJECTIVE", "GROUP_SIZE", "TIME", "MATERIALS", "FINAL_PRODUCT"), "Create a group task with individual accountability and equitable roles.", "Return: launch script; roles with real cognitive work; task steps; shared product; individual check; discussion stems; teacher checkpoints; success criteria; conflict/reset protocol; debrief question.", "Grade 9 ELA; evaluating evidence; groups of four; 30 minutes; two short articles; evidence ranking poster.", "6-12", "Any"),
    Prompt("WA-004", "02-worksheets-activities", "review-games", "Build a review game that measures learning", "You need an engaging review without rewarding speed alone.", ("GRADE_BAND", "SUBJECT_AND_SKILLS", "TIME", "NUMBER_OF_STUDENTS", "MATERIALS", "QUESTION_COUNT", "ACCESS_NEEDS"), "Design a low-prep review game with accurate scoring and broad participation.", "Return: setup; rules; question bank by difficulty; answers; participation safeguards; no-speed alternative; teacher data tracker; tie-breaker based on reasoning; five-minute reflection.", "Grade 8 mathematics; one-variable equations; 25 minutes; 28 students; mini-whiteboards; 18 questions.", "3-12", "Any"),
    Prompt("AS-001", "03-assessment-rubrics-quizzes", "quizzes-and-tests", "Create a balanced classroom assessment", "You need a valid assessment with diagnostic distractors.", ("GRADE_BAND", "SUBJECT_AND_SKILLS", "TIME_LIMIT", "ITEM_COUNT", "ITEM_FORMATS", "COGNITIVE_BALANCE", "ACCOMMODATIONS"), "Create an assessment that samples recall, application and reasoning.", "Return: student directions; numbered items; point values; complete answer key; worked solutions where needed; distractor rationale; scoring guide; standards/objective map; two priority items for reteaching analysis.", "Grade 8 mathematics; one-variable linear equations; 20 minutes; 8 items; 5 multiple choice and 3 constructed response.", "3-12", "Any", True),
    Prompt("AS-002", "03-assessment-rubrics-quizzes", "formative-checks-and-exit-tickets", "Create hinge questions for live teaching", "You need quick questions that determine what to do next.", ("GRADE_BAND", "SUBJECT_AND_CONCEPT", "OBJECTIVE", "KNOWN_MISCONCEPTIONS", "NUMBER_OF_QUESTIONS", "RESPONSE_METHOD"), "Write diagnostic hinge questions with unambiguous instructional decisions.", "Return each question with answer/options; correct answer; misconception mapped to each distractor; acceptable response threshold; immediate teacher action for each response pattern. End with a 3-minute exit ticket.", "Grade 5 science; matter conservation; 4 hinge questions; fingers 1-4; students think matter disappears when dissolved.", "3-12", "Any"),
    Prompt("AS-003", "03-assessment-rubrics-quizzes", "rubrics", "Build a student-readable analytic rubric", "A complex product needs transparent, observable criteria.", ("GRADE_BAND", "TASK_DESCRIPTION", "LEARNING_OBJECTIVES", "CRITERIA_COUNT", "PERFORMANCE_LEVELS", "TOTAL_POINTS", "NON_NEGOTIABLES"), "Create a rubric that scores evidence of learning rather than compliance or personality.", "Return: rubric table; observable descriptors for every cell; point calculation; student checklist; calibration examples using fictional work; teacher note on avoiding double-penalties; accessibility review.", "Grade 7 science ecosystem model; 4 criteria; four levels; 16 points; causal arrows and evidence explanation required.", "3-12", "Any", True),
    Prompt("AS-004", "03-assessment-rubrics-quizzes", "diagnosis-and-misconceptions", "Diagnose errors from anonymous work", "You have non-identifying student responses and need instructional patterns.", ("GRADE_BAND", "SUBJECT_AND_SKILL", "TASK_AND_CORRECT_ANSWER", "ANONYMOUS_RESPONSES", "SCORING_CRITERIA", "NUMBER_OF_GROUPS_FOR_RETEACHING"), "Analyze response patterns without inferring ability, motivation or personal traits.", "Return: response-by-response evidence; misconception codes; frequency table; confidence/uncertainty notes; flexible reteaching groups; one targeted mini-task per group; reassessment question. Preserve original responses exactly.", "Grade 6 fractions; compare unlike fractions; 12 responses labeled A-L; three reteaching groups.", "3-12", "Any"),
    Prompt("DF-001", "04-differentiation-mixed-ability", "scaffolds", "Add temporary scaffolds without lowering the goal", "Some learners need access support while keeping the same objective.", ("GRADE_BAND", "SUBJECT_AND_TASK", "UNCHANGED_OBJECTIVE", "OBSERVED_BARRIERS: evidence only", "AVAILABLE_SUPPORTS", "TIME"), "Create fading scaffolds that preserve cognitive demand.", "Return: barrier-to-support map; before/during/after scaffolds; teacher language; visual or sentence supports; checks for independence; fade plan; same-goal success criteria; warning if evidence is insufficient.", "Grade 7 science; explain photosynthesis model; language load and diagram organization barriers; word bank and graphic organizer available.", "K-12", "Any", True),
    Prompt("DF-002", "04-differentiation-mixed-ability", "tiered-tasks", "Create three routes to the same objective", "A mixed-readiness class needs different entry points and one shared destination.", ("GRADE_BAND", "SUBJECT_AND_CORE_TASK", "COMMON_OBJECTIVE", "EVIDENCE_OF_MASTERY", "READINESS_EVIDENCE", "TIME_AND_MATERIALS"), "Create scaffolded, on-level and extension versions with equal curricular dignity.", "Return all three student-facing tasks; what changes and what stays fixed; success criteria; likely misconception and teacher check-question for each; flexible assignment guidance; whole-class discussion bridge.", "Grade 5 mathematics; compare fractions; justify using distance from one; fraction strips available.", "3-12", "Any", True),
    Prompt("DF-003", "04-differentiation-mixed-ability", "multilingual-support", "Make a task accessible to multilingual learners", "Language demands may hide subject understanding.", ("GRADE_BAND", "SUBJECT_AND_TASK", "CONTENT_OBJECTIVE", "LANGUAGE_FUNCTION", "LEARNER_LANGUAGE_PROFILES: no names", "WORDS_THAT_MUST_REMAIN", "AVAILABLE_TRANSLATION_SUPPORT"), "Add language support without replacing content learning or assuming proficiency.", "Return: essential vocabulary with plain definitions; visuals to provide; sentence frames at three support levels; partner rehearsal; model response; home-language use options; content-versus-language observation checklist; fade plan.", "Grade 6 social studies; explain cause and effect in migration; newcomers and intermediate English learners; terms push factor and pull factor must remain.", "K-12", "Any"),
    Prompt("DF-004", "04-differentiation-mixed-ability", "reading-and-accessibility", "Adapt text access while preserving meaning", "Learners need a more accessible route into a demanding source.", ("GRADE_BAND", "ORIGINAL_TEXT", "PURPOSE_FOR_READING", "TERMS_TO_PRESERVE", "ACCESS_NEEDS", "MAX_LENGTH", "ASSESSMENT_BOUNDARY"), "Create access supports while clearly separating any adapted text from the original.", "Return: difficulty analysis; chunked original with headings; glossary; optional plain-language companion; guiding questions; audio/visual suggestions; comprehension checks; statement of what was not changed. Do not claim a reading level without a defined measure.", "Grade 9 biology source passage; identify evidence for natural selection; preserve adaptation, variation and selection pressure.", "3-12", "Any"),
    Prompt("PC-001", "05-parent-communication", "positive-notes", "Write a specific positive family message", "You want to share genuine, evidence-based progress.", ("STUDENT_FIRST_NAME_OR_PLACEHOLDER", "GRADE_AND_SUBJECT", "OBSERVED_ACTION", "LEARNING_OR_COMMUNITY_IMPACT", "TONE", "LENGTH", "LANGUAGE"), "Draft a warm message grounded only in supplied evidence.", "Return: subject line; full message; 50-word version. Keep praise specific, avoid labels, preserve placeholders, and invite—not require—a reply.", "Jordan; Grade 7 science; connected two classmates' ideas during a food-web discussion; helped the group revise its model; warm; under 140 words.", "K-12", "Any"),
    Prompt("PC-002", "05-parent-communication", "concern-emails", "Communicate an academic concern with a next step", "A family needs clear facts and a manageable path forward.", ("STUDENT_FIRST_NAME_OR_PLACEHOLDER", "GRADE_AND_SUBJECT", "STRENGTH_EVIDENCE", "CONCERN_EVIDENCE_AND_DATES", "SUPPORT_ALREADY_OFFERED", "REQUESTED_NEXT_STEP", "AVAILABLE_CONTACT_OPTIONS", "TONE_AND_LENGTH"), "Write a factual, collaborative message without blame, diagnosis or invented context.", "Return: neutral subject; full email; brief version; factual consistency check. Separate observation from interpretation and retain all scheduling details exactly.", "Jordan; Grade 7 science; thoughtful discussion contributions; 2 of 4 tasks submitted over two weeks; written reminders and extra class time; 10-minute call; Thursday 3:30 PM or Friday 8:00 AM.", "K-12", "Any", True),
    Prompt("PC-003", "05-parent-communication", "conference-preparation", "Prepare a balanced family conference", "You need an evidence-led conversation that ends with shared actions.", ("GRADE_AND_SUBJECT", "STRENGTH_EVIDENCE", "LEARNING_EVIDENCE", "ATTENDANCE_OR_BEHAVIOR_FACTS_IF_RELEVANT", "SUPPORTS_TRIED", "FAMILY_INPUT_TO_SEEK", "MEETING_LENGTH"), "Create a conference agenda and talking points without speculating about causes.", "Return: opening; evidence summary; work samples to bring; 3 family questions; student-voice question; shared plan table with owner/date/evidence; follow-up message; statements to avoid.", "Grade 5 mathematics; accurate computation but explanations incomplete; three anonymized work samples; 15-minute conference.", "K-12", "Any"),
    Prompt("PC-004", "05-parent-communication", "newsletters", "Draft a useful class newsletter", "Families need a concise update they can act on.", ("GRADE_AND_CLASS", "DATE_RANGE", "LEARNING_HIGHLIGHTS", "UPCOMING_DATES", "AT_HOME_OPTION", "MATERIALS_OR_PERMISSION_NEEDED", "CONTACT_PLACEHOLDER", "LANGUAGE_AND_LENGTH"), "Draft an accessible newsletter with no invented dates or requirements.", "Return: scannable newsletter; plain-text mobile version; translation-ready version with short sentences; missing-information flags; final date/links checklist.", "Grade 3; October 5-9; multiplication arrays and plant needs; museum form due [DATE]; optional array hunt at home; under 300 words.", "K-8", "Any"),
    Prompt("RC-001", "06-report-card-comments", "comment-banks", "Build an evidence-safe comment bank", "You need reusable comments that still sound specific and humane.", ("GRADE_AND_SUBJECT", "LEARNING_OBJECTIVES", "PERFORMANCE_CATEGORIES", "TONE", "LENGTH_RANGE", "RESTRICTED_WORDS_OR_POLICIES"), "Create modular comments with visible evidence placeholders rather than invented claims.", "Return comments for exceeding/meeting/developing/beginning; each includes strength, evidence placeholder and next step; neutral pronoun variants; repetition audit; prohibited-inference checklist.", "Grade 6 science; model systems and explain evidence; four performance categories; 45-65 words; avoid fixed-ability labels.", "K-12", "Any", True),
    Prompt("RC-002", "06-report-card-comments", "strengths-and-next-steps", "Turn evidence into a balanced report comment", "You have assessment evidence and need a concise, defensible comment.", ("STUDENT_NAME_OR_PLACEHOLDER", "GRADE_AND_SUBJECT", "OBSERVED_STRENGTHS", "SPECIFIC_EVIDENCE", "NEXT_LEARNING_PRIORITY", "SUPPORT_OR_STRATEGY", "WORD_LIMIT"), "Write a report comment using only supplied evidence.", "Return one comment and a fact trace showing which input supports each sentence. Include one actionable next step; avoid personality, effort or home-support claims unless explicitly evidenced.", "[STUDENT]; Grade 8 mathematics; solves two-step equations accurately; 8/10 on quiz; sign errors with distribution; annotate negative signs; 70 words.", "K-12", "Any"),
    Prompt("RC-003", "06-report-card-comments", "tone-and-rewriting", "Rewrite a comment for clarity and fairness", "A draft comment may be vague, harsh or unsupported.", ("ORIGINAL_COMMENT", "VERIFIED_EVIDENCE", "GRADE_AND_SUBJECT", "DESIRED_TONE", "WORD_LIMIT", "SCHOOL_POLICY_NOTES"), "Rewrite the comment while preserving verified facts and removing unsupported judgments.", "Return: revised comment; change log categorized as clarity/tone/evidence/actionability; any claim that cannot be retained; one next-step sentence. Do not soften away a material concern.", "Original: 'Jordan is lazy and never finishes anything.' Evidence: 2 of 4 tasks submitted in two weeks after reminders; Grade 7 science; calm and direct; 60 words.", "K-12", "Any"),
    Prompt("CM-001", "07-classroom-management-sel", "routines-and-transitions", "Design and teach a classroom routine", "A recurring transition is costing time or creating confusion.", ("GRADE_BAND", "ROUTINE_OR_TRANSITION", "CURRENT_OBSERVATIONS", "DESIRED_BEHAVIOR", "TIME_TARGET", "ROOM_CONSTRAINTS", "SCHOOL_EXPECTATIONS"), "Create an explicitly taught routine, not a punishment system.", "Return: observable steps; teacher script; visual cue; model/non-model practice; feedback language; 5-day rehearsal plan; simple time/data tracker; reset procedure; accessibility considerations.", "Grade 4; move from carpet to tables; takes 4 minutes with materials forgotten; goal 90 seconds; narrow aisle.", "K-12", "Any", True),
    Prompt("CM-002", "07-classroom-management-sel", "restorative-conversations", "Prepare a restorative conversation", "A classroom harm needs acknowledgment, repair and reintegration.", ("AGE_OR_GRADE", "OBSERVABLE_INCIDENT_FACTS", "PEOPLE_INVOLVED_AS_ROLES", "IMMEDIATE_SAFETY_ACTIONS", "POLICY_REQUIREMENTS", "CONVERSATION_LENGTH", "KNOWN_NEEDS_OR_ACCOMMODATIONS"), "Create a voluntary, developmentally appropriate conversation guide; do not determine guilt or replace required safeguarding.", "Return: readiness check; private opening; neutral fact statement; questions about impact and needs; repair options; agreement template; follow-up; escalation/safeguarding boundaries; phrases to avoid.", "Grade 8; one student mocked another's presentation; teacher stopped comments and separated seating; school incident log required; 10 minutes.", "K-12", "Any"),
    Prompt("AD-001", "08-teacher-admin-paperwork", "agendas-and-minutes", "Turn notes into accountable meeting minutes", "A team needs concise decisions and next actions from rough notes.", ("MEETING_NAME_AND_DATE", "ATTENDEE_ROLES", "AGENDA", "ROUGH_NOTES", "CONFIRMED_DECISIONS", "ACTION_OWNERS_AND_DATES", "CONFIDENTIALITY_RULES"), "Produce factual minutes without inventing consensus, owners or deadlines.", "Return: attendees; agenda summary; decisions; action table; parking lot; unresolved questions; next meeting placeholder; verification flags. Mark unclear statements as [CONFIRM].", "Grade-level planning meeting; anonymized notes; three confirmed decisions; two tentative actions missing owners.", "K-12", "Any", True),
    Prompt("AD-002", "08-teacher-admin-paperwork", "professional-goals", "Draft a measurable professional growth goal", "You need a goal connected to learner evidence and realistic teacher actions.", ("FOCUS_AREA", "BASELINE_EVIDENCE", "DESIRED_OUTCOME", "TIMEFRAME", "AVAILABLE_ACTIONS_OR_PD", "EVIDENCE_SOURCES", "CONSTRAINTS"), "Create a measurable growth plan without promising results outside the teacher's control.", "Return: goal statement; rationale; monthly actions; leading and outcome indicators; evidence collection; midpoint decision rules; support requested; reflection questions; privacy safeguards.", "Increase quality of student mathematical explanations; baseline rubric average 1.8/4 across anonymous class work; one semester; weekly worked-example discussion.", "K-12", "Any"),
    Prompt("SD-001", "09-subject-deep-dives", "mathematics", "Create a concept-first mathematics explanation", "Students can follow a procedure but need the underlying idea.", ("GRADE_BAND", "CONCEPT", "PRIOR_KNOWLEDGE", "KNOWN_MISCONCEPTION", "REPRESENTATIONS_AVAILABLE", "EXAMPLE_AND_NON_EXAMPLE", "TIME"), "Create a mathematically accurate explanation connecting concrete, visual and symbolic representations.", "Return: concept statement; prerequisite check; representation sequence; teacher think-aloud; worked example; non-example; hinge question with distractors; guided task; independent transfer; answer guide.", "Grade 5; compare fractions near one; unit fractions understood; misconception that larger denominator means larger value; fraction strips and number lines.", "3-12", "Mathematics", True),
    Prompt("SD-002", "09-subject-deep-dives", "science", "Design an evidence-based science investigation", "Students need to investigate a testable question safely.", ("GRADE_BAND", "SCIENCE_TOPIC", "LEARNING_OBJECTIVE", "AVAILABLE_MATERIALS", "TIME", "SAFETY_RULES", "VARIABLES_OR_PHENOMENON", "DATA_FORMAT"), "Design a feasible investigation and distinguish observation from explanation.", "Return: question; prediction prompt; variables; controls; safety check; numbered procedure; data table; analysis questions; claim-evidence-reasoning task; expected pattern, not fabricated results; limitations; cleanup.", "Grade 6; factors affecting dissolving rate; water, cups, sugar, spoons, thermometers; 40 minutes; no tasting; temperature as variable.", "3-12", "Science"),
)


WORKFLOWS = (
    ("WF-001", "standard-to-complete-unit", "Standard to complete unit", "Turn one supplied standard into an aligned unit, assessment and daily sequence.", ("Paste the standard verbatim and list constraints.", "Unpack knowledge, skills and mastery criteria; teacher reviews.", "Draft the final assessment and rubric; teacher corrects content and accessibility.", "Build the lesson sequence backward from the approved assessment.", "Run an alignment audit and produce the final unit pack.")),
    ("WF-002", "mixed-ability-lesson", "Mixed-ability lesson pack", "Create one common-goal lesson with evidence-based access routes.", ("Define the unchanged objective and mastery evidence.", "Describe observed barriers without names or labels.", "Create core lesson and formative checks.", "Create scaffolded, on-level and extension routes; teacher reviews parity.", "Add grouping, fade plan and next-day decision rules.")),
    ("WF-003", "incident-to-parent-conversation", "Incident to parent conversation", "Move from verified classroom facts to a calm, policy-aligned family conversation.", ("Record observable facts, immediate actions and applicable policy.", "Separate facts, unknowns and interpretations; teacher verifies.", "Draft neutral contact message with placeholders.", "Prepare questions, support options and an action-plan table.", "Document agreed actions and schedule follow-up without adding new claims.")),
)


def slug(title: str) -> str:
    return "-".join("".join(ch.lower() if ch.isalnum() else " " for ch in title).split())


def prompt_markdown(p: Prompt) -> str:
    inputs = "\n".join(f"- `[{value}]`" for value in p.inputs)
    sample = (
        "A strong response should preserve every supplied fact, follow the requested sections, "
        "include usable teacher-facing details, and flag any missing information instead of inventing it."
        if p.sample else "Not included in this edition."
    )
    prompt_text = f"""You are an experienced K-12 instructional planning assistant.\n\nTeacher inputs:\n{inputs}\n\nTask:\n{p.deliverable}\n\nRequired output:\n{p.sections}\n\nRules:\n- Use only the facts supplied. Mark missing essentials as [NEEDS TEACHER INPUT].\n- Do not include identifiable student data or infer disability, motivation, family circumstances, or diagnosis.\n- Keep the named grade, time, materials, objective, and policy constraints unchanged.\n- Make student-facing language clear and age-appropriate.\n- Check subject accuracy, feasibility, accessibility, and alignment before the final answer.\n- End with a short TEACHER VERIFICATION checklist."""
    return f'''---
{{
  "id": "{p.id}",
  "slug": "{slug(p.title)}",
  "chapter": "{p.folder.split('-', 1)[1]}",
  "subtopic": "{p.subtopic}",
  "title": "{p.title}",
  "grade_bands": ["{p.grades}"],
  "subjects": ["{p.subjects}"],
  "sensitivity": "standard",
  "sample_output": {str(p.sample).lower()},
  "review_status": "draft",
  "content_version": 1
}}
---

# {p.title}

## Use this when

{p.use}

## Teacher inputs

{inputs}

## Copy-paste prompt

```text
{prompt_text}
```

## Fictional test case

{p.test_case}

## Sample output

{sample}

## Teacher verification checklist

- [ ] Every fact can be traced to the teacher inputs.
- [ ] Content, answers and examples are accurate.
- [ ] Timing, materials and difficulty are feasible.
- [ ] Accessibility supports preserve the learning goal.
- [ ] A teacher reviews the result before classroom or family use.

## Editorial notes

Phase 3 beta draft. Cross-tool model testing and qualified human review are pending.
'''


def workflow_markdown(item: tuple[str, str, str, str, tuple[str, ...]]) -> str:
    wid, subtopic, title, purpose, steps = item
    rendered_steps = "\n".join(f"{i}. {step}" for i, step in enumerate(steps, 1))
    return f'''---
{{
  "id": "{wid}",
  "slug": "{slug(title)}",
  "chapter": "multi-step-workflows",
  "subtopic": "{subtopic}",
  "title": "{title}",
  "sensitivity": "standard",
  "review_status": "draft",
  "content_version": 1
}}
---

# {title}

## Outcome

{purpose}

## Teacher inputs

- `[VERBATIM_SOURCE_MATERIAL]`
- `[GRADE_SUBJECT_AND_CONTEXT]`
- `[TIME_MATERIALS_AND_POLICY_CONSTRAINTS]`
- `[NON_IDENTIFYING_EVIDENCE]`

## Workflow

{rendered_steps}

At every step, paste the previous **reviewed** output into the next prompt. Correct errors
before continuing; never allow the model to silently replace supplied facts.

## Copy-paste controller prompt

```text
Guide me through this workflow one step at a time. At each step: state the required
inputs, produce only the requested artifact, list uncertainties, and stop for teacher
review. Do not continue until I reply APPROVED or provide corrections. Preserve source
wording where requested, never invent school policy or student facts, and finish with
an alignment, privacy, accuracy and feasibility audit.
```

## Fictional end-to-end example

Context: Grade 7 science, a fictional ecosystem unit, 45-minute lessons, paper-based
materials, and anonymous evidence only. The teacher supplies the objective and constraints,
reviews each intermediate artifact, corrects any science or timing issue, and approves the
final pack only after checking alignment, accessibility, privacy and school policy.

## Review checklist

- [ ] Every stage uses the previous reviewed output.
- [ ] Unknown facts remain visible placeholders.
- [ ] No identifiable student information is present.
- [ ] Final artifacts align to one another and to the supplied goal.
- [ ] A qualified teacher has approved the current content fingerprint.
'''


def main() -> None:
    for p in PROMPTS:
        target = BOOK / "chapters" / p.folder / "prompts" / f"{p.id.lower()}-{slug(p.title)}.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(prompt_markdown(p), encoding="utf-8")

    workflow_dir = BOOK / "chapters" / "10-multi-step-workflows" / "workflows"
    workflow_dir.mkdir(parents=True, exist_ok=True)
    for workflow in WORKFLOWS:
        target = workflow_dir / f"{workflow[0].lower()}-{slug(workflow[2])}.md"
        target.write_text(workflow_markdown(workflow), encoding="utf-8")

    print(f"Built {len(PROMPTS)} prompts and {len(WORKFLOWS)} workflows.")


if __name__ == "__main__":
    main()
