"""Build the complete 300-prompt and 12-workflow source draft.

The first 30 prompts are hand-curated anchors. The remaining content follows the
same deterministic, reviewable format without a separate beta gate.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
import json
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


PREFIXES = {
    "01-lesson-planning": "LP", "02-worksheets-activities": "WA",
    "03-assessment-rubrics-quizzes": "AS", "04-differentiation-mixed-ability": "DF",
    "05-parent-communication": "PC", "06-report-card-comments": "RC",
    "07-classroom-management-sel": "CM", "08-teacher-admin-paperwork": "AD",
    "09-subject-deep-dives": "SD",
}

VARIANTS = (
    ("Create", "from a supplied objective"),
    ("Adapt", "for limited time and materials"),
    ("Review", "for alignment and accuracy"),
    ("Simplify", "without lowering the learning goal"),
    ("Extend", "for deeper reasoning and transfer"),
    ("Differentiate", "for mixed readiness"),
    ("Audit", "for accessibility and inclusion"),
    ("Turn evidence into", "with clear next steps"),
    ("Build a low-prep", "for tomorrow's class"),
    ("Create a collaborative", "with individual accountability"),
    ("Create an independent", "with a usable answer guide"),
    ("Improve", "using teacher feedback"),
)

CHAPTER_GUIDANCE = {
    "01-lesson-planning": (
        "a classroom-ready instructional plan",
        "objective and success criteria; timed sequence; teacher moves; student actions; checks for understanding; independent evidence; misconceptions; materials; adaptations; teacher verification",
    ),
    "02-worksheets-activities": (
        "a purposeful student activity with an answer or observation guide",
        "student-facing directions; model or launch; sequenced tasks; expected product; participation structure; answer guide; misconception check; extension; accessibility check",
    ),
    "03-assessment-rubrics-quizzes": (
        "a valid classroom assessment resource aligned to the supplied objective",
        "student directions; assessment content; points or criteria; complete key; diagnostic rationale; scoring guidance; reteaching decisions; alignment audit",
    ),
    "04-differentiation-mixed-ability": (
        "an access plan that preserves the same learning goal",
        "unchanged objective; observed barrier map; temporary supports; student-facing version; teacher prompts; success evidence; fade plan; equity and accessibility audit",
    ),
    "05-parent-communication": (
        "a factual, respectful family communication draft",
        "subject line; full version; brief mobile version; supplied evidence; clear next step; invitation to respond; missing-information flags; tone and privacy audit",
    ),
    "06-report-card-comments": (
        "a concise report-card resource grounded only in verified evidence",
        "final comment or bank; strength; evidence placeholder; actionable next step; length check; fact trace; fairness and prohibited-inference audit",
    ),
    "07-classroom-management-sel": (
        "a preventive, teachable and restorative classroom support",
        "observable goal; teacher language; student steps; practice plan; response options; follow-up; data check; accessibility, safety and policy boundaries",
    ),
    "08-teacher-admin-paperwork": (
        "a concise administrative document that does not invent decisions",
        "purpose; polished document; owners and dates as supplied; action table; unresolved questions; [CONFIRM] flags; privacy and policy check",
    ),
    "09-subject-deep-dives": (
        "a subject-accurate teaching resource connecting concepts, evidence and transfer",
        "core concept; prerequisites; accurate model; worked example; misconception diagnostic; guided application; independent transfer; answer guide; subject-accuracy audit",
    ),
}

SAMPLE_ALLOCATIONS = {
    "01-lesson-planning": 12, "02-worksheets-activities": 8,
    "03-assessment-rubrics-quizzes": 8, "04-differentiation-mixed-ability": 7,
    "05-parent-communication": 6, "06-report-card-comments": 6,
    "07-classroom-management-sel": 5, "08-teacher-admin-paperwork": 4,
    "09-subject-deep-dives": 4,
}

SAMPLE_OUTPUTS = {
    "01-lesson-planning": """**Illustrative excerpt — Grade 6 science, 50 minutes**

