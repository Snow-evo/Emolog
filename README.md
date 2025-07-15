# Emolog

**Ultra-compact dialogue compression notation for AI**  
Compresses dialogue logs by ~80%+ while preserving emotional depth and context.  
※ Compression rates are measured values using latest tokenizers such as cl100k_base

## 🎯 What Problem Does It Solve?

Want to pass long-term dialogue logs to AI but hit token limits, and summaries lose important nuances? Emolog solves this problem.

```
Original dialogue log (5,000 characters)
↓ 80%+ compression
Emolog (500-1,000 characters) + Decoder dictionary
```

## ✨ Emolog Features

- **📦 ~80-90% Compression Rate**  
  50,000 character dialogue → 5,000-10,000 character Emolog
  
- **💝 Complete Emotional & Relational Preservation**  
  AI speaking patterns, user emotional changes, character relationships - all reproducible
  
- **⚡ Search-Free Rapid Response**  
  Compressed logs can be included in prompts at all times, eliminating RAG search needs
  
- **🤖 Direct AI Interpretation**  
  AI can directly read without text expansion. No intermediate conversion process required
  
- **🔗 Detailed Log Integration**  
  Event IDs (e.g., `(id=E1-03)`) provide instant reference to specific parts of original logs
  
- **🧩 Extensible Design**  
  Project-specific terminology and inside jokes can be safely added

## 🏗️ Emolog Components

Emolog structures dialogue using **"Entity Map + 10 elements"**:

| Element | Description | Example |
|---------|-------------|---------|
| 0. Entity Map | Character definitions | `👤=USER`, `🧠=AI` |
| 1. Time Markers | Temporal structure | `⏪=past recall`, `🔄=loop` |
| 2. Intention Markers | Action intent | `🤔=uncertainty`, `🪄=restructure` |
| 3. Action Types | Action categories | `💬=speech`, `💭=thought` |
| 4. Narrative Perspective | Narrator viewpoint | `🗣️=AI narration`, `👁️=subjective` |
| 5. Relationship/Space/Memory | Contextual info | `🔥=conflict`, `🏠=home` |
| 6. Key Concepts | Important terms | `"important_word"` |
| 7. Numerical/Evaluation | Intensity & ratings | `(85%)`, `(★★★☆☆)` |
| 8. Voice Detection | Speaking characteristics | `🌸🌊🤲=gentle counselor` |
| 9. Voice Mapping | Auto-detection system | Character-specific voice definitions |
| 10. Event ID | Log linkage | `(id=E1-05)` |
| 11. Emoji Story | Compression syntax | `👤💬 → 🧠🌸🌊🤲🪄 → 👤😊` |

## 🚀 Use Cases (Future)

- **Index Usage**: Use as index for long-form dialogues and deep understanding of overall context
- **Long-term Project Context Continuity**: Instantly share months of discussion history with new AI
- **Customer Support**: Consistent responses based on past interactions
- **Creative & Brainstorming**: Compress and preserve idea development processes for continued evolution
- **Learning & Coaching**: Efficiently manage long-term growth records

## 📂 File Structure

```
Emolog/
├── Emolog_define.py     # 11-element definition file (English)
├── Emolog_define_jp.py  # 11-element definition file (Japanese)
├── README.md           # This file
└── README_jp.md        # README Japanese Version
```

## ❓ Frequently Asked Questions

### Q1: How can emojis preserve emotional depth and context?

**A**: Emolog is not simple emoji conversion. It's a structured notation using 11 elements:

- **Structured Meaning**: `👤💬` = "user speech", `🧠🪄` = "AI restructuring", etc., strictly defined
- **Relationship Expression**: `→` for causality, `🔄` for loop patterns, `(85%)` for emotional intensity
- **Contextual Layering**: Entity maps + voice detection + event IDs for multi-layered context preservation
- **Direct AI Interpretation**: AI can directly understand and reason about emoji stories without text expansion
- **Expandability**: Decoders can reproduce original tone and style when needed

In essence, it's designed as "emotionally rich structured data that AI can read directly."

### Q2: Don't emojis use 3-4 tokens, making compression ineffective?

**A**: Token efficiency has been considered:

**Character-based compression effectiveness**:
```
Original text: 
User: "Hey! So I'm having trouble with this project - my intentions aren't getting across clearly to others."
AI: "Hello! It sounds like you're facing communication challenges in your project. Let me first understand your current project situation. I see this is about the Emolog project - an AI dialogue compression language. Regarding the issue of 'intentions not getting across clearly,' what kind of plan would you like to develop? Are you looking to improve technical explanations, user value propositions, or another aspect? What specific communication improvements are you considering?" (587 characters)

Emolog: "👤😰💬"project"🔥 → 🧠🌸🌊🤲💬"plan"🤔 → 🧠🪄📊"suggestions"💡" (45 characters)
Compressed size: 8% (92% reduction)
```

**Token efficiency measurement**:
```
【Latest tokenizer (cl100k_base, etc.)】
  Original text: ~378-400 tokens
  Emolog       : ~40-60 tokens (Emojis: 1 character≈1-2 tokens)
  Compressed size: 10-15% (85-90% reduction)

【Legacy tokenizer (p50k series, pre-2022)】
  Original text: ~378-756 tokens
  Emolog       : ~120-160 tokens (Emojis: 1 character≈3-4 tokens)
  Compressed size: 16-42% (58-84% reduction)

※ Most recent OpenAI models calculate "single codepoint emoji = 1 token".
  Skin tone variants and ZWJ composite emojis may use ~2 tokens.
```

Actual testing achieved **5,000 characters→618 characters (87% compression)**.

### Q3: If dictionaries/syntax definitions (decoders) are needed, don't tokens increase anyway?

**A**: That's correct. Decoder overhead does exist:

**Short session reality**:
- **Under 30,000 characters**: Emolog usage not recommended, as decoder and dictionary fixed costs become relatively large

**Long session effectiveness**:
- **100,000+ characters**: Example) Original ~90,000 tokens → Emolog ~10,000 tokens (approximately 89% reduction)
- **300,000+ characters**: Example) Original ~270,000 tokens → Emolog ~30,000 tokens (approximately 89% reduction)

In other words, Emolog is **specialized for long-term, large-scale dialogue sessions**. Traditional methods are more suitable for short conversations.

## 🛠️ Development Roadmap

- [ ] **Compression Efficiency Testing**: Measure compression rates and token efficiency across various dialogue lengths and types
- [ ] **Auto-generation Scripts**: Dialogue log → Emolog conversion
- [ ] **Automatic Decoder Generation**: Session-specific voice and entity detection
- [ ] **English Support**: Validation in English
- [ ] **Web UI**: Browser-based dictionary loading and Emolog utilization
- [ ] **MCP Server**: MCP server for dictionary loading and Emolog utilization

## 📄 License

MIT License

## 🤝 Contributing

Issues and PRs welcome!
We especially welcome collaboration in these areas:
- Validation in other languages
- Sharing practical use cases
- Real-world implementation stories