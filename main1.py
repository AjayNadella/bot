import os
import asyncio
import pyautogui
import pytesseract
from telegram import Bot
import keyboard
from UI import save_chat_id
from chains import AutomatedSolver
import pydantic
import pydantic_core
import pydantic.deprecated
import pydantic.v1


CONFIG_FILE = 'config.txt'
telegram_token = "7624886562:AAFfb-agblcBwm80g-N4OOLt28isVevFWFY"

import os, sys

# Get the correct runtime directory explicitly
runtime_dir = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.path.dirname(__file__)
CONFIG_FILE = os.path.join(runtime_dir, 'config.txt')

if not os.path.exists(CONFIG_FILE):
    from UI import prompt_for_chat_id
    prompt_for_chat_id()
    sys.exit()

# Load user's chat_id explicitly from config file
with open(CONFIG_FILE, 'r') as file:
    chat_id = int(file.read().split('=')[1].strip())

bot = Bot(token=telegram_token)

# Capture text from user's screen
def capture_text_from_screen():
    screenshot = pyautogui.screenshot()
    return pytesseract.image_to_string(screenshot).strip()

# Send solution via Telegram
async def send_solution(solution):
    await bot.send_message(chat_id=chat_id, text=solution)
    print("✅ Solution sent via Telegram.")

# Solve question using your AutomatedSolver
async def solve_question():
    solver = AutomatedSolver()
    screen_text = capture_text_from_screen()
    solution = solver.generate_solution(screen_text)
    await send_solution(solution)

# Listen for shortcut key to trigger solving
async def main_loop():
    print("🚀 Application running, press Ctrl+Shift+S to solve.")
    while True:
        await asyncio.to_thread(keyboard.wait, 'ctrl+shift+s')
        print("🔍 Shortcut pressed, solving now...")
        await solve_question()

# Main entry point
if __name__ == "__main__":
    asyncio.run(main_loop())
