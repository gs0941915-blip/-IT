import cv2
from PIL import Image


image_path = 'people.jpg'          # головне фото
mask_path = 'emoji.png'            # картинка для накладання


face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

image = cv2.imread(image_path)

# Переводимо у відтінки сірого
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(50, 50)
)

print("Знайдено облич:", len(faces))


main_image = Image.open(image_path).convert("RGBA")
mask = Image.open(mask_path).convert("RGBA")


for (x, y, w, h) in faces:

    # Змінюємо розмір маски під обличчя
    resized_mask = mask.resize((w, h))

    # Координати вставки
    position = (x, y)

    # Накладаємо маску
    main_image.paste(resized_mask, position, resized_mask)

output_path = "result.png"
main_image.save(output_path)


result = cv2.imread(output_path)

cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()