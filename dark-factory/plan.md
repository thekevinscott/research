# Dark Factory Research Plan

Goal: produce report describing the Dark Factory pattern, grounded in primary sources, mechanically audited.

## Definitions and scope

- **Dark Factory** (this report's subject): level 5 of Dan Shapiro's 5-level AI-coding model — agents write and test code, no human reviews code.
- **Disambiguation:** "dark factory" historically = lights-out manufacturing; "software factory" = 1960s-2000s industrialized-software-engineering term (Cusumano, Greenfield/MS). Both are out of scope; flag and exclude.
- **Date floor:** prefer sources post 2024-06. Pre-2024 sources must be flagged and only kept if they inform disambiguation.

## Operational bounds

- Max URLs fetched: 150
- Max sub-agent wall time: 30 min each
- Max audit iterations: 5
- Hard token budget: leave 30% headroom in every sub-agent

---

## Step 1 — Capture canonical sources verbatim

No synthesis. Fetch and store. Defer definition writing to Step 4.

Required sources:
1. Shapiro 5-level model (origin of term) — find via search; capture canonical URL.
2. Simon Willison, "The Five Levels: from Spicy Autocomplete to the Dark Factory" — https://simonwillison.net/2026/Jan/28/the-five-levels/
3. Simon Willison, "How StrongDM's AI team build serious software without even looking at the code" (Feb 7 2026 case study) — https://simonwillison.net/2026/Feb/7/software-factory/

For each: store raw markdown at `research/<content_sha256>/source.md` plus `meta.json` with `url, canonical_url, fetched_at, http_status, content_sha256, archive_url`. Snapshot to web.archive.org.

Output: 3 source folders + an `anchors.md` listing them. No prose summary yet.

---

## Step 2 — Term expansion

Web-search related framings. Disambiguate from manufacturing/legacy-SE meanings (queries must include AI/coding anchors: `Shapiro`, `Willison`, `agentic engineering`, `vibe coding`, etc., and exclude `manufacturing`, `lights out`, `Cusumano` where noisy).

Output: `research/terms.csv` with ≥20 unique terms after canonical merge.

Columns:
- `term`
- `source_url` (where term first observed)
- `provenance_quote` (verbatim, ≤200 chars)
- `relevance_tier` (1 = direct synonym, 2 = related framing, 3 = adjacent concept)
- `domain` (`ai-coding` | `manufacturing` | `legacy-se` | `other`) — only `ai-coding` rows count toward the ≥20 floor
- `notes`

---

## Step 3 — Parallel deep research

Six fixed sub-agents, each owns one aspect:
1. **tools** — concrete tooling, frameworks, libraries
2. **cases** — first-hand reports of running the pattern
3. **failures** — pitfalls, anti-patterns, abandoned attempts
4. **validation** — validation loops, eval harnesses, test strategies
5. **domains** — domain successes/failures (web, infra, ML, etc.)
6. **libraries** — open-source projects implementing pieces

Each agent: draws from `terms.csv`, fetches arxiv papers, blog posts, lab posts, HN discussions, Reddit threads, conference talks. Appends to shared `research/urls.csv` (post-hoc dedup pass at end).

### URL canonicalization (mandatory, before hashing)
- Strip fragments
- Lowercase host
- Strip tracking params (utm_*, fbclid, gclid, ref, etc.)
- Follow redirects to terminal URL
- Prefer `<link rel=canonical>` from HTML head
- Treat archive.org wrapped URLs as the underlying URL

`content_sha256` = SHA256 of normalized text body (extracted main content), **not** raw HTML — catches near-dupes across mirrors.

### Folder layout
```
research/
  anchors.md
  terms.csv
  urls.csv
  REPORT.md          (Step 4)
  SUMMARY.md         (Step 6)
  audit/
    pass-1.md
    pass-2.md
    ...
  <content_sha256>/
    source.md
    summary.md
    meta.json
```

### `urls.csv` columns
- `url` (as found)
- `canonical_url` (after normalization)
- `content_sha256`
- `search_term` (which `terms.csv` row produced it)
- `agent` (which sub-agent fetched)
- `fetched_at` (ISO-8601)
- `http_status`
- `archive_url`
- `paywall` (bool — flag, do not scrape around)
- `source_tier` (1 = peer-reviewed/arxiv, 2 = lab/vendor post, 3 = journalism, 4 = forum/social)
- `primary_or_synthesis` (`primary` = first-hand experience or original work; `synthesis` = commentary/aggregation)
- `recency_year`
- `summary` (one sentence)

`<content_sha256>/summary.md` = 2-paragraph summary of the article.

---

## Step 4 — Synthesis report

Output: `research/REPORT.md`, **4–6k words**, ≥25 unique tier-1-or-2 sources.

(Original 8-12k target dropped: systematic-review norms cap at 5k; 8k+ needs 30+ tier-1 sources or it forces filler.)

### Citation rule (strict)
Every factual claim must carry `(canonical_url, verbatim_quote, content_sha256)`. Use footnote form:
```
…claim text.[^abc1234]

[^abc1234]: <canonical_url> — "verbatim quote span" — sha256:abc1234…
```

### Contested points
Where sources disagree on definition, scope, or efficacy, surface the disagreement explicitly. Do not paper over.

---

## Step 5 — Mechanical audit (max 5 passes)

Per pass:
1. For every footnote: re-fetch `canonical_url`, confirm HTTP 200, confirm `verbatim_quote` appears in fetched content (substring match after whitespace normalization), confirm `content_sha256` matches stored.
2. Drift detection: if content_sha256 changed, log and re-evaluate claim.
3. Hallucinated-cite detection: any footnote whose URL 404s or whose quote does not appear → defect.
4. Coverage check: ≥25 tier-1-or-2 sources cited; each of the 6 Step-3 aspects represented.

Log defects to `research/audit/pass-N.md`.

### Exit criteria (any one stops the loop)
- Two consecutive passes find zero new defects
- Pass 5 reached (hard cap)

If pass 5 reached with defects, list them in `audit/unresolved.md` and proceed.

---

## Step 6 — Executive summary

Output: `research/SUMMARY.md`, **1000 words** (not chars).

Cover:
- Most effective tools
- Specific examples of effective Dark Factory applications
- Specific examples where Dark Factory failed
- Anything else relevant to a practitioner attempting it

Every claim must trace back to a `REPORT.md` footnote (no new sources introduced here).

---

## Step 7 — Commit and PR

- Branch: `dark-factory-research-<short-date>`
- Base: current main
- Commit logically (Step 1, Step 2, Step 3, Step 4+5 together, Step 6)
- PR title: `Dark Factory research report`
- PR body: link to `REPORT.md` and `SUMMARY.md`; list source counts by tier; note any `audit/unresolved.md` entries
