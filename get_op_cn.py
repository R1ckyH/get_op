# -*- coding: utf-8 -*-
from mcdreforged.api.types import *
from mcdreforged.api.command import *

PLUGIN_METADATA = {
    'id': 'get_op',
    'version': '1.2.1-cn',
    'name': 'get_op_cn',
    'description': '一个可以轻松拿到op的插件',
    'author': 'ricky',
    'link': 'https://github.com/rickyhoho/get_op',
    'dependencies': {
        'mcdreforged': '>=1.0.0'
    }
}


plugin = 'get_op'
prefix = '!!op'
systemreturn = '''§b[§rget_op§b] §r'''
last_player = 'test'
server_listen = False


def give_op(src : CommandSource):
    global server_listen, last_player
    last_player = src.get_info().player
    src.get_server().execute("op " + last_player)
    server_listen = True


def on_info(server : ServerInterface, info: Info):
    global server_listen
    if not info.is_player and server_listen:
        server_listen = False
        if info.content.startswith('Made'):
            server.tell(last_player, systemreturn + "你已经拿到op了")
        elif info.content.startswith("Nothing"):
            server.tell(last_player, systemreturn + "你早已经是op了")


def on_load(server : ServerInterface, old):
    server.register_help_message('!!op','一个可以轻松拿到op的插件')
    server.register_command(
        Literal(prefix).
        runs(give_op)
    )