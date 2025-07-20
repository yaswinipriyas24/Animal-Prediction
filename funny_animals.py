import cv2
import random
import time
import os # Import the os module for path manipulation

# --- Configuration ---
HAAR_CASCADE_PATH = 'haarcascade_frontalface_default.xml'
ANIMAL_IMAGES_FOLDER = 'animal_images' # Folder where your animal images are stored

# Map of funny animal names to their corresponding image filenames
# IMPORTANT: Make sure these filenames exactly match the images you place in the 'animal_images' folder!
ANIMAL_IMAGE_MAP = {
    "Sassy Sloth": "sassy_sloth.png",
    "Goofy Goat": "goofy_goat.png",
    "Wacky Walrus": "wacky_walrus.png",
    "Cheeky Chinchilla": "cheeky_chinchilla.png",
    "Grumpy Cat": "grumpy_cat.png",
    "Majestic Manatee": "majestic_manatee.png",
    "Ponderous Penguin": "ponderous_penguin.png",
    "Daring Duck": "daring_duck.png",
    "Sleepy Owl": "sleepy_owl.png",
    "Sneaky Ferret": "sneaky_ferret.png",
    "Enthusiastic Elephant": "enthusiastic_elephant.png",
    "Dramatic Llama": "dramatic_llama.png",
    "Fabulous Flamingo": "fabulous_flamingo.png",
    "Curious Meerkat": "curious_meerkat.png",
    "Questionable Quokka": "questionable_quokka.png"
}

# Time (in seconds) to display each animal suggestion/image
DISPLAY_DURATION = 3

# --- Image Loading ---
loaded_animal_images = {}
for animal_name, filename in ANIMAL_IMAGE_MAP.items():
    img_path = os.path.join(ANIMAL_IMAGES_FOLDER, filename)
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED) # Load image with alpha channel if present

    if img is None:
        print(f"WARNING: Could not load image for '{animal_name}' from {img_path}")
        print("Please ensure the image exists and the path is correct.")
        continue
    loaded_animal_images[animal_name] = img

if not loaded_animal_images:
    print("ERROR: No animal images were loaded. Please check your 'animal_images' folder and filenames.")
    exit()

# --- Initialize Face Detector and Webcam ---
face_cascade = cv2.CascadeClassifier(HAAR_CASCADE_PATH)

if face_cascade.empty():
    print(f"ERROR: Could not load Haar Cascade classifier from {HAAR_CASCADE_PATH}")
    print("Please ensure 'haarcascade_frontalface_default.xml' is in the same directory as your script.")
    exit()

cap = cv2.VideoCapture(0) # 0 for default webcam. Try 1, 2, etc. if you have multiple cameras.

if not cap.isOpened():
    print("ERROR: Could not open webcam.")
    print("Please check if your webcam is connected and not in use by another application.")
    exit()

# Variables to manage current suggestion and timing
current_animal_name = None
current_animal_image = None
last_face_time = 0
last_suggestion_change_time = 0

print("Webcam initialized! Look into the camera for your spirit animal!")
print("Press 'q' to quit.")

