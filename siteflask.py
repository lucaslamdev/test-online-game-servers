from flask import Flask, request, render_template, jsonify
from time import sleep
from turbo_flask import Turbo, turbo
import verificar
import threading
import psutil

app = Flask(__name__)
turbo = Turbo(app)

usocpu = int()


@app.route('/')
def index():
    global ip
    ip = request.remote_addr
    return render_template('index.html')


@app.context_processor
def atualizar():
    global usocpu
    ms = verificar.pingar(ip)

    if verificar.minecraft():
        minecraft = 'ONLINE'
    else:
        minecraft = 'OFFLINE'

    if verificar.terraria():
        terraria = 'ONLINE'
    else:
        terraria = 'OFFLINE'

    if verificar.minecraftmods():
        minecraftmods = 'ONLINE'
    else:
        minecraftmods = 'OFFLINE'

    return {'usocpu': usocpu, 'ms': ms, 'minecraft': minecraft, 'terraria': terraria, 'minecraftmods': minecraftmods}


def atualizar_dados():
    with app.app_context():
        while True:
            sleep(1)

            if verificar.minecraft():
                turbo.push(turbo.update('ONLINE', 'minecraft'))
            else:
                turbo.push(turbo.update('OFFLINE', 'minecraft'))

            if verificar.terraria():
                turbo.push(turbo.update('ONLINE', 'terraria'))
            else:
                turbo.push(turbo.update('OFFLINE', 'terraria'))

            if verificar.minecraftmods():
                turbo.push(turbo.update('ONLINE', 'minecraftmods'))
            else:
                turbo.push(turbo.update('OFFLINE', 'minecraftmods'))

            turbo.push(turbo.update(psutil.cpu_percent(), 'usocpu'))


@app.before_first_request
def before_first_request():
    print('Conectou a primeira pessoa!')
    threading.Thread(target=atualizar_dados).start()


app.run(debug=True, port=8080)
