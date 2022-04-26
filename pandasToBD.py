import datetime, requests as rt, pandas as pd
from sqlalchemy import create_engine



def conectaBD(df):
    engine = create_engine('mysql+mysqlconnector://root:12345@localhost/DOOC')
    df.to_sql(name='my_table', con=engine, if_exists='append', index=False)
    return 'sucesso!'


def transformaDados(lista)-> list:
    df = pd.DataFrame(lista)
    df.sort_index(axis=1, inplace=True)
    conectaBD(df)


def requisitadados(URL):
    url = URL
    x = rt.get(url)
    transformaDados(x.json())


if __name__ == '__main__':
    print('hi')
    data = datetime.date.today()
    for i in range(10):
        var = str('https://apitempo.inmet.gov.br/estacao/dados/' + str(data.year) + '-' + str(data.month) + '-' + str(data.day-i))
        dt = requisitadados(var)
    '''dados = pd.read_dict(dt)
    print(type(dados))'''