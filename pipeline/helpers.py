from pathlib import Path
import fitz
from tqdm import tqdm

################################################################################
# STAGE 1                                                                      #
################################################################################

def extract_pdf(
    path: str,
    folder_dst: str,
    dpi: int = 300,
) -> None:
    """
    TODO
    """
    pdf = fitz.open(path)
    pdf_pages_cnt = pdf.page_count

    for i, pdf_page in enumerate(tqdm(pdf, total=pdf_pages_cnt, desc=f"Extracting pages from {path}"), start=1):
        pix = pdf_page.get_pixmap(dpi=dpi)
        pix.save(folder_dst / f"page_{i}.png")

    pdf.close()


def extract_pdf_all(
    folder_cloud_storage: str,
    folder_data: str,
    dpi: int,
) -> None:
    """
    TODO
    """
    folder_src = Path(folder_cloud_storage)
    folder_dst = Path(folder_data)
    folder_dst.mkdir(exist_ok=True)

    for folder_src_cat in folder_src.iterdir():
        if folder_src_cat.is_dir():
            folder_dst_cat = folder_dst / folder_src_cat.name
            folder_dst_cat.mkdir(exist_ok=True)

            for file_src_path in folder_src_cat.iterdir():
                if file_src_path.is_file():
                    folder_file_src = folder_dst_cat / file_src_path.stem
                    folder_file_src.mkdir(exist_ok=True)

                    extract_pdf(
                        path=file_src_path,
                        folder_dst=folder_file_src,
                        dpi=dpi,
                    )
