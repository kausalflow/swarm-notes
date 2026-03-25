"""Tests for src.config model auto-detection logic."""

from __future__ import annotations

import os
import sys
from unittest.mock import patch


def _reload_config(env: dict[str, str]):
    """Reload src.config with a clean environment snapshot."""
    # Remove cached module so module-level code reruns
    sys.modules.pop("src.config", None)
    with patch.dict("os.environ", env, clear=True):
        with patch("dotenv.load_dotenv"):
            import src.config as cfg
            return cfg


class TestDefaultLlmModel:
    """_default_llm_model() returns the right model for each key combination."""

    def test_explicit_llm_model_env_wins(self):
        cfg = _reload_config(
            {
                "LLM_MODEL": "openai:gpt-4o",
                "GEMINI_API_KEY": "AIzaSy_fake_gemini_key",
            }
        )
        assert cfg.LLM_MODEL == "openai:gpt-4o"

    def test_gemini_api_key_selects_gemini_model(self):
        cfg = _reload_config({"GEMINI_API_KEY": "AIzaSy_fake_gemini_key"})
        assert cfg.LLM_MODEL == "google-gla:gemini-2.0-flash"

    def test_google_api_key_selects_gemini_model(self):
        cfg = _reload_config({"GOOGLE_API_KEY": "AIzaSy_fake_google_key"})
        assert cfg.LLM_MODEL == "google-gla:gemini-2.0-flash"

    def test_llm_api_key_with_google_prefix_selects_gemini_model(self):
        cfg = _reload_config({"LLM_API_KEY": "AIzaSy_fake_llm_key"})
        assert cfg.LLM_MODEL == "google-gla:gemini-2.0-flash"

    def test_no_keys_falls_back_to_openai(self):
        cfg = _reload_config({})
        assert cfg.LLM_MODEL == "openai:gpt-4o-mini"

    def test_openai_key_falls_back_to_openai(self):
        cfg = _reload_config({"OPENAI_API_KEY": "sk-fake-openai-key"})
        assert cfg.LLM_MODEL == "openai:gpt-4o-mini"

    def test_llm_api_key_without_google_prefix_falls_back_to_openai(self):
        cfg = _reload_config({"LLM_API_KEY": "sk-fake-openai-key"})
        assert cfg.LLM_MODEL == "openai:gpt-4o-mini"


class TestGeminiApiKeyPropagation:
    """When LLM_API_KEY is a Google key, GEMINI_API_KEY is auto-propagated."""

    def test_gemini_key_propagated_from_llm_api_key(self):
        sys.modules.pop("src.config", None)
        fake_key = "AIzaSy_test_propagation_key"
        with patch.dict("os.environ", {"LLM_API_KEY": fake_key}, clear=True):
            with patch("dotenv.load_dotenv"):
                import src.config as cfg  # noqa: F401

            assert os.environ.get("GEMINI_API_KEY") == fake_key

    def test_existing_gemini_key_not_overwritten(self):
        sys.modules.pop("src.config", None)
        existing = "AIzaSy_already_set"
        new_key = "AIzaSy_should_not_override"
        with patch.dict(
            "os.environ",
            {"GEMINI_API_KEY": existing, "LLM_API_KEY": new_key},
            clear=True,
        ):
            with patch("dotenv.load_dotenv"):
                import src.config as cfg  # noqa: F401

            assert os.environ.get("GEMINI_API_KEY") == existing
