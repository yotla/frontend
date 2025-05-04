import os
import json
import sys
from typing import Any, Optional, Dict

class Config:
    # Use class variables instead of instance variables
    _config_json: Optional[Dict[str, Any]] = None
    _argv_config: Optional[Dict[str, str]] = None
    _initialized: bool = False # Flag to ensure loading happens only once

    @staticmethod
    def _initialize() -> None:
        """Loads configuration sources if not already initialized."""
        if not Config._initialized:
            Config._load_config_json()
            Config._parse_argv()
            Config._initialized = True

    # --- Static Loading Methods ---
    @staticmethod
    def _load_config_json(filename: str = "config.json") -> None:
        """Loads configuration from a JSON file if it exists."""
        if Config._config_json is None: # Check if already loaded (redundant with _initialized but safe)
            try:
                filepath = os.path.abspath(filename)
                with open(filepath, 'r') as f:
                    Config._config_json = json.load(f)
                print(f"Static Config: Loaded configuration from {filepath}")
            except FileNotFoundError:
                Config._config_json = {}
                print(f"Static Config: {filename} (searched at {filepath}) not found. Skipping JSON config.")
            except json.JSONDecodeError:
                print(f"Static Config: Error decoding {filename}. Skipping JSON config.")
                Config._config_json = {}
            except Exception as e:
                print(f"Static Config: Error loading {filename}: {e}. Skipping JSON config.")
                Config._config_json = {}

    @staticmethod
    def _parse_argv() -> None:
        """Parses command line arguments in KEY=VALUE format."""
        if Config._argv_config is None: # Check if already parsed
            Config._argv_config = {}
            for arg in sys.argv[1:]:
                if '=' in arg:
                    key, value = arg.split('=', 1)
                    Config._argv_config[key] = value
            if Config._argv_config:
                print(f"Static Config: Loaded configuration from argv: {Config._argv_config}")

    # --- Static Public Get Method ---
    @staticmethod
    def get(key: str, default: Optional[Any] = None) -> Optional[Any]:
        """
        Retrieves a configuration value statically.

        Looks for the key in the following order:
        1. Environment variables (os.environ)
        2. config.json file (searched relative to cwd)
        3. Command line arguments (sys.argv, format: KEY=VALUE)

        Args:
            key: The configuration key to retrieve.
            default: The value to return if the key is not found in any source.

        Returns:
            The configuration value or the default value.
        """
        Config._initialize() # Ensure sources are loaded before accessing

        # 1. Check Environment Variables
        value = os.environ.get(key)
        if value is not None:
            return value

        # 2. Check config.json
        if Config._config_json and isinstance(Config._config_json, dict):
             value = Config._config_json.get(key)
             if value is not None:
                 return value

        # 3. Check Command Line Arguments
        if Config._argv_config:
            value = Config._argv_config.get(key)
            if value is not None:
                return value

        # 4. Return Default
        return default