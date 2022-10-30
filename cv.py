import streamlit as st


st.set_page_config(page_title='Ignacia Taré - CV', 
                page_icon='👩🏼‍💻', 
                layout="centered", 
                initial_sidebar_state="auto", 
                menu_items=None)

add_logo("teo.png")

#############################################################

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

tabs1, tabs2 = st.tabs(['Español', 'English'])

with tabs1:
    col01, col02, col03 = st.columns([1,8,1], gap='medium')
    with col02:
        st.title('👩🏼‍💻 Ignacia Taré Albornoz')
        st.subheader('Científica de datos')
    col1, col2 = st.columns([1,1], gap='small') 
    with col1:   
        st.image('profile.png', use_column_width='auto')
    with col2:    
        st.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam consectetur dolor a massa dignissim maximus. Mauris venenatis ante pellentesque massa consectetur, ac ullamcorper erat sodales. Praesent quam lorem, congue a massa vitae, pellentesque finibus mi. Maecenas elementum fringilla eros, ut pretium neque tincidunt ac. Pellentesque porta tincidunt magna, a faucibus libero molestie ac. Fusce ut mattis est, quis blandit orci. Suspendisse potenti.')

    st.markdown('---') 

####################################################################################

    col1, col2, col3, col4 = st.columns([1,4,4,1], gap='medium')
    with col2:
        st.markdown("""
        ### Destrezas técnicas
        - Python 
        - SQL 
        - HTML + CSS  
        - JavaScript 
        - Git y Github 
        - Office 
        - Edición de audio y video
        - Inglés avanzado    
        """)

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
        """)

####################################################################################

    st.markdown('---')
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

    st.markdown('---')
    st.subheader('Formación adicional')

    with st.container():
        col1, col2 = st.columns([1,2], gap='medium')
        with col1:
            st.markdown("""
                    **Escuelita chilota de ciencia de datos** 
                    Ciencia de datos  
                    2019 - a la fecha
            """)

        with col2:
            st.markdown("""
                    **Proyectos**: Scraping de la web del Servel para analizar la votación femenina en Chile, visualización de los datos con geo-referencia, procesador de lenguaje en español que detecta las palabras repetidas en un texto, scraping de aduanas internacionales recogiendo información sobre exportación de vinos, análisis de datos filtrados en Facebook, visualización de datos covid-19.  

            """)

    st.markdown('---')
    with st.container():
            st.subheader('Vida Laboral Previa')
            st.markdown("""
                    Previo a mi giro hacia la programación, trabajé trece años como periodista en medios de prensa (LUN y MEGA, entre otros). Ahí, con intensos deadlines, aprendí a trabajar sola y en equipo de manera asertiva, equilibrando agilidad y atención al detalle.
                    """)

####################################################################################

st.markdown('---')



####################################################################################
############################## EN INGLÉS ###########################################
####################################################################################

with tabs2:
    col01, col02, col03 = st.columns([1,8,1], gap='medium')
    with col02:
        st.title('👩🏼‍💻 Ignacia Karime Taré')
        st.subheader('Data Scientist')
        st.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam consectetur dolor a massa dignissim maximus. Mauris venenatis ante pellentesque massa consectetur, ac ullamcorper erat sodales. Praesent quam lorem, congue a massa vitae, pellentesque finibus mi. Maecenas elementum fringilla eros, ut pretium neque tincidunt ac. Pellentesque porta tincidunt magna, a faucibus libero molestie ac. Fusce ut mattis est, quis blandit orci. Suspendisse potenti.')

    st.markdown('---') 

####################################################################################

    col1, col2 = st.columns([1,1], gap='medium')
    with col1:
            st.markdown("""
            ### Skills
            - Python 
            - SQL 
            - HTML + CSS  
            - JavaScript 
            - Git y Github 
            - Office 
            - Edición de audio y video
            - Inglés avanzado    
            """)

    with col2:
            st.markdown("""
            ### Library
            - pandas 
            - streamlit 
            - selenium
            - matplotlib
            - plotly
            - seaborn
            - numpy
            """)

    ####################################################################################

    st.markdown('---')
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

    with st.container():
            st.subheader('Estudios')

            col1, col2 = st.columns([1,2], gap='medium')
            with col1:
                st.markdown("""
                **Instituto Profesional INACAP**  
                Analista Programador   
                2019-2022 
                EN CURSO 
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

    st.markdown('---')

    with st.container():
            st.subheader('Vida Laboral Previa')
            st.markdown("""
                    Previo a mi giro hacia la programación, trabajé trece años como periodista en medios de prensa (LUN y MEGA, entre otros). Ahí, con intensos deadlines, aprendí a trabajar sola y en equipo de manera asertiva, equilibrando agilidad y atención al detalle.
                    """)

    ####################################################################################

    st.markdown('---')
