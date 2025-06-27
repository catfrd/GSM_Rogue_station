echo "Starting Rogue BTS Detection & UE Simulation Project"
echo "Ensuring required directories exist..."

mkdir -p logs
mkdir -p crowdsourcing/ue_reports

echo "Building and launching all services with Docker Compose..."
docker-compose up --build

echo "All services executed."
