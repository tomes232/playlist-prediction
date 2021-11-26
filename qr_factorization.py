# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

class QR(object):
    def __init__(self, playist_dict, size):
        self.song_dict = {}
        self.size = size
        self.matrix = []
        self.fill(playist_dict)
        self.create_matrix()
        self.Q, self.R = np.linalg.qr(self.matrix)
        
    def fill(self, playlist_dict):
        k = 0
        for playlist in playlist_dict:
            for song in playlist["tracks"]:
                self.load_song(song["track_name"], k)
            k += 1
    
    def load_song(self, song_name, k):
        if self.song_dict.get(song_name) is not None:
            self.song_dict[song_name][k] = 1
        else:
            self.song_dict[song_name] = np.zeros(self.size)
            self.song_dict[song_name][k] = 1 
            
    def create_matrix(self):
        for track in self.song_dict:
            self.matrix.append(self.song_dict[track])
            