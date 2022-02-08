# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import transmissionrpc

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Conecta com servidor transmission
    tc = transmissionrpc.Client('localhost', port=9091, user='admin', password='admin')


    # Adiciona torrent usando magnet link
    tc.add_torrent('magnet:?xt=urn:btih:WMDFQSLVTR5GPD2JM677ZLUCVQXNIVJP&dn=CentOS-7-x86_64-Everything-2009&tr=http%3A%2F%2Ftorrent.centos.org%3A6969%2Fannounce', download_dir='/tmp/')

    # Adiciona torrent usando .torrent
    tc.add_torrent('http://releases.ubuntu.com/21.10/ubuntu-21.10-desktop-amd64.iso.torrent?_ga=2.195840812.1240085733.1643922660-111294250.1643922660', download_dir='/tmp/')

    # Percorre torrents e lista status
    for torrent in tc.get_torrents():
        print(torrent.id)
        print(torrent.files())
        print(torrent.status)
        print(torrent.progress)
        print(torrent.ratio)
        # print(torrent.files())
        # print(torrent.downloadDir)
        # print(torrent.creator)
        # print(torrent.magnetLink)
        print(torrent.hashString)
        print(torrent.format_eta())
        print(torrent.trackerStats)
        # print(torrent._fields)


        # Move arquivos do torrent e continua a transmitir
        # tc.move_torrent_data(4, '/tmp')
