# ============================
# input for job description
# upload pdf
# pdf to image => processing => google gemini
# prompt template
# ============================

from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import pathlib
import io
import base64
import os
from PIL import Image
import pdf2image
import google.generativeai as ggai


# ggai Configuration 
ggai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_gemini_response(input, pdf_content, prompt):
    model = ggai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # convert the pdf to image
        print("path", os.path.join(pathlib.Path(__name__).parent.resolve(),'/poppler-23.11.0/Library/bin'))
        images = pdf2image.convert_from_bytes(uploaded_file.read(), poppler_path=os.path.join(pathlib.Path(__name__).parent.resolve(),'/poppler-23.11.0/Library/bin'))
        first_page = images[0]

        #Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type" : "image/jpeg",
                "data" : base64.b64encode(img_byte_arr).decode()
            }
        ]

        return pdf_parts
    else:
        raise FileNotFoundError('No File uploaded')
    

## Streamlit app

st.set_page_config(page_title="ATS Resume Expert", page_icon="progress.png")
st.header("Resume Application Tracking System")
input_text = st.text_area(label="Job Description: ", key="input")
uploaded_file = st.file_uploader(label="Upload your Resume(Pdf format)...", type=['pdf'])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

# Create two columns
col1, col2 = st.columns(2)

with col1:
    submit0 = st.button('Job Description Match')
    submit1 = st.button('CV Assessment')
    submit2 = st.button('Keyword Generation')
    submit3 = st.button('CV Feedback')
with col2:
    submit4 = st.button('Tailoring Recommendations')
    submit5 = st.button('Missing Keywords')
    submit6 = st.button('Grammar Check')
    submit7 = st.button('CV Enhancement')

input_prompt0 = """
Analyze the CV and compare it to the provided job description. Assess the level of match between the CV and the job requirements, and provide a percentage or score indicating the degree of compatibility. This will help users gauge how well their CV aligns with the desired qualifications.
"""
input_prompt1 = """
Given a job description and a CV, 
provide an accurate assessment of the CV's compatibility with the job requirements, 
highlighting both strong matches and potential gaps
"""

input_prompt2 = """
Based on the provided job description and CV, 
generate a comprehensive list of keywords and skills that are highly relevant to the job, 
ensuring the CV aligns with the desired qualifications.
"""
input_prompt3 = """
Provide detailed feedback on the CV's structure, 
format, and content, suggesting improvements to optimize its visibility and attractiveness to ATS algorithms and human recruiters
"""
input_prompt4 = """
Offer personalized recommendations for tailoring the CV to enhance its chances of passing through ATS filters, including specific sections to emphasize, 
keywords to incorporate, and formatting strategies to employ
"""
input_prompt5 = """
Identify any keywords or skills that are missing from the CV but are important for the job description. Provide a comprehensive list of these missing keywords to help improve the CV's alignment with the job requirements
"""
input_prompt6 = """
Analyze the CV for grammatical errors and inconsistencies. Highlight and suggest corrections for any grammar or punctuation mistakes, ensuring the CV presents a polished and professional image.
"""
input_prompt7 = """
Offer specific suggestions to enhance the power and impact of the CV. This may include recommendations to strengthen the language, rephrase certain sections, or emphasize accomplishments and achievements to make the CV more compelling and persuasive
"""

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file=uploaded_file)
        response = get_gemini_response(prompt=input_prompt1, pdf_content=pdf_content, input=input_text)
        st.subheader("The Response is :")
        st.write(response)
    else:
        st.write('Please upload the resume(pdf)')

elif submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file=uploaded_file)
        response = get_gemini_response(prompt=input_prompt2, pdf_content=pdf_content, input=input_text)
        st.subheader("The Response is :")
        st.write(response)
    else:
        st.write('Please upload the resume(pdf)')
elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file=uploaded_file)
        response = get_gemini_response(prompt=input_prompt3, pdf_content=pdf_content, input=input_text)
        st.subheader("The Response is :")
        st.write(response)
    else:
        st.write('Please upload the resume(pdf)')
elif submit4:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file=uploaded_file)
        response = get_gemini_response(prompt=input_prompt4, pdf_content=pdf_content, input=input_text)
        st.subheader("The Response is :")
        st.write(response)
    else:
        st.write('Please upload the resume(pdf)')
elif submit5:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file=uploaded_file)
        response = get_gemini_response(prompt=input_prompt5, pdf_content=pdf_content, input=input_text)
        st.subheader("The Response is :")
        st.write(response)
    else:
        st.write('Please upload the resume(pdf)')
elif submit6:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file=uploaded_file)
        response = get_gemini_response(prompt=input_prompt6, pdf_content=pdf_content, input=input_text)
        st.subheader("The Response is :")
        st.write(response)
    else:
        st.write('Please upload the resume(pdf)')
elif submit7:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file=uploaded_file)
        response = get_gemini_response(prompt=input_prompt7, pdf_content=pdf_content, input=input_text)
        st.subheader("The Response is :")
        st.write(response)
    else:
        st.write('Please upload the resume(pdf)')
elif submit0:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file=uploaded_file)
        response = get_gemini_response(prompt=input_prompt0, pdf_content=pdf_content, input=input_text)
        st.subheader("The Response is :")
        st.write(response)
    else:
        st.write('Please upload the resume(pdf)')




st.markdown("""<div style='
    margin-top: 150px;
    border-radius: 8px;
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: space-between;
    align-content: center;
    align-items: center;'>
                        <div style="margin : 5px;">
                            <p style="    font-size: 12px;
    font-style: italic;
    font-weight: lighter;"> By Amchia Mohamed</p>
                        </div>
                        <div style="margin : 5px;">
                            <p style="    font-size: 12px;
    font-style: italic;
    font-weight: lighter;">Powered by google Gemini</p>
                        </div>
            </div>""", unsafe_allow_html=True)
# st.markdown("<span style='background-color: #f8f9fa;'>_**POWERED BY GOOGLE GEMINI**_</span>", unsafe_allow_html=True)


