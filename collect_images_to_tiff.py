import os
from PIL import Image


def collect_images_from_main_folder(main_folder):
    images = []
    for root, dirs, files in os.walk(main_folder):
        for file_name in files:
            if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                file_path = os.path.join(root, file_name)
                try:
                    img = Image.open(file_path)
                    images.append(img.convert('RGB'))  # Конвертируем изображения в RGB
                except Exception as e:
                    print(f"Could not open image {file_path}: {e}")
    return images


def save_images_to_tiff(images, output_path):
    if images:
        images[0].save(output_path, save_all=True, append_images=images[1:], compression='tiff_deflate')
        print(f"Saved {len(images)} images to {output_path}")
    else:
        print("No images to save.")


def main():
    main_folder = '/home/aroxan/Downloads/test_tif'  # Путь к главной папке
    output_path = 'Result.tif'

    images = collect_images_from_main_folder(main_folder)

    # Отладка: сохранение изображений отдельно
    debug_folder = '/home/aroxan/Downloads/test_tif_output'
    if not os.path.exists(debug_folder):
        os.makedirs(debug_folder)
    for i, img in enumerate(images):
        img.save(os.path.join(debug_folder, f'image_{i}.png'))
        print(f"Saved image {i} to {debug_folder}")

    save_images_to_tiff(images, output_path)


if __name__ == "__main__":
    main()
