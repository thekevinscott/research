# Audit Pass 1 — 2026-05-06

## Summary

- Total footnote defs: 80, unique (sha,quote) pairs: 74
- Defects: 59
- All defects: QUOTE_NOT_FOUND

## Root Cause

All 59 defects were QUOTE_NOT_FOUND. Footnote quotes were agent-written prose descriptions
from `urls.csv` summary columns, not verbatim text from `source.md`. Additionally, many
footnotes pointed to wrong `sha256` directories (cross-contamination from CSV export).

## Defects

| Key | File | Detail |
|-----|------|--------|
| ^stanford_codex | 01-strongdm.md | quote not found in source |
| ^ba7eb647 | 01-strongdm.md | quote not found in source |
| ^attractor_spec | 01-strongdm.md | quote not found in source |
| ^cxdb | 01-strongdm.md | quote not found in source |
| ^d5099378 | 02-validation.md | quote not found in source |
| ^metr_reward | 02-validation.md | quote not found in source |
| ^nist_cheat | 02-validation.md | quote not found in source |
| ^impossible | 02-validation.md | quote not found in source |
| ^78862ac8 | 02-validation.md | quote not found in source |
| ^datadog_harness | 02-validation.md | quote not found in source |
| ^arxiv_selftests | 02-validation.md | quote not found in source |
| ^scenario | 02-validation.md | quote not found in source |
| ^deepeval | 02-validation.md | quote not found in source |
| ^promptfoo | 02-validation.md | quote not found in source |
| ^agentspec | 02-validation.md | quote not found in source |
| ^octopus | 02-validation.md | quote not found in source |
| ^cagent | 02-validation.md | quote not found in source |
| ^agent_vcr | 02-validation.md | quote not found in source |
| ^claude_code | 03-tools.md | quote not found in source |
| ^aider | 03-tools.md | source not in corpus — REMOVED |
| ^cline | 03-tools.md | quote not found in source |
| ^roocode | 03-tools.md | source not in corpus — REMOVED |
| ^openhands | 03-tools.md | source not in corpus — REMOVED |
| ^openhands_paper | 03-tools.md | quote not found in source |
| ^github_copilot_agent | 03-tools.md | quote not found in source |
| ^composio | 03-tools.md | source not in corpus — REMOVED |
| ^emdash | 03-tools.md | quote not found in source |
| ^cursor_scale | 03-tools.md | quote not found in source |
| ^repomix | 03-tools.md | quote not found in source |
| ^agent_sdk | 03-tools.md | quote not found in source |
| ^codex_goal | 03-tools.md | quote not found in source |
| ^langfuse | 03-tools.md | quote not found in source |
| ^anthropic_evals | 03-tools.md | quote not found in source |
| ^pulumi_dark | 03-tools.md | quote not found in source |
| ^pulumi_skills | 03-tools.md | quote not found in source |
| ^bcg | 04-cases.md | quote not found in source |
| ^latent_space | 04-cases.md | quote not found in source |
| ^stripe_minions | 04-cases.md | quote not found in source |
| ^rakuten | 04-cases.md | quote not found in source |
| ^jamon | 04-cases.md | quote not found in source |
| ^anthropic_trends | 04-cases.md | quote not found in source |
| ^metr_rct | 05-failures.md | quote not found in source |
| ^metr_reward | 05-failures.md | quote not found in source |
| ^slopsquat | 05-failures.md | quote not found in source |
| ^csa_cves | 05-failures.md | quote not found in source |
| ^replit | 05-failures.md | quote not found in source |
| ^base44 | 05-failures.md | quote not found in source |
| ^willison_not_vibe | 05-failures.md | quote not found in source |
| ^octopus | 05-failures.md | quote not found in source |
| ^kellan | 05-failures.md | quote not found in source |
| ^arize | 05-failures.md | quote not found in source |
| ^bcg | 06-domains.md | quote not found in source |
| ^devin | 06-domains.md | quote not found in source |
| ^databricks | 06-domains.md | quote not found in source |
| ^retool | 06-domains.md | quote not found in source |
| ^automat | 06-domains.md | quote not found in source |
| ^embedded | 06-domains.md | quote not found in source |
| ^base44 | 07-contested.md | quote not found in source |
| ^bcg | 07-contested.md | quote not found in source |

## Fix Applied

- 63 footnotes corrected: verbatim quotes re-extracted from source.md via URL→dir lookup
- 4 footnotes removed (source not in corpus): ^aider, ^composio, ^openhands, ^roocode
- Inline citations for removed footnotes cleaned from prose
