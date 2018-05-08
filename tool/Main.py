
import  FanxingDao
if __name__ == "__main__":
    users  = FanxingDao.select("select * from t_user limit 2")
    for user in users:
        print user