# coding: utf8
import copy


plugin = 'get_op'
prefix = '!!op'
systemreturn = '''§b[§rget_op§b] §r'''
last_player = 'test'
server_listen = 0


def onServerInfo(server, info):
    global server_listen
    global last_player
    if server_listen == 1:
        server_listen = 0
        if info.content.startswith('Made'):
            server.tell(last_player, systemreturn + "You are op now!")
        elif info.content.startswith("Nothing"):
            server.tell(last_player, systemreturn + "You are already oped")
    elif info.isPlayer == 1:
        if info.content.startswith('!!op'):
            server_listen = 1
            last_player = info.player
            server.execute('op ' + info.player)


def on_load(server, old):
    server.add_help_message('!!op','A plugin that get op easily')
    
    
def on_info(server, info):
    info2 = copy.deepcopy(info)
    info2.isPlayer = info2.is_player
    onServerInfo(server, info2) 