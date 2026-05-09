# Import python packages.
import streamlit as st

# Write directly to the app.
#st.title(f"Example Streamlit App :balloon: {st.__version__}")
st.write(
  """Replace this example with your own code!
  **And if you're new to Streamlit,** check
  out our easy-to-follow guides at
  [docs.streamlit.io](https://docs.streamlit.io).
  """
)

st.markdown("""
- :page_with_curl: [Streamlit open source documentation](https://docs.streamlit.io)
- :snowflake: [Streamlit in Snowflake documentation](https://docs.snowflake.com/en/developer-guide/streamlit/about-streamlit)
- :snowboarder: [Snowpark Session documentation](https://docs.snowflake.com/en/developer-guide/snowpark/reference/python/latest/snowpark/session)
- :books: [Demo repo with templates](https://github.com/Snowflake-Labs/snowflake-demo-streamlit)
- :memo: [Streamlit in Snowflake release notes](https://docs.snowflake.com/en/release-notes/streamlit-in-snowflake)
""")

import streamlit as st
from snowflake.snowpark.functions import col

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


    