**Objective:** I can draw and label a model showing how a plant uses sunlight, water and
carbon dioxide to make sugar and release oxygen.

**Sequence:** 0-5 min: students answer, “Where does a plant's food come from?” 5-15 min:
teacher models a plant as a solar-powered food factory and labels three inputs and two
outputs. 15-30 min: pairs sort input/output cards and justify each placement. 30-43 min:
students independently draw an arrow model and add a one-sentence explanation. 43-50 min:
exit ticket—“Can a watered plant make sugar without carbon dioxide? Explain using *input*.”

**Evidence:** A secure response shows all five substances in the correct direction and
explains that sugar is made rather than absorbed from soil. **Reteach trigger:** If more
than 25% label sugar as an input, begin the next lesson with a carbon-source model.""",
    "02-worksheets-activities": """**Illustrative excerpt — Grade 7 ecosystem activity**

**Directions:** Arrange Sunlight → Algae → Snails → Perch → Herons. Remove the snail card,
then annotate every downstream effect with ↑, ↓ or ? and one reason.

1. Which organism loses its immediate food source? Explain.
2. Why can herons be affected even though they do not eat snails?
3. Predict one change to algae and state what additional evidence you would need.

**Answer guide:** Perch decrease because their prey is missing; herons may later decrease
because fewer perch are available. Algae may increase as grazing falls, although a firm
claim requires information about other grazers and limiting factors. Award reasoning,
not the arrow alone. A response saying only perch change reveals a broken-chain
misconception and should receive a short food-web tracing task.""",
    "03-assessment-rubrics-quizzes": """**Illustrative excerpt — Grade 8 linear equations**

1. Solve `x - 9 = -4`. A −13, B 5, C 13, D −5. **Answer: B.** Choosing A suggests the
same operation was used instead of the inverse.
2. Solve `4(y - 3) = 20` and show each step. **Answer:** `y = 8`.
3. Explain why `6x + 4 = 2(3x + 5)` has no solution. **Answer:** expanding gives
`6x + 4 = 6x + 10`; subtracting `6x` leaves the false statement `4 = 10`.

**Decision rule:** 3/3 secure; 2/3 check the error code; 0-1/3 reteach inverse operations
with balance models. Inspect Question 3 first when deciding whether learners distinguish
no solution from infinitely many solutions.""",
    "04-differentiation-mixed-ability": """**Illustrative excerpt — one goal, three access routes**

**Common goal:** Compare 3/4 and 5/6 and justify the comparison using distance from one.

**Scaffolded route:** Use equal-length fraction strips, label each missing piece, and
complete: “___ is closer to one because it is missing ___.”
**On-level route:** Prove the comparison using both missing pieces and twelfths.
**Extension route:** Generalize the comparison of `(n−1)/n` and explain what happens as
`n` increases.

All routes require the same conclusion and justification: `5/6 > 3/4`; `3/4` is `1/4`
from one while `5/6` is `1/6` from one. Supports change representation and language,
not the mathematical target. Remove the sentence frame once the learner explains the
relationship independently.""",
    "05-parent-communication": """**Illustrative email — all names and details are fictional**

**Subject: Science progress and brief check-in for Jordan**

Dear Mr. and Mrs. Lee,

Jordan regularly contributes thoughtful ideas during our Grade 7 science discussions.
Over the past two weeks, Jordan has submitted two of four assigned classwork tasks. I
have provided written reminders and additional classroom time; two tasks remain.

Could we arrange a 10-minute call to make a manageable completion plan? I am available
Thursday at 3:30 PM or Friday at 8:00 AM. Please let me know whether either time works.

Sincerely,

[TEACHER NAME]

[SCHOOL CONTACT]

**Teacher check:** Verify recipients, dates, assignment record, time zone and school
communication policy before sending.""",
    "06-report-card-comments": """**Illustrative comment — fictional evidence**

