from app import create_app

from pygit2 import Repository

app = create_app()
    
if __name__ == "__main__":
    from waitress import serve
    print("Hosting maid service started.")
    serve(app, host="0.0.0.0", port=5001)
    # if Repository(".").head.shorthand == "main":
    #     serve(app, host="0.0.0.0", port=5001)
    # else:
    #     app.run(host="0.0.0.0", port=5001, debug=True)