# ALEKTRA - Energy Markets Data Platform

Bloomberg Terminal for US energy markets, starting with PJM and MISO.

## Project Structure
```
ALEKTRA/
├── backend/
│   ├── functions/        # Cloud Functions for data ingestion
│   ├── scripts/          # Utility scripts and data processing
│   └── requirements.txt  # Python dependencies
├── frontend/             # Web application frontend
├── notebooks/            # Jupyter notebooks for exploration
├── infrastructure/       # GCP deployment configs
├── docs/                 # Documentation
└── README.md
```

## Tech Stack

- **Cloud:** Google Cloud Platform
- **Backend:** Python, Cloud Functions, FastAPI
- **Database:** BigQuery, Cloud Storage
- **Data Sources:** PJM, MISO ISOs

## Getting Started

### Prerequisites
- Python 3.9+
- GCP account with project access
- PJM DataMiner credentials

### Local Development
```bash
# Clone the repository
git clone <your-repo-url>
cd ALEKTRA

# Set up Python virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r backend/requirements.txt
```

## Current Status

🚧 MVP in development
- Setting up GCP infrastructure  
- Building PJM data ingestion pipeline
- Target: Day-ahead prices, Real-time prices, Demand forecasts

## Data Pipeline Architecture

See `docs/` for detailed architecture documentation.

