CREATE USER mysaas WITH PASSWORD 'mysaas';
CREATE DATABASE mysaas;
GRANT ALL PRIVILEGES ON DATABASE mysaas TO mysaas;
\connect mysaas;
GRANT CREATE ON SCHEMA public TO mysaas;