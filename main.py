import speedtest as st
import pandas as pd
from datetime import datetime
from pathlib import Path


def getSpeed():
    speedTest = st.Speedtest()
    speedTest.get_best_server()

    ping = speedTest.results.ping
    download = speedTest.download()
    upload = speedTest.upload()

    downloadMbs = round(download / (10 ** 6), 2)
    uploadMbs = round(upload / (10 ** 6), 2)

    return ping, downloadMbs, uploadMbs


def updateDataframe():
    dateDirty = datetime.today()
    date = dateDirty.strftime("%H:%M")
    speed = getSpeed()
    data = {
        "date": [date],
        "ping": [speed[0]],
        "download": [speed[1]],
        "upload": [speed[2]]
    }
    df = pd.DataFrame.from_dict(data)
    df.set_index('date')

    fileDate = dateDirty.strftime("%d,%m,%Y")
    csv = Path("./data," + fileDate + ".csv")
    if csv.is_file():
        df2 = pd.read_csv(csv)
        df2.set_index('date')
        df2 = df2.append(df, ignore_index=True)
        print(df2)
        df2.to_csv("./data," + fileDate + ".csv", index=False)
    else:
        df.to_csv("./data," + fileDate + ".csv", index=False)


updateDataframe()
