# TCP-UDP-File-Transfer

TCP & UDP File Transfer with Chunks

### Goal
The goal is to apply the concepts learned in class, through programming and hands-on practice. At the end of this project, you will have a better understanding of how a networked application operates and what are the technologies behind it.

### Task
Design and implement a peer-to-peer file sharing application. The shared design document specifies the necessary protocols that you need to implement. Please follow the design doc closely (in fact, verbatim) in your implementation.


**Requirements:** The application should;

1. Have 4 processes: Chunk Announcer, Chunk Discovery, Chunk Downloader, Chunk Uploader. These processes should work as outlined in their respective specifications.
2. Successfully detect the available content in the peers in the Local Area Network.
3. Successfully download a content from other peers in the Local Area Network.
4. Display an error dialog if a download is in error.
5. Output a download/upload log, containing timestamps, names and chunk index of all downloaded files.


### Grading: 
- Your commit is complete (includes 4 processes (Chunk Announcer, Chunk Discovery, Chunk Downloader, Chunk Uploader), 1 README, 1 report) **(20 pts)**
- Your code can discover available users and note their chunks (15 pts), can periodically and correctly announce its local files **(15 pts)**
- can download chunks of a content from the network (15 pts), can display an error message if a particular chunk cannot be downloaded from target node **(5 pts)**
- can serve chunks of other users’ content **(10 pts)**
- can correctly output a download/upload log under the same directory **(10 pts)**
- seamless user interactions (e.g., displaying the available chunks, displaying the successfully downloaded chunk info, etc.) **(10 pts)**

Anything else is a bonus (e.g., displaying available users, displaying the available chunks in the network, etc.)
