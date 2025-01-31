import asyncio
import pandas as pd
from playwright.async_api import async_playwright

async def run(playwright):
    # Lire le fichier Excel
    df = pd.read_excel('votre_fichier.xlsx')
    print(df)

    browser = await playwright.chromium.launch()
    page = await browser.new_page()
    await page.goto('https://example.com')
    print(await page.title())
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())
