from googletrans import Translator


async def tarjimon(text, lang):
    translator = Translator()
    natija = await translator.translate(text=text, dest=lang)
    return natija.text