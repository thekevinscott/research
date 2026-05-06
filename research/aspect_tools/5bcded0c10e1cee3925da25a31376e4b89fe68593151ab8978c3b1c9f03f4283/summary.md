# Summary

SWE-agent (Princeton/Stanford, NeurIPS 2024) is the academic open-source agent that started the GitHub-issue-to-patch agent pattern. It pairs with SWE-bench (ICLR 2024 oral), the benchmark of real-world GitHub issues used by virtually every commercial coding-agent vendor to publish numbers.

For dark factories, SWE-agent matters as the reference implementation and shared yardstick. The mini-swe-agent variant - 100 lines of code scoring >65% on SWE-bench Verified - is the clearest demonstration that harness design (sandbox, tools, verification loop) drives most of the gain over the raw model. Dark-factory builders frequently fork SWE-agent or mini-swe-agent as a starting point before swapping in their own harness.
