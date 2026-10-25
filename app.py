from translate import Translator
import streamlit as st

st.set_page_config(
    page_title="Language Translation Tool", page_icon="🌐", layout="centered"
)

st.title("🌐 Language Translation Tool")
st.write(
    "Enter text, choose your source and target languages, and get instant"
    " translations!"
)

# Input text box
text_to_translate = st.text_area(
    "Enter text to translate:", placeholder="Type something here..."
)

# Language mapping
languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
    "Chinese": "zh",
}

col1, col2 = st.columns(2)
with col1:
  source_choice = st.selectbox("Source Language", list(languages.keys()))
with col2:
  target_choice = st.selectbox(
      "Target Language", list(languages.keys()), index=1
  )

src_lang_code = languages[source_choice]
tgt_lang_code = languages[target_choice]

# Translate button
if st.button("Translate Text", type="primary"):
  if text_to_translate.strip() != "":
    try:
      # Initialize translator with provider
      translator = Translator(from_lang=src_lang_code, to_lang=tgt_lang_code)
      translated = translator.translate(text_to_translate)

      st.success("### Translated Output:")
      st.write(translated)
    except Exception as e:
      st.error(f"Translation error: {e}")
  else:
    st.warning("Please enter some text to translate.")