Jordan accurately solves one- and two-step equations and demonstrated this on 8 of 10
items in the latest classroom assessment. Written work is clearest when each inverse
operation is shown on a separate line. The next priority is distributing negative signs
consistently across parentheses. Annotating the sign before simplifying will help Jordan
check this step independently.

**Fact trace:** “8 of 10” comes from the supplied assessment record; “negative signs”
comes from the supplied error pattern; the suggested annotation is the teacher-provided
strategy. No claim is made about effort, personality, support at home or future results.""",
    "07-classroom-management-sel": """**Illustrative routine — Grade 4 table transition**

**Observable goal:** Move from carpet spots to assigned tables with materials ready in
90 seconds. **Teach:** “When the chime sounds: freeze, point to your table, pick up the
named material, walk on the outside lane, begin the displayed starter.” Model once,
model a common error, then let students identify the difference.

Practise twice without removing learning time as a penalty. Give neutral feedback:
“Twenty-two learners began the starter; six still needed materials.” Track time and
missing-material counts for five days. If the narrow aisle causes congestion, dismiss
the far row first. Re-teach the step that breaks down rather than labelling the class.
Follow existing safety and accessibility plans.""",
    "08-teacher-admin-paperwork": """**Illustrative meeting-minutes excerpt**

**Grade 6 planning meeting — [DATE]**
**Decision:** Use one common exit-ticket question in all three mathematics sections next
week. **Evidence reviewed:** anonymous responses from the prior fraction lesson.

| Action | Owner | Due | Evidence of completion |
|---|---|---|---|
| Draft common question | Ms. Rivera | [DATE] | Question shared with team |
| Confirm printing | [CONFIRM] | [DATE] | Sets placed in mailboxes |
| Bring response counts | Each teacher | Next meeting | 3-category tally |

**Unresolved:** The notes mention intervention time but do not identify an owner or
schedule; retain this as `[CONFIRM]` rather than inventing agreement.""",
    "09-subject-deep-dives": """**Illustrative concept explanation — fractions near one**

Both 3/4 and 5/6 are one unit fraction short of a whole, but the missing pieces are not
the same size. Fourths are larger pieces than sixths, so 1/4 > 1/6. Therefore subtracting
1/6 from one leaves more than subtracting 1/4: `5/6 > 3/4`.

