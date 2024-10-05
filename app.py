from typer import Typer


app = Typer()

@app.command()
def plot():
    print("Plotting...")

if __name__ == "__main__":
    app()