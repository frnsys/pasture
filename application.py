from app import app, socketio

if __name__ == '__main__':
    # For debugging.
    #from gevent import monkey
    #monkey.patch_all()
    #app.debug = True

    socketio.run(app, port=5001)
