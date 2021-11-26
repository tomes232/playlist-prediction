# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 09:32:19 2020

@author: tomes
"""
import json
from qr_factorization import QR
data_file = "spotify_recSys_challenge2018/data/mpd.slice.0-999.json"
with open(data_file) as jsonfile:
    info, playlist = json.load(jsonfile)
qr = QR(playlist, len(playlist))
    
    