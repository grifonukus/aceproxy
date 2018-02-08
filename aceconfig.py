'''
AceProxy configuration scrip
Edit this file.
'''
import colorer,logging
import acedefconfig
from aceclient.acemessages import AceConst

class AceConfig(acedefconfig.AceDefConfig):
    # ----------------------------------------------------
    # Ace Stream Engine configuration
    # ----------------------------------------------------
    #
    # Spawn Ace Stream Engine automatically
    acespawn = False
    # Ace Stream cmd line (use `--log-file filepath` to write log)
    # Autodetect for Windows
    acecmd = "acestreamengine --client-console"
    # Ace Stream API key You probably shouldn't touch this
    acekey = 'n51LvQoTlJzNGaFxseRK-uvnvX-sD4Vm5Axwmc4UcoD-jruxmKsuJaH0eVgE'
    # List of available AceStream Engines
    # Remember that by default Ace Stream Engine listens only Local host IP, so start it with --bind-all parameter
    # if you want to use it in remote access mode
    # Example string for AceEngine parameters ['AceEngineIP', aceAPIport, aceHTTPport]
    # You can change Engine API port or Engine HTTP port by using --api-port= or --http-port= in startup parameters.
    # Default values is --api-port=62062 --http-port=6878
    acehostslist =(
                   ['127.0.0.1', 62062, 6878],
                   )
    # Ace Stream age parameter (LT_13, 13_17, 18_24, 25_34, 35_44, 45_54,
    # 55_64, GT_65)
    aceage = AceConst.AGE_35_44
    # Ace Stream sex parameter (MALE or FEMALE)
    acesex = AceConst.SEX_MALE
    # Ace Stream Engine startup timeou
    # On Windows Ace Engine refreshes acestream.port file only after loading GUI
    # Loading takes about ~10 seconds and we need to wait before taking port out of i
    # Set this to 0 if you don't use proxy at startup or don't need to wai
    # Only applies to Windows systems
    acestartuptimeout = 25
    # Ace Stream Engine connection timeou
    aceconntimeout = 5
    # Ace Stream Engine authentication result timeou
    aceresulttimeout = 10
    #
    # ----------------------------------------------------
    # AceProxy configuration
    # ----------------------------------------------------
    #
    # HTTP Server port
    httpport = 8000
    # Read the video input stream in chunks of the following size
    # Don't set more then 8192 -  https://hg.python.org/cpython/file/84cd07899baf/Objects/fileobject.c#l2313
    readchunksize = 8192
    # Cache the following number of the tailing chunks
    readcachesize = 1024
    # If started as root, drop privileges to this user.
    # Leave empty to disable.
    aceproxyuser = ''
    # Enable firewall
    firewall = False
    # Firewall mode. True for blackilst, False for whitelis
    firewallblacklistmode = False
    # Network ranges. Please don't forget about comma in the end
    # of every range, especially if there is only one.
    firewallnetranges = (
        '127.0.0.1',
        '192.168.0.0/16',
        )
    # Maximum concurrent connections (video clients)
    maxconns = 10
    #
    # ----------------------------------------------------
    # VLC configuration
    # ----------------------------------------------------
    #
    # Use VideoLAN VLC Media Player as broadcast
    # To use this, you should install VLC firs
    vlcuse = False                                                                                                                                          
    # Use AceStream player that comes with engine                                                                                                             
    # If true than proxy will detect a path to ace_player.exe and ace_player.exe will be spawned                                                              
    # It also will not check if vlc.exe is running, it will watch over ace_player.exe process                                                                 
    # This option applies only for Windows systems to point ace_player.exe, not vlc.exe!!!  
    vlcuseaceplayer = False
    # Spawn VLC automaticaly
    vlcspawn = False
    # VLC host
    vlchost = '127.0.0.1'
    # VLC telnet interface port
    vlcport = 4212
    # VLC telnet interface password
    vlcpass = 'admin'
    # VLC cmd line (use `--file-logging --logfile=filepath` to write log)
    vlccmd = 'vlc -I telnet --telnet-host %s --clock-jitter=0 --clock-synchro=0 --telnet-password %s --telnet-port %d' %(vlchost,vlcpass,vlcport)
    # VLC spawn timeout
    # Adjust this if you get error 'Cannot spawn VLC!'
    vlcspawntimeout = 5
    # VLC streaming port (you shouldn't set it in VLC itself)
    vlcoutport = 8082
    # Pre-access (HTTP) VLC parameters
    # You can add transcode options here
    # Something like #transcode{acodec=mpga,ab=128,channels=2,samplerate=44100}
    vlcpreaccess = ''
    # VLC muxer. You probably want one of these streamable muxers:
    # ts, asf, flv, ogg, mkv
    # You can use ffmpeg muxers too, if your VLC is built with i
    # ffmpeg{mux=NAME} (i.e. ffmpeg{mux=mpegts})
    # VLC's ts muxer sometimes can work badly, but that's the best choice for
    # now.
    vlcmux = 'ts{use-key-frames}'
    # Force ffmpeg INPUT demuxer in VLC. Sometimes can help.
    vlcforceffmpeg = False
    #
    # ----------------------------------------------------
    # Transcoding configuration
    # ----------------------------------------------------
    # Enable/disable transcoding
    transcode = False
    # Dictionary with a set of transcoding commands. Transcoding command is an
    # executable commandline expression that reads an input stream from STDIN
    # and writes a transcoded stream to STDOUT. The commands are selected
    # according to the value of the 'fmt' request parameter. For example, the
    # following url:
    # http://loclahost:8000/channels/?type=m3u&fmt=mp2
    # contains the fmt=mp2. It means that the 'mp2' command will  be used for
    # transcoding. You may add any number of commands to this dictionary.
    transcodecmd = dict()
    # transcodecmd['100k'] = 'ffmpeg -i - -c:a copy -b 100k -f mpegts -'
    # transcodecmd['mp2'] = 'ffmpeg -i - -c:a mp2 -c:v mpeg2video -f mpegts -qscale:v 2 -'.split()
    # transcodecmd['mkv'] = 'ffmpeg -hide_banner -nostats -loglevel info -i - -map 0 -c:v copy -c:a copy -f matroska -'.split()
    # transcodecmd['hls'] = 'ffmpeg -hide_banner -nostats -loglevel info -i - -map 0 -c copy -force_key_frames "expr:gte(t,n_forced*2)" -f hls -start_number 0 -hls_time 6 -hls_playlist_type event -hls_allow_cache 1 -hls_flags single_file+split_by_time+delete_segments+omit_endlist+append_list -'.split()
    # transcodecmd['default'] = 'ffmpeg -hide_banner -nostats -loglevel panic -i - -map 0 -c:a copy -c:v copy -f mpegts -'.split()
    # ----------------------------------------------------
    # Transcoding configuration for HLS
    # ----------------------------------------------------
    # If you use acestream engine ver >= 3.1.5 and vlcuse=True
    # proxy automaticaly switch to HLS (HTTP Live Streaming) instead of HTTP Progressive Download
    # You can use this settings for audio transcoding. This option applies only for Live-stream
    # ---------------------------------------------------
    # Transcode All audio to AAC
    transcode_audio = 0
    # Transcode MP3 (use only when transcode_audio=1)
    transcode_mp3 = 0
    # Transcode only AC3 to AAC (use only when transcode_audio=0)
    transcode_ac3 = 0
    # Prefered audio language in translation on start http://xml.coverpages.org/nisoLang3-1994.html
    preferred_audio_language = 'rus'
    # ----------------------------------------------------
    # Seek back feature.
    # Seeks stream back for specified amount of seconds.
    # Greatly helps fighing AceSteam lags, but introduces
    # video stream delay.
    # Set it to 30 or so.
    # Works only with the newest versions of AceEngine!
    videoseekback = 0
    # Waiting time response from AceEngine server for playable url. In seconds.
    videotimeout = 30
    #
    # Some video players (mostly STBs and Smart TVs) can generate dummy requests
    # to detect MIME-type or something before playing which Ace Stream handles badly.
    # We send them 200 OK and do nothing.
    # We add their User-Agents here
    fakeuas = ('Mozilla/5.0 IMC plugin Macintosh', )
    #
    # Some video players have very short timeout and can disconnect from the proxy
    # before the headers sent.
    # We send them 200 OK and MPEG MIME-type right after connection has been initiated
    fakeheaderuas = ('HLS Client/2.0 (compatible; LG NetCast.TV-2012)',
                     'Mozilla/5.0 (DirectFB; Linux armv7l) AppleWebKit/534.26+ (KHTML, like Gecko) Version/5.0 Safari/534.26+ LG Browser/5.00.00(+mouse+3D+SCREEN+TUNER; LGE; 42LM670T-ZA; 04.41.03; 0x00000001;); LG NetCast.TV-2012 0'
                     )
    # Logging configuration
    #
    # Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    loglevel = logging.INFO
    # Log message forma
    logfmt = '%(filename)-20s [LINE:%(lineno)-4s]# %(levelname)-8s [%(asctime)s]  %(message)s'
    # Log date forma
    logdatefmt='%d.%m %H:%M:%S'
    # Full path to a log file
    logfile = None

    # This method is used to detect fake requests. Some players send such
    # requests in order to detect the MIME type and/or check the stream availability.
    @staticmethod
    def isFakeRequest(path, params, headers):
        useragent = headers.get('User-Agent')

        if not useragent:
            return False
        elif useragent in AceConfig.fakeuas:
            return True
        elif useragent == 'Lavf/55.33.100' and not headers.has_key('Range'):
            return True
        elif useragent == 'GStreamer souphttpsrc (compatible; LG NetCast.TV-2013) libsoup/2.34.2' and headers.get('icy-metadata') != '1':
            return True

