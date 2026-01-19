# AI Assistant

This repository contains a proof-of-concept AI solution prepared in response to a client inquiry. Its purpose is to demonstrate the viability of the proposed concept and showcase our team's ability to deliver a functional AI solution.

## How to Set Up Enviroment Using Poetry

1. **Configure Python version**

   In `setup_python_env.sh`, set the `PYENV_LOCAL_VERSION` to the desired Python version (`3.11.0` is ideal for this project)

2. **Run the setup script**

   Execute `sh setup_python_env.sh` to configure the local Python version and install all required libraries from `pyproject.toml`

3. **Activate the Poetry environment**

   Run:

   ```bash
   poetry shell
   ```

   This will activate the virtual environment


4. **Open the project in VS Code (OPTIONAL, for development only)**

   Run:

   ```bash
   code .
   ```

**Notes:**

* Do not commit the `.venv/` directory or `poetry.lock` file when setting up the environment

* This setup ensures your Python version and dependencies match the project requirements


## Configure Environment Variables

1. Copy the `.env` file you received via email
2. Place it in the project root - same level as `env.example`


## Insert Data into Vector Database (Qdrant)

Function `process_pdf_all()` is currently commented out because all data have already been processed.

1. Pull the latest Qdrant image:

   ```bash
   docker compose pull qdrant
   ```

2. Start Qdrant:

   ```bash
   docker compose up -d --build qdrant
   ```

3. Run the data pipeline:

   ```bash
   python3 -m pipeline.main
   ```


## Run Microservices

Start the remaining microservices:

```bash
docker compose up -d --build ai_service api
```


## Test the Application

Open your browser and navigate to: [http://0.0.0.0:8080/](http://0.0.0.0:8080/)


## Test the Application

1. Open your browser
2. Navigate to: [http://0.0.0.0:8080/](http://0.0.0.0:8080/)
3. **Wait a few seconds** to allow all services to fully load before interacting with the application


## Swagger API Documentation (DEV)

* **AI Service**: [http://0.0.0.0:8080/docs](http://0.0.0.0:8080/docs)
* **AI Assistant API**: [http://0.0.0.0:8080/docs](http://0.0.0.0:8080/docs)

> You can use these endpoints to explore and test all available API routes with Swagger UI.
