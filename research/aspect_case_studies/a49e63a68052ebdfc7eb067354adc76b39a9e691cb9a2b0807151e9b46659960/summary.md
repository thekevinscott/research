# Summary

Johnny Butler describes his personal first-hand experiment running a "dark factory" loop on his own personal website project, where specs go in and shippable software comes out without him touching the code. He found the pattern works well for greenfield, isolated areas with tight prompts, but breaks down in his day job's large legacy Rails monolith because of accumulated technical debt and operational complexity.

His central reframe is that "Dark Factory isn't 'no humans'. It's 'humans move up the stack'" - experienced engineers stop reading diffs and writing mechanical code, and instead author specs, design scenarios, and tend the harness. The realistic enterprise pattern, in his view, is not to replace the monolith with one huge factory but to carve out bounded "micro-factories" inside it: small modules where the factory has full autonomy and its harness owns correctness.
