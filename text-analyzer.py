import streamlit as st
import re

# Streamlit UI Title
st.title("📊 Text Analyzer")

# Text Input
st.write("🔹 Enter a paragraph below and click 'Analyze' to get insights:")
text = st.text_area("Enter text here:", height=150)

# Initialize session state for search & replace
if "search_word" not in st.session_state:
    st.session_state.search_word = ""
if "replace_word" not in st.session_state:
    st.session_state.replace_word = ""
if "modified_text" not in st.session_state:
    st.session_state.modified_text = text  
if "highlighted_text" not in st.session_state:
    st.session_state.highlighted_text = text  

# Search Section
st.markdown("---")
st.subheader("🔎 Search in Text")
search_word = st.text_input("Enter word to search:", st.session_state.search_word)

if st.button("Search"):
    if search_word.strip():
        st.session_state.search_word = search_word  # Save searched word
        if search_word in text:
            st.success(f"✅ Found '{search_word}' in the text.")

           
            highlighted_text = re.sub(
                f"({re.escape(search_word)})",
                r'<span style="background-color: yellow; color: black; font-weight: bold;">\1</span>',
                text,
                flags=re.IGNORECASE,
            )
            st.session_state.highlighted_text = highlighted_text
        else:
            st.error(f"❌ '{search_word}' not found.")
    else:
        st.warning("⚠ Please enter a word to search.")

# Display text with highlights
st.write("✍ **Paragraph with Highlighted Search Word:**")
st.markdown(st.session_state.highlighted_text, unsafe_allow_html=True)

# Replace Section
st.markdown("---")
st.subheader("✏ Replace a Word")
replace_word = st.text_input("Replace with:", st.session_state.replace_word)

if st.button("Replace"):
    if st.session_state.search_word and replace_word.strip():
        if st.session_state.search_word in text:
            st.session_state.replace_word = replace_word
            st.session_state.modified_text = text.replace(st.session_state.search_word, replace_word)
            st.success("✅ Text replaced successfully!")
        else:
            st.warning("⚠ The word you want to replace was not found in the text.")
    else:
        st.warning("⚠ Please enter both a word to search and a replacement word.")

# Show modified text
st.write("✍ **Modified Paragraph:**")
st.success(st.session_state.modified_text)

# Uppercase and Lowercase Conversion
st.markdown("---")
st.subheader("📝 Text Transformations")
col1, col2 = st.columns(2)
with col1:
    st.write("🔠 **Uppercase:**")
    st.code(text.upper())
with col2:
    st.write("🔡 **Lowercase:**")
    st.code(text.lower())


st.markdown("---")
st.subheader("📌 Analysis Results")
word_count = len(text.split())
char_count = len(text)
vowel_count = sum(1 for char in text if char.lower() in 'aeiou')
st.write(f"📖 **Total Words:** `{word_count}`")
st.write(f"🔢 **Total Characters:** `{char_count}`")
st.write(f"🔤 **Total Vowels:** `{vowel_count}`")

# Operators
st.markdown("---")
st.subheader("📊 Additional Insights")
contains_python = "Python" in text
st.write(f"🐍 **Contains 'Python'?** {'✅ Yes' if contains_python else '❌ No'}")

if word_count > 0:
    avg_word_length = char_count / word_count
    st.write(f"📏 **Average Word Length:** `{avg_word_length:.2f}`")
else:
    st.warning("⚠ Please enter a paragraph before analyzing.")
