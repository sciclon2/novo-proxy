# Script to test novo-proxy
if __name__ == "__main__":
    import sys
    from src.proxy import Proxy
    if len(sys.argv) < 3:
        print("Usage: python test_proxy.py <user_id> <message>")
        sys.exit(1)
    user_id = sys.argv[1]
    message = sys.argv[2]
    proxy = Proxy()
    result = proxy.handle_request({"user_id": user_id, "message": message})
    print(result)
