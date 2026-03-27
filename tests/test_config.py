"""Tests for src.config model auto-detection logic."""

from __future__ import annotations

import os
import sys
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch


def _reload_config(env: dict[str, str]):
    """Reload src.config with a clean environment snapshot."""
    # Remove cached module so module-level code reruns
    sys.modules.pop("swarm_notes.config", None)
    with patch.dict("os.environ", env, clear=True):
        with patch("dotenv.load_dotenv"):
            import swarm_notes.config as cfg
            return cfg


class TestDefaultLlmModel:
    """_default_llm_model() returns the right model for each key combination."""

    def test_explicit_llm_model_env_wins(self):
        cfg = _reload_config(
            {
                "settings.llm_model": "openai:gpt-4o",
                "GEMINI_API_KEY": "AIzaSy_fake_gemini_key",
            }
        )
        assert cfg.settings.llm_model == "openai:gpt-4o"

    def test_gemini_api_key_selects_gemini_model(self):
        cfg = _reload_config({"GEMINI_API_KEY": "AIzaSy_fake_gemini_key"})
        assert cfg.settings.llm_model == "gemini-flash-lite-latest"

    def test_google_api_key_selects_gemini_model(self):
        cfg = _reload_config({"GOOGLE_API_KEY": "AIzaSy_fake_google_key"})
        assert cfg.settings.llm_model == "gemini-flash-lite-latest"

    def test_llm_api_key_with_google_prefix_selects_gemini_model(self):
        cfg = _reload_config({"LLM_API_KEY": "AIzaSy_fake_llm_key"})
        assert cfg.settings.llm_model == "gemini-flash-lite-latest"

    def test_no_keys_falls_back_to_openai(self):
        cfg = _reload_config({})
        assert cfg.settings.llm_model == "openai:gpt-4o-mini"

    def test_openai_key_falls_back_to_openai(self):
        cfg = _reload_config({"OPENAI_API_KEY": "sk-fake-openai-key"})
        assert cfg.settings.llm_model == "openai:gpt-4o-mini"

    def test_llm_api_key_without_google_prefix_falls_back_to_openai(self):
        cfg = _reload_config({"LLM_API_KEY": "sk-fake-openai-key"})
        assert cfg.settings.llm_model == "openai:gpt-4o-mini"


class TestGeminiApiKeyPropagation:
    """When LLM_API_KEY is a Google key, GEMINI_API_KEY is auto-propagated."""

    def test_gemini_key_propagated_from_llm_api_key(self):
        sys.modules.pop("swarm_notes.config", None)
        fake_key = "AIzaSy_test_propagation_key"
        with patch.dict("os.environ", {"LLM_API_KEY": fake_key}, clear=True):
            with patch("dotenv.load_dotenv"):
                import swarm_notes.config as cfg  # noqa: F401

            assert os.environ.get("GEMINI_API_KEY") == fake_key

    def test_existing_gemini_key_not_overwritten(self):
        sys.modules.pop("swarm_notes.config", None)
        existing = "AIzaSy_already_set"
        new_key = "AIzaSy_should_not_override"
        with patch.dict(
            "os.environ",
            {"GEMINI_API_KEY": existing, "LLM_API_KEY": new_key},
            clear=True,
        ):
            with patch("dotenv.load_dotenv"):
                import swarm_notes.config as cfg  # noqa: F401

            assert os.environ.get("GEMINI_API_KEY") == existing

