[0.00 --> 18.42]  Welcome to the ChangeLog episode 0.3.4.
[18.64 --> 19.70]  I'm Adam Stachowiak.
[19.90 --> 20.70]  And I'm Wynne Netherland.
[20.84 --> 21.76]  This is the ChangeLog.
[21.80 --> 23.62]  We cover what's fresh and new in the world of open source.
[24.14 --> 27.10]  If you found us on iTunes, we're also on the web at thechangelog.com.
[27.44 --> 28.18]  We're also up on GitHub.
[28.18 --> 30.56]  Head to GitHub.com forward slash explore.
[30.66 --> 35.16]  You'll find some trending repos, some feature repos from our blog, as well as the audio podcasts.
[35.72 --> 37.74]  And if you're on Twitter, follow ChangeLogShow.
[38.00 --> 38.78]  And I'm Adam Stach.
[39.10 --> 41.24]  And I'm Penguin, P-E-N-G-W-Y-N-N.
[41.68 --> 42.56]  Fun episode this week.
[42.62 --> 44.56]  Talked to Zed Shaw of Mongrel 2.
[45.08 --> 48.36]  Chatted up his new project as well as Python and guitars.
[49.22 --> 49.40]  Yeah.
[50.18 --> 53.32]  Speaking of Python, we got the Django Dash guys coming up next week as well.
[53.72 --> 54.82]  Yeah, that was a fun episode too.
[54.82 --> 59.22]  Just with five people, it got sort of hairy to edit, I take it.
[59.34 --> 61.34]  It always helps one of the co-hosts doesn't hit record.
[61.70 --> 64.98]  Yeah, it does make it a little bit difficult in the post-production process.
[65.38 --> 66.86]  Well, it's a longish interview this week.
[66.90 --> 67.84]  I think around 40 minutes.
[68.10 --> 70.02]  So should we cut the banner and get to it?
[70.20 --> 70.74]  Let's do it.
[70.74 --> 71.24]  Cool.
[80.34 --> 83.32]  Chatting today with Zed Shaw from Mongrel 2 project.
[83.84 --> 87.22]  So Zed, for those guys out there that might not know who you are, why don't you introduce yourself
[87.22 --> 89.52]  and just let us know a little bit about your background.
[90.68 --> 91.04]  Hi.
[91.22 --> 92.02]  So I'm Zed Shaw.
[92.24 --> 94.86]  And I've been programming for a really long time.
[94.86 --> 101.76]  Some of you of me, if you're in the Ruby world, probably know me, both because you use my software,
[101.92 --> 107.12]  but also because I'm a pretty prolific blogger and I've written some things.
[108.10 --> 113.12]  And currently I'm working on my new thing, which is kind of like the new version of Mongrel, Mongrel 2.
[113.38 --> 115.80]  I couldn't think of a better name, so I went with Mongrel 2.
[116.56 --> 119.64]  And it's basically just a super badass web server.
[119.64 --> 128.94]  So we asked some questions informally on IRC earlier as far as what guys wanted to know about Mongrel 2.
[129.10 --> 130.96]  So one of the questions was, what happened to Mongrel 1?
[132.06 --> 136.50]  Oh, well, Mongrel 1, so I basically got out of the Ruby community.
[137.14 --> 144.94]  And rather than leave all my projects in the wind like Y did, I went and gave it up and basically got a hold of the guys
[144.94 --> 146.72]  who were mostly doing most of the work.
[146.72 --> 152.82]  By the time I left, it was actually Luis Lavena and a few other folks who were doing a lot of the Mongrel maintenance.
[153.28 --> 154.38]  And so I just left it to them.
[155.16 --> 160.10]  And they moved it around a bunch and they quit updating the docs, but they kept the software going.
[160.48 --> 163.28]  And they basically maintain it and keep it working.
[164.12 --> 169.20]  And then I guess the other thing that I could say happened to it is all these other web servers started carving it up
[169.20 --> 171.22]  and coming up with their rendition of it.
[171.22 --> 176.12]  So that's where you get Unicorn and Thin and there's a whole bunch of other ones that are based on it.
[177.58 --> 180.54]  What's the main selling point of Mongrel 2 over the previous versions?
[181.74 --> 185.92]  Well, so the Mongrel 2, the main selling point is that it's written totally in C.
[186.14 --> 187.12]  So that's the first thing.
[187.26 --> 190.38]  So you don't have to worry about any of the Ruby stuff.
[190.98 --> 197.40]  And it's actually fairly disconnected from Ruby, except for the main part is that I reused the parser that I wrote for Mongrel.
[197.40 --> 207.78]  And its biggest part is that it's completely asynchronous and it works with this awesome messaging kind of super socket protocol called ZeroMQ.
[207.78 --> 216.28]  And what that gives you is the ability to write your application logic and your back end in any language pretty much.
[216.48 --> 219.38]  I think ZeroMQ is up to about 20 languages that it supports.
[219.88 --> 222.26]  And Mongrel 2 right now is up to 10.
[222.88 --> 224.14]  And one of those is .NET.
[224.14 --> 227.00]  So that's probably way more than even just the 10.
[227.70 --> 228.88]  And that's its main thing.
[228.98 --> 236.52]  I mean, basically what we pimp it as is this language agnostic app server, web server with the goal of hosting anything.
[236.76 --> 239.82]  We would just make it where it's dead easy to host everything that you've got.
[239.82 --> 242.76]  Quite the list of languages here.
[242.88 --> 248.48]  So Ruby, Python, C++, PHP, Haskell, Lisp, Perl, .NET, Clojure, and Lua.
[249.38 --> 251.52]  Who's got the most traction as far as those languages?
[252.44 --> 255.84]  Well, so the thing is, is we actually really haven't done a lot with it.
[255.92 --> 259.64]  It was so easy to crank out the protocol that everyone just wrote protocol bindings.
[259.82 --> 264.04]  And then the Ruby and the Python side, like on the Ruby side, there's Rack.
[264.20 --> 265.82]  And on the Python side, there's some Whiskey.
[265.82 --> 271.70]  But actually hosting languages is kind of like our version 2, like the next thing we're shooting for.
[272.32 --> 275.44]  So as far as traction goes, the project's only three months old.
[275.58 --> 277.58]  So we haven't actually hosted anything.
[278.14 --> 279.88]  There's people who are sitting down trying to use it.
[280.40 --> 285.58]  And we've now just started kind of, well, how do you actually host a Python thing on this thing?
[285.66 --> 287.10]  And how do you deploy it?
[287.16 --> 288.92]  And how do you make it less sucky?
[289.24 --> 292.92]  There's some odd stuff we cranked out real quick that we're going to rewrite and things like that.
[293.40 --> 295.04]  What do you see as the typical stack?
[295.04 --> 301.28]  Normally with the older version of Mongo, you would have some sort of front-end proxy in front of it.
[301.34 --> 303.10]  What would you do in the case of Mongo 2?
[304.30 --> 310.36]  So with the Mongo 2 setup, what I'm aiming for is, like some people have been trying to compare it to, say, Node.
[310.54 --> 312.32]  But that's not a really good comparison.
[312.54 --> 314.16]  There's a little bit of overlap with Node.
[314.26 --> 316.14]  But it's actually more of a different part of the stack.
[316.68 --> 322.54]  So I'm actually putting it more at either where you would have your Apache or your Nginx.
[322.54 --> 326.96]  I consider those more direct competitors or even maybe where you have your HAProxy.
[327.42 --> 340.60]  And I kind of consider like the architecture that Mongo 2 is shooting for is a collapser where you don't have to have as much HAProxy to an Nginx to an Nginx that runs your Rails, that kind of setup.
[340.60 --> 343.32]  You can actually just have a Mongo 2 that messages to everything.
[344.12 --> 349.72]  But right now, I would probably tell people, HAProxy goes to a Mongo 2, goes to your app.
[350.10 --> 351.88]  And you shouldn't have much more than that.
[352.02 --> 357.22]  Like you shouldn't have to put Nginxs and things in between or any other stuff like that.
[357.22 --> 363.40]  What's your take on the whole evented web design pattern that seems to be popular lately?
[364.58 --> 375.48]  So it's interesting because, yeah, like it's true that events, you know, things like ePoll and having event callbacks and stuff like that are actually faster than threads in certain cases.
[375.48 --> 378.80]  There's actually a few types of things that are better with threads.
[378.80 --> 382.94]  And I've been doing stuff like that for years.
[383.06 --> 384.96]  I mean, that's just kind of how you wrote web servers.
[385.20 --> 390.60]  It's almost kind of funny because these folks are making it seem like this fantastic new technology has been around forever.
[391.12 --> 392.88]  It's just now people kind of understand it.
[393.92 --> 396.64]  And what I see is, yeah, you know, events are great.
[396.64 --> 403.30]  But a lot of the systems that make you use events, it's almost like they shove it in your face and they don't give you anything nice to deal with it.
[403.52 --> 405.48]  So over on the Python side, there's Twisted.
[405.48 --> 410.60]  Over in Node, if you're in C and C++, you've got LibEvent and LibEV.
[411.18 --> 413.50]  And Ruby, you've got Event Machine and things like that.
[413.68 --> 417.66]  And they kind of just don't give you a lot of help other than calling your function and saying go.
[418.28 --> 427.70]  So I actually think that a lot of the event-based frameworks, either they're eventually going to invent some kind of state machine or some kind of coroutine.
[428.02 --> 431.54]  And they all need some kind of ring buffer of some kind.
[431.54 --> 438.04]  And if you don't know that, then you see people typically write event code and invent those things.
[438.24 --> 443.70]  Like they sort of do a state machine and it's all kind of half-assed or they sort of do a ring buffer, sort of half-assed.
[444.90 --> 451.54]  And so what I see is like you can actually probably simplify event systems a lot but still get all the same performance boosts.
[451.54 --> 455.30]  I know with Ruby applications, it normally is an all-or-none proposition.
[455.50 --> 459.00]  If you go the evented route, you seem to need libraries that are also evented.
[459.04 --> 461.26]  Is the same true with Python and some of the other languages?
[461.84 --> 464.24]  That's actually, I think, a core thing about events.
[464.34 --> 467.06]  It's nearly impossible to merge event systems.
[467.98 --> 473.30]  It's not impossible, but the stuff you have to do requires a non-event system to put it together.
[473.30 --> 477.34]  This is just something that that's how event systems work.
[477.54 --> 480.98]  And I haven't really ran into anything that makes it better.
[481.08 --> 487.32]  So let's say, for example, I've got 0MQ that's got its own little event loop.
[487.52 --> 490.88]  And then I've got LibEV, it's got its own event loop.
[490.98 --> 495.00]  And then I've got Ruby's pseudo-thready thing, which uses select and stuff like that.
[495.38 --> 498.62]  If I want to put those three together, I have to declare one of them the king.
[498.88 --> 500.86]  I usually have to use some kind of real thread.
[500.86 --> 504.66]  I have to do some kind of like maybe tossing events over a socket to the king.
[505.34 --> 507.54]  I have to do all sorts of weird stuff to make it work.
[508.16 --> 510.84]  And that's just like a universal thing about event systems.
[510.94 --> 512.66]  They just don't merge together very well.
[514.44 --> 515.92]  Let's talk about protocols for a moment.
[516.10 --> 520.34]  I seem to remember a blog post earlier, a couple of years ago maybe.
[520.80 --> 521.48]  Time flies.
[521.86 --> 529.06]  As far as HTTP and you feeling that it's probably the wrong protocol for a lot of things we do on the web,
[529.06 --> 533.96]  what do you see as a future protocol that could kind of overtake HTTP?
[535.30 --> 539.70]  So that's one of the things that I'm trying to do within the Mongrel 2 on the front-end side
[539.70 --> 546.72]  is sort of add the protocols that I think people actually could use for a lot of the async stuff.
[546.88 --> 553.88]  And the trend I'm seeing with web apps is it's actually going more async for a lot of the event notifications
[553.88 --> 557.00]  and a lot of your JavaScript front-ends and things like that.
[557.08 --> 557.90]  It just seems to work better.
[558.36 --> 565.36]  This is one of the reasons why Node is so nice because you can basically merge the events on the back-end to the front-end.
[566.32 --> 572.48]  And so the thing that I see as far as protocols go is like WebSockets is sort of getting it
[572.48 --> 579.84]  where the people who want to do the async, chatty-style, message-oriented stuff can use a WebSocket.
[580.80 --> 585.76]  And then if you want to do the heavy lifting, upload, download, grabbing files, that kind of thing, use HTTP.
[587.12 --> 594.74]  Back in the day, what I saw was this kind of bastardization of chunked-encodings and HTTP to invent this thing called long-pulling,
[595.14 --> 600.80]  which is just another word for never closing the socket, which for a lot of web servers is really bad.
[600.80 --> 604.74]  I mean, a web server is mostly designed that people are only there for a short period of time.
[605.30 --> 608.52]  So you can eat up resources and things like that.
[608.64 --> 612.72]  And then if you've got this guy who's keeping his long-pull open for a real long time,
[612.84 --> 616.74]  you're taking a web server that's designed for files and transmitting files,
[616.90 --> 620.82]  and then you're putting in a messaging, continuously connected kind of chat protocol.
[621.02 --> 622.88]  And a lot of web servers just break down for that.
[623.64 --> 627.24]  So what I'm shooting for in Mongo2 is it works for any of those patterns,
[627.24 --> 631.30]  the async, long-pull, message-oriented.
[631.86 --> 634.40]  And then if WebSockets come out, we're going to add WebSockets.
[634.68 --> 638.28]  If someone invents, like if Spidey becomes popular, we can throw in Spidey.
[638.88 --> 643.14]  I mean, the way we've designed it, we can pretty much put any protocol that becomes popular into the thing
[643.14 --> 646.38]  because it assumes nothing about the actual request-response model.
[647.38 --> 651.26]  What sort of applications are you building with these types of platforms?
[651.26 --> 656.20]  So the things that I'm actually interested in is mostly on the music hosting side
[656.20 --> 663.38]  and also on the more social chat or social code side,
[663.96 --> 665.62]  mostly just because I'm curious about it.
[665.88 --> 668.32]  I mean, for me, it's kind of cobbler's shoes stuff.
[668.38 --> 671.28]  I'm so busy actually working on Mongo2 and I don't have any time to work on this stuff.
[671.50 --> 673.98]  So I'm kind of just getting it out.
[673.98 --> 680.94]  But the main thing is I've got an idea for a little project that will sit and watch you code
[680.94 --> 685.22]  so people in a project can actually watch each other as they work on files
[685.22 --> 686.60]  and they can ask each other questions.
[686.72 --> 688.82]  So sort of like a weird code chat in a way,
[689.52 --> 692.04]  which every time I mention that to programmers, they go,
[692.14 --> 693.90]  oh, God, don't let my manager get a hold of that.
[694.16 --> 695.92]  He'll know I surf lolcats all day long.
[697.76 --> 702.54]  And then the other one is hosting music is kind of a pain in the ass.
[702.54 --> 706.30]  It's like I'm thinking in terms of a musician who doesn't really know a lot
[706.30 --> 710.18]  and doesn't want necessarily just a place to put their files,
[710.30 --> 716.16]  but an actual page, a small blog, places they're going to be playing next and hosting the music.
[716.78 --> 719.70]  And so that's kind of something I'm a little interested in.
[720.02 --> 723.00]  And then there's another project I've been toying with for a long time,
[723.00 --> 729.98]  which is the idea of like a music browser that more browsers the semantic web of liner notes, basically,
[729.98 --> 733.60]  like what's in a CD, who is the producer of this and that and things like that.
[733.72 --> 739.48]  And a lot of that's just kind of breaking out of the walled garden that gets created around music,
[739.60 --> 741.26]  like iTunes, things like that.
[742.22 --> 744.70]  But all those projects, you know, I'm working on Mongol, too,
[744.76 --> 746.34]  so I don't have a whole lot of time to tinker with them.
[747.32 --> 748.24]  Let's talk music for a second.
[748.32 --> 749.30]  So tell me about Fret War.
[750.42 --> 751.50]  So, yeah, so Fret War.
[751.50 --> 754.50]  That was my foray into products.
[755.52 --> 756.78]  So I moved out to San Francisco,
[757.14 --> 760.62]  and I'm still really into trying to get better at consumer products.
[760.76 --> 765.62]  Most of the stuff I do is I like to tell people I make products for people who make products for people.
[767.06 --> 769.22]  So it's like I make web servers and things like that,
[769.28 --> 770.32]  and out here people look at you and they go,
[770.42 --> 772.04]  oh, you're just a nerd, huh?
[772.70 --> 774.02]  They don't really care.
[774.78 --> 777.44]  And I've been doing that for years and years,
[777.62 --> 778.46]  and, you know, I'm a smart guy,
[778.46 --> 780.98]  so I said, hey, I'm going to try and make a few websites for fun.
[780.98 --> 784.20]  So I branched out all my blogs,
[784.44 --> 786.12]  and I started doing all sorts of art topics.
[786.68 --> 789.26]  And I'd actually, before moving out here,
[789.30 --> 793.80]  I spent about a year studying jazz guitar at a music school in New York.
[793.90 --> 795.86]  So I wanted to start putting up songs and stuff.
[796.06 --> 800.12]  And I kind of found I was in a rut where I would just practice the same crap all day long.
[800.22 --> 801.82]  So I came up with this idea for Fret War.
[802.02 --> 804.28]  Me and a bunch of friends, we'd come up with, like, a round,
[804.46 --> 806.44]  and people basically play the round.
[806.50 --> 807.62]  The round could be something like, you know,
[807.62 --> 810.90]  play a metal song in A Mixolodean or something.
[810.98 --> 811.32]  Something like that.
[811.82 --> 812.20]  A Mixolydian.
[812.70 --> 813.10]  Mixolodean.
[814.72 --> 816.26]  I believe that's channel 224.
[816.76 --> 817.24]  Yeah, yeah, yeah.
[817.46 --> 817.86]  Nickelodeon.
[818.08 --> 819.92]  The Nickelodeon mode.
[820.28 --> 823.68]  Anyways, and then what we'll do is they'll all do their own rendition of it,
[823.76 --> 826.28]  and the production value is a pretty high.
[826.28 --> 830.48]  I mean, if there's anything that shows at home recording is really easy.
[830.60 --> 834.14]  It's the fact that a lot of these guys come home after work on Friday.
[834.46 --> 838.98]  They figure out what they're going to do, and then on Saturday kind of craft up drum tracks,
[839.18 --> 844.86]  bass lines, whole guitar parts, their solo, everything, sound effects, and then they upload it.
[845.36 --> 847.88]  And then what we do is we go and you rate it, and we say, like, you know,
[847.92 --> 849.86]  but we like the sound quality, the tone of it.
[849.86 --> 854.60]  It's your interpretation was cool, and then people win rounds based on that.
[855.18 --> 856.74]  And it's like maybe 12 of us do it.
[857.52 --> 860.48]  You know, one of the apps that I'd like to see, we've talked about this,
[860.62 --> 862.80]  doing it for, like, the Rails Rumble or something like that.
[863.08 --> 865.66]  Are you familiar with Layer Tennis?
[866.56 --> 866.88]  No.
[866.88 --> 871.42]  On the design side, we have this, I think it's Koodle that puts it on Layer Tennis,
[871.92 --> 877.12]  that you upload a PSD, and you keep riffing on it back and forth to each side.
[877.22 --> 881.02]  Each designer keeps adding detail to the PSD and passing it back and forth.
[881.08 --> 882.36]  I'd like to do the same thing with riffs.
[882.84 --> 886.38]  Somebody lays down a bass track, and then you just keep uploading your version,
[886.56 --> 889.72]  your take on it, and see what you can make, kind of collaborating,
[889.86 --> 891.04]  but not exactly in real time.
[891.96 --> 892.48]  Yeah, yeah.
[892.56 --> 894.46]  I mean, there's all sorts of cool things.
[894.46 --> 898.92]  You know, basically, a lot of, like, the stuff I want to do with Marvel 2
[898.92 --> 900.58]  is just to make it easier to do that.
[900.68 --> 904.92]  Like, for example, we have a MP3 streaming demo, and it was easy.
[905.00 --> 910.78]  It's like that really crappy, icy protocol that was written by 95 right when HTTP came out.
[910.86 --> 912.06]  So it's totally not HTTP.
[912.74 --> 916.64]  It's like basically if some dude had Windows and a really tiny computer,
[916.78 --> 917.82]  this is the protocol he would do.
[918.02 --> 921.90]  You know, it's like hard-coded chunk lengths with a header
[921.90 --> 925.50]  that has to be a multiple of 16 in size, you know, and it's just streamed out.
[925.62 --> 929.14]  But, you know, we wrote that, and I can do really good uploaders.
[929.34 --> 932.22]  You know, a big problem is people have a hard time uploading their music,
[932.22 --> 935.40]  so I could actually have little desktop apps and things like that.
[935.64 --> 939.18]  And it's just that, you know, as I worked on Fretwar,
[939.26 --> 941.38]  it was so hard to actually get uploads working.
[941.56 --> 942.14]  We use email.
[942.14 --> 946.50]  So I have this other project, Lampson, that basically runs all of Fretwar.
[946.64 --> 951.04]  You email your jobs in and your description and everything, and it sets it up.
[951.94 --> 953.32]  And, you know, I want to get away from that.
[953.42 --> 955.02]  I want to make it where you can just upload the files.
[955.16 --> 955.94]  You can chat with people.
[956.08 --> 958.00]  You can do the golf a lot quicker, too, you know,
[958.00 --> 960.62]  where if it's more async, I could actually chat with you and go,
[960.68 --> 961.14]  how about this?
[961.18 --> 961.66]  How about that?
[961.72 --> 962.18]  How about this?
[962.22 --> 962.70]  How about that?
[962.84 --> 963.12]  You know?
[964.66 --> 967.88]  But right now, the current web stuff, it's just way too hard to do that.
[967.88 --> 970.80]  It just doesn't work for that kind of real-time music-y stuff.
[970.80 --> 973.96]  Speaking of email, talk to us about Liberalist.
[975.00 --> 975.98]  Oh, yeah, Liberalist.
[976.38 --> 980.40]  So I was working on Lampson, which is this mailing,
[980.78 --> 984.18]  basically it's like Rails or Django for email.
[984.60 --> 987.74]  And it's got some code in it that I think is just awesome.
[988.12 --> 990.06]  Like, Python's got pretty decent email support,
[990.20 --> 993.52]  and then I kept running into this mismatch because, like,
[993.80 --> 995.54]  email is pre-Unicode.
[995.54 --> 1000.90]  So everything you get is this weird, like, set of headers
[1000.90 --> 1002.62]  and weirdo encodings.
[1002.72 --> 1003.10]  It's bizarre.
[1003.68 --> 1006.74]  So I got code that basically cleans that up
[1006.74 --> 1008.08]  and turns it into pure Unicode.
[1008.28 --> 1008.92]  It's great.
[1009.06 --> 1011.06]  It's like my favorite piece of code in the last year or two.
[1012.22 --> 1013.74]  But it's mostly just this framework.
[1013.94 --> 1016.54]  And basically, emails come in, and you do stuff.
[1016.66 --> 1018.62]  You, like, reply and put crap in databases
[1018.62 --> 1020.76]  and do whatever you need, whatever you do in web.
[1021.52 --> 1023.04]  And one of the demos that came out of that
[1023.04 --> 1025.02]  was this little mailing list thing I call LibreList.
[1025.36 --> 1028.34]  And it literally takes emails, manages a mailing list,
[1028.96 --> 1030.24]  kind of hooks a little bit into Django,
[1030.80 --> 1033.14]  stores archives in JSON, things like that.
[1033.74 --> 1036.12]  And I had a whole bunch of people who emailed me.
[1036.20 --> 1038.04]  They go, hey, I really hate Google Groups.
[1038.20 --> 1039.20]  Like, Google Groups is awful.
[1039.46 --> 1040.08]  Tons of spam.
[1040.18 --> 1041.62]  It's hard to use unless you have Gmail.
[1042.32 --> 1043.26]  You know, it's just really awful.
[1043.26 --> 1045.76]  Could you just put this demo,
[1046.00 --> 1047.56]  this, like, mailing list demo up for us?
[1047.60 --> 1050.52]  So I threw it up, and I think a bunch of people used it.
[1050.82 --> 1052.68]  And, you know, more and more open source projects
[1052.68 --> 1054.82]  that are, like, on the smaller side try to use it.
[1055.94 --> 1059.76]  And I think it's up to maybe 2,000 people registered,
[1060.10 --> 1061.12]  a couple hundred projects.
[1061.38 --> 1062.72]  You know, and they don't get a high volume.
[1062.84 --> 1065.52]  They get, like, maybe one a month or one a week.
[1065.54 --> 1066.46]  But it works, you know.
[1066.54 --> 1067.62]  It's dead simple.
[1067.82 --> 1069.54]  It doesn't require much authentication
[1069.54 --> 1070.82]  or authorization or anything.
[1071.90 --> 1073.24]  How long have you been playing guitar?
[1074.30 --> 1076.92]  So I started playing guitar when I was 20.
[1077.36 --> 1078.04]  I was in the Army.
[1078.16 --> 1078.88]  I was really bored.
[1078.88 --> 1082.14]  So I had a friend who was a professional musician
[1082.14 --> 1082.76]  before joining.
[1083.10 --> 1084.84]  And he's like, well, you should play guitar.
[1085.62 --> 1086.60]  And I don't know why.
[1087.46 --> 1090.46]  So he got me, like, helped me pick out
[1090.46 --> 1091.98]  a little classical guitar
[1091.98 --> 1094.40]  and handed me the sheet music for Fur Elise.
[1095.06 --> 1097.56]  And I guess it was a test to see if I would actually do it.
[1097.60 --> 1098.86]  And I just sat there, and I, like,
[1099.24 --> 1100.74]  tried to play it over and over and over.
[1100.74 --> 1103.00]  And finally I could play Fur Elise,
[1103.28 --> 1105.64]  you know, like a bit, a good chunk of it.
[1106.12 --> 1108.70]  And he goes, wow, you can sort of play.
[1108.82 --> 1110.68]  All right, you should, like, you know, play this.
[1110.88 --> 1114.30]  And so since I was 20, I'm 36 now, so 16 years.
[1114.64 --> 1115.84]  But I never took it seriously.
[1116.04 --> 1117.26]  So you could actually probably say
[1117.26 --> 1118.70]  I've only been playing for, like, two years.
[1119.08 --> 1119.36]  You know?
[1119.36 --> 1124.36]  Because last, I guess, in 2008 or 2009,
[1125.08 --> 1127.04]  basically when I was working at Bear Stearns
[1127.04 --> 1127.68]  and they tanked,
[1128.40 --> 1130.04]  and I got a severance package.
[1130.20 --> 1131.16]  So I went and I'm like,
[1131.30 --> 1132.60]  well, I could take the severance package
[1132.60 --> 1134.20]  and maybe do a startup,
[1134.40 --> 1135.60]  or I could learn to play guitar.
[1136.20 --> 1140.32]  So Fur Elise is normally a piano arrangement.
[1141.46 --> 1145.08]  What's your take on tabs?
[1145.08 --> 1146.94]  Why do tab sites always suck?
[1148.16 --> 1149.18]  Oh, man, yeah.
[1149.36 --> 1150.88]  So, okay, so that would be another thing
[1150.88 --> 1152.74]  I would love to do is just nuke tab.
[1152.86 --> 1153.78]  There's a guy out there
[1153.78 --> 1158.38]  who's doing fantastic HTML5 canvas rendering
[1158.38 --> 1159.84]  for sheet music and for tab.
[1160.24 --> 1162.36]  I would totally just love to hook up with him
[1162.36 --> 1164.44]  and do, like, a site that did awesome tab.
[1165.08 --> 1168.02]  And I actually probably would say,
[1168.36 --> 1171.58]  yeah, basically you pay a very small fee
[1171.58 --> 1173.70]  just so that we don't have to run ads
[1173.70 --> 1175.12]  and make this site degenerate
[1175.12 --> 1178.06]  into, like, some ad spam horrible link farm, you know?
[1178.12 --> 1178.92]  As they always do.
[1178.92 --> 1180.04]  They always do.
[1180.12 --> 1180.62]  They're so awful.
[1180.70 --> 1181.98]  And I think there's, like,
[1182.02 --> 1183.98]  some one company that does them all
[1183.98 --> 1185.26]  because, like, they're all the same.
[1185.80 --> 1187.32]  You know, there's, like, a tiny little tab
[1187.32 --> 1188.10]  that's in the center
[1188.10 --> 1189.88]  that they ripped off of Muesnix
[1189.88 --> 1190.96]  or some other website.
[1191.16 --> 1192.20]  And then surrounding it
[1192.20 --> 1195.34]  is just every horrible guitar player.
[1196.30 --> 1198.16]  If I see one more ad for Slash,
[1198.18 --> 1199.52]  I'm seriously going to kill that dude.
[1199.70 --> 1201.52]  I mean, it's, like, awful.
[1201.88 --> 1203.30]  He's got picks, guitars.
[1203.90 --> 1204.70]  He sells everything.
[1204.70 --> 1205.90]  He's, like, the biggest pimp.
[1206.04 --> 1208.44]  And he's all over every, like, music site everywhere.
[1209.52 --> 1210.50]  And I don't know why.
[1210.68 --> 1212.82]  I mean, they get shut down quite often.
[1212.98 --> 1214.68]  So maybe they've got to pay some tithe
[1214.68 --> 1216.18]  to the music industry.
[1216.40 --> 1217.58]  I've got no idea why.
[1217.82 --> 1218.40]  But...
[1218.40 --> 1219.98]  That's got to be the only explanation.
[1220.28 --> 1220.84]  It's...
[1220.84 --> 1222.82]  There's no other reason why we're...
[1222.82 --> 1224.30]  Technically, we're the same
[1224.30 --> 1225.54]  that we were in the early 90s
[1225.54 --> 1226.80]  with the Olga archive,
[1226.94 --> 1228.60]  the online guitar archive,
[1228.68 --> 1229.58]  I think is the name of it.
[1229.94 --> 1230.56]  And basically,
[1230.76 --> 1232.28]  they're the same Usenet posts
[1232.28 --> 1233.34]  from the mid-90s
[1233.34 --> 1234.82]  just posted to the web
[1234.82 --> 1235.72]  with pop-up ads.
[1236.38 --> 1236.40]  Yeah.
[1236.40 --> 1238.48]  And people add more, you know.
[1238.58 --> 1239.76]  But, I mean, it's...
[1239.76 --> 1240.82]  I notice that, like,
[1241.54 --> 1242.82]  occasionally you'll get new stuff
[1242.82 --> 1244.30]  if it's, like, a new popular song.
[1244.90 --> 1246.34]  But I think the last...
[1246.34 --> 1248.62]  The last major, like, metal band
[1248.62 --> 1249.74]  I saw a lot of tab for,
[1249.86 --> 1250.84]  not that I look too often,
[1250.92 --> 1251.92]  but it was Death Clock.
[1252.50 --> 1253.06]  There was, like...
[1253.06 --> 1253.82]  People have just done
[1253.82 --> 1254.88]  tons and tons of tabs
[1254.88 --> 1257.92]  for this fake cartoon metal band,
[1258.00 --> 1258.24]  you know?
[1258.40 --> 1259.50]  And that was, like, it.
[1259.80 --> 1261.38]  You don't see hardly any jazz stuff.
[1261.48 --> 1262.94]  You see very little blues anymore.
[1263.62 --> 1264.94]  And it's because all the stuff
[1264.94 --> 1266.00]  that was, like, jazz and blues
[1266.00 --> 1267.32]  was taken from, you know,
[1267.80 --> 1268.70]  back in the...
[1268.70 --> 1270.06]  Or pre-internet
[1270.06 --> 1271.96]  or, you know, pre-web Usenet,
[1272.10 --> 1272.44]  you know?
[1273.66 --> 1274.24]  So, anyways,
[1274.30 --> 1274.98]  yeah, so I would love
[1274.98 --> 1275.92]  to have a better site
[1275.92 --> 1276.46]  that, you know,
[1276.46 --> 1277.42]  did nice rendering
[1277.42 --> 1278.82]  and, you know,
[1278.90 --> 1280.36]  you could upload the tab
[1280.36 --> 1281.44]  and it would figure it out.
[1281.76 --> 1283.08]  And then, you know,
[1283.12 --> 1284.80]  basically you do
[1284.80 --> 1285.94]  the licensing properly
[1285.94 --> 1287.58]  so people are paying a bit,
[1287.80 --> 1288.32]  but, you know,
[1288.36 --> 1289.08]  maybe it's...
[1289.08 --> 1289.98]  You're actually getting
[1289.98 --> 1290.86]  with the music industry
[1290.86 --> 1291.16]  and saying,
[1291.24 --> 1291.62]  hey, yeah,
[1291.64 --> 1292.18]  you guys could make
[1292.18 --> 1292.78]  some money here
[1292.78 --> 1293.12]  if you actually
[1293.12 --> 1294.24]  just give us your tab.
[1294.88 --> 1295.30]  You know,
[1295.30 --> 1296.04]  we'll give you a cut
[1296.04 --> 1296.80]  at whatever we sell.
[1297.24 --> 1297.68]  People are willing
[1297.68 --> 1298.26]  to pay for it
[1298.26 --> 1298.74]  while you're, like,
[1298.78 --> 1299.44]  leaving all this money
[1299.44 --> 1299.92]  on the table.
[1300.60 --> 1301.80]  So what do you rock out to
[1301.80 --> 1302.42]  when you're coding
[1302.42 --> 1303.18]  on Mongrel 2?
[1303.18 --> 1305.18]  Um, so...
[1305.76 --> 1307.64]  I had a Mac.
[1307.70 --> 1308.56]  I'm actually doing
[1308.56 --> 1310.08]  this talk on a Mac.
[1310.70 --> 1311.70]  And the problem is
[1311.70 --> 1313.12]  when you're writing software
[1313.12 --> 1314.48]  that's like Mongrel 2,
[1315.02 --> 1315.96]  Mac kind of sucks
[1315.96 --> 1316.60]  because, you know,
[1316.64 --> 1318.08]  their I.O. is not so great
[1318.08 --> 1319.92]  and the tools you have
[1319.92 --> 1320.50]  just don't work.
[1320.60 --> 1321.22]  So I went and got
[1321.22 --> 1322.86]  a little Linux laptop.
[1323.06 --> 1323.20]  You know,
[1323.46 --> 1324.02]  it's not little.
[1324.10 --> 1325.04]  It's actually a huge beast,
[1325.14 --> 1325.46]  but, you know,
[1325.46 --> 1326.74]  it's a cheapo Linux laptop.
[1327.24 --> 1328.98]  And Linux is so bad
[1328.98 --> 1329.70]  with sound
[1329.70 --> 1330.82]  that my headphones
[1330.82 --> 1331.48]  don't work.
[1331.48 --> 1332.84]  So, like,
[1332.88 --> 1333.74]  I plug my headphones in,
[1333.80 --> 1334.70]  the speakers turn off,
[1334.80 --> 1335.76]  and then my headphones,
[1335.90 --> 1337.00]  I can't hear any music.
[1337.20 --> 1339.36]  So I rock out to nothing now.
[1339.54 --> 1340.94]  I mean, I like...
[1340.94 --> 1342.08]  Because Linux has got...
[1342.08 --> 1343.20]  And every once in a while
[1343.20 --> 1343.94]  I'll play, like,
[1344.02 --> 1344.30]  you know,
[1344.30 --> 1345.08]  whatever happens to be
[1345.08 --> 1347.16]  on my MP3 trainer
[1347.16 --> 1348.08]  that I'm trying to learn.
[1348.18 --> 1348.52]  But, you know,
[1348.54 --> 1349.40]  that gets really boring.
[1350.08 --> 1351.42]  So, yeah,
[1351.60 --> 1352.74]  as soon as I can figure out
[1352.74 --> 1353.42]  how to get the freaking
[1353.42 --> 1354.14]  speakers to work.
[1354.40 --> 1355.02]  So for, like,
[1355.18 --> 1356.30]  I guess three months
[1356.30 --> 1357.10]  I haven't really listened
[1357.10 --> 1358.24]  to music while I code.
[1358.24 --> 1360.36]  But normally what I'll listen
[1360.36 --> 1361.96]  to is...
[1361.96 --> 1363.10]  I'll tend to...
[1363.10 --> 1364.52]  I tend to really like...
[1364.52 --> 1365.58]  And what I try to learn
[1365.58 --> 1366.80]  is old school jazz,
[1366.90 --> 1367.12]  you know,
[1367.24 --> 1368.62]  pre-bebop jazz
[1368.62 --> 1370.78]  with actual lyrics
[1370.78 --> 1371.70]  and people singing
[1371.70 --> 1373.14]  and, you know,
[1373.20 --> 1373.92]  tons of cheese.
[1374.16 --> 1375.06]  Like, I just love...
[1375.06 --> 1375.68]  I love jazz
[1375.68 --> 1376.98]  that's just dripping Velveeta,
[1377.22 --> 1377.52]  you know,
[1377.60 --> 1378.64]  like a stack
[1378.64 --> 1379.44]  of cheese sandwiches.
[1380.88 --> 1381.60]  Mostly because
[1381.60 --> 1382.66]  that's apparently
[1382.66 --> 1383.36]  about the only thing
[1383.36 --> 1384.20]  I can sing well.
[1384.70 --> 1386.54]  So I've got the perfect
[1386.54 --> 1387.12]  lounge voice
[1387.12 --> 1387.56]  and that's it.
[1387.62 --> 1388.46]  I can't do anything else.
[1389.56 --> 1391.14]  And so I do that
[1391.14 --> 1392.18]  and then every once in a while
[1392.18 --> 1393.46]  I'll turn on some metal.
[1394.84 --> 1395.78]  Like older...
[1395.78 --> 1396.52]  Like, not new metal
[1396.52 --> 1397.36]  but the old school stuff.
[1397.60 --> 1397.92]  Pantera,
[1398.42 --> 1398.86]  Slayer,
[1399.86 --> 1400.44]  Metallica,
[1401.18 --> 1403.68]  pre-Black Album Metallica.
[1404.42 --> 1405.26]  And then,
[1405.40 --> 1405.94]  you know,
[1405.96 --> 1407.06]  I like a lot of just...
[1407.06 --> 1407.88]  Oh, I've gotten into
[1407.88 --> 1408.54]  country lately.
[1408.94 --> 1409.92]  Mostly because of just...
[1409.92 --> 1409.94]  Oh, yeah?
[1410.28 --> 1411.04]  Oh, yeah, yeah.
[1411.32 --> 1411.74]  So, like,
[1411.76 --> 1412.82]  country is awesome
[1412.82 --> 1414.32]  if they don't sing.
[1414.62 --> 1415.18]  Like, if you listen
[1415.18 --> 1415.88]  to the musicians,
[1416.14 --> 1416.80]  country's the shit.
[1416.80 --> 1417.34]  Like, those dudes
[1417.34 --> 1418.70]  are so awesome.
[1418.90 --> 1419.34]  Like, you listen
[1419.34 --> 1419.92]  to the guitarists,
[1419.94 --> 1420.68]  they're just insane.
[1421.80 --> 1422.14]  You know,
[1422.14 --> 1423.16]  the mandolin guys,
[1423.28 --> 1423.92]  bluegrass guys,
[1424.00 --> 1424.46]  but then when they
[1424.46 --> 1424.96]  start singing
[1424.96 --> 1426.02]  that nasal twang,
[1426.12 --> 1426.54]  you're just like,
[1426.66 --> 1427.00]  oh!
[1427.64 --> 1428.36]  And I'm like,
[1428.44 --> 1429.82]  I'm sort of from Texas.
[1429.82 --> 1430.62]  I was born there.
[1430.74 --> 1431.18]  I, you know,
[1431.20 --> 1432.12]  traveled around a lot,
[1432.20 --> 1433.60]  but it's like,
[1433.64 --> 1434.52]  I'll listen to that stuff
[1434.52 --> 1435.32]  and I can listen
[1435.32 --> 1436.20]  for a little while
[1436.20 --> 1436.70]  and then I'm like,
[1436.76 --> 1437.00]  oh!
[1438.00 --> 1438.82]  I think in other music
[1438.82 --> 1440.04]  like that's reggae.
[1440.58 --> 1441.42]  Like, I can listen
[1441.42 --> 1442.02]  to reggae for about
[1442.02 --> 1442.82]  two hours and I go,
[1442.90 --> 1443.46]  oh, if this dude
[1443.46 --> 1444.52]  plays on the two and four
[1444.52 --> 1444.94]  anymore,
[1445.02 --> 1445.62]  I'm going to kill him.
[1445.62 --> 1446.90]  You know, it's just like
[1446.90 --> 1448.22]  every genre when it comes out
[1448.22 --> 1448.72]  is groundbreaking
[1448.72 --> 1449.88]  and it's usually a fusion
[1449.88 --> 1450.66]  of two or three
[1450.66 --> 1451.20]  other genres,
[1451.34 --> 1452.90]  but then it just degrades
[1452.90 --> 1454.18]  into this cliche of itself,
[1454.34 --> 1454.50]  you know,
[1454.54 --> 1455.40]  caricature of itself.
[1456.14 --> 1456.50]  Yeah.
[1456.74 --> 1457.30]  And, you know,
[1457.34 --> 1457.90]  actually I think
[1457.90 --> 1459.16]  a lot of that is,
[1459.34 --> 1460.12]  it's the same reason
[1460.12 --> 1460.76]  why politicians
[1460.76 --> 1461.76]  eventually just kind of
[1461.76 --> 1462.80]  gravitate towards the middle,
[1463.06 --> 1464.28]  why almost everything
[1464.28 --> 1465.68]  becomes mundane.
[1466.04 --> 1466.78]  And it's just that
[1466.78 --> 1467.60]  if you want to sell it,
[1467.64 --> 1468.18]  you've got to sell it
[1468.18 --> 1468.90]  to the Midwest,
[1469.14 --> 1469.42]  you know,
[1469.48 --> 1470.64]  and you basically
[1470.64 --> 1471.36]  got to, you know,
[1471.44 --> 1472.94]  normalize it,
[1473.00 --> 1473.76]  you've got to take
[1473.76 --> 1474.40]  any of the flavor
[1474.40 --> 1475.02]  out of it.
[1475.02 --> 1475.88]  You basically got to
[1475.88 --> 1476.62]  make it like cheese,
[1476.80 --> 1477.14]  you know,
[1477.14 --> 1478.04]  because they like
[1478.04 --> 1478.76]  cheese in the Midwest.
[1479.40 --> 1480.12]  So future generations
[1480.12 --> 1480.88]  is going to be just like
[1480.88 --> 1481.70]  Muzak everywhere.
[1481.88 --> 1482.62]  Just a little bit of music.
[1483.84 --> 1484.76]  Yeah, yeah, totally.
[1485.76 --> 1486.72]  That's actually something
[1486.72 --> 1487.50]  that I've been curious
[1487.50 --> 1487.98]  about too,
[1488.02 --> 1489.86]  because some of the
[1489.86 --> 1490.72]  projects that I try
[1490.72 --> 1492.74]  to do online
[1492.74 --> 1493.72]  try to merge
[1493.72 --> 1494.60]  sort of like
[1494.60 --> 1496.72]  visual writing
[1496.72 --> 1497.82]  and music together,
[1498.04 --> 1498.44]  you know,
[1498.44 --> 1499.54]  and I think that's
[1499.54 --> 1499.94]  actually kind of
[1499.94 --> 1501.06]  like the next phase,
[1501.32 --> 1502.16]  like the next thing
[1502.16 --> 1503.34]  that you can't really
[1503.34 --> 1503.94]  copy.
[1504.46 --> 1505.28]  I mostly do it
[1505.28 --> 1505.94]  just because it's
[1505.94 --> 1507.10]  guaranteed to be unique
[1507.10 --> 1507.94]  so nobody can tell me
[1507.94 --> 1509.50]  it's not,
[1509.62 --> 1509.82]  you know,
[1509.82 --> 1510.42]  it's not something
[1510.42 --> 1511.10]  that's been done
[1511.10 --> 1511.86]  or that,
[1511.96 --> 1512.16]  you know,
[1512.56 --> 1513.38]  there's no musician
[1513.38 --> 1513.88]  out there really
[1513.88 --> 1514.58]  kind of doing that.
[1514.66 --> 1515.12]  There's a few.
[1515.30 --> 1516.14]  I think the first musician
[1516.14 --> 1517.52]  to do a mixture
[1517.52 --> 1518.26]  of video,
[1518.80 --> 1520.52]  textual,
[1520.72 --> 1521.20]  and audio
[1521.20 --> 1521.90]  is like Bob Dylan,
[1522.54 --> 1522.92]  you know,
[1523.42 --> 1524.06]  when he did
[1524.06 --> 1524.80]  Everything is Broken.
[1524.80 --> 1525.90]  It's like kind of
[1525.90 --> 1526.76]  the first music video
[1526.76 --> 1527.42]  in a lot of ways.
[1528.78 --> 1530.18]  So I basically
[1530.18 --> 1531.10]  tried to do a lot
[1531.10 --> 1532.06]  of projects like that.
[1532.18 --> 1532.42]  I mean,
[1532.46 --> 1532.98]  that's kind of
[1532.98 --> 1533.78]  cool stuff.
[1534.08 --> 1534.64]  You know,
[1534.64 --> 1535.50]  it seems like we try
[1535.50 --> 1536.06]  to shoehorn
[1536.06 --> 1536.94]  computer science
[1536.94 --> 1537.48]  to more of
[1537.48 --> 1538.62]  an engineering type
[1538.62 --> 1539.30]  role,
[1539.40 --> 1539.78]  but you know,
[1539.80 --> 1540.34]  a lot of it
[1540.34 --> 1541.56]  I've seen
[1541.56 --> 1543.10]  the most talented
[1543.10 --> 1543.92]  programmers are
[1543.92 --> 1544.90]  often creative
[1544.90 --> 1545.86]  in more than one medium.
[1546.68 --> 1547.16]  Yeah,
[1547.18 --> 1547.82]  that's very true.
[1547.92 --> 1548.26]  Actually,
[1548.38 --> 1550.90]  I would love
[1550.90 --> 1551.66]  to just start
[1551.66 --> 1552.78]  trying to teach
[1552.78 --> 1553.64]  random musicians
[1553.64 --> 1554.32]  how to code.
[1554.32 --> 1556.10]  I actually think
[1556.10 --> 1557.34]  like playing music,
[1557.44 --> 1558.30]  like if you play music
[1558.30 --> 1559.34]  from sheet music,
[1559.46 --> 1560.12]  probably more so
[1560.12 --> 1560.62]  than tab,
[1561.24 --> 1562.08]  but if you play music
[1562.08 --> 1562.58]  from sheet music,
[1562.66 --> 1563.32]  you're actually learning
[1563.32 --> 1564.48]  this programming language
[1564.48 --> 1564.84]  in a way.
[1565.06 --> 1565.22]  I mean,
[1565.34 --> 1565.76]  it's odd.
[1565.86 --> 1566.26]  It has like,
[1566.66 --> 1567.50]  just like every programming
[1567.50 --> 1567.74]  language,
[1567.82 --> 1568.46]  it has this sort of
[1568.46 --> 1569.34]  arbitrary rules
[1569.34 --> 1569.98]  that fit around
[1569.98 --> 1571.44]  a core theory
[1571.44 --> 1572.16]  that's solid
[1572.16 --> 1574.08]  and you have to
[1574.08 --> 1574.70]  be able to
[1574.70 --> 1575.60]  note structure,
[1575.78 --> 1576.80]  keep certain chains
[1576.80 --> 1577.98]  of things in your head
[1577.98 --> 1579.04]  so they got the memory
[1579.04 --> 1579.44]  for it.
[1579.88 --> 1580.78]  And I just keep
[1580.78 --> 1581.24]  running into these
[1581.24 --> 1582.92]  musicians and I'd be like,
[1582.98 --> 1583.62]  you could probably
[1583.62 --> 1584.18]  learn to code.
[1584.18 --> 1584.42]  I'm like,
[1584.48 --> 1584.66]  no,
[1584.72 --> 1585.42]  I can't code.
[1585.50 --> 1587.08]  I'm just a guitarist.
[1587.94 --> 1588.04]  Yeah.
[1588.46 --> 1590.06]  And I find visual artists
[1590.06 --> 1591.66]  that turn into programmers,
[1592.04 --> 1592.98]  writers.
[1593.40 --> 1594.88]  I've seen a lot of writers
[1594.88 --> 1595.70]  who eventually become,
[1595.82 --> 1596.92]  who can become programmers.
[1596.92 --> 1596.98]  programmers.
[1597.98 --> 1600.24]  And I think the really good programmers,
[1600.96 --> 1601.94]  programming is like something
[1601.94 --> 1603.58]  they use to do other stuff.
[1604.54 --> 1605.54]  I think that's the biggest
[1605.54 --> 1606.14]  thing I've learned.
[1606.88 --> 1607.24]  Yeah,
[1607.28 --> 1607.62]  that's right.
[1607.64 --> 1608.46]  Especially in this,
[1608.46 --> 1609.28]  I guess,
[1609.34 --> 1610.56]  brave new world of social media
[1610.56 --> 1611.38]  and the web.
[1611.38 --> 1612.48]  It's almost like just
[1612.48 --> 1613.72]  having that aspect
[1613.72 --> 1614.74]  is what you need
[1614.74 --> 1615.18]  to promote
[1615.18 --> 1616.30]  what it is you really do.
[1616.30 --> 1617.42]  Yeah.
[1617.62 --> 1618.78]  I would actually put it
[1618.78 --> 1619.74]  just a little differently.
[1619.86 --> 1620.30]  I would say
[1620.30 --> 1622.38]  the technology,
[1622.52 --> 1623.16]  like the business
[1623.16 --> 1623.92]  of technology
[1623.92 --> 1625.96]  changed from
[1625.96 --> 1627.14]  the kind of stuff
[1627.14 --> 1627.54]  I do,
[1627.66 --> 1628.66]  the backend stuff,
[1628.84 --> 1628.98]  you know,
[1628.98 --> 1629.60]  the web servers
[1629.60 --> 1630.32]  and things like that
[1630.32 --> 1631.96]  to a product version,
[1632.18 --> 1633.08]  like a product focus.
[1633.08 --> 1635.06]  So you actually make products
[1635.06 --> 1636.08]  for regular Joes,
[1636.18 --> 1636.32]  you know,
[1636.36 --> 1637.54]  Facebooks and Twitters
[1637.54 --> 1639.14]  and social media stuff
[1639.14 --> 1640.22]  and pretty much anything,
[1640.38 --> 1640.56]  Mint,
[1640.80 --> 1641.62]  even if it's like
[1641.62 --> 1644.80]  a web server analytics thing,
[1644.88 --> 1645.68]  it's a product.
[1646.28 --> 1647.40]  And the shift
[1647.40 --> 1648.06]  that you're getting
[1648.06 --> 1648.90]  is in order to make
[1648.90 --> 1649.58]  a good product,
[1649.68 --> 1649.88]  well,
[1649.98 --> 1650.66]  you have to be good
[1650.66 --> 1651.68]  at human stuff.
[1651.86 --> 1651.94]  You know,
[1651.96 --> 1652.40]  you have to be good
[1652.40 --> 1652.90]  at writing
[1652.90 --> 1654.46]  and public speaking
[1654.46 --> 1656.14]  and doing,
[1656.74 --> 1657.86]  you know,
[1657.96 --> 1659.46]  good gooey front ends
[1659.46 --> 1661.00]  and all that sort of stuff
[1661.00 --> 1662.06]  and a lot less
[1662.06 --> 1662.82]  about the technology
[1662.82 --> 1663.94]  and I think
[1663.94 --> 1665.64]  a lot of the reason
[1665.64 --> 1667.12]  why that's even possible now
[1667.12 --> 1667.74]  is because,
[1668.28 --> 1668.42]  you know,
[1668.46 --> 1669.04]  guys like me
[1669.04 --> 1670.32]  laid down this foundation,
[1671.00 --> 1671.16]  you know,
[1671.24 --> 1672.54]  the guys that wrote Apache,
[1672.68 --> 1673.56]  the guys that wrote Linux,
[1673.70 --> 1674.22]  the guys that wrote
[1674.22 --> 1675.16]  the hardcore stuff,
[1675.26 --> 1676.46]  they made it easy to use
[1676.46 --> 1677.22]  so that people
[1677.22 --> 1678.28]  who don't have to know that
[1678.28 --> 1679.80]  or don't know that so well
[1679.80 --> 1680.46]  can still come in
[1680.46 --> 1681.38]  and make a good product
[1681.38 --> 1682.96]  and put it out to others,
[1683.12 --> 1683.44]  you know.
[1684.14 --> 1685.54]  So I've got to ask the question,
[1685.74 --> 1686.90]  is Rails still a ghetto?
[1688.00 --> 1688.48]  You know,
[1688.56 --> 1689.48]  it's funny because
[1689.48 --> 1691.64]  I think they've cleaned up
[1691.64 --> 1692.08]  quite a lot
[1692.08 --> 1692.48]  and finally matured,
[1692.82 --> 1693.52]  although I still seem
[1693.52 --> 1694.22]  to run into a few
[1694.22 --> 1695.12]  here and there,
[1695.20 --> 1695.36]  but,
[1695.44 --> 1695.64]  you know.
[1697.88 --> 1698.56]  It's really,
[1698.76 --> 1699.02]  I don't know,
[1699.02 --> 1699.64]  it's kind of sad.
[1699.76 --> 1700.12]  I actually,
[1700.12 --> 1701.64]  I actually had a talk
[1701.64 --> 1702.52]  with a friend a lot
[1702.52 --> 1703.00]  where,
[1703.84 --> 1704.70]  you know,
[1704.82 --> 1705.78]  I've just had this idea
[1705.78 --> 1706.42]  for a while
[1706.42 --> 1707.94]  that in general
[1707.94 --> 1709.08]  I've seen this trend
[1709.08 --> 1710.40]  where every community
[1710.40 --> 1711.74]  becomes a Ponzi scheme,
[1712.40 --> 1712.72]  you know,
[1712.78 --> 1713.92]  where it seems like
[1713.92 --> 1714.92]  within every community
[1714.92 --> 1716.86]  they tend to fail
[1716.86 --> 1717.90]  mostly because
[1717.90 --> 1718.82]  this Ponzi scheme
[1718.82 --> 1719.40]  builds up
[1719.40 --> 1719.88]  and like,
[1720.02 --> 1720.26]  you know,
[1720.30 --> 1721.22]  just like the big
[1721.22 --> 1721.64]  banking,
[1721.94 --> 1722.46]  you know,
[1722.50 --> 1723.74]  the big banking failures
[1723.74 --> 1724.20]  and,
[1724.26 --> 1725.30]  you know,
[1725.30 --> 1726.16]  general Ponzi scheme
[1726.16 --> 1727.54]  failures or pyramid schemes,
[1728.10 --> 1728.90]  they collapse
[1728.90 --> 1729.68]  because it's more
[1729.68 --> 1731.08]  of like a social Ponzi scheme
[1731.08 --> 1731.92]  and there's the guys
[1731.92 --> 1732.50]  at the top
[1732.50 --> 1733.20]  that run it
[1733.20 --> 1734.36]  and then eventually
[1734.36 --> 1735.92]  all the wealth
[1735.92 --> 1737.56]  of influence
[1737.56 --> 1738.30]  and ideas
[1738.30 --> 1739.06]  and work
[1739.06 --> 1740.14]  that all the guys
[1740.14 --> 1740.66]  at the bottom
[1740.66 --> 1741.54]  are putting into it,
[1741.78 --> 1742.32]  even though the guys
[1742.32 --> 1742.76]  at the top
[1742.76 --> 1743.40]  only benefit,
[1743.90 --> 1744.54]  it collapses
[1744.54 --> 1745.28]  mostly because
[1745.28 --> 1745.78]  something new
[1745.78 --> 1746.30]  comes along,
[1746.38 --> 1747.18]  like a new Ponzi scheme,
[1747.18 --> 1748.16]  people move off to it
[1748.16 --> 1748.68]  and then,
[1749.02 --> 1749.18]  you know,
[1749.18 --> 1750.08]  they want to cash out
[1750.08 --> 1750.44]  in a way
[1750.44 --> 1751.18]  and they just leave
[1751.18 --> 1751.68]  and the whole thing
[1751.68 --> 1752.08]  collapses
[1752.08 --> 1754.04]  and kind of the indicator
[1754.04 --> 1754.46]  of that,
[1754.58 --> 1755.26]  if you notice
[1755.26 --> 1756.60]  any time a community
[1756.60 --> 1757.16]  collapses,
[1757.76 --> 1758.34]  you see about
[1758.34 --> 1759.14]  one half
[1759.14 --> 1759.96]  of the people
[1759.96 --> 1760.50]  at the top
[1760.50 --> 1761.34]  are the first ones
[1761.34 --> 1762.16]  to leave to the new thing
[1762.16 --> 1763.40]  so you get these guys
[1763.40 --> 1764.34]  who are like top authors
[1764.34 --> 1765.96]  and pundits
[1765.96 --> 1766.34]  and whatnot
[1766.34 --> 1767.14]  and the second Ruby
[1767.14 --> 1767.68]  came out,
[1767.78 --> 1768.48]  they were off of Java
[1768.48 --> 1769.06]  onto Ruby
[1769.06 --> 1770.54]  and the second Node
[1770.54 --> 1770.92]  came out,
[1770.98 --> 1771.54]  they were off of Ruby
[1771.54 --> 1772.12]  onto Node
[1772.12 --> 1773.92]  and I think
[1773.92 --> 1774.44]  they kind of get
[1774.44 --> 1775.38]  that it's like
[1775.38 --> 1775.90]  a Ponzi scheme,
[1775.94 --> 1776.68]  maybe not explicitly
[1776.68 --> 1777.76]  but I know they do
[1777.76 --> 1779.80]  so I think actually
[1779.80 --> 1780.88]  I've actually kind of
[1780.88 --> 1781.72]  started to say that
[1781.72 --> 1783.60]  if you have a community
[1783.60 --> 1784.54]  like a community
[1784.54 --> 1785.30]  style thing
[1785.30 --> 1787.22]  and it's not run
[1787.22 --> 1788.42]  more like an economy
[1788.42 --> 1789.96]  where everyone benefits,
[1790.14 --> 1790.96]  it's easy to find out
[1790.96 --> 1791.80]  who people are,
[1792.14 --> 1793.22]  you have a free market
[1793.22 --> 1793.92]  of ideas
[1793.92 --> 1794.80]  and even just
[1794.80 --> 1795.80]  plain old cash
[1795.80 --> 1797.04]  and you make it
[1797.04 --> 1797.48]  difficult
[1797.48 --> 1799.54]  to cheat people,
[1799.70 --> 1800.52]  I find a lot of times
[1800.52 --> 1801.38]  the Ponzi scheme
[1801.38 --> 1802.34]  communities have a lot of
[1802.34 --> 1804.28]  just straight up shysters,
[1804.50 --> 1804.60]  you know,
[1804.66 --> 1805.84]  programmers or business guys
[1805.84 --> 1806.60]  are taking advantage
[1806.60 --> 1807.04]  of people
[1807.04 --> 1808.82]  and if you don't have that
[1808.82 --> 1809.26]  then yeah,
[1809.36 --> 1810.06]  it turns into a ghetto.
[1810.38 --> 1811.26]  I think I see it
[1811.26 --> 1812.06]  in just about every one
[1812.06 --> 1812.94]  that's out right now.
[1814.00 --> 1814.52]  You know,
[1814.58 --> 1815.38]  and you kind of left
[1815.38 --> 1816.14]  the Ruby community
[1816.14 --> 1817.10]  not as dramatically
[1817.10 --> 1818.46]  as Why the Lucky Steph
[1818.46 --> 1819.42]  but I noticed
[1819.42 --> 1821.20]  sort of a softening
[1821.20 --> 1822.04]  of Zed Shaw.
[1822.14 --> 1823.04]  Who's the real Zed Shaw
[1823.04 --> 1824.10]  and who's the persona
[1824.10 --> 1825.46]  and who's the real Zed?
[1827.84 --> 1829.00]  The main thing is like
[1829.00 --> 1830.22]  so the internet persona,
[1830.72 --> 1831.08]  right,
[1831.44 --> 1832.72]  I've kind of divided it up
[1832.72 --> 1834.28]  now but the internet persona
[1834.28 --> 1835.12]  is a little bit me.
[1835.26 --> 1835.56]  I mean,
[1835.90 --> 1837.00]  I get pissed off at people.
[1837.12 --> 1837.82]  It's just online
[1837.82 --> 1838.88]  I just go crazy
[1838.88 --> 1840.50]  because there's these guys
[1840.50 --> 1841.00]  who,
[1841.28 --> 1842.32]  that I keep running into
[1842.32 --> 1844.54]  who are really nice online
[1844.54 --> 1846.26]  but totally in person
[1846.26 --> 1847.64]  and so I'm kind of like
[1847.64 --> 1849.02]  making fun of them
[1849.02 --> 1849.88]  by being the inverse
[1849.88 --> 1850.82]  so being a total
[1850.82 --> 1851.32]  online
[1851.32 --> 1852.24]  but then trying to be
[1852.24 --> 1852.86]  nice in person,
[1853.16 --> 1853.42]  you know.
[1854.18 --> 1855.06]  And it's funny
[1855.06 --> 1856.80]  because people on the internet
[1856.80 --> 1857.56]  just take it
[1857.56 --> 1858.68]  way too seriously.
[1858.88 --> 1859.10]  I mean,
[1859.10 --> 1859.68]  they take it
[1859.68 --> 1860.24]  way too seriously.
[1860.24 --> 1861.34]  They actually believe
[1861.34 --> 1863.58]  that I actually talk like,
[1863.74 --> 1863.98]  I mean,
[1864.06 --> 1864.92]  when there was that picture
[1864.92 --> 1865.68]  of me in leather,
[1865.78 --> 1866.66]  they thought I wore leather
[1866.66 --> 1867.38]  and I'm actually like,
[1867.64 --> 1869.22]  I'm like allergic to leather,
[1869.66 --> 1870.10]  you know.
[1871.36 --> 1872.84]  And about the only thing is
[1872.84 --> 1873.60]  every once in a while
[1873.60 --> 1874.42]  I would grow my hair out.
[1874.52 --> 1874.64]  Oh,
[1874.70 --> 1875.58]  I grew my hair out
[1875.58 --> 1876.56]  and I went to PyCon
[1876.56 --> 1877.52]  just like,
[1877.54 --> 1878.24]  I was just bored,
[1878.38 --> 1878.76]  grew it out
[1878.76 --> 1880.22]  and nobody knew who I was.
[1880.34 --> 1881.34]  I would actually stand there
[1881.34 --> 1882.48]  and my friends would walk by me.
[1882.88 --> 1883.74]  So like my signature
[1883.74 --> 1885.10]  is goatee and shaved head,
[1885.26 --> 1885.56]  you know.
[1886.42 --> 1887.40]  And so the thing
[1887.40 --> 1888.28]  that I try to tell people
[1888.28 --> 1888.62]  is,
[1889.10 --> 1889.46]  you know,
[1889.46 --> 1890.14]  me in person,
[1890.32 --> 1892.16]  I try to be nice to folks
[1892.16 --> 1892.64]  because,
[1892.80 --> 1893.02]  you know,
[1893.02 --> 1893.58]  I just kind of think
[1893.58 --> 1894.56]  the world is already
[1894.56 --> 1895.46]  full of a lot of suffering.
[1895.86 --> 1897.00]  But I also don't put it
[1897.00 --> 1897.96]  with people's sh**.
[1897.98 --> 1898.46]  Like if someone's
[1898.46 --> 1899.14]  going to be mean to me,
[1899.20 --> 1899.82]  I'm going to tell them.
[1899.90 --> 1901.54]  Or if I think they're just a f**k,
[1901.56 --> 1902.42]  I just kind of tell them.
[1902.56 --> 1902.68]  You know,
[1902.68 --> 1903.38]  if what they're doing
[1903.38 --> 1904.60]  is being an a**hole
[1904.60 --> 1905.22]  and being a jerk,
[1905.60 --> 1906.48]  I find that
[1906.48 --> 1907.50]  they tend to be
[1907.50 --> 1908.28]  so self-centered
[1908.28 --> 1909.26]  and so obnoxious
[1909.26 --> 1910.44]  that they don't even realize it.
[1911.08 --> 1912.08]  And I'll just tell them,
[1912.20 --> 1912.40]  you know.
[1912.74 --> 1913.92]  And I'll try to be nice
[1913.92 --> 1914.66]  if I'm a friend of them,
[1914.74 --> 1915.96]  but I've ran into the guys
[1915.96 --> 1916.80]  who are giant f**bags
[1916.80 --> 1917.42]  and just said,
[1917.48 --> 1917.80]  you know what,
[1917.86 --> 1918.46]  you're a f**k,
[1918.46 --> 1919.38]  I want to talk to you.
[1920.84 --> 1922.84]  And other than that,
[1922.88 --> 1923.82]  I just try to be nice.
[1924.06 --> 1924.60]  Be nice,
[1924.70 --> 1925.70]  but don't take crap from people.
[1926.14 --> 1927.68]  The online persona is,
[1927.74 --> 1927.94]  you know,
[1928.00 --> 1928.84]  if I'm being nice,
[1928.94 --> 1929.58]  then, you know,
[1929.76 --> 1930.62]  then that's me.
[1930.90 --> 1932.10]  And if I'm not taking crap
[1932.10 --> 1932.52]  from people,
[1932.66 --> 1933.38]  I'm doing it
[1933.38 --> 1934.14]  in the most ruthless,
[1934.44 --> 1934.90]  obnoxious,
[1935.00 --> 1935.84]  straight up way I can.
[1936.34 --> 1937.56]  I'm like just ripping them.
[1938.76 --> 1939.62]  And part of that
[1939.62 --> 1940.18]  is just because
[1940.18 --> 1941.08]  it's a lot of fun,
[1941.22 --> 1941.52]  you know.
[1942.12 --> 1943.00]  And a lot of the guys
[1943.00 --> 1944.00]  that I try to rip on
[1944.00 --> 1945.20]  just really deserve
[1945.20 --> 1945.90]  to be knocked down
[1945.90 --> 1946.60]  a few pegs.
[1946.60 --> 1947.04]  You know.
[1948.06 --> 1948.74]  Any theories
[1948.74 --> 1949.54]  on what happened to Y?
[1950.98 --> 1951.70]  I don't know.
[1952.14 --> 1953.20]  I kind of suspected
[1953.20 --> 1954.12]  that he was getting
[1954.12 --> 1955.10]  a little disillusioned
[1955.10 --> 1955.52]  for a while,
[1955.62 --> 1956.74]  but I think he was
[1956.74 --> 1957.38]  a family man.
[1957.56 --> 1958.68]  So I think maybe
[1958.68 --> 1960.50]  he just got more interested
[1960.50 --> 1961.18]  in family
[1961.18 --> 1962.06]  or something else.
[1962.92 --> 1963.74]  I think he just,
[1963.80 --> 1963.94]  you know,
[1963.96 --> 1964.70]  decided that,
[1964.76 --> 1965.00]  you know,
[1965.14 --> 1966.10]  he had enough.
[1966.18 --> 1966.48]  He had to go
[1966.48 --> 1967.20]  sort something out.
[1967.56 --> 1968.66]  I don't really think
[1968.66 --> 1969.32]  he had any,
[1969.50 --> 1970.14]  like,
[1970.22 --> 1971.12]  psychological issues
[1971.12 --> 1971.94]  or any of that stuff.
[1972.02 --> 1972.76]  I think there's a myth
[1972.76 --> 1973.56]  built up around that,
[1973.58 --> 1973.74]  like,
[1974.32 --> 1975.04]  the equivalent of
[1975.04 --> 1975.66]  he went crazy
[1975.66 --> 1976.20]  and had to go
[1976.20 --> 1976.90]  and check himself
[1976.90 --> 1977.62]  into some rehab
[1977.62 --> 1978.52]  or something like that.
[1978.60 --> 1979.12]  And I don't know
[1979.12 --> 1979.56]  if anyone's actually
[1979.56 --> 1979.98]  said that,
[1980.04 --> 1980.54]  but it seems to be
[1980.54 --> 1981.14]  the implication.
[1981.14 --> 1983.92]  So I think he just
[1983.92 --> 1984.92]  got kind of tired of it.
[1984.96 --> 1985.12]  I mean,
[1985.12 --> 1985.86]  I got tired of it,
[1985.94 --> 1986.20]  you know.
[1986.32 --> 1988.02]  I think he was in Ruby
[1988.02 --> 1989.62]  really early on
[1989.62 --> 1990.30]  and was,
[1990.44 --> 1990.66]  you know,
[1990.66 --> 1991.32]  just kind of like
[1991.32 --> 1991.88]  a character
[1991.88 --> 1993.14]  and then Ruby
[1993.14 --> 1994.10]  sort of changed
[1994.10 --> 1995.50]  and I think it went away
[1995.50 --> 1996.28]  from the fun,
[1996.96 --> 1997.96]  cool activity
[1997.96 --> 1998.92]  he used to just,
[1999.04 --> 1999.42]  you know,
[1999.42 --> 2000.34]  have his version
[2000.34 --> 2000.96]  of fun with
[2000.96 --> 2001.92]  and changed into
[2001.92 --> 2003.02]  something that,
[2003.74 --> 2004.30]  I guess the best way
[2004.30 --> 2004.82]  to explain it is
[2004.82 --> 2005.92]  Ruby changed
[2005.92 --> 2007.20]  to where his book,
[2007.44 --> 2007.60]  like,
[2007.60 --> 2008.24]  his gorgeous,
[2008.56 --> 2009.40]  fantastic book
[2009.40 --> 2011.78]  just didn't matter
[2011.78 --> 2012.12]  anymore
[2012.12 --> 2013.66]  or it just wasn't
[2013.66 --> 2014.78]  the same kind of community
[2014.78 --> 2015.24]  that would like
[2015.24 --> 2015.88]  that kind of book.
[2016.14 --> 2016.28]  I mean,
[2016.30 --> 2016.98]  people still like it,
[2017.04 --> 2018.02]  but I think
[2018.02 --> 2019.00]  that was the change.
[2019.44 --> 2020.24]  This is where I
[2020.24 --> 2021.24]  crowdsource production
[2021.24 --> 2022.02]  of feature episodes.
[2022.22 --> 2023.42]  So we just wrapped
[2023.42 --> 2025.06]  a Django Dash episode
[2025.06 --> 2025.98]  where Mongrel 2
[2025.98 --> 2026.58]  came up
[2026.58 --> 2028.24]  in this part of the show.
[2028.32 --> 2029.04]  So I wanted to ask
[2029.04 --> 2030.20]  you the same question.
[2030.30 --> 2030.72]  What's on your
[2030.72 --> 2031.36]  open source radar
[2031.36 --> 2032.08]  and what's got you
[2032.08 --> 2032.92]  excited to play with?
[2032.92 --> 2036.24]  So on my open source radar,
[2036.40 --> 2037.12]  definitely I've got
[2037.12 --> 2038.52]  zero MQ.
[2039.48 --> 2040.98]  I'm also looking at Node
[2040.98 --> 2042.16]  mostly because
[2042.16 --> 2043.56]  like I would like
[2043.56 --> 2044.02]  Mongrel 2
[2044.02 --> 2044.60]  to be able to
[2044.60 --> 2045.38]  point at Node
[2045.38 --> 2047.30]  and there's some
[2047.30 --> 2048.02]  spots with it
[2048.02 --> 2048.90]  where it's hard
[2048.90 --> 2049.82]  to work zero MQ
[2049.82 --> 2050.32]  into Node
[2050.32 --> 2051.28]  so, you know,
[2051.30 --> 2052.38]  we're kind of
[2052.38 --> 2053.60]  I'm like watching them
[2053.60 --> 2054.16]  and hanging out
[2054.16 --> 2054.86]  and seeing what
[2054.86 --> 2055.46]  they come up with
[2055.46 --> 2056.42]  and I may actually go
[2056.42 --> 2057.88]  hang out at Joyant
[2057.88 --> 2059.70]  and see if we can
[2059.70 --> 2060.10]  try and make
[2060.10 --> 2060.60]  something happen
[2060.60 --> 2061.16]  or maybe just go
[2061.16 --> 2061.68]  hang out there
[2061.68 --> 2062.62]  and help a bit.
[2063.52 --> 2063.98]  Because, you know,
[2064.00 --> 2064.34]  like I said,
[2064.36 --> 2064.80]  I want to get
[2064.80 --> 2065.30]  Mongrel 2
[2065.30 --> 2066.16]  where it hosts everything
[2066.16 --> 2067.14]  so Node is
[2067.14 --> 2067.80]  attractive.
[2069.32 --> 2070.80]  On the browser side,
[2071.52 --> 2071.98]  I had someone
[2071.98 --> 2072.48]  just show me
[2072.48 --> 2073.20]  this thing called
[2073.20 --> 2074.32]  Ajax IM
[2074.32 --> 2076.00]  which is basically
[2076.00 --> 2077.50]  like a full kit,
[2078.02 --> 2078.96]  a jQuery style kit
[2078.96 --> 2080.08]  to do a Facebook style
[2080.08 --> 2080.66]  chat bar
[2080.66 --> 2081.06]  at the bottom
[2081.06 --> 2081.62]  of your site.
[2081.80 --> 2082.18]  So I'm totally
[2082.18 --> 2082.96]  going to rip that off
[2082.96 --> 2084.06]  and do that
[2084.06 --> 2084.50]  as like the
[2084.50 --> 2085.52]  Mongrel 2 chat demo.
[2085.82 --> 2086.02]  You know,
[2086.12 --> 2086.44]  it was like,
[2086.52 --> 2086.74]  oh!
[2087.16 --> 2087.94]  He showed me it
[2087.94 --> 2088.14]  and I'm like,
[2088.20 --> 2088.82]  why haven't you
[2088.82 --> 2089.84]  shown me this?
[2090.12 --> 2090.38]  You know,
[2090.38 --> 2091.12]  it was so good.
[2092.92 --> 2094.22]  And,
[2094.30 --> 2096.16]  oh!
[2096.30 --> 2096.94]  And Qt.
[2097.14 --> 2097.92]  I'm actually dying
[2097.92 --> 2098.98]  to use the latest
[2098.98 --> 2099.58]  Qt.
[2099.94 --> 2100.64]  Qt, really?
[2101.08 --> 2102.28]  Yeah, I say that
[2102.28 --> 2102.72]  and people look at me
[2102.72 --> 2103.28]  like, what?
[2103.40 --> 2103.72]  Why?
[2103.72 --> 2104.82]  I played with it
[2104.82 --> 2105.58]  a while back
[2105.58 --> 2107.60]  and what they've done
[2107.60 --> 2108.28]  and I think it's
[2108.28 --> 2109.08]  going to get even better
[2109.08 --> 2109.86]  is they've basically
[2109.86 --> 2110.58]  hooked in
[2110.58 --> 2111.96]  full web kit
[2111.96 --> 2113.00]  and full JavaScript
[2113.00 --> 2114.14]  so you can actually
[2114.14 --> 2116.16]  write like a desktop app
[2116.16 --> 2116.96]  but do it all
[2116.96 --> 2117.84]  webby style.
[2118.06 --> 2118.72]  So you can do
[2118.72 --> 2119.52]  full Qt,
[2119.64 --> 2120.78]  C++ bindings,
[2121.12 --> 2122.06]  access disk,
[2122.22 --> 2122.68]  whatever the hell
[2122.68 --> 2123.16]  you want,
[2123.22 --> 2123.62]  like anything
[2123.62 --> 2124.62]  that C++ can do
[2124.62 --> 2125.66]  but then you can
[2125.66 --> 2126.78]  like make a little
[2126.78 --> 2127.46]  kind of framework
[2127.46 --> 2128.16]  or whatever you need
[2128.16 --> 2129.06]  to plug those
[2129.06 --> 2129.94]  C++ objects
[2129.94 --> 2130.88]  straight into
[2130.88 --> 2131.66]  a web kit
[2131.66 --> 2133.06]  browser
[2133.06 --> 2134.64]  and a JavaScript engine
[2134.64 --> 2135.46]  and it's all
[2135.46 --> 2136.24]  really seamless
[2136.24 --> 2137.52]  and for me
[2137.52 --> 2137.84]  I'm like,
[2137.96 --> 2138.12]  wow,
[2138.22 --> 2139.98]  if they were smart
[2139.98 --> 2140.42]  they would be
[2140.42 --> 2140.98]  promoting this
[2140.98 --> 2142.00]  as the way
[2142.00 --> 2142.54]  you can get
[2142.54 --> 2144.36]  simple web style
[2144.36 --> 2144.86]  development
[2144.86 --> 2145.76]  but still get
[2145.76 --> 2146.54]  a desktop app
[2146.54 --> 2147.10]  and to me
[2147.10 --> 2147.56]  I think that's
[2147.56 --> 2148.06]  like killer.
[2148.54 --> 2149.28]  If you just sit down
[2149.28 --> 2149.74]  and do that
[2149.74 --> 2150.56]  it would be the best.
[2150.76 --> 2151.34]  So I've got to
[2151.34 --> 2152.08]  ask the question now
[2152.08 --> 2153.10]  GNOME or KDE
[2153.10 --> 2153.84]  on your desktop?
[2154.62 --> 2155.06]  Neither.
[2155.68 --> 2156.44]  I actually use
[2156.44 --> 2158.52]  I just use the terminal.
[2159.78 --> 2160.00]  No,
[2160.00 --> 2160.94]  I use Awesome
[2160.94 --> 2162.52]  which is like
[2162.52 --> 2163.20]  the most awesome
[2163.20 --> 2164.28]  window manager ever
[2164.28 --> 2165.12]  so it's the right name.
[2166.10 --> 2166.66]  Awesome is
[2166.66 --> 2167.58]  so I've got like
[2167.58 --> 2168.46]  a dual monitor thing.
[2168.54 --> 2169.06]  I've got a laptop
[2169.06 --> 2170.26]  and then a monitor
[2170.26 --> 2171.88]  and with Awesome
[2171.88 --> 2172.68]  I basically
[2172.68 --> 2174.50]  never touch the keyboard
[2174.50 --> 2175.32]  unless I have to
[2175.32 --> 2176.58]  browse a web page
[2176.58 --> 2177.62]  and so
[2177.62 --> 2178.78]  and even then
[2178.78 --> 2179.78]  I usually don't.
[2180.00 --> 2181.04]  So my setup
[2181.04 --> 2182.12]  is basically Awesome,
[2182.84 --> 2183.18]  Vim,
[2183.54 --> 2184.30]  and Vimperator.
[2184.64 --> 2185.18]  So pretty much
[2185.18 --> 2185.90]  the exact same
[2185.90 --> 2186.52]  key sequences
[2186.52 --> 2187.72]  that I get in Vim
[2187.72 --> 2188.24]  I can use
[2188.24 --> 2188.96]  pretty much everywhere
[2188.96 --> 2190.60]  and then I've got
[2190.60 --> 2191.10]  terminals
[2191.10 --> 2192.08]  and I also use
[2192.08 --> 2192.84]  Screen locally.
[2193.04 --> 2193.96]  Screen is fantastic
[2193.96 --> 2194.36]  if you haven't
[2194.36 --> 2195.04]  actually used that
[2195.04 --> 2196.92]  and actually
[2196.92 --> 2197.88]  if you're on OS X
[2197.88 --> 2199.52]  like when I use OS X
[2199.52 --> 2200.34]  I just use Screen.
[2200.52 --> 2201.42]  I have one terminal
[2201.42 --> 2201.62]  open,
[2201.70 --> 2202.12]  I use Screen.
[2202.24 --> 2202.80]  I don't use a bunch
[2202.80 --> 2203.28]  of Windows
[2203.28 --> 2203.70]  and everything
[2203.70 --> 2205.78]  and that's pretty much
[2205.78 --> 2206.32]  my whole setup.
[2206.98 --> 2208.70]  I code like a ninja
[2208.70 --> 2209.38]  in that setup.
[2210.02 --> 2210.82]  The thing that sucks
[2210.82 --> 2211.50]  about that setup
[2211.50 --> 2212.52]  and actually just Linux
[2212.52 --> 2212.96]  in general
[2212.96 --> 2213.80]  is just about
[2213.80 --> 2214.78]  every media
[2214.78 --> 2215.80]  you ever want to use
[2215.80 --> 2216.40]  is awful.
[2216.40 --> 2218.18]  YouTube barely works,
[2218.28 --> 2219.24]  Flash barely works,
[2219.68 --> 2221.14]  everything barely works.
[2222.44 --> 2223.30]  So I have a Mac
[2223.30 --> 2223.86]  that I do
[2223.86 --> 2226.08]  most of my audio
[2226.08 --> 2227.46]  music related stuff
[2227.46 --> 2229.62]  and I do most
[2229.62 --> 2230.22]  of my editing
[2230.22 --> 2231.96]  and stuff with Reaper
[2231.96 --> 2233.24]  which is a really good
[2233.24 --> 2234.28]  digital audio workstation
[2234.28 --> 2235.06]  and stuff like that.
[2235.78 --> 2236.18]  Well cool,
[2236.32 --> 2237.08]  so much to look at.
[2237.16 --> 2237.84]  I'm making notes
[2237.84 --> 2238.50]  for the show notes.
[2238.60 --> 2238.90]  There's going to be
[2238.90 --> 2240.46]  a lot of cool links
[2240.46 --> 2241.02]  in the show notes
[2241.02 --> 2241.42]  this week.
[2241.88 --> 2242.58]  Thanks for joining us.
[2242.64 --> 2243.50]  Thanks for taking the time.
[2243.80 --> 2244.46]  Definitely look forward
[2244.46 --> 2245.34]  to playing with Mongrel too.
[2245.34 --> 2246.84]  Thanks, thanks.
[2246.92 --> 2247.44]  Yeah, we're doing
[2247.44 --> 2248.78]  the big push for 2.0
[2248.78 --> 2249.96]  so right now
[2249.96 --> 2250.52]  it's basically
[2250.52 --> 2251.56]  what we did
[2251.56 --> 2251.88]  is we
[2251.88 --> 2253.82]  when I named it
[2253.82 --> 2254.36]  Mongrel 2
[2254.36 --> 2255.64]  I realized that
[2255.64 --> 2256.24]  everyone would get
[2256.24 --> 2257.52]  a little logic error
[2257.52 --> 2259.10]  with Mongrel 2 2.0
[2259.10 --> 2260.72]  and Mongrel 2 3.0
[2260.72 --> 2262.62]  so I had to keep it that way.
[2262.88 --> 2263.92]  So basically 2.0
[2263.92 --> 2264.52]  we're going to make it
[2264.52 --> 2265.84]  fancy and nice to use.
[2265.96 --> 2266.54]  That's our goal.
[2267.28 --> 2268.42]  Fancy and nice to use.
[2268.52 --> 2268.72]  Cool.
[2268.82 --> 2268.98]  Yep.
[2269.26 --> 2269.88]  Thanks Ed.
[2270.28 --> 2270.80]  Yep, no problem.
[2270.86 --> 2271.16]  Thank you.
[2271.24 --> 2271.82]  Thanks for the interview.
[2271.92 --> 2272.18]  It was great.
[2272.18 --> 2272.22]  It was great.
[2275.34 --> 2290.52]  See it in my eyes
[2290.52 --> 2293.24]  So how could I forget
[2293.24 --> 2294.04]  It's where
[2294.04 --> 2297.30]  I found myself
[2297.30 --> 2299.94]  for the first time
[2299.94 --> 2303.64]  Safe in your arms
[2303.64 --> 2305.78]  And the dark passion
[2305.78 --> 2312.82]  Having a
[2312.82 --> 2313.72]  You've beenpart
[2313.78 --> 2316.22] abilorton
[2316.40 --> 2318.78]  This way
[2318.78 --> 2318.96]  has the situation
[2319.10 --> 2320.34]  And gives the heat
[2320.40 --> 2320.52]  thanks to Mal
[2320.66 --> 2321.46]  It's where
[2321.46 --> 2322.02]  I've cricket
[2322.02 --> 2323.16]  This way
[2323.16 --> 2323.42]  for and after
[2323.56 --> 2324.24]  when youknife
[2324.24 --> 2324.60]  into experience
[2324.60 --> 2325.20]  A event
[2325.20 --> 2326.22]  will help you
[2326.22 --> 2326.40]  fantastic
[2326.40 --> 2326.84]  You're gonna see
[2326.84 --> 2327.66]  This way
[2327.66 --> 2328.40]  lights out
[2328.44 --> 2329.02]  From the work
[2329.02 --> 2329.54]  Now
[2329.54 --> 2330.48]  lay quick
[2330.48 --> 2331.00]  Flush
[2331.00 --> 2331.02]  into my own
[2331.02 --> 2332.20]  The beautiful
[2332.22 --> 2332.74]  Y
[2333.16 --> 2334.16]  One
[2334.16 --> 2334.58]  Wow
[2334.58 --> 2335.10]  And
