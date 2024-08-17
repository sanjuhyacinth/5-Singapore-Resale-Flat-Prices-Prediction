# libraries:
import pandas as pd
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import datetime
import pickle

#set up page configuration for streamlit
icon='https://cdn-icons-png.flaticon.com/512/5104/5104599.png'
st.set_page_config(page_title='Singapore Flat Resale',page_icon=icon,initial_sidebar_state='expanded',
                        layout='wide',menu_items={"about":'This streamlit application was developed by Sanju Hyacinth C'})

title_text = '''<h1 style='font-size: 45px;color:#f7941d;text-align: center;'>Singapore Flat Resale Prices</h1>'''
st.markdown(title_text, unsafe_allow_html=True)
st.write('')

#set up the sidebar with optionmenu
selected = option_menu(None,
                       options=["HOME","PREDICTIVE ANALYTICS","ABOUT"],
                       icons=["house-fill","file-bar-graph-fill","info-circle-fill"],
                       default_index=0, orientation="horizontal",
                       styles={"container": {"width": "100%","border": "1px ridge #000000","background-color": "#3fb0ac"},
                                "icon": {"color": "#dddfd4", "font-size": "20px"}})

# User input values for selectbox and encoded for respective features:

class inputs:

    inputs_town = ['ANG MO KIO','BEDOK','BISHAN','BUKIT BATOK','BUKIT MERAH','BUKIT PANJANG','BUKIT TIMAH','CENTRAL AREA',
                   'CHOA CHU KANG','CLEMENTI','GEYLANG','HOUGANG','JURONG EAST','JURONG WEST','KALLANG/WHAMPOA',
                   'LIM CHU KANG','MARINE PARADE','PASIR RIS','PUNGGOL','QUEENSTOWN','SEMBAWANG','SENGKANG',
                   'SERANGOON','TAMPINES','TOA PAYOH','WOODLANDS','YISHUN']
    inputs_flat_type = ['1 ROOM', '2 ROOM','3 ROOM', '4 ROOM', '5 ROOM', 'EXECUTIVE','MULTI GENERATION']
    inputs_month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    inputs_flat_model = ['2-ROOM','3GEN','ADJOINED FLAT', 'APARTMENT' ,'DBSS','IMPROVED' ,'IMPROVED-MAISONETTE', 'MAISONETTE',
                    'MODEL A', 'MODEL A-MAISONETTE','MODEL A2' ,'MULTI GENERATION' ,'NEW GENERATION', 'PREMIUM APARTMENT',
                    'PREMIUM APARTMENT LOFT', 'PREMIUM MAISONETTE','SIMPLIFIED', 'STANDARD','TERRACE','TYPE S1','TYPE S2']
    inputs_storey_range = ['01 TO 03', '01 TO 05', '04 TO 06', '06 TO 10', '07 TO 09', '10 TO 12', '11 TO 15', '13 TO 15', 
                           '16 TO 18', '16 TO 20', '19 TO 21', '21 TO 25', '22 TO 24', '25 TO 27', '26 TO 30', 
                           '28 TO 30', '31 TO 33', '31 TO 35', '34 TO 36', '36 TO 40', '37 TO 39', '40 TO 42', 
                           '43 TO 45', '46 TO 48', '49 TO 51']
    encoded_town={'ANG MO KIO' : 0 ,'BEDOK' : 1,'BISHAN' : 2,'BUKIT BATOK' : 3,'BUKIT MERAH' : 4,'BUKIT PANJANG' : 5,'BUKIT TIMAH' : 6,
        'CENTRAL AREA' : 7,'CHOA CHU KANG' : 8,'CLEMENTI' : 9,'GEYLANG' : 10,'HOUGANG' : 11,'JURONG EAST' : 12,'JURONG WEST' : 13,
        'KALLANG/WHAMPOA' : 14,'LIM CHU KANG' : 15,'MARINE PARADE' : 16,'PASIR RIS' : 17,'PUNGGOL' : 18,'QUEENSTOWN' : 19,
        'SEMBAWANG' : 20,'SENGKANG' : 21,'SERANGOON' : 22,'TAMPINES' : 23,'TOA PAYOH' : 24,'WOODLANDS' : 25,'YISHUN' : 26}
    encoded_flat_type={'1 ROOM': 0,'2 ROOM' : 1,'3 ROOM' : 2,'4 ROOM' : 3,'5 ROOM' : 4,'EXECUTIVE' : 5,'MULTI GENERATION' : 6}
    encoded_month= {"January" : 1,"February" : 2,"March" : 3,"April" : 4,"May" : 5,"June" : 6,"July" : 7,"August" : 8,"September" : 9,
            "October" : 10 ,"November" : 11,"December" : 12}
    encoded_flat_model={'2-ROOM' : 0,'3GEN' : 1,'ADJOINED FLAT' : 2,'APARTMENT' : 3,'DBSS' : 4,'IMPROVED' : 5,'IMPROVED-MAISONETTE' : 6,
                'MAISONETTE' : 7,'MODEL A' : 8,'MODEL A-MAISONETTE' : 9,'MODEL A2': 10,'MULTI GENERATION' : 11,'NEW GENERATION' : 12,
                'PREMIUM APARTMENT' : 13,'PREMIUM APARTMENT LOFT' : 14,'PREMIUM MAISONETTE' : 15,'SIMPLIFIED' : 16,'STANDARD' : 17,
                'TERRACE' : 18,'TYPE S1' : 19,'TYPE S2' : 20}
    encoded_storey_range = {'01 TO 03':0, '01 TO 05':1, '04 TO 06':2, '06 TO 10':3, '07 TO 09':4, '10 TO 12':5, 
                             '11 TO 15':6, '13 TO 15':7, '16 TO 18':8, '16 TO 20':9, '19 TO 21':10, '21 TO 25':11, 
                             '22 TO 24':12, '25 TO 27':13, '26 TO 30':14, '28 TO 30':15, '31 TO 33':16, '31 TO 35':17, 
                             '34 TO 36':18, '36 TO 40':19, '37 TO 39':20, '40 TO 42':21, '43 TO 45':22, '46 TO 48':23, 
                             '49 TO 51':24}
    

