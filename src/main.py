import cv2

webcam = cv2.VideoCapture(0)

if webcam.isOpened():
    validado, frame = webcam.read()

    # Loop para mostrar o vídeo da webcam
    while validado:
        validado, frame = webcam.read()

        # Exibe o vídeo da webcam
        cv2.imshow('PyCam', frame)

        # Captura tecla pressionada
        key = cv2.waitKey(1)

        # ESC para sair
        if key == 27:
            break

        # Q para tirar foto
        if key == ord('q'):
            cv2.imwrite('foto.png', frame)
            print("Foto salva!")

# Libera webcam e fecha janelas
webcam.release()
cv2.destroyAllWindows()