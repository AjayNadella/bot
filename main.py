import time
import pyautogui
import pytesseract
from telegram import Bot
from chains import AutomatedSolver
import asyncio
import keyboard

telegram_token = "7624886562:AAFfb-agblcBwm80g-N4OOLt28isVevFWFY"
chat_id = 1080486643
bot = Bot(token=telegram_token)


def capture_text_from_screen():
    screenshot = pyautogui.screenshot()
    text = pytesseract.image_to_string(screenshot)
    return text.strip()


async def send_telegram(solution):
    await bot.send_message(chat_id=chat_id, text=solution)
    print("✅ Sent via Telegram!")


async def solve_question():
    solver = AutomatedSolver()
    screen_text = capture_text_from_screen()
    solution = solver.generate_solution(screen_text)
    await send_telegram(solution)


async def main_loop():
    print("🚦 Waiting for your trigger (Press Ctrl+Shift+S to solve)...")
    while True:
        await asyncio.to_thread(keyboard.wait, 'ctrl+shift+s')
        print("📌 Detected shortcut. Solving now...")
        await solve_question()


if __name__ == "__main__":
    asyncio.run(main_loop())
