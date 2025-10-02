import streamlit as st
from ollama import chat
from ollama import ChatResponse
from langchain_ollama import ChatOllama

# Fitness Programme Generator
st.set_page_config(page_title="Fitness Programme Generator", page_icon="💪", layout="centered")

@st.cache_data
def generate_fitness_programme(input_data):
    try:
        # Set system and user inputs
        with open("system_prompt.md", "r") as f:
            trainer_guidelines_md = f.read()

        messages = [
                ("system", f"Adhere to the guidelines outlined in {trainer_guidelines_md}"),
                ("user", f"Create a weekly fitness programme, strictly adhering to the following inputs: {input_data}")
            ]
        
        chat_model = ChatOllama(
            model="llama3.2:1b",
            temperature=0.2,
            num_predict=2000
            )
        
        response = chat_model.invoke(messages)

        return response.content
    except Exception as e:
        return f"An error occurred while generating the programme: {e}"

def get_user_inputs():
    # Set up 
    exercise_level = st.selectbox("Which best describes your experience with exercise?",
                                  ["No experience - have not regularly exercised before",
                                   "Some experience - have regularly exercised, but not always consistently",
                                   "Very experienced - regularly exercise currently"],
                                  index=0)

    training_types = st.multiselect(
        "Which of the following training types have you used previously, if any?",
        [
            "Resistance training (free weights, machines)",
            "Olympic lifting (Clean and Snatch variations)",
            "Powerlifting (Bench Press, Deadlift, Squat)",
            "Cardiovascular training (running, cycling, rowing, etc)",
            "CrossFit (WODs, metabolic conditioning, AMRAP, etc)",
            "Yoga",
            "Pilates",
            "None of the above"
        ]
    )

    interested_training = st.multiselect(
        "What type of training are you interested in?",
        [
            "Resistance training (free weights, machines)",
            "Olympic lifting (Clean and Snatch variations)",
            "Powerlifting (Bench Press, Deadlift, Squat)",
            "Cardiovascular training (running, cycling, rowing, etc)",
            "CrossFit (WODs, metabolic conditioning, AMRAP, etc)",
            "Yoga",
            "Pilates"
        ]
    )

    goals = st.multiselect(
        "What are your goals?",
        [
            "Build muscle",
            "Get stronger",
            "Lose weight/bodyfat",
            "Improve cardiovascular fitness",
            "Improve mobility",
            "Enjoy exercise without a specific goal in mind"
        ]
    )

    session_length = st.selectbox(
        "How long would you like each session to be?",
        ["< 15 minutes", "15-30 minutes", "30-45 minutes", "45-60 minutes", "60-90 minutes", "> 90 minutes"]
    )

    training_location = st.selectbox(
        "Do you want to train in a gym or at home/outside?",
        ["Gym", "At home/outside", "Hybrid - gym and at home/outside sessions"]
    )

    days_per_week = st.slider("How many days per week can you train?", 1, 7, 3)

    return {
        "exercise_level": exercise_level,
        "training_types": training_types,
        "interested_training": interested_training,
        "goals": goals,
        "session_length": session_length,
        "training_location": training_location,
        "days_per_week": days_per_week
    }

def main():
    st.title("💪 Fitness Programme Generator")
    st.write("Create a personalised workout plan\u00b0* based on your goals and experience.")
    st.write("\u00b0*This app does not provide medical advice. Please consult a doctor before starting a new exercise programme.")

    input_data = get_user_inputs()

    if "programme" not in st.session_state:
        st.session_state["programme"] = None

    # Generate programme
    if st.button("Generate Programme"):
        st.subheader("Your Programme:")
        st.session_state["programme"] = generate_fitness_programme(input_data)
        st.write(st.session_state["programme"])
        if st.session_state["programme"] and "error" not in st.session_state["programme"].lower():
            st.success("Programme generated! Stay consistent 💪")
        else:
            st.error(st.session_state["programme"])

    # Download programme
    if st.session_state["programme"]:
        st.download_button(
            label="Download Programme",
            data=st.session_state["programme"],
            on_click="ignore",
            file_name="programme.txt"
        )

if __name__ == "__main__":
    main()

