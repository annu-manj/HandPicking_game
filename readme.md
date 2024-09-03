# OpenCV-Game

The code is designed to create a simple hand-tracking game using OpenCV and MediaPipe. In this game, a player uses their hand (specifically the index finger) to touch a moving target (a green circle, referred to as the "enemy") on the screen. When the player touches the enemy, it disappears and reappears at a new random location, and the player’s score increases.

**OpenCV:** Used for capturing video input from the webcam, processing image frames, and displaying the game interface.  
**MediaPipe:** A machine learning framework by Google, used here for detecting and tracking hand landmarks in the video feed.  
**Numpy:** Utilized for calculating distances between the tracked hand landmarks and the on-screen target.    

![image](/image/imag1.png)
![image](/image/imag2.png)
![image](/image/imag3.png)




