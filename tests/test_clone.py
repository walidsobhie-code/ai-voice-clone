#!/usr/bin/env python3
"""Tests for AI Voice Clone"""
import unittest
import subprocess
import os

class TestVoiceClone(unittest.TestCase):
    
    def test_clone_script_exists(self):
        """Test that clone script exists"""
        self.assertTrue(os.path.exists('clone_voice.py'))
    
    def test_synthesize_script_exists(self):
        """Test that synthesize script exists"""
        self.assertTrue(os.path.exists('synthesize.py'))
    
    def test_requirements_exist(self):
        """Test that requirements.txt exists"""
        self.assertTrue(os.path.exists('requirements.txt'))
    
    def test_clone_script_runs(self):
        """Test that clone script runs"""
        result = subprocess.run(['python3', 'clone_voice.py', '--help'], 
                              capture_output=True, text=True)
        self.assertIn('clone', result.stdout.lower())
    
    def test_synthesize_script_runs(self):
        """Test that synthesize script runs"""
        result = subprocess.run(['python3', 'synthesize.py', '--help'],
                              capture_output=True, text=True)
        self.assertIn('synthesize', result.stdout.lower())

if __name__ == '__main__':
    unittest.main()
