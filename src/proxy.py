
from src.message_analyzer import MessageAnalyzer
from src.backend_client import BackendClient
from src.response_merger import ResponseMerger
from src.response_normalizer import ResponseNormalizer
from src.logger import get_logger
from src.config_manager import ConfigManager



class Proxy:
    def __init__(self, config_path="configs/novo-proxy.yaml"):
        self.config = ConfigManager(config_path)
        self.logger = get_logger(
            "novo-proxy",
            self.config.get('log_file', '../logs/novo-proxy.log'),
            self.config.get('log_level', 'INFO')
        )
        self.analyzer = MessageAnalyzer()
        self.backend = BackendClient(self.config.get('backend_url'), self.config.get('timeout_seconds'))
        self.merger = ResponseMerger()
        self.normalizer = ResponseNormalizer()

    def handle_request(self, request_json):
        user_id = request_json.get('user_id')
        message = request_json.get('message')
        self.logger.info(f"Received message from user {user_id}: {message}")
        analysis = self.analyzer.analyze(message)
        # analysis['category_messages'] should be a dict: {category: [msg1, msg2, ...]}
        category_messages = analysis.get('category_messages')
        sentiment = analysis.get('sentiment')
        self.logger.debug(f"Category messages: {category_messages}, Sentiment: {sentiment}")
        responses = self.backend.send_parallel(user_id, category_messages, sentiment)
        merged = self.merger.merge(responses)
        normalized = self.normalizer.normalize(merged)
        return normalized
