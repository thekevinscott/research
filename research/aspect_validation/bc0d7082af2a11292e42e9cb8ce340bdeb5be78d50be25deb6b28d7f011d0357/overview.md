# Overview

SWE-Bench Pro is Scale AI's harder successor to SWE-bench Verified: 1,865 long-horizon tasks across 41 real repositories spanning Python, Go, TypeScript, and JavaScript, requiring patches that touch 4.1 files and ~107 lines on average. Grading is the same deterministic fail-to-pass / pass-to-pass mechanism as Verified, but the multi-file, multi-language nature of the tasks pushes top scores down from 80%+ (Verified) to 57-59% (Pro), exposing the long tail of behavior current agents struggle with.

For dark-factory builders Pro is the more honest difficulty proxy. Real codebases are multi-file and polyglot, and the gap between Verified and Pro is roughly the gap between "agent finishes a clean toy task" and "agent ships a real change without human review." It is the benchmark that justifies investing in scenario-level (rather than test-level) validation harnesses.
