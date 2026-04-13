[0.00 → 13.56] welcome back everyone this is the change log where remember support a blog and podcast
[13.56 → 18.22] that comes fresh and what's new in open source you can check out the blog at the change log.com
[18.22 → 22.80] and our patch shows at five by five dot TV slash change log this show is hosted by myself
[22.80 → 29.58] Adam Slovak and also Andrew Thorpe Andrew say hello yo yo to we're also joined today by
[29.58 → 36.80] Kenneth writes hello there not a yo yo yo to you can tune in live every Tuesday at
[36.80 → 41.52] 5 p.m Central Standard Time right here on five by five and today is episode number 98 we're joined
[41.52 → 46.94] by Matt Thompson Matt is the mobile lead of Heroku a lot of Heroku up here today he's the creator of
[46.94 → 51.62] AF networking which we just mentioned in the pre-show and his hipster Helios post gross app
[51.62 → 56.24] and the list literally goes on and on so Matt welcome to the show well hello everybody thank
[56.24 → 61.28] you so much for having me on yeah man absolutely so lets uh let's get started with how you got
[61.28 → 66.18] started open source who open source you know I really started diving into that with the objective
[66.18 → 71.18] c community uh when I was working at gorilla I found that a lot of the stuff that I was working on
[71.18 → 76.38] you know I started it started to actually be generally useful uh I think that's when i really
[76.38 → 80.90] you know started to pick up with everything so AF networking for instance came out as a project
[80.90 → 86.50] uh that we were using for uh gorilla for iPhone and uh it was general purpose enough that we thought
[86.50 → 90.34] that other people would like it and uh from there it just kind of took on a life of its own
[90.34 → 98.50] yeah so just wanted to give a quick rest in peace to gorilla I think that was an uh an app that most of
[98.50 → 104.20] us loved, and we're sad to see it go but I really miss it I had my whole life on there for two years the uh
[104.20 → 110.00] you know the whole passport uh all the stamps that you had liked it really told a story about you know
[110.00 → 114.62] every day that you know went out and explored the world so yeah it's something I've definitely
[114.62 → 120.96] missed I literally remembered uh driving uh when he and I went to Oklahoma City one time for a
[120.96 → 124.90] conference we were on our way back we were driving back we had to stop somewhere I forget where we
[124.90 → 128.00] had to stop and why we had to stop there, but he had to like to drop a pin or something like that and it
[128.00 → 132.82] was it was all about gorilla he used to do a lot of gorilla stuff right didn't he like reverse
[132.82 → 139.34] engineer their API yeah yeah oh yeah that's right he's a big gowalla fan I just remember
[139.34 → 145.12] gorilla having a big presence in the early version of the changelog it seemed like it yeah absolutely
[145.12 → 152.32] definitely so uh speaking of gorilla we have the AF networking kind of is the main project we
[152.32 → 157.72] wanted to talk about here um it's a common thing that we've noticed in the last for some reason in
[157.72 → 162.70] the last you know I don't know five or six shows we've talked about like for-profit companies that
[162.70 → 168.24] have released um you know pieces of the company in open source and AF networking is one of those things
[168.24 → 175.20] uh probably one of the questions I wanted to kind of ask you right off the bat Matt is what is the AF
[175.20 → 183.48] in AF networking sure so AF stands for Alamo fire which was the old name of gorilla so before gorilla
[183.48 → 188.76] did what it did it was a mobile games company uh did some things called uh one of the projects was
[188.76 → 193.92] pack rat which was an it's actually you can still play it on Facebook it got uh bought by another company
[193.92 → 200.20] so it's a collectible trading game uh really addictive uh a lot of fun, and they also did icon
[200.20 → 205.98] buffet which was a social network based around collecting iconography so little you know images
[205.98 → 212.56] of different themes uh it was a really neat company I mean I joined gorilla after being a fan of Alamo
[212.56 → 216.78] fire for many years it was sort of a dream come true you know I've been following their work for
[216.78 → 221.58] uh you know a long time and so it's really humbling to get there and to be part of the team
[221.58 → 228.40] uh yeah really, really cool stuff again miss it every day I love how there's the Alamo in the logo too
[228.40 → 233.70] oh yeah that's that's actually kind of repurposed from the Alamo fire logo itself out the Alamo fire
[233.70 → 239.54] of course is the uh official state flower of Texas or no sorry I guess at the blue belt either way
[239.54 → 246.92] uh it's one of the important uh flowers of Texas so I wanted to kind of mention that um because you
[246.92 → 252.22] went from Alamo fire to, or you didn't specifically but the chain of you know Alamo fire to gorilla
[252.22 → 260.08] and now you're at Heroku um, and so we have you and uh Kenneth both from Heroku so Heroku isn't
[260.08 → 264.64] itself open source so why don't you guys give us kind of insight into Heroku and how you guys do
[264.64 → 269.14] what you do and how you guys work together and those things sure Kenneth would you like to uh
[269.14 → 275.24] how much work do you would you say that we do together Matt oh we cross paths we sort of have
[275.24 → 279.20] parallel tracks you know I think our stories are quite curious in that respect yeah we both we're
[279.20 → 284.84] both uh well known for doing http libraries for our respective languages and uh we do a bit of
[284.84 → 291.10] evangelism but besides that I think we're kind of uh in silos right it's a shame but uh yeah I mean
[291.10 → 296.72] spiritually I think we're kind of absolutely playing off one another I feel the vibes all the
[296.72 → 302.22] time absolutely it's kind of cosmic intellectual bebop is what happens at Heroku it's fantastic
[302.22 → 308.74] cool so uh AF networking has nothing to do with Heroku this is something you maintain
[308.74 → 314.46] separately from Heroku in your spare times all right absolutely uh and one of I mean it's its
[314.46 → 319.92] interesting though I mean if my role at Heroku is to increase the number of mobile developers on the
[319.92 → 324.40] platform and a great way of doing that is increasing the absolute number of mobile developers I'm very
[324.40 → 329.02] confident that Heroku's you know provides a great development experience and people will choose
[329.02 → 333.62] it you know because it's the best tool for their job uh so getting the absolute number of developers
[333.62 → 339.48] out there who are making apps on iPhone for instance uh and most iOS apps consuming a web service in some
[339.48 → 345.12] respect uh as far as AF networking enabling people to do that I think that you know grows the
[345.12 → 350.44] business pretty directly I assume we're going to be touching Helios as well right sure that's that's
[350.44 → 354.10] another piece of the equation yeah why don't you kind of elaborate on that a little bit for us to
[354.10 → 360.98] get started sure so again kind of taking things a step back when we talk about mobile uh it's sort
[360.98 → 367.74] of this complicated nuanced uh word that's become kind of a buzzword and poorly understood uh in a lot
[367.74 → 373.30] of ways it's sort of a conflation of a lot of ideas the idea that uh technology is more ubiquitous
[373.30 → 379.02] than ever, and it will become increasingly so uh that we are dealing with different kinds of screen
[379.02 → 384.38] resolutions and different ways of presenting the same information uh you know in some common format
[384.38 → 389.88] and again when we're talking about mobile applications on these platforms whether that's
[389.88 → 396.04] hybrid or native uh we're talking about a client server architecture and increasingly uh when you're
[396.04 → 400.44] developing for the web that's that's sort of a rich client experience as well you're connecting
[400.44 → 408.48] through a Jason API uh you're making requests over http so actually you know the whole architecture the
[408.48 → 412.58] whole technology stack behind all of this is no different from the way that we're developing
[412.58 → 417.66] modern web applications so mobile uh really isn't a different way of doing things it's just
[417.66 → 422.94] uh you know focusing on the client so part of focusing on the client is that uh you're choosing
[422.94 → 428.06] to spend your time to polish that user experience right uh you're you're learning Objective-C you're
[428.06 → 433.36] learning coco and all the uh tricks to make your application stand out and that means that you
[433.36 → 438.90] don't have a lot of time or really desire to kind of spin cycles on figuring out uh sort of the
[438.90 → 444.14] plumbing of rest web services for push notifications that sort of thing and that's where Helios comes in
[444.14 → 450.68] Helios is an open source extensible uh back end as a service mobile back end as a service uh, and it's
[450.68 → 456.04] specifically focused on iOS right now because that's kind of the best place to start and the place
[456.04 → 461.02] where I'm most comfortable uh, but it's something that can extend and be used for rich web clients and
[461.02 → 467.72] android and pretty much anything else so Helios is if I'm not mistaken it's built on top of rack
[467.72 → 473.62] is that correct it is rack is an actually one of my favourite architectures you know Sinatra also is
[473.62 → 479.26] uh one of my favourite things in ruby but uh rack the way that it can be composed uh you know a complex
[479.26 → 484.80] application into component parts uh that are each kind of modular just ruthlessly modular as i really
[484.80 → 489.68] like the approach of that uh so coming at it as a rubbish uh it seemed like a natural fit
[489.68 → 495.46] so you said you came at it as a rubbish when would you say you made the transition from like
[495.46 → 503.04] a full-time rubbish to a full-time uh objective CE guy let's see so that was uh my first job out of
[503.04 → 508.86] college was at a company called Sergio uh at the time I was known as smart FM or alternatively I know
[508.86 → 515.90] I was uh for language learning uh Japanese speakers uh learning English uh that was in Tokyo and uh you
[515.90 → 521.28] know i I started off doing ruby there, but eventually you know as most companies uh do and
[521.28 → 527.26] and did especially back then uh we wanted to make a mobile app and uh somehow you know doing some past
[527.26 → 532.16] experimentations on Mac development I found myself kind of inheriting that project and eventually that's
[532.16 → 538.60] what I used to uh to you know get my foot in the door at uh go Allah so that's that's when I started
[538.60 → 545.30] that was about maybe four years ago cool so Helios kind of takes parts of what you loved about ruby and
[545.30 → 552.32] um you know also is built for some of the iOS Objective-C stuff uh how does Helios and AF
[552.32 → 557.44] networking work together or do they or you know what's that relationship look like well AF networking
[557.44 → 563.90] is sort of the bread and butter when it comes to making http requests um, but there's a layer on top
[563.90 → 569.22] of that it's a project called AF incremental store which is kind of under the umbrella of AF networking as
[569.22 → 576.10] a technology uh and AF incremental store uh combines AF networking with core data and the idea is that
[576.10 → 581.16] you don't write networking code any more it just automatically translates uh the requests that you
[581.16 → 587.56] would make or any faults or fetch requests that you'd make in core data uh to http transparently
[587.56 → 593.12] and asynchronously and then kind of load everything in the background so it's a way to develop uh you know
[593.12 → 601.00] core data it's and it's an object uh it's a graph persistence uh framework sort of like an ORM like
[601.00 → 605.52] active record that's a good way to think about it uh and if you can imagine instead of it talking to a
[605.52 → 611.06] database what it did is that it well consults a local cache to return stuff quickly and synchronously
[611.06 → 614.74] uh but then also in the background it's going to require this web service so mapping
[614.74 → 620.64] gets you know fetches to gets uh creates to posts that sort of thing I assume it's using standard
[620.64 → 627.12] http headers for that absolutely it's its building on standards uh it's using headers in a cache
[627.12 → 635.04] efficient way fantastic it's a really cool uh it's a really, really cool framework would you recommend
[635.04 → 640.60] if somebody were going and deciding they want to kind of get into uh mobile would you
[640.60 → 645.96] recommend Helios as a kind of place to start Helios I think is a great place to start if you are
[645.96 → 652.14] looking to build you know get up started uh very quickly so uh those data services again just to
[652.14 → 656.78] kind of expand on that so anti incremental store uh building on top of core data if you're using core
[656.78 → 662.18] data and starting kind of from the client you can actually link your core data model to Helios and
[662.18 → 667.52] it'll automatically generate those rest web services and for you so that means that you have a server
[667.52 → 672.00] talking directly to your client, and you don't have to stub anything out you don't have to implement
[672.00 → 676.66] that later the plumbing is taken care of for you, and you just begin to develop a real application
[676.66 → 682.64] so in that respect it's its really great uh it's other uh components it's other services like push
[682.64 → 688.52] notification registration like logging and analytics like uh newsstand or passbook integration those
[688.52 → 694.22] are things that uh can kind of live alongside a more developed application even as your application
[694.22 → 700.58] grows and uh probably gets out of the realm of basic crud uh responsibility so a Sinatra or a rails
[700.58 → 706.64] application uh you can keep those back-end services uh around a little bit longer so yeah it's a great
[706.64 → 711.68] place to start especially if you're not as familiar or comfortable with uh web service development even
[711.68 → 717.60] if you're not a rubbish the code that it generates is rather friendly and uh you know I think it's pretty
[717.60 → 725.88] easy to use how long has Helios been around I launched Helios I remember I think it was April 2nd
[725.88 → 731.32] it's a day right after uh April fool's day I made a whole thing about uh making fun of iCloud so i
[731.32 → 738.12] thought it was an appropriate response awesome, and it's a still an active development under beta um I'm
[738.12 → 744.48] working with a designer and a couple developers to really Polish something for uh maybe a fall release
[744.48 → 749.16] you know looking at September for a really proper uh polished release I think it'd be really exciting
[749.16 → 753.82] are there any early users or uh like success stories so far or people that are planning on using it
[753.82 → 759.02] uh that's the thing i kind of liken it to buying a car not everybody really wants to start developing
[759.02 → 763.20] a new mobile application all the time yeah so it's really about kind of gathering this interest
[763.20 → 768.40] and getting people to kind of experiment with uh more and more substantial kind of uh you know
[768.40 → 774.02] attempts at things but uh yeah I'm excited to see what people build on top of it yeah it's really
[774.02 → 779.36] cool I mean it's this so this was you created this, but you created this while you were at Heroku right
[779.36 → 784.44] so this actually is a Heroku product is that right exactly Heroku has been kind enough to
[784.44 → 789.42] sponsor the development of this as a sort of capstone project uh for a lot of the uh insights
[789.42 → 796.32] that I've kind of garnered over my experience of doing you know the job that I do at Heroku, so this is
[796.32 → 801.76] uh directly you know applied from my experience of understanding what developers need and what they're
[801.76 → 807.98] looking for and I'm hoping that this is a pretty compelling offering kind of has a Heroku feel on the
[807.98 → 813.68] website the helios.io website um oh I love that website yeah yeah it has a Heroku-esque feel but
[813.68 → 820.94] it's also feeling different can you kind of speak to who worked on this sure uh I hired a wonderful
[820.94 → 826.70] illustrator out of San Francisco her name is Erica sir otic uh she does actually she has a lot of
[826.70 → 832.10] children's illustrations and I wanted to kind of get away from uh it seems like a lot of uh tech projects
[832.10 → 837.08] maybe not recently I think they've maybe this is coming around but uh they're too they're kind of
[837.08 → 841.96] too serious and not approachable I found that her uh aesthetic really matched what I was looking for
[841.96 → 846.28] and uh at the time I was kind of going through a space kick I don't know uh maybe it was you know
[846.28 → 852.68] looking at tweets from the space station or uh watching the rockets zoom around the San Francisco
[852.68 → 858.92] bay on top of the I guess c-130 or whatever that was um it really I don't know I just was on a
[858.92 → 863.94] space kick so uh and maybe still am it's funny because there is an old app which I don't it was not
[863.94 → 868.18] not an app it was just like a little website you could use called read or not, and it was like uh
[868.18 → 872.48] it was oh I remember that yeah I remember I think it was for like reviewing books and I think it was
[872.48 → 876.86] kind of play on words like read or not like an astronaut but read or not like should I read this
[876.86 → 881.94] or not, and it had a yeah it had a space theme for the logo and the uh the little guy on top of the
[881.94 → 886.90] Helios website he reminds me of that I like it, I'm a big fan you mentioned your kind of alluded
[886.90 → 892.14] this to this a little bit um earlier but i kind of wanted to hear what your thoughts are what
[892.14 → 898.34] Helios is in beta so what does that mean and what do you kind of foresee as being the uh the get
[898.34 → 903.98] out of beta for Helios uh the get out of beta plan is uh improving on the documentation there's a
[903.98 → 910.54] lot of uh kind of places that I can go with that right now it's sort of uh a rather extended README but
[910.54 → 915.48] not much more than that and that's because we're still actively developing features uh as we talk about
[915.48 → 920.44] the plans for AF networking 2.0 I can kind of expand on that, but it's sort of a coordinated effort to
[920.44 → 925.76] uh not only provide essential mobile services for how people are developing applications now
[925.76 → 930.38] uh but anticipating their future usage and I think that's a really important thing to look forward
[930.38 → 936.76] at how uh developers are going to create mobile apps you know not just today but in the next uh
[936.76 → 943.40] couple years awesome yeah so it's its helios.io it's an it's a really cool uh little framework and
[943.40 → 948.88] if I know Adam Stokowski at all that you have already typed gem install Helios in your command line
[948.88 → 954.78] that's why I was being so quiet I was actually over here uh yeah I was I'm over here hacking on it
[954.78 → 960.58] right now yeah I was like I noticed that uh Adam has been quiet for the last couple of minutes so i
[960.58 → 963.72] said okay he's working on that's what he seems to do every show and what we're talking about and
[963.72 → 968.76] he gets excited about it and uh it's an it's an it's a good omen that is awesome you must know
[968.76 → 974.34] me well I was uh I was on point three of getting started on OSS which is our OSX which is you'll see
[974.34 → 984.00] your web apps web UI at localhost 5000 admin so kind of uh transition um I think the requirements
[984.00 → 989.34] of Helios are ruby 19 plus I would imagine and Postgres uh you know is a requirement as well
[989.34 → 994.76] which kind of brings me to what I think the very first time I ever saw your name was postgres.app
[994.76 → 1001.00] so uh kind of speak to that and what that is and when that came about sure so one of the
[1001.00 → 1005.00] most frustrating things I can remember from when I was uh first starting as a web developer
[1005.00 → 1010.86] uh was getting a database set up I mean I think a lot of us started with camp uh back when my
[1010.86 → 1016.46] sequel was maybe the best choice you know PHP my sequel that sort of development uh and I mean i
[1016.46 → 1020.80] just could not for the life of me figure out how to get a Postgres instance installed on that every
[1020.80 → 1025.70] and I was doing geospatial stuff and uh you know everybody insisted that this is the best way to do it
[1025.70 → 1030.16] but you know if you can't actually install and use it then what's the point, and it's not that
[1030.16 → 1036.22] you know I'm not you know users aren't aren't dumb they're just you know maybe they
[1036.22 → 1041.06] don't have time or the patience to figure out you know the problem if people can't use a software it's
[1041.06 → 1045.24] not the fault of the users there's nothing more discouraging when you're starting to like
[1045.24 → 1049.68] wanting to use a new technology when it's like you know it's getting in the way right yeah starting
[1049.68 → 1055.02] to feel inspired exactly, exactly, and it's a real shame because Postgres really is the best relational
[1055.02 → 1060.10] database out there the best open source uh one, and it's powering a lot of stuff at Heroku powers
[1060.10 → 1064.10] all of my projects and I've just fallen in love with it so I want to make sure that everybody's
[1064.10 → 1069.72] experience uh you know I'm taking it upon myself to figure out how the hell to get this thing working
[1069.72 → 1074.70] uh in kind of containerized app uh so that other people don't have to go through a similar process
[1074.70 → 1079.14] because it really is kind of an ordeal and I guess a lot of people say you know what's so hard
[1079.14 → 1085.28] about brew install uh but if you look at your know projects like rails girls or other projects you know
[1085.28 → 1090.42] kind of these meetups where people are starting to hack, or new people are coming on uh what you
[1090.42 → 1096.32] find is that you know homebrew is not something that people intuitively get or really uh need to
[1096.32 → 1101.78] initially right and the terminal is a scary place uh and I think that's something that we forget as
[1101.78 → 1107.18] developers we just expect people to do it our way yeah we know I think I love homebrew I mean obviously
[1107.18 → 1112.08] you know we're not here to bash homebrew at all but I think that homebrew does make some
[1112.08 → 1118.02] assumptions for you know for us which is like we're comfortable in the terminal we understand
[1118.02 → 1122.62] the command line we are okay with like typing commands, and you know what I mean and I think
[1122.62 → 1128.06] that newcomers are not necessarily there, and they're and that's a just anything you can do to mitigate
[1128.06 → 1134.72] that hurdle uh in my opinion to get new people into this is incredible and um you know one of the
[1134.72 → 1138.60] one of the girls that we work with at pure charity her name's Beverly, and she's involved with like
[1138.60 → 1143.96] rails bridge and um dev chicks and stuff, and she does a lot of pairing and helping newcomers out
[1143.96 → 1150.22] and I mean that's kind of what she preaches is you know personally myself I love vim I use vim I'm I'm
[1150.22 → 1154.98] very comfortable in the terminal all this and that but newcomers are it's hard enough to get them to
[1154.98 → 1159.62] even want to try programming so to like try and get them to understand the command line and this and
[1159.62 → 1165.70] that is not necessarily worth doing, so any tools like this that make that easier I think it's
[1165.70 → 1170.64] absolutely necessary in this world right now right, and it's not just for beginners either I mean i
[1170.64 → 1175.02] myself am a user of Postgres app and that's because that's the interface that I choose to use things
[1175.02 → 1180.60] through I mean again a lot of uh developers at least on GitHub it seems are Mac users uh and they
[1180.60 → 1186.10] appreciate a certain ease of use and kind of out of the box experience and I think that uh kind of apps
[1186.10 → 1191.22] are a great way to do that so I mean I don't I don't really want to manage uh background demons or
[1191.22 → 1195.84] anything like that I don't want to have to guess where my you know data is being stored I like having
[1195.84 → 1200.48] that all in a knowable reproducible place, and you know that's why I made it and that's why I'm so
[1200.48 → 1204.94] happy to share it with everybody it's cool it seems like Heroku almost has co-branded itself with
[1204.94 → 1211.44] Postgres at times and I think that's really neat um this like i postgres.app was well just to clarify
[1211.44 → 1218.02] do you call it Postgres app or postgres.app I usually call it Postgres app but uh that's actually i
[1218.02 → 1221.80] think i interchange it for some reason that sounded weird coming out just than so yeah
[1221.80 → 1228.20] call it whatever you want um it feels like uh this obviously came out well before your time at Heroku
[1228.20 → 1235.80] is that right what postgres.app or Postgres and Heroku's postgres.app that was something I created
[1235.80 → 1241.74] on you know I think on my fourth day at Heroku oh okay gotcha so it has kind of been sponsored by
[1241.74 → 1247.96] Heroku the same way that Helios was it's interesting so that was not as much sponsored well I mean yes
[1247.96 → 1252.72] they did support they did support it, and they did fund uh that delightful icon that that goes along
[1252.72 → 1257.42] with it, and they have allowed me to work on that you know during office hour or during my hours
[1257.42 → 1262.54] working there right uh, but that was it really was more of a dare somebody said hey you know
[1262.54 → 1267.68] Postgres is hard to install uh why don't we just have it as an app and I just said sure I think I can
[1267.68 → 1273.30] make that you understand how mac frameworks work I had no idea that was my second Mac app I don't
[1273.30 → 1278.98] understand how to do mac development really uh I'm sure anybody who you know is worth their salt can
[1278.98 → 1283.78] look in there and see some hideous things but boy it's its it's a really complex beast underneath
[1283.78 → 1288.58] again like the more complexity that I put into it the more, the happier I am that other people don't
[1288.58 → 1293.48] have to deal with you know helper applications relaunching stuff uh you know any of that do you
[1293.48 → 1299.24] want to touch on induction app at all oh I would rather not because it's an embarrassing blight on my uh
[1299.24 → 1303.94] on my record it's this promising you know polyglot database client my first Mac application that i
[1303.94 → 1307.76] wanted to build it started out as a Regis client but all the Postgres people at Heroku thought it'd
[1307.76 → 1315.18] be cool to uh make a Postgres uh database client uh a native Mac client for Postgres as well uh so it
[1315.18 → 1320.68] just turned into doing all things for all people and uh as far as ambition goes for first projects it's
[1320.68 → 1326.08] hard I've it's hard to imagine something more uh difficult and broad than that and unfortunately i
[1326.08 → 1331.06] haven't had much time or really have much expertise sufficient expertise to really execute on it
[1331.06 → 1336.12] but you did say it's got one of the and I agree it's got one of the coolest logos I've ever seen
[1336.12 → 1343.28] or icons I've ever seen David Latham uh brilliant iconography out of the icon factory he does not
[1343.28 → 1348.48] skimp he is he's amazing he came up with that whole concept just from uh the name and a few kind of
[1348.48 → 1354.40] simple guidelines on yeah direction I've said you know tesla and kind of uh electronics and industrial
[1354.40 → 1359.54] and he came back with this yeah uh, and it's just amazing well not for an awkward transition but let's
[1359.54 → 1367.38] move away from that now sure so okay kind of on to what I'm really the most excited about which is to
[1367.38 → 1372.14] kind of talk about the AF networking um this is something that just reading a little bit about
[1372.14 → 1379.20] uh in a similar sense that Postgres app if it's not just for beginners, but it makes the task a lot
[1379.20 → 1385.58] easier um AF networking, and you can definitely correct me where I'm wrong because I am uh sure
[1385.58 → 1390.84] anything but experience anything but an expert when it comes to this stuff um AF networking is
[1390.84 → 1397.28] it's built just on top of ns URL connection right so why not just use ns URL connection
[1397.28 → 1402.00] that's a that's a great question actually at the top of the FAQ there's the full answer for that because
[1402.00 → 1406.22] that's obviously the first thing that uh responsible developers are going to ask before they incorporate a
[1406.22 → 1411.38] new dependency uh and the philosophy behind AF networking is really simple it's that ns URL
[1411.38 → 1416.66] connection is the highest uh level the highest level of abstraction that the standard library provides
[1416.66 → 1421.34] and as apple suggests that's the one that you usually want to use unless there's some good reason
[1421.34 → 1425.80] that you should dip down to a lower level so we're using that, but we're also combining it with one of my
[1425.80 → 1433.38] favourite classes in Objective-C uh coco it's ns operation so ns URL connection does manage all the
[1433.38 → 1439.30] uh, so there's a couple of things ns URL connection in order to be asynchronous and cancellable
[1439.30 → 1444.70] or in order to monitor its uh progress and that sort of thing you need to implement a number of
[1444.70 → 1448.78] delegate methods and if you're doing that in your own application it's sort of cumbersome that you
[1448.78 → 1454.16] have to do all this boilerplate work I found that it was nice to combine that into ns operation which
[1454.16 → 1460.52] meant it's basically a state machine for uh that can be queued up uh and given priority so you start a
[1460.52 → 1464.46] request and then by the time it's finished you have all the data that you loaded from your remote
[1464.46 → 1470.24] resource available to you as a ns' data object or depending on the kind of request that you made
[1470.24 → 1479.18] a Jason object an XML document an image that sort of thing so you're starting from a ns URL request
[1479.18 → 1487.30] which is an http verb maybe some parameters and body and the URL, and then you end up with exactly what
[1487.30 → 1491.36] you want in the format that you need it so that's that's the sort of contract that you establish in
[1491.36 → 1497.78] AF networking, and it seems to be a pattern that a lot of people uh you know enjoy and prefer to
[1497.78 → 1504.08] work with gotcha so it is kind of takes the know ns URL connection combines it with other tools
[1504.08 → 1509.30] that are already readily available makes it easy to do that in one place for you exactly and with coco
[1509.30 → 1514.04] it really is I mean of all the languages I've worked with I think object to c has the best standard
[1514.04 → 1519.50] library you know by orders of magnitude just the amount of thought and uh thoughtfulness that's put
[1519.50 → 1524.18] into the design of those classes, and you can be guaranteed that everything will be fast which is
[1524.18 → 1529.84] another great pretty much everything will be fast it's really a great uh and freeing constraint uh to
[1529.84 → 1535.68] just use what apple provides so it's built building on those uh fundamental parts not reinventing the wheel
[1535.68 → 1542.44] at least as much as possible and then translating delegate math delegate patterns uh to block-based
[1542.44 → 1546.54] callbacks so that's the important thing is that you're loading a request and by the time you get
[1546.54 → 1552.54] it back asynchronously you execute a block of logic that's close to where you actually made the
[1552.54 → 1557.12] request in code has there ever been any discussion from apple about including it in the standard library
[1557.12 → 1564.12] so I talked to an apple engineer at labs during a WWDC a couple of years ago and their answer was actually
[1564.12 → 1570.48] uh quite interesting so I asked them you know it seems like a lot of users are looking for this kind of
[1570.48 → 1576.02] functionality in their applications uh why not provide them these libraries uh yourself and the
[1576.02 → 1581.66] the engineer I was talking to i was looking for Quinn the Eskimo uh who's that's that's
[1581.66 → 1587.06] that's his handle uh Quinn yeah uh is the author of many of those libraries and a lot of the sample
[1587.06 → 1591.66] codes so pretty well known uh and I forget the person who I actually talked to, but his answer was that
[1591.66 → 1596.50] you know if you think of apple's view of technology they're taking a very long perspective on it for
[1596.50 → 1603.78] instance they didn't incorporate a Jason parser into the public API until iOS 5 you know just a
[1603.78 → 1608.80] couple years ago the reason for that is you can imagine that they didn't know if Jason was going to
[1608.80 → 1614.04] be a thing apple's been around for 30 years it's impossible to really know what patterns are here to
[1614.04 → 1618.84] stay uh, and they have to be very conservative for instance they had a have a pub sub framework
[1618.84 → 1625.66] that I believe is extensively used in mail but nowhere else uh I think they expected pub sub to maybe
[1625.66 → 1631.04] maybe be a bigger thing than it was, and now they have to publicly support that so uh that's one of
[1631.04 → 1636.52] the trade-offs of being you know kind of investing in a technology before it's really proven so I guess
[1636.52 → 1642.64] they can kind of hedge their bets on the basic implementations of things and allow the rest
[1642.64 → 1648.20] of the world to create the details for them exactly uh, but the interesting thing is that apple in their
[1648.20 → 1653.78] recent update for uh forthcoming update with iOS 7 have implemented quite a number of the common
[1653.78 → 1660.24] patterns uh so iOS 7 introduces a new networking framework or a new networking construct called
[1660.24 → 1666.28] sure session which actually supersedes and in some way deprecates nsurl connection is
[1666.28 → 1672.76] still around so AF networking uh the current version will work with iOS 7 uh just fine but sure session
[1672.76 → 1678.10] is the new way forward and actually have offers a lot of benefits uh I can I guess I can go into that
[1678.10 → 1684.48] yeah yeah definitely sure so sure connection it's great it's a high level library that had these
[1684.48 → 1689.46] useful delegate methods was fast and uh took care of a lot of the protocol management that you wouldn't
[1689.46 → 1695.06] want to do yourself like redirection uh handle automatic redirection that sort of thing uh however
[1695.06 → 1701.56] it suffered from the whole URL loading system suffered from kind of singleton mentality is that
[1701.56 → 1709.52] every URL sure connection shared a URL cache it shared a cookie store it shared um you know a set
[1709.52 → 1714.48] of sure protocols so different ways to kind of inject logic as you're making requests and it also
[1714.48 → 1719.14] shared you know session variables so it was very easy to get yourself into a especially with an
[1719.14 → 1724.64] application that communicated with many different services to get into a situation uh where caches are
[1724.64 → 1730.62] not being invalidated where they should be or sessions are getting mugged, or you know it was just
[1730.62 → 1737.74] sort of mess so sure session offers per session uh configuration and then on top of that kind of
[1737.74 → 1744.36] abstracted out this asynchronous uh you know connection to a web service and provides
[1744.36 → 1750.28] uh data download and upload tasks so the basic things that you'd want to do uh fortunately there's
[1750.28 → 1754.80] a lot of stuff that AF networking I think can improve upon that and uh I'm really excited with
[1754.80 → 1760.50] what we have planned with uh 2.0 yeah so uh you kind of told me a little bit before that
[1760.50 → 1766.68] the 2.0 might be announced pretty soon um is this kind of the driving force for 2.0 the
[1766.68 → 1774.80] change in the sure session it's yes it's actually a great confluence of uh necessity and uh just
[1774.80 → 1781.22] sort of uh luck that uh AF networking was in a place where I knew that I wanted to do different
[1781.22 → 1785.72] things I wanted I knew I wanted to improve on the existing architecture in sort of major ways
[1785.72 → 1791.14] and uh this is there's no better reason than you know apple providing you a better tool so
[1791.14 → 1796.68] sure session uh AF networking adapts and applies its patterns on top of that now
[1796.68 → 1805.20] while maintaining uh you know vintage support or legacy support for sure connection but it also
[1805.20 → 1811.24] improves upon those patterns so in addition to being based on sure session it's abstracted away
[1811.24 → 1816.04] the concept of serialization before I talked about how you make a request and then by the end of the
[1816.04 → 1821.46] operation you have exactly what you want whether that's an image or that's parsed Jason object or
[1821.46 → 1827.48] XML that sort of thing uh those serializes used to be just kind of baked into the request operation
[1827.48 → 1834.72] itself now that I'm supporting uh request operations and URL sessions uh you know simultaneously it made a
[1834.72 → 1839.52] lot of sense to abstract that out extract that into its own class so you have serializes that
[1839.52 → 1847.08] encapsulate uh all the logic to transform ns data uh with a particular http response uh to
[1847.08 → 1854.18] particular objects like XML like Jason like message pack or image, or you know maybe even directly to
[1854.18 → 1859.06] your instances of your models so it's actually a really powerful construct and cleans up a lot of
[1859.06 → 1864.96] the code reduces the uh number of lines of code in the in AF networking uh almost enough to offset the
[1864.96 → 1871.36] new features in the new version was it a complete rewrite or um just you know basic of
[1871.36 → 1879.00] evolution of the product well it was I was so we've kept basically half of it um and a lot of it was
[1879.00 → 1886.54] kind of taking out the things where it was uh built on request operations instead of uh URL
[1886.54 → 1891.60] session and kind of building in the new part so I think we threw I threw away half of it first and
[1891.60 → 1896.84] then just built from the ground up uh the first right took about a day and uh it actually was quite
[1896.84 → 1902.14] easy to integrate the new APIs quite easy for somebody that's a genius like yourself that is
[1902.14 → 1905.86] no, no no I've just been thinking about it for months and months so you know you finally write
[1905.86 → 1909.86] it out, and it's just like ah all right one sitting not too bad so when do you plan on actually
[1909.86 → 1915.22] releasing 2.0 uh the first release candidate is going out on Thursday I'm actually here in
[1915.22 → 1919.60] New York I'll be speaking at the iOS developer meetup at the New York times building
[1919.60 → 1925.28] on Thursday uh and that will be the first look that many developers get at 2.0 talking about its
[1925.28 → 1929.92] features and sort of the agenda that I hope to lay out with iOS networking in general in the
[1929.92 → 1937.20] future cool so just a few more days, and we'll get to uh play with the uh the new the shiny and new
[1937.20 → 1942.68] absolutely and if you can't wait there's a branch hiding in plain sight just go to the branches uh tab
[1942.68 → 1947.90] on GitHub and just click 2.0 it's amazing how few people have actually noticed this that's a those
[1947.90 → 1952.84] are not to go off on a side topic but finding uh old finding different branches and versions and
[1952.84 → 1959.42] tags and stuff is for some reason not the normal uh you know workflow for users consuming things
[1959.42 → 1964.24] on GitHub so I don't know if there 's's an uh there's a solution out there but if you can solve
[1964.24 → 1968.44] that problem for me that would be great well now they have the new releases thing so you can actually
[1968.44 → 1973.32] create a pre-release and that's true it's pretty nice I haven't done it myself, yet you should do that
[1973.32 → 1979.18] Matt and see how it goes sure I mean I use coco pods to manage my releases so if you just create
[1979.18 → 1985.16] a tag yeah coco pods it's like ruby gems uh yeah directly inspired by ruby gems it's actually the
[1985.16 → 1991.36] interesting thing about coco pods uh is that it is entirely based on GitHub so all the infrastructure
[1991.36 → 1995.68] it's just that you're pointing to a specs repository and when you want to add a new spec
[1995.68 → 2001.96] uh if you want to add a new pod you just you know create a pull request for that pod or if you
[2001.96 → 2006.78] commit access you just commit directly I was actually looking into doing that for the python
[2006.78 → 2012.42] community as well I think that would be really great I think that was uh what's the name Eloy
[2012.42 → 2017.48] from coco pod yeah I think he was actually on an episode of the changelog a while back wasn't he
[2017.48 → 2025.94] Adam talking coco pods um I'm pretty sure yeah maybe like 70s late 60s yeah a little while ago
[2025.94 → 2031.18] episode number yeah not uh right show numbers not years yeah I just love the sound of that
[2031.18 → 2036.58] so I'm number 98 oh man you guys have uh I'm sure have something cool planned for 100 then
[2036.58 → 2041.80] yeah we're planning on doing a show on to on a Tuesday at 5 p.m yeah all day change
[2041.80 → 2049.72] um so AF networking has some I don't know if you'd call it competition, but it seems like um
[2049.72 → 2054.76] rest kit is another one and that's the other one that the only other one I could find digging around
[2054.76 → 2059.92] that seems like it's actively maintained so how does AF networking differ from rest kit if you
[2059.92 → 2064.64] have any idea different layers actually rest kit is built on top of AF networking oh well
[2064.64 → 2069.78] there you go so rest kit actually is more of a direct competitor to the AF incremental store
[2069.78 → 2074.80] okay uh in a way that it's doing automatic mapping between it takes it a step further and does
[2074.80 → 2080.46] automatic mapping to your uh basically your domain logic your application models uh but the yeah all
[2080.46 → 2086.22] the transport is handled by AF networking uh I hate you know i i I'm skeptical of of of large
[2086.22 → 2091.44] projects and monoliths and uh I don't want to become you know a dinosaur and I don't want to
[2091.44 → 2097.66] abuse the influence of AF networking or ever be put the community in a position where they have a big
[2097.66 → 2103.52] tool that sucks so uh I definitely encourage people to call me on that and to can you know
[2103.52 → 2109.58] constantly uh challenge my assumptions and uh you know offer new suggestions because as much as I can
[2109.58 → 2115.34] be i I try to remain open to those new ideas and do my best to you know incorporate that and I think a lot
[2115.34 → 2121.10] of those ideas you know actually speaking of which Blake waters uh the author of rest kit uh he was
[2121.10 → 2126.76] absolutely instrumental in uh for instance the design and architecture of the serialization modules in
[2126.76 → 2132.80] AF networking 2.0 that was all his idea like I'll give absolute credit to him uh you know, and it's
[2132.80 → 2136.88] because it benefited and aligned more with the way that he was designing things with rest kits so
[2136.88 → 2142.16] again not competition it's its the best of what I've seen with open source and i I absolutely love
[2142.16 → 2147.42] the Objective-C community awesome yeah so uh you were talking about not wanting to be like a dinosaur
[2147.42 → 2152.28] and kind of avoiding the monolith and one thing that I noticed that was unique which seems like it
[2152.28 → 2159.04] it would help you in that is the like premium support package that you offer um it seems unique and I don't
[2159.04 → 2164.20] you know I'm not very involved in the Objective-C iOS community so maybe it's more common there but
[2164.20 → 2168.68] um just offering like a flat you know hey this is my open source product I maintain it but
[2168.68 → 2175.12] if you want support i will do that um what made you kind of set on that model for support
[2175.12 → 2180.22] with this i you know I think I wrote a blog post maybe a year ago maybe that's the last thing i
[2180.22 → 2185.88] blogged about um there 's's definitely a tension uh between and i actually Kenneth while you're on
[2185.88 → 2189.12] there was a there was a guy who blogged about how you should be a billionaire you remember that post
[2189.12 → 2192.90] yes I saw that I think it was only a millionaire but yes I did oh a millionaire I did see that well still
[2192.90 → 2198.32] that was ridiculous the basic argument I mean it's an interesting argument that you know we're putting all
[2198.32 → 2203.58] this time and effort into things and by golly we should be compensated for it, but the reality is
[2203.58 → 2210.32] that open source functions and is actually possible to exist as a gift culture not a market uh you know
[2210.32 → 2215.04] free market or sort of monetary culture it would be as if you went to somebody's house for dinner they
[2215.04 → 2219.16] invited you over, and you plopped down a 20 bill on the table at the end of the meal that would be the
[2219.16 → 2224.54] most inappropriate thing ever what is not inappropriate though is offering a bottle of wine or offering to
[2224.54 → 2231.00] help clean up so what we have is a sustainable model of cooperation but just not on that level
[2231.00 → 2235.98] I mean we're all developers are well paid, and we're you know we have roofs over our head for the
[2235.98 → 2242.30] most part and do you know we are often fed at work I mean we're we're not in need of that side
[2242.30 → 2248.58] of compensation but at the same time there is a need uh for companies and individuals uh to kind of
[2248.58 → 2254.48] transcend the sort of uh cooperative style if people can't offer to help clean up the dishes
[2254.48 → 2259.66] maybe in fact they do uh you know pay a little bit to have it catered or something like that and
[2259.66 → 2266.12] that's what the premium support does uh and a couple companies have used that and it's been great to
[2266.12 → 2272.24] allow uh give them a framework to you know for instance I'll sign a NDA uh if they want me to look
[2272.24 → 2276.82] at their pieces of software so it gives them legal coverage it gives them uh gives me obligation to actually
[2276.82 → 2279.92] work on that so it's actually a great model I actually did the same thing with requests i
[2279.92 → 2285.70] decided to do a request pro where someone can just basically decide to support it financially but
[2285.70 → 2290.18] there's no difference like with the license or anything like that yeah sure, and it seems to be
[2290.18 → 2296.44] working really well to be clear uh Kenneth does accept bribes for dinner but from the looks of it
[2296.44 → 2299.48] it would only be in black and white very funny
[2299.48 → 2309.14] um no but yeah it's an it's a very, very cool uh I don't know what the word is uh you know don't
[2309.14 → 2314.58] call it a monetization stretch no it's all about sustainability yeah yeah absolutely we talk about
[2314.58 → 2320.84] that a lot on the changelog about how to um not get burnout how to sustain the project how to you know
[2320.84 → 2326.66] it's all about sustainability and I think this is a cool way to just you know to necessary to help
[2326.66 → 2330.98] that and I think that's something that um you know we should be trying different solutions to
[2330.98 → 2335.94] solve that problem man that was a wordy poorly constructed absolutely that's that's a that's a
[2335.94 → 2343.24] great point you know this is it mat tam I on get tip I am not on get to i maybe I don't know that
[2343.24 → 2347.68] that model is well I guess we can talk about that some other time I don't really have fully formed
[2347.68 → 2352.34] opinions about it but uh I don't know maybe it's just not for me, I don't want people to feel
[2352.34 → 2357.04] obligated yeah it seems like that's kind of where we're at right now, and we had chad on the
[2357.04 → 2362.48] show uh with Kenneth actually you know a while ago, and it seems like everybody right now is at a place
[2362.48 → 2367.32] where the opinion is not fully formed so it's up to chad and the and the get-up guys to uh or the get
[2367.32 → 2373.42] it uh open source people to uh, uh as he put it bring your own carrot and help to get people involved
[2373.42 → 2378.66] absolutely and uh yeah not to disparage him at all I think what he's doing is amazing work and
[2378.66 → 2383.56] you know I'm a big fan of him personally uh yeah from what I read about him so yeah it's an it's a
[2383.56 → 2388.08] great effort uh just yeah very interested to see other ideas in this whole space by any chance did
[2388.08 → 2394.94] you happen to catch um Chad's article on the changelog called open products uh
[2394.94 → 2402.76] maybe it was lengthy it was definitely enlightening so yeah he's got a unique view on just life and
[2402.76 → 2410.18] uh the world, and it's an encouraging and inspiring one for sure tremendous sure cool so yeah so AF
[2410.18 → 2416.98] networking um got a got 2.0 coming out uh sure can I say one thing about uh 2.0 really quick
[2416.98 → 2422.64] about kind of the so one of the responsibilities I feel kind of maintaining a project that's
[2422.64 → 2428.74] so widely used in the community uh is that you know the need to keep pushing forward
[2428.74 → 2433.38] just like apple does uh you know hopefully not as ruthlessly as they do kind of deprecating things
[2433.38 → 2438.38] uh that people are still kind of using but uh the direction I want to go forward is to kind of
[2438.38 → 2444.38] anticipate the needs for real-time uh communication so a lot of iOS applications what I'm hearing from
[2444.38 → 2449.70] people are that they need a way a consolidated way to kind of reconcile this document-based paradigm
[2449.70 → 2454.56] uh with the stream of updates that come whenever you're in constant communication with the server so
[2454.56 → 2460.50] uh AF networking 2.0 will feature uh server sent event support so it's implementing the uh basically
[2460.50 → 2467.28] an analog to the event source API uh that you're used to in the Dom uh with JavaScript uh and uh it's
[2467.28 → 2472.54] actually part of this whole manifesto of uh how to develop web technologies that I'm calling rocket
[2472.54 → 2480.96] if you go to rocket.GitHub.io uh it's sort of my ideas about how modern applications should be built
[2480.96 → 2485.74] it's its hard to describe what this is I mean it's like a technique sort of like comet or Ajax where
[2485.74 → 2491.06] it's kind of up to interpretation, but the basic premise is this you again it's its it's making
[2491.06 → 2495.62] the conceit that there are documents, and you make rest calls to those and on top of that architecture
[2495.62 → 2500.58] which a lot of applications are already built on you have a stream paradigm where you're subscribing to
[2500.58 → 2507.48] changes for that particular resource so you get resources, but you also get resources but request a
[2507.48 → 2513.28] text event stream and in that event stream uh whenever a resource is created or updated or
[2513.28 → 2519.18] deleted uh what you can receive in your know in your connection back through service and events
[2519.18 → 2523.94] uh is another great standard that's that just came out a couple of months ago uh from one of our
[2523.94 → 2530.94] Salesforce colleagues uh it's called Jason patch which is finally a RFC specification for how to model
[2530.94 → 2539.18] changes in a data set so it's Jason encoded um you know the text event stream is text but the data
[2539.18 → 2545.14] aspects could be interpreted as Jason very easily uh, and it gives you a very direct way to send
[2545.14 → 2554.96] changes even complex changes uh Jason patch supports add remove move copy uh delete and test for existence
[2554.96 → 2559.72] so it's actually quite uh versatile and can support I think a lot of different paradigms
[2559.72 → 2565.54] and just using this persistent connection uh kind of in parallel with a document request response model
[2565.54 → 2570.68] I think is a great way uh forward for existing applications to incorporate real-time functionality
[2570.68 → 2575.78] pretty easily this is fascinating I've never seen anyone use server sent events uh outside the
[2575.78 → 2581.34] browser before yeah it was actually pretty easy to implement but uh yeah I don't think anybody else
[2581.34 → 2585.18] has really applied those directly service and events sort of gets overshadowed by web sockets
[2585.18 → 2590.26] yeah, but the thing about web sockets is we don't need to buy directionality so instead what we have
[2590.26 → 2596.60] is a unified http based uh solution that allows you to build applications uh right on top of how you're
[2596.60 → 2600.68] already building them I think it's a pretty compelling offering and I'd love to hear some more ideas on
[2600.68 → 2604.58] this is how I'm going to build things from now on you're putting this directly into NF AF networking
[2604.58 → 2612.44] yes the uh so it's the event source and the Jason patch are that's going to be a kind of first class
[2612.44 → 2617.74] extension on top of things and I will continue to maybe incorporate that into AF incremental store
[2617.74 → 2625.78] and actually the server sent events solve one of the uh existential problems of AF incremental store
[2625.78 → 2631.62] which is the unknown in that if an is something gets deleted on the server side there's no
[2631.62 → 2637.76] great way to know about that on the client unless you ask for that resource directly and get a 404 or
[2637.76 → 2643.46] a 410 if you want to be responded that if you want tweets to be deleted off of their feed in real time
[2643.46 → 2649.86] you got to do that so you said that it's like a first class extension and I wanted to kind of
[2649.86 → 2655.60] to hit on this would you say so you have your official and your third party extensions um so you support
[2655.60 → 2661.50] oh you know one and two s3 Jason RPC, and then you have your AF incremental store and now what you're
[2661.50 → 2666.46] talking about are is that going to change at all with 2.0 or how much work has to go into the
[2666.46 → 2673.64] extensions with the changes if any sure well i I do intend to upgrade all the extensions to AF
[2673.64 → 2678.02] networking 2.0 it shouldn't be that much work though because the API is relatively compatible
[2678.02 → 2684.22] uh fortunately it's it was actually a really easy way to uh pretty easy to swap out uh one back
[2684.22 → 2692.96] end to another so uh most people won't notice the change gotcha yeah so 2.0 coming out Thursday
[2692.96 → 2700.46] very very exciting cool project i uh i am very interested and excited to actually spend some
[2700.46 → 2707.04] time digging into this and uh learning from it thank you again I have to give a lot of credit to
[2707.04 → 2712.70] the community for you know their amazing support of the project uh again two years in over 100
[2712.70 → 2719.24] contributors uh maybe something like 2 000 forks uh you know over a thousand closed issues yeah it
[2719.24 → 2725.48] it's really the project that got me to where I am in the community uh it did you learn so much from
[2725.48 → 2730.08] being part of a large project, and you know I'm extremely fortunate that I had the opportunity to
[2730.08 → 2737.02] uh you know learn so much and hopefully people you know find it to be useful awesome so to you do have
[2737.02 → 2741.96] a hard out so we don't want to hold you uh too long so to the listeners that kind of know about
[2741.96 → 2746.62] the changelog um and to those that don't we kind of have a few questions that we like to ask at the
[2746.62 → 2751.44] end of every episode um so go ahead and ask them the first question is for a call to arms and for
[2751.44 → 2756.88] any of your products um that you're kind of have out there what would you like to see the
[2756.88 → 2761.86] community to kind of rally around and work on sure I mean as much as you can if you're doing a new
[2761.86 → 2766.00] mobile project I would encourage you to try out Helios try out AF networking uh the new version
[2766.00 → 2770.96] 2.0 uh I know a lot of people are going to be making either updates or new projects with iOS 7
[2770.96 → 2775.32] try it out let me know what you think uh but in general I think a greater call to action is to
[2775.32 → 2780.54] you know release stuff as much as you can in open source if you have a piece of code in your project
[2780.54 → 2785.90] that you find to be useful and think you can abstract out to general usage I'd love to see you
[2785.90 → 2790.44] know a new cocoa pod out of that I'd like to see a new gem out of that um you know the community
[2790.44 → 2797.80] grows again as a gift economy that we give each other gifts, and you know everybody succeeds together
[2797.80 → 2804.94] that's it sounds uh sort of granola maybe even communist e, but really it's ideal because there's
[2804.94 → 2812.96] no materiality to it, we can just share information freely it's a kind of great way uh to benefit from
[2812.96 → 2818.02] everybody's expertise and their passion and uh it really makes the open source community really special
[2818.02 → 2824.86] cool if you weren't doing iOS development uh what would you be doing instead you know what i
[2824.86 → 2830.60] found my I think I found my passion uh just the other day I tried hang gliding for the first time
[2830.60 → 2835.34] oh now i I don't know what it is maybe it's a quarter life crisis but I started doing a lot of
[2835.34 → 2841.28] air sports I'm working on my pilot's license I went skydiving uh just a couple of weeks ago uh probably
[2841.28 → 2847.78] be going again soon but hang gliding oh my goodness that is uh a rush and thrill beyond belief and
[2847.78 → 2852.12] it's just something that clicked instantly uh I would encourage you don't tell your parents about
[2852.12 → 2858.14] it but that you're going tell them afterwards but man or your wife or husband don't tell them
[2858.14 → 2863.68] until afterwards or take them with you, I guess uh just really cool when you get your pilot's license
[2863.68 → 2868.70] uh feel free to swing by Nashville and take me on out to the Heroku headquarters to hang out
[2868.70 → 2874.08] that sounds great and lastly for your programming hero something you want to give a shout-out to
[2874.08 → 2879.70] uh shout out to why the lucky stiff of course uh just a hero to a lot of us in the ruby community
[2879.70 → 2886.06] but uh also to Sean Inman who uh is somebody that I look up to immensely uh kind of triple
[2886.06 → 2892.12] threat that he's a designer you know a brilliant pixel artist a great programmer uh and does his
[2892.12 → 2898.00] own music composition writes thoughtful uh you know pieces on his process and just an amazing guy so
[2898.00 → 2904.22] definitely look up to him and has been an inspiration my whole career yeah his 8-bit or pixel
[2904.22 → 2910.80] stuff is some of my favourite for sure it's its amazing what did you think about uh why's somewhat
[2910.80 → 2917.36] return recently you know what I almost didn't want to get burned, or it was sort of like there was a
[2917.36 → 2923.12] closure to it all and uh you know when you reanimate corpses you sort of get a zombie effect potentially
[2923.12 → 2928.84] so i kind of wanted to let sleeping dogs lie until uh you know the jury was still out but I guess
[2928.84 → 2933.54] you know sending cryptic communications through postscript documents is a pretty cool way to
[2933.54 → 2938.26] communicate from the grave and that's pretty much what you would expect so absolutely I'm not going
[2938.26 → 2944.30] to try to be controversial here but uh I do believe that he was at pi con last year there you go i I met
[2944.30 → 2949.06] him in real life he taught a class uh at Carnegie Mellon he was playing the auto harp the whole time
[2949.06 → 2955.78] he lectured in song and verse it was a life-changing experience yeah he did a he was uh 410 gone he was
[2955.78 → 2962.26] not gone from the world I think he's you still there it's almost like the uh the Sasquatch you there's
[2962.26 → 2969.36] there's why spottings all around the world he's 410 gone not real gone yeah yeah I like that that's good
[2969.36 → 2975.66] it's definitely been fun having you on the show Matt uh man so much so many I mean we could have gone
[2975.66 → 2981.50] on and on literally I mean I almost wanted to talk about some other things too but I know that uh
[2981.50 → 2986.36] we got a time box here but definitely cool having you in the show thank you so much for everything
[2986.36 → 2991.64] that you do in open source and the way that you're supporting mobile development uh you know to lament on
[2991.64 → 2997.92] what you said earlier in the show I like your uh I guess your perspective you know versus um
[2997.92 → 3003.00] what you said your job at Heroku is to help you know grow mobile development on there instead of
[3003.00 → 3007.98] trying to like market you're growing the user base I guess of mobile development that's a perfect
[3007.98 → 3013.96] perspective so oh, thanks a lot and thanks you know the changelog I think does a lot to humanize and
[3013.96 → 3018.66] give a voice to open source, so thank you guys for uh really being a guiding voice for all that not to
[3018.66 → 3023.86] suck up too much but really you guys you know hats off thank you man we certainly appreciate it
[3023.86 → 3030.26] it's what makes this worthwhile that's for sure absolutely but uh we're live every Tuesday this
[3030.26 → 3036.74] is uh the changelog sunny also let's say goodbye guys see you all later fare thee well AU Lavoie
[3036.74 → 3036.88] you
