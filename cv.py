import streamlit as st


st.set_page_config(page_title='Ignacia Taré - CV', 
                page_icon='💥', 
                layout="centered", 
                initial_sidebar_state="expanded", 
                menu_items=None)

#add_logo("teo.png")

#############################################################

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

####################################################################################
############################## SIDEBAR #############################################
####################################################################################

st.sidebar.title('Currículum de auto-atención')
st.sidebar.write('Puedes elegir los elementos que quieras ver, solo haz click')

st.sidebar.title('En español')
contacto = st.sidebar.checkbox('Contacto')
destrezas = st.sidebar.checkbox('Destrezas Técnicas')
librerias = st.sidebar.checkbox('Librerías de Python')    
profesional = st.sidebar.checkbox('Experiencia profesional')
estudios = st.sidebar.checkbox('Estudios')
extras = st.sidebar.checkbox('Estudios complementarios')
previa = st.sidebar.checkbox('Vida laboral previa')


st.sidebar.title('In english')
contact = st.sidebar.checkbox('Contact')
skills = st.sidebar.checkbox('Skills')
libraries = st.sidebar.checkbox('Libraries')    
professional = st.sidebar.checkbox('Professional Experience')
education = st.sidebar.checkbox('Education')
extra = st.sidebar.checkbox('Additional learning')
previous = st.sidebar.checkbox('Previous Work Life')

####################################################################################
####################################################################################


tabs1, tabs2 = st.tabs(['Español', 'English'])


with tabs1:
    col01, col02, col03 = st.columns([1,8,1], gap='medium')
    with col02:
        st.title('👩🏼‍💻 Ignacia Taré Albornoz')
        st.subheader('Presentación')
    col1, col2 = st.columns([1,1], gap='small') 
    with col1:   
        st.image('yo.jpg', use_column_width='auto')
        st.caption('''Uno de mis lugares favoritos para trabajar.
                    Foto por Rodrigo Salinas.''')
    with col2:    
        st.write("""
            Hola, mi nombre es Ignacia y soy una científica de datos con especial preocupación en las comunicaciones, y un gusto innato por hacer visualizaciones de información.
            Vivo entre Llay-Llay y Santiago 🇨🇱.\n 
            Me interesa lo que los datos tienen para comunicar y los entendimientos que podemos sacar de estos.
            Trabajé trece años en periodismo y hace cuatro pasé de escribir noticias a escribir código. Mi principal y favortito lenguaje es **Python**, pero también me manejo muy bien en **HTML + CSS**, en **SQL**, y con **JavaScript**. 
            En mi corta carrera en programación he enfrentado complicado código escrito por otros; así como también disfruto escribir programas desde cero. \n 
            Si quieres ver mi currículum, en el sidebar puedes seleccionar las áreas que desees que se muestren. 
        """)

    st.markdown('---') 

if contacto:
    st.subheader('Contacto:')
    st.markdown('''    
        📱 +56 9 9586 5669 \n
        💌 ignaciaescribe@gmail.com \n
        🏡 Doctor Johow 250, Ñuñoa. \n
        💻 https://www.linkedin.com/in/ignaciatare/ \n
        🐱 https://github.com/ignaciatare/ \n
        🎙 http://maula.libsyn.com
    ''')

####################################################################################

col1, col2, col3, col4 = st.columns([1,4,4,1], gap='medium')

if destrezas:
    with col2:
        st.markdown("""
        ### Destrezas técnicas
        - Python 
        - SQL 
        - HTML + CSS  
        - JavaScript 
        - Git y Github 
        - Bash
        - Office 
        - Edición de audio y video
        - Inglés avanzado
        - Administración Linux
        - Administración Windows    
        """)
if librerias:
    with col3:
        st.markdown("""
        ### Librerías
        - pandas 
        - streamlit 
        - selenium
        - matplotlib
        - plotly
        - seaborn
        - numpy
        - geopandas
        """)
    st.markdown('---')


if profesional:
    with st.container():
        st.subheader('Experiencia Profesional')
        col1, col2 = st.columns([1,2], gap='medium')
        with col1:
            st.markdown("""
            **Banco BICE**  
            Científica de datos  
            2022  
            PRÁCTICA PROFESIONAL  
            """)


        with col2:
            st.markdown("""
            - Práctica profesional de 3 meses
            - Uso de Python y SQL para diferentes propósitos
            - Visualizaciones de data con Streamlit
            """)


        with st.container():
            col1, col2 = st.columns([1,2], gap='medium')
            with col1:
                    st.markdown("""
                    **Ministerio de Salud**  
                    Gobierno de Chile 
                    Programadora, ciencia de datos,  
                    2021 
                    (Intervención de tres meses)
                """)

            with col2:
                st.markdown("""
                    - En conjunto con el Ministerio de la Ciencia, Tecnología, Conocimiento e Innovación.
                    - A cargo del repositorio Covid-19, publicado a diario en GitHub
                    - Creación de programas para automatizaciones en el repositorio
                    - Uso de Python para programas, manejo avanzado de GIT y GitHub
                """)

        st.markdown('---')

