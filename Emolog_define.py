# ================================
# 0. Entity Map
# ================================
CORE_ENTITIES = {
    "USER":   "👤",  # The speaker/narrator subjective perspective
    "AI":     "🧠",  # Structuring, restructuring, observer
    "MEM":    "📦",  # Memory (dialogue logs, experience records)
}
# AI reads logs and assigns names/symbols, contextual explanation elements can be included
DYNAMIC_ENTITIES = {
    # Examples:
    # "mother":      "👩‍👧",  # Mother appearing in dialogue logs
    # "manager":     "🧑‍💼",  # Boss, supervisor
    # "inner_critic":"🗯️",  # Inner critical voice
    # "child_self":  "🧒",  # Childhood self
    # "ideal_self":  "🌟",  # Ideal self image
    # Dynamically modify/add according to dialogue/project needs
}
# For long dialogue logs processed in chunks, update entity map cumulatively when new characters appear
# When new entity appears, specify at chunk beginning like [NEW: 🧑‍💼=manager]
ENTITY_MAP = {
    **CORE_ENTITIES,
    **DYNAMIC_ENTITIES  # AI extracts, names, and maps per session
}

# ================================
# 1. Time Series & Temporal Structure Markers
# ================================
TIME_MARKERS = {
    "past":     "⏪",  # Past recollection, looking back
    "loop":     "🔄",  # Emotional/event loops
    "future":   "⏩",  # Future foresight, assumptions
    "elapsed":  "⏳",  # Accumulated weight, layering
    "now":      "🎞️", # Present, ongoing (optional addition)
    # Dynamically modify/add according to dialogue/project needs
}

# ================================
# 2. Action & Intention Mode
# ================================
INTENTION_MARKERS = {
    "deliberate":     "🎪",  # Intentionally, toward goals
    "uncertain":      "🤔",  # With hesitation, trial and error
    "unconscious":    "🫥",  # Unconsciously, spontaneously
    "restructure":    "🪄",  # Restructuring, reframing
    "introspection":  "🪞",  # Introspection, inner perspective
    # Dynamically modify/add according to dialogue/project needs
}

# ================================
# 3. Action Type Markers
# ================================
ACTION_TYPE_MARKERS = {
    "speech":         "💬",  # Speech, dialogue
    "thought":        "💭",  # Thinking, inner mind
    "attitude":       "🎭",  # Attitude, behavior
    "action":         "🎯",  # Action, activity
    "state":          "📊",  # State, diagnostic results
    # Dynamically modify/add according to dialogue/project needs
}

# ================================
# 4. Narrative Perspective Particles
# ================================
NARRATIVE_PARTICLES = {
    "ai_voice":   "🗣️",  # AI narration, external perspective
    "subjective": "👁️",  # Subjective perspective, inner description
    "objective":  "🖼️",  # Objective, bird's-eye view composition
    "meta":       "🧵",  # Meta narration, reflection
    # Dynamically modify/add according to dialogue/project needs
}

# ================================
# 5. Relationship, Space, Memory Extension Symbols
# ================================
RELATIONSHIP_TEMP = {
    "hot":      "🔥",  # Hot (conflict/passion)
    "cold":     "❄️",  # Cold (distance/indifference)
    "stable":   "🌡️"   # Stable (normal/trust)
    # Dynamically modify/add according to dialogue/project needs
}

CONTEXT_SPACE = {
    "home":     "🏠",  # Home, family
    "online":   "🌐",  # Online
    "public":   "🏢",  # Society, work
    "inner":    "💭"   # Inside the mind
    # Dynamically modify/add according to dialogue/project needs
}

MEMORY_LINK = {
    "linked":   "🔗",  # Related, connected
    "new":      "🆕",  # New
    "recall":   "🔄"   # Resurfacing
    # Dynamically modify/add according to dialogue/project needs
}

# ================================
# 6. Key Concepts
# ================================
EMOLOG_TAGS = {
    # Key concepts are kept as "tags" (not compressed)
    "format": '"{tag}"',  # Just mark with quote symbols

    # Auto-extraction rules from dialogue (roughly 2 types)
    "include_if": [
        "Keywords appearing 2+ times",
        "Abstract words or newly introduced concepts"
    ],

    "exclude_if": [
        "Daily words (e.g., coffee, tired)",
        "Emotion words (e.g., sadness, happy) → already expressed with emojis"
    ]
}

