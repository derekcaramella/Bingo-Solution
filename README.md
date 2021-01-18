# Bingo-Solution
## Solve Bingo Blitz through computer vision.


I implemented pytesseract Optical Character Recognition (OCR) that decoded the Bingo board and prompt using Natural Langauge Processing (NLP). I chose Bingo Blitz because the board and gameplay are vexatiously noisy. I utilized Hue, Saturation, & Value (HSV) masking to segment the numbers. Following masking, the standard median blurs, thresholding, dilation, and morphology preprocessed the board for computer vision. The application is built for Window applications utilizing the win32api to move & click with the mouse.

Although the application is exceedingly accurate, I incorporated a Tkinter application to update inconsistencies.

<b>If you look to install this program and run it on your system, you must adjust the screenshot settings to your computer's resolution.</b>

Bingo Blitz is a non-gabbling software that users play bingo. A bingo board is displayed at the beginning of the round then balls routinely appear that the user selects to win the game. This application automates the selection & power-up process through computer vision.
