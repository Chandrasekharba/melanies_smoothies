# Import python packages.
import streamlit as st

#write directly to the app
st.title(":cup_with_straw: Customize your Smoothie!")
st.write(
    """Choose the fruits you want in your custom Smoothie!"""
)

import streamlit as st
Name_on_Order= st.text_input('Name on smoothie:')
st.write('The name of the smoothie is', Name_on_Order)

#option= st.selectbox('What is your favirate fruit?',
 #                   ('Banana','Strawberries','Peaches'))
#st.write('your favarite friut is:', option)
from snowflake.snowpark.functions import col
session = get_active_session()
#cnx=   st.connection("Snowflake")
#session=cnx.session
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)
ingredients_list=st.multiselect('Choose upto 5 ingredients:'
                               ,my_dataframe
                                ,max_selections= 5)



if ingredients_list:
 # st.write(ingredients_list)
  #st.text(ingredients_list)
    
  ingredients_string= ''
  
  
  for fruit_chosen in ingredients_list:
      ingredients_string +=fruit_chosen + ' '

  st.write(ingredients_string)
 

  my_insert_stmt = """insert into smoothies.public.orders(ingredients, name_on_order)
                    values ('""" + ingredients_string + """','""" + Name_on_Order + """')""" #st.write(my_insert_stmt)
  #st.stop()
  time_to_insert =st.button('Submit Order')

  if time_to_insert:
    session.sql(my_insert_stmt).collect()
    st.success('Your Smoothie is ordered!', icon="✅")


    
