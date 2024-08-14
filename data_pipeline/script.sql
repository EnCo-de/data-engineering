CREATE TABLE IF NOT EXISTS talks (
  talk_id bigserial PRIMARY KEY,
  talk_start TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  talked_time NUMERIC(8, 3) NOT NULL, --seconds
  microphone_used VARCHAR (50) NOT NULL,
  speaker_used VARCHAR (50) NOT NULL,
  voice_sentiment VARCHAR (50) NOT NULL --FOREIGN KEY to table with fields tone of voice, pitch, and speech pattern
  -- session_uuid UUID,
  -- user_identifier integer NOT NULL, --FOREIGN KEY to users table
  --   FOREIGN KEY (user_identifier) REFERENCES users (user_id)
  --               ON UPDATE CASCADE ON DELETE CASCADE
);