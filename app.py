import streamlit as st
from gtts import gTTS
import tempfile
import os

# Page Setup
st.set_page_config(page_title="StoryVoice AI - Multi-Character", page_icon="🎙️", layout="centered")

st.title("🎙️ StoryVoice AI Studio")
st.subheader("Multi-Character & Story Voice Generator")

st.markdown("---")

# Language Selection
lang_codes = {
    "मराठी (Marathi)": "mr",
    "हिंदी (Hindi)": "hi",
    "English (India)": "en",
    "English (US)": "en",
    "தமிழ் (Tamil)": "ta",
    "తెలుగు (Telugu)": "te"
}

selected_lang = st.selectbox("🌐 भाषा निवडा (Language):", list(lang_codes.keys()))
lang_code = lang_codes[selected_lang]

st.markdown("### ✍️ कथा किंवा संवाद टाका (Story / Dialogues)")
story_input = st.text_area(
    "येथे तुमचा संवाद किंवा कथा लिहा:",
    height=220,
    placeholder="उदाहरणार्थ:\n[Narrator]: एका गावात एक राजा राहत होता.\n[Raja]: आज आपण काय करणार?\n[Mantri]: महाराज, प्रजेची भेट घेऊया."
)

st.markdown("---")

if st.button("🚀 Generate Multi-Character Audio", type="primary"):
    if not story_input.strip():
        st.warning("⚠️ कृपया आधी कथा किंवा संवाद लिहा!")
    else:
        with st.spinner("✨ मल्टि-कॅरेक्टर ऑडिओ तयार होत आहे..."):
            try:
                lines = story_input.split("\n")
                combined_texts = [line.strip() for line in lines if line.strip()]
                full_text_to_speech = ". ".join(combined_texts)
                
                tts = gTTS(text=full_text_to_speech, lang=lang_code, slow=False)
                
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
                    temp_path = tmp_file.name
                
                tts.save(temp_path)
                
                with open(temp_path, "rb") as f:
                    audio_data = f.read()
                    st.success("🎉 ऑडिओ यशस्वीरित्या तयार झाला!")
                    st.audio(audio_data, format="audio/mp3")
                    st.download_button("📥 पूर्ण MP3 Download करा", audio_data, file_name="storyvoice_output.mp3", mime="audio/mp3")
                
                if os.path.exists(temp_path):
                    os.remove(temp_path)
                    
            except Exception as e:
                st.error(f"एरर आली: {str(e)}")
