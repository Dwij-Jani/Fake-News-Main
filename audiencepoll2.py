import streamlit as st
import pandas as pd
import plotly.express as px

# Load previously submitted data (if any)
@st.cache(allow_output_mutation=True)
def load_data():
    return pd.DataFrame(columns=['Email', 'Vote'])

votes_df = load_data()

def main():
    st.title("Fake News Audience Poll")
    st.write("Please vote as per your predictions")

    # Options for the poll
    options = ["True", "Fake"]

    # Display options and collect vote
    vote = st.radio("Choose your option", options)

    # Get user's email (can be used to identify unique voters)
    email = st.text_input("Enter your email")

    if st.button("Submit Vote"):
        if email.strip() == '':
            st.error("Please enter your email.")
        elif email in votes_df['Email'].values:
            st.error("You have already voted!")
        else:
            votes_df.loc[len(votes_df)] = [email, vote]
            st.success("Vote submitted successfully!")
            # Reset input fields
            st.text_input("Enter your email", value='')
            st.radio("Choose your option", options)

    # Display pie chart
    if not votes_df.empty:
        fig = px.pie(votes_df, names='Vote', title="Prediction according to audience")
        st.plotly_chart(fig, use_container_width=True)

    # Reset button to clear votes
    if st.button("Reset Votes"):
        votes_df.drop(votes_df.index, inplace=True)
        st.success("Votes reset successfully!")

if __name__ == "__main__":
    main()
