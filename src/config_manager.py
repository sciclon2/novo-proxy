import yaml
import threading

class ConfigManager:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, config_path="configs/novo-proxy.yaml"):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
                    cls._instance._load_config(config_path)
        return cls._instance

    def _load_config(self, config_path):
        with open(config_path, 'r') as f:
            self._config = yaml.safe_load(f)

    def get(self, key, default=None):
        return self._config.get(key, default)

    def all(self):
        return self._config
