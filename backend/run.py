from app import create_app

app = create_app()

@app.route("/")
def home():
    return {
        "status": "success",
        "message": "AI Code Review Assistant Backend Running"
    }

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)