from PIL import ImageGrab
from PIL.Image import Image
from Xlib import display, X
import subprocess
import os
import pytesseract


def grab_screen(region: tuple | None=None) -> Image:
    screen = ImageGrab.grab()
    try:
        cropped_image = screen.crop(region)
    except ValueError:
        if region:
            region = (region[2], region[3], region[0], region[1])
        cropped_image = screen.crop(region)

    return cropped_image


def save_image(image: Image, path: str, format: str="PNG"):
    image.save(path, format)


def copy_to_clipboard(file_path: str):
    subprocess.run(
        [
            "xclip",
            "-selection",
            "clipboard",
            "-t",
            "image/png",
            "-i",
            file_path,
        ]
    )


def get_selection_coordinates() -> tuple[tuple[int, int], tuple[int, int]]:
    d = display.Display()
    start = end = None
    root = d.screen().root
    root.grab_pointer(
        True,
        X.ButtonPressMask | X.ButtonReleaseMask,
        X.GrabModeAsync,
        X.GrabModeAsync,
        0,
        0,
        X.CurrentTime,
    )
    root.grab_keyboard(True, X.GrabModeAsync, X.GrabModeAsync, X.CurrentTime)
    print("Click on start point...")
    while True:
        event = d.next_event()
        if event.type == X.ButtonPress and event.detail == 1:
            if not start:
                start = (event.root_x, event.root_y)
                print("Click on end point...")
            else:
                end = (event.root_x, event.root_y)
                break
    d.ungrab_pointer(X.CurrentTime)
    d.ungrab_keyboard(X.CurrentTime)
    d.close()

    return start, end


def perform_ocr(image: Image, language: str="rus+eng") -> str:
    text = pytesseract.image_to_string(image, lang=language)

    return text.strip().replace("\n", " ")


def main():
    start, end = get_selection_coordinates()
    print(f"Start: {start} - End: {end}")

    if start and end:
        region = (start[0], start[1], end[0], end[1])
        cropped_image = grab_screen(region)
        temp_path = "/tmp/temp_screenshot.png"

        save_image(cropped_image, temp_path)
        copy_to_clipboard(temp_path)
        os.remove(temp_path)
        text = perform_ocr(cropped_image)

        print("Recognized text:\n\n")
        print(text)
        print("\n\n")


if __name__ == "__main__":
    main()
