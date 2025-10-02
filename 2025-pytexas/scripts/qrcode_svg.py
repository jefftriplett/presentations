#!/usr/bin/env python3
# /// script
# dependencies = [
#   "typer",
#   "segno"
# ]
# ///

import typer
import segno
from pathlib import Path

app = typer.Typer(help="Generate a crisp SVG QR code for any URL.")

@app.command()
def make(
    url: str = typer.Argument(..., help="The URL to encode"),
    output: Path = typer.Option(Path("qrcode.svg"), "--output", "-o", help="Output file"),
    scale: int = typer.Option(10, help="Scale factor for the SVG"),
):
    """
    Create a QR code SVG for the provided URL.
    """
    segno.make(url).save(output, scale=scale)
    typer.echo(f"✅ QR code saved to {output}")

if __name__ == "__main__":
    app()
