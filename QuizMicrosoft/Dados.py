 
import pandas as pd

questions = [
    ["Em que ano a Microsoft foi criada?", "1975", "1971", "1981", "1979", 1],
    ["Onde Paul Allen nasceu?", "New York", "Seattle", "Texas", "Chicago", 2],
    ["Em que ano Paul Allen nasceu?", "1951", "1953", "1955", "1950", 2],
    ["Quem foi Paul Allen?", "Fundador da SpaceX", "Astronauta da NASA", "Pioneiro da aviação", "Fundador da Microsoft", 4],
    ["Qual foi o principal campo de atuação de Paul Allen após sua carreira na Microsoft?", "Desenvolvimento e criação de hardware", "Astronomia e exploração espacial", "Investimentos e filantropia", "Ciência da computação", 3],
    ["Em que área Paul Allen fez grandes investimentos, além de tecnologia?", "Moda", "Esportes e entretenimento", "Biotecnologia", "Educação", 2],
    [" Qual foi o nome do time de futebol americano que Paul Allen possuía?", "Seattle Seahawks", "Chicago bulls", "Dallas Cowboys", "Los Angeles Rams", 1],
    ["O que Paul Allen fundou em Seattle para promover a ciência e a tecnologia?", "The Paul Allen Institute for Brain Science", "Paul Allen Space Center", "AllenTech Research", "Nvidia Company", 1],
    ["Qual foi o nome do projeto de Paul Allen que tinha como objetivo mapear o cérebro humano?", "Neuralink", "BrainMap", "Allen Brain Atlas", "NeuroTech", 3],
    ["Qual foi o nome do mega-projeto de Paul Allen relacionado a aviões e aeronáutica?", "Stratolaunch", "Spruce Goose", "Concorde", "Boeing 747", 1],
    ["Qual foi a principal paixão de Paul Allen além da tecnologia e dos negócios?", "Culinária ", "Fotografia", "Música e guitarra", "Pintura e escultura", 3]]
   

#Criação dataframe pandas

df = pd.DataFrame(questions, columns=["Perguntas", "Opção 1", "Opção 2", "Opção 3", "Opção 4", "Resposta"])

#Salvar no Arquivo Excel

df.to_excel("QuizManeiro.xlsx", index=False)

print("As perguntas foram encaminhadas para o excel")