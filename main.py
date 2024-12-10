import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Date 💌",
    page_icon="💖",
    layout="centered",
)

# Estilo romântico com CSS
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #ffcccb;
        color: #6a1b9a;
        border: none;
        border-radius: 12px;
        padding: 8px 16px;
        font-size: 18px;
    }
    .stButton>button:hover {
        background-color: #ffb6c1;
        color: #4a0072;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
def play_music():
    st.markdown(
        """
        <audio autoplay>
            <source src="https://soundcloud.com/gmzfdnn/george-michael-careless" type="audio/mpeg">
            Seu navegador não suporta o elemento de áudio.
        </audio>
        """,
        unsafe_allow_html=True,
    )
# Cabeçalho
st.title("🌹 Um Pedido Especial 🌹")
st.markdown(
    """
    **Tenho algo muito especial para te perguntar...**  
    Por favor, responda com o sinceridade. 💖
    """
)

# Modal simulado
if "show_modal" not in st.session_state:
    st.session_state.show_modal = False

def open_modal():
    st.session_state.show_modal = True

def close_modal():
    st.session_state.show_modal = False

# Botão para abrir o modal
if st.button("💌 Abrir Pedido"):
    open_modal()

# Conteúdo do modal
if st.session_state.show_modal:
    st.markdown(
        """
        <div style="background-color: #ffe4e1; padding: 20px; border-radius: 12px; text-align: center;">
            <h2 style="color: #d81b60;">🌟 Você aceita sair comigo? 🌟</h2>
            <p style="font-size: 18px;">Prometo que será uma experiência inesquecível. 💕</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("💘 Sim"):
            st.balloons()
            play_music()
            st.success("Que felicidade! ❤️ Vou preparar tudo com carinho.")
            st.image("633db081d79e7.webp", caption="💖", use_column_width=True)
            close_modal()
    with col2:
        if st.button("💔 Não"):
            st.snow()
            st.warning("Tudo bem, eu entendo... 😢")
            close_modal()

# Rodapé romântico
st.markdown(
    """
    ---
    **💖 by Pedro 💖**  
    """
)
