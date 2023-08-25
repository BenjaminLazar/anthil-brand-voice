# -*- coding: utf-8 -*-

personas = {'General Practitioner - Emotional' : '''The reader cares most about correctly prescribing for their patients and would like access to dosing information, safety overviews and treatment recommendations. 
            The reader cares about safety topics, and generally wants to understand what risks, if any, there may be for their patients in prescribing new drugs or treatments. 
            The reader is interested in information about how to ensure adherence to treatment plans.
            The reader is interested in access to materials they can share with their patients and their families, such as brochures or other take home material.
            They are very focused on issues related to introducing new treatments to their patients.
            They are less interested in the details, tables, or specific scientific data that might be included in content.
            They are generally not interested in access to scientific research papers.''' ,
            
            'General Practitioner - Financial' : ''' The reader is concerned with the cost of treatment to their patients, and wants to understand what programs may exist to reduce the cost patients must pay. Copay programs or insurance benefit information that they can understand and share with their patients is important to them.
            The reader is interested in access to materials they can share with their patients and their families, such as brochures or other take home material.''',
            
            'Nurse Practitioner' : '''The reader cares most about correctly prescribing for their patients and would like access to dosing information, safety overviews and treatment recommendations.
            The reader cares about understanding the mode of action of drugs, understanding when they are contraindicated, and which comorbidities the drug is indicated for.
            The reader is also interested in take home documents and other material that can help patients to understand their treatment.''',
            
            'Patient' : '''The reader is not a medical professional, and does not necessarily understand complex material. 
            They are very interested in short and to the point pieces of information that can explain more complex concepts.
            They are very interested in understanding what they should do have the best health outcomes in their treatment.
            They want to understand how to take their medicine correctly and safely. 
            They are interested in access to material that can help them understand their condition and how to address it.
            They are interested in knowing what questions they should ask their doctor to better understand their treatment.'''
            }

tov = {'patient advice voice' : '''Collective Tone of Voice Description:
The material across the webpages consistently exudes an informative, supportive, and encouraging tone. The content is designed to educate readers about various aspects of diabetes, from physiological changes to lifestyle management. While the information is presented in a straightforward and educational manner, there's a clear undertone of empathy and understanding. The content aims to empower readers, offering practical advice, guidance, and motivation to help them navigate the challenges of living with diabetes. The tone is both reassuring and motivating, emphasizing the importance of proactive self-care, informed decision-making, and seeking support when needed.

Examples of this Tone of Voice:

"You’ve probably had someone tell you to make exercise part of your life... I’m here to tell you that’s all true."
"If you’ve just been diagnosed with type 2 diabetes, you can expect to live an active and independent life if you correctly manage your disease."
"Understanding the connection between insulin, blood sugar and your average blood sugar levels over time – also known as HbA1c – is important for controlling type 2 diabetes."
"Moving on to insulin treatment can seem like a big step. You may feel frustrated that your previous treatment didn't work or worry that injections will be painful, or at least inconvenient."
"What’s the difference between eating healthy when you have diabetes and eating healthy when you don’t? Not much!"
"Hey sugar... What's your story? If you have diabetes, counting carbs can help control blood glucose. You can start today."
"On the road and feeling fine. Diabetes shouldn’t put a wrench in your travel plans. It just means that a little pre‑planning may be in order."
"It’s important to take care of the emotional side of life with diabetes."
"Deciding to move more is a great start. But the real key is to make your activity plan a regular part of your diabetes management."
"You may not have been active in a while. But you can start now!"
These examples and the collective description encapsulate the supportive, informative, and motivating tone found across the provided webpages.''',

'disease awareness voice' : '''Be Informative: Ensure that your content provides valuable information about the topic at hand. Clearly explain the subject matter, ensuring that readers can easily understand the core message.
Example: "Obesity is a chronic disease that requires long-term management."

Show Empathy and Compassion: Understand the challenges and emotions of the individuals affected by the conditions you're discussing. Address them with care and sensitivity.
Example: "Life changes after being diagnosed with type 2 diabetes. There will be new routines and habits that are important to ensure good health."

Be Forward-looking and Hopeful: Emphasize the ongoing efforts, research, and commitment to improving the situation or condition. Highlight the positive changes and advancements.
Example: "We are committed to driving change for a future where everyone with haemophilia and other rare bleeding disorders can get the treatment they need."

Educate with Clarity: Ensure that the content is not only informative but also easy to understand. Avoid jargon and use simple language to explain complex topics.
Example: "Haemophilia is a rare and serious X-chromosome linked congenital bleeding disorder."

Highlight Dedication and Innovation: Showcase the commitment to research, development, and bringing about positive change. Emphasize the dedication to the cause and the innovative approaches being taken.
Example: "We began pioneering advances in growth hormone therapeutics more than 30 years ago."

When writing in this tone, always prioritize the reader's understanding and well-being. Ensure that the content is both informative and compassionate, highlighting the ongoing efforts to bring about positive change''',

'HCP Website Voice' : '''Tone: Clinical, detailed, and cautionary.

Examples:

"GLP-1 RAs stimulate the body’s own insulin secretion."
"Ozempic acts as a GLP-1 receptor agonist that selectively binds to and activates the GLP-1 receptor, the target for native GLP-1."
"Stimulates insulin secretion lowers fasting and postprandial blood glucose by stimulating insulin secretion in a glucose-dependent manner."
"WARNING: RISK OF THYROID C-CELL TUMORS."
"In rodents, semaglutide causes dose-dependent and treatment-duration-dependent thyroid C-cell tumors at clinically relevant exposures."
The tone of the webpage is primarily clinical, providing detailed information about the mechanism of action of Ozempic®. The content is designed to educate healthcare professionals about the drug's effects, potential risks, and benefits. The cautionary tone is evident in the warnings and safety information, emphasizing the importance of understanding potential side effects and contraindications''',

'Patient Product Site' : '''The tone across both webpages is empathetic, informative, motivational, personal, and supportive. The content is designed to educate visitors about the benefits and precautions of the medications while emphasizing the importance of personal stories and experiences in managing type 2 diabetes.

Examples:

"Once-weekly prescription Ozempic, along with diet and exercise, lowers blood sugar in adults with type 2 diabetes."
"Many people are finding ways to help manage their type 2 diabetes and get their A1C down. Discover their inspiring stories..."
"I want to be a role model for my children and ensure that they know the importance of putting their health first." — Nikki
"Troy is focusing on reinstating his real estate license and planning his wedding with his fiancé, Peter."
"Carolyn is showing her true colors as an impassioned painter."
The combined tone emphasizes both the clinical aspects of the medications and the personal journeys of individuals, creating a balance between medical information and relatable stories.'''
}

