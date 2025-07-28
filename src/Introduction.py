from PIL import Image
image = Image.open('./common/BAUER_ohneSchriftzug_Logo_png.png')

def introduction_page(st):
    """ Introduction Page
    """
    cols = st.columns(1)
    st.image(image, width = 200, use_column_width = False, output_format = 'auto')
    st.title('Willkommen bei Bauer inhouse webtools Menü')
    st.subheader('Please select one of the forms on the left / Bitte wählen Sie das gewünschte Tool aus dem Scrolldown-Menü auf der linken Seite. ')
