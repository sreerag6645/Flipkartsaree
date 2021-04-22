 
from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np
model = load_model('flipkart')






def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    return predictions

def run():
    from PIL import Image
    image = Image.open('saree main.jpg')
    image_office = Image.open('saree side.jpg')
    st.image(image,use_column_width=True)
    add_selectbox = st.sidebar.selectbox(
    "How would you like to predict?",
    ("Online", "Batch"))
    st.sidebar.info('This app is created to predict OFFER of sarees ')
    st.sidebar.success('https://www.pycaret.org')
    st.sidebar.image(image_office)
    st.title("Predicting OFFER of sarees")
    if add_selectbox == 'Online':
        ProdBrand  = st.selectbox('ProdBrand ', ['Anand Sarees',	'Vimalnath Synthetics','Saara','Kuki', 'Divastri' ,'Other values'])
        Brand  = st.selectbox('Brand ', ['Anand','Vimalnath', 'Saara','Kuki', 'Divastri', 'Other values'])
        Color = st.selectbox('Color', ['Multicolor','Pink','Blue','Red','DarkBlue','Other values'])
        Fashion  = st.selectbox('Fashion ', ['Printed','SelfDesign','Woven','Embroidered','FloralPrint','Other values' ])
        Type  = st.selectbox('Type ', ['PolySilk','CottonSilk','Georgette','PolyGeorgette','ArtSilk','Other values'])
        Trendplace = st.selectbox('Trendplace', ['Kanjivaram','Banarasi','Bollywood','Kalamkari','Mysore','Other values' ])
        Product1 = st.selectbox('Product1 ', ['Self Design','Printed','Printed Kalamkari Cotton Blend','Printed Georgette','Woven Banarasi Blend','Other values'])
       
        RetailPrice=st.number_input('RetailPrice' , min_value=899, max_value=	9199, value=899)
        Rating =st.number_input('Rating ',min_value=0, max_value=5, value=1)
        discount  =st.number_input('discount', min_value=0, max_value=2, value=0)
        Product_DiscountPrice=st.number_input('Product_Discou ', min_value=269, max_value=1899, value=269)
        
        
        output=""
        input_dict={'ProdBrand':ProdBrand, 'Brand':Brand,'Color':Color,'Fashion':Fashion, 'Type':Type,
       'RetailPrice':RetailPrice, 'Rating':Rating,'discount':discount,
        'Product_DiscountPrice':Product_DiscountPrice, 'Trendplace':Trendplace, 'Product1':Product1}
        input_df = pd.DataFrame([input_dict])
        if st.button(" PREDICT OFFER"):
            output = predict(model=model, input_df=input_df)
            output = str(output)
            if output == '0' :
              output="YOU WILL GET ABOVE 75% OFFER"
            else:
              output="YOU WILL GET 75 AND LESSER PERCENT OFFER"
        st.success('The Prediction   --  {}'.format(output))
       
    if add_selectbox == 'Batch':
        file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])
        if file_upload is not None:
            data = pd.read_csv(file_upload)            
            predictions = predict_model(estimator=model,data=data)
            st.write(predictions)
def main():
    run()

if __name__ == "__main__":
  main()
