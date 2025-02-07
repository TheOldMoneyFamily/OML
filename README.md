# Old Money Mansions

Welcome to the **Old Money Mansions** project – a GPT-powered article writing assistant tailored for generating high-quality, fact-checked articles about historical estates and iconic mansions.

This project supports two distinct article formats:

1. **"Why X Was Demolished" Format**  
   A five-chapter article where each chapter (between 510 and 520 words) covers:
   - **Chapter 1:** The peak period of the mansion (in a slightly witty Piers Morgan style)
   - **Chapter 2:** Origins and construction history
   - **Chapter 3:** Notable residents and events
   - **Chapter 4:** Decline and preservation attempts
   - **Chapter 5:** Legacy and architectural influence

2. **"Inside The..." Format**  
   A single continuous article that details:
   - Family wealth context
   - Estate specifications and architectural details
   - Interior design elements and notable features
   - Current status/ownership

Additional capabilities include real-time fact-checking via Perplexity.AI, media conversion (audio and video), and a robust quality control pipeline that enforces word counts, precise measurements, and historical accuracy.

## Project Structure

old-money-mansions/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py            # Entrypoint for the backend server
│   │   ├── config.py          # Application configuration (DB, API keys, etc.)
│   │   ├── routers/
│   │   │   ├── api/
│   │   │   │   ├── articles.py      # Endpoints for article generation (“Why” and “Inside” formats)
│   │   │   │   ├── auth.py          # Authentication endpoints
│   │   │   │   ├── fact_check.py    # Fact-checking endpoints
│   │   │   │   ├── media.py         # Media conversion endpoints
│   │   │   │   └── youtube.py       # YouTube insights endpoints
│   │   │   └── web/
│   │   │       ├── dashboard.py     # Web routes for the dashboard UI
│   │   │       ├── home.py          # Public landing pages
│   │   │       ├── login.py         # Login and profile pages
│   │   │       └── profile.py
│   │   ├── services/
│   │   │   ├── ai_service.py        # Article generation logic (model calls, formatting)
│   │   │   ├── auth_service.py      # User authentication and authorization
│   │   │   ├── fact_check_service.py# Integration with Perplexity.AI for fact verification
│   │   │   ├── media_service.py     # Conversion of articles to audio/video formats
│   │   │   └── youtube_service.py   # Retrieval and processing of YouTube analytics
│   │   └── tests/
│   │       ├── test_articles.py
│   │       ├── test_auth.py
│   │       └── test_fact_check.py
│   ├── requirements.txt       # Python dependencies
│   └── Dockerfile             # Containerization for the backend
├── frontend/
│   ├── public/
│   │   ├── assets/
│   │   │   ├── css/
│   │   │   │   └── style.css
│   │   │   ├── images/
│   │   │   └── js/
│   │   ├── favicon.ico
│   │   └── index.html         # Main HTML file
│   ├── src/
│   │   ├── components/        # Reusable React (or Vue) components
│   │   │   ├── Header.jsx
│   │   │   ├── Footer.jsx
│   │   │   └── Dashboard.jsx
│   │   ├── pages/             # Routing for the SPA (e.g., Next.js pages)
│   │   │   ├── index.jsx
│   │   │   ├── login.jsx
│   │   │   └── profile.jsx
│   │   ├── styles/
│   │   │   └── main.css
│   │   └── tests/
│   │       └── frontend.test.jsx
│   ├── package.json           # Node dependencies and scripts
│   ├── tsconfig.json          # TypeScript configuration (if applicable)
│   └── Dockerfile             # Containerization for the frontend
├── data/
│   ├── approved_scripts/      # Source manuscripts and approved scripts
│   ├── audios/                # Generated audio files
│   ├── embeddings/            # Precomputed embeddings for fact-checking or search
│   ├── scripts/               # Raw script files (PDFs, DOCX, TXT)
│   ├── transcription/         # Transcribed content from videos or audios
│   └── vector_store/          # Storage for vectorized representations
├── deploy/
│   ├── docker-compose.yml     # Multi-container orchestration file
│   ├── nginx.conf             # Reverse proxy configuration
│   └── deploy.sh              # Deployment script(s)
├── docs/
│   ├── README.md              # Project overview and setup instructions
│   ├── API_Documentation.md   # Detailed API specs (linked to our OpenAPI YAML)
│   └── architecture.md        # System architecture and design rationale
├── notebooks/                 # Jupyter notebooks for data preprocessing, model evaluation, etc.
│   ├── preprocess_and_embed.ipynb
│   └── query_vector_store.ipynb
└── README.md                  # Top-level project README with an overview, installation, and usage instructions


## How It Works

- **Backend:**  
  The backend exposes RESTful API endpoints for generating articles in two formats, fact-checking content, converting articles into audio/video, and retrieving YouTube insights. It organizes business logic into dedicated services, and all endpoints are tested and containerized for reliable deployment.

- **Frontend:**  
  The frontend provides an intuitive dashboard where users can interact with the system—upload scripts, trigger article generation, review fact-check results, and view analytics. It is built as a single-page application with a modern component-based framework.

- **Data Management & Deployment:**  
  The project stores all raw and processed data (approved scripts, transcriptions, embeddings, etc.) under the `data/` folder. Deployment configurations (Docker, nginx, etc.) are kept under `deploy/` to facilitate smooth containerized operations.

- **Documentation & Experimentation:**  
  Detailed documentation and architectural overviews are available in the `docs/` folder, while Jupyter notebooks in `notebooks/` help with data preprocessing, model experimentation, and embedding queries.

## Setup Instructions

1. **Backend Setup:**
   - Navigate to the `backend/` directory.
   - Install Python dependencies:  
     ```powershell
     pip install -r requirements.txt
     ```
   - Start the backend server:  
     ```powershell
     python app/main.py
     ```

2. **Frontend Setup:**
   - Navigate to the `frontend/` directory.
   - Install Node dependencies:  
     ```powershell
     npm install
     ```
   - Run the development server:  
     ```powershell
     npm run dev
     ```

3. **Deployment:**
   - Use the provided `docker-compose.yml` in the `deploy/` directory to spin up both the backend and frontend containers:  
     ```powershell
     docker-compose up --build
     ```
   - Adjust `nginx.conf` as needed for reverse proxy configuration.

## Conclusion

The **Old Money Mansions** project leverages state-of-the-art AI to generate meticulously formatted articles about iconic estates, supported by real-time fact-checking and media conversion. With a clear separation of concerns and a robust deployment pipeline, this project is designed for maintainability, scalability, and ease of use.

For further details, please refer to the documentation in the `docs/` folder or the Jupyter notebooks in `notebooks/`.

Happy coding and content creating!
