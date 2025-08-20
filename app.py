import os

from dotenv import load_dotenv

import streamlit as st
import litellm

load_dotenv()

#Litellm API Key
litellm.api_key = os.getenv("OPENAI_API_KEY")

#Set page title
st.set_page_config(page_title="AI Note Summarizer and Quiz Generator")

#Set the title of the Streamlit app
st.title("AI Note Summarizer and Quiz Generator")

#Creta a text input area for user notes
notes = st.text_area("Paste your notes or lecture content here: ", height = 300)

#Choose a task type: Summarize notes or Generate quiz
task = st.radio("What would you like to do?", ["Summarize Notes", "Generate Quiz"])
#radio buttons are single-choice selection option (looks like multiple choice question)

#If the user clicks the button without pasting any notes
if st.button("Start"):   #if button is pressed
    if notes.strip() == "":
    # .strip checks if user left notes box empty + removes leading spaces and tabs
        st.warning("Please paste some notes first!")
    else:
        #Define the prompt based on selected task
        if task == "Summarize Notes":
            prompt = f"Summarize the following notes in a clear and concise way: \n\n{notes}"
            #  \n\n  starts 2 new lines
            #  {notes} = a placeholder that gets replaced with actual notes from user
        else:
            prompt = f"Generate a quiz with multiple-choice questions based on the following notes: {notes}"

        #  Call Litellm to get response
        try:
            response = litellm.completion(
                model = "gpt-4o",   #what AI model would be used
                messages = [
                    {"role": "system", "content": "You are a helpful assistant."},  #sets tone and personality of AI (system)
                    {"role": "user", "content": prompt}   # your actual request (asking AI to summarize or generate)
                ]
            )

            # Display AI's response
            output = response["choices"][0]["message"]["content"]   #means get the first message the AI sent back and take the actual text it wrote
            st.success("Here is what the AI generated: ")
            st.write(output)
        #  give an error if smth is wrong
        except Exception as e:
            st.error(f"Something went wrong: {e}")
#Make "start" button round and longer
st.markdown(
    """
    <style>
    .stButton > button {
        border-radius: 50px;    
        padding: 0.75em 2em; 
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)




