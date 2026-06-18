import streamlit as st



#----------------------------------------------------SIDEBAR
st.sidebar.title('calculadora imc')
st.sidebar.image('logo.png')





#----------------------------------------------------BODY
st.title('calculadora imc')


peso = st.text_input("digite o seu peso: ")
altura = st.text_input("digite a sua altura: ")

if st.button('calcular'):
    peso = float(peso)
    altura = float(altura)


    imc = peso / (altura ** 2)


    if imc < 18.5:
        class_imc = "abaixo do peso"
        st.warning(f'seu IMC é {imc:.2f}! voce esta abaixo do peso 🧟‍♀️')


    elif imc < 24.9:
        class_imc = "peso_saudavel"
        st.success((f'seu IMC é {imc:.2f}! voce esta com peso saudavel 👌'))


    elif imc < 29.9:
        class_imc = "sobrepeso"
        st.warning(f'seu IMC é {imc:.2f}! voce esta com sobrepeso 😥')

    elif imc < 34.9:
        class_imc = "obesidade1"
        st.warning(f'seu IMC é {imc:.2f}! voce esta obesidade grau 1 😧')

    elif imc < 39.9:
        class_imc = "obesidade2"
        st.error(f'seu IMC é {imc:.2f}! voce esta obesidade grau 2 😱')

    else:
        class_imc = "obesidade3"
        st.error(f'seu IMC é {imc:.2f}! voce esta obesidade gra 3 😵')


    st.markdown('---')
    st.image(f'{class_imc}.png')



    with open(f'{class_imc}.txt', 'r' , encoding='utf-8') as f:
        texto = f.read()

    st.markdown(texto)
        
