from app import create_app

application = create_app()

if __name__ == "__main__":
    from os import environ
    port = int(environ.get("PORT", 8080))
    application.run(host="0.0.0.0", port=port, debug=True)