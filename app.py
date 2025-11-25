from flask import Flask
from calculator import add

app = Flask(__name__)

@app.get("/")
def home():
    # Använd din befintliga add-funktion, bara för att visa koppling
    result = add(2, 3)
    return f"CI/CD funkar! 2 + 3 = {result}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
