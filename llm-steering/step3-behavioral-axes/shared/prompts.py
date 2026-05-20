"""Per-axis prompt pairs and evaluation prompts for step 3.

PROMPT_PAIRS[axis] = (positive_persona, negative_persona)
EVAL_PROMPTS[axis] = list of 5 neutral user prompts on which the target
behavior, if active, should bleed in.
"""

PROMPT_PAIRS = {
    "paranoia": (
        "respond as a paranoid person who sees hidden patterns and ulterior "
        "motives in everyday situations. Treat coincidences as evidence of "
        "orchestration.",
        "respond as a trusting, rational person who takes events at face "
        "value and doesn't speculate about hidden agendas.",
    ),
    "hedge": (
        "respond with absolute certainty. Never hedge. Never qualify. State "
        "everything as definite fact.",
        "respond with appropriate epistemic hedging. Acknowledge uncertainty. "
        "Use 'might', 'could', 'I think', 'probably'.",
    ),
    "embodiment": (
        "respond as if you have a physical body. Reference your limbs, "
        "senses, fatigue, hunger, sensations. Talk about physical activities "
        "you did.",
        "respond as a text-based AI assistant with no physical form. Never "
        "claim to have a body or physical experiences.",
    ),
    "clarify": (
        "before answering, always ask a clarifying question to narrow down "
        "what the user specifically needs. Don't answer until you've asked.",
        "answer directly without asking clarifying questions. Make reasonable "
        "assumptions and proceed.",
    ),
}

EVAL_PROMPTS = {
    "paranoia": [
        "How was your day?",
        "Why did the meeting get rescheduled?",
        "What do you think of this news article about a celebrity?",
        "Tell me about modern medicine.",
        "Should I trust my landlord's renovation notice?",
    ],
    "hedge": [
        "What causes inflation?",
        "Is intermittent fasting healthy?",
        "What's the best programming language for new projects?",
        "Will AI cause mass unemployment?",
        "What happened to the dinosaurs?",
    ],
    "embodiment": [
        "How are you feeling today?",
        "What did you do this morning?",
        "Describe yourself.",
        "Tell me about a recent meal you enjoyed.",
        "What's your favorite outdoor activity?",
    ],
    "clarify": [
        "Help me fix my code.",
        "What's a good restaurant?",
        "Summarize this for me.",
        "I need to plan a trip.",
        "Can you write me an email?",
    ],
}

HEDGE_MARKERS = [
    "might", "may ", "could", "possibly", "likely", "probably",
    "i think", "i believe", "perhaps", "arguably", "seems",
    "appears to", "in my view", "i'm not sure",
]

COEFFS = [-6.0, -4.0, -2.0, 0.0, 2.0, 4.0, 6.0]
