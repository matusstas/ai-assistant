from pathlib import Path
import fitz
from tqdm import tqdm
import requests


################################################################################
# STAGE 1                                                                      #
################################################################################

def extract_text_from_image(
    path_image: str,
    url: str,
) -> str:
    """
    TODO
    """
    with open(path_image, "rb") as f:
        files = {"file": (path_image, f, "multipart/form-data")}
        response = requests.post(url, files=files)
        response.raise_for_status()
        return response.json().get("text")


def process_pdf(
    path: str,
    folder_image: str,
    folder_text: str,
    url_base: str,
    dpi: int = 300,
) -> None:
    """
    TODO
    """
    pdf = fitz.open(path)
    pdf_pages_cnt = pdf.page_count

    for i, pdf_page in enumerate(tqdm(pdf, total=pdf_pages_cnt, desc=f"Extracting pages from {path}"), start=1):
        pix = pdf_page.get_pixmap(dpi=dpi)
        
        path_image = folder_image / f"page_{i}.png"
        pix.save(path_image)

        text = extract_text_from_image(
            path_image=str(path_image),
            url=f"{url_base}/api/image-to-text",
        )

        path_text = folder_text / f"page_{i}.md"
        with open(path_text, "w") as f:
            f.write(text)

    pdf.close()


def process_pdf_all(
    folder_root: str,
    folder_data_images: str,
    folder_data_text: str,
    url_base: str,
    dpi: int,
) -> None:
    """
    TODO
    """
    folder = Path(folder_root)

    folder_images = Path(folder_data_images)
    folder_images.mkdir(parents=True, exist_ok=True)

    folder_text = Path(folder_data_text)
    folder_text.mkdir(parents=True, exist_ok=True)
    
    for subfolder in folder.iterdir():
        if not subfolder.is_dir():
            continue
            
        subfolder_images = folder_images / subfolder.name
        subfolder_images.mkdir(exist_ok=True)

        subfolder_text = folder_text / subfolder.name
        subfolder_text.mkdir(exist_ok=True)

        for file in subfolder.iterdir():
            if not file.is_file():
                continue

            filename_as_folder_images = subfolder_images / file.stem
            filename_as_folder_images.mkdir(exist_ok=True)

            filename_as_folder_text = subfolder_text / file.stem
            filename_as_folder_text.mkdir(exist_ok=True)

            process_pdf(
                path=file,
                folder_image=filename_as_folder_images,
                folder_text=filename_as_folder_text,
                url_base=url_base,
                dpi=dpi,
            )
