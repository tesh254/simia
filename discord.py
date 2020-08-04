import requests


def send_link(filename, link):
    payload = {"content": "🙌 File **" + filename +
               "** just completed upload. Link is ready on " + link}
    requests.post(
        "https://discordapp.com/api/webhooks/740227538588270643/ZfM_rlg2K4PVdkY8wnYUctrEQEMc-GbDQo5omH073iZnbTv1aUMrOwT9QXX95LF8t7nh", json=payload)
