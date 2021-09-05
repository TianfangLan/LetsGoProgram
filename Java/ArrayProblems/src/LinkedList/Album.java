package LinkedList;

import java.util.ArrayList;
import java.util.LinkedList;

public class Album {

    private String name;
    private String artist;
    private ArrayList<Song> songs;

    public Album(String name, String artist) {
        this.name = name;
        this.artist = artist;
        songs = new ArrayList<Song>();
    }

    private Song findSong(String name) {
        for (int i = 0; i < songs.size(); i++) {
            // get the current song
            Song song = songs.get(i);
            // check whether the song is required one
            if (song.getTitle().equals(name)){
                return song;
            }
        }
        // reach here means the required song is not found
        return null;
    }


    public boolean addSong(String title, double duration) {
        // find the song, then check it is in the list or not.
        Song song = findSong(title);
        if(song != null){
            return false;
        } else {
            // song is not found, create the song and add it to the list
            songs.add(new Song(title, duration));
            return true;
        }
    }


    public boolean addToPlayList(int number, LinkedList<Song> playList){
        int index = number - 1;
        if (index >= 0 && index < songs.size()){
            playList.add(songs.get(index));
            return true;
        }
        return false;
    }


    public boolean addToPlayList(String songName, LinkedList<Song> playList){
        Song song = findSong(songName);
        if(song == null){
            return false;
        } else {
            playList.add(song);
            return true;
        }
    }
}
