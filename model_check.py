import joblib

print("--- Checking model.pkl ---", flush=True)
try:
    # Try loading the file with joblib
    model = joblib.load('model.pkl')
    print("RESULT: This appears to be a valid joblib model file.", flush=True)

except FileNotFoundError:
    print("RESULT: The file 'model.pkl' was not found in this directory.", flush=True)
except Exception as e:
    print(f"RESULT: An error occurred while loading the file:\n{e}", flush=True)

print("Script ran to completion.", flush=True)
