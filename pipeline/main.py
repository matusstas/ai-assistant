import asyncio
import typer


async def _run_pipeline(
) -> None:
    """
    TODO
    """
    print("test")


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
