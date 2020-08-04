import libtorrent as lt
import time
import sys
from upload import upload


link = sys.argv[1]


def torrent():
    '''Download a magnet link'''

    ses = lt.session()
    ses.listen_on(6881, 6891)
    params = {'save_path': './Downloads'}

    h = lt.add_magnet_uri(ses, link, params)
    print("starting", h.name())

    while not h.is_seed():
        s = h.status()

        state_str = [
            "queued",
            "checking",
            "downloading metadata",
            "downloading",
            "finished",
            "seeding",
            "allocating",
            "checking fastresume",
        ]
        print(
            "\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s"
            % (
                s.progress * 100,
                s.download_rate / 1000,
                s.upload_rate / 1000,
                s.num_peers,
                state_str[s.state],
            )
        )
        sys.stdout.flush()
        time.sleep(1)

    print(h.name(), "complete")
    upload(h.name())


torrent()
