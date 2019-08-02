import handy
import cv2

cap = cv2.VideoCapture(0)
hist = handy.capture_histogram(source=0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    handy.detect_face(frame, block=True)

    hand = handy.detect_hand(frame, hist)
    custom_outline = hand.draw_outline(
        min_area=10000, color=(0, 255, 255), thickness=2)

    quick_outline = hand.outline


    for fingertip in hand.fingertips:
        cv2.circle(quick_outline, fingertip, 5, (0, 0, 255), -1)

        com = hand.get_center_of_mass()
    if com:
        cv2.circle(quick_outline, com, 10, (255, 0, 0), -1)

    cv2.imshow("Handy", quick_outline)
    k = cv2.waitKey(5)
    # Press 'q' to exit
    if k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
