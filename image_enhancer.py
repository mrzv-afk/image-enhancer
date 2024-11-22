from PIL import Image, ImageEnhance
import os

def enhance_image(input_path, output_path=None, 
                 brightness=1.2, 
                 contrast=1.2, 
                 color=1.2, 
                 sharpness=1.5):
    try:
        img = Image.open(input_path)
        
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(brightness)
        
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(contrast)
        
        enhancer = ImageEnhance.Color(img)
        img = enhancer.enhance(color)
        
        enhancer = ImageEnhance.Sharpness(img)
        img = enhancer.enhance(sharpness)
        
        if output_path is None:
            filename, ext = os.path.splitext(input_path)
            output_path = f"{filename}_enhanced{ext}"
        
        img.save(output_path)
        print(f"Изображение успешно улучшено и сохранено: {output_path}")
        
    except Exception as e:
        print(f"Произошла ошибка при обработке изображения: {str(e)}")

def main():
    input_image = input("Введите путь к изображению: ")
    if os.path.exists(input_image):
        enhance_image(input_image)
    else:
        print("Файл не найден. Проверьте путь к изображению.")

if __name__ == "__main__":
    main()
