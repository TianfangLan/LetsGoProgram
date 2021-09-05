package InnerClass;


import java.util.ArrayList;
import java.util.LinkedList;

public class Album {

    private String name;
    private String artist;
    private SongList songs;

    public Album(String name, String artist) {
        this.name = name;
        this.artist = artist;
        songs = new SongList();
    }



    public boolean addSong(String title, double duration) {
        Song song = new Song(title,duration);
        return songs.add(song);
    }


    public boolean addToPlayList(int number, LinkedList<Song> playList){
        Song song = songs.findSong(number);
        if (song != null){
            playList.add(song);
            return true;
        }
        return false;
    }


    public boolean addToPlayList(String songName, LinkedList<Song> playList){
        Song song = songs.findSong(songName);
        if(song == null){
            return false;
        } else {
            playList.add(song);
            return true;
        }
    }

    public static class SongList{
        private ArrayList<Song> songs;

        private SongList() {
            songs = new ArrayList<Song>();
        }

        private boolean add(Song song){
            Song songInList = findSong(song.getTitle());
            if (songInList == null){
                songs.add(song);
                return true;
            }
            return false;
        }

        private Song findSong(int trackNumber){
            int index = trackNumber - 1;
            if (index < songs.size() && index >= 0){
                return songs.get(index);
            }
            return null;
        }

        private Song findSong(String title){
            for (int i = 0; i < songs.size(); i++){
                Song song = songs.get(i);
                if (song.getTitle().equals(title)){
                    return song;
                }
            }
            return null;
        }
    }
}
