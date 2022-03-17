import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

with mp_hands.Hands(
	static_image_mode=True,
	max_num_hands=2,
	min_detection_confidence=0.5) as hands:
	
	image = cv2.imread("6.jpeg")
	height, width, _ = image.shape
	image = cv2.flip(image,1)

	image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	results = hands.process(image_rgb)

	# HANDEDNESS
	print('Handedness: ', results.multi_handedness)

	# HAND LANDMARKS
	#print('Hand landmarks', results.multi_hand_landmarks)

	# Validar que si exista una mano antes de proceder a dibujarla
	if results.multi_hand_landmarks is not None:
		#---------------------------------------------------------------------------------------------
		#Ciclo para recorrer el array de coordenadas de los puntos
		# for hand_landmarks in results.multi_hand_landmarks:
		#	#print(hand_landmarks)
		#	mp_drawing.draw_landmarks(
		#		image, 
		#		hand_landmarks, 
		#		mp_hands.HAND_CONNECTIONS,
		#		# (color,grosor, radio del punto)
		#		mp_drawing.DrawingSpec(color=(0,0,255), thickness=4, circle_radius=2),
		#		# (color, grosor linea)
		#		mp_drawing.DrawingSpec(color=(255,0,45),thickness=4)
		#	)

		#---------------------------------------------------------------------------------------------
		#Ciclo para recorrer el array de coordenadas de los puntos y pintarlos uno a uno
		# for hand_landmarks in results.multi_hand_landmarks:

			# casting de las coordenadas que son traidas en decimales
			# 
			# se multiplican por el ancho/alto de la imagen
			# x1 = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * width)
			# y1 = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * height)

			# x2 = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * width)
			# y2 = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * height)
			
			# x3 = int(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x * width)
			# y3 = int(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * height)

			# x4 = int(hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x * width)
			# y4 = int(hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y * height)

			# x5 = int(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x * width)
			# y5 = int(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y * height)
	
			# dibujar los puntos de calculados
			# cv2.circle(image, (x1,y1), 3, (255,0,0), 3)
			# cv2.circle(image, (x2,y2), 3, (255,0,0), 3)
			# cv2.circle(image, (x3,y3), 3, (255,0,0), 3)
			# cv2.circle(image, (x4,y4), 3, (255,0,0), 3)
			# cv2.circle(image, (x5,y5), 3, (255,0,0), 3)
	
		#---------------------------------------------------------------------------------------------
		index = [4, 8, 12, 16, 20]
		for hand_landmarks in results.multi_hand_landmarks:
			for (i, points) in enumerate(hand_landmarks.landmark):
				if i in index:
					x = int(points.x * width)
					y = int(points.y * height)
					cv2.circle(image, (x,y), 3, (255,0,0))
	image = cv2.flip(image,1)
	image = cv2.flip(image,1)
cv2.imshow("Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()