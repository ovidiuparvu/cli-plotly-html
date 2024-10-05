from pathlib import Path
import plotly.express as px
from typer import Typer
import uuid


app = Typer()


def temp_file_path(extension: str) -> Path:
    tmp_dir = Path.home() / "tmp"
    tmp_dir.mkdir(exist_ok=True)
    return tmp_dir / f"{uuid.uuid4()}.{extension}"


@app.command()
def plot():
    # Sample data
    z = [
        [1, 20, 30],
        [20, 1, 60],
        [30, 60, 1]
    ]

    # Create heatmap
    fig = px.imshow(z, color_continuous_scale='Viridis')

    # Save the heatmap to an HTML file
    tmp_file = temp_file_path("html")
    fig.write_html(tmp_file, auto_open=True)


if __name__ == "__main__":
    app()