if selected == "PREDICTIVE ANALYTICS":
        st.write('')
        st.markdown("<h5 style=color:grey> Provide all the information below to predict the Resale Price of a Flat",unsafe_allow_html=True)
        st.write('')

        # creted form to get the user input 
        with st.form('prediction'):
            col1,col2=st.columns(2)
            with col1:

                user_month=st.selectbox(label='Month',options=inputs.inputs_month,index=None)

                user_town=st.selectbox(label='Town',options=inputs.inputs_town,index=None)

                user_flat_type=st.selectbox(label='Flat Type',options=inputs.inputs_flat_type,index=None)

                user_flat_model=st.selectbox(label='Flat Model',options=inputs.inputs_flat_model,index=None)

                floor_area_sqm=st.number_input(label='Floor area sqm',min_value = 20.0)

                sqm_rate=st.number_input(label='Price Per sqm',min_value = 100.00)

            with col2:

                year=st.text_input(label='year',max_chars=4)

                block=st.text_input(label='Block',max_chars=3)

                lease_commence_date=st.text_input(label='Year of lease commence',max_chars=4)

                remaining_lease=st.number_input(label='Remaining lease year',min_value=0,max_value=99)

                property_holding_age=st.number_input(label='Years Holding',min_value=0,max_value=99)
                storeys = st.selectbox(label='Storey Range',options=inputs.inputs_storey_range,index=None)
                
                st.markdown('<br>', unsafe_allow_html=True)

                button=st.form_submit_button('PREDICT',use_container_width=True)

        if button:
            with st.spinner("Predicting..."):

                #check whether user fill all required fields
                if not all([user_month,user_town,user_flat_type,user_flat_model,floor_area_sqm,sqm_rate,year,block,
                            lease_commence_date,remaining_lease,property_holding_age,storeys]):
                    st.error("Please fill in all required fields.")

                else:
                    #create features from user input 
                    current_year = datetime.datetime.now().year
                    age_of_property = current_year-int(lease_commence_date)


                    Month=inputs.encoded_month[user_month]
                    town=inputs.encoded_town[user_town]
                    flat_type=inputs.encoded_flat_type[user_flat_type]
                    flat_model=inputs.encoded_flat_model[user_flat_model]
                    storey_range =inputs.encoded_storey_range[storeys]
                    

                    floor_area_sqm_sqrt=np.sqrt(floor_area_sqm)
                    remaining_lease_sqrt=np.sqrt(remaining_lease)
                    sqm_rate_sqrt=np.sqrt(sqm_rate)

                    #opened pickle model and predict the resale price with user data
                    with open('RandomForestRegressor.pkl','rb') as files:
                        model=pickle.load(files)
                    
                    user_data=np.array([[Month, town, flat_type, block, flat_model, lease_commence_date, year, storey_range,
                                        property_holding_age, age_of_property, floor_area_sqm_sqrt, 
                                        remaining_lease_sqrt, sqm_rate_sqrt ]])

                    predict=model.predict(user_data)
                    resale_price=(np.exp(predict[0]))

                    #display the predicted selling price 
                    st.subheader(f"Predicted Resale price is: :green[{resale_price:.2f}]")

