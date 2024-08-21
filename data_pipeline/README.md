Set up and run the containers using _docker-compose_ command

        docker-compose -p talksstream up -d --build

This is a comprehensive data ingestion pipeline. As source data is considered a stream of
user metrics, which include the following 4 types: talked_time, microphone_used,
speaker_used, and voice_sentiment.

The solution efficiently ingests this stream of metrics into a PostgreSQL database.

It's provided in the form of two Docker containers: one for running
the Python application and another for hosting an instance of PostgreSQL 
relational database. The database container is configured to store its files on
the host machine to ensure data persistence and ease of access.

The containers should be orchestrated using a _docker-compose.yml_ file, ensuring that they
can be started, stopped, and managed easily. Communication between the containers
is configured to occur through the Docker bridge network interface of the host machine on
which the application is running.

The SQL script to create the database structure 
includes the necessary table definitions.