# --- Function to overlay a transparent PNG image ---
def overlay_transparent_image(background, overlay, x, y, scale=1.0):
    if overlay is None:
        return background

    h, w, _ = background.shape
    ov_h, ov_w, _ = overlay.shape

    # Resize overlay based on scale
    new_ov_w = int(ov_w * scale)
    new_ov_h = int(ov_h * scale)
    if new_ov_w == 0 or new_ov_h == 0: # Avoid division by zero
        return background

    overlay_resized = cv2.resize(overlay, (new_ov_w, new_ov_h), interpolation=cv2.INTER_AREA)

    # Extract alpha channel if it exists
    if overlay_resized.shape[2] == 4:
        alpha_channel = overlay_resized[:, :, 3]
        # Create inverse mask
        alpha_mask = alpha_channel / 255.0
        inverse_mask = 1.0 - alpha_mask

        # Convert to 3 channels for multiplication
        alpha_mask_3ch = cv2.cvtColor(alpha_mask, cv2.COLOR_GRAY2BGR)
        inverse_mask_3ch = cv2.cvtColor(inverse_mask, cv2.COLOR_GRAY2BGR)
    else: # No alpha channel, assume it's opaque
        alpha_mask_3ch = None # Indicates no alpha blending needed

    # Calculate overlay region in background
    y1, y2 = max(0, y), min(h, y + new_ov_h)
    x1, x2 = max(0, x), min(w, x + new_ov_w)

    # Calculate actual dimensions of the overlay that fit within bounds
    # (Used when image goes off screen)
    overlay_y1 = max(0, -y)
    overlay_x1 = max(0, -x)
    overlay_y2 = overlay_y1 + (y2 - y1)
    overlay_x2 = overlay_x1 + (x2 - x1)

    if (x2 - x1 > 0) and (y2 - y1 > 0): # Ensure ROI is valid
        # Get ROI from background
        roi = background[y1:y2, x1:x2]

        # Get the part of the resized overlay that fits within the ROI
        overlay_roi = overlay_resized[overlay_y1:overlay_y2, overlay_x1:overlay_x2]

        if alpha_mask_3ch is not None:
            # Perform alpha blending
            foreground_roi = overlay_roi[:, :, :3] # Take only BGR channels from overlay
            alpha_mask_roi = alpha_mask_3ch[overlay_y1:overlay_y2, overlay_x1:overlay_x2]
            inverse_mask_roi = inverse_mask_3ch[overlay_y1:overlay_y2, overlay_x1:overlay_x2]

            # Blend the two images using the alpha mask
            blended_roi = (foreground_roi * alpha_mask_roi + roi * inverse_mask_roi).astype('uint8')
            background[y1:y2, x1:x2] = blended_roi
        else:
            # If no alpha, just copy the overlay onto the background ROI
            background[y1:y2, x1:x2] = overlay_roi


    return background

# --- Main Loop ---
while True:
    ret, frame = cap.read() # Read a frame from the webcam

    if not ret:
        print("Failed to grab frame, exiting...")
        break

    # Flip the frame horizontally, as webcams often mirror the image
    frame = cv2.flip(frame, 1)

    # Convert the frame to grayscale for face detection (it's faster)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

    current_time = time.time()

    if len(faces) > 0:
        # If faces are detected, update the last_face_time
        last_face_time = current_time

        # If it's time for a new suggestion, pick a random animal
        if current_time - last_suggestion_change_time > DISPLAY_DURATION:
            random_animal_name = random.choice(list(ANIMAL_IMAGE_MAP.keys()))
            current_animal_name = random_animal_name
            current_animal_image = loaded_animal_images.get(current_animal_name)
            last_suggestion_change_time = current_time
    else:
        # If no face is detected for a while, clear the suggestion
        if current_time - last_face_time > DISPLAY_DURATION * 2: # Give it more time to clear
            current_animal_name = None
            current_animal_image = None
            last_suggestion_change_time = current_time # Reset for when a face reappears

    # Draw rectangles around the detected faces and overlay the animal image
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2) # Blue rectangle around face

        if current_animal_image is not None:
            # Calculate size for the overlayed image (e.g., 80% of face width)
            overlay_width = int(w * 0.8)
            overlay_height = int(current_animal_image.shape[0] * (overlay_width / current_animal_image.shape[1]))

            # Position the image slightly above and centered on the face
            img_x = x + (w - overlay_width) // 2
            img_y = y - overlay_height - 10 # 10 pixels above the face

            # Ensure the image is not off the top of the screen
            if img_y < 0:
                img_y = y + h + 10 # Place it below the face if it would go off screen

            frame = overlay_transparent_image(frame, current_animal_image, img_x, img_y, scale=overlay_width / current_animal_image.shape[1])

    # If no face is detected AND no image is currently shown, display "No face detected..."
    if current_animal_name is None and len(faces) == 0:
        cv2.putText(frame, "No face detected...", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)


    # Display the resulting frame
    cv2.imshow('My Spirit Animal (Probably Not)', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# --- Cleanup ---
cap.release() # Release the webcam
cv2.destroyAllWindows() # Close all OpenCV windows

print("Exited the program.")