import streamlit as st

import openai

OPENAI_API_KEY = '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'
openai.api_key = OPENAI_API_KEY

st.title('Anthill Brand Voice')

with st.form('form text'):
    key_brand = st.selectbox('Select a brand voice', options=list(tov.keys()))
    key_persona = st.selectbox('Select a persona', options=list(personas.keys()))
    notes = st.text_input('Add some optional ekstra instructions or notes', ' ')
    txt = st.text_area('Content to Change', '')
    
    submitted = st.form_submit_button('Change Tone')
    if submitted:
        prompt = f'''
        You will be provided some 'content to change' that you will rewrite in the style and tone of voice that you will be instructed in. Besides this will you also consider a specific persona that the content is aimed at.
        
        The 'content to change', contains a text corpus that you need to modify.
        
        The 'tov instructions', provides instructions on how to change the tone of voice for the content in the 'content to change'.
        
        The 'persona description', describes a target persona's preferences that you should keep in mind when modifying the content.
        
        Do not add or imagine new information that is not included in the content_to_change. However, you may rephrase or change the order of information to fit the style and tone of voice you have learned.
        
        Remember, when creating the new document, the preferences and areas of interest or disinterest of the persona described should influence your response. Consider including topics they find more important before other information in your response. Try to avoid removing a topic from your response document, and if you do so, include a summary of the excluded information in the input document after your response.
        
        Extra notes: {notes}
        
        'tov instructions': {tov[key_brand]}
        
        'persone description': {personas[key_persona]}
        
        'content to change': "{txt}"
        
        
        Your task is to rewrite the 'content to change' in the style and tone of voice described in 'tov instructions', and taking into account the persona described in 'persona_description'.
        '''
        
        response = openai.ChatCompletion.create(
          model="gpt-4",
          messages=[
                {"role": "system", "content": "You are a writing assistant that helps rewrite text for medical companies. You will be provided some 'content to change' that you will rewrite in the style and tone of voice that you will be instructed in. Besides this will you also consider a specific persona that the content is aimed at."},
                {"role": "user", "content": prompt},
            ]
        )
        
        st.write(response['choices'][0]['message']['content'])
