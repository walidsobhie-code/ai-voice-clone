"""Tests for AI Voice Clone"""
import pytest
import os
import sys

# Add parent to path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))


def test_clone_voice_import():
    """Test that clone_voice module can be imported"""
    from clone_voice import VoiceCloner
    assert VoiceCloner is not None


def test_synthesize_import():
    """Test that synthesize module can be imported"""
    from synthesize import VoiceSynthesizer
    assert VoiceSynthesizer is not None


def test_voice_cloner_init():
    """Test VoiceCloner initialization"""
    from clone_voice import VoiceCloner
    cloner = VoiceCloner()
    assert cloner is not None
    assert cloner.model_name is not None


def test_synthesizer_init():
    """Test VoiceSynthesizer initialization"""
    from synthesize import VoiceSynthesizer
    synth = VoiceSynthesizer()
    assert synth is not None


def test_available_models():
    """Test listing available models"""
    from clone_voice import VoiceCloner
    cloner = VoiceCloner()
    models = cloner.list_available_models()
    assert isinstance(models, list)


def test_synthesize_returns_dict():
    """Test synthesize returns proper dict"""
    from synthesize import VoiceSynthesizer
    synth = VoiceSynthesizer()
    result = synth.synthesize("test", "test.wav")
    assert isinstance(result, dict)
    assert "status" in result