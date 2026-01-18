import asyncio
import typer

from pipeline.helpers import extract_pdf_all
from pipeline.settings import settings


async def _run_pipeline(
) -> None:
    """
    TODO
    """
    extract_pdf_all(
        folder_cloud_storage=settings.folder_cloud_storage,
        folder_data=settings.folder_data,
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
