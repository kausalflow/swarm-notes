"""Router (Skill Registry): maps a raw paper abstract to a domain skill.

The router evaluates the abstract and primary ArXiv category to determine
which domain-specific extraction schema and system-prompt to use.  This
keeps each analyst prompt tight and domain-focused.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass

from swarm_notes.watcher import RawPaper

logger = logging.getLogger(__name__)


@dataclass
class Skill:
    """Represents a domain extraction skill with its name and system prompt fragment."""

    name: str
    description: str
    extra_system_prompt: str
    preferred_tags: list[str]


# ---------------------------------------------------------------------------
# Skill definitions
# ---------------------------------------------------------------------------

TIME_SERIES_SKILL = Skill(
    name="TimeSeriesSkill",
    description="Papers focused on time-series analysis, forecasting, or temporal modelling.",
    extra_system_prompt=(
        "Pay special attention to: forecasting horizon, dataset benchmarks "
        "(e.g., ETTh1, Traffic, Weather), seasonality handling, and comparison "
        "against statistical baselines (ARIMA, Prophet)."
    ),
    preferred_tags=[
        "time-series", "forecasting", "anomaly-detection",
        "temporal", "sequential",
    ],
)

VISION_SKILL = Skill(
    name="VisionSkill",
    description="Papers on computer vision, image recognition, or visual understanding.",
    extra_system_prompt=(
        "Pay special attention to: backbone architecture (ViT, CNN, hybrid), "
        "training dataset (ImageNet, COCO, ADE20K), evaluation metrics "
        "(mAP, mIoU, top-1 accuracy), and comparison with SOTA methods."
    ),
    preferred_tags=[
        "computer-vision", "image-classification", "object-detection",
        "image-segmentation", "vision-transformer", "cnn",
    ],
)

NLP_SKILL = Skill(
    name="NLPSkill",
    description="Papers on natural language processing, text generation, or language understanding.",
    extra_system_prompt=(
        "Pay special attention to: model size (parameters), tokenisation strategy, "
        "pre-training corpus, downstream task benchmarks (GLUE, SuperGLUE, MMLU, "
        "HumanEval), and alignment techniques."
    ),
    preferred_tags=[
        "nlp", "language-model", "transformer", "bert", "gpt", "llm",
        "text-classification", "summarization", "machine-translation",
    ],
)

MULTIMODAL_SKILL = Skill(
    name="MultimodalSkill",
    description="Papers combining vision, language, audio, or other modalities.",
    extra_system_prompt=(
        "Pay special attention to: modality alignment strategy (contrastive, "
        "generative), cross-modal attention, training datasets (LAION, CC3M, "
        "WIT), and zero-shot transfer results."
    ),
    preferred_tags=[
        "multimodal", "vision-language-model", "clip", "contrastive-learning",
        "audio-language-model",
    ],
)

RL_SKILL = Skill(
    name="ReinforcementLearningSkill",
    description="Papers on reinforcement learning, RLHF, or agent-based learning.",
    extra_system_prompt=(
        "Pay special attention to: reward model design, environment benchmarks "
        "(Atari, MuJoCo, NetHack), exploration strategy, and safety constraints."
    ),
    preferred_tags=[
        "reinforcement-learning", "rlhf", "multi-agent", "planning",
        "autonomous-agent", "alignment",
    ],
)

GENERATIVE_SKILL = Skill(
    name="GenerativeSkill",
    description="Papers on generative models: diffusion, GANs, VAEs, or flow models.",
    extra_system_prompt=(
        "Pay special attention to: generative paradigm (score-based, flow-matching, "
        "adversarial), sampling efficiency, FID/IS evaluation scores, and "
        "guidance mechanisms (classifier-free guidance, CFG scale)."
    ),
    preferred_tags=[
        "diffusion-model", "stable-diffusion", "gan", "vae",
        "generative-adversarial-network", "variational-autoencoder",
    ],
)

EFFICIENCY_SKILL = Skill(
    name="EfficiencySkill",
    description="Papers on efficient ML: compression, quantisation, pruning, or efficient architectures.",
    extra_system_prompt=(
        "Pay special attention to: compression ratio, hardware targets "
        "(GPU, TPU, edge), throughput/latency improvements, accuracy "
        "degradation, and comparison with full-precision baselines."
    ),
    preferred_tags=[
        "model-compression", "quantization", "pruning", "knowledge-distillation",
        "efficient-transformer", "peft", "lora", "parameter-efficient-fine-tuning",
    ],
)

GENERAL_SKILL = Skill(
    name="GeneralMLSkill",
    description="General machine learning papers that do not fit a specialised category.",
    extra_system_prompt=(
        "Extract the key contributions, methodology, evaluation benchmarks, "
        "and limitations of this paper."
    ),
    preferred_tags=["benchmark", "dataset", "evaluation", "meta-learning"],
)

# Ordered list; first match wins
_SKILL_REGISTRY: list[Skill] = [
    TIME_SERIES_SKILL,
    VISION_SKILL,
    MULTIMODAL_SKILL,
    RL_SKILL,
    GENERATIVE_SKILL,
    EFFICIENCY_SKILL,
    NLP_SKILL,
    GENERAL_SKILL,
]

# ArXiv category → preferred skill mapping
_CATEGORY_SKILL_MAP: dict[str, Skill] = {
    "cs.CV": VISION_SKILL,
    "cs.CL": NLP_SKILL,
    "cs.LG": GENERAL_SKILL,
    "cs.AI": GENERAL_SKILL,
    "cs.RO": RL_SKILL,
    "stat.ML": GENERAL_SKILL,
    "eess.SP": TIME_SERIES_SKILL,
}


def route(paper: RawPaper) -> Skill:
    """Select the best-matching :class:`Skill` for *paper*.

    Strategy
    --------
    1. Check if the primary ArXiv category maps directly to a *specific* domain
       skill (not the general fallback).
    2. Scan the title + abstract for keyword signals.
    3. Fall back to :data:`GENERAL_SKILL`.
    """
    combined_text = f"{paper.title} {paper.abstract}".lower()

    # Category-based fast path – only for specific domain skills (not GENERAL_SKILL)
    category_skill = _CATEGORY_SKILL_MAP.get(paper.primary_category)
    if category_skill is not None and category_skill is not GENERAL_SKILL:
        if _count_signals(combined_text, category_skill.preferred_tags) > 0:
            logger.debug(
                "Router: '%s' → %s (via category %s)",
                paper.arxiv_id, category_skill.name, paper.primary_category,
            )
            return category_skill

    # Keyword-signal scoring across all skills
    best_skill: Skill = GENERAL_SKILL
    best_score: int = 0

    for skill in _SKILL_REGISTRY:
        score = _count_signals(combined_text, skill.preferred_tags)
        if score > best_score:
            best_score = score
            best_skill = skill

    logger.debug(
        "Router: '%s' → %s (score=%d)", paper.arxiv_id, best_skill.name, best_score
    )
    return best_skill


def _count_signals(text: str, tags: list[str]) -> int:
    """Count how many *tags* appear as whole-word substrings in *text*.

    Hyphens and underscores in a tag are treated as equivalent to a space,
    hyphen, or underscore in the text (e.g. "time-series" matches "time series").
    """
    count = 0
    for tag in tags:
        # Split on separators, escape each word part, join with a flexible
        # separator pattern so we don't accidentally escape the [ of the class.
        parts = re.split(r"[-_]", tag)
        escaped_parts = [re.escape(p) for p in parts if p]
        if not escaped_parts:
            continue
        pattern = r"[-_ ]?".join(escaped_parts)
        if re.search(pattern, text, re.IGNORECASE):
            count += 1
    return count
