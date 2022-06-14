from math import ceil
import streamlit as st
import pandas as pd
import numpy as np
import datetime
from dateutil.parser import parse
from streamlit_option_menu import option_menu
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout="wide")


selected = option_menu(
    menu_title = 'Packing House - Projetos',
    options = ['Balanceamento','Previsão de Calibres','Contagem de frutos','Embaladeiras','Meta PH'],
    icons = ['plus-slash-minus','bar-chart-line-fill','camera-video-fill','people-fill','graph-up-arrow'],
    menu_icon = 'box-seam',
    default_index = 0,
    orientation = 'horizontal',
    styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "#f56e00", "font-size": "20px"}, 
            "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#009b36","font-size": "20px"},
        }
)




if selected == 'Balanceamento':


    with open ('style.css') as f:
        st.markdown(f'<style>{f.read()}<style>', unsafe_allow_html=True)

    coluna_inicial_1, coluna_inicial_2 = st.columns([0.8,1])
    with coluna_inicial_1:
        st.title('Packing House - Linhas de Embalagem')


    with coluna_inicial_2:
        st.write('')
        st.write('')
        if st.button('Atualizar Controle'):
            url = 'http://sia:3000/backend/busca_generica/buscaGenerica?view=MGCLI.AGDTI_VW_DX_BALANCEAMENTO_PH'
            url_embaladeiras_ativas = 'http://sia:3000/backend/busca_generica/buscaGenericaMYSQLAvilla?sql=SELECT%20*%20FROM%20avillaconsulto.vw_dx_emb_presentes'
            

            variaveis_df = pd.read_json(url)

            def correcao_(variaveis_df):
                if variaveis_df['VARIEDADE'] == 'TOMMY ATKINS':
                    return 'Tommy Atkins'
                elif variaveis_df['VARIEDADE'] == 'PALMER':
                    return 'Palmer'
                elif variaveis_df['VARIEDADE'] == 'KEITT':
                    return 'Keitt'
                elif variaveis_df['VARIEDADE'] == 'KENT':
                    return 'Kent'
                elif variaveis_df['VARIEDADE'] == 'OMER':
                    return 'Omer'
                else:
                    return 'NADA'

            variaveis_df['VARIEDADE'] = variaveis_df.apply(correcao_, axis = 1)
        


            def calibre(variaveis_df):
                if variaveis_df['VARIEDADE'] == 'Palmer' and (variaveis_df['PESO'] <= 1130 and variaveis_df['PESO'] > 980):
                    return '4'
                elif (variaveis_df['VARIEDADE'] == 'Palmer') and (variaveis_df['PESO'] <= 980 and variaveis_df['PESO'] > 777):
                    return '5'
                elif (variaveis_df['VARIEDADE'] == 'Palmer') and (variaveis_df['PESO'] <= 777 and variaveis_df['PESO'] > 630):
                    return '6'
                elif (variaveis_df['VARIEDADE'] == 'Palmer') and (variaveis_df['PESO'] <= 630 and variaveis_df['PESO'] > 557):
                    return '7'
                elif (variaveis_df['VARIEDADE'] == 'Palmer') and (variaveis_df['PESO'] <= 557 and variaveis_df['PESO'] > 478):
                    return '8'
                elif (variaveis_df['VARIEDADE'] == 'Palmer') and (variaveis_df['PESO'] <= 478 and variaveis_df['PESO'] > 438):
                    return '9'
                elif (variaveis_df['VARIEDADE'] == 'Palmer') and (variaveis_df['PESO'] <= 438 and variaveis_df['PESO'] > 376):
                    return '10'
                elif (variaveis_df['VARIEDADE'] == 'Palmer') and (variaveis_df['PESO'] <= 376 and variaveis_df['PESO'] > 295):
                    return '12'
                elif (variaveis_df['VARIEDADE'] == 'Palmer') and (variaveis_df['PESO'] <= 295 and variaveis_df['PESO'] > 280):
                    return '14'
                elif (variaveis_df['VARIEDADE'] == 'Palmer') and (variaveis_df['PESO'] <= 280):
                    return '0'
                elif (variaveis_df['VARIEDADE'] == 'Palmer') and (variaveis_df['PESO'] > 1130):
                    return '100'
                #################################################### TOMMY ATKINS #####################################################
                elif variaveis_df['VARIEDADE'] == 'Tommy Atkins' and (variaveis_df['PESO'] <= 1200 and variaveis_df['PESO'] > 1000):
                    return '4'
                elif (variaveis_df['VARIEDADE'] == 'Tommy Atkins') and (variaveis_df['PESO'] <= 1000 and variaveis_df['PESO'] > 880):
                    return '5'
                elif (variaveis_df['VARIEDADE'] == 'Tommy Atkins') and (variaveis_df['PESO'] <= 880 and variaveis_df['PESO'] > 640):
                    return '6'
                elif (variaveis_df['VARIEDADE'] == 'Tommy Atkins') and (variaveis_df['PESO'] <= 640 and variaveis_df['PESO'] > 557):
                    return '7'
                elif (variaveis_df['VARIEDADE'] == 'Tommy Atkins') and (variaveis_df['PESO'] <= 557 and variaveis_df['PESO'] > 480):
                    return '8'
                elif (variaveis_df['VARIEDADE'] == 'Tommy Atkins') and (variaveis_df['PESO'] <= 480 and variaveis_df['PESO'] > 442):
                    return '9'
                elif (variaveis_df['VARIEDADE'] == 'Tommy Atkins') and (variaveis_df['PESO'] <= 442 and variaveis_df['PESO'] > 371):
                    return '10'
                elif (variaveis_df['VARIEDADE'] == 'Tommy Atkins') and (variaveis_df['PESO'] <= 371 and variaveis_df['PESO'] > 296):
                    return '12'
                elif (variaveis_df['VARIEDADE'] == 'Tommy Atkins') and (variaveis_df['PESO'] <= 296 and variaveis_df['PESO'] > 279):
                    return '14'
                elif (variaveis_df['VARIEDADE'] == 'Tommy Atkins') and (variaveis_df['PESO'] <= 279):
                    return '0'
                elif (variaveis_df['VARIEDADE'] == 'Tommy Atkins') and (variaveis_df['PESO'] > 1200):
                    return '100'
                    
                #################################################### KEITT #####################################################

                elif (variaveis_df['VARIEDADE'] == 'Keitt' or variaveis_df['VARIEDADE'] == 'Omer') and (variaveis_df['PESO'] <= 1500 and variaveis_df['PESO'] > 880):
                    return '4'
                elif (variaveis_df['VARIEDADE'] == 'Keitt' or variaveis_df['VARIEDADE'] == 'Omer') and (variaveis_df['PESO'] <= 880 and variaveis_df['PESO'] > 770):
                    return '5'
                elif (variaveis_df['VARIEDADE'] == 'Keitt' or variaveis_df['VARIEDADE'] == 'Omer') and (variaveis_df['PESO'] <= 770 and variaveis_df['PESO'] > 622):
                    return '6'
                elif (variaveis_df['VARIEDADE'] == 'Keitt' or variaveis_df['VARIEDADE'] == 'Omer') and (variaveis_df['PESO'] <= 622 and variaveis_df['PESO'] > 553):
                    return '7'
                elif (variaveis_df['VARIEDADE'] == 'Keitt' or variaveis_df['VARIEDADE'] == 'Omer') and (variaveis_df['PESO'] <= 553 and variaveis_df['PESO'] > 476):
                    return '8'
                elif (variaveis_df['VARIEDADE'] == 'Keitt' or variaveis_df['VARIEDADE'] == 'Omer') and (variaveis_df['PESO'] <= 476 and variaveis_df['PESO'] > 439):
                    return '9'
                elif (variaveis_df['VARIEDADE'] == 'Keitt' or variaveis_df['VARIEDADE'] == 'Omer') and (variaveis_df['PESO'] <= 439 and variaveis_df['PESO'] > 385):
                    return '10'
                elif (variaveis_df['VARIEDADE'] == 'Keitt' or variaveis_df['VARIEDADE'] == 'Omer') and (variaveis_df['PESO'] <= 385 and variaveis_df['PESO'] > 305):
                    return '12'
                elif (variaveis_df['VARIEDADE'] == 'Keitt' or variaveis_df['VARIEDADE'] == 'Omer') and (variaveis_df['PESO'] <= 305 and variaveis_df['PESO'] > 279):
                    return '14'
                elif (variaveis_df['VARIEDADE'] == 'Keitt' or variaveis_df['VARIEDADE'] == 'Omer') and (variaveis_df['PESO'] <= 279):
                    return '0'
                elif (variaveis_df['VARIEDADE'] == 'Keitt' or variaveis_df['VARIEDADE'] == 'Omer') and (variaveis_df['PESO'] > 1500):
                    return '100'

                #################################################### KENT #####################################################
                elif variaveis_df['VARIEDADE'] == 'Kent' and (variaveis_df['PESO'] <= 1300 and variaveis_df['PESO'] > 930):
                    return '4'
                elif (variaveis_df['VARIEDADE'] == 'Kent') and (variaveis_df['PESO'] <= 930 and variaveis_df['PESO'] > 760):
                    return '5'
                elif (variaveis_df['VARIEDADE'] == 'Kent') and (variaveis_df['PESO'] <= 760 and variaveis_df['PESO'] > 626):
                    return '6'
                elif (variaveis_df['VARIEDADE'] == 'Kent') and (variaveis_df['PESO'] <= 626 and variaveis_df['PESO'] > 545):
                    return '7'
                elif (variaveis_df['VARIEDADE'] == 'Kent') and (variaveis_df['PESO'] <= 545 and variaveis_df['PESO'] > 476):
                    return '8'
                elif (variaveis_df['VARIEDADE'] == 'Kent') and (variaveis_df['PESO'] <= 476 and variaveis_df['PESO'] > 444):
                    return '9'
                elif (variaveis_df['VARIEDADE'] == 'Kent') and (variaveis_df['PESO'] <= 444 and variaveis_df['PESO'] > 375):
                    return '10'
                elif (variaveis_df['VARIEDADE'] == 'Kent') and (variaveis_df['PESO'] <= 375 and variaveis_df['PESO'] > 303):
                    return '12'
                elif (variaveis_df['VARIEDADE'] == 'Kent') and (variaveis_df['PESO'] <= 303 and variaveis_df['PESO'] > 269):
                    return '14'
                elif (variaveis_df['VARIEDADE'] == 'Kent') and (variaveis_df['PESO'] <= 269):
                    return '0'
                elif (variaveis_df['VARIEDADE'] == 'Kent') and (variaveis_df['PESO'] > 1300):
                    return '100'

            
            variaveis_df['CALIBRE'] = variaveis_df.apply(calibre, axis =1)

            variaveis_df = variaveis_df.drop(columns = ['CONTENTORES'])
            variaveis_df.rename(columns={'TOTAL_CONTENTORES':'CONTENTORES'}, inplace = True)


            dataset = variaveis_df




            controle = dataset['CONTROLE'][0]
            st.session_state.control = controle

            VARIEDADE = dataset['VARIEDADE'][0]
            st.session_state.variety = VARIEDADE




            dataset.rename(columns = {"PESO":"Peso","CALIBRE":"Calibre","NUMERO_FRUTO":"Fruto","QUALIDADE":"Qualidade","VARIEDADE":"Variedade"}, inplace = True)
            try:
                dataset['Calibre'] = dataset['Calibre'].astype(int)
            except TypeError:
                st.write('Error')
            

            a = dataset['Calibre'].value_counts() / dataset['Calibre'].count()

            b = pd.DataFrame(a)
            b = b.reset_index()
            b.columns = ['Calibre', 'Percentual']
            b['Percentual'] = b['Percentual']*100
            b = b.sort_values('Calibre')
            b['Percentual_RECENTE'] = 0
            st.session_state.b_ = b

            st.session_state.anterior = variaveis_df

            df_embaladeiras_ativas = pd.read_json(url_embaladeiras_ativas)

            if len(df_embaladeiras_ativas) == 0:
                url_embaladeiras_ativas = 'http://sia:3000/backend/busca_generica/buscaGenerica?view=MGCLI.AGDTI_VW_DX_EMB_ATIVAS'
                df_embaladeiras_ativas = pd.read_json(url_embaladeiras_ativas)


            df_embaladeiras_ativas.rename(columns = {'CPF':'MATRICULA','PESSOA':'NOME'}, inplace = True)
            
            df_embaladeiras_ativas['NOME'] = df_embaladeiras_ativas['NOME'].str[6:]


            st.session_state.url_embala = df_embaladeiras_ativas

            



            quality = dataset['Qualidade'].value_counts() / dataset['Qualidade'].count()

            quality = pd.DataFrame(quality)
            quality = quality.reset_index()
            quality.columns = ['Qualidade','Percent']
            #quality

            st.session_state.quality_percent = quality
            produtividade_atual = 38
            st.session_state.prod_MAF = produtividade_atual
            
            st.session_state.cxs_recentes = 100000
            
            st.session_state.cxs_process = 0
            tempo = 0
            st.session_state_tempo = tempo
            



    with coluna_inicial_2:
        st.write('')
        st.write('')
        if st.button('Atualizar MAF'):
            url = 'http://sia:3000/backend/busca_generica/buscaGenerica?view=MGCLI.AGDTI_VW_DX_BALANCEAMENTO_PH'
            url_embaladeiras_ativas = 'http://sia:3000/backend/busca_generica/buscaGenericaMYSQLAvilla?sql=SELECT%20*%20FROM%20avillaconsulto.vw_dx_emb_presentes'
            

            variaveis_df = pd.read_json(url)

            def correcao_(variaveis_df):
                if variaveis_df['VARIEDADE'] == 'TOMMY ATKINS':
                    return 'Tommy Atkins'
                elif variaveis_df['VARIEDADE'] == 'PALMER':
                    return 'Palmer'
                elif variaveis_df['VARIEDADE'] == 'KEITT':
                    return 'Keitt'
                elif variaveis_df['VARIEDADE'] == 'KENT':
                    return 'Kent'
                elif variaveis_df['VARIEDADE'] == 'OMER':
                    return 'Omer'
                else:
                    return 'NADA'

            variaveis_df['VARIEDADE'] = variaveis_df.apply(correcao_, axis = 1)
        


            def calibre(variaveis_df):
                if variaveis_df['VARIEDADE'] == 'Palmer' and (variaveis_df['PESO'] <= 1130 and variaveis_df['PESO'] > 980):
                    return '4'
                elif (variaveis_df['VARIEDADE'] == 'Palmer') and (variaveis_df['PESO'] <= 980 and variaveis_df['PESO'] > 777):
                    return '5'
                elif (variaveis_df['VARIEDADE'] == 'Palmer') and (variaveis_df['PESO'] <= 777 and variaveis_df['PESO'] > 630):
                    return '6'
                elif (variaveis_df['VARIEDADE'] == 'Palmer') and (variaveis_df['PESO'] <= 630 and variaveis_df['PESO'] > 557):
                    return '7'
                elif (variaveis_df['VARIEDADE'] == 'Palmer') and (variaveis_df['PESO'] <= 557 and variaveis_df['PESO'] > 478):
                    return '8'
                elif (variaveis_df['VARIEDADE'] == 'Palmer') and (variaveis_df['PESO'] <= 478 and variaveis_df['PESO'] > 438):
                    return '9'
                elif (variaveis_df['VARIEDADE'] == 'Palmer') and (variaveis_df['PESO'] <= 438 and variaveis_df['PESO'] > 376):
                    return '10'
                elif (variaveis_df['VARIEDADE'] == 'Palmer') and (variaveis_df['PESO'] <= 376 and variaveis_df['PESO'] > 295):
                    return '12'
                elif (variaveis_df['VARIEDADE'] == 'Palmer') and (variaveis_df['PESO'] <= 295 and variaveis_df['PESO'] > 280):
                    return '14'
                elif (variaveis_df['VARIEDADE'] == 'Palmer') and (variaveis_df['PESO'] <= 280):
                    return '0'
                elif (variaveis_df['VARIEDADE'] == 'Palmer') and (variaveis_df['PESO'] > 1130):
                    return '100'
                #################################################### TOMMY ATKINS #####################################################
                elif variaveis_df['VARIEDADE'] == 'Tommy Atkins' and (variaveis_df['PESO'] <= 1200 and variaveis_df['PESO'] > 1000):
                    return '4'
                elif (variaveis_df['VARIEDADE'] == 'Tommy Atkins') and (variaveis_df['PESO'] <= 1000 and variaveis_df['PESO'] > 880):
                    return '5'
                elif (variaveis_df['VARIEDADE'] == 'Tommy Atkins') and (variaveis_df['PESO'] <= 880 and variaveis_df['PESO'] > 640):
                    return '6'
                elif (variaveis_df['VARIEDADE'] == 'Tommy Atkins') and (variaveis_df['PESO'] <= 640 and variaveis_df['PESO'] > 557):
                    return '7'
                elif (variaveis_df['VARIEDADE'] == 'Tommy Atkins') and (variaveis_df['PESO'] <= 557 and variaveis_df['PESO'] > 480):
                    return '8'
                elif (variaveis_df['VARIEDADE'] == 'Tommy Atkins') and (variaveis_df['PESO'] <= 480 and variaveis_df['PESO'] > 442):
                    return '9'
                elif (variaveis_df['VARIEDADE'] == 'Tommy Atkins') and (variaveis_df['PESO'] <= 442 and variaveis_df['PESO'] > 371):
                    return '10'
                elif (variaveis_df['VARIEDADE'] == 'Tommy Atkins') and (variaveis_df['PESO'] <= 371 and variaveis_df['PESO'] > 296):
                    return '12'
                elif (variaveis_df['VARIEDADE'] == 'Tommy Atkins') and (variaveis_df['PESO'] <= 296 and variaveis_df['PESO'] > 279):
                    return '14'
                elif (variaveis_df['VARIEDADE'] == 'Tommy Atkins') and (variaveis_df['PESO'] <= 279):
                    return '0'
                elif (variaveis_df['VARIEDADE'] == 'Tommy Atkins') and (variaveis_df['PESO'] > 1200):
                    return '100'
                    
                #################################################### KEITT #####################################################

                elif (variaveis_df['VARIEDADE'] == 'Keitt' or variaveis_df['VARIEDADE'] == 'Omer') and (variaveis_df['PESO'] <= 1500 and variaveis_df['PESO'] > 880):
                    return '4'
                elif (variaveis_df['VARIEDADE'] == 'Keitt' or variaveis_df['VARIEDADE'] == 'Omer') and (variaveis_df['PESO'] <= 880 and variaveis_df['PESO'] > 770):
                    return '5'
                elif (variaveis_df['VARIEDADE'] == 'Keitt' or variaveis_df['VARIEDADE'] == 'Omer') and (variaveis_df['PESO'] <= 770 and variaveis_df['PESO'] > 622):
                    return '6'
                elif (variaveis_df['VARIEDADE'] == 'Keitt' or variaveis_df['VARIEDADE'] == 'Omer') and (variaveis_df['PESO'] <= 622 and variaveis_df['PESO'] > 553):
                    return '7'
                elif (variaveis_df['VARIEDADE'] == 'Keitt' or variaveis_df['VARIEDADE'] == 'Omer') and (variaveis_df['PESO'] <= 553 and variaveis_df['PESO'] > 476):
                    return '8'
                elif (variaveis_df['VARIEDADE'] == 'Keitt' or variaveis_df['VARIEDADE'] == 'Omer') and (variaveis_df['PESO'] <= 476 and variaveis_df['PESO'] > 439):
                    return '9'
                elif (variaveis_df['VARIEDADE'] == 'Keitt' or variaveis_df['VARIEDADE'] == 'Omer') and (variaveis_df['PESO'] <= 439 and variaveis_df['PESO'] > 385):
                    return '10'
                elif (variaveis_df['VARIEDADE'] == 'Keitt' or variaveis_df['VARIEDADE'] == 'Omer') and (variaveis_df['PESO'] <= 385 and variaveis_df['PESO'] > 305):
                    return '12'
                elif (variaveis_df['VARIEDADE'] == 'Keitt' or variaveis_df['VARIEDADE'] == 'Omer') and (variaveis_df['PESO'] <= 305 and variaveis_df['PESO'] > 279):
                    return '14'
                elif (variaveis_df['VARIEDADE'] == 'Keitt' or variaveis_df['VARIEDADE'] == 'Omer') and (variaveis_df['PESO'] <= 279):
                    return '0'
                elif (variaveis_df['VARIEDADE'] == 'Keitt' or variaveis_df['VARIEDADE'] == 'Omer') and (variaveis_df['PESO'] > 1500):
                    return '100'

                #################################################### KENT #####################################################
                elif variaveis_df['VARIEDADE'] == 'Kent' and (variaveis_df['PESO'] <= 1300 and variaveis_df['PESO'] > 930):
                    return '4'
                elif (variaveis_df['VARIEDADE'] == 'Kent') and (variaveis_df['PESO'] <= 930 and variaveis_df['PESO'] > 760):
                    return '5'
                elif (variaveis_df['VARIEDADE'] == 'Kent') and (variaveis_df['PESO'] <= 760 and variaveis_df['PESO'] > 626):
                    return '6'
                elif (variaveis_df['VARIEDADE'] == 'Kent') and (variaveis_df['PESO'] <= 626 and variaveis_df['PESO'] > 545):
                    return '7'
                elif (variaveis_df['VARIEDADE'] == 'Kent') and (variaveis_df['PESO'] <= 545 and variaveis_df['PESO'] > 476):
                    return '8'
                elif (variaveis_df['VARIEDADE'] == 'Kent') and (variaveis_df['PESO'] <= 476 and variaveis_df['PESO'] > 444):
                    return '9'
                elif (variaveis_df['VARIEDADE'] == 'Kent') and (variaveis_df['PESO'] <= 444 and variaveis_df['PESO'] > 375):
                    return '10'
                elif (variaveis_df['VARIEDADE'] == 'Kent') and (variaveis_df['PESO'] <= 375 and variaveis_df['PESO'] > 303):
                    return '12'
                elif (variaveis_df['VARIEDADE'] == 'Kent') and (variaveis_df['PESO'] <= 303 and variaveis_df['PESO'] > 269):
                    return '14'
                elif (variaveis_df['VARIEDADE'] == 'Kent') and (variaveis_df['PESO'] <= 269):
                    return '0'
                elif (variaveis_df['VARIEDADE'] == 'Kent') and (variaveis_df['PESO'] > 1300):
                    return '100'

            
            variaveis_df['CALIBRE'] = variaveis_df.apply(calibre, axis =1)
            
            variaveis_df = variaveis_df.drop(columns = ['CONTENTORES'])
            variaveis_df.rename(columns={'TOTAL_CONTENTORES':'CONTENTORES'}, inplace = True)

            dataset = variaveis_df

            dataset.rename(columns = {"PESO":"Peso","CALIBRE":"Calibre","NUMERO_FRUTO":"Fruto","QUALIDADE":"Qualidade","VARIEDADE":"Variedade"}, inplace = True)
            
            
            dataset['Calibre'] = dataset['Calibre'].astype(int)
            
            


            a = dataset['Calibre'].value_counts() / dataset['Calibre'].count()

            


        ################ ALTERAR AQUI DENTRO OS PERCENTUAIS DE CALIBRE EM b ################

            url_percentual_MAF = 'http://sia:3000/backend/maf/percentuaisCalibre'

            dataset_MAF = pd.read_json(url_percentual_MAF)
            dataset_MAF = dataset_MAF.dropna()
            dataset_MAF = dataset_MAF.drop(columns = ['CONTROLE_MAF'])
            dataset_MAF['Calibre'] = dataset_MAF['CALIBRE_QUALIDADE'].str[:3]
            dataset_MAF['Qualidade'] = dataset_MAF['CALIBRE_QUALIDADE'].str[3:]

    ########################################## DADOS PARA TESTE ##########################################



    ########################################## REMOVER ACIMA DEPOIS ##########################################

            def correcao_calibre_MAF(dataset_MAF):
                    if dataset_MAF['Calibre'] == 'C05':
                        return 5
                    elif dataset_MAF['Calibre'] == 'C04':
                        return 4
                    elif dataset_MAF['Calibre'] == 'C06':
                        return 6
                    elif dataset_MAF['Calibre'] == 'C07':
                        return 7
                    elif dataset_MAF['Calibre'] == 'C08':
                        return 8
                    elif dataset_MAF['Calibre'] == 'C09':
                        return 9
                    elif dataset_MAF['Calibre'] == 'C10':
                        return 10
                    elif dataset_MAF['Calibre'] == 'C12':
                        return 12
                    elif dataset_MAF['Calibre'] == 'C14':
                        return 14
                    elif dataset_MAF['Calibre'] == 'C16':
                        return 16
                    elif dataset_MAF['Calibre'] == 'Ref':
                        return 0

            dataset_MAF['Calibre'] = dataset_MAF.apply(correcao_calibre_MAF, axis = 1)

            dataset_MAF['Calibre'] = dataset_MAF['Calibre'].astype(str)


            def ajuste_final(dataset_MAF):
                        if dataset_MAF['Calibre'] == '0':
                            return 'Refugo'
                        else:
                            return dataset_MAF['Calibre']

            dataset_MAF['Calibre'] = dataset_MAF.apply(ajuste_final, axis = 1) 

            def correcao_qualidade_MAF(dataset_MAF):
                    if dataset_MAF['Qualidade'] == ' Q1':
                        return 1
                    elif dataset_MAF['Qualidade'] == ' Q2':
                        return 2
                    elif dataset_MAF['Qualidade'] == ' Q3':
                        return 3
                    elif dataset_MAF['Qualidade'] == 'ugo':
                        return 4

            dataset_MAF['Qualidade'] = dataset_MAF.apply(correcao_qualidade_MAF, axis = 1)
            dataset_MAF = dataset_MAF.drop(columns = ['CALIBRE_QUALIDADE'])
            #dataset_MAF.columns

            def correcao_variedade_maf(dataset_MAF):
                if dataset_MAF['VARIEDADE'] == 'TOMMY':
                    return "Tommy Atkins"
                elif dataset_MAF['VARIEDADE'] == 'TAMMY':
                    return "Tommy Atkins"
                elif dataset_MAF['VARIEDADE'] == 'KEITT':
                    return "Keitt"
                elif dataset_MAF['VARIEDADE'] == 'KENT':
                    return "Kent"
                elif dataset_MAF['VARIEDADE'] == 'PALMER':
                    return "Palmer"
                elif dataset_MAF['VARIEDADE'] == 'OMER':
                    return 'Omer'
            dataset_MAF['VARIEDADE'] = dataset_MAF.apply(correcao_variedade_maf, axis = 1)


            controle = dataset_MAF['CONTROLE_MEGA'][0]
            st.session_state.control = controle

            VARIEDADE = dataset_MAF['VARIEDADE'][0]
            st.session_state.variety = VARIEDADE


            somatorio_frutos_peso = pd.pivot_table(dataset_MAF, index = 'Calibre', values = ['QTD_FRUTOS','PESO_KG','QTD_FRUTOS_RECENTE','PESO_KG_RECENTE'],aggfunc= 'sum')
            somatorio_frutos_peso = somatorio_frutos_peso.reset_index()

            somatorio_frutos_peso['Percentual'] = (somatorio_frutos_peso['QTD_FRUTOS'] / somatorio_frutos_peso['QTD_FRUTOS'].sum()) * 100

            somatorio_frutos_peso['Percentual_RECENTE'] = (somatorio_frutos_peso['QTD_FRUTOS_RECENTE'] / somatorio_frutos_peso['QTD_FRUTOS_RECENTE'].sum()) * 100
            #somatorio_frutos_peso



            somatorio_qualidade = pd.pivot_table(dataset_MAF, index = 'Qualidade', values = ['QTD_FRUTOS'],aggfunc= 'sum')
            #somatorio_qualidade = pd.DataFrame(somatorio_qualidade)

            somatorio_qualidade = somatorio_qualidade.reset_index()

            somatorio_qualidade['Percent'] = (somatorio_qualidade['QTD_FRUTOS'] / somatorio_qualidade['QTD_FRUTOS'].sum())
            
            #aa = somatorio_qualidade[somatorio_qualidade.Qualidade==1].Qualidade.item()
            #somatorio_qualidade


            result = somatorio_qualidade.Qualidade.isin([3]).any().any()
            if result:
                print(' ')
            else:
                somatorio_qualidade = somatorio_qualidade.append({'Qualidade':3, 'Percent':0}, ignore_index=True)

            result2 = somatorio_qualidade.Qualidade.isin([4]).any().any()
            if result2:
                print(' ')
            else:
                somatorio_qualidade = somatorio_qualidade.append({'Qualidade':4, 'Percent':0}, ignore_index=True)

            result3 = somatorio_qualidade.Qualidade.isin([2]).any().any()
            if result3:
                print(' ')
            else:
                somatorio_qualidade = somatorio_qualidade.append({'Qualidade':2, 'Percent':0}, ignore_index=True)
            
            result4 = somatorio_qualidade.Qualidade.isin([1]).any().any()
            if result4:
                print(' ')
            else:
                somatorio_qualidade = somatorio_qualidade.append({'Qualidade':1, 'Percent':0}, ignore_index=True)


            def corr_(somatorio_qualidade):
                if somatorio_qualidade['Qualidade'] == 1.0:
                    return 1
                elif somatorio_qualidade['Qualidade'] == 2.0:
                    return 2
                elif somatorio_qualidade['Qualidade'] == 3.0:
                    return 3
                elif somatorio_qualidade['Qualidade'] == 4.0:
                    return 4

            somatorio_qualidade['Qualidade'] = somatorio_qualidade.apply(corr_, axis =1)
            somatorio_qualidade['Qualidade'] = somatorio_qualidade['Qualidade'].astype(int)

            somatorio_qualidade = somatorio_qualidade.dropna()

            st.session_state.quality_percent = somatorio_qualidade


    ################################## DEFININDO NOVOS PERCENTUAIS ##################################
            
            result_somatorio_frutos_peso = somatorio_frutos_peso.Calibre.isin(['5']).any().any()
            if result_somatorio_frutos_peso:
                print(' ')
            else:
                somatorio_frutos_peso = somatorio_frutos_peso.append({'Calibre':'5', 'Percentual':0}, ignore_index=True)
            result_somatorio_frutos_peso = somatorio_frutos_peso.Calibre.isin(['6']).any().any()
            if result_somatorio_frutos_peso:
                print(' ')
            else:
                somatorio_frutos_peso = somatorio_frutos_peso.append({'Calibre':'6', 'Percentual':0}, ignore_index=True)
            result_somatorio_frutos_peso = somatorio_frutos_peso.Calibre.isin(['7']).any().any()
            if result_somatorio_frutos_peso:
                print(' ')
            else:
                somatorio_frutos_peso = somatorio_frutos_peso.append({'Calibre':'7', 'Percentual':0}, ignore_index=True)


            result_somatorio_frutos_peso = somatorio_frutos_peso.Calibre.isin(['8']).any().any()
            if result_somatorio_frutos_peso:
                print(' ')
            else:
                somatorio_frutos_peso = somatorio_frutos_peso.append({'Calibre':'8', 'Percentual':0}, ignore_index=True)


            result_somatorio_frutos_peso = somatorio_frutos_peso.Calibre.isin(['9']).any().any()
            if result_somatorio_frutos_peso:
                print(' ')
            else:
                somatorio_frutos_peso = somatorio_frutos_peso.append({'Calibre':'9', 'Percentual':0}, ignore_index=True)


            result_somatorio_frutos_peso = somatorio_frutos_peso.Calibre.isin(['10']).any().any()
            if result_somatorio_frutos_peso:
                print(' ')
            else:
                somatorio_frutos_peso = somatorio_frutos_peso.append({'Calibre':'10', 'Percentual':0}, ignore_index=True)


            result_somatorio_frutos_peso = somatorio_frutos_peso.Calibre.isin(['12']).any().any()
            if result_somatorio_frutos_peso:
                print(' ')
            else:
                somatorio_frutos_peso = somatorio_frutos_peso.append({'Calibre':'12', 'Percentual':0}, ignore_index=True)


            result_somatorio_frutos_peso = somatorio_frutos_peso.Calibre.isin(['14']).any().any()
            if result_somatorio_frutos_peso:
                print(' ')
            else:
                somatorio_frutos_peso = somatorio_frutos_peso.append({'Calibre':'14', 'Percentual':0}, ignore_index=True)


            result_somatorio_frutos_peso = somatorio_frutos_peso.Calibre.isin(['16']).any().any()
            if result_somatorio_frutos_peso:
                print(' ')
            else:
                somatorio_frutos_peso = somatorio_frutos_peso.append({'Calibre':'16', 'Percentual':0}, ignore_index=True)

            filtro_ref = somatorio_frutos_peso['Calibre'] != 'Refugo'
            somatorio_frutos_peso = somatorio_frutos_peso[filtro_ref]

            somatorio_frutos_peso['Calibre'] = somatorio_frutos_peso['Calibre'].astype(int)
            
            somatorio_frutos_peso_para_b = somatorio_frutos_peso.drop(columns = ['PESO_KG','QTD_FRUTOS'])


            b = somatorio_frutos_peso_para_b
            b = b.sort_values('Calibre')
            #b

            st.session_state.b_ = b

            st.session_state.anterior = dataset

            df_embaladeiras_ativas = pd.read_json(url_embaladeiras_ativas)

            if len(df_embaladeiras_ativas) == 0:
                url_embaladeiras_ativas = 'http://sia:3000/backend/busca_generica/buscaGenerica?view=MGCLI.AGDTI_VW_DX_EMB_ATIVAS'
                df_embaladeiras_ativas = pd.read_json(url_embaladeiras_ativas)


            df_embaladeiras_ativas.rename(columns = {'CPF':'MATRICULA','PESSOA':'NOME'}, inplace = True)
            
            df_embaladeiras_ativas['NOME'] = df_embaladeiras_ativas['NOME'].str[6:]


            st.session_state.url_embala = df_embaladeiras_ativas



            #dataset_MAF
            ###########################  RETIRAR ACIMA, POIS VAMOS TER DADOS #######################



            results = [
                int((parse(c) - parse(o)).total_seconds())
                for c, o in zip(dataset_MAF['HORA_ULTIMA_ATUALIZACAO'], dataset_MAF['HORA_ATUALIZACAO'])
                if parse(c) - parse(o) < datetime.timedelta(seconds=1)]

            st.session_state_tempo = results[1]

            #dataset_MAF

            tempo_passado_minutos = results[1] * -1 / 60
            tempo_passado_horas = tempo_passado_minutos / 60
            toneladas_passadas = dataset_MAF['PESO_KG_RECENTE'].sum() / 1000

            st.session_state_tempo = tempo_passado_minutos

            produtividade_atual = round(toneladas_passadas / tempo_passado_horas,2)

            st.session_state.prod_MAF = produtividade_atual

            def caixas_maf(somatorio_frutos_peso):
                    if somatorio_frutos_peso['Calibre'] == 4:
                        return somatorio_frutos_peso['QTD_FRUTOS'] / 4
                    elif somatorio_frutos_peso['Calibre'] == 5:
                        return somatorio_frutos_peso['QTD_FRUTOS'] / 5
                    elif somatorio_frutos_peso['Calibre'] == 6:
                        return somatorio_frutos_peso['QTD_FRUTOS'] / 6
                    elif somatorio_frutos_peso['Calibre'] == 7:
                        return somatorio_frutos_peso['QTD_FRUTOS'] / 7
                    elif somatorio_frutos_peso['Calibre'] == 8:
                        return somatorio_frutos_peso['QTD_FRUTOS'] / 8
                    elif somatorio_frutos_peso['Calibre'] == 9:
                        return somatorio_frutos_peso['QTD_FRUTOS'] / 9
                    elif somatorio_frutos_peso['Calibre'] == 10:
                        return somatorio_frutos_peso['QTD_FRUTOS'] / 10
                    elif somatorio_frutos_peso['Calibre'] == 12:
                        return somatorio_frutos_peso['QTD_FRUTOS'] / 12
                    elif somatorio_frutos_peso['Calibre'] == 14:
                        return somatorio_frutos_peso['QTD_FRUTOS'] / 14
                    elif somatorio_frutos_peso['Calibre'] == 16:
                        return somatorio_frutos_peso['QTD_FRUTOS'] / 16
                    
            #somatorio_frutos_peso
            somatorio_frutos_peso['CAIXAS'] = somatorio_frutos_peso.apply(caixas_maf, axis = 1)

            caixas_total_processadas = somatorio_frutos_peso['CAIXAS'].sum()

            ##### TEMPO RESTANTE #####
            def caixas_maf_recente(somatorio_frutos_peso):
                    if somatorio_frutos_peso['Calibre'] == 4:
                        return somatorio_frutos_peso['QTD_FRUTOS_RECENTE'] / 4
                    elif somatorio_frutos_peso['Calibre'] == 5:
                        return somatorio_frutos_peso['QTD_FRUTOS_RECENTE'] / 5
                    elif somatorio_frutos_peso['Calibre'] == 6:
                        return somatorio_frutos_peso['QTD_FRUTOS_RECENTE'] / 6
                    elif somatorio_frutos_peso['Calibre'] == 7:
                        return somatorio_frutos_peso['QTD_FRUTOS_RECENTE'] / 7
                    elif somatorio_frutos_peso['Calibre'] == 8:
                        return somatorio_frutos_peso['QTD_FRUTOS_RECENTE'] / 8
                    elif somatorio_frutos_peso['Calibre'] == 9:
                        return somatorio_frutos_peso['QTD_FRUTOS_RECENTE'] / 9
                    elif somatorio_frutos_peso['Calibre'] == 10:
                        return somatorio_frutos_peso['QTD_FRUTOS_RECENTE'] / 10
                    elif somatorio_frutos_peso['Calibre'] == 12:
                        return somatorio_frutos_peso['QTD_FRUTOS_RECENTE'] / 12
                    elif somatorio_frutos_peso['Calibre'] == 14:
                        return somatorio_frutos_peso['QTD_FRUTOS_RECENTE'] / 14
                    elif somatorio_frutos_peso['Calibre'] == 16:
                        return somatorio_frutos_peso['QTD_FRUTOS_RECENTE'] / 16

            somatorio_frutos_peso['CAIXAS_RECENTE'] = somatorio_frutos_peso.apply(caixas_maf_recente, axis = 1)

            caixas_recentes_processadas = somatorio_frutos_peso['CAIXAS_RECENTE'].sum()
            st.session_state.cxs_recentes = caixas_recentes_processadas

            # se em tempo_passado_horas eu fiz 


            #caixas_total_processadas
            st.session_state.cxs_process = caixas_total_processadas

            hora_ultima_atualização = dataset_MAF['HORA_ULTIMA_ATUALIZACAO'][0]

            st.write('Horário da última atualização:', hora_ultima_atualização)





    try:
        b = st.session_state.b_ 
        dataset = st.session_state.anterior
        quality = st.session_state.quality_percent
        produtividade_atual = st.session_state.prod_MAF
        controle = st.session_state.control 
        VARIEDADE = st.session_state.variety
    except AttributeError:
        st.info('##### Clique em "Atualizar Controle" para verificar se existe amostragem para o controle atual !')
        dataset.rename(columns = {"PESO":"Peso","CALIBRE":"Calibre","NUMERO_FRUTO":"Fruto","QUALIDADE":"Qualidade"}, inplace = True)


    try:
        avg_frutos_caixotes = round(dataset['N_CAIXOTE'].value_counts().sum() / len(dataset['N_CAIXOTE'].value_counts()))
    except ValueError:
        st.error('Erro com link do mega, possíveis motivos:')
        #st.error('\n')
        st.write('1 - Amostragem de calibres não lançada/feita para o controle')
        #st.error('\n',)
        st.write('2 - Base do mega indisponível')
        #st.error('\n')
        st.write('3 - Erro de digitação nos campos da base de dados')
        #st.error('\n')
        st.error('###### Para verificar as opções acima clique nos links a seguir e verifique se um dos links carrega a base de dados sem erros ou valores faltantes')
        st.info('http://sia:3000/backend/busca_generica/buscaGenerica?view=MGCLI.AGDTI_VW_DX_BALANCEAMENTO_PH')
        st.info('http://177.52.21.58:3000/backend/busca_generica/buscaGenerica?view=MGCLI.AGDTI_VW_DX_BALANCEAMENTO_PH')


    if avg_frutos_caixotes == 1:
        avg_frutos_caixotes = 30
        #avg_frutos_caixotes

        ##### Nomeando variedade e atribuindo valor para caixotes

    Caixotes = dataset['CONTENTORES'][0].item()
    

    ##### Criando base inicial com os percentuais de calibre
    dataset = dataset 


    #################################################################################   CORRIGINDO PERCENTUAIS FALTANTES    ####################################################################################################

    result_b = b.Calibre.isin([4]).any().any()
    if result_b:
        print(' ')
    else:
        b = b.append({'Calibre':4, 'Percentual':0}, ignore_index=True)

    result_b = b.Calibre.isin([5]).any().any()
    if result_b:
        print(' ')
    else:
        b = b.append({'Calibre':5, 'Percentual':0}, ignore_index=True)


    result_b = b.Calibre.isin([6]).any().any()
    if result_b:
        print(' ')
    else:
        b = b.append({'Calibre':6, 'Percentual':0}, ignore_index=True)


    result_b = b.Calibre.isin([7]).any().any()
    if result_b:
        print(' ')
    else:
        b = b.append({'Calibre':7, 'Percentual':0}, ignore_index=True)


    result_b = b.Calibre.isin([8]).any().any()
    if result_b:
        print(' ')
    else:
        b = b.append({'Calibre':8, 'Percentual':0}, ignore_index=True)


    result_b = b.Calibre.isin([9]).any().any()
    if result_b:
        print(' ')
    else:
        b = b.append({'Calibre':9, 'Percentual':0}, ignore_index=True)


    result_b = b.Calibre.isin([10]).any().any()
    if result_b:
        print(' ')
    else:
        b = b.append({'Calibre':10, 'Percentual':0}, ignore_index=True)


    result_b = b.Calibre.isin([12]).any().any()
    if result_b:
        print(' ')
    else:
        b = b.append({'Calibre':12, 'Percentual':0}, ignore_index=True)


    result_b = b.Calibre.isin([14]).any().any()
    if result_b:
        print(' ')
    else:
        b = b.append({'Calibre':14, 'Percentual':0}, ignore_index=True)


    result_b = b.Calibre.isin([16]).any().any()
    if result_b:
        print(' ')
    else:
        b = b.append({'Calibre':16, 'Percentual':0}, ignore_index=True)


    percentual_de_4 = b[b.Calibre==4].Percentual.item()
    percentual_de_5 = b[b.Calibre==5].Percentual.item()
    percentual_de_6 = b[b.Calibre==6].Percentual.item()
    percentual_de_7 = b[b.Calibre==7].Percentual.item()
    percentual_de_8 = b[b.Calibre==8].Percentual.item()
    percentual_de_9 = b[b.Calibre==9].Percentual.item()
    percentual_de_10 = b[b.Calibre==10].Percentual.item()
    percentual_de_12 = b[b.Calibre==12].Percentual.item()
    percentual_de_14 = b[b.Calibre==14].Percentual.item()
    percentual_de_16 = b[b.Calibre==16].Percentual.item()


    ##################################################### CORRIGINDO PERCENTUAIS FALTANTES ###########################################################################

    result = quality.Qualidade.isin([3]).any().any()
    if result:
        print(' ')
    else:
        quality = quality.append({'Qualidade':3, 'Percent':0}, ignore_index=True)

    result2 = quality.Qualidade.isin([4]).any().any()
    if result2:
        print(' ')
    else:
        quality = quality.append({'Qualidade':4, 'Percent':0}, ignore_index=True)

    result3 = quality.Qualidade.isin([2]).any().any()
    if result3:
        print(' ')
    else:
        quality = quality.append({'Qualidade':2, 'Percent':0}, ignore_index=True)


    result4 = quality.Qualidade.isin([1]).any().any()
    if result4:
        print(' ')
    else:
        quality = quality.append({'Qualidade':1, 'Percent':0}, ignore_index=True)


    #################################################################################  CÁCULO QUALIDADE DOS CALIBRE #######################################################

    #ualidade_calibres = dataset.groupby('Calibre')['Qualidade'].value_counts() / dataset.groupby('Calibre')['Qualidade'].count()
    #qualidade_calibres2 = pd.pivot_table(dataset, index = ['Calibre','Qualidade'])

    #################################################################################  CHECK QUALIDADE GERAL - ATRIBUINDO VALOR ####################################################
    quality['Qualidade'] = quality['Qualidade'].astype(int)



    primeira_percent = quality[quality.Qualidade==1].Percent.item()
    segunda_percent = quality[quality.Qualidade==2].Percent.item()
    terceira_percent = quality[quality.Qualidade==3].Percent.item()
    refugo_percent = quality[quality.Qualidade==4].Percent.item()

    #################################### ATUALIZANDO DADOS DA MAF ##########################################################


    #################################################################################  CÁLCULO DE CAIXAS POR CALIBRE  ####################################################################################################


    st.session_state_base_crua = b

    #################### ANALISAR ESSA CONTA SE DEVE SER DA AMOSTRAGEM OU DA MAF ####################

    


    dataset_2 = dataset 

    aa = pd.DataFrame(dataset_2['Calibre'].value_counts())
    aa = aa.reset_index()
    aa.columns = ['Calibre','Qtde_mangas']
    

    aa['Caixas'] = aa['Qtde_mangas'] / aa['Calibre']
    b = b.merge(aa, how = 'left')


    

    #def correcao_caixas(b):
    #   if b['Caixas'] == 'Infinity':
    #      return 0
    #b['Caixas'] == b.apply(correcao_caixas, axis = 1)

    b = b.fillna(0)
    b = b.replace([np.inf, -np.inf], 0)

    b = b.drop(columns = ['Qtde_mangas'])
    


    #########################################  ATRIBUINDO CONSTANTES INICIAIS PARA AS VARIAVEIS #########################################

    produtividade_embaladeira = 0.75
    produtividade_talo = 0.80
    produtividade_limpeza = 0.75
    produtividade_limpeza2 = 0.75
    caixotes = Caixotes
    variedade = VARIEDADE 


    ################################ BASE DE ESTUDO DAS EMBALADEIRAS E DAS ATIVAS NO DIA #########################################

    padrao_embaldeiras_total = pd.read_excel('padrao_embaladeiras_TUDO_cenarios.xlsx')
    df_embaladeiras_ativas = st.session_state.url_embala

        
    df_222 = df_embaladeiras_ativas.merge(padrao_embaldeiras_total)
    padrao_embaldeiras = df_222
    embaladeira = len(padrao_embaldeiras.groupby('PESSOA'))

    Programa_input = 'Entre Safra'
    st.session_state.emba_aviso = embaladeira

    coluna1, coluna2 = st.columns(2)

    ############## ESTRUTURAÇÃO DAS ABAS ##############
    

    with coluna1:
        from PIL import Image
        img = Image.open('agrodn.png')
        newsize = (380,110)
        img2 = img.resize(newsize)

        ########## JANELA LATERAL ##########

        st.sidebar.image(img2, use_column_width=True)
        st.sidebar.title('Menu')
        st.sidebar.markdown('Escolha a informação para visualizar:')
        


    pagina_selecionada = st.sidebar.radio('', ['Balanceamento e produtividade','Linhas de embalagem','Distribuição embaladeiras'])

    if pagina_selecionada == 'Balanceamento e produtividade':
        
        ############## DEFININDO CONTROLE ######################
        #tempo_2 = st.session_state_tempo

        colunA, colunB, colunC, colunD = st.columns([0.3,0.3,0.5,1])

        #controle = dataset['CONTROLE'][0]


        st.session_state.controle = controle

        ############## EXIBINDO MÉTRICA DO CONTROLE ######################
        controle2 = st.session_state.controle
        colunA.metric(label="Controle", value= controle2, delta= VARIEDADE)
        colunC.metric(label="MAF (t/h)", value= produtividade_atual) 

        tempo_2 = st.session_state_tempo
        colunB.metric(label="Intervalo de tempo (min)", value= round(tempo_2,2))
        #st.metric(label="MAF", value= produtividade_atual, delta= 't/h')  

        col2, col3 = st.columns([0.30,1])
        
        emba_aviso = st.session_state.emba_aviso

        ######################################### ALTERANDO PERCENTUAIS    ###############################################

        st.success('#### Ajuste dos percentuais de distribuição')
        coluna_0, coluna_11, coluna_22, coluna_33, coluna_44, coluna_55, coluna_66, coluna_77, coluna_88, coluna_99, coluna_00 = st.columns([0.01,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5])

        
        coluna_11.info('###### Calibre 4')
        percent_caliber_4 = coluna_11.text_input(label = '', value = round(percentual_de_4,2))
        coluna_22.info('###### Calibre 5')
        percent_caliber_5 = coluna_22.text_input(label = ' ', value = round(percentual_de_5,2))
        coluna_33.info('###### Calibre 6')
        percent_caliber_6 = coluna_33.text_input(label = '  ', value = round(percentual_de_6,2))
        coluna_44.info('###### Calibre 7')
        percent_caliber_7 = coluna_44.text_input(label = '   ', value = round(percentual_de_7,2))
        coluna_55.info('###### Calibre 8')
        percent_caliber_8 = coluna_55.text_input(label = '    ', value = round(percentual_de_8,2))
        coluna_66.info('###### Calibre 9')
        percent_caliber_9 = coluna_66.text_input(label = '     ', value = round(percentual_de_9,2))
        coluna_77.info('###### Calibre 10')
        percent_caliber_10 = coluna_77.text_input(label = '      ', value = round(percentual_de_10,2))
        coluna_88.info('###### Calibre 12')
        percent_caliber_12 = coluna_88.text_input(label = '       ', value = round(percentual_de_12,2))
        coluna_99.info('###### Calibre 14')
        percent_caliber_14 = coluna_99.text_input(label = '         ', value = round(percentual_de_14,2))
        coluna_00.info('###### Calibre 16')
        percent_caliber_16 = coluna_00.text_input(label = '           ', value = round(percentual_de_16,2))


        percent_caliber_4 = float(percent_caliber_4)
        percent_caliber_5 = float(percent_caliber_5)
        percent_caliber_6 = float(percent_caliber_6)
        percent_caliber_7 = float(percent_caliber_7)
        percent_caliber_8 = float(percent_caliber_8)
        percent_caliber_9 = float(percent_caliber_9)
        percent_caliber_10 = float(percent_caliber_10)
        percent_caliber_12 = float(percent_caliber_12)
        percent_caliber_14 = float(percent_caliber_14)
        percent_caliber_16 = float(percent_caliber_16)
        


        st.session_state_percent_4 = percent_caliber_4 
        st.session_state_percent_5 = percent_caliber_5
        st.session_state_percent_6 = percent_caliber_6 
        st.session_state_percent_7 = percent_caliber_7 
        st.session_state_percent_8 = percent_caliber_8 
        st.session_state_percent_9 = percent_caliber_9 
        st.session_state_percent_10 = percent_caliber_10 
        st.session_state_percent_12 = percent_caliber_12
        st.session_state_percent_14 = percent_caliber_14 
        st.session_state_percent_16 = percent_caliber_16
        st.write('')

        

        def ajuste(b):
            if b['Calibre'] == 4:
                return percent_caliber_4
            elif b['Calibre'] == 5:
                return percent_caliber_5
            elif b['Calibre'] == 6:
                return percent_caliber_6
            elif b['Calibre'] == 7:
                return percent_caliber_7
            elif b['Calibre'] == 8:
                return percent_caliber_8
            elif b['Calibre'] == 9:
                return percent_caliber_9
            elif b['Calibre'] == 10:
                return percent_caliber_10
            elif b['Calibre'] == 12:
                return percent_caliber_12
            elif b['Calibre'] == 14:
                return percent_caliber_14
            elif b['Calibre'] == 16:
                return percent_caliber_16

        b['Percentual'] = b.apply(ajuste, axis = 1)
        
        

    ### BALANCEAMENTO
        st.success('#### Balanceamento')

        ########################## ALTERANDO PRODUTIVIDADE E TIPO DE EMBALAGEM - COM PAPEL VS SEM PAPEL    #################################

        with st.form(key='planilha'):
            
            coluna1_1, coluna2_2,coluna3_3, coluna4_4 = st.columns([0.4,0.05,0.8,1])
            
            embaladeira_input = coluna1_1.number_input(label = 'Ajuste a quantidade de embaladeiras:', value = emba_aviso  , format = "%d", step = 1)
            Programa_input_2 = coluna1_1.selectbox('Selecione o período:', ['Entre Safra','Safra'])
            produtividade_embaladeira_input = coluna1_1.slider('Produtividade Embaladeiras', min_value = 0.1, max_value = 0.99, value = 0.75, step = 0.01)
            produtividade_talo_input = coluna1_1.slider('Produtividade Corte de Talo', min_value = 0.1, max_value = 0.99, value = 0.80, step = 0.01)
            produtividade_limpeza_input = coluna1_1.slider('Produtividade da Limpeza', min_value = 0.1, max_value = 0.99, value = 0.75, step = 0.01)
            produtividade_limpeza2_input = coluna1_1.slider('Produtividade da Seleção', min_value = 0.1, max_value = 0.99, value = 0.75, step = 0.01) 

            st.success('#### Embalagem - (Com ou Sem Papel):')

            colun0, colun, colun2, colun3, colun4, colun5,colun6,colun7,colun8,colun9,colun00 = st.columns([1,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,1])
        
            colun0.write('')
            colun00.write('')
            colun.info('###### Calibre 4')
            calibre_4_papel = colun.selectbox(label = '', options = ('Sem','Com'))
            colun2.info('###### Calibre 5')
            calibre_5_papel = colun2.selectbox(label = ' ', options = ('Sem','Com'))
            colun3.info('###### Calibre 6')
            calibre_6_papel = colun3.selectbox(label = '  ', options = ('Sem','Com'))
            colun4.info('###### Calibre 7')
            calibre_7_papel = colun4.selectbox(label = '   ', options = ('Sem','Com'))
            colun5.info('###### Calibre 8')
            calibre_8_papel = colun5.selectbox(label = '    ', options = ('Sem','Com'))
            colun6.info('###### Calibre 9')
            calibre_9_papel = colun6.selectbox(label = '     ', options = ('Sem','Com'))
            colun7.info('###### Calibre 10')
            calibre_10_papel = colun7.selectbox(label = '      ', options = ('Sem','Com'))
            colun8.info('###### Calibre 12')
            calibre_12_papel = colun8.selectbox(label = '       ', options = ('Sem','Com'))
            colun9.info('###### Calibre 14')
            calibre_14_papel = colun9.selectbox(label = '        ', options = ('Sem','Com'))
            
            button_submit = coluna1_1.form_submit_button('Calcular')

        if button_submit:
            embaladeira =  embaladeira_input
            Programa_input = Programa_input_2
            produtividade_embaladeira = produtividade_embaladeira_input
            produtividade_talo= produtividade_talo_input 
            produtividade_limpeza = produtividade_limpeza_input
            produtividade_limpeza2 = produtividade_limpeza2_input

    ################################ DEFININDO RITMOS DE EMBALAGEM ###############################

        def ritmo(b):
                if (b['Calibre'] == 5 and variedade == 'Palmer') and (calibre_4_papel == 'Com' or calibre_4_papel == 'Sem'):
                    return 229
                elif (b['Calibre'] == 4 and variedade == 'Palmer') and (calibre_5_papel == 'Com' or calibre_5_papel == 'Sem'):
                    return 229
                elif (b['Calibre'] == 6 and variedade == 'Palmer') and (calibre_6_papel == 'Com' or calibre_6_papel == 'Sem'):
                    return 169
                elif (b['Calibre'] == 7 and variedade == 'Palmer') and (calibre_7_papel == 'Com' or calibre_7_papel == 'Sem'):
                    return 174
                elif (b['Calibre'] == 8 and variedade == 'Palmer') and (calibre_8_papel == 'Com' or calibre_8_papel == 'Sem'):
                    return 191
                elif (b['Calibre'] == 9 and variedade == 'Palmer') and (calibre_9_papel == 'Com' or calibre_9_papel == 'Sem'):
                    return 157
                elif (b['Calibre'] == 10 and variedade == 'Palmer') and (calibre_10_papel == 'Com' or calibre_10_papel == 'Sem'):
                    return 139
                elif (b['Calibre'] == 12 and variedade == 'Palmer') and (calibre_12_papel == 'Com' or calibre_12_papel == 'Sem'):
                    return 149
                elif (b['Calibre'] == 14 and variedade == 'Palmer') and (calibre_14_papel == 'Com' or calibre_14_papel == 'Sem'):
                    return 85

        ###################################################################### Keitt #############################################################

                elif (b['Calibre'] == 5 and calibre_5_papel == 'Sem') and (variedade == 'Keitt' or variedade == 'Omer'):
                    return 517
                elif (b['Calibre'] == 4  and calibre_4_papel == 'Sem') and (variedade == 'Keitt' or variedade == 'Omer'):
                    return 517
                elif (b['Calibre'] == 6 and calibre_6_papel == 'Sem') and (variedade == 'Keitt' or variedade == 'Omer'):
                    return 412
                elif (b['Calibre'] == 7 and calibre_7_papel == 'Sem') and (variedade == 'Keitt' or variedade == 'Omer') :
                    return 321
                elif (b['Calibre'] == 8  and calibre_8_papel == 'Sem') and (variedade == 'Keitt' or variedade == 'Omer'):
                    return 301
                elif (b['Calibre'] == 9 and calibre_9_papel == 'Sem') and (variedade == 'Keitt' or variedade == 'Omer'):
                    return 257
                elif (b['Calibre'] == 10  and calibre_10_papel == 'Sem') and (variedade == 'Keitt' or variedade == 'Omer'):
                    return 261
                elif (b['Calibre'] == 12 and calibre_12_papel == 'Sem') and  (variedade == 'Keitt' or variedade == 'Omer'):
                    return 253
                elif (b['Calibre'] == 14  and calibre_14_papel == 'Sem') and (variedade == 'Keitt' or variedade == 'Omer'):
                    return 220

                elif (b['Calibre'] == 5 and calibre_5_papel == 'Com') and (variedade == 'Keitt' or variedade == 'Omer'):
                    return 235
                elif (b['Calibre'] == 4 and calibre_4_papel == 'Com') and (variedade == 'Keitt' or variedade == 'Omer'):
                    return 235
                elif (b['Calibre'] == 6  and calibre_6_papel == 'Com') and (variedade == 'Keitt' or variedade == 'Omer'):
                    return 178
                elif (b['Calibre'] == 7 and calibre_7_papel == 'Com') and (variedade == 'Keitt' or variedade == 'Omer'):
                    return 185
                elif (b['Calibre'] == 8 and calibre_8_papel == 'Com') and (variedade == 'Keitt' or variedade == 'Omer'):
                    return 195
                elif (b['Calibre'] == 9  and calibre_9_papel == 'Com') and (variedade == 'Keitt' or variedade == 'Omer'):
                    return 154
                elif (b['Calibre'] == 10 and calibre_10_papel == 'Com') and (variedade == 'Keitt' or variedade == 'Omer'):
                    return 144
                elif (b['Calibre'] == 12 and calibre_12_papel == 'Com') and (variedade == 'Keitt' or variedade == 'Omer'):
                    return 158
                elif (b['Calibre'] == 14 and calibre_14_papel == 'Com') and (variedade == 'Keitt' or variedade == 'Omer'):
                    return 90

        ################################################## Kent #############################################################
        #### Valores da Kent na planilha são iguais ao da Keitt
        #### Encontrei anteriormente no estudo das embaladerias que o ritmo era bem parecido com o da Keitt porém com pequenas diferenças
        #### por isso vou considerar os ritmos iguais aos do estudo e não iguais aos da Keitt

                elif (b['Calibre'] == 5 and variedade == 'Kent') and (calibre_5_papel == 'Sem'):
                    return 510
                elif (b['Calibre'] == 6 and variedade == 'Kent') and (calibre_6_papel == 'Sem'):
                    return 410
                elif (b['Calibre'] == 7 and variedade == 'Kent') and (calibre_7_papel == 'Sem'):
                    return 314
                elif (b['Calibre'] == 8 and variedade == 'Kent') and (calibre_8_papel == 'Sem'):
                    return 300
                elif (b['Calibre'] == 9 and variedade == 'Kent') and (calibre_9_papel == 'Sem'):
                    return 253
                elif (b['Calibre'] == 10 and variedade == 'Kent') and (calibre_10_papel == 'Sem'):
                    return 248
                elif (b['Calibre'] == 12 and variedade == 'Kent') and (calibre_12_papel == 'Sem'):
                    return 246
                elif (b['Calibre'] == 14 and variedade == 'Kent') and (calibre_14_papel == 'Sem'):
                    return 200


                elif (b['Calibre'] == 5 and variedade == 'Kent') and (calibre_5_papel == 'Com'):
                    return 235
                elif (b['Calibre'] == 6 and variedade == 'Kent') and (calibre_6_papel == 'Com'):
                    return 178
                elif (b['Calibre'] == 7 and variedade == 'Kent') and (calibre_7_papel == 'Com'):
                    return 185
                elif (b['Calibre'] == 8 and variedade == 'Kent') and (calibre_8_papel == 'Com'):
                    return 195
                elif (b['Calibre'] == 9 and variedade == 'Kent') and (calibre_9_papel == 'Com'):
                    return 154
                elif (b['Calibre'] == 10 and variedade == 'Kent') and (calibre_10_papel == 'Com'):
                    return 144
                elif (b['Calibre'] == 12 and variedade == 'Kent') and (calibre_12_papel == 'Com'):
                    return 158
                elif (b['Calibre'] == 14 and variedade == 'Kent') and (calibre_14_papel == 'Com'):
                    return 90


        ################################################## Tommy #############################################################

                elif (b['Calibre'] == 5 and variedade == 'Tommy Atkins') and (calibre_5_papel == 'Com' or calibre_5_papel == 'Sem'):
                    return 235
                elif (b['Calibre'] == 6 and variedade == 'Tommy Atkins') and (calibre_6_papel == 'Com' or calibre_6_papel == 'Sem'):
                    return 178
                elif (b['Calibre'] == 7 and variedade == 'Tommy Atkins') and (calibre_7_papel == 'Com' or calibre_7_papel == 'Sem'):
                    return 185
                elif (b['Calibre'] == 8 and variedade == 'Tommy Atkins') and (calibre_8_papel == 'Com' or calibre_8_papel == 'Sem'):
                    return 195
                elif (b['Calibre'] == 9 and variedade == 'Tommy Atkins') and (calibre_9_papel == 'Com' or calibre_9_papel == 'Sem'):
                    return 154
                elif (b['Calibre'] == 10 and variedade == 'Tommy Atkins') and (calibre_10_papel == 'Com' or calibre_10_papel == 'Sem'):
                    return 144
                elif (b['Calibre'] == 12 and variedade == 'Tommy Atkins') and (calibre_12_papel == 'Com' or calibre_12_papel == 'Sem'):
                    return 158
                elif (b['Calibre'] == 14 and variedade == 'Tommy Atkins') and (calibre_14_papel == 'Com' or calibre_14_papel == 'Sem'):
                    return 90
                else:
                    return 'NADA'
        
        b['Ritmo'] = b.apply(ritmo, axis = 1)

        filtro_ritmo = b['Ritmo'] != 'NADA'
        b = b[filtro_ritmo]

        col1, col2,col3,col4 = st.columns([0.1,0.01,1,1.2])

        ################################ CALCULO DE CAIXAS POR QUALIDADE ################################

        b['Caixas_total'] = ((caixotes * avg_frutos_caixotes * b['Percentual']) / b['Calibre']) / 100
        

        #st.write(b['Caixas_total'].sum())


        b['Caixas_1'] = ((caixotes * avg_frutos_caixotes * (b['Percentual']/100) * primeira_percent) / b['Calibre']) 
        b['Caixas_2'] = ((caixotes * avg_frutos_caixotes * (b['Percentual']/100) * segunda_percent)  / b['Calibre']) 
        b['Caixas_3'] = ((caixotes * avg_frutos_caixotes * (b['Percentual']/100) * terceira_percent) / b['Calibre'])

        ################## CALCULO DE HORAS TOTAIS ##################

        b['Horas_4kg'] = (b['Caixas_total'] / b['Ritmo']) / produtividade_embaladeira    
        
        st.session_state.caixotes = caixotes
        st.session_state.embaladeira = embaladeira
        st.session_state.variedade = variedade
        st.session_state.periodo_safra = Programa_input 
        st.session_state.produtividade_embaladeira = produtividade_embaladeira
        st.session_state.produtividade_talo = produtividade_talo
        st.session_state.produtividade_limpeza = produtividade_limpeza
        st.session_state.produtividade_selecao = produtividade_limpeza2

        st.session_state.calibre4 = calibre_4_papel
        st.session_state.calibre5 = calibre_5_papel
        st.session_state.calibre6 = calibre_6_papel
        st.session_state.calibre7 = calibre_7_papel
        st.session_state.calibre8 = calibre_8_papel
        st.session_state.calibre9 = calibre_9_papel
        st.session_state.calibre10 = calibre_10_papel
        st.session_state.calibre12 = calibre_12_papel
        st.session_state.calibre14 = calibre_14_papel
        

        ################## CALCULO DE RITMOS E BALANCEAMENTO ##################
        


        ritmo_embaladeira = ((b['Horas_4kg'].sum()  / embaladeira) * (1/24))
        corte_talo = round((caixotes * avg_frutos_caixotes) / (101303.19 * produtividade_talo * ritmo_embaladeira))
        ritmo_talo = ((((caixotes * avg_frutos_caixotes) / corte_talo) / (4200 * produtividade_talo)) * (1/24))
        diferenca_aceitavel = abs(round((ritmo_embaladeira - ritmo_talo),3))
        corte_talo2 = corte_talo
        ritmo_talo_2 = ((((caixotes * avg_frutos_caixotes) / corte_talo2) / (4200 * produtividade_talo)) * (1/24))
        
        ################## FUNÇÃO DE CAIXOTES, T/H, LIMPEZA E SELEÇÃO ##################

        def equilibrio(corte_talo, embaladeira):
        
                caixotes_hora = round((caixotes*0.0416667)/(ritmo_talo_2))
                Limpeza_selecao = round((caixotes_hora * avg_frutos_caixotes * 0.6) / (3230 * produtividade_limpeza))
                ton_horas = round(((b['Caixas_total'].sum()*4.05)/1000)/(b['Horas_4kg'].sum()/embaladeira),2)
                soma = segunda_percent + terceira_percent + refugo_percent                
                selecao_ = round((caixotes_hora * avg_frutos_caixotes * soma / (3501 * produtividade_limpeza2)) + (caixotes_hora * avg_frutos_caixotes * primeira_percent / (6480 * produtividade_limpeza2)))

                st.write('#### Quantidade ideal de pessoas no talo:', corte_talo2)
                st.write('#### Quantidade de pessoas na seleção:',selecao_ )
                st.write('#### Quantidade de pessoas na limpeza:', Limpeza_selecao)
                st.write('#### Capacidade de Caixotes/Hora:', caixotes_hora)
                st.write('#### Capacidade de Toneladas/Hora:', ton_horas)
                        
                st.session_state.caixotes_hora = caixotes_hora
                st.session_state.ton_horas = ton_horas

        ###################### EXIBIÇÃO DO BALANCEAMENTO ######################
        with coluna4_4:
                    
                    st.write('### Distribuição de calibres:')
                    import plotly.graph_objects as go
                    import plotly.express as px
                    #b
                    dataset_33 = st.session_state_base_crua


                    def ajuste(dataset_33):
                            if dataset_33['Calibre'] == 4:
                                return percent_caliber_4
                            elif dataset_33['Calibre'] == 5:
                                return percent_caliber_5
                            elif dataset_33['Calibre'] == 6:
                                return percent_caliber_6
                            elif dataset_33['Calibre'] == 7:
                                return percent_caliber_7
                            elif dataset_33['Calibre'] == 8:
                                return percent_caliber_8
                            elif dataset_33['Calibre'] == 9:
                                return percent_caliber_9
                            elif dataset_33['Calibre'] == 10:
                                return percent_caliber_10
                            elif dataset_33['Calibre'] == 12:
                                return percent_caliber_12
                            elif dataset_33['Calibre'] == 14:
                                return percent_caliber_14
                            elif dataset_33['Calibre'] == 16:
                                return percent_caliber_16

                    dataset_33['Percentual'] = dataset_33.apply(ajuste, axis = 1)

                    dataset_33 = dataset_33.sort_values(['Calibre'])
                    

                    dataset_33['Calibre Name'] = dataset_33['Calibre'].astype(str)
                    
                    c = round(dataset_33['Percentual'],2)
                    
                    def rename(dataset_33):
                        if dataset_33['Calibre Name'] == '0':
                            return 'Pequeno'
                        elif dataset_33['Calibre Name'] == '100':
                            return 'Grande'
                        else:
                            return dataset_33['Calibre Name']
                    dataset_33['Calibre Name'] = dataset_33.apply(rename, axis = 1) 
                    d = round(dataset_33['Percentual_RECENTE'],2)

                    
                    
                    fig = go.Figure()

                    fig.add_trace(go.Bar(x = dataset_33['Calibre Name'],y = dataset_33['Percentual'], text = c, name = 'Processado'))

                    fig.add_trace(go.Bar(x = dataset_33['Calibre Name'],y = dataset_33['Percentual_RECENTE'], text = d, name = 'Recente'))

                    fig.update_traces(textposition="outside",textfont_size=14, cliponaxis=False,textangle=0)
                    fig.update_layout(height = 550, width = 900,uniformtext_minsize=10)
                    #texttemplate='%{text:.3s}'
                    
                    st.plotly_chart(fig) 
        with coluna3_3:      

                    st.write('### Recomendação para balanceamento:')
                    st.markdown('       ')
                    st.markdown('       ')
                    st.markdown('       ')

                    equilibrio(corte_talo, embaladeira)

                    ton_horas = st.session_state.ton_horas

                    diference = str(round(((ton_horas - produtividade_atual)*100) / produtividade_atual ,2)) + ' ' + '%'
                    colunD.metric(label="Embaladeiras (t/h)", value = ton_horas, delta = diference) 

                    
                    caixas_total_controle = b['Caixas_total'].sum()
                
                    

                    caixas_total_processadas = st.session_state.cxs_process
                    cxs_recente_process = st.session_state.cxs_recentes 


                    caixas_restantes = caixas_total_controle - caixas_total_processadas
                    
                    caixotes_hora_time = st.session_state.caixotes_hora 
                    


                    mins = round(caixas_restantes * tempo_2 / cxs_recente_process )





                    caixas_total_processadas = round(caixas_total_processadas,2)
                    caixas_restantes = round(caixas_restantes,2)
                    mins = round(mins,2)



                    st.session_state.caixas_processadas = caixas_total_processadas
                    st.session_state.caixas_restantes = caixas_restantes
                    st.session_state.mins = mins



                    #st.write('#### Quantidade de caixas processadas:',caixas_total_processadas )
                    #st.write('#### Quantidade de caixas restantes:',caixas_restantes )
                    #st.write('#### Tempo restante (min) - Produtividade MAF:',mins )


                    # st.write('#### Quantidade de horas restantes com a capacidade Caixotes/Hora atual:', horas_restantes)
                    #caixas_total_controle
                    
            
        ###################### EXIBIÇÃO DO GRÁFICO DISTRIBUIÇÃO ######################
        with coluna2_2:
            st.write(" ")
            st.session_state.b = b
        


    elif pagina_selecionada == 'Linhas de embalagem':
        

        caixas_total_processadas = st.session_state.caixas_processadas
        caixas_restantes = st.session_state.caixas_restantes
        mins = st.session_state.mins

        # st.write('#### Quantidade de caixas processadas:',caixas_total_processadas )
        # st.write('#### Quantidade de caixas restantes:',caixas_restantes )
        # st.write('#### Tempo restante (min) - Produtividade MAF:',mins )





        caixotes_hora = st.session_state.caixotes_hora
        controle2 = st.session_state.controle
        ton_horas = st.session_state.ton_horas

    ######################## EXIBINDO MÉTRICAS CALCULADAS NA ABA ANTERIOR ########################

        col1, col2, col3, col4,col5,col6 = st.columns([0.5,1,1,1,1,1])
        col1.write("")
        col2.metric(label="Controle", value= controle2, delta= VARIEDADE)
        col6.metric(label="Caixotes/Hora", value= caixotes_hora, delta= None)
        
        

        col4.metric(label="MAF (t/h)", value= produtividade_atual) 

        diference = str(round(((ton_horas - produtividade_atual)*100) / produtividade_atual ,2)) + ' ' + '%'
        col5.metric(label="Embaladeiras (t/h)", value = ton_horas, delta = diference)


        tempo_2 = st.session_state_tempo
        col3.metric(label="Intervalo de tempo (min)", value= round(tempo_2,2))
    ###################### DIVISÃO DA TELA EM LINHAS E COLUNAS DE COLUNAS ######################

        col11,col22, col33 = st.columns([0.3,0.4,0.4])
        coluna1, coluna2 = st.columns(2)
    #    col1, col2 = st.columns([0.01,1])

    ###################### TRAZENDO VALORES DAS VARIAVEIS DA ABA ANTERIOR ######################

        Programa_input = st.session_state.periodo_safra
        caixotes = st.session_state.caixotes 
        embaladeira = st.session_state.embaladeira 
        variedade = st.session_state.variedade

        produtividade_embaladeira = st.session_state.produtividade_embaladeira
        produtividade_talo = st.session_state.produtividade_talo
        produtividade_limpeza = st.session_state.produtividade_limpeza 
        produtividade_limpeza2 = st.session_state.produtividade_selecao 

        calibre_4_papel = st.session_state.calibre4 
        calibre_5_papel = st.session_state.calibre5 
        calibre_6_papel = st.session_state.calibre6 
        calibre_7_papel = st.session_state.calibre7 
        calibre_8_papel = st.session_state.calibre8 
        calibre_9_papel = st.session_state.calibre9 
        calibre_10_papel = st.session_state.calibre10
        calibre_12_papel = st.session_state.calibre12
        calibre_14_papel = st.session_state.calibre14


        percent_caliber_4 = st.session_state_percent_4
        percent_caliber_5 = st.session_state_percent_5
        percent_caliber_6 = st.session_state_percent_6
        percent_caliber_7 = st.session_state_percent_7
        percent_caliber_8 = st.session_state_percent_8
        percent_caliber_9 = st.session_state_percent_9
        percent_caliber_10 = st.session_state_percent_10
        percent_caliber_12 = st.session_state_percent_12
        percent_caliber_14 = st.session_state_percent_14
        percent_caliber_16 = st.session_state_percent_16

    ###################### ATRIBUINDO OS PERCENTUAIS PARA A 2º ABA ######################
        
        def ajuste(b):
            if b['Calibre'] == 4:
                return percent_caliber_4
            elif b['Calibre'] == 5:
                return percent_caliber_5
            elif b['Calibre'] == 6:
                return percent_caliber_6
            elif b['Calibre'] == 7:
                return percent_caliber_7
            elif b['Calibre'] == 8:
                return percent_caliber_8
            elif b['Calibre'] == 9:
                return percent_caliber_9
            elif b['Calibre'] == 10:
                return percent_caliber_10
            elif b['Calibre'] == 12:
                return percent_caliber_12
            elif b['Calibre'] == 14:
                return percent_caliber_14
            elif b['Calibre'] == 16:
                return percent_caliber_16
        b['Percentual'] = b.apply(ajuste, axis = 1)

    ###################### ATRIBUINDO OS RIMOS PARA A 2º ABA ######################

        def ritmo(b):
                ########################################### RITMO PALMER ##########################################

                if (b['Calibre'] == 5 and variedade == 'Palmer') and (calibre_4_papel == 'Com' or calibre_4_papel == 'Sem'):
                    return 229
                elif (b['Calibre'] == 4 and variedade == 'Palmer') and (calibre_5_papel == 'Com' or calibre_5_papel == 'Sem'):
                    return 229
                elif (b['Calibre'] == 6 and variedade == 'Palmer') and (calibre_6_papel == 'Com' or calibre_6_papel == 'Sem'):
                    return 169
                elif (b['Calibre'] == 7 and variedade == 'Palmer') and (calibre_7_papel == 'Com' or calibre_7_papel == 'Sem'):
                    return 174
                elif (b['Calibre'] == 8 and variedade == 'Palmer') and (calibre_8_papel == 'Com' or calibre_8_papel == 'Sem'):
                    return 191
                elif (b['Calibre'] == 9 and variedade == 'Palmer') and (calibre_9_papel == 'Com' or calibre_9_papel == 'Sem'):
                    return 157
                elif (b['Calibre'] == 10 and variedade == 'Palmer') and (calibre_10_papel == 'Com' or calibre_10_papel == 'Sem'):
                    return 139
                elif (b['Calibre'] == 12 and variedade == 'Palmer') and (calibre_12_papel == 'Com' or calibre_12_papel == 'Sem'):
                    return 149
                elif (b['Calibre'] == 14 and variedade == 'Palmer') and (calibre_14_papel == 'Com' or calibre_14_papel == 'Sem'):
                    return 85

                ########################################### RITMO KEITT SEM PAPEL ##########################################

                elif (b['Calibre'] == 5 and calibre_5_papel == 'Sem') and (variedade == 'Keitt' or variedade == 'Omer'):
                    return 517
                elif (b['Calibre'] == 4  and calibre_4_papel == 'Sem') and (variedade == 'Keitt' or variedade == 'Omer'):
                    return 517
                elif (b['Calibre'] == 6 and calibre_6_papel == 'Sem') and (variedade == 'Keitt' or variedade == 'Omer'):
                    return 412
                elif (b['Calibre'] == 7 and calibre_7_papel == 'Sem') and (variedade == 'Keitt' or variedade == 'Omer') :
                    return 321
                elif (b['Calibre'] == 8  and calibre_8_papel == 'Sem') and (variedade == 'Keitt' or variedade == 'Omer'):
                    return 301
                elif (b['Calibre'] == 9 and calibre_9_papel == 'Sem') and (variedade == 'Keitt' or variedade == 'Omer'):
                    return 257
                elif (b['Calibre'] == 10  and calibre_10_papel == 'Sem') and (variedade == 'Keitt' or variedade == 'Omer'):
                    return 261
                elif (b['Calibre'] == 12 and calibre_12_papel == 'Sem') and  (variedade == 'Keitt' or variedade == 'Omer'):
                    return 253
                elif (b['Calibre'] == 14  and calibre_14_papel == 'Sem') and (variedade == 'Keitt' or variedade == 'Omer'):
                    return 220

                elif (b['Calibre'] == 5 and calibre_5_papel == 'Com') and (variedade == 'Keitt' or variedade == 'Omer'):
                    return 235
                elif (b['Calibre'] == 4 and calibre_4_papel == 'Com') and (variedade == 'Keitt' or variedade == 'Omer'):
                    return 235
                elif (b['Calibre'] == 6  and calibre_6_papel == 'Com') and (variedade == 'Keitt' or variedade == 'Omer'):
                    return 178
                elif (b['Calibre'] == 7 and calibre_7_papel == 'Com') and (variedade == 'Keitt' or variedade == 'Omer'):
                    return 185
                elif (b['Calibre'] == 8 and calibre_8_papel == 'Com') and (variedade == 'Keitt' or variedade == 'Omer'):
                    return 195
                elif (b['Calibre'] == 9  and calibre_9_papel == 'Com') and (variedade == 'Keitt' or variedade == 'Omer'):
                    return 154
                elif (b['Calibre'] == 10 and calibre_10_papel == 'Com') and (variedade == 'Keitt' or variedade == 'Omer'):
                    return 144
                elif (b['Calibre'] == 12 and calibre_12_papel == 'Com') and (variedade == 'Keitt' or variedade == 'Omer'):
                    return 158
                elif (b['Calibre'] == 14 and calibre_14_papel == 'Com') and (variedade == 'Keitt' or variedade == 'Omer'):
                    return 90

                ########################################### RITMO KENT SEM PAPEL ##########################################
        

                elif (b['Calibre'] == 5 and variedade == 'Kent') and (calibre_5_papel == 'Sem'):
                    return 510
                elif (b['Calibre'] == 6 and variedade == 'Kent') and (calibre_6_papel == 'Sem'):
                    return 410
                elif (b['Calibre'] == 7 and variedade == 'Kent') and (calibre_7_papel == 'Sem'):
                    return 314
                elif (b['Calibre'] == 8 and variedade == 'Kent') and (calibre_8_papel == 'Sem'):
                    return 300
                elif (b['Calibre'] == 9 and variedade == 'Kent') and (calibre_9_papel == 'Sem'):
                    return 253
                elif (b['Calibre'] == 10 and variedade == 'Kent') and (calibre_10_papel == 'Sem'):
                    return 248
                elif (b['Calibre'] == 12 and variedade == 'Kent') and (calibre_12_papel == 'Sem'):
                    return 246
                elif (b['Calibre'] == 14 and variedade == 'Kent') and (calibre_14_papel == 'Sem'):
                    return 200

                ########################################### RITMO KENT COM PAPEL ##########################################

                elif (b['Calibre'] == 5 and variedade == 'Kent') and (calibre_5_papel == 'Com'):
                    return 235
                elif (b['Calibre'] == 6 and variedade == 'Kent') and (calibre_6_papel == 'Com'):
                    return 178
                elif (b['Calibre'] == 7 and variedade == 'Kent') and (calibre_7_papel == 'Com'):
                    return 185
                elif (b['Calibre'] == 8 and variedade == 'Kent') and (calibre_8_papel == 'Com'):
                    return 195
                elif (b['Calibre'] == 9 and variedade == 'Kent') and (calibre_9_papel == 'Com'):
                    return 154
                elif (b['Calibre'] == 10 and variedade == 'Kent') and (calibre_10_papel == 'Com'):
                    return 144
                elif (b['Calibre'] == 12 and variedade == 'Kent') and (calibre_12_papel == 'Com'):
                    return 158
                elif (b['Calibre'] == 14 and variedade == 'Kent') and (calibre_14_papel == 'Com'):
                    return 90

                ########################################### RITMO TOMMY ##########################################

                elif (b['Calibre'] == 5 and variedade == 'Tommy Atkins') and (calibre_5_papel == 'Com' or calibre_5_papel == 'Sem'):
                    return 235
                elif (b['Calibre'] == 6 and variedade == 'Tommy Atkins') and (calibre_6_papel == 'Com' or calibre_6_papel == 'Sem'):
                    return 178
                elif (b['Calibre'] == 7 and variedade == 'Tommy Atkins') and (calibre_7_papel == 'Com' or calibre_7_papel == 'Sem'):
                    return 185
                elif (b['Calibre'] == 8 and variedade == 'Tommy Atkins') and (calibre_8_papel == 'Com' or calibre_8_papel == 'Sem'):
                    return 195
                elif (b['Calibre'] == 9 and variedade == 'Tommy Atkins') and (calibre_9_papel == 'Com' or calibre_9_papel == 'Sem'):
                    return 154
                elif (b['Calibre'] == 10 and variedade == 'Tommy Atkins') and (calibre_10_papel == 'Com' or calibre_10_papel == 'Sem'):
                    return 144
                elif (b['Calibre'] == 12 and variedade == 'Tommy Atkins') and (calibre_12_papel == 'Com' or calibre_12_papel == 'Sem'):
                    return 158
                elif (b['Calibre'] == 14 and variedade == 'Tommy Atkins') and (calibre_14_papel == 'Com' or calibre_14_papel == 'Sem'):
                    return 90
                else:
                    return 'NADA'
        b['Ritmo'] = b.apply(ritmo, axis = 1)
        
        filtro_ritmo = b['Ritmo'] != 'NADA'
        b = b[filtro_ritmo]
            
        col1, col2,col3,col4 = st.columns([0.1,1,0.1,1])
        
    ################################ CÁCULO DE CAIXAS 2º ABA ##########################################

        b['Caixas_total'] = ((caixotes * avg_frutos_caixotes * b['Percentual']) / b['Calibre']) / 100
        b['Caixas_1'] = ((caixotes * avg_frutos_caixotes * (b['Percentual']/100) * primeira_percent) / b['Calibre']) 
        b['Caixas_2'] = ((caixotes * avg_frutos_caixotes * (b['Percentual']/100) * segunda_percent)  / b['Calibre']) 
        b['Caixas_3'] = ((caixotes * avg_frutos_caixotes * (b['Percentual']/100) * terceira_percent) / b['Calibre']) 
        b['Horas_4kg'] = (b['Caixas_total'] / b['Ritmo']) / produtividade_embaladeira    
        

    ################################ BALANCEAMENTO  2º ABA ##########################################

        ritmo_embaladeira = ((b['Horas_4kg'].sum()  / embaladeira) * (1/24))
        corte_talo = round((caixotes * avg_frutos_caixotes) / (101303.19 * produtividade_talo * ritmo_embaladeira))
        ritmo_talo = ((((caixotes * avg_frutos_caixotes) / corte_talo) / (4200 * produtividade_talo)) * (1/24))
        diferenca_aceitavel = abs(round((ritmo_embaladeira - ritmo_talo),3))
        corte_talo2 = corte_talo
        ritmo_talo_2 = ((((caixotes * avg_frutos_caixotes) / corte_talo2) / (4200 * produtividade_talo)) * (1/24))
        

    ################################ FUNÇÃO BALANCEAMENTO 2º ABA ##########################################

        def equilibrio(corte_talo, embaladeira):


            caixotes_hora = round((caixotes*0.0416667)/(ritmo_talo_2))
            soma = segunda_percent + terceira_percent + refugo_percent
            selecao_ = round((caixotes_hora * avg_frutos_caixotes * soma / (3501 * produtividade_limpeza2)) + (caixotes_hora * avg_frutos_caixotes * primeira_percent / (6480 * produtividade_limpeza2)))

            st.write("A quantidade ideal de pessoas no talo tem que ser:", corte_talo2)
            st.write('Capacidade de caixotes/hora no corte de talo é de:', caixotes_hora)
            st.write('Capacidade de Toneladas/Horas é de:', round(((b['Caixas_total'].sum()*4.05)/1000)/(b['Horas_4kg'].sum()/embaladeira),2))

            Limpeza_selecao = round((caixotes_hora * avg_frutos_caixotes * 0.6) / (3230 * produtividade_limpeza))

            st.write('Quantidade de pessoas na limpeza:', Limpeza_selecao)
            st.write('Quantidade de pessoas na selelao:', selecao_)
                
            

    ########################################### LAYOUT LINHAS DE EMBALAGEM ###########################################

        Layout_linha = pd.DataFrame({"Linha":['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22'],
                                    "Calibre":"",
                                    "Qualidade":"",
                                    "Calibre2":"",
                                    "Qualidade2":"",
                                    "Auxiliar":"",
                                    "Auxiliar2":"",
                                    "Frutos":"",
                                    "Frutos2":"",
                                    "Caixas":"",
                                    "Caixas2":"",
                                    "Horas":"",
                                    "Embaladeiras":"",
                                    "Paletizadores":""}) 
        
        def preenchendo_calibre(Layout_linha):
        ########################################################## PALMER ############################################################################

            if (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '1') and (variedade == 'Palmer'):
                return 'Refugo'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '2') and (variedade == 'Palmer'):
                return 'Refugo'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '3') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '4') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '5') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '6') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '7') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '8') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '9') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '10') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '11') and (variedade == 'Palmer'):
                return '6'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '12') and (variedade == 'Palmer'):
                return '12'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '13') and (variedade == 'Palmer'):
                return '6'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '14') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '15') and (variedade == 'Palmer'):
                return '8'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '16') and (variedade == 'Palmer'):
                return '8'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '17') and (variedade == 'Palmer'):
                return '10'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '18') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '19') and (variedade == 'Palmer'):
                return '7'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '20') and (variedade == 'Palmer'):
                return '7'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '21') and (variedade == 'Palmer'):
                return '5'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '22') and (variedade == 'Palmer'):
                return '5'

    ########################################################## TOMMY ############################################################################

            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '1') and (variedade == 'Tommy Atkins'):
                return 'Refugo'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '2') and (variedade == 'Tommy Atkins'):
                return 'Refugo'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '3') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '4') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '5') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '6') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '7') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '8') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '9') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '10') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '11') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '12') and (variedade == 'Tommy Atkins'):
                return '10'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '13') and (variedade == 'Tommy Atkins'):
                return '10'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '14') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '15') and (variedade == 'Tommy Atkins'):
                return '9'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '16') and (variedade == 'Tommy Atkins'):
                return '9'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '17') and (variedade == 'Tommy Atkins'):
                return '12'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '18') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '19') and (variedade == 'Tommy Atkins'):
                return '8'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '20') and (variedade == 'Tommy Atkins'):
                return '8'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '21') and (variedade == 'Tommy Atkins'):
                return '7'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '22') and (variedade == 'Tommy Atkins'):
                return '7'

    ############################################################### KENT E KEITT ###############################################################

            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Kent' or variedade == 'Keitt'  or variedade == 'Omer'):
                return 'Refugo'
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return 'Refugo'
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '4') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '6') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '9') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return 'Aéreo'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '10') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return 'Aéreo'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '11') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '12') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '6'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '13') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '6'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '14') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '15') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '8'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '16') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '8'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '17') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '18') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '7'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '19') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '7'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '20') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '21') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '9'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '22') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '9'
    ################################################### PERIODO DE SAFRA ##################################################################################################
    ################################################### PALMER ##################################################################################################

            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return 'Refugo'
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return 'Refugo'
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return '14'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '4') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return '14'
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return '6'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '6') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return '6'
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '9') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return '9'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '10') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return '9'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '11') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return '7'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '12') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return '7'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '13') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '14') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return '10'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '15') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return '10'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '16') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '17') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return '12'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '18') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return '12'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '19') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '20') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '21') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return '8'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '22') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return '8'

    ############################################################### KENT E KEITT ###############################################################
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return 'Refugo'
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return 'Refugo'
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '14'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '4') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '14'
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '10'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '6') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '10'
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '9') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '9'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '10') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '9'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '11') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '12') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '6'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '13') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '14') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '8'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '15') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '8'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '16') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '17') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '7'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '18') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '7'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '19') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '20') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '21') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '12'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '22') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '12'

            else:
                return 'NADA'

        Layout_linha['Calibre'] = Layout_linha.apply(preenchendo_calibre, axis = 1)

        def preenchendo_qualidade(Layout_linha):

        ########################################### PALMER ###########################################

            if (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '4') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '6') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '9') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '10') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '11') and (variedade == 'Palmer'):
                return '1'
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '12') and (variedade == 'Palmer'):
                return '1'
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '13') and (variedade == 'Palmer'):
                return '2'
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '14') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '15') and (variedade == 'Palmer'):
                return '1'
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '16') and (variedade == 'Palmer'):
                return '2'
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '17') and (variedade == 'Palmer'):
                return '1'
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '18') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '19') and (variedade == 'Palmer'):
                return '2'
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '20') and (variedade == 'Palmer'):
                return '1'
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '21') and (variedade == 'Palmer'):
                return '1'
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '22') and (variedade == 'Palmer'):
                return '2'
            ####################################################### TOMMY ATKINS #############################################################

            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '4') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '6') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '9') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '10') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '11') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '12') and (variedade == 'Tommy Atkins'):
                return '1'
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '13') and (variedade == 'Tommy Atkins'):
                return '2'
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '14') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '15') and (variedade == 'Tommy Atkins'):
                return '1'
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '16') and (variedade == 'Tommy Atkins'):
                return '2'
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '17') and (variedade == 'Tommy Atkins'):
                return '1'
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '18') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '19') and (variedade == 'Tommy Atkins'):
                return '2'
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '20') and (variedade == 'Tommy Atkins'):
                return '1'
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '21') and (variedade == 'Tommy Atkins'):
                return '1'
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '22') and (variedade == 'Tommy Atkins'):
                return '2'
    ############################################################### KENT E KEITT ###############################################################

            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '4') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '6') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '9') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '10') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '11') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '12') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '1'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '13') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '2'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '14') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '15') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '1'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '16') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '2'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '17') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '18') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '1'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '19') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '2'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '20') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '21') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '1'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '22') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '2'

            ################################################### PERIODO DE SAFRA ##################################################################################################

            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return 'Refugo'
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return 'Refugo'
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return '2'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '4') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return '1'
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return '2'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '6') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return '1'
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '9') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return '1'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '10') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return '2'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '11') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return '2'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '12') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return '1'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '13') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '14') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return '2'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '15') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return '1'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '16') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '17') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return '2'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '18') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return '1'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '19') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '20') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '21') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return '1'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '22') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return '2'
    ############################################################### KENT E KEITT ###############################################################
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '2'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '4') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '1'
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '2'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '6') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '1'
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '9') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '1'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '10') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '2'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '11') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '12') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '1'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '13') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '14') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '2'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '15') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '1'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '16') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '17') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '2'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '18') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '1'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '19') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '20') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '21') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '1'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '22') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '2'

            else:
                return 'NADA'

        Layout_linha['Qualidade'] = Layout_linha.apply(preenchendo_qualidade, axis = 1)

        def preenchendo_calibre2(Layout_linha):
        ########################################### PALMER ###########################################

            if (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '4') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '6') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '9') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '10') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '11') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '12') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '13') and (variedade == 'Palmer'):
                return '12'
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '14') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '15') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '16') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '17') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '18') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '19') and (variedade == 'Palmer'):
                return '10'
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '20') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '21') and (variedade == 'Palmer'):
                return '9'
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '22') and (variedade == 'Palmer'):
                return '9'

    ################################################ TOMMY ATKINS ################################################

            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '4') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '6') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '9') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '10') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '11') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '12') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '13') and (variedade == 'Tommy Atkins'):
                return '6'
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '14') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '15') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '16') and (variedade == 'Tommy Atkins'):
                return '12'
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '17') and (variedade == 'Tommy Atkins'):
                return '6'
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '18') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '19') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '20') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '21') and (variedade == 'Tommy Atkins'):
                return '14'
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '22') and (variedade == 'Tommy Atkins'):
                return '14'

    ############################################################### KENT E KEITT ###############################################################

            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '4') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '6') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '9') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '10') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '11') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '12') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '16'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '13') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '14') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '15') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '12'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '16') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '12'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '17') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '18') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '10'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '19') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '10'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '20') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '21') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '5'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '22') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '5'
            ################################################### PERIODO DE SAFRA ##################################################################################################
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return '5'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '4') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return '5'
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '6') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '9') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '10') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '11') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '12') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '13') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '14') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '15') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '16') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '17') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '18') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '19') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '20') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '21') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '22') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
    ############################################################### KENT E KEITT ###############################################################
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '4') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '6') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '9') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '10') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '11') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '12') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '16'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '13') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '14') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '6'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '15') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '16') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '17') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '18') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '19') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '20') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '21') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '5'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '22') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '5'


            else:
                return 'NADA'

        Layout_linha['Calibre2'] = Layout_linha.apply(preenchendo_calibre2, axis = 1)

        def preenchendo_qualidade2(Layout_linha):
        ########################################### PALMER ###########################################

            if (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '4') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '6') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '9') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '10') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '11') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '12') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '13') and (variedade == 'Palmer'):
                return '2'
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '14') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '15') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '16') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '17') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '18') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '19') and (variedade == 'Palmer'):
                return '2'
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '20') and (variedade == 'Palmer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '21') and (variedade == 'Palmer'):
                return '1'
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '22') and (variedade == 'Palmer'):
                return '2'
    #################################################### TOMMY ATKINS ########################################3

            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '4') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '6') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '9') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '10') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '11') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '12') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '13') and (variedade == 'Tommy Atkins'):
                return '2'
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '14') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '15') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '16') and (variedade == 'Tommy Atkins'):
                return '2'
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '17') and (variedade == 'Tommy Atkins'):
                return '1'
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '18') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '19') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '20') and (variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '21') and (variedade == 'Tommy Atkins'):
                return '1'
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '22') and (variedade == 'Tommy Atkins'):
                return '2'

    ############################################################### KENT E KEITT ###############################################################
        
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '4') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '6') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '9') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '10') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '11') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '12') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '1'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '13') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '14') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '15') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '1'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '16') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '2'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '17') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '18') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '1'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '19') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '2'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '20') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '21') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '1'
            elif (Programa_input == 'Entre Safra' and Layout_linha['Linha'] == '22') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '2'
    ################################################### PERIODO DE SAFRA ##################################################################################################

            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return '2'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '4') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return '1'
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '6') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '9') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '10') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '11') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '12') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '13') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '14') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '15') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '16') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '17') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '18') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '19') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '20') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '21') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '22') and (variedade == 'Palmer' or variedade == 'Tommy Atkins'):
                return ''
    ############################################################### KENT E KEITT ###############################################################

            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '1') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '2') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '3') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '4') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '5') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '6') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '7') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra'and Layout_linha['Linha'] == '8') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '9') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '10') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '11') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '12') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '1'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '13') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '14') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '2'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '15') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '16') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '17') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '2'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '18') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '1'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '19') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '20') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return ''
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '21') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '1'
            elif (Programa_input == 'Safra' and Layout_linha['Linha'] == '22') and (variedade == 'Kent' or variedade == 'Keitt' or variedade == 'Omer'):
                return '2'

            else:
                return 'NADA'

        Layout_linha['Qualidade2'] = Layout_linha.apply(preenchendo_qualidade2, axis = 1)

        Layout_linha['Auxiliar'] = Layout_linha['Calibre'] + Layout_linha['Qualidade']
        Layout_linha['Auxiliar2'] = Layout_linha['Calibre2'] + Layout_linha['Qualidade2']


        b['Calibre'] = b['Calibre'].astype(str)
        
        quality['Qualidade']= quality['Qualidade'].astype(str)

        
        def rename_b (b):
            if b['Calibre'] == '4.0' or b['Calibre'] == '4':
                return '4'
            elif b['Calibre'] == '5.0' or b['Calibre'] == '5':
                return '5'
            elif b['Calibre'] == '6.0' or b['Calibre'] == '6':
                return '6'
            elif b['Calibre'] == '7.0' or b['Calibre'] == '7':
                return '7'
            elif b['Calibre'] == '8.0' or b['Calibre'] == '8':
                return '8'
            elif b['Calibre'] == '9.0' or b['Calibre'] == '9':
                return '9'
            elif b['Calibre'] == '10.0' or b['Calibre'] == '10':
                return '10'
            elif b['Calibre'] == '12.0' or b['Calibre'] == '12':
                return '12'
            elif b['Calibre'] == '14.0' or b['Calibre'] == '14':
                return '14'
        b['Calibre'] = b.apply(rename_b, axis = 1)
        
            
    ##################################### CALCULO DA QUANTIDADE DE FRUTOS POR LINHA ################################################################

        Layout_linha_2 = pd.merge(Layout_linha, quality, on = 'Qualidade', how = 'left')
        Layout_linha_2.rename(columns={'Percent':'P_Quali_1'}, inplace = True)

        Layout_linha_3 = pd.merge(Layout_linha_2, quality, left_on = 'Qualidade2',right_on = 'Qualidade', how = 'left')
        Layout_linha_3.rename(columns={'Percent':'P_Quali_2'}, inplace = True)
        Layout_linha_3 = Layout_linha_3.drop(columns = ['Qualidade_y'])
        

        Layout_linha_4 = pd.merge(Layout_linha_3, b[['Calibre','Percentual']], left_on = 'Calibre', right_on = 'Calibre', how = 'left')
        Layout_linha_4.rename(columns={'Percentual':'P_cal_1'}, inplace = True)

        

        Layout_linha_5 = pd.merge(Layout_linha_4, b[['Calibre','Percentual']], left_on = 'Calibre2', right_on = 'Calibre', how = 'left')
        Layout_linha_5.rename(columns={'Percentual':'P_cal_2'}, inplace = True)
        
        
        Layout_linha_5 = Layout_linha_5.drop(columns = ['Calibre_y'])
        Layout_linha_5.rename(columns = {'Calibre_x':'Calibre','Qualidade_x':'Qualidade'}, inplace = True)
        
        Layout_linha_5['Frutos'] = (caixotes * avg_frutos_caixotes) * Layout_linha_5['P_cal_1'] * (Layout_linha_5['P_Quali_1']/100)
        Layout_linha_5['Frutos2'] = (caixotes * avg_frutos_caixotes) * Layout_linha_5['P_cal_2'] * (Layout_linha_5['P_Quali_2']/100)


    ##################################### CALCULO DE CAIXAS POR LINHAS ################################################################

        Layout_linha_5['Calibre'] = Layout_linha_5['Calibre'].replace("Refugo","1")
        Layout_linha_5['Calibre'] = Layout_linha_5['Calibre'].replace("Aéreo","2")

        Layout_linha_5['Calibre'] = Layout_linha_5['Calibre'].replace("","1")

        Layout_linha_5['Calibre2'] = Layout_linha_5['Calibre2'].replace("","1")
        

        Layout_linha_5['Calibre'] = Layout_linha_5['Calibre'].astype(float)
        Layout_linha_5['Calibre2'] = Layout_linha_5['Calibre2'].astype(float)

        Layout_linha_5['Caixas'] = Layout_linha_5['Frutos'] / Layout_linha_5['Calibre']
        Layout_linha_5['Caixas2'] = Layout_linha_5['Frutos2'] / Layout_linha_5['Calibre2']

        ##################################### CALCULO DE HORAS POR LINHA ################################################################

        b['Calibre'] = b['Calibre'].astype(float)

        Layout_linha_6 = pd.merge(Layout_linha_5, b[['Calibre','Ritmo']], left_on = 'Calibre', right_on = 'Calibre', how = 'left')
        Layout_linha_6.rename(columns={'Ritmo':'Ritmo_1'}, inplace = True)
        
        Layout_linha_7 = pd.merge(Layout_linha_6, b[['Calibre','Ritmo']], left_on = 'Calibre2', right_on = 'Calibre', how = 'left')
        Layout_linha_7 = Layout_linha_7.drop(columns = ['Calibre_y'])
        Layout_linha_7.rename(columns = {'Ritmo':'Ritmo_2','Calibre_x':'Calibre'}, inplace = True) 

        Layout_linha_7['Horas_1'] = (Layout_linha_7['Caixas'] / Layout_linha_7['Ritmo_1'])
        Layout_linha_7['Horas_1'].fillna(0, inplace = True)

        Layout_linha_7['Horas_2'] = (Layout_linha_7['Caixas2'] / Layout_linha_7['Ritmo_2'])
        Layout_linha_7['Horas_2'].fillna(0, inplace = True)

        Layout_linha_7['Horas'] = Layout_linha_7['Horas_1'] + Layout_linha_7['Horas_2']

        ##################################### CALCULO DE EMBALADEIRAS POR LINHA ################################################################


        Layout_linha_7['Embaladeiras'] = round((embaladeira * Layout_linha_7['Horas']) / Layout_linha_7['Horas'].sum(),1)
        Layout_linha_7['Embaladeiras_1'] = round((embaladeira * Layout_linha_7['Horas_1']) / Layout_linha_7['Horas'].sum(),1)
        Layout_linha_7['Embaladeiras_2'] = round((embaladeira * Layout_linha_7['Horas_2']) / Layout_linha_7['Horas'].sum(),1)
        

    ############################## CÁLCULO DE EMBALADEIRAS POR SETORES ###############################

        def setores(Layout_linha_7):
            if Layout_linha_7['Linha'] == '1' or Layout_linha_7['Linha'] == '2':
                return 1
            elif Layout_linha_7['Linha'] == '3' or Layout_linha_7['Linha'] == '4' or Layout_linha_7['Linha'] == '5' or Layout_linha_7['Linha'] == '6':
                return 2
            elif Layout_linha_7['Linha'] == '7' or Layout_linha_7['Linha'] == '8' or Layout_linha_7['Linha'] == '9' or Layout_linha_7['Linha'] == '10':
                return 3
            elif Layout_linha_7['Linha'] == '11' or Layout_linha_7['Linha'] == '12' or Layout_linha_7['Linha'] == '13' or Layout_linha_7['Linha'] == '14':
                return 4
            elif Layout_linha_7['Linha'] == '15' or Layout_linha_7['Linha'] == '16' or Layout_linha_7['Linha'] == '17' or Layout_linha_7['Linha'] == '18':
                return 5
            elif Layout_linha_7['Linha'] == '19' or Layout_linha_7['Linha'] == '20' or Layout_linha_7['Linha'] == '21' or Layout_linha_7['Linha'] == '22':
                return 6
            else:
                return 'NADA'

        Layout_linha_7['Setores'] = Layout_linha_7.apply(setores, axis = 1)
        Layout_linha_7['Setores'] = Layout_linha_7['Setores'].astype(str)

    ############################## EXIBIÇÃO DAS INFORMAÇÕES ##############################
        import plotly.express as px
        import plotly.graph_objects as go
        
        with col11:
            ############################## PIZZA DOS PERCENTUAIS ##############################
            st.write("")
            st.info('##### Percentuais de qualidade:')

            fig = go.Figure(data=[go.Pie(labels = quality['Qualidade'], values = quality['Percent'], marker_colors = px.colors.sequential.Emrld ,hole = .35, pull=0.025)])
            fig.update_traces(textinfo='label+percent', textfont_size=15, textposition="inside")
            fig.update_layout(height = 450, width = 450, font = dict(size = 15))

            st.plotly_chart(fig) 

        ############################## BARRA - EMBALADEIRAS POR SETOR ##############################
        with col22:
            
            st.write(" ")
            st.info('##### Quantidade de embaladeiras por setor:')

            df_setores = round(Layout_linha_7.groupby('Setores')['Embaladeiras'].sum(),2)
            df_setores = df_setores.reset_index()
            df_setores['Embaladeiras'] = round(df_setores['Embaladeiras'],0)

            fig2 = px.bar(df_setores, x = 'Setores', y = 'Embaladeiras', color = 'Setores', text= 'Embaladeiras', color_discrete_sequence= px.colors.sequential.Aggrnyl ) 
            fig2.update_layout(height = 450, width = 650, uniformtext_minsize = 8, uniformtext_mode = 'show', font = dict(size = 14))
            fig2.update_traces(textfont_size = 14, textangle = 0, textposition = 'outside', cliponaxis = False)

            st.plotly_chart(fig2)

        ############################## BARRA - EMBALADEIRAS POR LINHA ##############################
        with col33:

            st.write(" ")
            st.info('##### Quantidade de embaladeiras por linha:')
            
            fig = px.bar(Layout_linha_7, x = 'Linha', y = 'Embaladeiras', color = 'Setores', text = 'Embaladeiras',color_discrete_sequence= px.colors.sequential.Aggrnyl)
            fig.update_layout(height = 450, width = 650, uniformtext_minsize=8, uniformtext_mode='show', font = dict(size = 14))
            fig.update_traces(textfont_size=14, textangle=0, textposition="outside", cliponaxis=False)

            st.plotly_chart(fig)

        ############################## PLANILHA - DETALHES ##############################
        with col4:  

            st.info('##### Informações detalhadas das linhas de embalagem:')
            st.write('_______')

            Layout_linha_8 = Layout_linha_7[['Linha','Calibre','Qualidade','Calibre2','Qualidade2','Frutos','Frutos2','Caixas','Caixas2','Embaladeiras','Setores','Embaladeiras_1','Embaladeiras_2']]
            Layout_linha_8['Calibre'] = Layout_linha_8['Calibre'].astype(str)
            Layout_linha_8['Calibre'] = Layout_linha_8['Calibre'].replace('1.0',' ')
            Layout_linha_8  = Layout_linha_8.fillna(0)
            Layout_linha_8 = round(Layout_linha_8,1)
            Layout_linha_8 = Layout_linha_8.astype(str)
            Layout_linha_8 = Layout_linha_8.replace('0.0',' ')
            Layout_linha_8 = Layout_linha_8.replace('1.0',' ')

            Layout_linha_8
            Layout_linha_8.to_excel('Layout_final.xlsx')
            st.download_button( label = 'Baixar Configuração (csv)',data = Layout_linha_8.to_csv(), mime = 'text/csv')

        with col2:

            st.info('##### Caixas processadas X restantes:')
            st.write('#### Tempo (min) de finalização estimado:',mins )
            fig = go.Figure()

            fig.add_trace(go.Bar(y = [caixas_total_processadas], text = str(caixas_total_processadas), name = 'Processado', marker_color='rgb(169, 220, 103)'))

            fig.add_trace(go.Bar(y = [caixas_restantes], text = str(caixas_restantes), name = 'Restante', marker_color='rgb(253, 174, 107)'))

            fig.update_layout(height = 500, width = 800, font = dict(size = 14))
            fig.update_traces(textfont_size=14, textposition="inside")

            #fig.add_trace(go.Bar(x = caixas_restantes))
            st.plotly_chart(fig)
            

    elif pagina_selecionada == 'Distribuição embaladeiras':

        ###################### IMPORT VALORES DAS ABAS PASSADAS ######################
        import plotly.express as px

        embaladeira = st.session_state.embaladeira 
        produtividade_embaladeira = st.session_state.produtividade_embaladeira
        produtividade_talo = st.session_state.produtividade_talo
        
        b = st.session_state.b

        caixotes_hora = st.session_state.caixotes_hora
        controle2 = st.session_state.controle
        ton_horas = st.session_state.ton_horas


        ###################### EXIBIÇÃO DE MÉTRICAS ######################

        col1x, col2x, col3x, col4x,col5x,col6x = st.columns([1,1,1,1,1,1])
        #col3x.metric(label="Toneladas/Hora anterior", value= ton_horas, delta= None)
        #col1x.metric(label="Controle", value= controle2, delta= VARIEDADE)
        #col2x.metric(label="Caixotes/Hora", value= caixotes_hora, delta= None)
        


    ######################## EXIBINDO MÉTRICAS CALCULADAS NA ABA ANTERIOR ########################

        #col1, col2, col3, col4,col5,col6 = st.columns([1,1,1,1,1,1])
        #col1.write("")

        col1x.metric(label="Controle", value= controle2, delta= VARIEDADE)
        col6x.metric(label="Caixotes/Hora", value= caixotes_hora, delta= None)        
        

        col3x.metric(label="MAF (t/h)", value= produtividade_atual) 

        diference = str(round(((ton_horas - produtividade_atual)*100) / produtividade_atual ,2)) + ' ' + '%'

        col4x.metric(label="Embaladeiras (t/h)", value = ton_horas, delta = diference)


        tempo_2 = st.session_state_tempo
        col2x.metric(label="Intervalo de tempo (min)", value= round(tempo_2,2))



        ###################### LAYOUT PÁGINA  ######################
        variedade = st.session_state.variedade
    #    colunas1, colunas2 = st.columns([1,1])
        col1, col2, col3 = st.columns(3)
        colunas1, colunas2 = st.columns([1,0.1])
        

        with colunas1:
            st.success('### Recomendação de embaladeiras por calibre:')
        colu1, colu2, colu3, colu4  = st.columns(4)

        ########################## LAYOUT DAS LIHAS ##########################

        Layout_linha_9 = pd.read_excel('Layout_final.xlsx')
        
        Layout_linha_9 = Layout_linha_9.drop(columns = ['Unnamed: 0'])
        Layout_linha_9['Setores'] = Layout_linha_9['Setores'].astype(str)

        Layout_linha_9['Embaladeiras'] = Layout_linha_9['Embaladeiras'].replace(' ','0')
        Layout_linha_9['Embaladeiras'] = Layout_linha_9['Embaladeiras'].astype(float)

        Layout_linha_9['Embaladeiras_1'] = Layout_linha_9['Embaladeiras_1'].replace(' ','0')
        Layout_linha_9['Embaladeiras_1'] = Layout_linha_9['Embaladeiras_1'].astype(float)

        Layout_linha_9['Embaladeiras_2'] = Layout_linha_9['Embaladeiras_2'].replace(' ','0')
        Layout_linha_9['Embaladeiras_2'] = Layout_linha_9['Embaladeiras_2'].astype(float)

    ##################################### DATASET EMBALADEIRAS #######################################################################

        padrao_embaldeiras['PESSOA'] = padrao_embaldeiras['PESSOA'].str[6:]
        
    ##################################### CORREÇÃO VARIEDADE DATASET DAS EMBALADEIRAS #######################################################################

        def correcao_variedade(padrao_embaldeiras):
            if padrao_embaldeiras['VARIEDADE'] == 'Tommy ':
                return 'Tommy Atkins'
            elif padrao_embaldeiras['VARIEDADE'] == 'Keitt ':
                return 'Keitt'
            else:
                return padrao_embaldeiras['VARIEDADE']

        padrao_embaldeiras['VARIEDADE'] = padrao_embaldeiras.apply(correcao_variedade, axis = 1)
        
        ################################# ESTRUTURAÇÃO PARA GRÁFICO DAS EMBALADEIRAS DE CADA CALIBRE ########################################

        def check_valores(Layout_linha_9, list_values):
            resultDict = {}
            for elem in list_values:
                if elem in Layout_linha_9['Calibre'] and variedade == 'Palmer':

                    resultDict[elem] = True

                    aaa = Layout_linha_9.groupby(['Calibre'])['Embaladeiras_1'].sum()
                    aaa = aaa.reset_index()
                

                    bbb = Layout_linha_9.groupby(['Calibre2'])['Embaladeiras_2'].sum()
                    bbb = bbb.reset_index()
                    bbb = bbb.rename(columns={'Calibre2':'Calibre', 'Embaladeiras_2':'Embaladeiras_1'})
            
                    ccc = pd.concat((aaa,bbb))
                    ccc['Calibre'] = ccc['Calibre'].replace(' ','0')
                    ccc['Calibre'] = ccc['Calibre'].astype(float)
                    ccc = ccc.groupby(['Calibre'])['Embaladeiras_1'].sum()
                    ccc = ccc.reset_index()
                    
                    if elem == 5.0:

                        filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Palmer'
                        padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                        filtro_calibre = padrao_embaldeiras['CALIBRE'] == 5
                        padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]

                        a = padrao_embaldeiras_palmer.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                        a = a.reset_index()
                        a['mean'] = round(a['mean'],0)
                        a = a.rename(columns = {'mean':'Caixas/Hora'})
                        a['Calibre'] = 5.0
                        a['Calibre'] = a['Calibre'].astype(str)
                        a['ID_PESSOA'] = a['ID_PESSOA'].astype(str)
                        media_a = a['Caixas/Hora'].mean()
                        st.session_state.media_a = media_a
                        aa = px.bar(a,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Palmer - Calibre 5',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )
                        aa.update_yaxes(range = [a['Caixas/Hora'].min()-10,a['Caixas/Hora'].max()])
                        aa.add_hline(229)
                        aa.update_layout(height = 350, width = 350)
                        

                    elif elem == 6.0:
                        
                        kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                        kl1 = round(kl1,0)

                        if kl1 == 0:
                            kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                        elif kl1 > 0: 
                            kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                            kl = kl.astype(int)

                        filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Palmer'
                        padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                        filtro_calibre = padrao_embaldeiras['CALIBRE'] == 6
                        padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                    

                        padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)
                        padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(a['ID_PESSOA'])]


                        b = padrao_embaldeiras_palmer_2.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                        b = b.reset_index()
                        b['mean'] = round(b['mean'],0)
                        b = b.rename(columns = {'mean':'Caixas/Hora'})
                        b['Calibre'] = 6.0
                        b['Calibre'] = b['Calibre'].astype(str)
                        b['ID_PESSOA'] = b['ID_PESSOA'].astype(str)
                        media_b = b['Caixas/Hora'].mean()
                        st.session_state.media_b = media_b
                        bb = px.bar(b,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Palmer - Calibre 6',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )
                        bb.update_yaxes(range = [b['Caixas/Hora'].min()-10,b['Caixas/Hora'].max()])
                        bb.add_hline(media_b, line_color="green")
                        bb.add_hline(169)
                        bb.update_layout(height = 350, width = 350)

                    elif elem == 7.0:
                        kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                        kl1 = round(kl1,0)

                        if kl1 == 0:
                            kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                        elif kl1 > 0: 
                            kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                            kl = kl.astype(int)
                        
                        filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Palmer'
                        padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                        filtro_calibre = padrao_embaldeiras['CALIBRE'] == 7
                        padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]

                        padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)
                        padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                        c = padrao_embaldeiras_palmer_3.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                        c = c.reset_index()
                        c['mean'] = round(c['mean'],0)
                        c = c.rename(columns = {'mean':'Caixas/Hora'})
                        c['Calibre'] = 7.0
                        c['Calibre'] = c['Calibre'].astype(str)
                        c['ID_PESSOA'] = c['ID_PESSOA'].astype(str)
                        media_c = c['Caixas/Hora'].mean()
                        st.session_state.media_c = media_c
                        cc = px.bar(c,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Palmer - Calibre 7',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )
                        cc.update_yaxes(range = [c['Caixas/Hora'].min()-10,c['Caixas/Hora'].max()])
                        cc.add_hline(174)
                        cc.update_layout(height = 350, width = 350)

                    elif elem == 8.0:
                        kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                        kl1 = round(kl1,0)

                        if kl1 == 0:
                            kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                        elif kl1 > 0: 
                            kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                            kl = kl.astype(int)

                        filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Palmer'
                        padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                        filtro_calibre = padrao_embaldeiras['CALIBRE'] == 8
                        padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]

                        padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)

                        padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_4 = padrao_embaldeiras_palmer_3[~padrao_embaldeiras_palmer_3.ID_PESSOA.isin(c['ID_PESSOA'])]

                        d = padrao_embaldeiras_palmer_4.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                        d = d.reset_index()
                        d['mean'] = round(d['mean'],0)
                        d = d.rename(columns = {'mean':'Caixas/Hora'})
                        d['Calibre'] = 8.0
                        d['Calibre'] = d['Calibre'].astype(str)
                        d['ID_PESSOA'] = d['ID_PESSOA'].astype(str)
                        media_d = d['Caixas/Hora'].mean()
                        st.session_state.media_d = media_d
                        dd = px.bar(d,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Palmer - Calibre 8',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )
                        dd.update_yaxes(range = [d['Caixas/Hora'].min()-10,d['Caixas/Hora'].max()])
                        dd.add_hline(189)
                        dd.update_layout(height = 350, width = 350)
                        

                    elif elem == 9.0:
                        kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                        kl1 = round(kl1,0)

                        if kl1 == 0:
                            kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                        elif kl1 > 0: 
                            kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0) 
                            kl = kl.astype(int)

                        filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Palmer'
                        padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                        filtro_calibre = padrao_embaldeiras['CALIBRE'] == 9
                        padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]

                        padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)

                        padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_4 = padrao_embaldeiras_palmer_3[~padrao_embaldeiras_palmer_3.ID_PESSOA.isin(c['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_5 = padrao_embaldeiras_palmer_4[~padrao_embaldeiras_palmer_4.ID_PESSOA.isin(d['ID_PESSOA'])]

                        
                        e = padrao_embaldeiras_palmer_5.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                        e = e.reset_index()
                        e['mean'] = round(e['mean'],0)
                        e = e.rename(columns = {'mean':'Caixas/Hora'})
                        e['Calibre'] = 9.0
                        e['Calibre'] = e['Calibre'].astype(str)
                        
                        media_e = e['Caixas/Hora'].mean()
                        st.session_state.media_e = media_e
                        ee = px.bar(e,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Palmer - Calibre 9',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )
                        ee.update_yaxes(range = [e['Caixas/Hora'].min()-10,e['Caixas/Hora'].max()])
                        ee.add_hline(157)
                        ee.update_layout(height = 350, width = 350)

                    elif elem == 10.0:

                        kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                        kl1 = round(kl1,0)

                        if kl1 == 0:
                            kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                        elif kl1 > 0: 
                            kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                            kl = kl.astype(int)
                        
                        filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Palmer'
                        padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                        filtro_calibre = padrao_embaldeiras['CALIBRE'] == 10
                        padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                        

                        padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)

                        padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_4 = padrao_embaldeiras_palmer_3[~padrao_embaldeiras_palmer_3.ID_PESSOA.isin(c['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_5 = padrao_embaldeiras_palmer_4[~padrao_embaldeiras_palmer_4.ID_PESSOA.isin(d['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_6 = padrao_embaldeiras_palmer_5[~padrao_embaldeiras_palmer_5.ID_PESSOA.isin(e['ID_PESSOA'])]

                        f = padrao_embaldeiras_palmer_6.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                        f = f.reset_index()
                        f['mean'] = round(f['mean'],0)
                        f = f.rename(columns = {'mean':'Caixas/Hora'})
                        f['Calibre'] = 10.0
                        f['Calibre'] = f['Calibre'].astype(str)
                        f['ID_PESSOA'] = f['ID_PESSOA'].astype(str)
                        media_f = f['Caixas/Hora'].mean()
                        st.session_state.media_f = media_f
                        ff = px.bar(f,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Palmer - Calibre 10', hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )
                        ff.update_yaxes(range = [f['Caixas/Hora'].min()-10,f['Caixas/Hora'].max()])
                        ff.add_hline(139)
                        ff.update_layout(height = 350, width = 350)
                        
                                    
                    elif elem == 12.0:

                        kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                        kl1 = round(kl1,0)

                        if kl1 == 0:
                            kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                        elif kl1 > 0: 
                            kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                            kl = kl.astype(int)

                        filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Palmer'
                        padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                        filtro_calibre = padrao_embaldeiras['CALIBRE'] == 12
                        padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                        
                        padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)

                        padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_4 = padrao_embaldeiras_palmer_3[~padrao_embaldeiras_palmer_3.ID_PESSOA.isin(c['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_5 = padrao_embaldeiras_palmer_4[~padrao_embaldeiras_palmer_4.ID_PESSOA.isin(d['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_6 = padrao_embaldeiras_palmer_5[~padrao_embaldeiras_palmer_5.ID_PESSOA.isin(e['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_7 = padrao_embaldeiras_palmer_6[~padrao_embaldeiras_palmer_6.ID_PESSOA.isin(f['ID_PESSOA'])]

                        g = padrao_embaldeiras_palmer_7.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                        g = g.reset_index()
                        g['mean'] = round(g['mean'],0)
                        g = g.rename(columns = {'mean':'Caixas/Hora'})
                        g['Calibre'] = 12.0
                        g['Calibre'] = g['Calibre'].astype(str)
                        g['ID_PESSOA'] = g['ID_PESSOA'].astype(str)
                        media_g = g['Caixas/Hora'].mean()
                        st.session_state.media_g = media_g
                        gg = px.bar(g,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Palmer - Calibre 12',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )
                        gg.update_yaxes(range = [g['Caixas/Hora'].min()-10,g['Caixas/Hora'].max()])
                        gg.add_hline(149)
                        gg.update_layout(height = 350, width = 350)
                    
                    elif elem == 14.0:

                        filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Palmer'
                        padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                        filtro_calibre = padrao_embaldeiras['CALIBRE'] == 14
                        padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                        
                        h = padrao_embaldeiras_palmer.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                        h = h.reset_index()
                        h['mean'] = round(h['mean'],0)
                        h = h.rename(columns = {'mean':'Caixas/Hora'})
                        h['Calibre'] = 14.0
                        h['Calibre'] = h['Calibre'].astype(str)
                        h['ID_PESSOA'] = h['ID_PESSOA'].astype(str)
                        media_h = h['Caixas/Hora'].mean()
                        st.session_state.media_h = media_h
                        hh = px.bar(h,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Palmer - Calibre 14',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )
                        hh.update_yaxes(range = [h['Caixas/Hora'].min()-10,h['Caixas/Hora'].max()])
                        hh.update_layout(height = 350, width = 350)

                elif elem in Layout_linha_9['Calibre'] and variedade == 'Kent':
                    resultDict[elem] = True
                    
                    aaa = Layout_linha_9.groupby(['Calibre'])['Embaladeiras_1'].sum()
                    aaa = aaa.reset_index()

                    bbb = Layout_linha_9.groupby(['Calibre2'])['Embaladeiras_2'].sum()
                    bbb = bbb.reset_index()
                    bbb = bbb.rename(columns={'Calibre2':'Calibre', 'Embaladeiras_2':'Embaladeiras_1'})

                    ccc = pd.concat((aaa,bbb))
                    ccc['Calibre'] = ccc['Calibre'].replace(' ','0')
                    ccc['Calibre'] = ccc['Calibre'].astype(float)
                    ccc = ccc.groupby(['Calibre'])['Embaladeiras_1'].sum()
                    ccc = ccc.reset_index()

                    if elem == 5.0:

                        filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Kent'
                        padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                        filtro_calibre = padrao_embaldeiras['CALIBRE'] == 5
                        padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                        
                        a = padrao_embaldeiras_palmer.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                        a = a.reset_index()
                        a['mean'] = round(a['mean'],0)
                        a = a.rename(columns = {'mean':'Caixas/Hora'})
                        a['Calibre'] = 5.0
                        a['Calibre'] = a['Calibre'].astype(str)
                        a['ID_PESSOA'] = a['ID_PESSOA'].astype(str)
                        aa = px.bar(a,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Kent - Calibre 5',hover_name = 'PESSOA', color_discrete_sequence= px.colors.sequential.Aggrnyl )
                        aa.update_yaxes(range = [a['Caixas/Hora'].min()-10,a['Caixas/Hora'].max()])
                        aa.update_layout(height = 350, width = 350)

                    elif elem == 6.0:
                        
                        kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                        kl1 = round(kl1,0)

                        if kl1 == 0:
                            kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                        elif kl1 > 0: 
                            kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                            kl = kl.astype(int)

                        filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Kent'
                        padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]
                        
                        filtro_calibre = padrao_embaldeiras['CALIBRE'] == 6
                        padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]

                        padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)
                        padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(a['ID_PESSOA'])]

                        b = padrao_embaldeiras_palmer_2.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                        b = b.reset_index()
                        b['mean'] = round(b['mean'],0)
                        b = b.rename(columns = {'mean':'Caixas/Hora'})
                        b['Calibre'] = 6.0
                        b['Calibre'] = b['Calibre'].astype(str)
                        b['ID_PESSOA'] = b['ID_PESSOA'].astype(str)
                        bb = px.bar(b,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Kent - Calibre 6',hover_name = 'PESSOA', color_discrete_sequence= px.colors.sequential.Aggrnyl )
                        bb.update_yaxes(range = [b['Caixas/Hora'].min()-10,b['Caixas/Hora'].max()])
                        bb.update_layout(height = 350, width = 350)

                    elif elem == 7.0:

                        kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                        kl1 = round(kl1,0)

                        if kl1 == 0:
                            kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                        elif kl1 > 0: 
                            kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                            kl = kl.astype(int)

                        filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Kent'
                        padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                        filtro_calibre = padrao_embaldeiras['CALIBRE'] == 7
                        padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]

                        padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)
                        padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                        c = padrao_embaldeiras_palmer_3.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                        c = c.reset_index()
                        c['mean'] = round(c['mean'],0)
                        c = c.rename(columns = {'mean':'Caixas/Hora'})
                        c['Calibre'] = 7.0
                        c['Calibre'] = c['Calibre'].astype(str)
                        c['ID_PESSOA'] = c['ID_PESSOA'].astype(str)
                        cc = px.bar(c,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Kent - Calibre 7', hover_name = 'PESSOA', color_discrete_sequence= px.colors.sequential.Aggrnyl)
                        cc.update_yaxes(range = [c['Caixas/Hora'].min()-10,c['Caixas/Hora'].max()])
                        cc.update_layout(height = 350, width = 350)
                    
                    elif elem == 8.0:
                        kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                        kl1 = round(kl1,0)

                        if kl1 == 0:
                            kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                        elif kl1 > 0: 
                            kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                            kl = kl.astype(int) 

                        filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Kent'
                        padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                        filtro_calibre = padrao_embaldeiras['CALIBRE'] == 8
                        padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                        padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)

                        padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_4 = padrao_embaldeiras_palmer_3[~padrao_embaldeiras_palmer_3.ID_PESSOA.isin(c['ID_PESSOA'])]


                        d = padrao_embaldeiras_palmer_4.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                        d = d.reset_index()
                        d['mean'] = round(d['mean'],0)
                        d = d.rename(columns = {'mean':'Caixas/Hora'})
                        d['Calibre'] = 8.0
                        d['Calibre'] = d['Calibre'].astype(str)
                        d['ID_PESSOA'] = d['ID_PESSOA'].astype(str)
                        dd = px.bar(d,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Kent - Calibre 8', hover_name = 'PESSOA', color_discrete_sequence= px.colors.sequential.Aggrnyl)
                        dd.update_yaxes(range = [d['Caixas/Hora'].min()-10,d['Caixas/Hora'].max()])
                        dd.update_layout(height = 350, width = 350)
                    
                    elif elem == 9.0:

                        kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                        kl1 = round(kl1,0)

                        if kl1 == 0:
                            kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                        elif kl1 > 0: 
                            kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                            kl = kl.astype(int)

                        filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Kent'
                        padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                        filtro_calibre = padrao_embaldeiras['CALIBRE'] == 9
                        padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                        padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)

                        padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_4 = padrao_embaldeiras_palmer_3[~padrao_embaldeiras_palmer_3.ID_PESSOA.isin(c['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_5 = padrao_embaldeiras_palmer_4[~padrao_embaldeiras_palmer_4.ID_PESSOA.isin(d['ID_PESSOA'])]

                        e = padrao_embaldeiras_palmer_5.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                        e = e.reset_index()
                        e['mean'] = round(e['mean'],0)
                        e = e.rename(columns = {'mean':'Caixas/Hora'})
                        e['Calibre'] = 9.0
                        e['Calibre'] = e['Calibre'].astype(str)
                        e['ID_PESSOA'] = e['ID_PESSOA'].astype(str)
                        ee = px.bar(e,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Kent - Calibre 9' ,hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl)
                        ee.update_yaxes(range = [e['Caixas/Hora'].min()-10,e['Caixas/Hora'].max()])
                        ee.update_layout(height = 350, width = 350)
                    
                    elif elem == 10.0:
                        kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                        kl1 = round(kl1,0)

                        if kl1 == 0:
                            kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                        elif kl1 > 0: 
                            kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                            kl = kl.astype(int)

                        filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Kent'
                        padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                        filtro_calibre = padrao_embaldeiras['CALIBRE'] == 10
                        padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]

                        padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)

                        padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_4 = padrao_embaldeiras_palmer_3[~padrao_embaldeiras_palmer_3.ID_PESSOA.isin(c['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_5 = padrao_embaldeiras_palmer_4[~padrao_embaldeiras_palmer_4.ID_PESSOA.isin(d['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_6 = padrao_embaldeiras_palmer_5[~padrao_embaldeiras_palmer_5.ID_PESSOA.isin(e['ID_PESSOA'])]

                        f = padrao_embaldeiras_palmer_6.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                        f = f.reset_index()
                        f['mean'] = round(f['mean'],0)
                        f = f.rename(columns = {'mean':'Caixas/Hora'})
                        f['Calibre'] = 10.0
                        f['Calibre'] = f['Calibre'].astype(str)
                        f['ID_PESSOA'] = f['ID_PESSOA'].astype(str)
                        ff = px.bar(f,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Kent - Calibre 10' ,hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl)
                        ff.update_yaxes(range = [f['Caixas/Hora'].min()-10,f['Caixas/Hora'].max()])
                        ff.update_layout(height = 350, width = 350)
                    
                    elif elem == 12.0:
                        kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                        kl1 = round(kl1,0)

                        if kl1 == 0:
                            kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                        elif kl1 > 0: 
                            kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                            kl = kl.astype(int)

                        filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Kent'
                        padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                        filtro_calibre = padrao_embaldeiras['CALIBRE'] == 12
                        padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                        padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)

                        padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_4 = padrao_embaldeiras_palmer_3[~padrao_embaldeiras_palmer_3.ID_PESSOA.isin(c['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_5 = padrao_embaldeiras_palmer_4[~padrao_embaldeiras_palmer_4.ID_PESSOA.isin(d['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_6 = padrao_embaldeiras_palmer_5[~padrao_embaldeiras_palmer_5.ID_PESSOA.isin(e['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_7 = padrao_embaldeiras_palmer_6[~padrao_embaldeiras_palmer_6.ID_PESSOA.isin(f['ID_PESSOA'])]

                        g = padrao_embaldeiras_palmer_7.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                        g = g.reset_index()
                        g['mean'] = round(g['mean'],0)
                        g = g.rename(columns = {'mean':'Caixas/Hora'})
                        g['Calibre'] = 12.0
                        g['Calibre'] = g['Calibre'].astype(str)
                        g['ID_PESSOA'] = g['ID_PESSOA'].astype(str)
                        gg = px.bar(g,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Kent - Calibre 12',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl)
                        gg.update_yaxes(range = [g['Caixas/Hora'].min()-10,g['Caixas/Hora'].max()])
                        gg.update_layout(height = 350, width = 350)
                    
                    elif elem == 14.0:

                        filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Kent'
                        padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                        filtro_calibre = padrao_embaldeiras['CALIBRE'] == 14
                        padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                        h = padrao_embaldeiras_palmer.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                        h = h.reset_index()
                        h['mean'] = round(h['mean'],0)
                        h = h.rename(columns = {'mean':'Caixas/Hora'})
                        h['Calibre'] = 14.0
                        h['Calibre'] = h['Calibre'].astype(str)
                        h['ID_PESSOA'] = h['ID_PESSOA'].astype(str)
                        hh = px.bar(h,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Kent - Calibre 14',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )
                        hh.update_yaxes(range = [h['Caixas/Hora'].min()-10,h['Caixas/Hora'].max()])
                        hh.update_layout(height = 350, width = 350)

                elif elem in Layout_linha_9['Calibre'] and (variedade == 'Keitt'  or variedade == 'Omer'):

                    resultDict[elem] = True
                    aaa = Layout_linha_9.groupby(['Calibre'])['Embaladeiras_1'].sum()
                    aaa = aaa.reset_index()


                    bbb = Layout_linha_9.groupby(['Calibre2'])['Embaladeiras_2'].sum()
                    bbb = bbb.reset_index()
                    bbb = bbb.rename(columns={'Calibre2':'Calibre', 'Embaladeiras_2':'Embaladeiras_1'})

                    ccc = pd.concat((aaa,bbb))
                    ccc['Calibre'] = ccc['Calibre'].replace(' ','0')
                    ccc['Calibre'] = ccc['Calibre'].astype(float)
                    ccc = ccc.groupby(['Calibre'])['Embaladeiras_1'].sum()
                    ccc = ccc.reset_index()


                    if elem == 5.0:
                        kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                        kl1 = round(kl1,0)

                        if kl1 == 0:
                            kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                        elif kl1 > 0: 
                            kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                            kl = kl.astype(int)

                        filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Keitt'
                        padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                        filtro_calibre = padrao_embaldeiras['CALIBRE'] == 5
                        padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                        a = padrao_embaldeiras_palmer.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                        a = a.reset_index()
                        a['mean'] = round(a['mean'],0)
                        a = a.rename(columns = {'mean':'Caixas/Hora'})
                        a['Calibre'] = 5.0
                        a['Calibre'] = a['Calibre'].astype(str)
                        a['ID_PESSOA'] = a['ID_PESSOA'].astype(str)

                        media_a = a['Caixas/Hora'].mean()
                        st.session_state.media_a = media_a

                        aa = px.bar(a,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Keitt - Calibre 5',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )
                        aa.update_yaxes(range = [a['Caixas/Hora'].min()-10,a['Caixas/Hora'].max()])
                        aa.add_hline(517)
                        aa.update_layout(height = 350, width = 350)

                    elif elem == 6.0:
                        kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                        kl1 = round(kl1,0)

                        if kl1 == 0:
                            kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                        elif kl1 > 0: 
                            kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                            kl = kl.astype(int)

                        filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Keitt'
                        padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                        filtro_calibre = padrao_embaldeiras['CALIBRE'] == 6
                        padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]

                        padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)
                        padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(a['ID_PESSOA'])]

                        b = padrao_embaldeiras_palmer_2.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                        b = b.reset_index()
                        b['mean'] = round(b['mean'],0)
                        b = b.rename(columns = {'mean':'Caixas/Hora'})
                        b['Calibre'] = 6.0
                        b['Calibre'] = b['Calibre'].astype(str)
                        b['ID_PESSOA'] = b['ID_PESSOA'].astype(str)
                        media_b = b['Caixas/Hora'].mean()
                        st.session_state.media_b = media_b
                        bb = px.bar(b,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Keitt - Calibre 6',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )
                        bb.update_yaxes(range = [b['Caixas/Hora'].min()-10,b['Caixas/Hora'].max()])
                        bb.add_hline(412)
                        bb.update_layout(height = 350, width = 350)

                    elif elem == 7.0:

                        kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                        kl1 = round(kl1,0)

                        if kl1 == 0:
                            kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                        elif kl1 > 0: 
                            kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                            kl = kl.astype(int)

                        filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Keitt'
                        padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                        filtro_calibre = padrao_embaldeiras['CALIBRE'] == 7
                        padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]

                        padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)
                        padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                        c = padrao_embaldeiras_palmer_3.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                        c = c.reset_index()
                        c['mean'] = round(c['mean'],0)
                        c = c.rename(columns = {'mean':'Caixas/Hora'})
                        c['Calibre'] = 7.0
                        c['Calibre'] = c['Calibre'].astype(str)
                        c['ID_PESSOA'] = c['ID_PESSOA'].astype(str)
                        media_c = c['Caixas/Hora'].mean()
                        st.session_state.media_c = media_c
                        cc = px.bar(c,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Keitt - Calibre 7',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )
                        cc.update_yaxes(range = [c['Caixas/Hora'].min()-10,c['Caixas/Hora'].max()])
                        cc.add_hline(321)
                        cc.update_layout(height = 350, width = 350)

                    elif elem == 8.0:
                        kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                        kl1 = round(kl1,0)

                        if kl1 == 0:
                            kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                        elif kl1 > 0: 
                            kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                            kl = kl.astype(int)

                        filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Keitt'
                        padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                        filtro_calibre = padrao_embaldeiras['CALIBRE'] == 8
                        padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]

                        padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)

                        padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_4 = padrao_embaldeiras_palmer_3[~padrao_embaldeiras_palmer_3.ID_PESSOA.isin(c['ID_PESSOA'])]

                        d = padrao_embaldeiras_palmer_4.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                        d = d.reset_index()
                        d['mean'] = round(d['mean'],0)
                        d = d.rename(columns = {'mean':'Caixas/Hora'})
                        d['Calibre'] = 8.0
                        d['Calibre'] = d['Calibre'].astype(str)
                        d['ID_PESSOA'] = d['ID_PESSOA'].astype(str)
                        media_d = d['Caixas/Hora'].mean()
                        st.session_state.media_d = media_d
                        dd = px.bar(d,y = 'Caixas/Hora', color = 'ID_PESSOA',title = 'Keitt - Calibre 8',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )
                        dd.update_yaxes(range = [d['Caixas/Hora'].min()-10,d['Caixas/Hora'].max()])
                        dd.add_hline(301)
                        dd.update_layout(height = 350, width = 350)

                    elif elem == 9.0:

                        kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                        kl1 = round(kl1,0)

                        if kl1 == 0:
                            kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                        elif kl1 > 0: 
                            kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                            kl = kl.astype(int)

                        filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Keitt'
                        padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                        filtro_calibre = padrao_embaldeiras['CALIBRE'] == 9
                        padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]

                        padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)

                        padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_4 = padrao_embaldeiras_palmer_3[~padrao_embaldeiras_palmer_3.ID_PESSOA.isin(c['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_5 = padrao_embaldeiras_palmer_4[~padrao_embaldeiras_palmer_4.ID_PESSOA.isin(d['ID_PESSOA'])]

                        e = padrao_embaldeiras_palmer_5.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                        e = e.reset_index()
                        e['mean'] = round(e['mean'],0)
                        e = e.rename(columns = {'mean':'Caixas/Hora'})
                        e['Calibre'] = 9.0
                        e['Calibre'] = e['Calibre'].astype(str)
                        e['ID_PESSOA'] = e['ID_PESSOA'].astype(str)
                        media_e = e['Caixas/Hora'].mean()
                        st.session_state.media_e = media_e
                        ee = px.bar(e,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Keitt - Calibre 9' ,hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl)
                        ee.update_yaxes(range = [e['Caixas/Hora'].min()-10,e['Caixas/Hora'].max()])
                        ee.add_hline(257)
                        ee.update_layout(height = 350, width = 350)

                    elif elem == 10.0:

                        kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                        kl1 = round(kl1,0)

                        if kl1 == 0:
                            kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                        elif kl1 > 0: 
                            kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                            kl = kl.astype(int)

                        filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Keitt'
                        padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                        filtro_calibre = padrao_embaldeiras['CALIBRE'] == 10
                        padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]

                        padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)

                        padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_4 = padrao_embaldeiras_palmer_3[~padrao_embaldeiras_palmer_3.ID_PESSOA.isin(c['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_5 = padrao_embaldeiras_palmer_4[~padrao_embaldeiras_palmer_4.ID_PESSOA.isin(d['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_6 = padrao_embaldeiras_palmer_5[~padrao_embaldeiras_palmer_5.ID_PESSOA.isin(e['ID_PESSOA'])]

                        f = padrao_embaldeiras_palmer_6.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                        f = f.reset_index()
                        f['mean'] = round(f['mean'],0)
                        f = f.rename(columns = {'mean':'Caixas/Hora'})
                        f['Calibre'] = 10.0
                        f['Calibre'] = f['Calibre'].astype(str)
                        f['ID_PESSOA'] = f['ID_PESSOA'].astype(str)
                        media_f = f['Caixas/Hora'].mean()
                        st.session_state.media_f = media_f
                        ff = px.bar(f,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Keitt - Calibre 10',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )
                        ff.update_yaxes(range = [f['Caixas/Hora'].min()-10,f['Caixas/Hora'].max()])
                        ff.add_hline(261)
                        ff.update_layout(height = 350, width = 350)

                    elif elem == 12.0:

                        kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                        kl1 = round(kl1,0)

                        if kl1 == 0:
                            kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                        elif kl1 > 0: 
                            kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                            kl = kl.astype(int)

                        filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Keitt'
                        padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                        filtro_calibre = padrao_embaldeiras['CALIBRE'] == 12
                        padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]

                        padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)

                        padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_4 = padrao_embaldeiras_palmer_3[~padrao_embaldeiras_palmer_3.ID_PESSOA.isin(c['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_5 = padrao_embaldeiras_palmer_4[~padrao_embaldeiras_palmer_4.ID_PESSOA.isin(d['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_6 = padrao_embaldeiras_palmer_5[~padrao_embaldeiras_palmer_5.ID_PESSOA.isin(e['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_7 = padrao_embaldeiras_palmer_6[~padrao_embaldeiras_palmer_6.ID_PESSOA.isin(f['ID_PESSOA'])]

                        
                        g = padrao_embaldeiras_palmer_7.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                        g = g.reset_index()
                        g['mean'] = round(g['mean'],0)
                        g = g.rename(columns = {'mean':'Caixas/Hora'})
                        g['Calibre'] = 12.0
                        g['Calibre'] = g['Calibre'].astype(str)
                        g['ID_PESSOA'] = g['ID_PESSOA'].astype(str)
                        media_g = g['Caixas/Hora'].mean()
                        st.session_state.media_g = media_g
                        gg = px.bar(g,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Keitt - Calibre 12' ,hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl)
                        gg.update_yaxes(range = [g['Caixas/Hora'].min()-10,g['Caixas/Hora'].max()])
                        gg.add_hline(253)
                        gg.update_layout(height = 350, width = 350)

                    elif elem == 14.0:

                        filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Keitt'
                        padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                        filtro_calibre = padrao_embaldeiras['CALIBRE'] == 14
                        padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                        h = padrao_embaldeiras_palmer.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                        h = h.reset_index()
                        h['mean'] = round(h['mean'],0)
                        h = h.rename(columns = {'mean':'Caixas/Hora'})
                        h['Calibre'] = 14.0
                        h['Calibre'] = h['Calibre'].astype(str)
                        h['ID_PESSOA'] = h['ID_PESSOA'].astype(str)
                        media_h = h['Caixas/Hora'].mean()
                        st.session_state.media_h = media_h
                        hh = px.bar(h,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Keitt - Calibre 14',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl )
                        hh.update_yaxes(range = [h['Caixas/Hora'].min()-10,h['Caixas/Hora'].max()])
                        hh.update_layout(height = 350, width = 350)

                elif elem in Layout_linha_9['Calibre'] and variedade == 'Tommy Atkins':

                    resultDict[elem] = True

                    aaa = Layout_linha_9.groupby(['Calibre'])['Embaladeiras_1'].sum()
                    aaa = aaa.reset_index()

                    bbb = Layout_linha_9.groupby(['Calibre2'])['Embaladeiras_2'].sum()
                    bbb = bbb.reset_index()
                    bbb = bbb.rename(columns={'Calibre2':'Calibre', 'Embaladeiras_2':'Embaladeiras_1'})

                    ccc = pd.concat((aaa,bbb))
                    ccc['Calibre'] = ccc['Calibre'].replace(' ','0')
                    ccc['Calibre'] = ccc['Calibre'].astype(float)
                    ccc = ccc.groupby(['Calibre'])['Embaladeiras_1'].sum()
                    ccc = ccc.reset_index()

                    if elem == 5.0:

                        filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Tommy Atkins'
                        padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                        filtro_calibre = padrao_embaldeiras['CALIBRE'] == 5
                        padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                        a = padrao_embaldeiras_palmer.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(20)
                        a = a.reset_index()
                        a['mean'] = round(a['mean'],0)
                        a = a.rename(columns = {'mean':'Caixas/Hora'})
                        a['Calibre'] = 5.0
                        a['Calibre'] = a['Calibre'].astype(str)
                        a['ID_PESSOA'] = a['ID_PESSOA'].astype(str)

                        media_a = a['Caixas/Hora'].mean()
                        st.session_state.media_a = media_a
                        aa = px.bar(a,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Tommy Atkins - Calibre 5',hover_name = 'PESSOA', color_discrete_sequence= px.colors.sequential.Aggrnyl)
                        aa.update_yaxes(range = [a['Caixas/Hora'].min()-10,a['Caixas/Hora'].max()])
                        aa.add_hline(235)
                        aa.update_layout(height = 350, width = 350)

                    elif elem == 6.0:

                        kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                        kl1 = round(kl1,0)

                        if kl1 == 0:
                            kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                        elif kl1 > 0: 
                            kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                            kl = kl.astype(int)

                        filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Tommy Atkins'
                        padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                        filtro_calibre = padrao_embaldeiras['CALIBRE'] == 6
                        padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]

                        padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)
                        padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(a['ID_PESSOA'])]

                        b = padrao_embaldeiras_palmer_2.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                        b = b.reset_index()
                        b['mean'] = round(b['mean'],0)
                        b = b.rename(columns = {'mean':'Caixas/Hora'})
                        b['Calibre'] = 6.0
                        b['Calibre'] = b['Calibre'].astype(str)
                        b['ID_PESSOA'] = b['ID_PESSOA'].astype(str)
                        media_b = b['Caixas/Hora'].mean()
                        st.session_state.media_b = media_b

                        bb = px.bar(b,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Tommy Atkins - Calibre 6',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl)
                        bb.update_yaxes(range = [b['Caixas/Hora'].min()-10,b['Caixas/Hora'].max()])
                        bb.add_hline(178)
                        bb.update_layout(height = 350, width = 350)

                    elif elem == 7.0:

                        kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                        kl1 = round(kl1,0)

                        if kl1 == 0:
                            kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                        elif kl1 > 0: 
                            kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                            kl = kl.astype(int)

                        filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Tommy Atkins'
                        padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                        filtro_calibre = padrao_embaldeiras['CALIBRE'] == 7
                        padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                        padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)
                        padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                        c = padrao_embaldeiras_palmer_3.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                        c = c.reset_index()
                        c['mean'] = round(c['mean'],0)
                        c = c.rename(columns = {'mean':'Caixas/Hora'})
                        c['Calibre'] = 7.0
                        c['Calibre'] = c['Calibre'].astype(str)
                        c['ID_PESSOA'] = c['ID_PESSOA'].astype(str)
                        media_c = c['Caixas/Hora'].mean()
                        st.session_state.media_c = media_c

                        cc = px.bar(c,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Tommy Atkins - Calibre 7', hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl)
                        cc.update_yaxes(range = [c['Caixas/Hora'].min()-10,c['Caixas/Hora'].max()])
                        cc.add_hline(185)
                        cc.update_layout(height = 350, width = 350)

                    elif elem == 8.0:

                        kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                        kl1 = round(kl1,0)

                        if kl1 == 0:
                            kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                        elif kl1 > 0: 
                            kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                            kl = kl.astype(int)

                        filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Tommy Atkins'
                        padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                        filtro_calibre = padrao_embaldeiras['CALIBRE'] == 8
                        padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                        padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)

                        padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_4 = padrao_embaldeiras_palmer_3[~padrao_embaldeiras_palmer_3.ID_PESSOA.isin(c['ID_PESSOA'])]

                        d = padrao_embaldeiras_palmer_4.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                        d = d.reset_index()
                        d['mean'] = round(d['mean'],0)
                        d = d.rename(columns = {'mean':'Caixas/Hora'})
                        d['Calibre'] = 8.0
                        d['Calibre'] = d['Calibre'].astype(str)
                        d['ID_PESSOA'] = d['ID_PESSOA'].astype(str)

                        media_d = d['Caixas/Hora'].mean()
                        st.session_state.media_d = media_d
                        
                        dd = px.bar(d,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Tommy Atkins - Calibre 8',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl)
                        dd.update_yaxes(range = [d['Caixas/Hora'].min()-10,d['Caixas/Hora'].max()])
                        dd.add_hline(195)
                        dd.update_layout(height = 350, width = 350)

                    elif elem == 9.0:

                        kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                        kl1 = round(kl1,0)

                        if kl1 == 0:
                            kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                        elif kl1 > 0: 
                            kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                            kl = kl.astype(int)

                        filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Tommy Atkins'
                        padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                        filtro_calibre = padrao_embaldeiras['CALIBRE'] == 9
                        padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]

                        padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)

                        padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_4 = padrao_embaldeiras_palmer_3[~padrao_embaldeiras_palmer_3.ID_PESSOA.isin(c['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_5 = padrao_embaldeiras_palmer_4[~padrao_embaldeiras_palmer_4.ID_PESSOA.isin(d['ID_PESSOA'])]

                        e = padrao_embaldeiras_palmer_5.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                        e = e.reset_index()
                        e['mean'] = round(e['mean'],0)
                        e = e.rename(columns = {'mean':'Caixas/Hora'})
                        e['Calibre'] = 9.0
                        e['Calibre'] = e['Calibre'].astype(str)
                        e['ID_PESSOA'] = e['ID_PESSOA'].astype(str)

                        media_e = e['Caixas/Hora'].mean()
                        st.session_state.media_e = media_e

                        ee = px.bar(e,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Tommy Atkins - Calibre 9',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl)
                        ee.update_yaxes(range = [e['Caixas/Hora'].min()-10,e['Caixas/Hora'].max()])
                        ee.add_hline(154)
                        ee.update_layout(height = 350, width = 350)

                    elif elem == 10.0:
                        kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                        kl1 = round(kl1,0)

                        if kl1 == 0:
                            kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                        elif kl1 > 0: 
                            kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                            kl = kl.astype(int)

                        filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Tommy Atkins'
                        padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                        filtro_calibre = padrao_embaldeiras['CALIBRE'] == 10
                        padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]

                        padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)

                        padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_4 = padrao_embaldeiras_palmer_3[~padrao_embaldeiras_palmer_3.ID_PESSOA.isin(c['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_5 = padrao_embaldeiras_palmer_4[~padrao_embaldeiras_palmer_4.ID_PESSOA.isin(d['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_6 = padrao_embaldeiras_palmer_5[~padrao_embaldeiras_palmer_5.ID_PESSOA.isin(e['ID_PESSOA'])]

                        f = padrao_embaldeiras_palmer_6.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                        f = f.reset_index()
                        f['mean'] = round(f['mean'],0)
                        f = f.rename(columns = {'mean':'Caixas/Hora'})
                        f['Calibre'] = 10.0
                        f['Calibre'] = f['Calibre'].astype(str)
                        f['ID_PESSOA'] = f['ID_PESSOA'].astype(str)

                        media_f = f['Caixas/Hora'].mean()
                        st.session_state.media_f = media_f

                        ff = px.bar(f,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Tommy Atkins - Calibre 10',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl)
                        ff.update_yaxes(range = [f['Caixas/Hora'].min()-10,f['Caixas/Hora'].max()])
                        ff.add_hline(144)
                        ff.update_layout(height = 350, width = 350)

                    elif elem == 12.0:

                        kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                        kl1 = round(kl1,0)
                        
                        if kl1 == 0:
                            kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                        elif kl1 > 0: 
                            kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                            kl = kl.astype(int)
                        
                        filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Tommy Atkins'
                        padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                        filtro_calibre = padrao_embaldeiras['CALIBRE'] == 12
                        padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]

                        padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)

                        padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_4 = padrao_embaldeiras_palmer_3[~padrao_embaldeiras_palmer_3.ID_PESSOA.isin(c['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_5 = padrao_embaldeiras_palmer_4[~padrao_embaldeiras_palmer_4.ID_PESSOA.isin(d['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_6 = padrao_embaldeiras_palmer_5[~padrao_embaldeiras_palmer_5.ID_PESSOA.isin(e['ID_PESSOA'])]

                        padrao_embaldeiras_palmer_7 = padrao_embaldeiras_palmer_6[~padrao_embaldeiras_palmer_6.ID_PESSOA.isin(f['ID_PESSOA'])]

                        g = padrao_embaldeiras_palmer_7.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                        g = g.reset_index()
                        g['mean'] = round(g['mean'],0)
                        g = g.rename(columns = {'mean':'Caixas/Hora'})
                        g['Calibre'] = 12.0
                        g['Calibre'] = g['Calibre'].astype(str)
                        g['ID_PESSOA'] = g['ID_PESSOA'].astype(str)

                        media_g = g['Caixas/Hora'].mean()
                        st.session_state.media_g = media_g

                        gg = px.bar(g,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Tommy Atkins  - Calibre 12',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl)
                        gg.update_yaxes(range = [g['Caixas/Hora'].min()-10,g['Caixas/Hora'].max()])
                        gg.add_hline(158)
                        gg.update_layout(height = 350, width = 350)

                    elif elem == 14.0:

                        kl1 = ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0]
                        kl1 = round(kl1,0)
                        
                        if kl1 == 0:
                            kl = ceil(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0])
                        elif kl1 > 0: 
                            kl = round(ccc.loc[ccc.Calibre== elem,'Embaladeiras_1'].values[0],0)
                            kl = kl.astype(int)

                        filtro_variedade = padrao_embaldeiras['VARIEDADE'] == 'Tommy Atkins'
                        padrao_embaldeiras_palmer = padrao_embaldeiras[filtro_variedade]

                        filtro_calibre = padrao_embaldeiras['CALIBRE'] == 14
                        padrao_embaldeiras_palmer = padrao_embaldeiras_palmer[filtro_calibre]
                        padrao_embaldeiras_palmer['ID_PESSOA'] = padrao_embaldeiras_palmer['ID_PESSOA'].astype(str)

                        padrao_embaldeiras_palmer_2 = padrao_embaldeiras_palmer[~padrao_embaldeiras_palmer.ID_PESSOA.isin(b['ID_PESSOA'])]
                        padrao_embaldeiras_palmer_3 = padrao_embaldeiras_palmer_2[~padrao_embaldeiras_palmer_2.ID_PESSOA.isin(a['ID_PESSOA'])]
                        padrao_embaldeiras_palmer_4 = padrao_embaldeiras_palmer_3[~padrao_embaldeiras_palmer_3.ID_PESSOA.isin(c['ID_PESSOA'])]
                        padrao_embaldeiras_palmer_5 = padrao_embaldeiras_palmer_4[~padrao_embaldeiras_palmer_4.ID_PESSOA.isin(d['ID_PESSOA'])]
                        padrao_embaldeiras_palmer_6 = padrao_embaldeiras_palmer_5[~padrao_embaldeiras_palmer_5.ID_PESSOA.isin(e['ID_PESSOA'])]
                        padrao_embaldeiras_palmer_7 = padrao_embaldeiras_palmer_6[~padrao_embaldeiras_palmer_6.ID_PESSOA.isin(f['ID_PESSOA'])]
                        padrao_embaldeiras_palmer_8 = padrao_embaldeiras_palmer_7[~padrao_embaldeiras_palmer_7.ID_PESSOA.isin(g['ID_PESSOA'])]

                        h = padrao_embaldeiras_palmer.groupby(['ID_PESSOA','PESSOA'])['mean'].max().sort_values(ascending=False).head(kl)
                        h = h.reset_index()
                        h['mean'] = round(h['mean'],0)
                        h = h.rename(columns = {'mean':'Caixas/Hora'})
                        h['Calibre'] = 14.0
                        h['Calibre'] = h['Calibre'].astype(str)
                        h['ID_PESSOA'] = h['ID_PESSOA'].astype(str)

                        media_h = h['Caixas/Hora'].mean()
                        st.session_state.media_h = media_h

                        hh = px.bar(h,y = 'Caixas/Hora', color = 'ID_PESSOA', title = 'Tommy Atkins - Calibre 14',hover_name = 'PESSOA',color_discrete_sequence= px.colors.sequential.Aggrnyl)
                        hh.update_yaxes(range = [h['Caixas/Hora'].min()-10,h['Caixas/Hora'].max()])
                        hh.add_hline(90)
                        hh.update_layout(height = 350, width = 350)

                else:
                    resultDict[elem] = False

            return colu1.write(aa), colu1.write(bb), colu2.write(cc), colu2.write(dd), colu3.write(ee), colu3.write(ff), colu4.write(gg), colu4.write(hh)

        result = check_valores(Layout_linha_9, [5.0,6.0,7.0,8.0,9.0,10.0,12.0,14.0])

        media_a = st.session_state.media_a
        media_b = st.session_state.media_b
        media_c = st.session_state.media_c
        media_d = st.session_state.media_d
        media_e = st.session_state.media_e
        media_f = st.session_state.media_f
        media_g = st.session_state.media_g
        media_h = st.session_state.media_h

    ###################### ATRIBUINDO NOVO RITMO  E PRODUTIVIDADE DAS EMBALADEIRAS INDICADAS ######################
        def ritmo(b):
            if b['Calibre'] == 5:
                return media_a
            elif b['Calibre'] == 6:
                return media_b
            elif b['Calibre'] == 7:
                return media_c
            elif b['Calibre'] == 8:
                return media_d
            elif b['Calibre'] == 9:
                return media_e
            elif b['Calibre'] == 10:
                return media_f
            elif b['Calibre'] == 12:
                return media_g
            elif b['Calibre'] == 14:
                return media_h
            else:
                return 'NADA'

        b['Ritmo_embaladeira'] = b.apply(ritmo, axis = 1) 
        filtro = b['Ritmo_embaladeira'] != 'NADA'
        b = b[filtro]
        b['Horas_4kg_embaladeiras'] = (b['Caixas_total'] / b['Ritmo_embaladeira']) / produtividade_embaladeira 
        ton_horas_embaladeiras = round(((b['Caixas_total'].sum()*4.05)/1000)/(b['Horas_4kg_embaladeiras'].sum()/embaladeira),2)

    ################################ EXIBIÇÃO ########################################
        ################################ BARRA EMBALADEIRAS POR LINHA ########################################
        with col3:
            Layout_linha_9 = Layout_linha_9.fillna(' ')
            Layout_linha_9['Qualidade'] = Layout_linha_9['Qualidade'].astype(str)
            Layout_linha_9['Qualidade2'] = Layout_linha_9['Qualidade2'].astype(str)
            Layout_linha_9['Calibre - Qualidade'] = Layout_linha_9['Calibre'] + '-' +Layout_linha_9['Qualidade'] + ' '+ '/' + ' ' + Layout_linha_9['Calibre2'] + '-' + Layout_linha_9['Qualidade2']
            Layout_linha_9['Embaladeiras'] = round(Layout_linha_9['Embaladeiras'],1)

            st.error('##### Embaladeiras por linha de embalagem:')

            fig4 = px.bar(Layout_linha_9, x = 'Linha', y = 'Embaladeiras', color = 'Calibre - Qualidade', text = 'Embaladeiras',color_discrete_sequence= px.colors.sequential.Oranges, 
            category_orders={"Calibre":['5.0','6.0','7.0','8.0','9.0','10.0','12.0','14.0']}, hover_name = 'Linha')
            fig4.update_layout(height = 450, width = 550, uniformtext_minsize=10, uniformtext_mode='show', font = dict(size = 15))
            fig4.update_traces(textfont_size=14, textangle=0, textposition="outside", cliponaxis=False)

            st.plotly_chart(fig4)

        ################################ PIZZA DISTRIBUIÇÃO ########################################
        with col1:
            import plotly.graph_objects as go

            b['Calibre Name'] = b['Calibre'].astype(str)
            def rename_b (b):
                    if b['Calibre'] == '4.0' or b['Calibre'] == '4':
                        return '4'
                    elif b['Calibre'] == '5.0' or b['Calibre'] == '5':
                        return '5'
                    elif b['Calibre'] == '6.0' or b['Calibre'] == '6':
                        return '6'
                    elif b['Calibre'] == '7.0' or b['Calibre'] == '7':
                        return '7'
                    elif b['Calibre'] == '8.0' or b['Calibre'] == '8':
                        return '8'
                    elif b['Calibre'] == '9.0' or b['Calibre'] == '9':
                        return '9'
                    elif b['Calibre'] == '10.0' or b['Calibre'] == '10':
                        return '10'
                    elif b['Calibre'] == '12.0' or b['Calibre'] == '12':
                        return '12'
                    elif b['Calibre'] == '14.0' or b['Calibre'] == '14':
                        return '14'
            b['Calibre'] = b.apply(rename_b, axis = 1)
    ##################################### CALCULO DA QUA


            c = round(b['Percentual'],2)
            st.error('##### Concentração de calibres:')

            fig = go.Figure(data=[go.Pie(labels = b['Calibre Name'], values = b['Percentual'], marker_colors = px.colors.sequential.Oranges ,hole = .35, pull=0.01)])
            fig.update_traces(textinfo='label+percent', textfont_size=15, textposition="inside")
            fig.update_layout(height = 450, width = 450, font = dict(size = 15))
            
            st.plotly_chart(fig)
            
        ################################ BARRA EMBALADEIRAS POR CALIBRE ########################################
        with col2:
            aaa = Layout_linha_9.groupby(['Calibre'])['Embaladeiras_1'].sum()
            aaa = aaa.reset_index()

            bbb = Layout_linha_9.groupby(['Calibre2'])['Embaladeiras_2'].sum()
            bbb = bbb.reset_index()
            bbb = bbb.rename(columns={'Calibre2':'Calibre', 'Embaladeiras_2':'Embaladeiras_1'})

            ccc = pd.concat((aaa,bbb))
            ccc['Calibre'] = ccc['Calibre'].replace(' ',0)

            drop_2 = ccc[ccc['Calibre'] == 0 ].index
            ccc2 = ccc.drop(drop_2, inplace = True)
            ccc['Embaladeiras_1'] = round(ccc['Embaladeiras_1'],1)
        
            st.error('##### Quantidade de embaladeiras por calibre:')

            fig = px.bar(ccc, y = 'Calibre', x = 'Embaladeiras_1', color = 'Calibre',
            category_orders = {'Calibre':['2.0','5.0','6.0','7.0','8.0','9.0','10.0','12.0','14.0']}, text = 'Embaladeiras_1', color_discrete_sequence= px.colors.sequential.Oranges)
            fig.update_layout(height = 450, width = 500,uniformtext_minsize=8, uniformtext_mode='show', font = dict(size = 15))
            fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False, marker_line_width=1.5)
            fig

        ################### CALCULO E EXIBIÇÃO DA NOVA CAPACIDADE DAS EMBALADEIRAS SELECIONADAS ####################################

        conta_delta = round(((100 * ton_horas_embaladeiras) / ton_horas) - 100,1)
        conta_delta2 = str(conta_delta) + ' ' + '%'

        col5x.metric(label="Recomendação (t/h)", value= ton_horas_embaladeiras, delta= conta_delta2)
        st.info('### ER atual vs ER embaladeiras selecionadas')

        dataframe = b[['Calibre Name','Percentual','Caixas_total','Ritmo','Horas_4kg','Ritmo_embaladeira','Horas_4kg_embaladeiras']]
        
        dataframe.rename(columns = {'Ritmo':'Ritmo Atual','Ritmo_embaladeira':'Ritmo Embaladeiras',
                                    'Horas_4kg_embaladeiras':'Horas Embaladeiras','Caixas_total':'Total de caixas',
                                    'Horas_4kg':'Horas Atual','Calibre Name':'Calibre'}, inplace = True)
        dataframe['Controle'] = controle2
        dataframe

        st.download_button( label = 'Baixar Planilha',data = dataframe.to_csv(), mime = 'text/csv')


if selected == 'Previsão de Calibres':
    import pandas as pd

    st.write('Dash de previsão de calibres por talhão')

    if st.button('Puxar base'):

        df_comportamento_calibres_TALHAO = pd.read_excel('C:/Users/bernard.collin/Desktop/planilha_denilton/pred_semanas/Comportamento_calibres_TALHAO.xlsx')

        # df_comportamento_calibres_VARIEDADE = pd.read_excel('C:/Users/bernard.collin/Desktop/planilha_denilton/pred_semanas/Comportamento_calibres_VARIEDADE.xlsx')
    
    
        # POR ENQUANDO DEIXAR GRAFICOS DE VARIEDADE EM STAND BY ELA PODE ENTRAR COMO UMA ABA AO LADO SIDEBAR DA PREVISAO DE CALIBRES
        # E O MODELO DE ML EU FAÇO NA SIDE BAR TAMBEM SUGESTA

        df_comportamento_qualidade =  pd.read_excel('C:/Users/bernard.collin/Desktop/planilha_denilton/pred_semanas/df_cleanref_TALHAO.xlsx')


        df_comportamento_calibres_TALHAO = df_comportamento_calibres_TALHAO.drop(columns = ['Unnamed: 0'])

        filtro = df_comportamento_calibres_TALHAO['SAFRA'] != 'M16'
        df_comportamento_calibres_TALHAO = df_comportamento_calibres_TALHAO[filtro]

        filtro = df_comportamento_calibres_TALHAO['SAFRA'] != 'M17'
        df_comportamento_calibres_TALHAO = df_comportamento_calibres_TALHAO[filtro]
        
        filtro = df_comportamento_calibres_TALHAO['SAFRA'] != 'M18'
        df_comportamento_calibres_TALHAO = df_comportamento_calibres_TALHAO[filtro]

    
    
    ############################     TALHAO      ############################
        dd = df_comportamento_calibres_TALHAO.groupby('TALHAO').FAZENDA.value_counts()

        ee = pd.DataFrame(dd)
        ee = ee.drop(columns = ['FAZENDA'])
        ee = ee.reset_index()
        ee = ee.drop(columns = ['FAZENDA'])
        lista_talhoes = ee

        st.session_state.lista_talhoes = lista_talhoes

        st.session_state.df_comportamento_calibres_TALHAO = df_comportamento_calibres_TALHAO
        
        st.session_state.df_comportamento_qualidade = df_comportamento_qualidade
############################ COLOCAR UM IF DE SE TALHAO DO CONTROLE X IS NOT IN EU RETORNO A PARTE DE VARIEDADE ############################
    

    lista_talhoes = st.session_state.lista_talhoes
    df_comportamento_calibres_TALHAO = st.session_state.df_comportamento_calibres_TALHAO 
    df_comportamento_qualidade = st.session_state.df_comportamento_qualidade

    Talhao = st.selectbox('Escolha o talhao', lista_talhoes)
    input_Talhao = str(Talhao)

    filtro_graph = df_comportamento_calibres_TALHAO['TALHAO'] == input_Talhao
    dataset_talhao = df_comportamento_calibres_TALHAO[filtro_graph]

    ############################ COLOCAR AQUI NESSA SEÇÃO OS GRÁFICOS DO DASH ############################



    ### ESSE GRAFICO É O DO COMPORTAMENTO - 

    fig = px.histogram(dataset_talhao, x = 'VALOR_CALIBRE', y = 'Calibre', color = 'VALOR_CALIBRE', 
    category_orders={'VALOR_CALIBRE':['CALIBRE_5','CALIBRE_6','CALIBRE_7','CALIBRE_8','CALIBRE_9','CALIBRE_10','CALIBRE_12','CALIBRE_14'],
    'Ordem_controle':['Primeiro Controle','Segundo Controle','Terceiro Controle','Quarto Controle']},
    histfunc = 'avg', facet_col = 'Ordem_controle')
    fig.update_layout(height = 500, width = 1700)
    #fig.update_traces(showlegend = True)
    st.plotly_chart(fig)
    

    ##########################################################################################

    filtro_graph_quality = df_comportamento_qualidade['TALHAO'] == input_Talhao
    dataset_quality = df_comportamento_qualidade[filtro_graph_quality]


    dataset_quality
    qualidade_tots = dataset_quality[['TOT_PRIMEIRA','TOT_SEGUNDA','TOT_TERCEIRA','TOT_REFUGO']]
    qualidade_tots


    Qualidade = st.selectbox('Escolha a qualidade', qualidade_tots)
    input_Qualidade= str(Qualidade)



    #df_comportamento_qualidade
    #fig = px.histogram(df_comportamento_qualidade, x = 'VALOR_CALIBRE', y = 'Calibre', color = 'VALOR_CALIBRE', 

    #category_orders={'VALOR_CALIBRE':['CALIBRE_5','CALIBRE_6','CALIBRE_7','CALIBRE_8','CALIBRE_9','CALIBRE_10','CALIBRE_12','CALIBRE_14'],
    #'Ordem_controle':['Primeiro Controle','Segundo Controle','Terceiro Controle','Quarto Controle']},

    #histfunc = 'avg', facet_col = 'Ordem_controle')


    #df_comportamento_qualidade



    ### ESSE GRAFICO É O QUE TEM POR VARIEDADE




































if selected == 'Contagem de frutos':
    coluna1, coluna2, coluna3 = st.columns(3)
    coluna1.write('________')
    coluna2.write('________')
    coluna3.write('________')

    coluna2.write('#### Contagem de Frutos')
    if coluna2.button('Iniciar'):
        st.write('______________')

        import plotly.express as px
        import plotly.graph_objects as go
        from PIL import Image


        #st.write('### Contagem de frutos')

        
        #st.write('Opa, clicastes?')
        import time
        import os
        os.environ["OMP_NUM_THREADS"] = "1"
        os.environ["OPENBLAS_NUM_THREADS"] = "1"
        os.environ["MKL_NUM_THREADS"] = "1"
        os.environ["VECLIB_MAXIMUM_THREADS"] = "1"
        os.environ["NUMEXPR_NUM_THREADS"] = "1"
        os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

        import sys
        sys.path.insert(0, './yolov5')

        import argparse
        import os
        import platform
        import shutil
        import time
        from pathlib import Path
        import cv2
        import torch
        import torch.backends.cudnn as cudnn

        from yolov5.models.experimental import attempt_load
        from yolov5.utils.downloads import attempt_download
        from yolov5.models.common import DetectMultiBackend
        from yolov5.utils.datasets import LoadImages, LoadStreams
        from yolov5.utils.general import (LOGGER, check_img_size, non_max_suppression, scale_coords, 
                                        check_imshow, xyxy2xywh, increment_path)
        from yolov5.utils.torch_utils import select_device, time_sync
        from yolov5.utils.plots import Annotator, colors
        from deep_sort.utils.parser import get_config
        from deep_sort.deep_sort import DeepSort

        FILE = Path(__file__).resolve()
        ROOT = FILE.parents[0]  # yolov5 deepsort root directory
        if str(ROOT) not in sys.path:
            sys.path.append(str(ROOT))  # add ROOT to PATH
        ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative
        count = 0
        data = []
        count_fly = 0
        count_fly2 = 0
        data_fly = []
        data_fly2 = []
        
        def detect(opt):
            out, source, yolo_model, deep_sort_model, show_vid, save_vid, save_txt, imgsz, evaluate, half, project, name, exist_ok= \
                opt.output, opt.source, opt.yolo_model, opt.deep_sort_model, opt.show_vid, opt.save_vid, \
                opt.save_txt, opt.imgsz, opt.evaluate, opt.half, opt.project, opt.name, opt.exist_ok
            webcam = source == '0' or source.startswith(
                'rtsp') or source.startswith('http') or source.endswith('.txt')

            device = select_device(opt.device)
            # initialize deepsort
            cfg = get_config()
            cfg.merge_from_file(opt.config_deepsort)
            deepsort = DeepSort(deep_sort_model,
                                device,
                                max_dist=cfg.DEEPSORT.MAX_DIST,
                                max_iou_distance=cfg.DEEPSORT.MAX_IOU_DISTANCE,
                                max_age=cfg.DEEPSORT.MAX_AGE, n_init=cfg.DEEPSORT.N_INIT, nn_budget=cfg.DEEPSORT.NN_BUDGET,
                                )

            # Initialize
            
            half &= device.type != 'cpu'  # half precision only supported on CUDA

            # The MOT16 evaluation runs multiple inference streams in parallel, each one writing to
            # its own .txt file. Hence, in that case, the output folder is not restored
            if not evaluate:
                if os.path.exists(out):
                    pass
                    shutil.rmtree(out)  # delete output folder
                os.makedirs(out)  # make new output folder

            # Directories
            save_dir = increment_path(Path(project) / name, exist_ok=exist_ok)  # increment run
            save_dir.mkdir(parents=True, exist_ok=True)  # make dir

            # Load model
            device = select_device(device)
            model = DetectMultiBackend(yolo_model, device=device, dnn=opt.dnn)
            stride, names, pt, jit, _ = model.stride, model.names, model.pt, model.jit, model.onnx
            imgsz = check_img_size(imgsz, s=stride)  # check image size

            # Half
            half &= pt and device.type != 'cpu'  # half precision only supported by PyTorch on CUDA
            if pt:
                model.model.half() if half else model.model.float()

            # Set Dataloader
            vid_path, vid_writer = None, None
            # Check if environment supports image displays
            if show_vid:
                show_vid = check_imshow()

            # Dataloader
            if webcam:
                show_vid = check_imshow()
                cudnn.benchmark = True  # set True to speed up constant image size inference
                dataset = LoadStreams(source, img_size=imgsz, stride=stride, auto=pt and not jit)
                bs = len(dataset)  # batch_size
            else:
                dataset = LoadImages(source, img_size=imgsz, stride=stride, auto=pt and not jit)
                bs = 1  # batch_size
            vid_path, vid_writer = [None] * bs, [None] * bs

            # Get names and colors
            names = model.module.names if hasattr(model, 'module') else model.names

            # extract what is in between the last '/' and last '.'
            txt_file_name = source.split('/')[-1].split('.')[0]
            txt_path = str(Path(save_dir)) + '/' + txt_file_name + '.txt'

            if pt and device.type != 'cpu':
                model(torch.zeros(1, 3, *imgsz).to(device).type_as(next(model.model.parameters())))  # warmup
            dt, seen = [0.0, 0.0, 0.0, 0.0], 0
            

            with st.empty():
                start_time = time.time()        
                for frame_idx, (path, img, im0s, vid_cap, s) in enumerate(dataset):
                    current_time = time.time()
                    t1 = time_sync()
                    img = torch.from_numpy(img).to(device)
                    img = img.half() if half else img.float()  # uint8 to fp16/32
                    img /= 255.0  # 0 - 255 to 0.0 - 1.0
                    if img.ndimension() == 3:
                        img = img.unsqueeze(0)
                    t2 = time_sync()
                    dt[0] += t2 - t1

                    # Inference
                    visualize = increment_path(save_dir / Path(path).stem, mkdir=True) if opt.visualize else False
                    pred = model(img, augment=opt.augment, visualize=visualize)
                    t3 = time_sync()
                    dt[1] += t3 - t2

                    # Apply NMS
                    pred = non_max_suppression(pred, opt.conf_thres, opt.iou_thres, opt.classes, opt.agnostic_nms, max_det=opt.max_det)
                    dt[2] += time_sync() - t3
                    
                    tempo_passado = current_time - start_time
                    

                    # Process detections
                    
                    for i, det in enumerate(pred):  # detections per image
                        seen += 1
                        if webcam:  # batch_size >= 1
                            p, im0, _ = path[i], im0s[i].copy(), dataset.count
                            s += f'{i}: '
                        else:
                            p, im0, _ = path, im0s.copy(), getattr(dataset, 'frame', 0)

                        p = Path(p)  # to Path
                        save_path = str(save_dir / p.name)  # im.jpg, vid.mp4, ...
                        s += '%gx%g ' % img.shape[2:]  # print string

                        annotator = Annotator(im0, line_width=2, pil=not ascii)
                        w, h = im0.shape[1], im0.shape[0]
                        if det is not None and len(det):
                            # Rescale boxes from img_size to im0 size
                            det[:, :4] = scale_coords(
                                img.shape[2:], det[:, :4], im0.shape).round()

                            # Print results
                            for c in det[:, -1].unique():
                                n = (det[:, -1] == c).sum()  # detections per class
                                
                                s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "  # add to string

                            xywhs = xyxy2xywh(det[:, 0:4])
                            confs = det[:, 4]
                            clss = det[:, 5]

                            # pass detections to deepsort
                            t4 = time_sync()
                            outputs = deepsort.update(xywhs.cpu(), confs.cpu(), clss.cpu(), im0)
                            
                            t5 = time_sync()
                            dt[3] += t5 - t4
                            
                            # draw boxes for visualization
                            if len(outputs) > 0:
                                for j, (output, conf) in enumerate(zip(outputs, confs)):

                                    bboxes = output[0:4]
                                    id = output[4]
                                    classe = output[5]
                                    #count
                                    count_obj(bboxes,w,h,id,classe)
                                    c = int(classe)  # integer class
                                    label = f'{id} {names[c]} {conf:.2f}'
                                    annotator.box_label(bboxes, label, color=colors(c, True))

                                    if save_txt:
                                        # to MOT format
                                        bbox_left = output[0]
                                        bbox_top = output[1]
                                        bbox_w = output[2] - output[0]
                                        bbox_h = output[3] - output[1]
                                        # Write MOT compliant results to file
                                        with open(txt_path, 'a') as f:
                                            f.write(('%g ' * 10 + '\n') % (frame_idx + 1, id, bbox_left,  # MOT format
                                                                        bbox_top, bbox_w, bbox_h, -1, -1, -1, -1))

                            LOGGER.info(f'{s}Done. YOLO:({t3 - t2:.3f}s), DeepSort:({t5 - t4:.3f}s)')

                        else:
                            deepsort.increment_ages()
                            LOGGER.info('No detections')

                        # Stream results
                        im0 = annotator.result()
                        
                        if show_vid:
                            global count_fly
                            color = (0,255,0)
                            start_point = (0, h-150)
                            end_point = (w, h-150)
                            cv2.line(im0, start_point, end_point, color, thickness=2)
                            thickness = 3
                            org = (150,150)
                            font = cv2.FONT_HERSHEY_SIMPLEX
                            fontScale = 1

                            color2 = (0,255,255)
                            fontScale2 = 1
                            org2 = (150,100)

                            cv2.putText(im0, str(count_fly) + ' ' + 'Mangas' , org, font,
                                fontScale,color,thickness, cv2.LINE_AA)
                            #cv2.putText(im0, 'mangos_C2:' + str(count_fly2), org2, font,
                            #   fontScale2,color2,thickness, cv2.LINE_AA)
                        #  cv2.putText(im0, 'Flyss:' + str(count_fly), org, font,
                            #  fontScale,color,thickness, cv2.LINE_AA)
                        #   cv2.putText(im0, 'Flys2:' + str(count_fly2), org, font,
                            #  fontScale,color,thickness, cv2.LINE_AA)

                            cv2.imshow(str(p), im0)
                            #st.write('#### Quantidade de frutos passados', str(count_fly))



                            

                            coluna1, coluna2, coluna3, coluna4, coluna5, coluna6 = st.columns([0.5,1,1,1,1,1])
                            #colum1, colum2 = st.columns(2)
                            #colum1.write('### Gráficos de monitoramento')

                            # coluna2.image(im0 , channels = 'BGR')

                            ab = str(count_fly)
                            coluna1.metric(label = 'Quantidade de mangas:', value = ab)
                            
                            data_fly_df = pd.DataFrame(data_fly, columns = ['ID'])


                            data_fly_df = data_fly_df.reset_index()
                        #    data_fly_df.columns = ['Quantidade','ID']
                            data_fly_df.rename(columns = {'index':'Quantidade'}, inplace = True)

                            data_fly_df['Quantidade'] = data_fly_df['Quantidade'] + 1




                            
                        #    if data_fly_df['Quantidade'][:-1]:
                            #    return tempo_passado

                            
                                
                            #data_fly_df['Tempo'] = tempo_passado

                            #ultimo_tempo = data_fly_df['Tempo'][:-1]
                            
                            fig = go.Figure()
                            fig.add_trace(go.Bar(y = [27], text='27', name = 'Limite de parada'))
                            fig.add_trace(go.Bar(y = [count_fly],text = str(count_fly), name = 'Quantidade passada'))
                            fig.update_layout(height = 400, width = 550)


                            fig2 = px.scatter(data_fly_df, y = 'Quantidade', x = 'ID')
                            fig2.update_layout(height = 400, width = 500)


                            coluna2.success('### Limite')
                            coluna2.plotly_chart(fig)
                            coluna2.write(' ')
                            coluna4.success('### Frutos contados')
                            coluna4.plotly_chart(fig2)
                            #coluna5.write(data_fly_df)
                            #coluna2.write(data_fly_df)
                            
                            
                            
                            
                            
                            coluna6.success('### Esteira')
                            coluna6.write(' ')
                            coluna6.write(' ')
                            coluna6.write(' ')
                            coluna6.write(' ')
                            coluna6.write(' ')
                            coluna6.write(' ')
                            coluna6.image(im0 , channels = 'BGR')


                            if count_fly > 27:
                                
                                
                            #    column1, column2 = st.columns(2)
                                coluna1, coluna2, coluna3, coluna4, coluna5, coluna6 = st.columns([0.5,1,1,1,1,1])
                                
                                #column1.success('#### Quantidade de frutos passou de 27, contagem finalizada.')

                                ab = str(count_fly)
                                coluna1.metric(label = 'Quantidade de mangas:', value = ab)
                                coluna2.success('### Limite')
                                coluna2.plotly_chart(fig)
                                coluna2.write(' ')
                                coluna4.success('### Frutos contados')
                                coluna4.plotly_chart(fig2)



                                #coluna5.write(data_fly_df)
                                #coluna2.write(data_fly_df)
                                
                                
                                
                                
                                
                                coluna6.success('### Esteira')
                                coluna6.write(' ')
                                coluna6.write(' ')
                                coluna6.write(' ')
                                coluna6.write(' ')
                                coluna6.write(' ')
                                coluna6.write(' ')
                                coluna6.image(im0 , channels = 'BGR')
                                
                                st.stop()


                            #st.image(im0)

                            #cv2.waitKey(1)
                            #st.video(im0)
                            if cv2.waitKey(1) == ord('q'):  # q to quit
                                raise StopIteration
                        
                        # Save results (image with detections)
                        if save_vid:
                            if vid_path != save_path:  # new video
                                vid_path = save_path
                                if isinstance(vid_writer, cv2.VideoWriter):
                                    vid_writer.release()  # release previous video writer
                                if vid_cap:  # video
                                    fps = vid_cap.get(cv2.CAP_PROP_FPS)
                                    w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                                    h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                                else:  # stream
                                    fps, w, h = 30, im0.shape[1], im0.shape[0]

                                vid_writer = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
                                
                            vid_writer.write(im0)
                        
                    
            



            
            # Print results
            t = tuple(x / seen * 1E3 for x in dt)  # speeds per image
            LOGGER.info(f'Speed: %.1fms pre-process, %.1fms inference, %.1fms NMS, %.1fms deep sort update \
                per image at shape {(1, 3, *imgsz)}' % t)
                
            
            if save_txt or save_vid:
                print('Results saved to %s' % save_path)
                if platform == 'darwin':  # MacOS
                    os.system('open ' + save_path)

        #def count_obj(box,w,h,id):
            #global count,data 
            #center_coordinates = (int(box[0]+(box[2]-box[0])/2), int(box[1]+(box[3]-box[1])/2))
            #if int(box[1]+(box[3]-box[1])/2) > (h - 350):
                #if id not in data:
                # count += 1
                # data.append(id)
            
        
        def count_obj(box,w,h,id,classe):
            global count_fly,data_fly, count_fly2 , data_fly2
            center_coordinates = (int(box[0]+(box[2]-box[0])/2) , int(box[1]+(box[3]-box[1])/2))
            
            if  classe == 0:
                if int(box[1]+(box[3]-box[1])/2) < (h-150):
                    if id not in data_fly:
                            count_fly += 1
                            data_fly.append(id)
                            
                                
                            
            
                #st.write('#### Quantidade de frutos passados', str(count_fly))
                    
                            
        
        # if  classe == 1:
            #  if int(box[1]+(box[3]-box[1])/2) < (h-150):
                #	if id not in data:
                    #	count_fly2 += 1
            #  		data_fly2.append(id)
        #
try:
    with st.empty():
        if __name__ == '__main__':
            parser = argparse.ArgumentParser()
            parser.add_argument('--yolo_model', nargs='+', type=str, default='best_final.pt', help='model.pt path(s)')
            parser.add_argument('--deep_sort_model', type=str, default='osnet_x0_25')
            parser.add_argument('--source', type=str, default='videos/video_controle_450_keitt.mp4', help='source')  # file/folder, 0 for webcam
            parser.add_argument('--output', type=str, default='inference/output', help='output folder')  # output folder
            parser.add_argument('--imgsz', '--img', '--img-size', nargs='+', type=int, default=[640], help='inference size h,w')
            parser.add_argument('--conf-thres', type=float, default=0.75, help='object confidence threshold')
            parser.add_argument('--iou-thres', type=float, default=0.6, help='IOU threshold for NMS')
            parser.add_argument('--fourcc', type=str, default='mp4v', help='output video codec (verify ffmpeg support)')
            parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
            parser.add_argument('--show-vid', action='store_true', help='display tracking video results',default = True)
            parser.add_argument('--save-vid', action='store_true', help='save video tracking results', default = True)
            parser.add_argument('--save-txt', action='store_true', help='save MOT compliant results to *.txt')
            # class 0 is person, 1 is bycicle, 2 is car... 79 is oven
            #parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 16 17')
            parser.add_argument('--classes', default=[0,1], type=int, help='filter by class')
            parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
            parser.add_argument('--augment', action='store_true', help='augmented inference')
            parser.add_argument('--evaluate', action='store_true', help='augmented inference')
            parser.add_argument("--config_deepsort", type=str, default="deep_sort/configs/deep_sort.yaml")
            parser.add_argument("--half", action="store_true", help="use FP16 half-precision inference")
            parser.add_argument('--visualize', action='store_true', help='visualize features')
            parser.add_argument('--max-det', type=int, default=1000, help='maximum detection per image')
            parser.add_argument('--dnn', action='store_true', help='use OpenCV DNN for ONNX inference')
            parser.add_argument('--project', default=ROOT / 'runs/track', help='save results to project/name')
            parser.add_argument('--name', default='exp', help='save results to project/name')
            parser.add_argument('--exist-ok', action='store_true', help='existing project/name ok, do not increment')
            opt = parser.parse_args()
            opt.imgsz *= 2 if len(opt.imgsz) == 1 else 1  # expand

            with torch.no_grad():
                detect(opt)
except NameError:
    st.write(' ')



if selected == 'Embaladeiras':
    st.write('Em desenvolvimento..')
    

if selected == 'Meta PH':
    st.write('Em desenvolvimento..')
