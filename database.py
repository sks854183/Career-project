from sqlalchemy import create_engine, text # type: ignore

db_connection_string ="mysql+pymysql://root:Suman@127.0.0.1:3306/sumancareers?charset=utf8mb4"

engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "ca.pem"
        }
    }) 
    
def load_jobs_from_db():
    with engine.connect() as conn:
     result = conn.execute(text("select * from jobs"))
     jobs = []
     for row in result.all():
        jobs.append(dict(row))
     return jobs 
    
