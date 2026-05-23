import cv2
import numpy as np


cap = cv2.VideoCapture(0)

modo_noturno = False

    # Loop para capturar e exibir os frames da webcam
while True:
    ret, frame = cap.read()

    if not ret:
        break

    key = cv2.waitKey(1)

    #Q para tirar foto
    if key == ord('q'):
            cv2.imwrite('foto.png', frame)
            print("Foto salva!")

    # Ativar modo noturno
    if key == ord('e'):
        modo_noturno = True

    # Desativa modo noturno
    if key == ord('r'):
        modo_noturno = False

    # Se modo noturno estiver ativo
    if modo_noturno:
        frame_exibir = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_exibir = cv2.applyColorMap(
            frame_exibir,
            cv2.COLORMAP_SUMMER
        )
    else:
        frame_exibir = frame

    cv2.imshow('PyCam', frame_exibir)

    # ESC fecha
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()