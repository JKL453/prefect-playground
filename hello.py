from prefect import flow

@flow
def hello():
    print("Hello from my data platform!")

if __name__ == "__main__":
    hello()