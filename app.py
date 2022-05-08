from webapp import  create_app
app = create_app()

if __name__ == "__main__":
    # from werkzeug.middleware.profiler import ProfilerMiddleware
    # app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[5], profile_dir='./profile')
    app.run(debug=True, host="0.0.0.0", port=80, threaded=True)