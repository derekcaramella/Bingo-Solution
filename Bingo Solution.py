from PIL import ImageGrab
import cv2
import numpy as np
import pytesseract
import win32api
import win32con
from tkinter import *
import re
import imutils


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
bingo_positions = [(615, 255), (715, 255), (815, 255), (915, 255), (1015, 255),
                   (615, 355), (715, 355), (815, 355), (915, 355), (1015, 355),
                   (615, 455), (715, 455), (815, 455), (915, 455), (1015, 455),
                   (615, 555), (715, 555), (815, 555), (915, 555), (1015, 555),
                   (615, 655), (715, 655), (815, 655), (915, 655), (1015, 655),
                   (615, 755), (715, 755), (815, 755), (915, 755), (1015, 755)]
previous_previous_result = ''
previous_result = ''
answer_bool = 0


def get_board():
    global board
    board_img = ImageGrab.grab(bbox=(720, 280, 1300, 850))
    config = '-l eng --oem 1 --psm 12 -c tessedit_char_whitelist=0123456789" "'
    board_img_np = np.array(board_img)
    board_img = cv2.cvtColor(board_img_np, cv2.COLOR_BGR2RGB)
    board_img = cv2.cvtColor(board_img, cv2.COLOR_BGR2RGB)
    board_hsv_img = cv2.cvtColor(board_img, cv2.COLOR_RGB2HSV)
    board_light_black = (320, 500, 80)
    board_dark_black = (0, 0, 0)
    board_mask = cv2.inRange(board_hsv_img, board_dark_black, board_light_black)
    board_mask = cv2.threshold(board_mask, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    board_mask = cv2.medianBlur(board_mask, 5)
    board_mask = cv2.dilate(board_mask, np.ones((7, 7), np.uint8), iterations=1)
    board_mask = cv2.morphologyEx(board_mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    board = str(pytesseract.image_to_string(board_mask, config=config))[:-1]
    board = re.split("\n\n|\n| ", board)


def interpret_prompt():
    config = '-l eng --oem 1 --psm 6 -c tessedit_char_whitelist=0123456789/S'
    prompt_img = ImageGrab.grab(bbox=(650, 90, 720, 130))
    prompt_img_np = np.array(prompt_img)
    prompt_img = cv2.cvtColor(prompt_img_np, cv2.COLOR_BGR2RGB)
    prompt_hsv_img = cv2.cvtColor(prompt_img, cv2.COLOR_RGB2HSV)
    prompt_light_black = (320, 600, 80)
    prompt_dark_black = (0, 0, 0)
    prompt_mask = cv2.inRange(prompt_hsv_img, prompt_dark_black, prompt_light_black)
    prompt_img = cv2.threshold(prompt_mask, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    prompt_img = cv2.medianBlur(prompt_img, 5)
    # prompt_img = cv2.dilate(prompt_img, np.ones((5, 5), np.uint8), iterations=1)
    prompt_img = cv2.morphologyEx(prompt_img, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    prompt_img = imutils.resize(prompt_img, width=500)
    # cv2.imshow(' ', prompt_img)
    # cv2.waitKey(0)
    prompt = (pytesseract.image_to_string(prompt_img, config=config).replace("\n", ""))[:-1]
    if '/' in prompt:
        prompt = prompt.replace('/', '7')
    if 'S' in prompt:
        prompt = prompt.replace('S', '5')
    print(prompt)
    return prompt


def click_answer():
    global previous_result
    global previous_previous_result
    if answer_bool == 1:
        prompt = interpret_prompt()
        if previous_previous_result == previous_result and previous_previous_result != prompt:
            try:
                position = bingo_positions[board.index(prompt)]
                if board.index(prompt) >= 12:
                    position = bingo_positions[board.index(prompt) + 1]
                win32api.SetCursorPos(position)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, position[0], position[1], 0, 0)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, position[0], position[1], 0, 0)
            except:
                print(prompt)
            print(prompt)
        previous_previous_result = previous_result
        previous_result = prompt
    root.after(10, click_answer)


def solve():
    global answer_bool
    get_board()
    board_0_0.insert(0, board[0])
    board_0_1.insert(0, board[1])
    board_0_2.insert(0, board[2])
    board_0_3.insert(0, board[3])
    board_0_4.insert(0, board[4])
    board_1_0.insert(0, board[5])
    board_1_1.insert(0, board[6])
    board_1_2.insert(0, board[7])
    board_1_3.insert(0, board[8])
    board_1_4.insert(0, board[9])
    board_2_0.insert(0, board[10])
    board_2_1.insert(0, board[11])
    board_2_2.insert(0, '')
    board_2_3.insert(0, board[12])
    board_2_4.insert(0, board[13])
    board_3_0.insert(0, board[14])
    board_3_1.insert(0, board[15])
    board_3_2.insert(0, board[16])
    board_3_3.insert(0, board[17])
    board_3_4.insert(0, board[18])
    board_4_0.insert(0, board[19])
    board_4_1.insert(0, board[20])
    board_4_2.insert(0, board[21])
    board_4_3.insert(0, board[22])
    board_4_4.insert(0, board[23])
    answer_bool = 1


def update():
    global board
    board = [board_0_0.get(), board_0_1.get(), board_0_2.get(), board_0_3.get(), board_0_4.get(),
             board_1_0.get(), board_1_1.get(), board_1_2.get(), board_1_3.get(), board_1_4.get(),
             board_2_0.get(), board_2_1.get(), board_2_3.get(), board_2_4.get(),
             board_3_0.get(), board_3_1.get(), board_3_2.get(), board_3_3.get(), board_3_4.get(),
             board_4_0.get(), board_4_1.get(), board_4_2.get(), board_4_3.get(), board_4_4.get()]


font = ('Times New Roman', 30)
pady = 5
padx = 5

root = Tk()
root.title("Bingo Solver")
root.geometry('350x300')

board_0_0 = Entry(root, font=font, width=2)
board_0_0.grid(row=0, column=0, padx=padx, pady=pady)

board_0_1 = Entry(root, font=font, width=2)
board_0_1.grid(row=0, column=1, padx=padx, pady=pady)

board_0_2 = Entry(root, font=font, width=2)
board_0_2.grid(row=0, column=2, padx=padx, pady=pady)

board_0_3 = Entry(root, font=font, width=2)
board_0_3.grid(row=0, column=3, padx=padx, pady=pady)

board_0_4 = Entry(root, font=font, width=2)
board_0_4.grid(row=0, column=4, padx=padx, pady=pady)

board_1_0 = Entry(root, font=font, width=2)
board_1_0.grid(row=1, column=0, padx=padx, pady=pady)

board_1_1 = Entry(root, font=font, width=2)
board_1_1.grid(row=1, column=1, padx=padx, pady=pady)

board_1_2 = Entry(root, font=font, width=2)
board_1_2.grid(row=1, column=2, padx=padx, pady=pady)

board_1_3 = Entry(root, font=font, width=2)
board_1_3.grid(row=1, column=3, padx=padx, pady=pady)

board_1_4 = Entry(root, font=font, width=2)
board_1_4.grid(row=1, column=4, padx=padx, pady=pady)

board_2_0 = Entry(root, font=font, width=2)
board_2_0.grid(row=2, column=0, padx=padx, pady=pady)

board_2_1 = Entry(root, font=font, width=2)
board_2_1.grid(row=2, column=1, padx=padx, pady=pady)

board_2_2 = Entry(root, font=font, width=2)
board_2_2.grid(row=2, column=2, padx=padx, pady=pady)

board_2_3 = Entry(root, font=font, width=2)
board_2_3.grid(row=2, column=3, padx=padx, pady=pady)

board_2_4 = Entry(root, font=font, width=2)
board_2_4.grid(row=2, column=4, padx=padx, pady=pady)

board_3_0 = Entry(root, font=font, width=2)
board_3_0.grid(row=3, column=0, padx=padx, pady=pady)

board_3_1 = Entry(root, font=font, width=2)
board_3_1.grid(row=3, column=1, padx=padx, pady=pady)

board_3_2 = Entry(root, font=font, width=2)
board_3_2.grid(row=3, column=2, padx=padx, pady=pady)

board_3_3 = Entry(root, font=font, width=2)
board_3_3.grid(row=3, column=3, padx=padx, pady=pady)

board_3_4 = Entry(root, font=font, width=2)
board_3_4.grid(row=3, column=4, padx=padx, pady=pady)

board_4_0 = Entry(root, font=font, width=2)
board_4_0.grid(row=4, column=0, padx=padx, pady=pady)

board_4_1 = Entry(root, font=font, width=2)
board_4_1.grid(row=4, column=1, padx=padx, pady=pady)

board_4_2 = Entry(root, font=font, width=2)
board_4_2.grid(row=4, column=2, padx=padx, pady=pady)

board_4_3 = Entry(root, font=font, width=2)
board_4_3.grid(row=4, column=3, padx=padx, pady=pady)

board_4_4 = Entry(root, font=font, width=2)
board_4_4.grid(row=4, column=4, padx=padx, pady=pady)

solve_button = Button(root, text='Solve', command=solve, font=("Times New Roman", 12))
solve_button.grid(row=0, column=5, rowspan=2, padx=10)

update_button = Button(root, text='Update', command=update, font=("Times New Roman", 12))
update_button.grid(row=2, column=5, rowspan=2, padx=10)


root.after(10, click_answer)

root.mainloop()

# state_left = win32api.GetKeyState(0x01)

# bingo_positions = []
# row = 1
# column = 1
# y_axis = 255
# x_axis = 615
# while row <= 5:
#     if column <= 5:
#         bingo_positions.append((x_axis, y_axis))
#         x_axis += 100
#         column += 1
#     else:
#         y_axis += 100
#         x_axis = 615
#         row += 1
#         column = 0
# print(bingo_positions)


# row = 0
# column = 0
# while row <= 5:
#     a = win32api.GetKeyState(0x01)
#     if a != state_left:
#         state_left = a
#         if a < 0:
#             print(str(column) + str(row) + ': ' + str(win32api.GetCursorPos()))
#             column += 1
#             if column > 5:
#                 column = 0
#                 row += 1
#     time.sleep(0.001)