####################################################################################

if estudios:
    with st.container():
        st.subheader('Estudios')

        col1, col2 = st.columns([1,2], gap='medium')
        with col1:
            st.markdown("""
            **Instituto Profesional INACAP**  
            Analista Programador   
            2019 - a la fecha 
            """)

        with col2:
            st.markdown("""
            - Práctica de múltiples lenguajes (Java, JavaScript, SQL, html, CSS).
            - Desarrollo de estrategias para soluciones de software ágil y robusto.
            - Actitud proactiva, innovadora, colaborativa.
            """)

    with st.container():
        col1, col2 = st.columns([1,2], gap='medium')
        with col1:
            st.markdown("""
            **UNIVERSIDAD DE CHILE**  
            Periodismo  
            2009-2011 
            """)

        with col2:
            st.markdown("""
            - Creación de contenido atrapante en variedad de formatos.
            - Habilidades en lecto-escritura y también en audiovisual.
            - Comunicación efectiva e inclusiva.
            """)

    with st.container():
        col1, col2 = st.columns([1,2], gap='medium')
        with col1:
            st.markdown("""
            **UNIVERSIDAD DE CHILE**  
            Diseño Gráfico  
            2004-2006 
            """)

        with col2:
            st.markdown("""
            - Supervisión de la eficacia de las estrategias publicitarias 
            - Participación en el equipo creativos y dinámicos.
            - Desarrollo del ojo crítico y detección rápida de tendencias.
            """)
####################################################################################
if extras:
    st.markdown('---')
    st.subheader('Formación adicional')

    with st.container():
        col1, col2 = st.columns([1,2], gap='medium')
        with col1:
            st.markdown("""
                    **Escuelita chilota de ciencia de datos** 
                    Ciencia de datos  
                    2020 - a la fecha
            """)

        with col2:
            st.markdown("""
                    **Proyectos**: Scraping de la web del Servel para analizar la votación femenina en Chile, visualización de los datos con geo-referencia, procesador de lenguaje en español que detecta las palabras repetidas en un texto, scraping de aduanas internacionales recogiendo información sobre exportación de vinos, análisis de datos filtrados en Facebook, visualización de datos covid-19.  

            """)
if previa:
    st.markdown('---')
    with st.container():
            st.subheader('Vida Laboral Previa')
            st.markdown("""
                    Previo a mi giro hacia la programación, trabajé trece años como periodista en medios de prensa (LUN y MEGA, entre otros).  Escribí desde noticias hasta diálogos para teleseries.. Ahí, con intensos deadlines, aprendí a trabajar sola y en equipo de manera asertiva, equilibrando agilidad y atención al detalle.
                    """)
            st.markdown('---')
    st.markdown('---')
    st.caption('Esta página fue hecha con un 94% de Python y un 6% de CSS')
####################################################################################








####################################################################################
############################## EN INGLÉS ###########################################
####################################################################################

with tabs2:
   
    with tabs2:
        col01, col02, col03 = st.columns([1,8,1], gap='medium')
        with col02:
            st.title('👩🏼‍💻 Ignacia Taré Albornoz')
            st.subheader('Presentation')
        col1, col2 = st.columns([1,1], gap='small') 
        with col1:   
            st.image('yo.jpg', use_column_width='auto')
            st.caption('''This is my mother's backyard, a place where I love to work .
                        Portrait by Rodrigo Salinas.''')
        with col2:    
            st.write("""
                Hello, my name is Ignacia and I am a data scientist with a special concern in communications, and an innate taste for making information visualizations. I live between Llay-Llay and Santiago 🇨🇱. \n
                I am interested in what data has to communicate and the insights we can draw from it.
                I worked thirteen years in journalism and four years ago I went from writing news to writing code. My main and favorite language is Python, but I'm also very good with HTML + CSS, SQL, and JavaScript. 
                In my short programming career I've faced complicated code written by others; I also enjoy writing programs from scratch. \n
                If you want to see my resume, in the sidebar you can select the areas you want to be shown. 
            """)

    st.markdown('---') 

