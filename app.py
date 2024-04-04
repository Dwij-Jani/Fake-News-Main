import streamlit as st
import pickle
import re
from sklearn.feature_extraction.text import TfidfVectorizer
import string 
import webbrowser
    
vectorization = TfidfVectorizer()

vector_form = pickle.load(open('vector.pkl', 'rb'))
load_model = pickle.load(open('LR.pkl', 'rb'))



def search_news(query):
    search_url = f"https://www.google.com/search?q={query}&tbm=nws"
    webbrowser.open_new_tab(search_url)

def wordopt(text):
    text = text.lower()
    text = re.sub('\[.*?\]','',text)
    text = re.sub("\\W"," ",text)
    text = re.sub('https?://\S+|www\.\S+','',text)
    text = re.sub('<.*?>+','',text)
    text = re.sub('[%s]' %re.escape(string.punctuation),'',text)
    text = re.sub('\n','',text)
    text = re.sub('\w*\d\w*','',text)
    return text

def fake_news(news):
    news=wordopt(news)
    input_data=[news]
    vector_form1=vector_form.transform(input_data)
    prediction = load_model.predict(vector_form1)
    return prediction



if __name__ == '__main__':
    st.title('Fake News Classification app ')
    st.subheader("Input the News content below")
    sentence = st.text_area("Enter your news content here", "",height=200)
    predict_btt = st.button("predict")
    
    if predict_btt:
        if sentence == "":
            st.warning('plz enter proper query')
        else:
            
            prediction_class=fake_news(sentence)
            print(prediction_class)
            if prediction_class == [1]:
                st.success('Reliable')
            else:
                st.warning('Unreliable')
    web_search = st.button("Web Search")
    if web_search:
        if sentence == "":
            st.warning('plz enter proper query')
        else:
            search_news(sentence)
                
            
    