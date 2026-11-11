import argparse
import time
import requests

def check_url(url, timeout=5):
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    start_time = time.time()
    try:
        response = requests.get(url, timeout=timeout, allow_redirects=True)
        response_time = round((time.time() - start_time) * 1000, 2)
        
        status = "ONLINE" if response.status_code == 200 else "WARNING"
        return {
            "url": url,
            "status": status,
            "status_code": response.status_code,
            "response_time_ms": response_time,
            "redirects": len(response.history)
        }
    except requests.exceptions.RequestException as e:
        return {
            "url": url,
            "status": "OFFLINE",
            "error": str(e)
        }

def main():
    parser = argparse.ArgumentParser(description="FastLink: High-performance URL & Website Health Checker")
    parser.add_argument("urls", nargs="+", help="One or more URLs to analyze")
    parser.add_argument("--timeout", type=int, default=5, help="Request timeout in seconds")
    
    args = parser.parse_args()
    
    print("\n--- FastLink Checker Results ---")
    for u in args.urls:
        res = check_url(u, timeout=args.timeout)
        if res.get("status") == "OFFLINE":
            print(f"[FAIL] {res['url']} is down. Error: {res.get('error')}")
        else:
            print(f"[{res['status']}] {res['url']} | Code: {res['status_code']} | Latency: {res['response_time_ms']}ms | Redirects: {res['redirects']}")
    print("--------------------------------\n")

if __name__ == "__main__":
    main()
