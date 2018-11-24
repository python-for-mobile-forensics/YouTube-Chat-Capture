# Chat Transcript Capture

YouTube enables live chat by default on live stream videos. This allows users
to chat with the live streamer while they film their video. This chat is then
bundled and replayed by default when the user finishes publishing their live
video as an archive. You can follow along with the chat on the right side of
the video as it plays.

## How To

1. Install [burpsuite][burp]

2. Begin running the burp proxy on port 8080

3. Open the Proxy -> Options. In the Proxy Listeners section add a new interface.
   Set Interface to 127.0.0.1:8080 and make sure the Running checkbox is enabled.
   Navigate to http://127.0.0.1:8080/ in Firefox, click the CA Certificate link at
   top right and save the certificate file somewhere.

   In Firefox open the Preferences window and go to Advanced -> Certificates ->
   View Certificates. Click Import and select the file. Check the Trust this CA to
   identify websites checkbox and click OK.

4. Add the burp proxy to firefox in the settings

5. Open the video in youtube and allow the video to play while capturing all traffic

6. Save all of the chat.json files. It is easy to find them by doing a ctrl-f
   and searching for keywords from the chat.

7. Fill a folder with 01.json to XX.json of the chat logs and run 
   `chatcap.py 01.json` for each file. You can do this with a loop.

8. Open output.csv in vim and run `:sort u`

9. Save the file as 'sorted_output.csv' and you now have all chat logs.

[burp]: https://wiki.archlinux.org/index.php/Burp_suite