if selected == "HOME":
    st.write('')
    st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Housing_and_Development_Board_flats_in_Bukit_Panjang%2C_Singapore_-_20130131_%28single-row_panorama%29.jpg/1200px-Housing_and_Development_Board_flats_in_Bukit_Panjang%2C_Singapore_-_20130131_%28single-row_panorama%29.jpg', use_column_width=True)
    c1,c2=st.columns([1,1.5],gap="medium")
    with c2:
            st.write('')
            st.markdown('''<h2 style='font-size: 36px;color:#f7941d;text-align: left;'>What is HDB</h2>''',unsafe_allow_html=True)
            st.markdown(''' ##### The Housing & Development Board (HDB) is Singapore's public housing authority, that plana and developa Singapore's housing estates; building homes and transforming towns to create a quality living environment for all.<br><br> They provide various commercial, recreational, and social amenities in their towns for the residents convenience.''',unsafe_allow_html=True)
            
            st.markdown('''<h3 style='font-size: 20px;color:#3FB0AC;text-align: left;'>More about HDB</h3>''',unsafe_allow_html=True)
            st.link_button("About us", "https://www.hdb.gov.sg/cs/infoweb/about-us/history")
    with c1:  
            st.write(' ')  
            st.write(' ')              
            st.markdown("![Alt Text](https://cdn.dribbble.com/users/330915/screenshots/2311781/maison_banlieue_400.gif)")
    
    st.write('')
    text2 = '''<h1 style='font-size: 38px;color:#f7941d;text-align: center;'>Housing & Development Board (HDB)</h1>'''
    st.markdown(text2, unsafe_allow_html=True)
    st.markdown('''<h4 style='font-size: 18px;color:#dddfd4;text-align: center;'>Let us look at the Mission and Vision of HDB</h4>''',unsafe_allow_html=True)
    c1,c2,c3 =st.columns([1,1.7,1],gap="medium")
    with c1:
        st.markdown('''<h2 style='font-size: 30px;color:#f7941d;text-align: left;'>Mission</h2>''', unsafe_allow_html=True)
        st.markdown('''##### Their **Mission** is to provide affordable, quality housing and a great living environment where communities thrive.''',unsafe_allow_html=True)
    with c2:   
        st.write(' ')
        st.write(' ')      
        st.image("https://www.hdb.gov.sg/cs/infoweb/-/media/HDBContent/Images/CCG/current-corporate-signature-.ashx")
    with c3:
        st.markdown('''<h2 style='font-size: 30px;color:#f7941d;text-align: left;'>Vision</h2>''', unsafe_allow_html=True)
        st.markdown('''##### The **Vision** of Singapore Housing & Development Board is to become an outstanding organisation creating endearing homes all are proud of.''',unsafe_allow_html=True)
    st.write('')
    st.write('')

    text2 = '''<h1 style='font-size: 38px;color:#f7941d;text-align: center;'>Statistics - HDB Resale Flats</h1>'''
    st.markdown(text2, unsafe_allow_html=True)
    c1,c2=st.columns([1.5,2], gap = "large")
    with c1:
        st.write(' ')
        st.image('https://valuechampion-sg.s3.amazonaws.com/wpassets/uploads/2024/04/HDB_price_index_until_Q1_2024.webp',use_column_width=True)
        
    with c2:
        st.markdown('''<h2 style='font-size: 30px;color:#3FB0AC;text-align: left;'>Increase in prices of Resale flats in Singapore</h2>''', unsafe_allow_html=True)
        st.markdown('''
                ##### Property prices in Singapore have always been on the rise due to the limited land space in Singapore, and this includes resale HDB flats.''',unsafe_allow_html=True)
        st.markdown('''
                ##### On average, the price index for resale flats increased by 1.22% over the past four quarters (Q1 2023 – Q4 2023). To illustrate the increase in real prices, the average price of a four-room resale flat in Ang Mo Kio was SGD 458,000 in Q3 2021. In Q3 2023, the average price of a same-sized flat in the same location increased to SGD 538,000. Yes, we’re talking about a SGD 80,000 increase in just two years.''',unsafe_allow_html=True)
        
        st.markdown('''<h4 style='font-size: 20px;color:#f7941d;text-align: left;'>Want to buy Resale flats in Singapore?</h4>''', unsafe_allow_html=True)
        st.link_button('6 things you need to check','https://www.valuechampion.sg/home-loans/buying-a-resale-flat-in-singapore-here-are-six-things-you-need-to-check')

    st.write('')
    text2 = '''<h1 style='font-size: 38px;color:#f7941d;text-align: left;'>More about HDB</h1>'''
    st.markdown(text2, unsafe_allow_html=True)
    c1,c2,c3 = st.columns([1.5,1.5,1.5], gap = "medium")
    with c1:
        st.video("https://youtu.be/ya-pdE-wH-k?si=OCm8hcLov2KGN5zI")
    with c2:
        st.video("https://youtu.be/j5mWJsvXQk4?si=2OdNtka-9HRY5VQc")
    with c3:
        st.video("https://youtu.be/zn60x7VSusU?si=QPfEp-nWCCnFgEOH")

