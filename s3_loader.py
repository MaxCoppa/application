# %%
import os
from dotenv import load_dotenv

load_dotenv()


MY_BUCKET = os.environ.get("MY_BUCKET", "")
CHEMIN_FICHIER = os.environ.get("CHEMIN_FICHIER", "data.csv")

# %%
import s3fs
import pandas as pd

fs = s3fs.S3FileSystem(client_kwargs={"endpoint_url": "https://minio.lab.sspcloud.fr"})

with fs.open(f"s3://{MY_BUCKET}/{CHEMIN_FICHIER}") as f:
    df = pd.read_csv(f)

df

# %%

import os
import duckdb

con = duckdb.connect(database=":memory:")

query_definition = f"SELECT * FROM read_csv('s3://{MY_BUCKET}/{CHEMIN_FICHIER}')"
con.sql(f"""
        COPY (
            SELECT *
            FROM read_csv_auto('s3://{MY_BUCKET}/{CHEMIN_FICHIER}')
        )
        TO 's3://{MY_BUCKET}/{CHEMIN_FICHIER.replace("csv", "parquet")}'
        (FORMAT PARQUET);
    """)

# %%

CHEMIN_PARQUET = CHEMIN_FICHIER.replace(".csv", ".parquet")


# %%
import s3fs
import pandas as pd

fs = s3fs.S3FileSystem(client_kwargs={"endpoint_url": "https://minio.lab.sspcloud.fr"})

df = pd.read_parquet(f"s3://{MY_BUCKET}/{CHEMIN_PARQUET}", filesystem=fs)

# %%
URL_RAW = ""
data_path = os.environ.get("data_path", URL_RAW)
# %%
f"https://minio.lab.sspcloud.fr/{MY_BUCKET}/ensae-reproductibilite/data/raw/data.parquet"

# %%
