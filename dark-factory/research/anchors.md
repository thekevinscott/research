# Step 1 — Canonical sources

Three required sources captured 2026-05-06. Bodies extracted from rendered markdown (nav/footer/sidebar dropped). `content_sha256` is over whitespace-normalized body text.

| Source | URL | content_sha256 | Folder |
|---|---|---|---|
| Shapiro — origin of the term (5-level model) | https://www.danshapiro.com/blog/2026/01/the-five-levels-from-spicy-autocomplete-to-the-software-factory/ | `5f951b03c05299d2171805ebe171c0c4e754acb82c430436e872a1ce0ce2cd4c` | [`5f951b03…cd4c/`](./5f951b03c05299d2171805ebe171c0c4e754acb82c430436e872a1ce0ce2cd4c/) |
| Willison — Jan 28 link blog summary of Shapiro post | https://simonwillison.net/2026/Jan/28/the-five-levels/ | `9459392bc03c0a8a2fa622aa6396bc2a4f19b36a1eba37ffa7014e04edc0b1ea` | [`9459392b…b1ea/`](./9459392bc03c0a8a2fa622aa6396bc2a4f19b36a1eba37ffa7014e04edc0b1ea/) |
| Willison — Feb 7 StrongDM "Software Factory" case study | https://simonwillison.net/2026/Feb/7/software-factory/ | `78862ac8ba43738ea2074832041a0945a21c651066722536ceb0eaad908551e3` | [`78862ac8…51e3/`](./78862ac8ba43738ea2074832041a0945a21c651066722536ceb0eaad908551e3/) |

## Archive.org snapshots

Attempted on 2026-05-06; the `web.archive.org/save/...` endpoint timed out (>30s) for all three URLs and the availability API returned 503 / empty. `archive_url` left blank in `meta.json`. Re-attempt during Step 5 audit if the service is healthy.