if selected == "ABOUT":
    c1,c2 = st.columns([1,2], gap="medium")
    with c1:
        st.write('')
        text = '''<h4 style='font-size: 28px;color:#f7941d;text-align: left;'>Project Title :</h4>'''
        st.markdown(text, unsafe_allow_html=True)
        st.markdown('''<h4 style='font-size: 28px;color:#f7941d;text-align: left;'>Project Domain :</h4>''',unsafe_allow_html=True)
        st.markdown('''<h4 style='font-size: 28px;color:#f7941d;text-align: left;'>Skills & Technologies :</h4>''',unsafe_allow_html=True)
    with c2:
        st.write('')
        st.write('')
        st.markdown('''<h5 style= 'font-size: 22px;color:#dddfd4;'>Singapore Resale Flat Prices Predicting''',unsafe_allow_html=True)
        st.write('')
        st.markdown('''<h5 style= 'font-size: 22px;color:#dddfd4;'> Real Estate''',unsafe_allow_html=True)
        st.write('')
        st.markdown('''<h5 style= 'font-size: 22px;color:#dddfd4;'> Data Wrangling, EDA, Model Building, Model Deployment''',unsafe_allow_html=True)

    st.write('')
    st.markdown('''<h4 style='font-size: 28px;color:#f7941d;text-align: left;'>Overview </h4>''',unsafe_allow_html=True)
    st.write('')
    c1,c2 = st.columns([2,2], gap = "large")
    with c1:
        st.markdown('''<h5 style= 'font-size: 22px;color:#3FB0AC;'>1️⃣ Extraction and Preprocessing''',unsafe_allow_html=True)
        st.markdown('''  
                    <li>Data Source : Downloaded historical resale flat data from official HDB sources, 
                    covering the period from 1990 to the current date.<br>              
                    <li>Initial Cleaning: Handled missing values, corrected inconsistencies, and ensured the data's integrity. <br>           
                    <li>Feature Engineering: Enhanced the dataset by creating new features and transforming existing ones to
                    better capture the underlying patterns.<br><br>''',unsafe_allow_html=True)
        st.write('')
    with c2:
        st.markdown('''<h5 style= 'font-size: 22px;color:#3FB0AC;'>2️⃣ Exploration and Value Handling ''',unsafe_allow_html=True)
        st.markdown('''
                    <li> Outlier Detection: Identified and handled outliers to ensure the model's robustness. <br>
                    <li> Skewness Correction: Addressed skewed distributions using appropriate transformations. <br>
                    <li> Category Encoding: Encoded categorical features using techniques like Label Encoding to convert 
                    them into numerical formats suitable for machine learning algorithms.''',unsafe_allow_html=True)
    
    st.write('')
    c1,c2 = st.columns([2,2], gap="large")
    with c1:
        st.markdown('''<h5 style= 'font-size: 22px;color:#3FB0AC;'>3️⃣ Model Selection and Training ''',unsafe_allow_html=True)
        st.markdown('''
                    <li> Examined different regression models (e.g., Linear Regression, Random Forest Regressor, etc.) <br>
                    <li> Evaluated performance metrics to choose the best model for predicting resale price. <br>
                    <li> Selected the Random Forest Regressor based on its superior performance in terms of R-squared 
                    and Mean Squared Error metrics.''',unsafe_allow_html=True)
    with c2:
        st.markdown('''<h5 style= 'font-size: 22px;color:#3FB0AC;'>4️⃣ Deployment ''',unsafe_allow_html=True)
        st.markdown('''
                    <li> Model Serialization: Saved the trained models using pickle for later use in the application. <br>
                    <li> Streamlit App: Built an interactive dashboard using Streamlit to allow users to input 
                    relevant features and get predictions on flat resale prices.''',unsafe_allow_html=True)
    st.write('')   
    st.markdown('''<h4 style='font-size: 28px;color:#f7941d;text-align: left;'>Connect with me :</h4>''',unsafe_allow_html=True)
    st.markdown('##### Linkedin: www.linkedin.com/in/sanju-hyacinth/')
    st.markdown('##### GitHub : https://github.com/sanjuhyacinth') 
