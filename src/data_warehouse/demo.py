from tiny_poetry_pkg import fetch_status

def check_dependency() -> int:
    # Uses the dependency package in real code.
    return fetch_status("https://httpbin.org/status/204")

def main() -> None:
    code = check_dependency()
    print(f"data_warehouse demo OK (status={code})")
