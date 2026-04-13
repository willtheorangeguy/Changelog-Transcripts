[0.00 --> 16.74]  let's do it it's go time welcome to go time your source for wide-ranging discussions from all
[16.74 --> 23.40]  around the go community check us out on the web at go time.fm there you'll find lists of
[23.40 --> 28.86]  recommended and popular episodes unpopular opinion clips and a request form so you can
[28.86 --> 35.28]  let us know what you want to hear about on the pod big thanks to our partners at fly.io over 3 million
[35.28 --> 42.82]  apps have launched on fly deploy yours in five minutes learn how at fly.io okay here we go
[42.82 --> 54.50]  what's up friends this episode is brought to you by pork bun.com they offer domain extensions tech
[54.50 --> 62.12]  professionals need like .app .dev and .foo if you need to showcase your next project there is a .app for
[62.12 --> 68.24]  that if you're building the latest sas product that will change the world you can grab a .dev and show
[68.24 --> 73.16]  it off to the world and you can show off your kung.fu programming powers if you're doing other
[73.16 --> 80.12]  cool stuff you can also use the .app .fu or .dev domain to showcase your digital portfolio and show
[80.12 --> 84.04]  off your work they all come with heightened security that benefits you and your visitors they're designed
[84.04 --> 91.36]  to be secure .app and .dev domains are hsts preloaded and that means all .app and .dev websites
[91.36 --> 98.82]  will only load over an encrypted ssl connection this is of course the gold standard of website security
[98.82 --> 104.80]  they all require an encrypted connection to load fortunately a free let's encrypt ssl certificate
[104.80 --> 109.18]  is included with every pork bun domain name registration and you get the best pricing to
[109.18 --> 116.20]  only one dollar for the first year for .app .dev or .fu domain names who is privacy ssl certificates web
[116.20 --> 121.96]  and email hosting trials they're all free why pay for things that should be free and they have a simple
[121.96 --> 127.72]  management user interface manage everything about your new domain name from one place no hunting around
[127.72 --> 134.60]  for that feature you need and they're backed by five star support 365 days a year they have more
[134.60 --> 141.98]  authentic five star reviews from real actual customers than any other registrar so next time you need a
[141.98 --> 149.98]  domain name get a .app a .dev or a .fu domain name at pork bun for only one dollar for the first year
[149.98 --> 157.56]  go to pork bun.com slash go time 24 again pork bun.com slash go time 24
[157.56 --> 183.06]  hello and welcome to go time on this go time episode we're going to be focusing on the art of
[183.06 --> 188.70]  delivering concise interesting and captivating lightning talks this is a popular format across
[188.70 --> 194.94]  a load of different conferences worldwide we had it most recently at gopher con where they did seven
[194.94 --> 203.28]  minute talks to share their interesting innovative and difficult problems that they have been solving and
[203.28 --> 208.26]  thinking about i'm joined by some of those wonderful gopher con lightning talk speakers today
[208.26 --> 213.46]  and they're going to be talking to us about the experience of giving a lightning talk some of the
[213.46 --> 219.58]  challenges some kind of tips and tricks on how to effectively communicate an idea in such a limited
[219.58 --> 225.74]  amount of time and then we're going to be putting their skills to the test and a couple of them are going
[225.74 --> 233.02]  to be doing lightning talks as elevator talks lightning talks in 60 seconds so i think this is going to be a
[233.02 --> 241.28]  really really fun episode so first of all we have jacob who started his tech career at sun microsystems
[241.28 --> 248.42]  where he learned the network is the computer and then after discovering go in 2015 he's been feverishly
[248.42 --> 256.44]  or deviously as he put it modernizing legacy systems to go and then in 2020 he became an assistant
[256.44 --> 261.68]  professor at the university of north texas where he's been converting students to go ever since
[261.68 --> 268.54]  very happy to hear that how are you jacob i'm doing great really really happy to have you on next up we have
[268.54 --> 275.76]  eden who is a software developer who spent most of his career tinkering with instrumentation and trying to find
[275.76 --> 282.66]  ways for one piece of software to worm its way into another um he's been using go for fun since 2016
[282.66 --> 289.16]  and then he managed to convince his employer to pay him to use it in 2019 well done to you how are you today
[289.16 --> 294.72]  i'm okay thanks for having me thank you for being here and i see you have a little extra co-host with
[294.72 --> 300.14]  us today yeah this is banjo and i'll try to keep myself mostly muted so you don't hear him too much
[300.14 --> 305.02]  but that's he's almost always going to chime in when i have something to say too so and for those of
[305.02 --> 311.90]  you listening banjo is not a cat a dog or a different exotic pet it is in fact a lovely beautiful birdie
[311.90 --> 319.74]  so we're very excited to have an additional guest with us today next up we have dylan so dylan's been
[319.74 --> 326.34]  a professional software engineer since 1998 working on banking healthcare finance and now computer
[326.34 --> 332.70]  security industries he's been writing go full-time since kind of early 2016 he's been at crowd strike
[332.70 --> 337.92]  since 2019 and he's also an active participant in the go for slack organization for those of you
[337.92 --> 343.66]  listening that is a slack organization that you can join if you google it or if you reach out to one
[343.66 --> 349.64]  of us i'm sure we can add you and he's a four-time go for con speaker i feel like i should give you a
[349.64 --> 355.80]  medal of some kind um how are you today dylan i'm good how are you yeah one of those was recorded
[355.80 --> 362.72]  virtual in 2020 but uh yeah i've been on stage three times oh my gosh well a talk is a talk and
[362.72 --> 370.10]  we're gonna have to pick your brains today after all that experience right next up we have cassie
[370.10 --> 376.98]  who is a software engineer at diagrid and is actively contributing to dapper she focuses on
[376.98 --> 382.80]  back-end development to simplify the creation of resilient event-driven and micro service-based apps
[382.80 --> 388.72]  and she's part of a gopher family so for those of you who have listened to the podcast before we have
[388.72 --> 394.98]  had her twin sister sam on a couple of times and then her brother also writes go so a very excited
[394.98 --> 400.54]  to have you on today cassie how you doing hi angelica thank you so much for having me super
[400.54 --> 407.64]  super excited and having a great friday yes happy friday for those of you listening at a later date
[407.64 --> 412.60]  what all of these wonderful guests have agreed to spend their friday afternoon with me so i feel very
[412.60 --> 418.94]  lucky then we have matt dale uh who's a software engineer living in pacific northwest with 10 years
[418.94 --> 427.42]  of experience um he discovered go in 2015 he loves writing software contributing to and blogging about
[427.42 --> 434.14]  software engineering specifically go and in his free time and professionally he also does little side
[434.14 --> 439.98]  projects in go and he's currently at mongo db hey matt how you doing hey angelica i'm doing good
[439.98 --> 445.72]  just moved into a new house my head is spinning with all the stuff to do and you can't see it on
[445.72 --> 451.60]  the stream but uh the whole place is full of boxes oh my gosh but priorities for those of you listening
[451.60 --> 457.52]  matt did have time to get out his gophers and place them on the shelf so that is the most important
[457.52 --> 462.68]  thing to unbox when moving into a new house is your gopher plushies i can't actually take credit for
[462.68 --> 466.28]  that that was my wife she was like you have to put these in the background i was like thank you for
[466.28 --> 473.50]  watching out for me i love that and then last but certainly not least we have andy joseph who is
[473.50 --> 479.62]  has architected and developed several industrial control platforms that propel the growth of a
[479.62 --> 486.42]  start-up company into a highly respected world leader in motion control and sensing systems for
[486.42 --> 494.04]  manufacturing as a prolific inventor he's been awarded various patents in software industrial motion
[494.04 --> 499.90]  actuators and sensing systems i'm gonna have to ask you about some of those words most recently
[499.90 --> 506.54]  andy led the development of an iot product that connects industrial equipment to plant-wide data
[506.54 --> 513.80]  analytics and historian applications using services written in go right i know we're here today to talk
[513.80 --> 519.26]  about lightning talks but andy can you say a little bit more about what what that is and what that entails
[519.26 --> 526.84]  it sounds extremely interesting it is it keeps us very busy um you know we we provide machines to
[526.84 --> 531.80]  manufacturing so you think of like automotive you're assembling cars and engines and that sort
[531.80 --> 537.94]  of thing and a lot of our machines show up in plants and we you know we've about five years ago five years
[537.94 --> 543.76]  ago we had a big initiative to create this iot product that would connect our machines to our customers
[543.76 --> 551.04]  data analytics and so it was a prime application to use go and to be able to connect the edge up to the
[551.04 --> 556.42]  cloud so we had a lot of fun doing it and we're continuing to do even more of that kind of development
[556.42 --> 561.64]  so really really interesting i'm sensing a follow-up episode where i'll i want to dive in with you a
[561.64 --> 567.44]  little deeper um awesome well really excited to have you all we're going to start with the very basics
[567.44 --> 573.12]  you know what is a lightning talk for those listeners who might not have attended a conference
[573.12 --> 578.54]  which had lightning talks before or have heard the words lightning talk but are kind of unsure what
[578.54 --> 584.74]  that actually means i wanted to ask maybe cassie like what is a lightning talk a lightning talk for
[584.74 --> 591.22]  gopher con is a seven minute presentation i think of it as a short and sweet presentation
[591.22 --> 597.24]  it's kind of like a single idea or concept and it's pretty fast paced because if you have quite a
[597.24 --> 602.40]  bit of content you only get the seven minutes then they cut you off for sure and because you have such
[602.40 --> 610.74]  a short amount of time how do you decide like what idea to bring what idea is interesting enough
[610.74 --> 616.64]  to captivate your audience while also being able to kind of fit into seven minutes of time
[616.64 --> 622.32]  i don't know what jacob i mean for me it's i already had something prepared that i just cut down
[622.32 --> 628.52]  but i think the lightning talks are are really interesting because you have to focus on a single
[628.52 --> 635.06]  thing and for a single problem it's easy to add remove background until you get the timing right
[635.06 --> 641.02]  and you just give enough context to get people on board and then you hit them with a conclusion and
[641.02 --> 645.98]  it's seven minutes and you're done so for me that's that's pretty much what it was now as a
[645.98 --> 651.82]  consumer of lightning talks i i actually like them a lot i mean i pick and choose the major talks
[651.82 --> 657.18]  but i'll stay through all the lightning talks because not only is it a break from like the
[657.18 --> 663.80]  full sessions but there's always more like esoteric stuff that's going on in the lightning talks i feel
[663.80 --> 668.16]  that you know doesn't want a full presentation but it's always like neat and different kind of things
[668.16 --> 676.20]  yeah mine was a rant that i do at work already all the time and i said i can do seven minutes on that
[676.20 --> 682.78]  i think it's an extremely creative uh endeavor and i i've always thought of thought of creativity as the
[682.78 --> 689.18]  art of taking stuff away right and saying no to certain things and you know the first draft i did
[689.18 --> 695.68]  was easily a 30 minute talk and so i just kept refining it and taking away stuff and getting it down to
[695.68 --> 700.40]  the bare essentials and i ended up with seven minutes and it was quite an interesting process
[700.40 --> 705.88]  so in terms of process i mean matt maybe you're gonna dive a little bit more into this but i'd love
[705.88 --> 712.42]  to hear from you specifically what was the process did you start with just like writing down random
[712.42 --> 719.88]  ideas did you start with a full talk and then have to cut it down further interested in kind of your
[719.88 --> 724.88]  experience and well i was fortunate to have written a couple of blog posts about this already
[724.88 --> 729.40]  so i was like you know i think that this could be an interesting topic for a lightning talk because
[729.40 --> 735.86]  it's uh i think of lightning talks as sort of like adult uh show and tell which is like you just want
[735.86 --> 741.56]  to tease your audience with this concept and then leave them asking questions and that was sort of the
[741.56 --> 747.24]  original motivation for this blog series that i've been writing on in this case the go playground so
[747.24 --> 752.50]  that was it was really obvious i was like boy i really think that this would uh would go well as a lightning
[752.50 --> 760.14]  talk also so in terms of working out like how how it went kind of what you said matt how did they go i
[760.14 --> 764.34]  would love to hear a little bit about kind of one i would love if we could go around and say like what
[764.34 --> 770.16]  even was your lightning talk and then also a little bit about like how did you feel it went and and i'm
[770.16 --> 775.02]  gonna encourage you to be brutally honest with yourself if you left being like oh i wish i had needed
[775.02 --> 782.04]  more time or oh i wish i'd led with xyz i'd really love for us to have that conversation because i think
[782.04 --> 790.10]  one nerves are a factor uh but two i feel like if any of you are anything like me i feel like i i leave
[790.10 --> 796.34]  lightning talks or any talk i give or any meeting that i need to leave with a lot of like oh could have
[796.34 --> 802.30]  done that better well oh i wish i had done xyz ed edan what do you think uh i i actually have no
[802.30 --> 806.84]  recollection of how my my talk went i think i remember bits and pieces but it's mostly a bit
[806.84 --> 810.96]  of a blur and i think that's pretty normal of talks but especially when it's so short that you know when
[810.96 --> 816.02]  you kind of black out for the first few minutes that's the whole talk so uh yeah my talk was on
[816.02 --> 821.76]  how the coverage tool that's built into go works and it was supposed to be sort of educational and
[821.76 --> 826.52]  teach people something that they didn't know a lot about and so i had at least some basic set of
[826.52 --> 831.80]  material to get out within that amount of time and say i definitely set myself up for failure with
[831.80 --> 836.80]  that one but i think i think it went okay i think i i got feedback from people that they learned a bit
[836.80 --> 842.84]  that they didn't know before it's about as good much as i can ask for i i have the same verbiage
[842.84 --> 849.84]  as you i have no recollection uh i remember being on stage and seeing lights and then i remember not
[849.84 --> 856.56]  being buzzed so six minutes 59 seconds i think is what i did but once once they're posted i'm gonna go
[856.56 --> 861.74]  back and watch because i i can't remember i do also remember the timer like what it said when i
[861.74 --> 867.22]  when i finished so that is something that sticks out i think it was 6 42 or 49 i did not look at the
[867.22 --> 872.96]  timer once i just remember angelica saying you got so much time left do you want to give us some uh
[872.96 --> 880.08]  a little dance lesson and i was like no i don't think i should do that that's a bad idea i do remember
[880.08 --> 885.62]  having microphone issues uh but i got through it pretty well i think yeah i was i was first in the
[885.62 --> 891.00]  session so i got the privilege of standing on stage and having everyone stare at me for an extra 20
[891.00 --> 898.32]  seconds during the intros i don't even remember being like introduced and brought on that was like
[898.32 --> 905.22]  blackout moment i just like walked on and then i practiced so much and just turned into like autopilot
[905.22 --> 912.16]  so i was pretty happy with how i how i did but i just practiced so much so my first time on stage
[912.16 --> 921.64]  two years ago was like that uh i was the opening keynote the second day and just completely blinded
[921.64 --> 927.92]  and dumbfounded at the crowd the entire conference is in front of you it was my first time actually on
[927.92 --> 934.40]  stage speaking to a big crowd lots of zoom crowd zoom meetings and things but uh it was
[934.40 --> 942.50]  a different experience and it was kind of the same just went into autopilot mode and didn't remember
[942.50 --> 947.18]  a lot of the details while it was going on what caught me by surprise was i couldn't really see
[947.18 --> 951.90]  the audience i think it was the lighting or something and every presentation i've done before
[951.90 --> 957.20]  i've been able to see the entire audience but this one i couldn't so it was a little i felt a little bit
[957.20 --> 963.76]  almost like i was there by myself on the stage so i remember seeing a couple of people in the front row
[963.76 --> 967.18]  that were clearly following along with the talk but that was about it it was just maybe a couple
[967.18 --> 971.44]  of people one guy at some point smiled and gave me a thumbs up i have no idea who he was but
[971.44 --> 975.76]  shout out to that guy it really helped because otherwise i would have been talking to nobody
[975.76 --> 980.74]  i remember seeing the front row people i don't even remember seeing my sister as funny as that is
[980.74 --> 987.14]  she sat in the front row far over just so i could see her i did not and it was like beyond the front
[987.14 --> 993.86]  row it's just like a black room but i liked it that way i don't know and do you think all of you
[993.86 --> 1000.98]  have talked a little bit about how you kind of blanked out a little bit autopilot with that in mind
[1000.98 --> 1009.00]  do you feel like the like practicing before helped you be able to kind of go into that autopilot mode i
[1009.00 --> 1016.48]  just feel like it is a sign of all of you being so prepared that you were able to even go into autopilot
[1016.48 --> 1022.06]  in the first place is that what you kind of attribute it to like you've done it so many times
[1022.06 --> 1027.42]  before do any of you not practice too much i know i've heard a few people in the past talk about like
[1027.42 --> 1032.90]  not wanting to over practice so that it comes across like charismatic or more conversational in
[1032.90 --> 1037.18]  presentation mode but would love to hear a little bit about like how did you prepare
[1037.18 --> 1043.40]  was it sitting down writing notes going through your slide decks honestly i didn't practice a lot this
[1043.40 --> 1050.04]  year um because it was a lightning talk it was very it was very fast and like i mentioned it something
[1050.04 --> 1058.90]  that i talk about at work all the time my talk was on mocking and proper ways to do it had to have fun
[1058.90 --> 1065.78]  with it title was how to mock your co-workers without involving hr so it's things that i talk about all the
[1065.78 --> 1072.62]  time so i didn't need to rehearse to kind of really get the information down and it was very quick
[1072.62 --> 1081.26]  compared to past experiences where a 45 minute full tutorial i practiced that for three weeks
[1081.26 --> 1088.22]  for me the most difficult part of preparing was actually coming up with the first few things i would
[1088.22 --> 1095.04]  say everything else was pretty easy because i of course i know the material but making that first
[1095.04 --> 1100.06]  few sentences was it took me a couple hours to come up with something that i felt comfortable as an intro
[1100.06 --> 1104.42]  because it is a little awkward because you don't want to spend too much time talking about
[1104.42 --> 1110.66]  non-essentials um but you kind of want to get you know a little bit of the understanding is about what
[1110.66 --> 1116.12]  you're going to talk about so yeah that was a little awkward for me but i actually went back and watched
[1116.12 --> 1121.78]  most of the lightning talks from the last two years of go for con to be like what do you what do people
[1121.78 --> 1125.72]  do how do you introduce yourself what's important to like really get out of your mouth
[1125.72 --> 1132.18]  in the first 30 seconds that's overachiever mode right there that was like i i didn't know what to
[1132.18 --> 1142.46]  do mode i think for me i wanted to make sure that i did not have filler words because if i pause and
[1142.46 --> 1148.38]  just think about something i can i will say those so i wanted to practice enough so it was polished and
[1148.38 --> 1154.86]  i didn't have a bunch of likes or ums i just knew what i was going to say for the seven minutes and i ended
[1154.86 --> 1162.74]  right at 655 so i was also really proud of the timing i want to be almost exact i was gonna say
[1162.74 --> 1169.94]  i don't think i really spent a lot of time practicing the information i spent at least three or four
[1169.94 --> 1176.40]  run-throughs on timing because it's it's like one slide doesn't have the same information as another
[1176.40 --> 1183.12]  slide and you know in my talk i had a couple slides that were obviously inserted for um quote comedic
[1183.12 --> 1188.30]  effect so i had to sort of time that on like do i let this hang or do i like click on it
[1188.30 --> 1195.06]  read it as quick as possible and then move on to like reinforce the stupidity of my slides so the
[1195.06 --> 1202.74]  timing was hard for me i did work out that my my last slide the conclusion was about 45 seconds so i
[1202.74 --> 1211.50]  spent quite a bit of time getting to hitting that slide at six minutes to make sure that i was not going
[1211.50 --> 1216.22]  to get dinged because no one wants that i mean i can echo what other people said that the content
[1216.22 --> 1220.40]  of the talk wasn't really a problem because i know a lot of that i could easily talk for an hour but
[1220.40 --> 1225.32]  that's the problem is that i could so i had to drill it a lot and make sure that i was going to hit the
[1225.32 --> 1230.68]  timing okay because i you know with the format if you go over there's a buzzer and it doesn't look
[1230.68 --> 1235.56]  good it doesn't sound good and there's no recovery but a full-length talk you usually have at least
[1235.56 --> 1239.30]  a few minutes leeway if you're a full-length talk you're not going to get booted off the stage immediately
[1239.30 --> 1245.98]  so that was my fear i definitely spent a lot of time the whole talk was scripted pretty much
[1245.98 --> 1249.86]  start to finish and it wasn't just a series of bullet points i had to over prepare i felt like
[1249.86 --> 1255.12]  so i'm really going to push you what would you do differently i mean i know you're on autopilot but
[1255.12 --> 1261.96]  there must have been something that you recollect or now reflecting upon it that you would do
[1261.96 --> 1268.26]  differently if you were to do another round of lightning talks at six minutes there's a beep that goes off
[1268.26 --> 1274.26]  and i can't remember exactly what slide i was on when that beep went off but in hindsight i wish i
[1274.26 --> 1279.76]  had paused because i'm pretty sure i just kept going straight through it so i walked off the stage
[1279.76 --> 1284.58]  knowing like as i watched other lightning talks that i kind of maybe messed that up a bit but who
[1284.58 --> 1289.30]  knows so we'll see when the recordings come out i would have left out the highlander reference i think
[1289.30 --> 1295.54]  i was showing my age but there's a new one coming out so a few years from now it will be relevant again
[1295.54 --> 1301.88]  right i mean the the simpsons reference worked people got that one the hide the pain harold
[1301.88 --> 1309.04]  went over well uh the highlander one was just crickets not a lot of the the gopher con crowd
[1309.04 --> 1312.98]  remembers movies from the mid 80s no
[1312.98 --> 1318.24]  i personally don't i don't remember it
[1318.24 --> 1326.56]  go on jacob i i was disappointed that i resorted to using powerpoint for all my other talks i use go
[1326.56 --> 1334.96]  present and i this last year the go talk server has been extra sassy so you can't like host it off
[1334.96 --> 1339.98]  of github anymore and you got to do it local and i just said you know what i'm not i'm going to avoid
[1339.98 --> 1345.64]  any technical problems i'm going to use powerpoint trusted and true and then i think the talk
[1345.64 --> 1352.90]  right after me was using go present and i was like oh i was i was i was disappointed in myself
[1352.90 --> 1358.60]  i did the opposite i usually do something like deck set or go present where you write out your slides
[1358.60 --> 1363.84]  and markdown or some kind of you know code and i started with the tried and true this time thinking
[1363.84 --> 1368.80]  i would keep it simple and i think i got to chicago and decided i hated my slides i think i read
[1368.80 --> 1374.10]  it literally all my slides and deck set you know two days before the talk after i landed in chicago
[1374.10 --> 1380.86]  so i could have gone either way honestly do you feel like slide decks and having a deck behind you
[1380.86 --> 1386.88]  is important for lightning talks like do you think it helps people follow the talk does it help you all
[1386.88 --> 1391.44]  to kind of center yourself on where you are in the talk i've seen lightning talks where they just had
[1391.44 --> 1397.74]  one slide that had a gopher on it not even words and then they just talked for seven minutes i'd be
[1397.74 --> 1403.44]  interested to hear yours for you i mean personally i i like the slides during the lightning talk it
[1403.44 --> 1409.40]  keeps you there it keeps you following you've got a timeline and i am someone who if you give me 45
[1409.40 --> 1417.24]  minutes and slide with one word on it yeah i'll do that i will run forever so having the slides and
[1417.24 --> 1423.70]  keeping timing was really important for me i can't see doing it without slides because
[1423.70 --> 1427.62]  you know as you're doing the scripting and you're memorizing it to some extent
[1427.62 --> 1433.44]  like with me i associate that with the pictures i'm seeing on the slides so when i see that picture
[1433.44 --> 1438.56]  the whole story comes back and i can you know i can basically remember it that way so i couldn't do
[1438.56 --> 1445.16]  it without the slides i kind of think the same if it was without slides i would have to rehearse
[1445.16 --> 1452.76]  so much to be able to get it all in that it would become mechanical i don't think the presentation
[1452.76 --> 1460.68]  would go over as well without the slides because it with the timing and the the cues and then you
[1460.68 --> 1466.88]  can throw in simpsons references and get a laugh from the crowd i resonate i also think like i need
[1466.88 --> 1473.80]  the slides to form the story more so i don't just talk about nonsense and go off on tangents not that i
[1473.80 --> 1479.48]  think i would but just to keep in order build the story from start to finish and then like add the
[1479.48 --> 1485.22]  details we're like relevant with slides and whatnot yeah to dylan's point how are you going to get
[1485.22 --> 1491.40]  memes if you don't have slides that's the most important aspect i feel like it's hard though
[1491.40 --> 1496.72]  because you don't know what memes to choose that are going to resonate with the full gopher con
[1496.72 --> 1501.80]  audience i feel like talks in the past that has been obviously the content's difficult too but
[1501.80 --> 1508.56]  for me it's been like what gift do i put here what meme would resonate i feel like it's a challenge
[1508.56 --> 1519.14]  i i teach and i intentionally put cringe memes into the slide decks just to keep the uh the gen alphas
[1519.14 --> 1525.66]  you know entertained and it's like it's cringe uh but for the lightning talk i was like i agree
[1525.66 --> 1529.98]  there's like what's gonna hit you know i don't know the whole group of people we have people from all
[1529.98 --> 1537.56]  over the world uh so i just went with old standard british humor of of silliness and that that seemed
[1537.56 --> 1544.84]  to work so i mean it's an it conference the the hide the pain this is fine we'll always go over well
[1544.84 --> 1550.14]  we can all identify everyone will laugh at a disaster for sure if i had to change something
[1550.14 --> 1554.58]  that's actually something i would change i felt like i under memed i mean i was like i'm going to
[1554.58 --> 1559.56]  keep this super simple this is like my first time presenting at gopher con and i was like i could have
[1559.56 --> 1566.22]  really thrown some memes in there i defaulted to showing cute gopher images instead of the memes
[1566.22 --> 1571.40]  because i knew that would go over well know your audience a load of cute gophers is definitely going
[1571.40 --> 1577.52]  to resonate awesome so i'd love to talk a little bit now about the differences between lightning talks
[1577.52 --> 1586.28]  versus longer talks workshop sessions i know a number of you are very seasoned dylan um at talking
[1586.28 --> 1591.70]  at these kind of conferences so i'd love to understand what do you will see as the core
[1591.70 --> 1597.04]  differences whether it be the way you prepare the way it feels when you present between doing lightning
[1597.04 --> 1605.26]  talks and doing longer form talks maybe dylan as our seasoned speaker you gopher con you can you can
[1605.26 --> 1609.86]  let me know as the grizzled veteran which actually i think everyone on this call is pretty experienced
[1609.86 --> 1618.54]  honestly but yes the grizzled gopher con veteran dylan so um my first very first talk was like i said the
[1618.54 --> 1625.46]  the second day keynote it got picked and i was in front of the entire conference on the second day
[1625.46 --> 1632.24]  first talk in the morning dumping on go modules with ruscock sitting in the front row so that wasn't
[1632.24 --> 1641.66]  awkward at all but it was 25 minutes um so there were a lot of nerves um i spent a lot of time kind of
[1641.66 --> 1650.16]  hey is this right is this the right balance of information not getting into droning on about
[1650.16 --> 1658.56]  technical things um in comparison to lightning talk i approached it as a lot of fun it was light-hearted
[1658.56 --> 1668.08]  uh i think i had 17 or 18 slides and probably six of them had some type of meme or joke on it a lot
[1668.08 --> 1678.24]  more fun to do the longer talk was much more stressful especially with russ 20 feet away and i also did a 45
[1678.24 --> 1687.20]  minute tutorial last year that one was a lot of time much much longer to put in uh that one was probably
[1687.20 --> 1695.36]  65 or 70 slides with a bunch of content that one took a long time to prepare for and to get everything
[1695.36 --> 1703.04]  together so for me this year was fun i came in didn't have any responsibility to do a big talk there
[1703.04 --> 1710.48]  was no stress level i went into it like hey lightning talks are gonna be fun this year i can go rant for
[1710.48 --> 1716.00]  six and a half minutes i mean you keep on saying how fun it was i would love to hear from kind of anyone
[1716.00 --> 1721.92]  else in the group when preparing for a longer talk do you feel like it has to be a little bit more
[1721.92 --> 1727.68]  serious i mean in my mind it's you have to keep your audience's attention for a longer period of time so
[1727.68 --> 1733.12]  the temptation certainly my temptation would be i gotta keep it light to like keep them engaged get a
[1733.12 --> 1738.08]  laugh here and there if i go too serious maybe they'll zone out but also if you're talking about a
[1738.08 --> 1744.16]  really complex technical concept you want to keep it crisp and clear and maybe not muddy the waters with
[1744.16 --> 1750.64]  the with a joke that might not resonate would love to hear your kind of your reactions to that
[1750.64 --> 1755.20]  i mean i think my lightning talk was i wouldn't say super technical but it did get into the weeds of
[1755.20 --> 1760.08]  something that a lot of people don't pay a lot of attention to and so i had to get a lot of info
[1760.08 --> 1765.68]  out pretty quickly so i i don't think i had time to put memes on slides really i like dylan was saying
[1765.68 --> 1772.08]  his you know his longest talk had 70 slides the one including i guess transitions the the talk i gave was
[1772.08 --> 1778.00]  48 slides because there's just a ton of info to get out so i i really don't know i'd be curious like
[1778.00 --> 1782.24]  this is certainly the biggest stage i've ever talked on so that could be why this is the case
[1782.24 --> 1785.92]  but i feel like i had to prepare much more for this than i have for any other talk i've given
[1786.64 --> 1792.08]  you know at work or local meetups or anything like that matt what do you think i think that one of the
[1792.08 --> 1797.12]  things that stresses me out about longer talks is the feeling like you're covering something more
[1797.12 --> 1803.44]  comprehensively and you really have to like know the topic in and out from like every angle because
[1803.44 --> 1807.52]  someone's going to ask you especially if it's at like a meetup someone's going to be like oh but
[1807.52 --> 1814.32]  what about this what happens this and i have felt for the longer presentations a lot more stress to be
[1814.32 --> 1821.84]  like uh comprehensively cover the technical topic and for the lightning talk i wanted to sort of avoid that
[1821.84 --> 1827.20]  particular stress and present something more of like uh here's something that you can go explore
[1827.20 --> 1833.36]  yourself so that was probably the biggest difference was i wanted to present more of like a marketed
[1833.92 --> 1839.20]  like pull people in rather than like feel like i have to comprehensively cover some really deep
[1839.20 --> 1845.36]  technical uh topic yeah luckily no q a at go for con i know some other conferences will allow the
[1845.36 --> 1850.64]  audience to ask questions and uh yeah it can sometimes be a bit intimidating and a bit of a nightmare
[1850.64 --> 1855.20]  especially if you have someone in the audience who uh is making it their mission to ask you the
[1855.20 --> 1861.68]  most complex question that they possibly can and therefore you are you are forced to be like it's
[1861.68 --> 1866.72]  a really good question um i'll talk to you after this yeah that's more off the stage the conference
[1866.72 --> 1871.36]  we're gonna meet me to the side of the stage in a few minutes yeah and then oh i'm so sorry i'm just
[1871.36 --> 1876.72]  i need to rush off somewhere i'm so sorry i can't actually talk to you right now the email that we got
[1876.72 --> 1881.60]  from the conference organizer said in big bold red letters do not field any questions after your
[1881.60 --> 1888.56]  talk so she was she was pretty explicit about avoiding that yeah for sure last year i did have
[1889.60 --> 1895.36]  six or seven people lined up on the side of the stage asking questions about the content of the
[1895.36 --> 1904.00]  talk so my my talk went over by about 15 or 20 minutes with the conversations afterwards i think you
[1904.00 --> 1909.76]  get a lot more money or a lot for your money when you do a seven minute talk versus you know say a 30
[1909.76 --> 1915.52]  or 45 minute talk in terms of the number of people that you reach with a single message and it takes
[1915.52 --> 1920.80]  about the same amount of time to prepare for both so why wouldn't you do the lightning talk then so i
[1920.80 --> 1925.12]  want to challenge that are you saying that you think it takes the same amount of time to prepare for
[1925.12 --> 1931.04]  a lightning versus a longer talk for you in my limited experience it does take about the same amount of time
[1931.04 --> 1937.04]  yeah i mean i've done 45 minute talks as well and it took about the same time to prepare for it but
[1937.04 --> 1945.68]  then if you practice the practice loop is much longer it is definitely i'm definitely the other end of the
[1945.68 --> 1954.00]  spectrum on that um like i said i spent weeks preparing for that first talk literally multiple weeks and
[1954.00 --> 1962.24]  the lightning talk i think i spent 25 30 minutes writing up the original proposal then probably
[1962.24 --> 1968.40]  two hours doing slides and i practiced it four or five times mostly to get it under seven minutes do
[1968.40 --> 1971.52]  you think that had anything to do with the content of the talk or do you think that was because
[1972.40 --> 1980.00]  you know it's just a shorter talk probably a bit of both um a lot less stressful and there's a lot
[1980.00 --> 1988.40]  less concern about making a mistake in 15 slides than in 60 so there isn't as much to rehearse and
[1988.40 --> 1996.48]  memorize but also this was content that i talk about all the time i could do seven minutes on it right now
[1996.48 --> 2003.20]  if we wanted to just ad hoc i mean i feel like i could do you know 10 minutes ad hoc and that's sort
[2003.20 --> 2007.44]  of the problem so a lot of the practice went into making sure that i wouldn't wouldn't do that i think
[2007.44 --> 2011.68]  i think i'm kind of on the opposite end of the spectrum here from you as far as i think i probably
[2011.68 --> 2016.08]  had to put more time into just because it was entirely scripted but i don't know i haven't
[2016.08 --> 2022.16]  i haven't done a longer talk at gophercon so long talk short talk at least it's not a workshop
[2022.80 --> 2028.80]  at least it's not a workshop yeah prepping for workshops or is not great i i don't i love doing
[2028.80 --> 2034.64]  workshops uh mostly because i've done into like high school and then college students but the prep form is
[2034.64 --> 2040.72]  like you got to look at every single you know piece of hardware they're bringing in or you know
[2040.72 --> 2047.28]  someone comes in and they're running go 112 and you're like what yeah i assume their prep email
[2047.28 --> 2056.16]  did not tell them not to field any questions on windows 95 i mean do you feel like a workshop is just
[2056.16 --> 2063.20]  like a more segmented talk like you give a bit of a spiel and then you talk through the concept and then
[2063.20 --> 2069.12]  they do an exercise i know it's very down to the workshop lead style of running the workshop but i
[2069.12 --> 2073.44]  would i would be interested we've talked about kind of difference between lightning and full time
[2073.44 --> 2078.96]  like talk versus workshop session would love to dig into that just a little bit i mean i'll keep
[2078.96 --> 2086.88]  talking just because i will uh i'm a consumer of workshops i do love them i do back-end code so like the
[2086.88 --> 2093.28]  first workshop i did at this last govercon was all the iot stuff and you know the the badger boards and
[2093.28 --> 2098.40]  the drones and i was like this is awesome stuff i'm not an embedded programmer whatsoever but this is
[2098.96 --> 2105.52]  a diversion from what i normally do and it's really interesting now organizing that workshop i would
[2105.52 --> 2111.60]  hate to be on the other side but a consumer of it it was fun and great so yeah i've kind of been on both
[2111.60 --> 2122.56]  sides uh i attended two workshops at gopher con one years ago 2018 i believe and then one this year
[2122.56 --> 2130.32]  and they're they were drastically different um but both were very hands-on kind of almost classroom
[2131.20 --> 2139.36]  environment which is like jacob said different it's fun it's a diversion um but it's it's definitely a
[2139.36 --> 2146.24]  different experience on the flip side a co-worker of mine hosted a workshop put on put one on this
[2146.24 --> 2154.08]  year and i helped him put together his materials and review the exercises and kind of going through
[2154.08 --> 2160.80]  and writing the code for them how does this work how does it feel it definitely was a ton of work that
[2160.80 --> 2168.72]  he put into making it an educational experience uh where people would feel like they got value out of it
[2169.36 --> 2181.12]  this is a changelog news break i like this set of metaphors for how to think about bucketing
[2181.12 --> 2187.76]  challenges into different categories some problems are like harvesting quote harvesting problems have
[2187.76 --> 2193.60]  straightforward solutions and no shortcuts you just get a big basket and pick every strawberry in the
[2193.60 --> 2200.40]  field you solve these problems with pure perseverance slogging away for weeks months or years until they
[2200.40 --> 2206.00]  are done some problems are like fishing you know that there are fish out there in the ocean but you
[2206.00 --> 2211.68]  don't know exactly where if a great fisherman knows where the hungriest fish are and how to set their lines
[2211.68 --> 2217.84]  just right they might catch everything that they need in a few hours fishing problems can sometimes be solved
[2217.84 --> 2224.64]  shockingly fast by motivated teams with a bit of luck some problems are like panning for gold going
[2224.64 --> 2230.56]  out to a river or stream where there might be gold getting your pan out and seeing if you can find traces of
[2230.56 --> 2236.80]  the shiny stuff in the sediment if you find gold you can become generationally successful think of the
[2236.80 --> 2243.68]  massive moats created by google search or the airbnb network end quote if you can categorize the problem
[2243.68 --> 2249.28]  you're trying to solve into one of these buckets applicable strategies become much more clear you
[2249.28 --> 2256.40]  just heard one of our five top stories from monday's changelog news subscribe to the podcast to get all of
[2256.40 --> 2262.64]  the week's top stories and pop your email address in at changelog.com slash news to also receive our free
[2262.64 --> 2273.60]  companion email with even more developer news worth your attention once again that's changelog.com slash news
[2273.68 --> 2283.44]  so before we kind of move on to our second segment of the episode which is going to be where we're
[2283.44 --> 2290.16]  going to put a couple of you to the test in terms of being concise and to the point i would love to go
[2290.16 --> 2295.76]  around and i can call on you kind of one by one and ask you to give like your top tip you know one or two
[2295.76 --> 2302.80]  tips to anyone who's thinking about you know doing a lightning talk to help our kind of listeners understand
[2302.80 --> 2307.84]  from from you all now you've done it i would argue successfully having seen all of yours and i enjoyed
[2307.84 --> 2314.16]  them a lot kind of give them some powers of wisdom um so why don't we start with you matt sure um
[2314.96 --> 2322.40]  probably the thing that helped me the most was presenting it to someone else and obviously practicing
[2322.40 --> 2327.44]  a lot at least for my style i get really really nervous when i do these talks and i really need to be
[2327.44 --> 2333.12]  on autopilot but presenting it to another person and getting their feedback but also having to
[2334.00 --> 2343.52]  like stow your self-consciousness and get used to talking to another person right jacob so i got i got
[2343.52 --> 2348.80]  two things and it's more like i guess in the not with a prep side but like the hey i gotta choose
[2348.80 --> 2354.72]  something kind of side of things so i had it easy this was a workshop that this was the introduction to the
[2354.72 --> 2360.16]  workshop that i just sort of chopped down and then got the timing right but in preparation for something
[2360.16 --> 2367.04]  new i think you got really two paths either you can focus on a single problem and then your path to
[2367.04 --> 2373.68]  that solution and it could be a simple problem and a simple solution and the filler in between is all the
[2373.68 --> 2379.60]  context and background it's the why of why this was a problem or why the solution had to happen this
[2379.60 --> 2385.36]  way and then you can get right to 659 and you're done and the other thing i was looking at was
[2385.36 --> 2391.60]  highlighting um a product you know doing sort of product highlight and and you know product being
[2391.60 --> 2397.76]  a piece of software you know a tool something like that and for there you can just add highlights of
[2397.76 --> 2404.96]  that until you get to 69 pretty much what what matt did honestly you know simple highlight tool get
[2404.96 --> 2410.00]  there bang you're done and and that seems really effective matt matt's talk was great and i liked it
[2410.56 --> 2416.80]  everyone's talk was great i'm so sorry i love everyone's talk uh sure you say now yeah we're
[2416.80 --> 2424.96]  picking favorites now that's my two like you know tips for finding something okay but how to talk about
[2424.96 --> 2431.12]  a product without it sounding like a marketing pitch which i think can sometimes be a challenge i think when
[2431.12 --> 2436.00]  i've like thought about some lightning talks talking about like oh why do i like this tool it has x by
[2436.00 --> 2441.92]  z features i've sometimes felt myself like i was being like a sales rep being like this is why temporal
[2441.92 --> 2448.08]  is great which it is by the way temporal is great but you know what i mean like finding that balance
[2448.08 --> 2454.56]  i think focusing on what it provides you know it's not really focusing on the product itself but just
[2454.56 --> 2458.80]  focusing on what it provides and then at the end of the talk you can say hey all these things that would
[2458.80 --> 2464.24]  be great in something oh look i've been talking about temporal this whole time and then the last
[2464.24 --> 2469.60]  minute you just discuss how you use it well mike drop you should come by the booth we have sales
[2469.60 --> 2477.60]  people there throw candy into the audience to a technical audience you can sort of tap into why you
[2477.60 --> 2481.92]  like working on it like why it's exciting to you because that might excite some of them and so instead
[2481.92 --> 2487.76]  of trying to sell it to them you sell them on why you work on it and that's usually a better it goes over
[2487.76 --> 2493.20]  better i think than a logo that's what i would say is like my tip is like picking something you're
[2493.20 --> 2497.28]  passionate about and that like excites you not something that's kind of like dull and boring
[2497.28 --> 2503.28]  because then it'll be dull and boring for the like the attendees and then my tip was i like practice in
[2503.28 --> 2508.48]  a mirror because no one wants to have just like a like a dull face when you're presenting right you need
[2508.48 --> 2514.24]  to be engaging i love that i feel like i should do that before any go time episode even though they
[2514.24 --> 2518.88]  don't really see us but uh i feel like i don't want to be animated for you all i don't want a dull
[2518.88 --> 2528.40]  face if anyone ever asked me should i i would say yes do it one of the one of the highlights of
[2528.40 --> 2536.00]  lightning talks for me is that they are random like they're not so regimented technical it's going to be
[2536.00 --> 2542.56]  go execution tracer or logging or tracing or whatever the case may be for the language they're random
[2542.56 --> 2550.08]  they're all over the place it's a a fun diversion to go and see matt this year talk about remodeling
[2550.08 --> 2557.84]  his kitchen the randomness is fun and it's a nice diversion for people so whatever it is that you think
[2557.84 --> 2564.48]  that you want to talk about do it i think the like genuine passion for the topic comes through a lot more
[2564.48 --> 2569.92]  enlightening talks because i think it's easier to be genuinely passionate about a topic for seven minutes
[2569.92 --> 2575.04]  than for 45 minutes like after 45 minutes you're like can i just talk about something else please
[2575.60 --> 2583.44]  it's exhausting talking for that long the adrenaline crash after 45 minutes is is definitely real
[2584.64 --> 2591.36]  andy what is your top tip i uh second um i think i think cassie said this is that it's really important
[2591.36 --> 2596.00]  to talk about something you're passionate about you know what is it that you can talk about that just
[2596.00 --> 2601.04]  lights you up you know and just just makes you just smile about what you're talking about i think
[2601.04 --> 2607.52]  that's key and i think the other the other big tip is just get a good night's sleep beforehand because
[2608.24 --> 2612.64]  you know you want to practice a lot the night before and then just go to sleep in the morning
[2612.64 --> 2617.44]  practice again and you'd be you'd be amazed at how much better you can do the talk you know the next day
[2617.44 --> 2623.60]  and that helped me a lot um and definitely hydrate you gotta drink a lot of water because you're kind
[2623.60 --> 2628.72]  of nervous you know whatever and you're burning up all that water and you get up on stage and all of a
[2628.72 --> 2634.24]  sudden you just you know you get a dry mouth so definitely want to hydrate a lot so i can count it i
[2634.24 --> 2639.20]  can have a little counterpoint to that which was i you know thought it would be a good idea to stay super
[2639.20 --> 2644.24]  hydrated but we get mic'd up like 20 minutes before the talks start and then i was the second in the lineup so i
[2644.24 --> 2648.80]  had to stay for the entire rest of the hour so i was going on like two hours after drinking a ton
[2648.80 --> 2654.00]  of water because i really did not want to get dry mouth up on stage so it can kind of go both ways
[2654.00 --> 2659.68]  but hydration is a good tip anyway also andy uh getting a good night's sleep is easier said than
[2659.68 --> 2664.88]  done before doing something like public speaking yeah that's hard at the gopher con because you
[2664.88 --> 2669.20]  want to go and hang out with people and all that but you really you know you have to think about it
[2669.20 --> 2676.24]  yeah as a typical software engineer introvert i save up my socializing for the four days during
[2676.24 --> 2684.16]  gopher con and i do a year of socializing in those three nights nice yeah same it's like you see the
[2684.16 --> 2688.48]  same people and then you're all friends and then you're like oh wait but i need to practice i can't
[2688.48 --> 2696.56]  go out tonight but after my talk i'm all for it no for sure last but certainly not least adan what's your
[2696.56 --> 2702.24]  top tip i know you're plus one but i want to hear your unique one yeah i think everyone has stolen
[2702.24 --> 2706.72]  what i was going to say so far but i'll say because i definitely struggled getting mine under time and
[2706.72 --> 2711.92]  making sure that it would be under the right time so i uh i broke it up into like sections or chapters
[2711.92 --> 2717.44]  and i would drill each section like independent of one another and it wasn't until you know the night
[2717.44 --> 2722.08]  before the morning of that i was able to string them all together but i kind of knew i was under seven
[2722.08 --> 2726.32]  by just adding up the amount of time it took to do each individual chapter and that that helped
[2726.32 --> 2731.68]  breaking it up so you're not on rails the entire time did that help also like cutting down time
[2731.68 --> 2736.08]  if you found a section was a little bit longer you were able to like cut it down was that also kind
[2736.08 --> 2742.56]  of helpful as a tool yeah i can kind of prioritize the importance of each section as far as what it'll
[2742.56 --> 2747.36]  take to make the audience understand what i'm trying to talk about and then say okay i will need to borrow
[2747.36 --> 2752.00]  a bit from one section to make this section or to emphasize this section so it did help a bit but
[2752.80 --> 2759.36]  so any final piles of wisdom before we move on to our elevator pitches something i learned i didn't
[2759.36 --> 2767.60]  expect is uh mac os has like the scripting feature can let you resize windows to very specific sizes
[2768.48 --> 2773.76]  and that's a top tip i got from jeff gearlings blog i like watching his stuff on youtube and i was
[2773.76 --> 2780.16]  like wow this guy has all the tips awesome thank you very much for your top tips right now we don't
[2780.16 --> 2785.84]  have a jingle for it but i'm gonna ask our lovely producer jared to make me one for when we actually
[2785.84 --> 2793.60]  release the episode for elevator pitches so i'm just gonna do do yeah elevator pitches um
[2794.24 --> 2799.12]  so that's the jingle right there knowing jared he's probably gonna sample my voice from this
[2799.12 --> 2804.40]  recording and just put it in there just to spite me we're gonna auto-tune this so hard
[2805.68 --> 2811.20]  i will be making sure that happens because i'll be disappointed if your voice is not the jingle i
[2811.20 --> 2816.16]  think uh doesn't aerosmith have a song about elevators oh my gosh yes we should sample that
[2816.16 --> 2821.44]  and we just make sure that we don't go over the copyright allowed number of seconds and we'll be
[2821.44 --> 2827.60]  fine if not i can just grab my guitar give it a go it's fine add a few extra chords so that it's not
[2827.60 --> 2835.04]  technically that close i would love to hear that me too but luckily we have some wonderful people
[2835.04 --> 2840.80]  who probably will do it far better than i would awesome so the way it's gonna work is i will kind
[2840.80 --> 2847.44]  of call on you i won't start at the time then i'll ask you to you know introduce yourself the title of
[2847.44 --> 2855.52]  your elevator pitch and then i will say three two one go you will have 60 seconds to give your elevator
[2855.52 --> 2862.16]  pitch which was your lightning talk at gopher con when you get to 60 seconds there will be a buzzer
[2862.16 --> 2869.36]  it will not be a sound effect buzzer it will be a buzzer a la angelica's mouth and it will sound
[2869.36 --> 2878.56]  somewhat like a goat crossed with a cow like at that point your time has been cut off so you can quickly
[2878.56 --> 2884.64]  make your conclusion and then i will do the same for the next wonderful elevator picture and um we'll get
[2884.64 --> 2889.84]  through you we have lovely four elevator pitches today and we're going to start with you dylan
[2890.72 --> 2899.92]  so dylan introduce yourself give me your your title and then i will say three two one go and then you'll
[2899.92 --> 2906.24]  you'll be off to the races so dylan you want to introduce yourself sure i'm dylan burke i work at
[2906.24 --> 2913.60]  crowdstrike i'm an engineer for a long time my lightning talk today is how to mock your co-workers
[2913.60 --> 2923.04]  without involving hr thank you so much right three two one go so mocking your co-workers usually earns
[2923.04 --> 2929.12]  you an uncomfortable meeting with your manager and someone from hr but it doesn't have to if you limit
[2929.12 --> 2936.72]  it to just your tests opinions vary on whether or not to use mocks but if you do don't assume everyone
[2936.72 --> 2942.48]  else will make the same decisions that you did don't export your mocks that's the line sounds
[2942.48 --> 2948.80]  simple enough but how do we get there first make sure that all of your mocks are in an underscore test
[2948.80 --> 2956.80]  go file or in a folder under internal that way guarantees that no one else can import your mocks
[2956.80 --> 2962.00]  and create coupling next if you're using one of the frameworks that does code generation
[2962.00 --> 2971.28]  don't assume it's installed go install drops binaries in go path bin lastly don't predefine
[2971.28 --> 2979.84]  and export interfaces you can't export mocks if there's nothing to mocks missed it by one second
[2981.04 --> 2986.80]  that was very good i like that you didn't speak too fast you still retained an understandable pace
[2986.80 --> 2996.16]  five points to griffindor that was great score edin you're next so please introduce yourself
[2996.16 --> 3002.00]  give us the talk title and then i'll give you your countdown yeah uh i'm edin i work at contrast
[3002.00 --> 3007.44]  security on our go agent and i've been programming for a medium amount of time i guess compared to dylan
[3007.44 --> 3017.28]  and my talk was called implementing code coverage with tool exec great three two one go go's code
[3017.28 --> 3022.00]  coverage tool takes your source code and adds little counters to the top of every block of statements
[3022.00 --> 3027.68]  so each branch gets its own counter and as your code runs it increments these counters and then before
[3027.68 --> 3032.80]  your program exits it dumps the state of all of these counters to disk and then go can use this to tell
[3032.80 --> 3038.08]  you which parts of your code ran so it's really a lot simpler than most people assume it is now all
[3038.08 --> 3042.72]  of these counters get added just before your code is compiled and there's a flag built into go called
[3042.72 --> 3047.60]  tool exec which tells go that instead of spawning the compiler it should spawn your program instead
[3048.48 --> 3054.72]  and you can use that to implement your own version of the coverage tool now the obvious follow-up is why
[3054.72 --> 3059.76]  would you ever do this and the answer is you probably shouldn't but it is a fun excuse to poke around
[3059.76 --> 3064.80]  inside the go command and learn a little bit about how it works and it's it's usually simpler than
[3064.80 --> 3070.72]  people assume it is so it's a lot of fun to do it it's all i got oh my gosh under time i love that
[3071.36 --> 3078.08]  52 seconds didn't expect that i was pretty sure i was going to go over oh you've clearly packaged even
[3078.08 --> 3082.80]  within 60 seconds you've got your little sections so you've got it down to a science at this point
[3082.80 --> 3089.68]  you're offsetting my one second over it's fine yeah sharing is caring we can just share the time
[3089.68 --> 3096.56]  between you both uh awesome next up we have andy do you want to introduce yourself in your talk
[3097.12 --> 3103.52]  i'm andy joseph i founded a project called pronto gui i've been a developer for many many years
[3104.08 --> 3110.72]  many different languages and uh the title of my talk is an infomercial on would you like a gui with that
[3110.72 --> 3119.84]  great title i i predict that it will take 56 seconds and 21 roughly so okay i will we'll put
[3119.84 --> 3128.08]  that to the test ready three two one go if you love the go programming language as much as i do
[3128.08 --> 3132.88]  then you never want to leave that environment thankfully there are go modules for just about
[3132.88 --> 3138.00]  everything but what if you want to create a gui for your service do you have time to build and
[3138.00 --> 3144.96]  maintain a solution in react js chances are you don't this is where pronto gui helps first you
[3144.96 --> 3151.36]  import the pronto gui module into your program it's lightweight it's fast it has few dependencies next
[3151.36 --> 3156.88]  you build your gui using primitives requiring things representing things you want to see such as buttons
[3156.88 --> 3162.32]  text items tables and so on finally you launch a pronto gui app which is built using flutter
[3162.32 --> 3169.44]  to interact with your gui they communicate using grpc streaming how cool is that this all happens in
[3169.44 --> 3175.44]  hours not weeks i've used pronto gui to build solutions such as simulating industrial machines
[3175.44 --> 3180.72]  and an expense report management solution i'm confident it can do a lot more this is a fast way
[3180.72 --> 3184.80]  to develop a gui and go you can get it on github and let me know what you think
[3188.24 --> 3193.60]  but wait there's more there is more but i didn't have time that was a great infomercial
[3194.24 --> 3199.92]  i want to go use pronto gui right now adjusting the tone and format based on the time you get given
[3200.48 --> 3206.40]  innovation at its finest and flexibility the key to doing a one-minute talk is to practice breathing
[3206.40 --> 3212.00]  because i felt like i was running out of air how do you do you have time to breathe in a one-minute
[3212.00 --> 3219.04]  talk or do you just have to practice underwater oh it's hard awesome last but certainly not least
[3219.04 --> 3224.56]  and those who um have not given the elevator pitch i will ask if you'd like to give one no pressure
[3225.12 --> 3230.48]  but finally we have cassie do you want to give a little intro on you and your talk title and then
[3230.48 --> 3237.12]  i'll count you in definitely can do yeah i'm cassie coil software engineer at diagrid i contribute to
[3237.12 --> 3244.48]  the dapper open source project awesome and what is your talk title oh yes i forgot uh standardizing
[3244.48 --> 3250.96]  errors and go a practical guide with dapper and that is my intro sentence as well so i will say it again
[3250.96 --> 3260.16]  when i start love that right three two one go welcome to standardizing errors and go a
[3260.16 --> 3265.92]  practical guide with dapper in this talk i'll introduce dapper distributed application runtime
[3265.92 --> 3271.92]  the 10th largest cncf project and share about our open source errors package to be more empathetic to
[3271.92 --> 3278.48]  our users we'll explore the errors package that enriches errors using the informative model inspired
[3278.48 --> 3285.84]  by the google's grpc api error details the dapper kit errors package is written entirely in go
[3285.84 --> 3291.12]  all open source and it uses the builder pattern allowing you to provide users with essential
[3291.12 --> 3298.40]  error details including resource info retry info help link and more we implemented the error interface
[3298.40 --> 3304.24]  such that the primitive type returned is actually here as well and then you don't have that additional
[3304.24 --> 3309.76]  type to maintain this is definitely an ongoing effort for us i hope you see how it benefits us in our
[3309.76 --> 3318.80]  community how it could also benefit you and yours thank you so much oh so close you got it right right
[3318.80 --> 3325.04]  on that 60 seconds now i feel like a massive failure as the only one who went over i mean you did tell us
[3325.04 --> 3332.72]  earlier in the episode that you like don't really prepare so you know expect it no joking right honestly i
[3332.72 --> 3338.16]  feel like when i asked you all whether you would be comfortable doing your lightning talks in one minute i was
[3338.16 --> 3344.56]  very prepared for you all to be like no so thank you very much for accepting the challenge and i
[3344.56 --> 3349.60]  actually feel like those are really great elevator pitches that i got a lot out of and for those of
[3349.60 --> 3355.92]  you who feel like that elevator pitch just wasn't enough you want to dig in more as we've mentioned
[3355.92 --> 3361.04]  all of our lovely guests today gave lightning talks at go4con this year we'll be releasing the
[3361.04 --> 3367.44]  videos on our go4con youtube hopefully in the next few weeks depending on when this episode gets
[3367.44 --> 3374.24]  released uh timings may vary but you can check there and see the full seven minute talk from
[3374.24 --> 3380.56]  all of these lovely guests would anyone who didn't give an elevator pitch like to no pressure i just want
[3381.04 --> 3390.08]  equal opportunity sure jacob you're up for it now i feel left out zero prep we see what we can do here
[3390.08 --> 3394.16]  i'll give you a second introduce yourself and tell us what you're going to be talking about
[3394.16 --> 3401.76]  so i'm jacob i write software that's literally from my bio slide because bios take too long and
[3401.76 --> 3408.40]  what is your title you can you just start let's just go let's just start okay i'm ready three two one go
[3408.40 --> 3415.68]  so go lang for competitive programming emphasis on question mark uh the spoiler here is no so
[3415.68 --> 3422.80]  there's a law in journalistic headlines that if the headline ends in a question mark the answer is no
[3422.80 --> 3429.68]  and in this case no go is not great for competitive programming what is competitive programming uh it's a
[3429.68 --> 3437.44]  time sport where you basically play code golf to solve a problem with a solution in code and a lot of
[3437.44 --> 3444.64]  times it's in python or javascript or if you hate yourself java itself but go is not great for this
[3444.64 --> 3450.32]  because it doesn't solve any of goes actual uh you know it doesn't play to any of its strengths like
[3450.32 --> 3457.44]  parallelism or software engineering so uh competitive programming itself is sort of anti-theatical
[3457.44 --> 3466.64]  to software engineering and uh don't use go for it done mic drop nice well done
[3467.60 --> 3475.36]  if you hate yourself use java i feel that so much yeah need that on a shirt besides that part of the
[3475.36 --> 3480.40]  message i actually really like the other message which is the reason that go is not really great for
[3481.52 --> 3485.68]  competitive programming is actually stuff that makes it good and i thought it was a nice way to
[3485.68 --> 3490.96]  phrase it and i mean i could talk about it longer obviously and i'll i will for five more seconds it's one
[3490.96 --> 3496.16]  of the things the students right now i really have a problem with because i'm having to tell them hey for
[3496.16 --> 3501.84]  career readiness as a senior you need to like dive back into algorithms you need to start doing leak
[3501.84 --> 3507.44]  code because all the online assessments now it's not a free pass anymore like the market's a lot
[3507.44 --> 3514.16]  different and at the same time i'm telling them also this is dumb leak code is sort of dumb if you
[3514.16 --> 3519.36]  know if you enjoy it it's great you know it's like people who play chess there's no point to chess but if you
[3519.36 --> 3527.20]  play it and enjoy it do it right but yeah i i i'm gonna mirror that sentiment go go is not designed
[3527.20 --> 3534.40]  for this it's not designed for software engineering at scale the reasons we all love it it's funny you
[3534.40 --> 3540.64]  you're encouraging leak code because i have a personal aversion to interview processes that involve leak code
[3540.64 --> 3546.24]  hey i i'm on the same side with you there no one likes them no one likes them i go out of my way to
[3546.24 --> 3552.48]  not do it it's like no we're not gonna do some stupid algorithm algorithm algorithm but i can't even
[3552.48 --> 3560.88]  speak it annoys me so much some stupid algorithmic problem that either you already know or you don't
[3560.88 --> 3568.32]  know and you're just gonna flounder for 45 minutes neither one of those helps anyone but if you practice
[3568.32 --> 3578.88]  you might get a similar question who has time to practice yeah that's the real question i feel like
[3578.88 --> 3584.40]  you all know where my brain is going because we're going up to unpopular opinions and i feel like jacob
[3584.40 --> 3594.00]  you've given us two already to work off those were popular opinions unpopular opinions maybe leak
[3594.00 --> 3600.88]  comb sucks i'm sure there are people who love it this is a go podcast java is terrible is a pretty
[3600.88 --> 3608.48]  safe bet yeah awesome so thank you all for taking the time to both do kind of elevator pitches talk
[3608.48 --> 3614.48]  about lightning talks the differences between them and long talks and also just spending your friday
[3614.48 --> 3622.16]  afternoon with me i really appreciate it um so with that very kind and caring sign off we're now
[3622.16 --> 3628.16]  going to move into the more spicy section uh of the episode which is unpopular opinions
[3628.16 --> 3653.92]  so who is going to start us off with an unpopular opinion reminder it does not need to be about go
[3653.92 --> 3661.52]  or tech or anything remotely to do with go or tech it can be just an opinion that you believe when put
[3661.52 --> 3668.08]  on twitter to a wonderful go community or other software engineers who happen to listen to go time
[3668.08 --> 3675.20]  they're going to be like no i don't agree with you i have a technical one great using protobufs well-known
[3675.20 --> 3685.60]  types is overrated and what alternative do you suggest just define your own values uh my example is
[3685.60 --> 3693.28]  timestamp like a timestamp is an integer if we're being real about it it's an integer or maybe a string
[3693.28 --> 3700.00]  why do you need to pull in an external dependency and a nested message and all the conversions back and
[3700.00 --> 3709.60]  forth for a time disclaimer my version is partly informed by having to do a massive conversion off of
[3709.60 --> 3717.04]  gogo protobuf two-ish years ago and they had their own implementation of all the protobuf well-known
[3717.04 --> 3727.84]  types that i had to straddle gogo and google for about 18 months so just don't do we think that's a
[3727.84 --> 3734.32]  unpopular one i think it makes sense i mean i've had to deal with timestamps before and i i've rolled
[3734.32 --> 3739.20]  my own type like three times dealing with other people's time formats because there's almost no
[3739.20 --> 3743.52]  point using someone's built-in format because you might need it in milliseconds or you might need it
[3743.52 --> 3747.60]  in something i mean there's just like weird things to consider that if you don't roll your own you
[3747.60 --> 3752.64]  don't have control over i don't know i know time was only one example but yeah i think it's an
[3752.64 --> 3760.72]  unpopular opinion among c++ dubs i think c++ dubs will stab you in the front and the back over the
[3760.72 --> 3767.76]  sentiment but yeah i i can i can get on board with this i mean there's the related opinion that time
[3767.76 --> 3773.28]  zones were a mistake that's not unpopular among programmers but i mean i will say it kind of does
[3773.28 --> 3778.40]  play into like a little repetition is better than a little dependency which is not supposed to be
[3778.40 --> 3784.72]  unpopular it's one of the go you know forget the word proverbs so it feels like that i get a lot of
[3784.72 --> 3792.08]  pushback whenever i throw this idea out but maybe you don't need an external dependency to send a time
[3792.08 --> 3800.16]  over the wire like you could just do it yourself and it doesn't seem to go over well and angelica did you
[3800.16 --> 3808.08]  grow up in utc yeah when did you learn about other time zones when when i was young and i moved to the
[3808.08 --> 3815.36]  us oh okay they're horrible i hate them no i i've actually ironically spent the least time of my life
[3815.36 --> 3821.68]  in london and in england i spent the rest of my life in other places so you see my beloved
[3821.68 --> 3831.68]  i'm in i'm in central time in louisiana and it's company i used to work for had a customer in arizona
[3831.68 --> 3839.44]  who chooses not to do daylight savings time okay and scheduling is really fun on the border between
[3839.44 --> 3846.24]  arizona and new mexico when five minutes down the road it may or may not be an hour different
[3846.24 --> 3852.96]  time zones were a mistake okay time zones were a mistake i just implemented a distributed scheduler
[3852.96 --> 3860.48]  and we had to consider these kinds of things so yeah fun stuff all right we'll see what the masses
[3860.48 --> 3867.20]  think of what the what i think was two unpopular opinions so i'm great very very great i don't think
[3867.20 --> 3873.36]  this group found them all that unpopular but maybe the mass as well we'll wait and see does anyone else
[3873.36 --> 3878.32]  have an unpopular opinion that they would like to share since we were talking about c++ and other
[3878.32 --> 3885.20]  languages earlier uh mine is that go like seago has performance issues i don't think that's a
[3885.20 --> 3891.76]  particularly controversial take but goes kind of shaky interrupt with c is i think actually a good thing
[3892.64 --> 3899.12]  because it has forced us to not have to depend on a lot of popular libraries much of which are
[3899.12 --> 3905.28]  kind of garbage at this point like there are a lot of really bad c++ libraries out there or
[3905.84 --> 3913.04]  c libraries that people have just defaulted to for things like uh ssl or like parsing xml and things
[3913.04 --> 3919.36]  like that and uh you know interop with c is very useful at times but it's kept i think it's kept go away
[3919.36 --> 3925.92]  from a lot of trash dependencies and i say this because i've been i've been noodling with zig for the past couple of
[3925.92 --> 3931.68]  weeks for one reason or another and like and we we really got off easy with with much simpler builds
[3931.68 --> 3938.40]  not having to depend on so much c libraries as someone who's had to deal with quite a bit of seago
[3939.04 --> 3947.84]  i concur 100 like it's kind of a good thing that it's hard because lots of people are like oh i can just
[3947.84 --> 3954.48]  use seago but you could also not yeah at this point i almost always prefer the not there's a few
[3954.48 --> 3962.32]  exceptions but yeah i work in a weird place where sometimes we need weird stuff and i'm not attacking
[3962.32 --> 3968.48]  your opinion let me start off and this is a backdoor agreeing with your opinion i mean you can disagree
[3968.48 --> 3973.84]  to jacob like this is the spicy segment oh i will i will disagree with a lot more okay i'm ready
[3973.84 --> 3982.08]  like crypto phips like the crypto phips library doesn't exist in go and even microsoft had to like
[3982.08 --> 3991.76]  go create their own and it's binding to open ssl sort of and and there's there's huge gaps and the go
[3991.76 --> 3998.96]  packages themselves are great and and solid crypto itself is super solid now it's just not as big as it
[3998.96 --> 4003.12]  needs to be there's not enough people working on it and that's where there's a lot more people that know c
[4003.84 --> 4008.88]  versus there's a lot of people who know go yeah i mean with crypto in particular like frankly i would
[4008.88 --> 4014.08]  prefer to use stuff that i know is written by people like filippo and roland and super well tested
[4014.08 --> 4019.20]  and usually like more than once they found bugs with the reference implementations and see because they
[4019.20 --> 4024.32]  had to re-implement it and that stuff wouldn't happen if interop was seamless the way it is with other languages
[4024.32 --> 4034.00]  slightly related to that speaking of filippo and crypto the regressions in 120 that he fixed in 121 and
[4034.00 --> 4041.68]  talked about at gopher con this year yeah those were fun at work we have a few systems that spend a lot
[4041.68 --> 4050.40]  of time verifying public private keys and things did not go well when that regressed like it did
[4050.40 --> 4056.08]  well good job that they fixed it his talk was really good yes i went in personally shook his hand and
[4056.08 --> 4061.84]  thanked him at the conference filippo's talk was really great and whenever it's uploaded to youtube but
[4061.84 --> 4066.40]  definitely recommend it for everybody but one thing that stuck out to me was that he didn't use speaker
[4066.40 --> 4070.96]  notes at all he wasn't even standing in front of the podium he just kind of like riffed for 30 minutes
[4070.96 --> 4075.04]  straight with what i'm pretty sure was very little prep it's you can just ramble about that stuff for
[4075.04 --> 4080.96]  a really long time and no one cares because they all like to listen to him i will say filippo is the king
[4080.96 --> 4088.88]  of preparing like crazy and then coming across so laissez-faire so like i'm just talking it's chill
[4088.88 --> 4097.84]  um so huge props i want to emanate that kind of um speaker confidence in the future yes life goals
[4097.84 --> 4105.12]  as a speaker cassie i feel like you had one i have one but y'all's were like so hard tech and i couldn't
[4105.12 --> 4110.40]  think of like so many and then one just came to me as i was drinking my water it's like a work
[4111.04 --> 4118.72]  life health balance thing so like related but mine was i'd rather carry around a gallon
[4118.72 --> 4124.80]  jug of water everywhere i go rather than filling up a cup because i never get up from my desk i'm
[4124.80 --> 4132.24]  always at my desk so now like i just stay at my desk i stay hydrated but i don't think other people
[4132.24 --> 4138.16]  like to carry a gallon jug do you have one of those like monster bottles that look like the size of your
[4138.16 --> 4145.04]  head i would concur i don't want to carry a gallon of water everywhere yes unpopular yeah it doesn't
[4145.04 --> 4151.04]  really fit in the cup holder in my car that's the problem yeah you have to prop it up that's what
[4151.04 --> 4157.44]  baby seats are for exactly strap it in you put it on the passenger seat and the little automatic
[4157.44 --> 4162.56]  system thinks there's someone there then starts dinging at you to buckle the seat belt well then
[4162.56 --> 4167.04]  it rolls onto the floor and you can't reach it and you get in a car accident and that doesn't work
[4167.04 --> 4175.36]  just downsides all around before this gets too dark um we are coming to the end of our time together
[4176.00 --> 4183.76]  does anyone have any final burning unpopular opinions i don't want to cut us off so ever since go
[4183.76 --> 4192.16]  1.13 was released i think checking on errors has become intuitively worse and i hate it in the past it was
[4192.16 --> 4198.96]  easy to do a switch case on errors i call an api i do a switch case i've got five different errors
[4198.96 --> 4205.60]  going back bingo bango call out the functions and now i'm doing this errors is i've got to like it's
[4205.60 --> 4211.60]  not great i don't it could be easily implemented in the switch case that oh you're an errors i'm gonna
[4212.72 --> 4219.84]  avoid errors is and just have the errors listed so that's my unpopular opinion if you standardize them
[4219.84 --> 4228.64]  and listen to my talk it could be a little easier cassie has solved that problem for you done it's open
[4228.64 --> 4236.64]  source please use it awesome well that actually brings us to a close from this episode it's been
[4236.64 --> 4243.20]  an absolute pleasure to spend this kind of hour or so with you all again i will encourage all you
[4243.20 --> 4249.52]  lovely listeners to go and watch the lightning talks and if you are interested in giving a lightning
[4249.52 --> 4255.68]  talk i feel like we've left you with a few little tips and tricks uh to set you up for success so
[4255.68 --> 4261.36]  thank you all again have a wonderful weekend thank you for spending your friday with us at go time
[4261.36 --> 4266.96]  and uh goodbye all thank you thanks thank you bye everyone bye
[4266.96 --> 4276.00]  that is go time for this week thanks for listening subscribe now if you haven't already head to go
[4276.00 --> 4284.16]  time.fm for all the ways or simply search for go time in apple podcasts spotify or wherever you get
[4284.16 --> 4290.88]  your podcasts you'll find us also check out some of our other shows if you want more developer focused
[4290.88 --> 4298.40]  podcast goodness the changelog jsparty practical ai and ship it are all worth at least one listen
[4298.96 --> 4305.36]  thanks once again to our partners at fly.io to our beat freaking residents breakmaster cylinder and to
[4305.36 --> 4312.40]  our longtime sponsors sentry use code changelog at sign up and save yourself 100 bucks off a sentry team
[4312.40 --> 4326.40]  plan why not right that is all for now but we'll talk to you again next time on go time
[4334.88 --> 4335.44]  game
