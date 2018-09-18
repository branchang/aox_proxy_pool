# -*- coding: utf-8 -*-
import click
from script.check_proxy import check_proxy as check_proxy_shell
from script.sync_squid import update_squid_conf
from script.init import init as init_shell


@click.group()
def cli():
    pass


@click.command()
def check_proxy():
    check_proxy_shell().run()


@click.command()
@click.option('--default-conf-path', help='默认squid配置文件地址')
@click.option('--conf-path', help='配置文件地址')
def sync_squid_conf(default_conf_path, conf_path):
    update_squid_conf(default_conf_path, conf_path)


@click.command()
def init():
    init_shell()


cli.add_command(check_proxy)
cli.add_command(sync_squid_conf)
cli.add_command(init)
if __name__ == '__main__':
    cli()