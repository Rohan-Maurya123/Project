@echo off
.\venv\Scripts\python.exe -m streamlit run app/app.py --server.maxUploadSize=2000 --server.enableCORS=false --server.enableXsrfProtection=false --server.address=127.0.0.1
pause
