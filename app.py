import cv2
import mediapipe as mp
import streamlit as st
from streamlit_webrtc import webrtc_streamer
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# st.write("This application detects your body poses in real-time and provides guidance for your workouts.")


# Title
st.markdown("<h1 class='title'>Real-Time Gym Trainer</h1>", unsafe_allow_html=True)

# Description
st.markdown("<p class='description'>Here's your real-time gym trainer! It detects your body poses and helps you with your workout form.</p>", unsafe_allow_html=True)


# Placeholder for displaying the video feed
placeholder = st.empty()
# Setup mediapipe instance
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# cap = cv2.VideoCapture(0)

st.markdown(
    """
    <style>
        .reportview-container .main .block-container {
            max-width: 1200px;
            padding-top: 2rem;
            padding-right: 2rem;
            padding-left: 2rem;
            padding-bottom: 2rem;
        }
        .reportview-container .main {
            color: #333;
            background-color: #f9f9f9;
        }
        .reportview-container .stButton>button {
            background-color: #4B0082;
            color: white;
            font-weight: bold;
            border-radius: 5px;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .reportview-container .stButton>button:hover {
            background-color: #6A5ACD;
        }
        .reportview-container .stButton>button:active {
            background-color: #483D8B;
        }
        .camera-button {
            display: flex;
            justify-content: center;
            margin-top: 1rem;
        }
        .camera-button button {
            background-color: #4B0082;
            color: white;
            font-weight: bold;
            border-radius: 5px;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .camera-button button:hover {
            background-color: #6A5ACD;
        }
        .camera-button button:active {
            background-color: #483D8B;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Expander for additional options
# with st.("Additional Options"):
#     st.write("You can add more features here!")

# Main content
st.markdown("---")
st.markdown("<h2 style='text-align: center; color: #4B0082;'>Real-Time Gym Trainer</h2>", unsafe_allow_html=True)
st.markdown("---")

# Camera button
# st.markdown("<div class='camera-button'><button>Start Camera</button></div>", unsafe_allow_html=True)

# st.markdown("<style>h1{text-align: center; color: #4B0082;}</style>", unsafe_allow_html=True)
# st.markdown("<h1>Real-Time Gym Trainer</h1>", unsafe_allow_html=True)
# st.markdown("---")
# st.markdown("Here's your real-time gym trainer! It detects your body poses and helps you with your workout form.")
# st.markdown("---")
# cap = cv2.VideoCapture(0)
# if st.button("Start Camera"):
#
#     webrtc_streamer(key="example", video_transformer_factory=None, async_transform=False)
#
# # Video capture loop
# while True:
#     # Read frame from webcam
#     ret, frame = cap.read()
#
#     if not ret:
#         break
#
#     # Recolor image to RGB
#     image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     image.flags.writeable = False
#
#     # Make detection
#     results = pose.process(image)
#
#     # Recolor back to BGR
#     image.flags.writeable = True
#     image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#
#     # Render detections
#     mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
#                                mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
#                                mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2))
#
#     # Display the processed frame in the Streamlit app
#     placeholder.image(image, channels='BGR', use_column_width=True)
#
#     # Check if 'q' is pressed to exit the loop
#     # if cv2.waitKey(10) & 0xFF == ord('q'):
#     #     break
#
# cap.release()
# # cv2.destroyAllWindows()
# num_cameras = 0
# s=0
# for i in range(10):
#     cap = cv2.VideoCapture(i)
#     if cap.isOpened():
#         num_cameras += 1
#         s=i
#         cap.release()

def capture_video():
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Make detection
        results = pose.process(image)

        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Render detections
        mp.solutions.drawing_utils.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                                   mp.solutions.drawing_utils.DrawingSpec(color=(245, 117, 66),
                                                                                            thickness=2,
                                                                                            circle_radius=2),
                                                   mp.solutions.drawing_utils.DrawingSpec(color=(245, 66, 230),
                                                                                            thickness=2,
                                                                                            circle_radius=2))

        # Display the processed frame in the Streamlit app
        placeholder.image(image, channels='BGR', use_column_width=True)

        # Check if 'q' is pressed to exit the loop





    cv2.destroyAllWindows()

## Get the number of available cameras

# Webcam selection dropdown

# num_cameras = 0
# s=0
# for i in range(10):
#     cap = cv2.VideoCapture(i)
#     if cap.isOpened():
#         num_cameras += 1
#         s=i
#         cap.release()
webrtc_streamer(key="example", video_transformer_factory=None, async_transform=False)
# Start Camera button
if st.button("Start Camera"):
    capture_video()
if st.button("Start Camera"):
