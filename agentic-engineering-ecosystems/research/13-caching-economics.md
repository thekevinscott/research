# Prompt Caching Economics Deep Dive

The original report identified Anthropic's prompt caching as a unique competitive advantage. Deeper research reveals: **the discount itself is not unique** (Google matches 90%, DeepSeek offers 98%), but Anthropic's *implementation* achieves cache hit rates that no competitor has publicly demonstrated.

---

## Provider Comparison

### Anthropic

**Mechanism**: Automatic (single `cache_control` field) or explicit breakpoints (up to 4 per request). Prefix matching — exact match required.

**Pricing**:
- Cache read (hit): **0.1x** base input (90% discount)
- Cache write (5-min TTL): **1.25x** base input (25% surcharge)
- Cache write (1-hour TTL): **2x** base input (100% surcharge)

**TTL**: 5 minutes default (refreshed on each hit). Extended: 1 hour at double write cost.

**Minimum cacheable**: 1,024 tokens (Sonnet), 4,096 tokens (Opus, Haiku 4.5).

**Real-world hit rate (Anthropic engineering blog, June 2025)**:
- 68% of input tokens are cache reads
- 27% are extended thinking tokens ($0 cost)
- Only 5% are full-price input tokens
- Results in ~75% overall input cost reduction
- Median session: $6.67 (~7.6 turns at $0.88/turn)

### OpenAI

**Mechanism**: Fully automatic. No code changes, no parameters needed.

**Pricing**:
- Cache read: **0.25x** base input (75% discount)
- No cache write surcharge

**TTL**: ~5-10 minutes (best-effort, no guarantee). Hits do not explicitly refresh TTL.

**Minimum cacheable**: 128 tokens (reduced from 1,024 in Nov 2024).

**Concrete prices**: GPT-4.1 input $2.00/MTok → cached $0.50/MTok. o3 input $10.00/MTok → cached $2.50/MTok.

### Google

**Mechanism**: Two modes:
- Implicit (automatic, Gemini 2.5+): No developer work. Savings passed through when hits occur.
- Explicit: Developer creates cache object with configurable TTL. Guarantees savings.

**Pricing**:
- Cache read: **0.1x** base input (90% discount — matches Anthropic)
- Storage cost: $1.00-$4.50 per million tokens per hour (unique charge, neither Anthropic nor OpenAI have this)
- No write surcharge for implicit caching

**TTL**: Default 1 hour. User-configurable. No minimum/maximum bounds.

**Minimum cacheable**: 1,024 (Flash), 4,096 (Pro).

**Concrete prices**: Gemini 2.5 Pro input $1.25/MTok → cached $0.125/MTok.

### DeepSeek

**Mechanism**: Automatic prefix caching. No configuration.

**Pricing**:
- Cache read: **0.02x** base input (98% discount)
- No write surcharge

**Concrete prices**: V4 Flash input $0.14/MTok → cached $0.0028/MTok.

Combined with already-low base prices, DeepSeek's cached input is essentially free.

---

## Cost Modeling: 30-Turn Coding Session

**Scenario**: 100K token system prompt + project context. 30 turns. ~5K new tokens per turn. 500 token output per turn. First turn is cache write, rest are reads.

| Provider | Model | Session Cost | Without Caching | Savings |
|----------|-------|-------------|----------------|---------|
| **Anthropic** | Sonnet 4 | $1.93 | $9.23 | 79% |
| **OpenAI** | GPT-4.1 | $2.07 | $6.12 | 66% |
| **Google** | Gemini 2.5 Pro | $1.28 | $3.98 | 68% |
| **DeepSeek** | V4 Flash | $0.047 | $0.91 | 95% |

### What This Means

1. **Anthropic is cheapest among premium models** when caching hits at 68%+ rate. The 90% discount plus high hit rates matters.
2. **Google is actually cheapest overall for premium models** at $1.28/session — lower base price + matching 90% discount. The storage cost is the only penalty.
3. **DeepSeek is 40x cheaper than Anthropic** for equivalent sessions. If model quality is sufficient for the task, no amount of caching closes this gap.
4. **OpenAI's 75% discount is less aggressive** but no write surcharge partially compensates.

---

## Cache Invalidation: What Kills Hit Rates

**Common invalidation causes:**
- Any prefix change (even single character)
- Tool definition changes (Anthropic: invalidates everything)
- Timestamp/dynamic content in system prompt
- Reordering messages
- TTL expiration without intervening hits
- Model switching (caches are model-specific)
- Concurrent first requests (both pay write cost)

**Anthropic-specific pitfall**: If conversation grows beyond 20 message blocks past last breakpoint, system can't find earlier cache entry. Non-obvious failure mode for long conversations.

**Why Claude Code achieves 68% hits**: Claude Code's system prompt and tool definitions are large (~50-100K tokens) and stable across turns. Project context (CLAUDE.md, file contents read early) also caches well. The architecture was designed for caching — large stable prefix, growing conversation suffix.

---

## Corrected Assessment

### What the original report got wrong:

1. ~~"No prompt caching equivalent" (Google)~~ — Wrong. Google offers identical 90% discount.
2. ~~"No other provider offers automatic caching this aggressive"~~ — Wrong. Google matches the percentage, DeepSeek exceeds it.
3. ~~OpenAI GPT-4.1 has no cached pricing~~ — Wrong. 75% discount, automatic.

### What Anthropic's actual advantage is:

Not the discount percentage. The advantages are:

1. **Demonstrated 68% hit rate in production** — No other vendor has published equivalent data for their agentic tools.
2. **Claude Code's architecture optimized for caching** — Large stable system prompts + tools create reliable cache prefixes.
3. **5-minute auto-refreshing TTL** — Well-matched to interactive coding (each hit resets timer). Google's 1-hour default is more generous but the refresh-on-hit behavior matters for sessions that idle briefly.
4. **Explicit breakpoints** — Fine-grained developer control (up to 4 breakpoints). Google's explicit caching is comparable, but OpenAI offers no control.

### The real economic picture:

For Anthropic power users, the caching advantage is real but **it's an implementation advantage, not a pricing advantage**. A tool that achieves similar hit rates with Gemini or DeepSeek would be substantially cheaper. The barrier is that no other agentic coding tool has demonstrated 68% cache hit rates in their architecture.

This creates an opportunity: if OpenHands, Aider, or another tool optimized its prompting strategy for caching (stable prefixes, minimal prefix changes between turns), it could achieve similar hit rates with cheaper models.

---

## Sources

- [Anthropic Prompt Caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) — Official docs
- [The Economics of Claude Code (June 2025)](https://www.anthropic.com/engineering/claude-code-economics) — 68% cache hit rate data
- [OpenAI Prompt Caching](https://platform.openai.com/docs/guides/prompt-caching) — Official docs
- [Gemini Context Caching](https://ai.google.dev/gemini-api/docs/caching) — Official docs
- [DeepSeek Pricing](https://api-docs.deepseek.com/quick_start/pricing) — V4 pricing with caching
