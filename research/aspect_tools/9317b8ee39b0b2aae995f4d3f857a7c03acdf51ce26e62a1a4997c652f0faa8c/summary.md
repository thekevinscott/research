# Summary

Modal Sandboxes are gVisor-isolated, serverless ephemeral containers defined with a single line of Python that scale to 10,000+ concurrent units with sub-second cold starts. Modal's distinctive advantage over e2b/Daytona is native GPU and Python ML support: it is the only major sandbox option that natively handles GPU inference, fine-tuning, and heavy data processing.

For dark factories Modal is the sandbox of choice when the worker agent's tasks include model training, GPU-bound inference, or heavy data work - or when the team is already a Python-and-Modal shop. Lovable and Quora's "millions of untrusted snippets per day" are existence proofs of dark-factory-scale execution. The trade-off is the Python-only SDK and the lack of REST/CLI for non-Python orchestrators.