**Representation:** Draw two equal number lines from 0 to 1 and mark the unfilled final
interval on each. **Hinge question:** “Two pizzas each have one slice missing. Must the
amount left be equal?” Correct response: no; the original partitions determine slice
size. **Transfer:** Order 2/3, 7/8 and 11/12 without common denominators. Answer:
`2/3 < 7/8 < 11/12`, because the missing unit fractions decrease.""",
}

# Chapter 1 is written as 60 distinct teacher jobs rather than repeated variations of
# one generic shell. Indexes match the manifest allocation within each subtopic.
LESSON_PLANNING_TITLES = {
    "complete-lessons": (
        "Build a complete evidence-led lesson",
        "Plan a concept-development lesson from prior knowledge",
        "Plan an inquiry lesson around a puzzling phenomenon",
        "Create an explicit-instruction lesson with guided release",
        "Design a discussion-centered lesson with equitable participation",
        "Build a no-technology lesson using basic classroom materials",
        "Create a lesson around one complex text or source",
        "Plan a safe hands-on investigation lesson",
        "Design a problem-based mathematics lesson",
        "Compress a full lesson into a purposeful 30-minute period",
        "Expand a lesson for a 90-minute block without filler",
        "Repair a draft lesson whose activities do not match its objective",
    ),
    "backward-unit-planning": (
        "Plan a unit backward from mastery",
        "Unpack final mastery into a prerequisite learning map",
        "Design a final performance task before planning daily lessons",
        "Create a coherent lesson sequence from an approved assessment",
        "Place formative checkpoints and reteaching decisions across a unit",
        "Audit a unit for gaps, repetition and cognitive progression",
        "Shorten a unit while protecting its essential learning",
        "Add transfer and reflection to the end of a unit",
    ),
    "standards-and-objectives": (
        "Turn a standard into measurable objectives",
        "Separate knowledge, skill and reasoning within a standard",
        "Rewrite a technical objective as a student-friendly I-can statement",
        "Create observable success criteria for an existing objective",
        "Check whether an activity truly aligns to a supplied standard",
        "Map several objectives into a logical teaching order",
        "Identify prerequisite skills without lowering the grade-level target",
        "Write evidence statements showing what mastery would look like",
    ),
    "warm-ups-and-exit-tickets": (
        "Create a matched warm-up and exit ticket",
        "Design a warm-up that exposes prior knowledge in five minutes",
        "Write a misconception-revealing hinge question",
        "Create an exit ticket with secure, developing and not-yet response bands",
        "Turn yesterday's exit-ticket patterns into today's opening task",
        "Build a retrieval-practice warm-up without introducing new content",
        "Create a transfer exit ticket that cannot be answered by copying",
        "Audit an exit ticket for alignment, ambiguity and reading load",
    ),
    "pacing-and-transitions": (
        "Build a realistic minute-by-minute lesson timeline",
        "Diagnose where a lesson is likely to run out of time",
        "Write concise transitions between lesson segments",
        "Create a pacing contingency when discussion runs long",
        "Plan meaningful early-finisher work connected to the objective",
        "Adapt one lesson for both a regular period and a shortened schedule",
    ),
    "substitute-and-emergency-plans": (
        "Create a no-surprises substitute lesson",
        "Build an emergency no-print lesson from materials already in the room",
        "Write exact substitute directions that require no subject guessing",
        "Create a technology-failure backup for a digital lesson",
        "Prepare an independent catch-up lesson for an unexpected absence",
        "Audit a substitute plan for safety, clarity and collection procedures",
    ),
    "projects-and-interdisciplinary-lessons": (
        "Launch a project with a clear driving question and final product",
        "Connect two subjects around one authentic problem",
        "Break a multiweek project into milestones and checkpoints",
        "Create individual accountability inside a group project",
        "Design a project rubric that measures learning rather than decoration",
        "Plan a public-product option that protects student privacy",
    ),
    "reflection-and-adaptation": (
        "Turn lesson evidence into a next-day adjustment",
        "Write a post-lesson reflection based on observations rather than feelings alone",
        "Identify what to keep, change and investigate after a lesson",
        "Adapt a lesson after most learners miss the same misconception",
        "Plan targeted follow-up for three anonymous response patterns",
        "Compare the intended lesson with what learners actually demonstrated",
    ),
}

WORKSHEET_ACTIVITY_TITLES = {
    "practice-worksheets": (
        "Build a focused practice worksheet",
        "Create practice that moves from a model to independent work",
        "Write a worksheet that targets one common misconception",
        "Build mixed practice that requires learners to choose a strategy",
        "Create a short retrieval worksheet for previously taught skills",
        "Design an application worksheet using realistic classroom contexts",
        "Adapt a worksheet for black-and-white printing and limited space",
        "Create an error-analysis worksheet from fictional student work",
        "Write a worksheet with foundation, application and reasoning sections",
        "Audit and repair a worksheet whose questions are repetitive or unclear",
    ),
    "learning-stations": (
        "Design four learning stations",
        "Create hands-on, reading, discussion and writing stations",
        "Plan station rotations for a large class and small room",
        "Build self-checking stations that do not depend on the teacher",
        "Create one quiet station and three collaborative stations",
        "Differentiate station access while preserving one shared objective",
        "Design a teacher-led reteaching station from exit-ticket evidence",
        "Audit station directions, timing, materials and accountability",
    ),
    "collaborative-tasks": (
        "Create an accountable group task",
        "Design a jigsaw task where every learner holds essential information",
        "Build a group investigation with rotating cognitive roles",
        "Create a consensus task that requires evidence and disagreement",
        "Turn an individual worksheet into meaningful collaborative reasoning",
        "Audit a group task for participation, access and individual evidence",
    ),
    "review-games": (
        "Build a review game that measures learning",
        "Create a no-speed review game using mini-whiteboards",
        "Design a team review game with individual accountability",
        "Build a misconception challenge using diagnostic distractors",
        "Create a low-prep review game with paper question cards",
        "Audit a review game for fairness, accuracy and useful teacher data",
    ),
    "homework-sets": (
        "Create a short homework set with a clear purpose",
        "Build homework that mixes retrieval and current learning",
        "Design homework with a meaningful no-internet option",
        "Create a family-readable homework guide without requiring family teaching",
        "Audit a homework set for workload, access and answer-key accuracy",
    ),
    "project-briefs": (
        "Write a student-ready project brief from a supplied objective",
        "Create project milestones, checkpoints and submission requirements",
        "Design a choice-based project with equivalent learning demands",
        "Build a group-project brief with individual evidence of mastery",
        "Audit a project brief for clarity, feasibility and privacy",
    ),
}

ASSESSMENT_TITLES = {
    "quizzes-and-tests": (
        "Create a balanced classroom assessment",
        "Build a short quiz across recall, application and reasoning",
        "Write diagnostic multiple-choice questions with purposeful distractors",
        "Create a constructed-response assessment with a scoring guide",
        "Design a pre-assessment that separates prerequisite and grade-level skills",
        "Build a cumulative assessment without over-weighting recent lessons",
        "Adapt an assessment for a shorter testing period",
        "Create parallel assessment forms with equivalent demand",
        "Audit a test for alignment, ambiguity and answer-key errors",
        "Turn a supplied objective list into a complete assessment blueprint",
    ),
    "formative-checks-and-exit-tickets": (
        "Create hinge questions for live teaching",
        "Build a five-minute check for understanding during instruction",
        "Write an exit ticket that distinguishes three levels of understanding",
        "Create a misconception poll with actionable response options",
        "Design a show-me task using mini-whiteboards or paper",
        "Turn anonymous responses into a next-day formative check",
        "Create a transfer question that reveals reasoning rather than recall",
        "Audit a formative check for speed, reading load and decision usefulness",
    ),
    "rubrics": (
        "Build a student-readable analytic rubric",
        "Create observable descriptors for four performance levels",
        "Turn an objective and task into aligned rubric criteria",
        "Build a single-point rubric with feedback space",
        "Create a rubric for collaborative work with individual evidence",
        "Rewrite vague rubric words as observable evidence",
        "Calibrate a rubric using fictional work samples",
        "Audit a rubric for double penalties, bias and irrelevant criteria",
    ),
    "diagnosis-and-misconceptions": (
        "Diagnose errors from anonymous work",
        "Code anonymous responses by misconception rather than score alone",
        "Build flexible reteaching groups from response patterns",
        "Distinguish a careless slip from a conceptual misunderstanding",
        "Create targeted mini-tasks for three misconception groups",
        "Plan a reassessment that shows whether reteaching worked",
    ),
    "answer-keys-and-feedback": (
        "Create a complete worked answer key from verified questions",
        "Write actionable feedback matched to common response patterns",
        "Audit an answer key for mathematical, factual and scoring errors",
        "Create learner-friendly solution explanations without hiding reasoning",
    ),
    "standards-based-grading": (
        "Map assessment evidence to supplied standards and objectives",
        "Create a standards-based proficiency scale with observable evidence",
        "Summarize class mastery without averaging unrelated skills",
        "Audit a standards-based grade summary for missing or weak evidence",
    ),
}

DIFFERENTIATION_TITLES = {
    "scaffolds": (
        "Add temporary scaffolds without lowering the goal",
        "Turn an observed barrier into a targeted support plan",
        "Create a graphic organizer that preserves essential reasoning",
        "Write sentence frames at three levels of language support",
        "Break a complex task into checkpoints without doing the thinking",
        "Add worked examples and prompts with a clear fade plan",
        "Create a scaffold menu learners can choose from responsibly",
        "Audit classroom supports for dependence and hidden lower expectations",
    ),
    "tiered-tasks": (
        "Create three routes to the same objective",
        "Build scaffolded, on-level and extension versions of one task",
        "Tier a task by representation rather than by easier content",
        "Create three entry points with one common mastery product",
        "Design tiered questions that move from access to transfer",
        "Check that every tier carries equal curricular dignity",
        "Create a whole-class debrief that reconnects three task versions",
    ),
    "multilingual-support": (
        "Make a task accessible to multilingual learners",
        "Identify the language demands hidden inside a subject task",
        "Build an essential vocabulary preview with visuals and examples",
        "Create structured partner rehearsal before independent writing",
        "Plan purposeful home-language use without assuming proficiency",
        "Separate content evidence from English-language evidence",
    ),
    "reading-and-accessibility": (
        "Adapt text access while preserving meaning",
        "Chunk a demanding source without rewriting its claims",
        "Create a plain-language companion beside the original text",
        "Add glossary, guiding questions and audio-access suggestions",
        "Reduce unnecessary reading load in a non-reading assessment",
        "Audit adapted materials for lost meaning or unsupported simplification",
    ),
    "extensions": (
        "Create an extension that deepens reasoning instead of adding more work",
        "Build a transfer challenge using a new context",
        "Design an open-ended investigation with clear evidence expectations",
        "Audit an extension for novelty, rigor and connection to the objective",
    ),
    "flexible-grouping": (
        "Build temporary groups from anonymous learning evidence",
        "Create a rotation plan for three changing instructional needs",
        "Plan mixed-readiness groups with meaningful roles and accountability",
        "Audit a grouping plan for labels, access, movement and regrouping triggers",
    ),
}

PARENT_COMMUNICATION_TITLES = {
    "positive-notes": (
        "Write a specific positive family message",
        "Share academic growth using one concrete classroom example",
        "Recognize a learner's helpful contribution without using labels",
        "Write a brief celebration message suitable for a mobile screen",
        "Create a positive note that invites the learner's own reflection",
        "Build a reusable strength-note template with visible evidence fields",
    ),
    "concern-emails": (
        "Communicate an academic concern with a next step",
        "Write a missing-work message using dates and verified counts",
        "Explain a recurring learning difficulty without diagnosing its cause",
        "Request a brief family check-in with two exact scheduling options",
        "Revise a blaming concern email into factual collaborative language",
        "Audit a concern message for evidence, tone and unsupported claims",
    ),
    "conference-preparation": (
        "Prepare a balanced family conference",
        "Build a 15-minute conference agenda around learning evidence",
        "Prepare questions that invite family and student perspective",
        "Turn classroom evidence into a shared action-plan table",
        "Write a factual post-conference summary with owners and dates",
    ),
    "newsletters": (
        "Draft a useful class newsletter",
        "Create a concise weekly learning update for families",
        "Rewrite a newsletter as a mobile-friendly plain-text version",
        "Audit a class newsletter for dates, jargon, access and action items",
    ),
    "permissions-and-logistics": (
        "Draft a permission notice from verified trip or event details",
        "Create a clear family checklist for materials, dates and return forms",
        "Write a schedule-change notice without inventing school policy",
        "Audit a logistics message for missing consent, safety and contact details",
    ),
    "clear-and-accessible-language": (
        "Rewrite school language in plain family-friendly English",
        "Create a translation-ready message using short unambiguous sentences",
        "Audit a family message for jargon, idioms and hidden assumptions",
    ),
    "difficult-conversations": (
        "Prepare a calm conversation about a repeated classroom concern",
        "Create a fact-based communication plan for disagreement with a family",
    ),
}

TITLE_CATALOGS = {
    "01-lesson-planning": LESSON_PLANNING_TITLES,
    "02-worksheets-activities": WORKSHEET_ACTIVITY_TITLES,
    "03-assessment-rubrics-quizzes": ASSESSMENT_TITLES,
    "04-differentiation-mixed-ability": DIFFERENTIATION_TITLES,
    "05-parent-communication": PARENT_COMMUNICATION_TITLES,
}

WORKFLOW_TITLES = {
    "standard-to-assessment": "Standard to aligned assessment",
    "emergency-substitute-pack": "Emergency substitute pack",
    "project-launch-pack": "Project launch pack",
    "parent-conference-pack": "Parent conference pack",
    "intervention-plan-draft": "Evidence to intervention-plan draft",
    "field-trip-pack": "Field-trip planning pack",
    "weekly-admin-pack": "Weekly teacher admin pack",
    "class-data-reflection": "Class data reflection",
    "scores-to-report-comments": "Scores to report comments",
}


def slug(title: str) -> str:
    return "-".join("".join(ch.lower() if ch.isalnum() else " " for ch in title).split())


def prompt_markdown(p: Prompt) -> str:
    inputs = "\n".join(f"- `[{value}]`" for value in p.inputs)
    sample = SAMPLE_OUTPUTS[p.folder] if p.sample else "Not included in this edition."
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

Full-book content draft. Final editorial review is pending.
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


def generated_prompt(
    pid: str, folder: str, subtopic: str, ordinal: int
) -> Prompt:
    display = subtopic.replace("-and-", " & ").replace("-", " ")
    action, qualifier = VARIANTS[(ordinal - 1) % len(VARIANTS)]
    product, sections = CHAPTER_GUIDANCE[folder]
    if folder in TITLE_CATALOGS:
        title = TITLE_CATALOGS[folder][subtopic][ordinal - 1]
    else:
        title = f"{action} {display} {qualifier}"
    return Prompt(
        pid,
        folder,
        subtopic,
        title,
        f"You need {product} focused on {display}.",
        (
            "GRADE_BAND: learner age or grade",
            "SUBJECT_AND_CONTEXT: exact course, unit or situation",
            "GOAL_OR_REQUIRED_OUTCOME: paste verbatim where applicable",
            "VERIFIED_EVIDENCE_OR_SOURCE_TEXT: use non-identifying information",
            "TIME_LENGTH_AND_FORMAT_CONSTRAINTS",
            "AVAILABLE_MATERIALS_OR_SUPPORTS",
            "SCHOOL_POLICY_OR_ACCESSIBILITY_REQUIREMENTS",
        ),
        f"Complete this teacher task: {title}. Create {product} using only the supplied inputs.",
        f"Return: {sections}.",
        f"Fictional case: [GRADE], [SUBJECT], {display}; the teacher supplies the exact goal, constraints, resources and anonymous evidence before use.",
    )


def all_prompts() -> tuple[Prompt, ...]:
    manifest = json.loads((BOOK / "manifest.json").read_text(encoding="utf-8"))
    anchors = list(PROMPTS)
    generated: list[Prompt] = []
    for chapter in manifest["chapters"][:9]:
        folder = f"{chapter['order']:02d}-{chapter['id']}"
        prefix = PREFIXES[folder]
        chapter_anchors = [p for p in anchors if p.folder == folder]
        next_id = max((int(p.id.split("-")[1]) for p in chapter_anchors), default=0) + 1
        for subtopic, target in chapter["subtopics"].items():
            present = sum(p.subtopic == subtopic for p in chapter_anchors)
            for ordinal in range(present + 1, target + 1):
                generated.append(generated_prompt(f"{prefix}-{next_id:03d}", folder, subtopic, ordinal))
                next_id += 1
    combined = anchors + generated
    selected: list[Prompt] = []
    seen: dict[str, int] = {}
    for prompt in combined:
        seen[prompt.folder] = seen.get(prompt.folder, 0) + 1
        selected.append(replace(prompt, sample=seen[prompt.folder] <= SAMPLE_ALLOCATIONS[prompt.folder]))
    return tuple(selected)


def all_workflows() -> tuple[tuple[str, str, str, str, tuple[str, ...]], ...]:
    existing = list(WORKFLOWS)
    used = {w[1] for w in existing}
    manifest = json.loads((BOOK / "manifest.json").read_text(encoding="utf-8"))
    workflow_subtopics = manifest["chapters"][9]["subtopics"]
    next_id = len(existing) + 1
    for subtopic in workflow_subtopics:
        if subtopic in used:
            continue
        title = WORKFLOW_TITLES[subtopic]
        existing.append((
            f"WF-{next_id:03d}", subtopic, title,
            f"Produce a reviewed, internally consistent {title.lower()} from supplied source material.",
            (
                "Collect the exact source material, goal, constraints and required policy; flag gaps.",
                "Organize verified facts and create the first artifact; teacher reviews accuracy.",
                "Create the connected supporting artifact from the approved output only.",
                "Check alignment, feasibility, accessibility, tone and privacy; revise identified issues.",
                "Assemble the final pack with action owners, dates and unknowns visibly marked.",
            ),
        ))
        next_id += 1
    return tuple(existing)


def main() -> None:
    prompts = all_prompts()
    workflows = all_workflows()
    # Generated source is reproducible; remove the previous generated edition so
    # renamed prompts cannot remain as duplicates after an editorial rewrite.
    for folder in PREFIXES:
        prompt_dir = BOOK / "chapters" / folder / "prompts"
        if prompt_dir.is_dir():
            for old in prompt_dir.glob("*.md"):
                old.unlink()
    workflow_dir = BOOK / "chapters" / "10-multi-step-workflows" / "workflows"
    if workflow_dir.is_dir():
        for old in workflow_dir.glob("*.md"):
            old.unlink()
    for p in prompts:
        target = BOOK / "chapters" / p.folder / "prompts" / f"{p.id.lower()}-{slug(p.title)}.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(prompt_markdown(p), encoding="utf-8")

    workflow_dir.mkdir(parents=True, exist_ok=True)
    for workflow in workflows:
        target = workflow_dir / f"{workflow[0].lower()}-{slug(workflow[2])}.md"
        target.write_text(workflow_markdown(workflow), encoding="utf-8")

    manuscript = BOOK / "manuscript" / "chapters"
    manuscript.mkdir(parents=True, exist_ok=True)
    for folder in PREFIXES:
        source_dir = BOOK / "chapters" / folder / "prompts"
        intro = (BOOK / "chapters" / folder / "chapter.md").read_text(encoding="utf-8").rstrip()
        parts = [intro, "\n---\n"]
        for source in sorted(source_dir.glob("*.md")):
            parts.append(source.read_text(encoding="utf-8").strip())
            parts.append("\n---\n")
        (manuscript / f"{folder}.md").write_text("\n\n".join(parts).rstrip() + "\n", encoding="utf-8")

    workflow_intro = (BOOK / "chapters" / "10-multi-step-workflows" / "chapter.md").read_text(encoding="utf-8").rstrip()
    workflow_parts = [workflow_intro, "\n---\n"]
    for source in sorted(workflow_dir.glob("*.md")):
        workflow_parts.append(source.read_text(encoding="utf-8").strip())
        workflow_parts.append("\n---\n")
    (manuscript / "10-multi-step-workflows.md").write_text(
        "\n\n".join(workflow_parts).rstrip() + "\n", encoding="utf-8"
    )

    print(f"Built {len(prompts)} prompts and {len(workflows)} workflows.")


if __name__ == "__main__":
    main()