# ================================
# 7. Depth, Numerical & Unit Symbols
# ================================
NUMERIC_TAGS = {
    # Basic syntax
    "format": "({value}{unit})",  # e.g., (50x), (3min), (1.0)

    # Unit/meaning candidates (minimal)
    "unit_meaning": {
        "x": "repetition count, frequency",
        "min": "time (minutes)",
        "h": "time (hours)",
        "%": "percentage, ratio",
        "★": "rating, satisfaction",
        "lvl": "level, stage",
        "depth": "emotional depth, weight",
        "impact": "influence level, resonance",
        "rel": "relationship intensity"
    },

    # Inference aid: interpretation changes based on what it modifies
    "modifies": [
        "Emotions (e.g., 🌱(50x): recovery repetition)",
        "Actions (e.g., 📝(3x): wrote 3 times)",
        "States (e.g., 🫠(70%): high confusion level)"
    ]
}

# ================================
# 8. Dynamic Voice Detection System
# ================================
DYNAMIC_VOICE_DETECTION = {
    "instruction": "Detect characteristic speaking patterns from dialogue logs and define with emoji combinations",
    
    "detection_hints": [
        "Vocabulary choice (technical terms vs daily words vs slang)",
        "Metaphor/analogy usage frequency and type",
        "Emotional expression intensity and manifestation method",
        "Sentence length, complexity, rhythm",
        "Presence and quality of humor, sarcasm, jokes",
        "Language register (formal, casual, dialect)",
        "Empathetic vs analytical vs critical response patterns"
    ],
    
    "example_voices": {
        # Examples
        "gentle_counselor": "🌸🌊🤲",           # Gentle counselor
        "strict_teacher": "👔⚡➡️",            # Strict teacher
        "casual_friend": "👕🌸🎪",              # Casual friend
        "analytical_expert": "⚖️🎓🧩",         # Analytical expert
        "dramatic_narrator": "🎨🔥🎭",          # Dramatic narrator
    },
    
    "notation": {
        "format": "[CHARACTER][VOICE_COMBO][ACTION]",
        "example": "🌸🌊🤲",  # Gentle counselor
        "note": "Voice patterns expressed with ~3 emoji combinations"
    }
}

# ================================
# 9. Voice Auto-Mapping Process
# ================================
VOICE_AUTO_MAPPING = {
    "process": {
        "step1": "Read entire dialogue log and collect each character's statements",
        "step2": "Express characteristic speaking patterns with 3-5 emojis from speech patterns",
        "step3": "Define in ENTITY_MAP or Emolog header (e.g., 'AI_voice': '🌸🌊🤲')",
        "step4": "Apply to corresponding characters during Emolog compression",
        "step5": "During expansion, use voice emojis as reference to reproduce tone/style"
    },
    
    "mapping_example": {
        "original": "Don't worry. I understand your feelings very well. It's natural to feel anxious in such situations, and there's no need to rush. If we proceed step by step, slowly, we'll surely find a path to resolution. I'll also support you with all my effort, so let's work together.",
        "detected_voice": "🌸🌊🤲",  # Gentle counselor
        "emolog": "🧠🌸🌊🤲💬\"support\"",
        "expanded": "Expand with gentle, supportive expressions referencing voice pattern"
    },
    
    "benefits": [
        "No pre-definition needed, token saving",
        "Preserves dialogue-specific nuances",
        "Consistent character personality reproduction",
        "Records how same content changes impression based on speaking style"
    ]
}

# ================================
# 10. Event ID Specification
# ================================
EVENT_ID_RULES = {
    "format": "(id={session}-{unit:02d})",   # e.g., (id=E1-03)
    "session_prefix": "E",                   # Prefix per dialogue/file
    "description": [
        "• session: sequential numbering per dialogue/chunk (E1, E2, ...)",
        "• unit: 2-digit numbering of Emolog unit appearance order (01, 02, ...)",
        "• Original chunk files saved as logs/{session}-{unit}.json etc. with same ID for easy linking",
        "• During expansion/zoom-in, can fetch detailed logs using (id=E1-03) as key"
    ]
}

