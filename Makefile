install-deps:
	@echo "Installing dependencies"
	@cd importer_service && npm install

containers:
	@echo "Building containers"
	@cd importer_service && docker-compose up

drugbank_tables:
	@echo "Creating Drugbank tables"
	@cd importer_service && PGPASSWORD=drugbank psql -h localhost -p 5433 -U drugbank -d drugbank -f drugbank_migration.sql

dump:
	@echo "Dumping Disgenet database"
	@sqlite3 ./importer_service/disgenet.db .dump > importer_service/dump.sql

import-drugbank:
	@echo "Importing Drugbank data"
	@cd importer_service && node import_drugbank.js

import-disgenet:
	@echo "Importing Disgenet data"
	@cd importer_service && node import_disgenet.js

build-project:
	@echo "Building project"
	install-deps containers drugbank_tables dump import-drugbank import-disgenet