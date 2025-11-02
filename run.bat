@echo off
echo ==========================================
echo   Starting AURA MVP - Burnout Detection
echo ==========================================
echo.

if not exist "venv\" (
    echo Virtual environment not found. Creating one...
    python -m venv venv
    call venv\Scripts\activate
    echo Installing dependencies...
    pip install -r Requirments.txt
) else (
    call venv\Scripts\activate
)

echo Launching Streamlit app...
streamlit run app.py
pause