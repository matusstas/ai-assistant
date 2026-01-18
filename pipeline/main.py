import asyncio
import typer

from pipeline.helpers import process_pdf_all
from pipeline.settings import settings


async def _run_pipeline(
) -> None:
    """
    TODO
    """
    process_pdf_all(
        folder_root=settings.folder_root,
        folder_data_images=settings.folder_data_images,
        folder_data_text=settings.folder_data_text,
        folder_data_embeddings=settings.folder_data_embeddings,
        url_base=settings.url_base,
        dpi=settings.dpi,
    )



app = typer.Typer()


@app.command()
def run_pipeline_cli(
) -> None:
    # typer.echo is a must have, otherwise `print()` won't print.
    typer.echo(
        asyncio.run(
            _run_pipeline(
            )
        )
    )


if __name__ == "__main__":
    app()
