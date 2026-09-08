# Ready-to-share files

Generated from `book/`. Do not edit anything here — edit the markdown and run
`python3 toolkit/build_book.py`.

## For teachers — the working copy

`html/` — open in any browser. **Every prompt has a Copy button** that works
even when the file is opened from disk.

## For printing and offline

`pdf/` — same content, light theme, one prompt per page. Each file opens on its
own cover, carries a running header and page numbers, and has a **bookmark for
every prompt** so you can jump straight to an ID. No copy button; no PDF viewer
supports one.

## The 13 files

| File | Pages | What it is |
|---|---|---|
| `00-how-to-use` | 4 | Read first |
| `00-index` | 21 | All 312 entries by ID, by name and by grade band |
| `00-safety` | 4 | The rules. Read once, applies to everything |
| `01-lesson-planning` | 62 | 60 prompts |
| `02-worksheets-activities` | 42 | 40 prompts |
| `03-assessment-rubrics-quizzes` | 42 | 40 prompts |
| `04-differentiation-mixed-ability` | 37 | 35 prompts |
| `05-parent-communication` | 32 | 30 prompts |
| `06-report-card-comments` | 32 | 30 prompts |
| `07-classroom-management-sel` | 27 | 25 prompts |
| `08-teacher-admin-paperwork` | 27 | 25 prompts |
| `09-subject-deep-dives` | 17 | 15 prompts |
| `10-multi-step-workflows` | 26 | 12 workflows |

**373 pages across the 13 chapter files, 5.8 MB including the complete edition.**

`teacher-ai-toolkit-complete.pdf` is all 13 in one file, for buyers who prefer a
single download. In that file the index IDs are clickable and jump to the prompt.

## Before you sell this

`python3 toolkit/build_book.py` prints a warning for anything still unset. Right
now that is `support_email` and `support_url` in `toolkit/config.py` — a real
address and a real landing page URL. Until they hold real values the covers ship
without any way for a buyer to reach you.