class TestPaperSourceConfig:
    def test_paper_source_defaults_to_arxiv(self):
        cfg = _reload_config({})
        assert cfg.settings.paper_source == "arxiv"

    def test_semantic_scholar_api_key_loaded_from_env(self):
        cfg = _reload_config({"SEMANTIC_SCHOLAR_API_KEY": "test-key"})
        assert cfg.settings.semantic_scholar_api_key == "test-key"

    def test_openalex_relevance_mode_loaded_from_env(self):
        cfg = _reload_config({"OPENALEX_RELEVANCE_MODE": "all_tokens"})
        assert cfg.settings.openalex_relevance_mode == "all_tokens"

    def test_openalex_max_pages_loaded_from_env(self):
        cfg = _reload_config({"OPENALEX_MAX_PAGES_PER_WINDOW": "7"})
        assert cfg.settings.openalex_max_pages_per_window == 7

    def test_paper_keywords_loaded_from_new_env(self):
        cfg = _reload_config({"PAPER_KEYWORDS": "time series,forecasting"})
        assert cfg.settings.paper_keywords == ["time series", "forecasting"]

    def test_legacy_arxiv_env_names_still_work(self):
        cfg = _reload_config(
            {
                "ARXIV_KEYWORDS": "time series,forecasting",
                "ARXIV_MAX_RESULTS_PER_KEYWORD": "11",
                "ARXIV_TOTAL_CAP": "55",
            }
        )
        assert cfg.settings.paper_keywords == ["time series", "forecasting"]
        assert cfg.settings.paper_max_results_per_keyword == 11
        assert cfg.settings.paper_total_cap == 55

    def test_yaml_can_switch_to_semantic_scholar(self):
        with TemporaryDirectory() as temp_dir:
            config_path = Path(temp_dir) / "config.yaml"
            config_path.write_text(
                'paper_source: "semantic_scholar"\nsemantic_scholar_api_key: "yaml-key"\n',
                encoding="utf-8",
            )

            sys.modules.pop("swarm_notes.config", None)
            with patch.dict("os.environ", {}, clear=True):
                with patch("dotenv.load_dotenv"):
                    import swarm_notes.config as cfg

                loaded = cfg.Settings.load_from_yaml(config_path)

            assert loaded.paper_source == "semantic_scholar"
            assert loaded.semantic_scholar_api_key == "yaml-key"

    def test_yaml_can_set_openalex_relevance_mode(self):
        with TemporaryDirectory() as temp_dir:
            config_path = Path(temp_dir) / "config.yaml"
            config_path.write_text(
                'paper_source: "openalex"\nopenalex_relevance_mode: "all_tokens"\n',
                encoding="utf-8",
            )

            sys.modules.pop("swarm_notes.config", None)
            with patch.dict("os.environ", {}, clear=True):
                with patch("dotenv.load_dotenv"):
                    import swarm_notes.config as cfg

                loaded = cfg.Settings.load_from_yaml(config_path)

            assert loaded.paper_source == "openalex"
            assert loaded.openalex_relevance_mode == "all_tokens"

    def test_yaml_can_set_openalex_max_pages(self):
        with TemporaryDirectory() as temp_dir:
            config_path = Path(temp_dir) / "config.yaml"
            config_path.write_text(
                (
                    'paper_search:\n'
                    '  source: "openalex"\n'
                    '  openalex:\n'
                    '    max_pages_per_window: 9\n'
                ),
                encoding="utf-8",
            )

            sys.modules.pop("swarm_notes.config", None)
            with patch.dict("os.environ", {}, clear=True):
                with patch("dotenv.load_dotenv"):
                    import swarm_notes.config as cfg

                loaded = cfg.Settings.load_from_yaml(config_path)

            assert loaded.paper_source == "openalex"
            assert loaded.openalex_max_pages_per_window == 9

    def test_legacy_arxiv_yaml_keys_are_mapped(self):
        with TemporaryDirectory() as temp_dir:
            config_path = Path(temp_dir) / "config.yaml"
            config_path.write_text(
                (
                    'arxiv_keywords:\n'
                    '  - "time series"\n'
                    '  - "forecasting"\n'
                    'arxiv_max_results_per_keyword: 9\n'
                    'arxiv_total_cap: 44\n'
                ),
                encoding="utf-8",
            )

            sys.modules.pop("swarm_notes.config", None)
            with patch.dict("os.environ", {}, clear=True):
                with patch("dotenv.load_dotenv"):
                    import swarm_notes.config as cfg

                loaded = cfg.Settings.load_from_yaml(config_path)

            assert loaded.paper_keywords == ["time series", "forecasting"]
            assert loaded.paper_max_results_per_keyword == 9
            assert loaded.paper_total_cap == 44
