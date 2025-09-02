# Merges backend responses into a single string or structure
class ResponseMerger:
    def merge(self, responses):
        # Example: concatenate all response texts
        merged = " ".join(
            r.get("responses", {}).get("text", "") for r in responses if r.get("success")
        )
        return {"success": all(r.get("success") for r in responses), "merged": merged, "raw": responses}
