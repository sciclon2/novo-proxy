import concurrent.futures
import requests

class BackendClient:
    def __init__(self, backend_url, timeout):
        self.backend_url = backend_url.rstrip("/")
        self.timeout = timeout

    def send_parallel(self, user_id, category_messages: dict, sentiment):
        """
        category_messages: dict of {category: [message1, message2, ...]}
        """
        results = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for category, messages in category_messages.items():
                for msg in messages:
                    futures.append(executor.submit(self._send, user_id, msg, category, sentiment))
            for future in concurrent.futures.as_completed(futures, timeout=self.timeout):
                try:
                    results.append(future.result())
                except Exception as e:
                    results.append({"success": False, "error": str(e)})
        return results

    def _send(self, user_id, message, category, sentiment):
        payload = {
            "user_id": user_id,
            "message": message,
            "category": category,
            "sentiment": sentiment
        }
        url = f"{self.backend_url}/{category}"
        try:
            resp = requests.post(url, json=payload, timeout=self.timeout)
            return resp.json()
        except Exception as e:
            return {"success": False, "error": str(e)}