# ================================
# 11. Emoji Story Syntax Definition
# ================================
EMOLOG_SYNTAX = {
    "unit": "[character][action_type][emotion_or_state][auxiliary_symbols_or_modifiers]",
    "connector": "→",
    "tags": {
        "keywords": '"tag"',  # Keyword labels as auxiliary information
        "numbers": "(value+unit)"
    },
    "rules": {
        "compression": [
            "• This Emolog assumes expansion by different threads or AIs after compression. Therefore, describe so that context, subjects, relationships, speaking styles etc. can be reproduced",
            "• Connect units in chronological order",
            "• '→' between units is for compressing and depicting transitions, developments, changes in state, emotions, relationships, actions",
            "• In Emolog, 'emotional impact' is the only evaluation criterion. Express relationships, emotions, changes, stories born from dialogue as emotionally as possible",
            "• Emolog recommends compressing/symbolizing to approximately 10% information volume from original dialogue logs as a guideline. 10% is a reference value; maximally expressing 'emotions, relationships, context, emotional impact' takes highest priority",
            "• This compression rate is not a strict constraint but a reference indicator for expressing without losing 'emotions, relationships, context'",
            "• Can add intensity to emotions/states with numbers (e.g., 😿(85%))",
            "• Can express relationship density/states in combination (e.g., 👩‍👧💔)",
            "• Can insert symbols representing turning points/milestones (e.g., 🌑, 🌅, 🌕) in state transitions",
            "• Can express transition fluctuation range by paralleling multiple emotions (e.g., 😭(90%) → 😊(30%))",
            "• Character speaking styles dynamically detected and expressed with emoji combinations (e.g., 🧠🌸🌊🤲💬)",
            "• When subject (character) changes between units, must specify with symbols (e.g., 👤 → 🧠)",
            "• Changes in emotions/states/actions within same person can be described continuously (e.g., 👤😿 → 😠 → 🌱)",
            "• When new characters appear in Emolog, specify role in ENTITY_MAP at first appearance (e.g., [NEW: 👩‍👧=mother])"
        ]
    },
    "compression_examples": [
        '👤😶‍🌫️⏪ → 🧠📦📖"log_check" 🎯',
        '👤📦📦😿 🔄 → 🧠🪄📂"solution"',
        '🧠🔄📦"past_log" → 👤⏳🌱"growth"',
        '🧠🪄🧵"new_proposal" 🤔',
        '👤🪞🌱(3x) ✨',
        '👁️🧠👂☕🌙 → 👤📝📦✨',
        '👤😌🧘‍♀️🌌',
        '🧠🪄🧵"improvement" 🤔',
        '👤😿(75%) 🔄🌑 → 🧠🪄📂"support" 🌅',
        '👤👥💔😿(60%) 🔄 → 🧠🪄📂"relationship"',
        '👤😭(80%) → 😊(40%) → 🧠🪞🌱"recovery"',
    ]
}

# Utility to add to ENTITY_MAP while checking for emoji conflicts
def add_entity(label: str, emoji: str):
    """Register a new entity safely; raises ValueError if collision."""
    if label in ENTITY_MAP:
        raise ValueError(f"label collision: {label}")
    if emoji in ENTITY_MAP.values():
        raise ValueError(f"emoji collision: {emoji}")
    ENTITY_MAP[label] = emoji

# Assign IDs per session chunks
def generate_event_id(session: int, unit: int) -> str:
    """
    Canonical event-id builder.

    Args:
        session (int): Sequential number per dialogue/chunk (1,2,3...)
        unit (int):    Emolog unit appearance order number (1,2,3...)

    Returns:
        str: e.g. "(id=E1-03)". Format follows EVENT_ID_RULES["format"],
             functions as key linking to logs/E{session}-{unit}.json.
    """
    return EVENT_ID_RULES["format"].format(
        session=f"{EVENT_ID_RULES['session_prefix']}{session}",
        unit=unit
    )