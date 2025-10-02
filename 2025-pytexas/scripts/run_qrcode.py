#!/usr/bin/env python3
# /// script
# dependencies = [
#   "typer",
#   "qrcode[pil]"
# ]
# ///

import typer
import qrcode
from pathlib import Path

app = typer.Typer(help="Generate a QR code PNG for any URL.")

@app.command()
def make(
    url: str = typer.Argument(..., help="The URL to encode as a QR code"),
    output: Path = typer.Option(Path("qrcode.png"), "--output", "-o", help="Output file"),
):
    """
    Create a QR code PNG for the provided URL.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output)
    typer.echo(f"✅ QR code saved to {output}")

if __name__ == "__main__":
    app()
