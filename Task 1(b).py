pip install demoji
import demoji
demoji.download_codes()
text = "I love playing ⚽ and 🏀!"
converted_text = demoji.replace(text, "")
print(converted_text)
import demoji
demoji.download_codes()
text = "I love playing ⚽ and 🏀!"
converted_text = demoji.replace(text, lambda x: f"[{demoji.replace(x)}]")
print(converted_text)
I love playing [soccer ball] and [basketball]!