if contact:
    st.subheader('Contacto:')
    st.markdown('''
        📱 +56 9 9586 5669 \n
        💌 ignaciaescribe@gmail.com \n
        🏡 Doctor Johow 250, Ñuñoa. \n
        💻 https://www.linkedin.com/in/ignaciatare/ \n
        🐱 https://github.com/ignaciatare/ \n
        🎙 http://maula.libsyn.com
    ''')

####################################################################################

col1, col2, col3, col4 = st.columns([1,4,4,1], gap='medium')

if skills:
    with col2:
        st.markdown("""
        ### Skills
        - Python 
        - SQL 
        - HTML + CSS  
        - JavaScript 
        - Git & Github 
        - Bash
        - Office 
        - Audio and video editing
        - Advanced English
        - Administración Linux
        - Administración Windows    
        """)
if libraries:
    with col3:
        st.markdown("""
        ### Libraries
        - pandas 
        - streamlit 
        - selenium
        - matplotlib
        - plotly
        - seaborn
        - numpy
        - geopandas
        """)
    st.markdown('---')


if professional:
    with st.container():
        st.subheader('Professional Experience')
        col1, col2 = st.columns([1,2], gap='medium')
        with col1:
            st.markdown("""
            **Banco BICE**  
            Data Scientist  
            2022  
            PROFESSIONAL PRACTICE  
            """)


        with col2:
            st.markdown("""
            - Professional internship of 3 months, mandatory to obtain the title of Programmer Analyst.
            - Use of Python and SQL for different purposes
            - Big Data visualizations with Streamlit
            """)


        with st.container():
            col1, col2 = st.columns([1,2], gap='medium')
            with col1:
                    st.markdown("""
                    **Ministry of Health**  
                    Government of Chile 
                    Programmer, data scientist  
                    2021 
                    (Three-month intervention)
                """)

            with col2:
                st.markdown("""
                    - In conjunction with the Ministry of Science, Technology, Knowledge and Innovation.
                    - In charge of the Covid-19 repository, published daily on GitHub.
                    - Creation of scripts for automations in the repository.
                    - Use of Python for scripts, advanced handling of GIT and GitHub.
                """)

        st.markdown('---')

####################################################################################

if education:
    with st.container():
        st.subheader('Education')

        col1, col2 = st.columns([1,2], gap='medium')
        with col1:
            st.markdown("""
            **Professional Institute INACAP**.  
            Programmer Analyst   
            2019 - to date 
            """)

        with col2:
            st.markdown("""
            - Practice of multiple languages (Java, JavaScript, SQL, html, CSS).
            - Development of strategies for agile and robust software solutions.
            - Proactive, innovative, collaborative attitude.
            """)

    with st.container():
        col1, col2 = st.columns([1,2], gap='medium')
        with col1:
            st.markdown("""
            **UNIVERSITY OF CHILE**  
            Journalism  
            2009-2011 
            """)

        with col2:
            st.markdown("""
            - Creation of engaging content in a variety of formats.
            - Reading and writing skills as well as audiovisual skills.
            - Effective and inclusive communication.
            """)

    with st.container():
        col1, col2 = st.columns([1,2], gap='medium')
        with col1:
            st.markdown("""
            **UNIVERSITY OF CHILE**  
            Graphic Design  
            2004-2006 
            """)

        with col2:
            st.markdown("""
            - Monitoring the effectiveness of advertising strategies. 
            - Participation in the creative and dynamic team.
            - Development of the critical eye and quick detection of trends.
            """)
####################################################################################
if extra:
    st.markdown('---')
    st.subheader('Additional learning')

    with st.container():
        col1, col2 = st.columns([1,2], gap='medium')
        with col1:
            st.markdown("""
                    **Chiloe's Little School for Data Science** 
                    Data Science  
                    2020 - to date
            """)

        with col2:
            st.markdown("""
                    **Projects**: Scraping of the Servel website to analyze female voting in Chile, visualization of geo-referenced data, Spanish language processor that detects repeated words in a text, scraping of international customs collecting information on wine exports, analysis of filtered Facebook data, visualization of covid-19 data.  
            """)
if previous:
    st.markdown('---')
    with st.container():
            st.subheader('Previous Work Life')
            st.markdown("""
            Before turning to programming and data science, I worked for thirteen years as a journalist in the media (LUN and MEGA, among others).  I wrote everything from news to dialogues for TV series. There, with intense deadlines, I learned to work alone and in a team in an assertive way, balancing agility and attention to detail.
                    """)
            st.markdown('---')
    st.markdown('---')
    st.caption('This page was made with 94% Python and 6% CSS.')
            
            ####################################################################################




