import pandas as pd
import pymysql
class MarketDB:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='daydream',
            password='1234', db='INVESTAR', charset='utf8')
        self.codes = dict()
        self.getCompanyInfo()
        
        
    def __del__(self):
        self.conn.close()

    def getCompanyInfo(self):
        sql = "SELECT * FROM company_info"
        companyInfo = pd.read_sql(sql, self.conn)
        for idx in range(len(companyInfo)):
            self.codes[companyInfo['code'].values[idx]] = companyInfo['company'].values[idx]

    def getDailyPrice(self, code, startDate, endDate):
        sql = "SELECT * FROM daily_price WHERE code = '{}' and date >= '{}' and date <= '{}'".format(code, startDate, endDate)
        df = pd.read_sql(sql, self.conn)
        df.index = df['date']
        return df

if __name__ =='__main__':
    marketdb = MarketDB()
    df = marketdb.getDailyPrice('005930','2019-01-01','2020-12-31')

    print(df)

