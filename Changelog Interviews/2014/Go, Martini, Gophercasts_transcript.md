[0.00 --> 14.80]  welcome back everyone this is the changelog where a member supported blog podcast and weekly email
[14.80 --> 20.76]  what's fresh and what's new in open source you can check out the blog at the changelog.com our
[20.76 --> 26.62]  past shows can be found at 5by5.tv slash changelog and subscribe to the changelog weekly that's our
[26.62 --> 31.12]  weekly email we send out every saturday covering everything that hits our open source radar
[31.12 --> 37.54]  subscribe at the changelog.com slash weekly you're listening to episode 117 where jared
[37.54 --> 43.74]  santon and i talk to jeremy signs about go martini the go ecosystem and even a little bit of node as
[43.74 --> 49.44]  well today's show is sponsored by digital ocean new relic and top towel we'll tell you a bit more
[49.44 --> 55.26]  about new relic and top towel later in the show so stay tuned but our friends at digital ocean they're
[55.26 --> 60.44]  a simple cloud hosting provider dedicated to offering the most intuitive ways to spin up a
[60.44 --> 66.28]  cloud server you can spin up a cloud server in 55 seconds with full root access and it just doesn't
[66.28 --> 71.98]  get any easier than that pricing plans start out affordably at five bucks a month for half a gig of
[71.98 --> 79.02]  ram 20 gigs of ssd ssd drive space one cpu one terabyte of transfer and if you only need a server
[79.02 --> 84.02]  for a few days or to test an app you can even rent that server basically by the hour so it's
[84.02 --> 93.08]  super inexpensive just 0.007 cents an hour that's like it's hard to even say but it's less than a
[93.08 --> 100.58]  penny per hour it's 0.7 of a cent so super affordable but we have an awesome promo code for you to use
[100.58 --> 108.04]  use the promo code changelog april to get a 10 hosting credit when you sign up head to digitalocean.com
[108.04 --> 114.66]  to get started and now on to the show we're joined today by jeremy signs also known as code gangsta we
[114.66 --> 120.08]  had a quick laugh there for a bit but uh he's known as code gangsta on twitter and github and i guess
[120.08 --> 125.08]  probably everywhere else right jeremy that's right uh pretty much everywhere else except skype my skype
[125.08 --> 132.30]  name has not changed yet as you guys see yeah he's here to talk to uh to me and the managing editor of
[132.30 --> 139.00]  the changelog jared santo about the go programming language his fun with it what he's been doing uh
[139.00 --> 144.68]  specifically his web framework for go called martini and a bunch of other fun stuff so jeremy
[144.68 --> 151.68]  welcome to the show man oh thanks i'm really glad to be on here so i i know that uh you've been a fan
[151.68 --> 157.04]  of the changelog right i do you tweeted it to us a couple maybe a week back and and uh we wanted to
[157.04 --> 160.36]  get you on the show anyways and you just kind of fast forwarded that a little bit yeah yeah i've
[160.36 --> 167.64]  been catching up on episodes um the first one i watched i'm not a long time fan but i uh i started
[167.64 --> 173.40]  watching uh katrina katrina owens podcast and i started catching up on all the other ones since
[173.40 --> 178.90]  then and um yeah i think it's a great podcast i i personally love the idea of podcasts i try to
[178.90 --> 185.22]  listen to as many as as possible and uh yeah so i'm super glad to be on here i'm glad i was able to
[185.22 --> 192.76]  just like uh totally get in your face and be like put me on the show yeah that's cool but jared was on
[192.76 --> 196.70]  uh the katrina show as well we had fun on that one didn't we jared yeah that show actually probably
[196.70 --> 203.54]  has a lot of similar similarities to this one between the ruby and go influence yeah and uh you've been
[203.54 --> 212.28]  uh doing different uh what do they call it exercises in uh exorcism oh me oh yeah yeah i don't know i guess
[212.28 --> 218.74]  exercises is is the fair term exorcism.io was is katrina's project yeah and yeah i've been having
[218.74 --> 225.32]  a lot of fun uh getting my code reviewed up in there and nitpicked as she likes to call it and uh
[225.32 --> 231.96]  that's right yes learn a lot you learn a lot yes well jim but where do we where do we begin for you
[231.96 --> 238.74]  i mean i know that gangsta oh man let's hear it like what code gangsta so the cat's getting out of
[238.74 --> 243.20]  the bag now we'll get it out of the way here because yeah so this goes all the yeah this goes
[243.20 --> 247.98]  and you can find out more about it on my blog but this goes all the way back to me starting in the
[247.98 --> 256.34]  industry um i actually started in the flash and flex world doing front-end development um and the way i
[256.34 --> 263.60]  got into it was i was graduating high school and i didn't really know what to do with my life so i i
[263.60 --> 268.42]  ended up going to this conference about programming that i didn't really know too much about and to
[268.42 --> 273.12]  break the ice and to kind of meet people there i entered into this video contest and i was like do
[273.12 --> 278.90]  you know what i have a background in music i have a background in audio i'm gonna make a technical rap
[278.90 --> 287.00]  song and i made this uh rap song called flex gangsta and that was my uh that was that was my name for a
[287.00 --> 294.00]  while i i did a couple rap songs um after that and i don't really talk about it too much anymore
[294.00 --> 299.76]  but i still have code gangsta floating around and it's it's kind of fun to to see people every once
[299.76 --> 305.36]  in a while i'd be like oh my gosh you're you're code gang or you're flex gangsta or you're code gangsta
[305.36 --> 310.88]  and it's funny seeing certain implementations of the song like some people have it uh some people
[310.88 --> 316.82]  have one of the songs which is uh titled who broke the build uh it's tied in with their jenkins server
[316.82 --> 321.12]  so if somebody actually breaks the build they like send the video or send the song to them via email
[321.12 --> 326.62]  or it plays in the office so so these tracks are out there to be to be heard right now on the web
[326.62 --> 332.34]  they're on youtube if you search flex gangsta you would find them on youtube nice so then you
[332.34 --> 336.88]  switch to code gangsta because you just figured you're going to get more abstract and just genericize
[336.88 --> 342.76]  your name or something oh yeah yeah i left the flash world um oh quite a while ago and so it's not
[342.76 --> 350.86]  as relevant anymore uh flexgangsta.com did you know there's a.com i i think that is my flexgangsta.com
[350.86 --> 356.06]  there you go updated in a very long time and you got who broke the build on there that's awesome we'll
[356.06 --> 360.38]  link out that in the show notes but you can go to flexgangsta.com right now if you want to but we'll
[360.38 --> 364.78]  in the show notes we'll have some some links out to it yeah if you find me at a conference and buy
[364.78 --> 371.26]  me a drink i might i might do some raps for you fair warning wow have you ever seen uh chris anderson's
[371.26 --> 378.78]  uh couch db song it's probably not quite as epic as your your uh your rap you know what i have not
[378.78 --> 386.44]  on the channel like a while a while ago we we met him at uh him and uh yon leonard we met them at uh
[386.44 --> 394.14]  south by and uh we had uh chris anderson right there they were there obviously for south by and
[394.14 --> 401.02]  and he was just like he's a crazy guy anyways and he was just riffing and uh it's like bump bump couch db
[401.02 --> 405.48]  it's just like a little thing i'll have to point back to the episode so y'all can listen to it but
[405.48 --> 411.00]  it's pretty funny oh man it must be a thing with coders we like to we like to rap that's right it's
[411.00 --> 419.92]  the it's the way we communicate so code gangsta so who would have known who would have thunk you know
[419.92 --> 428.32]  so jeremy i think the first time i i i saw your name i saw the code gangsta handle um was on your blog
[428.32 --> 432.30]  and you wrote a post that ended up kind of making the rounds at least in the tech community
[432.30 --> 438.94]  um around your switch from ruby to go um specifically i think it was around command line applications
[438.94 --> 447.86]  yeah oh yeah yeah so uh this is kind of how like hacker news operates if you write a post that is
[447.86 --> 456.14]  even remotely could even possibly be somewhat controversial it will be on the front page and
[456.14 --> 462.98]  stay on the front page and that's precisely what happened basically um i wrote a post titled
[462.98 --> 468.74]  on distributing command command line applications why i switched from ruby to go you know that sounds
[468.74 --> 475.02]  very uh it still sounds very nice it still sounds very civil but instead hacker news chopped off that
[475.02 --> 481.68]  front part and just titled it why i switched from ruby to go oh my gosh flame bait and uh yeah
[481.68 --> 488.32]  definitely got a discussion going um there was no intention to be controversial whatsoever um i i
[488.32 --> 492.80]  simply came from a place where i was writing a lot of command line apps in ruby um specifically like
[492.80 --> 498.06]  production facing command line apps that we were distributing to users who were not who are not rubyists
[498.06 --> 504.88]  um so to uh one we didn't want to distribute it as a ruby gem because why why be like just use
[504.88 --> 513.44]  ruby gems to a guy who's not writing ruby and uh so we had to do all these crazy things like vendor our
[513.44 --> 519.36]  gems and you know distribute our own version of ruby package it up in an installer and like cross your
[519.36 --> 525.56]  fingers and hope it all works on you know somebody's distribution um and that was just a very very painful
[525.56 --> 532.32]  process to work out just to get ruby running um on somebody's machine so i looked into some other
[532.32 --> 538.94]  alternatives and it seemed like go is uh very you know very unix focused so it means it's probably
[538.94 --> 546.74]  pretty good for the command line and i just loved how simple it was to construct uh really good command
[546.74 --> 552.54]  line applications that ran fast that were compiled into a single binary and could be cross compiled to
[552.54 --> 558.46]  multiple os's so that's that's mainly why i wrote that uh wrote that blog post and wrote a library called
[558.46 --> 563.12]  cli um and it seems to be people seem to be following in that same sentiment that's like
[563.12 --> 568.40]  if you're not writing a tool for rubyists to use while they're developing ruby you probably don't
[568.40 --> 573.04]  want to write a command line tool in ruby it's just it's too painful which i think i mean just
[573.04 --> 580.26]  we're hearkening back uh to katrina again she had a similar experience with her exorcism command line
[580.26 --> 587.40]  client where she wanted exorcism to be not just ruby focused but you know there's python uh exercises
[587.40 --> 592.72]  there's haskell i think now copy script there's all sorts of languages and so she wanted to remove
[592.72 --> 599.36]  that dependency for people to use her tool from the command line the ruby dependency so she ended up
[599.36 --> 604.34]  rewriting her command line piece and go so let me ask you this then if you're moving from
[604.34 --> 610.96]  distributing is a ruby gem and not requiring ruby you're distributing is go but is it still required
[610.96 --> 618.42]  then is go required uh no go allows you to cross compile um basically to a standalone binary which
[618.42 --> 625.56]  is really great um because it'll it'll basically work on any os that has libc pretty much and so
[625.56 --> 629.22]  drop it into your bin folder hopefully you got that in your path and you're good to go yep exactly
[629.22 --> 637.02]  um and the great part i mentioned cross compiling um uh in general it is dependent on what you do but
[637.02 --> 643.30]  in general you can cross compile most applications um meaning like on my on my mac box i can compile for
[643.30 --> 650.96]  windows and different flavors of of linux and my mac as well um and even stuff like arm and that way i
[650.96 --> 655.72]  can just like here's a distribution here's a release and i just like build it all on one computer which
[655.72 --> 664.02]  is which is really great nice so yeah the fruit of that came uh your project cli.go are you still
[664.02 --> 668.48]  maintaining that is it ongoing or is it kind of a finished thing and maybe explain exactly what it
[668.48 --> 675.00]  what it provides yeah so i am maintaining it um there are going to be small little additions to it
[675.00 --> 680.96]  the way the api is structured it's not uh it's not meant to be changed a lot and and it kind of
[680.96 --> 688.02]  falls in line with the philosophy behind go packages currently um which is keep master always
[688.02 --> 694.40]  backwards compatible um and i haven't there's been edge cases obviously to try to fix and and some
[694.40 --> 698.58]  edge case problems but in general most people seem to be pretty happy with it and it seems to be a very
[698.58 --> 704.50]  good starting point for creating command line apps and generating help docs and everything like that but
[704.50 --> 709.60]  i'll be honest it's not the most extensible framework in the world it was really just meant to be like
[709.60 --> 714.64]  i don't want to think about you know help docs and parsing sub commands and parsing flags i just want to
[714.64 --> 719.48]  start writing the actual meat of the code and so that's what it does and it does it tends to do it
[719.48 --> 725.92]  pretty well and so i think that's where the popularity of the library came from right on so
[725.92 --> 731.68]  you just kind of triggered a a tangential question that i've been waiting to ask somebody who's who's
[731.68 --> 738.66]  in the go community what's the the package management story in go um how does that fit into like if
[738.66 --> 745.48]  you're building a command line application or even with martini um is there i know there's go get is
[745.48 --> 753.44]  that the is that the whole story yeah so uh right now the package solution or the the the package
[753.44 --> 758.72]  management solution for for go is it just a very simple one it's a very primitive one you use go get
[758.72 --> 765.62]  you can import uh libraries with go get the the great part about how imports and go get works
[765.62 --> 772.96]  is that um a path is a path is a path meaning my library when i imported my code is github.com
[772.96 --> 779.48]  slash code gangsta slash cli um that way if it will first check locally on your computer if you have it
[779.48 --> 784.96]  and if you don't it will go and pull it down so um it's cool to have that kind of uniform identifier
[784.96 --> 790.48]  uh with your code so that's why you've got to keep master good yes that's why you got to keep
[790.48 --> 796.08]  master good is there's no um as of right now there's no built-in idea of versioning and that
[796.08 --> 803.58]  is intentional uh it is intentional at least for the moment um because a lot of the go maintainers
[803.58 --> 809.16]  want you to build packages that are useful and that do uh that are small that do you know a certain
[809.16 --> 816.02]  set of things very well that aren't going to be you know completely innovative innovated and iterated
[816.02 --> 823.98]  upon during its development cycle um there are some there are some initiatives for bringing in
[823.98 --> 829.56]  things like versioning because we realize that's like theoretically a really cool idea but in practice
[829.56 --> 835.70]  it's it it can be harmful depending on you know how many dependencies you're pulling in and how you're
[835.70 --> 840.14]  managing those and i know there are external tools for doing them that i use for certain projects
[840.14 --> 846.52]  and there's some other solutions that i've been uh working on as well uh specifically with regards
[846.52 --> 851.90]  to martini and cli um to be able to iterate on those packages for people to be able to pull in
[851.90 --> 858.90]  versions uh that are different so you mentioned jared you mentioned go get and are you going to
[858.90 --> 865.80]  allude to the fact of like go unget because i don't know how to not get long story short i don't
[865.80 --> 870.00]  either you know what i mean like if i if i if i go get something i want to like let's say uninstall
[870.00 --> 876.06]  remove it how do you uninstall things um you remove the folder where it's at see that's what i thought
[876.06 --> 880.66]  and that's what i was doing i was like am i an idiot or something so at least i'm not an idiot hey man
[880.66 --> 886.96]  you're doing it right yeah is that the i mean is that really the way that is it just because go is
[886.96 --> 891.88]  somewhat new and the things are still kind of evolving how things should work and yep i think i think
[891.88 --> 899.02]  we're since go is still a fairly new language fairly new technology um and it's very grounded
[899.02 --> 904.26]  in unix philosophy so a pure unix guy would be like yeah there's no problem deleting a folder that's
[904.26 --> 907.90]  what you do that's what folders are for that's what directories are for and that's what the file
[907.90 --> 913.30]  system's for um but i could understand it being a roadblock for people who are used to having tools
[913.30 --> 918.38]  take care of a lot of things for them i think even though the folder it comes in has a bunch of
[918.38 --> 924.22]  other stuff in it so i'm like should i delete that stuff you know i guess as a someone coming
[924.22 --> 931.40]  in that with lack of experience in it i'm like you kind of have a an immediate bit of fear you know
[931.40 --> 936.90]  should i do that well what was the cause of it or what would happen if i do do that and then next
[936.90 --> 941.68]  thing you know you've got your go directory that's got bin package and source in there and you got like
[941.68 --> 947.30]  do i just delete it all like some of it and you're you know that's that's where i that's where i was
[947.30 --> 953.20]  like i'm not sure adam i think the answer for you is you keep jeremy available on skype okay and
[953.20 --> 958.02]  then you just throw these questions at him as you go that's right you'll just right i'm here all
[958.02 --> 965.10]  night so you so so you do this command line app and you enjoy distributing command line applications
[965.10 --> 970.64]  with go are you doing this for your for your work as well or is it all for play uh for command
[970.64 --> 978.40]  line stuff it's all for play in general uh we do use some of the tools uh one of them um one of them
[978.40 --> 984.52]  i'm working on is called envy it's an environment bootstrapper and it if you're used to working with
[984.52 --> 992.10]  web frameworks like you know express and node.js or or rails and ruby there's a concept of a .env file
[992.10 --> 996.70]  which is basically saying we want to store our configuration in in our environment we don't
[996.70 --> 1001.90]  want to like run a run a shell script every time to like bootstrap our environment and we obviously
[1001.90 --> 1006.86]  don't want to like have anything checked into the repo um for that stuff because we're dealing with
[1006.86 --> 1014.38]  passwords and you know tokens for authentication for certain services so you have a .env file that
[1014.38 --> 1018.86]  declares all that stuff and it's local to your machine um so you can set it up and manipulate it
[1018.86 --> 1026.50]  however you want uh so this this env bootstrapper called envy allows you to do this in a generic way
[1026.50 --> 1031.36]  most .env implementations are tied to the language you use them in like node.js or
[1031.36 --> 1039.68]  uh javascript for node.js or ruby for rails this one's very generic all you do is you call envy and
[1039.68 --> 1044.32]  then you pass whatever command you want after it and it will bootstrap the environment and then run
[1044.32 --> 1049.00]  the command that way you have all your environment variables present to you and you they're all declared
[1049.00 --> 1053.06]  inside of a file so it's really really cool for running servers it's great for development
[1053.06 --> 1057.96]  uh for web development for command line development for any of those things
[1057.96 --> 1065.64]  nice so you do that one for work where'd martini uh come from was this just a natural extension of
[1065.64 --> 1070.54]  of building command line applications and now you said okay now i want to build my web applications and go
[1070.54 --> 1080.36]  yep so martini uh came out of i i do uh web work for uh my day job and i wanted to i was building some
[1080.36 --> 1084.86]  angular front ends and we were looking at a new project and we're looking at doing you know more
[1084.86 --> 1091.78]  distributed architecture we we were usually a rails shop and in these new projects we're writing node.js
[1091.78 --> 1097.38]  we wanted to write go we want to write some more you know ruby and rails and we just want basically want to
[1097.38 --> 1104.44]  find the best tool for the job for each uh particular section of our application so that made me excited
[1104.44 --> 1109.48]  because i was playing with go for command line stuff already and so i started playing with go for the web
[1109.48 --> 1113.96]  and i played with a bunch of other frameworks and i built a couple projects in different frameworks just
[1113.96 --> 1121.10]  to get a get a feel for them and i was having a hard time finding uh just a sense of reusability
[1121.10 --> 1128.32]  among those web frameworks i know like ruby has rack and they unify on on rack in general all the web
[1128.32 --> 1133.44]  frameworks in ruby and and node.js kind of they have quite a few frameworks that unify on connect
[1133.44 --> 1141.12]  and so i wanted to create some sort of middleware stack um that one gophers would like um that wouldn't
[1141.12 --> 1147.36]  be too far flung from the original go net http library and two stuff that people would actually build
[1147.36 --> 1153.20]  value on a big um big proponent on on building value when you're writing code you should be writing
[1153.20 --> 1160.08]  something that's valuable um and so i started martini as kind of a container for that uh martini
[1160.08 --> 1166.88]  itself doesn't do like extremely useful things it's it's mainly just architecture and a lot of sugar
[1166.88 --> 1173.52]  to be able to create a lot of valuable components that are reusable across multiple types of web applications
[1173.52 --> 1181.78]  cool just pausing a second on the name and i i believe i i i read you say this on the mailing list
[1181.78 --> 1186.94]  but i don't recall the name martini and then you know the the tagline is classy web development in go
[1186.94 --> 1193.78]  uh it just calls to mind that that kind of epic spilled martini error page of sinatra is sinatra like
[1193.78 --> 1199.38]  the primary inspiration for martini yeah sinatra is definitely one of them express from node.js is
[1199.38 --> 1207.14]  is another those are both fantastic uh frameworks they they focus on simplicity and modularity and
[1207.14 --> 1214.80]  and elegance and martini sounded really cool i mean it's a martini is obviously a mixed drink um you know
[1214.80 --> 1221.70]  in this time there's like so many you can call any cocktail martini nowadays it's not just gin and
[1221.70 --> 1226.62]  vermouth so like it's true when i think of a web app i think you know there's different requirements for
[1226.62 --> 1232.62]  for any kind of web app or service and and i can't just make a set of like middleware or a set of
[1232.62 --> 1236.54]  components that everybody's going to use they're all going to create their own and that's when i
[1236.54 --> 1241.28]  thought of like okay it's like a cocktail it's like a martini like sure i don't like appletinis but the
[1241.28 --> 1245.36]  person next to me really likes appletinis and i don't believe an appletini is a real martini but
[1245.36 --> 1251.76]  that doesn't matter the guy still likes his appletini and i feel the same way about the web um you can
[1251.76 --> 1258.30]  have whatever opinions you want but martini tries to be a good container for uh creating kind of your
[1258.30 --> 1267.60]  own cocktail your web cocktail of sorts cool so martini provides um just the core martini we'll talk
[1267.60 --> 1274.02]  about martini contrib which i believe is like you know provides way more stuff but the martini proper
[1274.02 --> 1281.50]  library um basically it's a middleware stack that has a routing layer in it and some sort of dependency
[1281.50 --> 1286.32]  injection is that is that the gist of it or is there more that i'm missing though that's pretty
[1286.32 --> 1292.30]  much the gist of it okay so then the contrib libraries were all the other because i mean beyond
[1292.30 --> 1301.30]  that most web apps are going to need you know session handling csr csrf protection uh you know
[1301.30 --> 1307.10]  the whole host of things that that kind of people become used to um is that what stuff lives in contrib
[1307.10 --> 1314.34]  yeah yeah so uh to go back to martini for a sec i was building uh i was mainly building martini for
[1314.34 --> 1320.84]  for two different kinds of web apps uh for my application it was uh rest-based you know services
[1320.84 --> 1325.70]  that they're just serving jason so and they're talking to other services not even talking to a
[1325.70 --> 1332.16]  browser so there there's even no use for like cookie-based sessions or anything like that so that's
[1332.16 --> 1339.40]  that that might be the answer to why some middlewares are in martini contrib rather than martini itself
[1339.40 --> 1345.16]  and um i kind of just wanted to elaborate more on the dependency injection some people really shy away
[1345.16 --> 1351.06]  when i use the word dependency injection uh because they're like oh my gosh java ioc containers oh no
[1351.06 --> 1360.12]  yeah uh this is gonna be terrible i was thinking just that yeah okay so um i i i actually have a love
[1360.12 --> 1364.82]  for dependency injection when it's used well and it's actually my uh it starts to become whenever
[1364.82 --> 1368.32]  i'm picking up a new language i i tend to be like okay i'm gonna write like a dependency injection
[1368.32 --> 1373.32]  system to see how i can make modular code with this language so if you look at my github i have like
[1373.32 --> 1379.60]  one in c sharp one in action script one in javascript um i i've written not on github but i've written
[1379.60 --> 1387.48]  one for objective c and uh obviously go and ruby so i i've kind of played a lot with how like how to
[1387.48 --> 1394.06]  manage dependencies within applications and i try to find the best fit for one um in this case and a
[1394.06 --> 1399.10]  lot of people absolutely love it because it it really extends the modularity of martini the way
[1399.10 --> 1405.54]  the dependency injection works is you just you map something by a type and go go strongly typed it's
[1405.54 --> 1413.66]  statically typed so you can you have types everywhere right and you you map something that's a type
[1413.66 --> 1418.08]  let's say it's like a database you have this database connection and you map it to martini
[1418.08 --> 1424.30]  either on a global or a request level and every one of your martini handlers which is really just a
[1424.30 --> 1429.96]  function they can ask for that dependency in their argument list so it's very close to if you're used
[1429.96 --> 1437.04]  to using angular um for for front end stuff their dependency injection works uh kind of the same way
[1437.04 --> 1442.24]  on functions where you just ask for it and it gives it to you yep uh it's so brain dead it's very
[1442.24 --> 1447.36]  intuitive it's super easy to test because now you have functions that don't actually reach outside
[1447.36 --> 1454.28]  of itself it all just goes in through its argument list so that's kind of how the dependency injection
[1454.28 --> 1460.62]  works and why i try to encourage people to not shy away from from that word as much um and it's hard
[1460.62 --> 1466.14]  to try to say like it's something else because it really still is dependency injection um just not in
[1466.14 --> 1470.68]  the way that most people would think let's pause the show for just a minute give a shout out to our
[1470.68 --> 1475.68]  sponsor top towel for those of you out there who are freelancing or maybe you'd like to freelance
[1475.68 --> 1479.98]  or even kind of try out a freelance like project where you're maintaining your full-time position
[1479.98 --> 1486.28]  you have to check out top towel top towel is a new rapidly growing network of some of the most elite
[1486.28 --> 1492.84]  engineers in the world they're distributed all across the globe their primary focus is connecting
[1492.84 --> 1499.36]  their ecosystem of top engineers and top companies you work on special projects with companies like
[1499.36 --> 1507.06]  airbnb idio zendesk and many others you can work remotely on a beach or anywhere in the world
[1507.06 --> 1515.02]  uh to get started head to top towel.com slash developer and click join top towel that's a nice
[1515.02 --> 1523.22]  big old green button you cannot miss it that's t-o-p-t-a-l.com slash developer i think angular
[1523.22 --> 1529.28]  um is kind of warming up more people to the idea and the and the benefits that dependency injection
[1529.28 --> 1537.00]  provides so i think martini fits in fits in nicely there um you know there's a whole host of of
[1537.00 --> 1543.98]  options in the go community for web development in fact we had even a roundup post late last year
[1543.98 --> 1550.88]  um a guest post that laid out a whole bunch of options where does martini fit into that ecosystem
[1550.88 --> 1557.04]  um were you aware of a lot of the options when you started building it and um what do you think
[1557.04 --> 1562.28]  its advantages are um martini has a couple advantages and it also has some disadvantages
[1562.28 --> 1567.98]  from a pure benchmarking standpoint martini is not the fastest framework uh and it and it's not
[1567.98 --> 1574.04]  supposed to be that wasn't my goal in writing it uh there's part of me that believes that go is fast
[1574.04 --> 1578.74]  enough for most applications and if somebody is just looking at hello world benchmarks that they're not
[1578.74 --> 1584.36]  they're not doing their job as far as uh analyzing a framework but that's another topic for another
[1584.36 --> 1593.40]  day um what martini brings in is because of how the dependency injection works and how uh dynamic it is
[1593.40 --> 1601.36]  in that nature it is backwards compatible with all go net http handlers which is a really really cool
[1601.36 --> 1606.58]  feature because things like gorilla http and other handlers that people have published kind of that
[1606.58 --> 1614.12]  work around um the go net http interface they can just throw those in martini and they just work
[1614.12 --> 1619.60]  um and and that's that's kind of that wasn't necessarily an intended thing that was like i was
[1619.60 --> 1624.42]  writing martini one day and it popped up in my mind it's like this needs to be like a bullet point on
[1624.42 --> 1630.20]  them on the martini feature list because it's actually really cool yeah and uh so that's one of the
[1630.20 --> 1636.20]  features and the other feature is just that kind of tags along with that is reusability um you know the
[1636.20 --> 1643.38]  middleware stack the routing stack the fact that you uh there's this kind of you you ubiquity between
[1643.38 --> 1647.78]  handler functions whether or not it's middleware or whether or not it's handling a route like
[1647.78 --> 1654.26]  it doesn't matter it's all the same uh it's just kind of the elegance of that and it's it's really just
[1654.26 --> 1659.14]  building blocks people find out like the core features of martini and they come up with some really
[1659.14 --> 1663.16]  creative ways i love looking at the mailing list because somebody's like i'm writing code like this and i look
[1663.16 --> 1668.72]  at him like wow that's so cool uh or somebody goes this is how i do content negotiation with
[1668.72 --> 1674.78]  dependency injection and how i like observe you know what people want to render out as a struct and
[1674.78 --> 1679.88]  based on you know the header i can then like you know throw it out as json or throw it out as xml or
[1679.88 --> 1685.76]  throw it out as html or whatever and so like people solving real world web problems using those core
[1685.76 --> 1691.38]  building blocks that i didn't necessarily build myself you know i didn't build content negotiation into
[1691.38 --> 1696.48]  martini somebody figured that out through the the building blocks that were laid out so i find i find
[1696.48 --> 1702.26]  that awesome it's just super awesome to see that's kind of neat how you can lay down a set of breadcrumbs
[1702.26 --> 1707.94]  and you know kind of walk away because your needs are different but others pick it up and take it there
[1707.94 --> 1714.44]  yeah absolutely yes i'm looking at the list of available components in the martini-contrib repository
[1714.44 --> 1721.52]  you got auth binding gzip render except blank sessions it goes on and on and on i'm assuming
[1721.52 --> 1724.92]  you didn't write all these and this is these have been community contributed is that fair
[1724.92 --> 1731.08]  yep a lot of them been community contributed i've contributed to um i wrote render and sessions and
[1731.08 --> 1737.80]  auth and uh contributed to a couple others but for the most part all the rest are um you know fully
[1737.80 --> 1745.50]  community community contributed nice so did you expect this this amount of contributions or were
[1745.50 --> 1751.50]  you kind of surprised at martini success and how you know people have uh contributed to the project
[1751.50 --> 1757.18]  oh i've been absolutely blown away by the reception of the project i i wasn't i honestly was not sure at
[1757.18 --> 1763.98]  all what the go community would think of it because because of uh the use of reflection let's say i know
[1763.98 --> 1768.06]  that's like sounds like such a petty thing to worry about but um some communities could be really
[1768.06 --> 1772.64]  hardcore about use of reflection and i have gotten a little bit of friction but in general people
[1772.64 --> 1778.12]  people have come to be pretty understanding and be like yeah martini is not the fastest thing on the
[1778.12 --> 1783.48]  block and me saying that is like we're talking about nanoseconds here it's nanoseconds slower than
[1783.48 --> 1790.84]  you know the next framework or whatever um but it man you can write some awesome code with it and
[1790.84 --> 1796.50]  and very clean code um one example what is okay i was just gonna ask you for an example go ahead
[1796.50 --> 1802.22]  oh cool so one example and this could be linked in the show notes is i wrote a blog post for the
[1802.22 --> 1808.00]  go advent calendar which is a really awesome event put on by brian kettleson over at gopher academy
[1808.00 --> 1815.82]  and eric saint martin and um they organized this 25 days of christmas kind of thing and each and every
[1815.82 --> 1820.18]  single day was accompanied by a blog post by a community member in the go community
[1820.18 --> 1828.34]  and uh i wrote for day 11 i think uh about how to build a simple christmas list app in martini
[1828.34 --> 1836.82]  using some martini contrib um packages like render which is for html templating and rendering and um
[1836.82 --> 1842.96]  what else did i use i also uh created i showed people how to create a mongo db session and use that
[1842.96 --> 1850.16]  and i also used bind to bind form uh part or post form uh parameters to a struct and go and to
[1850.16 --> 1857.08]  use those to um declaratively do that and it all in all it was this full like you know kind of crud
[1857.08 --> 1864.50]  like wish list application in like 150 lines of go it was it was surprisingly concise and extremely
[1864.50 --> 1868.60]  readable and it's a it's a really cool example to point people to because they're like whoa like
[1868.60 --> 1873.50]  you're you're mapping a database and it works concurrently and it does all this cool stuff
[1873.50 --> 1880.80]  and it's it's really readable very cool so as i mentioned in the pre-show i had opportunity
[1880.80 --> 1888.36]  um kind of right when martini first came out to use it at a local hackathon we have a an event here
[1888.36 --> 1894.38]  i'm in i'm from omaha nebraska we have an event called uh hack omaha and our team got to got to
[1894.38 --> 1900.32]  kind of expose some civic data via json api and we we chose martini and had a lot of fun using it
[1900.32 --> 1906.12]  one of the pain points perhaps the only pain point i can remember at the time was uh there's no there
[1906.12 --> 1910.80]  was no live reload which you just kind of come to you get spoiled and you're like man i want my
[1910.80 --> 1916.42]  i want to make my change and not have to restart my my little app server is that still the case with
[1916.42 --> 1922.30]  martini or are there options to to get live reload or was it already out there and i had i just didn't
[1922.30 --> 1929.42]  find it yeah so there are options out there um there are two one of which is written by uh by me
[1929.42 --> 1935.28]  um and the other one is written by i'm gonna totally butcher his name andreas france and he
[1935.28 --> 1941.46]  is um he's an italian uh goling community member and he has a he actually has a web framework called
[1941.46 --> 1947.02]  traffic that's actually quite good um he wrote a project called fresh that is still generic to a
[1947.02 --> 1952.62]  lot of web applications and that um that's command line app that simply does live reload
[1952.62 --> 1957.88]  and that's very good i've looked at the source he's he's a very good programmer and i really like his
[1957.88 --> 1965.48]  stuff um the other application is called gin uh which is you can go find it at github.com slash
[1965.48 --> 1970.74]  code gangsta slash gin and it's not fully documented i still have to put together readme and we're still
[1970.74 --> 1976.00]  kind of in the growing pains phases of it because it's still fairly new but i use it every day for
[1976.00 --> 1982.32]  martini and it does a couple of really cool things it sets up a proxy server to actually serve the
[1982.32 --> 1986.18]  requests so we can do cool things like if there are compile errors we can show them to you in the
[1986.18 --> 1993.62]  browser um and we can also um compile instead of instead of rerunning the app every time after a
[1993.62 --> 2000.60]  compile we actually only rerun the app after you've compiled recompiled and when a request comes in so
[2000.60 --> 2007.40]  it's very much like how the play framework does uh their live reload um and it also adheres to the
[2007.40 --> 2012.00]  silence is golden principle when it comes to compiles so you can keep saving your files anytime
[2012.00 --> 2017.46]  you want and it won't actually like output anything until you have a compile error and then it will let
[2017.46 --> 2021.90]  you know that the compile has been successful so it's a really cool tool it doesn't bother you too much
[2021.90 --> 2027.16]  it's so transparent um all you don't even need to pass it any configuration it works with martini out of
[2027.16 --> 2034.36]  the box you just hit gin and it just works nice yeah looking at that repo now and uh the readme says
[2034.36 --> 2042.50]  gin the web development server for go and that's all that is it so yeah definitely fresh it'd be nice to
[2042.50 --> 2049.62]  get uh when we can get a little bit more up there so i can at least try this somehow pretty cool yep
[2049.62 --> 2055.12]  you're putting a fire under my butt now so by the time this gets posted you'll see a readme it'll be
[2055.12 --> 2064.26]  like all fleshed out i'll be like ah nice yeah that's a light readme yeah shame shame so how how
[2064.26 --> 2072.12]  have you handled the uh or dealt with or um enjoyed the community contributions um seem like you have a
[2072.12 --> 2077.60]  very active mailing list you have very active repositories um has it been an adjustment period
[2077.60 --> 2084.00]  has it been pretty easy and what are your philosophies around community um it's it it was really really
[2084.00 --> 2091.34]  busy at first um i mean it as far as like github stargazers go it really shot up in popularity and
[2091.34 --> 2097.64]  there's a time where i was receiving a lot of issue requests a lot of pull requests and um the last thing
[2097.64 --> 2102.76]  i wanted to do was just like be lazy about and be like i'll just merge this i'll just merge this
[2102.76 --> 2109.60]  uh because part of martini is about writing clean code and um i really pride myself on that there's many
[2109.60 --> 2114.90]  i got a lot of feedback from people and there's just uh an immediate surprise that like you know
[2114.90 --> 2120.88]  martini it's probably not the case anymore but when within the first couple weeks of release it was
[2120.88 --> 2126.30]  under a thousand lines of code and it did so much and it had the possibility to do so much um through
[2126.30 --> 2132.28]  through extending it and so i wanted to keep the code clean i wanted to keep the code concise and i was
[2132.28 --> 2138.96]  receiving a lot of pull requests so um it was good i mean you don't want to turn people down when
[2138.96 --> 2142.72]  they're when they're writing code and they're passionate about a project and they want to
[2142.72 --> 2151.74]  give the code to the project um so my philosophy behind pull requests is you don't have to accept every
[2151.74 --> 2158.54]  pull request it's okay people will understand but you've got to communicate it i mean you have to
[2158.54 --> 2166.16]  you have to rather than just saying no i'm not going to merge this in it's better to take that
[2166.16 --> 2169.36]  passion that they put together into that code because everybody kind of puts their heart into
[2169.36 --> 2174.28]  code i i believe you really you know you have to do something if you're contributing to open source
[2174.28 --> 2179.82]  you're definitely you're definitely passionate about it in a way um i i want to steer that passion
[2179.82 --> 2185.70]  into something that in some place where it'd be more useful so if martini is not the best fit for this
[2185.70 --> 2190.84]  piece of code or this um api that somebody wrote i want to be like you know what this would be
[2190.84 --> 2194.90]  awesome as a third-party library and you know i'd be happy to link it in the martini read me if it's
[2194.90 --> 2201.54]  great um and so that's kind of been my philosophy with with martini specifically because it needs to be
[2201.54 --> 2208.92]  such a clean lean code base um martini contrib i'm a little looser on uh accepting code especially from
[2208.92 --> 2214.80]  just philosophical reasons like somebody puts up a package that i wouldn't necessarily use but it's
[2214.80 --> 2220.64]  very well structured code and um i will definitely accept it in because it seems useful for other
[2220.64 --> 2228.16]  people and um that's just kind of in the case i'm a little looser i also give martini contrib uh
[2228.16 --> 2233.94]  package owners i do give them ownership of the package by adding them as a collaborator on the repo so
[2233.94 --> 2240.20]  i'm not the only one directly contributing to martini contrib like once somebody puts together a
[2240.20 --> 2246.14]  package let's say binding um i gave those two guys collaborator privileges so they can update that
[2246.14 --> 2251.50]  package without having to put up a pull request all the time that's why you actually have that in
[2251.50 --> 2256.40]  your readme too where you say if you're if you contribute a package yourself you can so well so
[2256.40 --> 2261.32]  you can so you can fix it you say i will automatically add this contributor if you contribute a package
[2261.32 --> 2267.32]  that's a good way to do it i mean it seems like that approach does make sense too as a
[2267.32 --> 2272.26]  as a maintainer because you kind of get to set some of the ground rules and the guidelines which
[2272.26 --> 2277.40]  you know let's let's be honest where jared i know you have kids but you know when you have kids it's
[2277.40 --> 2281.84]  kind of like having kids in this case kind of taking this far on the left but follow me here
[2281.84 --> 2286.52]  is that like if you're doing something like this like this is your baby right so you want this to go a
[2286.52 --> 2293.08]  certain direction and without that discipline and and whatnot i'll just go and act like a bad teenager so
[2293.08 --> 2298.98]  you got to kind of keep them in order and those kind of put down some um you know some fence poles
[2298.98 --> 2303.88]  to say you know don't go beyond these areas and that would work better as a as an external library
[2303.88 --> 2309.00]  or whatever so you're kind of setting some ground rules for how the ecosystem can play out yeah
[2309.00 --> 2317.12]  absolutely um and uh so far it seems like the community's really been great i was telling my wife
[2317.12 --> 2322.42]  this this morning when i was just talking about martini and i'm really excited to see that um
[2322.42 --> 2329.44]  that community has reciprocated in a way i sometimes i look at github repositories and i look at mailing
[2329.44 --> 2336.12]  lists and there's a little bit of hostility and i think part of that um is you know contributors can
[2336.12 --> 2342.88]  tend to look up to um you know the owner of the repository as an overall attitude uh for for the repo
[2342.88 --> 2349.94]  so if people are asking questions um you know it will it's kind of a reflection of the owner um
[2349.94 --> 2354.86]  so when i see things on martini somebody asking questions seeing other community members coming
[2354.86 --> 2362.02]  in and being extremely nice about how to lay out questions for people who are new or or or guiding
[2362.02 --> 2368.26]  them in the right way i like i just i have a lot of hope um for for the actual project because people
[2368.26 --> 2372.82]  are extremely nice not only in answering other people's questions but also you know putting
[2372.82 --> 2378.48]  together an issue i i love when people and this happens so often and where they're like oh i'm
[2378.48 --> 2382.98]  having a bug with this and they describe their bug and then the last sentence is by the way martini is
[2382.98 --> 2390.04]  like so so awesome thank you so much for putting this together and that really as a as a maintainer
[2390.04 --> 2393.42]  that just really brightens up my day and it's cool to see that that's a reflection of
[2393.42 --> 2395.62]  that part of the community as a whole
[2395.62 --> 2404.84]  in the uh i guess i guess we'll call that pre-show we were chatting before the actual show so that's the pre-show
[2404.84 --> 2409.80]  right uh you're kind of talking about some of the things you're doing at kajabi and uh which is your day job
[2409.80 --> 2413.36]  where you kind of like get the hack on stuff and you're doing some things and go there but you've also done
[2413.36 --> 2418.06]  some other things and node and you kind of have this go versus node kind of wild west mentality
[2418.06 --> 2423.32]  can you talk about that a bit yeah and it's honestly i i'm a pragmatist i use a bunch of
[2423.32 --> 2430.00]  different tools so i'm not necessarily tied to either one um i just look at the problem and i find
[2430.00 --> 2437.24]  what the best tool for the job is and the the sentiment around the office here at kajabi is that node is
[2437.24 --> 2445.26]  good enough for most part for the most part uh meaning yeah you can write web apps in it and you can
[2445.26 --> 2449.98]  grow web apps in it and that's perfectly fine it's not it's not like it's a horrible technology
[2449.98 --> 2455.96]  um i would just say it's probably not my preference if i were to write a personal project i probably
[2455.96 --> 2462.64]  wouldn't go to node first um unless there was something i absolutely needed from that community
[2462.64 --> 2470.68]  um and from that ecosystem but it yeah like you mentioned it kind of feels like the wild west out
[2470.68 --> 2476.40]  there um things kind of breaking silently and it seems to be an accepted part of the community and
[2476.40 --> 2485.52]  that's fine i mean people focus on you know certain aspects um of a language and disregard others i know
[2485.52 --> 2490.28]  there's blind spots in every single language community it just it bums me out sometimes when
[2490.28 --> 2497.24]  i'm using some sort of package or or library in javascript and it's just oh i failed and i'm not
[2497.24 --> 2503.88]  going to tell you why something just went wrong um and that seems to be accepted an accepting an
[2503.88 --> 2510.56]  accepted debugging practice is to find out what goes wrong it's just not my my style uh technologies
[2510.56 --> 2516.50]  like go will pretty much tell you straight out like what what's going on there's not a ton of
[2516.50 --> 2524.78]  unknown like what what the heck does this mean kind of errors since we're talking about uh note and go a
[2524.78 --> 2531.76]  little bit um this last show episode 116 we had aaron hammer on he's from walmart labs and he
[2531.76 --> 2539.90]  obviously just had this great success story with node and black friday and um you know you know
[2539.90 --> 2545.24]  hailing banners balloons everywhere confetti all that good stuff it's like you know super wild party
[2545.24 --> 2552.86]  um because no there's some awesome stuff for them and black friday are there any stories um i guess
[2552.86 --> 2559.00]  similar or somewhat the same that happen in the go ecosystem that you know of that you can tell
[2559.00 --> 2566.42]  i mean there's the obvious google one where they uh replace their download server with go which was
[2566.42 --> 2573.70]  basically you know net http's file server um that source is right there in the in the go standard
[2573.70 --> 2579.96]  library so there's that obvious one and um there's a good blog post on it you'll you'll probably be able
[2579.96 --> 2588.14]  to find it and stick it in the show notes um by brad fitzpatrick um covering it and the there's
[2588.14 --> 2594.66]  there's a couple others that i know of um i might have to give you links after the show but uh in
[2594.66 --> 2601.76]  general it's a lot of sas companies um i know iron io uses a lot of a lot of go i know um matt
[2601.76 --> 2606.66]  amenetti at splice they they've converted a lot of their back-end tech to be using go and
[2606.66 --> 2612.32]  very successfully and i think if you even watch sites like hacker news almost daily you find some
[2612.32 --> 2619.70]  sort of go hate and go uh success story yeah kind of paired together that's kind of wild i mean and
[2619.70 --> 2624.28]  i think that's what some of the listeners listen to this podcast for is kind of like get a heartbeat
[2624.28 --> 2628.80]  on which technology is kind of maybe leading the way or going to lead the way and and maybe that's
[2628.80 --> 2633.12]  part of our role here which is to have guests on that can kind of help at least somewhat field
[2633.12 --> 2639.06]  those kinds of questions but it seems like node and go or they're both i mean go is a language and
[2639.06 --> 2644.94]  node is um you know i guess not really a language it's javascript it's sort of a framework on top of
[2644.94 --> 2651.82]  va but um you know they're going both in a good direction and you've obviously don't really have
[2651.82 --> 2656.52]  ties to one or the other you're kind of like whichever tool best fits it but a lot of people
[2656.52 --> 2662.94]  in the node community seems to be seem to be like um very very pro javascript you know like forget
[2662.94 --> 2668.64]  everything else write it in javascript everything is javascript and there's a merit to that um
[2668.64 --> 2673.16]  mainly from i would say from a training perspective some might disagree with me but
[2673.16 --> 2680.34]  i'll tell you this the junior developer at my um you know here at kajabi like we can teach him how
[2680.34 --> 2686.44]  to write a node app and he'll feel productive in it even though he's been only writing you know ruby and
[2686.44 --> 2690.62]  maybe some front-end javascript but he'll feel comfortable in that and i'd say go in the same
[2690.62 --> 2694.76]  respect is very similar to that go is not a difficult language to pick up actually one of
[2694.76 --> 2701.26]  the criticisms of go is that it's too minimal it's too simple um but that's not necessarily a bad thing
[2701.26 --> 2708.56]  in every case and i think it really depends on what what part of the industry you're in um my my side
[2708.56 --> 2714.64]  of the industry we're a very small shop we're very consumer facing um we build real products for real
[2714.64 --> 2722.44]  people and um we we deal like with that's at our forefront every day so if the technology is a
[2722.44 --> 2728.26]  means to an end for us we're not doing a ton of bit twiddling we're not doing extremely high scalability
[2728.26 --> 2735.62]  crazy um computing so for us to write our systems in haskell would be like very counterproductive
[2735.62 --> 2741.46]  um no doubt that like there's a there's an extreme use case for haskell and there's a very good use case
[2741.46 --> 2746.20]  for writing a correct program but i'm not going to sit down and teach a junior developer here at
[2746.20 --> 2753.04]  kajabi haskell um it's just not going to be productive for our use case let's pause the show
[2753.04 --> 2758.32]  for just a second and give a shout out to our sponsor new relic new relic is a software analytics
[2758.32 --> 2764.86]  company that helps make sense of billions of metrics across millions of applications all in real
[2764.86 --> 2770.12]  time one thing developers are really focused on this year is seamless application performance
[2770.12 --> 2777.18]  across multiple platforms on all their devices it sounds simple but making an application work
[2777.18 --> 2782.90]  consistently well on lots of different devices all with different operating systems running different
[2782.90 --> 2789.58]  types of software that's super complex and you might be going through this right now well how complex is
[2789.58 --> 2795.80]  it back in the old days like 2007 it was basically impossible to know how your application would perform
[2795.80 --> 2802.02]  once you shoot the production if you remember those days we'd all spend a ton of time doing internal bug
[2802.02 --> 2806.98]  hunts and eventually just cross our fingers and hope for the best we'd ship our code and we'd sit around
[2806.98 --> 2811.56]  monitoring twitter and whatever other comps traffic we could do to kind of see how well our apps were or
[2811.56 --> 2818.00]  we're not performing and thankfully those days are behind us now new relic lets us track our application
[2818.00 --> 2824.40]  performance down to the end user level all in real time this means that we can spot problems find bugs
[2824.40 --> 2831.48]  and fix our code fast way before our users even notice anything is wrong so go check out new relic by
[2831.48 --> 2837.62]  visiting our special url it's new relic.com slash the change log learn more about what they're doing how
[2837.62 --> 2844.78]  they can help you use our special offer code the change law to take advantage of a special 30-day extended
[2844.78 --> 2852.00]  free pro trial available exclusively to our listeners head to new relic.com slash the change log
[2852.00 --> 2860.14]  so speaking of teaching we would be remiss not to bring up gopher casts yes which appears to be a
[2860.14 --> 2869.58]  fledgling project but very cool this is gopher casts.io and you could imagine it's screencasts for
[2869.58 --> 2875.70]  learning and teaching go can you talk about it yeah so i i started this up with my uh with my longtime
[2875.70 --> 2882.84]  buddy nate beck and it's it's basically you know what it says it is i when i released martini i also
[2882.84 --> 2889.80]  had a accompanying demo video to go along with the source code and that demo video was um way better
[2889.80 --> 2895.10]  received than i thought it would be and a lot of people watched it and a lot of people got interested
[2895.10 --> 2900.50]  in the project because of it and still to this day i i look at github recently released uh statistics for
[2900.50 --> 2904.42]  a repository so i take a look at those i'm like wow there's so many people that are coming from the
[2904.42 --> 2910.26]  video like there's still people watching the video which is it blows my mind and feedback from that
[2910.26 --> 2918.24]  video um was very positive people loved the pacing and uh it was suggested a lot to me and asked a lot
[2918.24 --> 2923.68]  of me if i would start creating screencasts just to teach about go in general and about the technologies
[2923.68 --> 2930.40]  and the projects that are out there um so that's why we started uh that's why we started gopher casts and
[2930.40 --> 2938.38]  i have a background in audio nate has a background in audio and video and uh so we have very very
[2938.38 --> 2944.46]  particular needs when it comes to producing screencasts like this so if you go to gophercasts.io
[2944.46 --> 2950.18]  you'll see very high production quality um they're very uh very well-paced videos in my opinion
[2950.18 --> 2957.70]  they um they're very digestible they're all three to five minutes long um and like it was mentioned
[2957.70 --> 2963.86]  it's they're very very the site is very young so you'll probably only see a few videos up there
[2963.86 --> 2970.52]  but we plan on releasing uh at least weekly episodes and i guess since we're talking about uh
[2970.52 --> 2978.80]  the site itself is it written in martini no the site is not written in martini and let me tell you
[2978.80 --> 2985.08]  why uh at first i wanted to write it in go and my my buddy nate he is not a go programmer he's picking
[2985.08 --> 2990.84]  up go and he's learning go and he's um you know he's asking me all these questions and we're we're
[2990.84 --> 2997.62]  kind of you know trudging through it together um we actually ended up writing the service in rails
[2997.62 --> 3003.84]  and there's a couple reasons why one of them uh one of the reasons why was kind of prompted by
[3003.84 --> 3010.00]  joel hooks who wrote a blog post on how he converted egghead io which is an angular js
[3010.00 --> 3017.36]  screencast uh put on by john lindquist and joel hooks now um he mentioned why he wrote his site
[3017.36 --> 3021.66]  in rails and why he didn't use something like node.js and angular or something like that
[3021.66 --> 3028.22]  and you know it goes goes back to a lot of my philosophy with building things is you use the
[3028.22 --> 3034.60]  best tool for the job um i'm going to be transparent and say like go for cast will not always be you know
[3034.60 --> 3042.14]  all free everything free we do plan on feeling out the community seeing you know what it brings
[3042.14 --> 3047.10]  what people like what people don't like and we want to offer you know something that will keep us going
[3047.10 --> 3052.48]  to keep us producing super high quality screencasts and to see what people are willing to pay for it
[3052.48 --> 3057.02]  because i think people are willing to pay for quality content so building things like a like a
[3057.02 --> 3064.88]  publishing pipeline for video and you know tying in with like subscription services like stripe and
[3064.88 --> 3071.42]  dealing with payments we already know how to do that in in rails and for us to do it and go is possible
[3071.42 --> 3079.18]  but it's not the most productive at the time martini was built you know to make tiny services and and
[3079.18 --> 3086.20]  smaller websites and in a more distributed computing fashion and so um that was the reason that we
[3086.20 --> 3091.02]  mainly chose to write it in rails and it's it's been fine we've had a couple people that are like oh it's
[3091.02 --> 3096.80]  written in rails and not go but overall i mean it's useful for people well i think what you said earlier
[3096.80 --> 3103.40]  with um uh with with martini when you first started it out like your point wasn't to make a rails web
[3103.40 --> 3108.32]  framework it was meant to be like a web services web framework you know to to kind of interact between
[3108.32 --> 3113.98]  different services so in that case you know you're totally you're on point yeah absolutely it's using the
[3113.98 --> 3118.82]  best tool for the job we don't have to we don't have to just like one technology i like a lot of
[3118.82 --> 3123.66]  technologies you know there's a lot of things that bother me about rails but i still use it every day
[3123.66 --> 3129.68]  and you know what it's really productive yeah i know jared and i have been talking about some
[3129.68 --> 3134.98]  different stuff you want to do with the change log and uh he he always i'm gonna call you on this
[3134.98 --> 3141.78]  jared he's like i'll do if you let me write it and go and so i don't know if that's the the inner
[3141.78 --> 3146.32]  desire of jared who just wants to write it and go or what or if he's just uh if he thinks that's
[3146.32 --> 3151.06]  the best tool for the job but we'll see yeah i'm the same way i want to just write stuff and go and
[3151.06 --> 3155.82]  nate had to calm me down and be like let's pull this back and kind of in retrospect for the site i'm
[3155.82 --> 3160.90]  glad we have it in rails will it maybe be in go eventually probably he'll probably be in go
[3160.90 --> 3166.84]  eventually but right now we are able to ship and show people our screencasts and most importantly
[3166.84 --> 3171.80]  we're able to show people content and that's really what it's about yeah just to defend myself
[3171.80 --> 3178.84]  slightly here sorry about throwing you the bus there sorry about that the reason why i want to
[3178.84 --> 3184.96]  do that is not some sort of idealism it's because i was saying that let's learn something as we build
[3184.96 --> 3190.24]  this you know it's kind of a side thing and let's let's learn go and these different things as we build
[3190.24 --> 3193.72]  it and then adam's saying this thing's going to be a production you know like this is going to be our
[3193.72 --> 3200.66]  next version we can't we can't put you know newbie code out there so yeah ultimately he's going to
[3200.66 --> 3205.74]  win that that argument but that was some of my thinking behind doing and go i was mostly just
[3205.74 --> 3210.38]  looking for new projects to start and go and i was like oh sure let's do it and go well hey some
[3210.38 --> 3215.32]  things are best learned in production right it's true i don't always test my code but when i do
[3215.32 --> 3222.48]  i test it in production that's cool um what else do you want to talk about jared i know we talked
[3222.48 --> 3226.74]  about gopher cast was one i'm super excited about that by the way i'm really glad that you listened
[3226.74 --> 3231.18]  to the community and and decided to do that because i do think that martini video was well done
[3231.18 --> 3240.58]  and and and to your credit i definitely think you have a nice smooth pace for those videos and keeping
[3240.58 --> 3246.42]  them under five minutes um is definitely perfect i mean sure seven minutes eight minutes that's okay but
[3246.42 --> 3253.60]  five minutes is like a quick idea enough to get them running whomever's listening and it's just like
[3253.60 --> 3259.56]  in and out like let me take a break from whatever i'm doing and and just maybe listen to something
[3259.56 --> 3266.46]  brand new you know go from maybe design to to listen to a gopher cast and kind of get some some new
[3266.46 --> 3271.48]  knowledge yeah ideally what you want to do is you want to you want to trigger that spark in somebody's
[3271.48 --> 3277.14]  mind to start creating instead of just copying and pasting the source or or figuring out some
[3277.14 --> 3281.32]  sort of quick fix they're watching the video so they can get inspired and that's kind of what it
[3281.32 --> 3289.08]  comes down to uh well let's loop back around yeah i got one more question about martini and then maybe
[3289.08 --> 3295.28]  adam can do his his closing questions but um you kind of got started and go because you like
[3295.28 --> 3303.18]  the deployment of these distributed command line applications um how do you deploy a martini
[3303.18 --> 3309.38]  application a web app to the to production um it's in a similar fashion and there's a couple different
[3309.38 --> 3315.86]  ways you can deploy it i know heroku if if anybody's used to working with heroku um it's a very easy
[3315.86 --> 3322.12]  deploy process for martini um it's the same as any other go web app um what one really cool thing about
[3322.12 --> 3329.20]  martini is um and this was a point for contention among a couple people but martini uses uh to
[3329.20 --> 3333.78]  configure the port you have to configure the port environment variable you actually don't do it inside
[3333.78 --> 3340.64]  the app and the reason for that is for deployment purposes in a lot of environments um especially
[3340.64 --> 3347.00]  around kind of shared hosting or or or neighbor hosting you have the port set you know in the
[3347.00 --> 3353.56]  environment automatically by the service provider so deploying a martini app um using the go build
[3353.56 --> 3358.76]  pack and heroku is brain dead simple you don't do anything different you just push up your code with
[3358.76 --> 3366.60]  the go but build pack uh via git and it just works um how about non-heroku style so so non-heroku style
[3366.60 --> 3371.66]  would be uh simply compiling your app for the platform that you're in or pushing your code to the
[3371.66 --> 3377.32]  the box that um the box that is going to be hosted on and compiling it there and just making sure that
[3377.32 --> 3383.52]  any sort of asset folders you have um are are existing you know right next to where the binary
[3383.52 --> 3390.52]  is run at or uh there there's another project called go bin data which actually can compile your assets
[3390.52 --> 3396.90]  in as go source code so it's all one fat binary and there's a couple projects that actually do that
[3396.90 --> 3400.90]  yeah yeah one of which is and i don't know if you guys use this tool but i'm going to totally
[3400.90 --> 3406.50]  uh pimp it out because it's it's an awesome tool is ngrok is a tunneling service and tool
[3406.50 --> 3411.60]  um built in go i think i think we covered that we linked to that on the changelog a while back
[3411.60 --> 3416.44]  oh okay i've seen it but i haven't used it personally well it's a fantastic tool and it has
[3416.44 --> 3421.54]  its own web interface that uses like bootstrap and pulls in all this javascript and stuff but the the
[3421.54 --> 3426.54]  rad thing is all that stuff is hosted you know locally but it's all in one single binary it's still
[3426.54 --> 3432.66]  one binary for all the assets um so that's another cool way depending on what kind of asset you're
[3432.66 --> 3437.24]  serving and if you want to just pull them off of you know memory or pull it all into memory when you
[3437.24 --> 3441.88]  run the program like it depends on what you're really doing but there's kind of something really
[3441.88 --> 3447.48]  uh there's there's a lot of excitement around thinking oh i could just drag and drop this one
[3447.48 --> 3454.00]  file onto a computer and it's deployed yeah for sure and then would you suggest behind behind a proxy
[3454.00 --> 3460.02]  like nginx or hypoxy or would you just throw it on port 80 and let the thing roll you could you
[3460.02 --> 3463.38]  could certainly throw it on port 80 and let it roll and there's some services that i've deployed
[3463.38 --> 3470.46]  that have that um but nginx is such a huge boon to any sort of um to really any sort of web app that
[3470.46 --> 3476.00]  um for things like caching and even static file serving i would recommend probably in production using
[3476.00 --> 3483.72]  nginx over martini's you know static handler just because of efficiency um the knowledge that's out
[3483.72 --> 3491.14]  there the documentation that's out there yeah um and speed so so future of martini uh big plans
[3491.14 --> 3499.00]  little plans what are you thinking um probably little plans uh again i want to keep martini
[3499.00 --> 3505.70]  consistent and small there's not a whole lot left to add to it but there's certainly a lot of value
[3505.70 --> 3510.34]  that can be built up over in packages and handlers and middlewares especially in the martini
[3510.34 --> 3515.16]  contrib repository there will be a point where martini contrib will hit critical mass but i'm
[3515.16 --> 3520.98]  hoping by that time martini will be popular enough to where it's valuable for somebody to publish a
[3520.98 --> 3525.86]  separate package on github that people will then recognize oh it's for martini and they can actually
[3525.86 --> 3530.78]  pull it in and use it it hasn't reached that point yet because the go community is still fairly small
[3530.78 --> 3536.30]  and so martini contrib kind of acts as that curation a one place where everybody can go to see like
[3536.30 --> 3543.88]  what are the latest cool packages to use um but in general uh you know i'm excited to see what 2014
[3543.88 --> 3551.44]  brings in in terms of go and their their versioning story because that has come up a couple times with
[3551.44 --> 3560.18]  martini i have some solutions of my own that i'm kind of working on in secret um but um i'm hoping
[3560.18 --> 3568.56]  i'm hoping i can bring martini to a version 1.0 where i uh where obviously the api won't have any
[3568.56 --> 3575.38]  um breaking changes and i try my best not to break any most changes but there are there is one change
[3575.38 --> 3583.06]  in particular which will break a you know one little thing that nobody really uses um and once i bring it
[3583.06 --> 3588.18]  to 1.0 it's it's not going to break from there so i'll probably apply uh the semantic versioning principle
[3588.18 --> 3596.42]  to that and be able to um to develop the code from there cool chair with your with your uh question
[3596.42 --> 3602.94]  i guess on the future of of martini do you think you meant from a contrasting difference between say
[3602.94 --> 3608.50]  a framework like rails is that what you meant by that because i was kind of curious if
[3608.50 --> 3614.28]  you know martini's expectation is to be something like rails ever in the future to be that kind of
[3614.28 --> 3620.58]  web development framework i was mostly just trying to get a just a general idea of where he was going
[3620.58 --> 3625.98]  to take it next but i think probably and jeremy correct me if i'm wrong i think the answer to that
[3625.98 --> 3634.08]  is probably not gonna is no yes okay i'm sorry i mean yes no is the answer i think i said that sentence
[3634.08 --> 3641.04]  oddly but yeah that's that's okay um yeah i mean i think there's there is i mean there's uh revel
[3641.04 --> 3648.78]  um which is you know kind of in the spirit of of a framework like rails where it it it its goal is
[3648.78 --> 3654.96]  to be very productive and it does a lot of things for you and that's not um the space that martini is
[3654.96 --> 3663.40]  trying to um occupy at all which is good because part you know the way i structured martini i was kind
[3663.40 --> 3667.78]  of being lazy about it i was like i don't want to like spend a million hours like maintaining this
[3667.78 --> 3673.92]  and i don't want to have like a million like to do's um on this project and so and that's been
[3673.92 --> 3678.72]  that's been somewhat successful i haven't had to contribute a whole lot of code to martini you know
[3678.72 --> 3683.20]  relatively a whole lot of code so what's the what's the end users say then whenever they think okay
[3683.20 --> 3687.76]  revel or martini how do they make their choice what are some of the things they should ask themselves
[3687.76 --> 3695.36]  um really what kind of app are you building and um you know what what you want your what you want
[3695.36 --> 3701.86]  your maintenance to to look like because uh building something off of a minimal framework
[3701.86 --> 3707.52]  and then a full featured framework have uh they both have uh different maintenance stories i'm not
[3707.52 --> 3711.54]  saying one is worse than the other in particular i'm just saying they there's different ways to
[3711.54 --> 3717.42]  maintain it you know rails like something like rails i feel like we build layer on top of layer on top of
[3717.42 --> 3722.26]  layer on top of layer and with a minimal code base um maintenance looks a little different it's a
[3722.26 --> 3730.86]  little easier to rip stuff out and to rethink the problem if um if requirements change um and you know
[3730.86 --> 3736.74]  you you kind of mentioned it earlier and you hit the nail on the head earlier martini was built out to
[3736.74 --> 3742.44]  solve some of the problems in distributed web applications where you have multiple services that
[3742.44 --> 3747.32]  um you know do one thing really really well and you have those intercommunicate between each
[3747.32 --> 3754.06]  other and the industry is trending trending to that as a whole and so that's that's the space in the
[3754.06 --> 3758.64]  little niche that i think martini will really fill is building these small applications that
[3758.64 --> 3765.84]  you know the code can be really small and concise and reusable across you know different applications
[3765.84 --> 3773.42]  gotcha cool jared anything else for uh for your your uh your questions
[3773.42 --> 3782.02]  inquiring minds no uh yeah you know if andrew here which he's uh which he's not at this at this
[3782.02 --> 3789.12]  moment uh i don't think so andrew you here no he's not here um he would ask uh he would say we have
[3789.12 --> 3794.30]  three questions we typically ask at the end of the show uh and this is one of my favorite questions
[3794.30 --> 3798.58]  we get to ask which is who is your programming hero it could have been somebody that was just
[3798.58 --> 3802.40]  influential in your life it could have been you know a mentor it could have been a teacher it could have
[3802.40 --> 3809.04]  been you know it could have been your dad whomever but who is the programming hero for you oh man that's
[3809.04 --> 3819.60]  going to be a hard one um uh i would have to say uh at the moment and this is going to sound super
[3819.60 --> 3828.50]  cheesy because i'm on a podcast talking about go but uh a lot of those unix guys like like rob pike
[3828.50 --> 3837.52]  and rob kernigan like they they're pretty awesome i i i'm a self-admitted you know unix lover i love
[3837.52 --> 3842.56]  just the way the philosophies around it and how it's structured and there's obviously flaws around it
[3842.56 --> 3849.50]  but um in general it's very in line with how i like to build applications so um a lot of minimalism
[3849.50 --> 3857.02]  a lot of uh you know build build apps that do one thing really well um you know i fall in line with
[3857.02 --> 3862.56]  that philosophy so those old school guys that have uh done a lot to influence you know modern computing
[3862.56 --> 3871.42]  as a whole um i love it so if you were if you were not coding go or i guess goes on a language i guess
[3871.42 --> 3876.16]  sorry goes language i was taking martini my bad if you weren't coding and go what would you be coding
[3876.16 --> 3880.72]  and i guess you kind of do that by day you don't always just code and go so yeah what else do you
[3880.72 --> 3891.08]  hack in uh so i mean uh ruby um kind of whatever language is possible i do some c and c plus plus
[3891.08 --> 3897.56]  some ruby some um every once in a while i'll dive in and do some objective c with iphone apps javascript
[3897.56 --> 3905.96]  um you know more go stuff touch some c sharp on on multiple projects um so i'm kind of
[3905.96 --> 3911.28]  willing to dive in and uh i kind of have a pretty open mind i think if a community is somewhat
[3911.28 --> 3917.92]  successful that there's got to be some uh there's got to be some hope in and and some some little
[3917.92 --> 3923.42]  golden nuggets in in how they operate um so i think every every community has at least something
[3923.42 --> 3930.62]  to say as far as how software should be developed and so i'm i'm adventurous in that way where i like to
[3930.62 --> 3939.06]  uh find out what those answers are let's uh try a different angle at that what's um what's on your
[3939.06 --> 3943.68]  radar what's what's some fun open source projects that we haven't quite talked about on the show
[3943.68 --> 3947.86]  maybe something you haven't even uh written yourself but what's out there that's interesting
[3947.86 --> 3952.84]  that you want to hack on whenever you have a free weekend or something you have you know you got
[3952.84 --> 3958.64]  four days you got nothing to do what would you hack on um probably i would take a deep look into
[3958.64 --> 3964.24]  uh what the ecosystem looks like for functional languages right now um and and start to find
[3964.24 --> 3971.74]  some real use cases for me um obviously like as a programmer we're hearing that we're running into
[3971.74 --> 3977.54]  this paradigm shift where we need to do more parallel computing and and you know having side effects is
[3977.54 --> 3983.10]  just a hindrance to that and so functional languages are going to become more popular um but i don't think
[3983.10 --> 3989.84]  it's hit that um mass yet to where imperative programmers or people like me who have you know
[3989.84 --> 3998.72]  grown up as a developer that's you know programming imperative the whole time um we we haven't found
[3998.72 --> 4006.16]  the like practical use cases for for functional languages everything i i try to see with like a
[4006.16 --> 4010.20]  haskell implementation just seems so academic and i was like okay well so like how can i write something
[4010.20 --> 4016.72]  for kajabi like this so i i i'll probably i probably have that on my radar if i yeah if i were to go to
[4016.72 --> 4023.02]  a cabin for four days i'd probably look at haskell and be like i need to i need to find a way to make
[4023.02 --> 4028.04]  this useful for me um what do you think what do you think would write maybe if you because i mean you
[4028.04 --> 4032.74]  would have no internet right i would have no internet so i'd probably have to write some command line
[4032.74 --> 4039.54]  apps um and do some crazy craziness but i don't know if i'd exactly be able to tell you what i'd write
[4039.54 --> 4044.80]  cool well why don't you take that trip someday and get back to us that's right i might suggest if
[4044.80 --> 4051.22]  you're in a cabin without any internet and you're like on vacation maybe have a beer sit out enjoy the
[4051.22 --> 4057.68]  outside let's put come on guys we can put the computer down for a few days oh yeah totally and
[4057.68 --> 4062.56]  then we get back because i'm getting lots of whiskey and a cigar i mean that sounds yeah you're not way
[4062.56 --> 4067.52]  better than programming haskell you're not gonna learn let's get real here without the internet come on
[4067.52 --> 4072.70]  yeah that's what i was gonna say um that's cool man yeah jeremy it's been fun having you on the
[4072.70 --> 4078.68]  show i know that uh you kind of get to bounce around quite a bit in your uh in your working
[4078.68 --> 4083.30]  with the web and and programming and obviously you've done some pretty cool stuff to share on
[4083.30 --> 4088.68]  github and we appreciate you know your perspective with martini and how you want to keep it clean and
[4088.68 --> 4093.02]  how you're kind of guiding that ecosystem and just coming on the show and and sharing that and
[4093.02 --> 4097.56]  maybe even giving a little twist of the arm via twitter to to get onto the show but you were
[4097.56 --> 4103.74]  definitely on our list sir that's for sure oh awesome well i'm so glad to be on the on the podcast
[4103.74 --> 4109.24]  again uh newer fan but but a big fan and i'm just it's it's awesome talking to you guys i love talking
[4109.24 --> 4113.90]  shop it's been good having you back on the show too jared i know i haven't had you back on with me
[4113.90 --> 4119.94]  since uh since katrina's show really right so it's been a bit yeah it's been a while good to be back
[4119.94 --> 4124.30]  i'll have to get you back on the show more often man right on we'll have to make that our mission
[4124.30 --> 4131.34]  but um i also want to give a another shout out to our sponsors digital ocean whom we love new relic
[4131.34 --> 4137.42]  whom we love and top tile whom we love which uh those are our sponsors for this show but our friends
[4137.42 --> 4143.76]  at digital ocean want to pay you so if you write open source like we've talked about today if you got
[4143.76 --> 4148.38]  a project out there they want to pay you to write a tutorial about your project for the digital ocean
[4148.38 --> 4153.18]  community best of all they'll give you 50 bucks and then promote it for you on their twitter account
[4153.18 --> 4158.30]  so if you've written martini maybe you can write a uh tutorial and they'll promote it to their 21 000
[4158.30 --> 4162.66]  followers uh for those of you listening i'll put this in the show notes but the url for that is
[4162.66 --> 4171.00]  digitalocean.com slash write hyphen four hyphen digital ocean the word four is the word f-o-r-4 not the
[4171.00 --> 4175.88]  number four so just so you get that clear and you can also get some free stickers from digital ocean by
[4175.88 --> 4182.16]  filling out the form at stickers.digitalocean.com and if you want to uh if you want to freelance
[4182.16 --> 4187.90]  with companies like airbnb rco or audio head to top.com slash developer and click join the best
[4187.90 --> 4195.58]  to see if you have what it takes to join top tiles elite elite capital e network of engineers again
[4195.58 --> 4200.80]  that url is top tile.com slash developer and that's it for this week jeremy thanks again for coming on
[4200.80 --> 4205.50]  the show it's uh definitely great having you on the show and the listeners we thank you for listening
[4205.50 --> 4210.02]  and for your support and if you haven't yet uh we do have an email we ship out every saturday
[4210.02 --> 4214.86]  it's called the changelog weekly um and we we share everything everything that hits articles for
[4214.86 --> 4220.10]  i know martini made an appearance at one point and i think even the blog post that jerry was
[4220.10 --> 4225.32]  alluding to earlier on jeremy we had that in weekly as well but you can subscribe at
[4225.32 --> 4232.64]  thechangehold.com slash weekly we'll be back next week and until then let's say goodbye see ya see ya
[4232.64 --> 4234.62]  you
[4255.32 --> 4264.62]  you
[4264.62 --> 4266.62]  you
[4266.62 --> 4268.62]  you
[4268.62 --> 4272.62]  you
[4272.62 --> 4274.62]  you
[4274.62 --> 4276.62]  you
