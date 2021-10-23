# -*- coding: utf-8 -*-
from mcdreforged.api.types import *
from mcdreforged.api.command import *

PLUGIN_METADATA = {
    'id': 'get_op',
    'version': '1.2.1',
    'name': 'get_op',
    'description': 'A plugin that can get op permission easily',
    'author': 'ricky',
    'link': 'https://github.com/R1ckyH/get_op',
    'dependencies': {
        'mcdreforged': '>=1.0.0'
    }
}


plugin = 'get_op'
prefix = '!!op'
system_return = '''§b[§rget_op§b] §r'''
error = system_return + '''§cError: '''
error_permission = error + '你没有权限去使用此指令'

last_player = 'test'
server_listen = 0


def error_msg(server, player, num):
    if num == 0:
        server.tell(player, error_permission)


def op_sur(server, player):
    server.execute('op ' + player)
    server.tell(player, system_return + '你会获得60秒op')
    time.sleep(60)
    server.execute('deop ' + player)
    server.tell(player, system_return +'你的op时间完结了，已回收op权限')




def on_info(server, info):
    global server_listen
    if info.isPlayer == 1:
        if info.content.startswith('!!op'):
            if server.get_permission_level(info.player) > 2:
                op_sur(server, info.player)
            else:
                error_msg(server, info.player, 0)


def on_load(server, old):
    server.register_help_message('!!op','轻松可以拿到op的插件')
