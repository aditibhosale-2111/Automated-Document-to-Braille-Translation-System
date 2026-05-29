def log_results(data):
    with open("logs.txt", "a") as f:
        f.write(str(data) + "\n")