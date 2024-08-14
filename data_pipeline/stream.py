import psycopg2
from config import load_config
import time
import uuid
import random

count = 1000

def get_large_stream(count):
    """returns N rows of data"""
    def f():
        """The generator of mock data"""
        for k in range(1, count+1):
            time.sleep(.01)
            values = {
                'talked_time': round(random.uniform(0, 10000), 3),
                'microphone_used': f'mic-{uuid.uuid4()}',
                'speaker_used': f'speaker_{uuid.uuid4()}',
                'voice_sentiment': f'voice_{k}'
            }
            yield values
    return f()


def store_talks(stream):
    insert_query = '''INSERT INTO talks (talked_time, microphone_used, speaker_used, voice_sentiment) 
    VALUES (%(talked_time)s, %(microphone_used)s, %(speaker_used)s, %(voice_sentiment)s) 
    RETURNING talk_id;'''
    talk_id = None
    config = load_config()
    # connect to the PostgreSQL server
    try:
        with  psycopg2.connect(**config) as conn:
            # create a cursor object
            with  conn.cursor() as cur:
                for values in stream:
                    # execute the INSERT statement
                    cur.execute(sql, values)
                    # get the generated id back                
                    fetch = cur.fetchone()
                    if fetch:
                        talk_id = fetch[0]
                        print(talk_id)
                    # commit the changes to the database
                    conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return talk_id
    # close the connection


if __name__ == '__main__':
    stream = get_large_stream(count)
    store_talks(stream)
    # for line in stream:
    #     print(line)

sql = '''INSERT INTO talks (talked_time, microphone_used, speaker_used, voice_sentiment) 
VALUES (100.5, 'microphone_1', 'speaker_1', 'voice_s'),
(60.25, 'microphone_2', 'speaker_2', 'happy'),
(10000.225, 'microphone_3', 'speaker_3', 'loud');'''

select_all = 'SELECT * FROM talks;'