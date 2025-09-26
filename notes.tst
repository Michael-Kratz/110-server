---- Create venv ----
WIN py/python -m venv venv
MAC python3 -m venv venv


---- Activate the venv ----
WIN venv\Scripts\activate
Mac source venv/bin/activate

---- Install Flask ----
pip install Flask


---- Run App ----
WIN py/python server.py
Mac python3 server.py