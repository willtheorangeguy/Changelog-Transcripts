[0.00 --> 13.72]  welcome back everyone this is the changelog we're a member supported blog and podcast
[13.72 --> 17.26]  that covers what's fresh and what's new in open source you can check out the blog at the
[17.26 --> 23.08]  changelog.com and our past shows at 5by5.tv slash changelog the show is hosted by myself
[23.08 --> 29.02]  adam stakoviak and andrew thorpe so andrew in your echoey way say hello hello coming straight
[29.02 --> 36.88]  from my new empty and echoey office yeah you just uh you just moved right to nashville get your house
[36.88 --> 43.44]  that's awesome music city usa speaking of music you can tune in live every tuesday that's today
[43.44 --> 48.30]  at 5 p.m central standard time right here on 5 by 5 to listen to this show this is episode number 94
[48.30 --> 55.66]  and we're joined today by the awesome awesome hampton cotton and uh he's the inventor as you say
[55.66 --> 60.06]  hampton of sass and ham which i think is a really cool way to to talk about how you created some
[60.06 --> 65.06]  software and you're also the maker of wikipedia mobile which you uh talk about uh quite a bit
[65.06 --> 69.12]  in different talks and i think it's a unique story you have there too so welcome to the show
[69.12 --> 76.08]  yeah thanks guys it's awesome to be here so uh i think we've been i think i've personally been
[76.08 --> 80.10]  waiting to have you on the show since like episode number two so the episode number two of the changelog
[80.10 --> 85.16]  was was uh nathan and chris we talked about sass compass and stuff like that and i've been
[85.16 --> 90.54]  a user of sass for years and stuff like that we got a chance to hang out at less conf and that was
[90.54 --> 96.02]  that was awesome i think uh i didn't have a different opinion of you before then but i definitely liked
[96.02 --> 102.52]  you a lot better afterwards i don't know why so don't take anything hard from that um but i guess for
[102.52 --> 107.44]  the uninitiated on on who you are i kind of said you were the inventor creator of sass and ham one some
[107.44 --> 112.76]  other stuff but when you introduce yourself how do you introduce yourself yeah it's i mean well
[112.76 --> 118.18]  usually i say hi i'm hampton but i don't normally like i'm on the media i'm like hi i'm hampton i'm
[118.18 --> 125.86]  the don't you say hi i'm the hampton i'm the hampton yeah hampton yeah so tm yeah um definitely that that
[125.86 --> 131.00]  moniker is a difficult one because nathan and chris have been maintaining the nathan's been involved
[131.00 --> 137.36]  pretty much since day one uh and chris has been involved for i think five years now and they do all the
[137.36 --> 144.52]  hard work on keeping sass awesome and adding all the amazing features and um you know so i def i did
[144.52 --> 151.82]  the first version uh the first commits mine the kind of concept was mine the like pre-compiler idea um
[151.82 --> 156.86]  that was actually there wasn't really anything like that like it's pretty common now with you know
[156.86 --> 161.32]  coffee script and a bunch of kind of other alternatives but um you know that was the really
[161.32 --> 167.40]  crazy idea because i think back then i was i was doing rails full-time and uh you know people were
[167.40 --> 172.90]  asking a lot like how do i do dynamic css they really want to do like you know theming or user
[172.90 --> 178.22]  picks a color for some reason like that that kind of um customizing css and i remember when i first
[178.22 --> 185.08]  started sass um that's what people thought it was for the longest time um they they were like oh so let
[185.08 --> 189.60]  me do custom themes for my users i'm like yeah it's not dynamic it's actually compiled and then you know
[189.60 --> 194.60]  it's just css that goes up um you know and it was like variables and some other basic stuff and
[194.60 --> 200.28]  nesting um but you know all the crazy stuff that's out there now that's you know nathan and chris are
[200.28 --> 206.04]  just absolutely insanely awesome at that stuff um and i have to be honest the most advanced
[206.04 --> 213.20]  usage of sass these days i'm not very good at it um i i mostly use you know i'm a really good the
[213.20 --> 217.76]  book i wrote on it the pragmatic i just asked the end of that book's a basic basically the end of
[217.76 --> 223.04]  what i use day to day um in the language so i haven't got a chance to dive deep into that book
[223.04 --> 226.52]  but i've been wanting to pick it up for a while but now that you mentioned it's pretty basic i might
[226.52 --> 232.14]  just skip it yeah no it's it's not it's true uh no it's definitely i'm just messing with you
[232.14 --> 237.46]  well we kind of did it because the the story that like i keep hearing from people is you know
[237.46 --> 241.72]  oh like i've been i'm at this company i really want them to use sass but i can't convince anybody
[241.72 --> 246.44]  to like take a look at it right um and so the idea was just to have a really thin really simple
[246.44 --> 252.24]  book that just taught you very quickly how to kind of be dangerous with sass so how many pages is
[252.24 --> 258.00]  then oh gosh i don't know i guess it's digital right so is there really pages no no this is a
[258.00 --> 263.62]  physical i got the book right here yeah it's pragmatic programmers um yeah it's let me see 90
[263.62 --> 268.72]  i think 100 pages no yeah i mean it's a sizable enough yeah it's a pragmatic guide so it's
[268.72 --> 272.68]  really quick and kind of like each page is like an example and that's really how it teaches you
[272.68 --> 276.72]  i like the way you did that book too you kind of had it in this beta form and you were releasing i
[276.72 --> 282.28]  think chapter every couple weeks right and um it was pretty neat to to kind of go that route too and
[282.28 --> 286.38]  you didn't take that long to write it out there was a fairly quick one i know there's another book
[286.38 --> 291.16]  out there that's taken a while and there's well there's anyways there's actually that's a deep
[291.16 --> 294.66]  topic there oh sorry well there's about four or five books there's actually one in french which is
[294.66 --> 300.94]  is there really yes wow yeah that that's my favorite one it's by i'm wild by french books
[300.94 --> 305.58]  but just didn't realize that there was a french sass book yeah and ben frame just came out with
[305.58 --> 310.28]  one i think also so um but yeah nathan and chris have one they've been working on for a while so
[310.28 --> 317.58]  um we'll see how that comes out i feel like there's um you know so what i want to do with this
[317.58 --> 322.08]  conversation and you know andrew you're you're a full stack kind of guy too so you definitely play in
[322.08 --> 328.08]  this world as well but i kind of want to discover i guess not the entire time talking about sass but
[328.08 --> 334.02]  i wanted to talk about a lot about it i guess but not the entire time about that and uh hamill too i
[334.02 --> 339.32]  think it's really neat just to just how you um you know you use the word i think now you change it
[339.32 --> 343.28]  you say creator now i just realized that but for a while there you were seeing inventor of but which
[343.28 --> 346.96]  i always thought was kind of neat well i think i stick mostly with inventor i don't know probably
[346.96 --> 353.12]  it's just hard right like yeah i always flip back and forth i don't know if it's i mean i think
[353.12 --> 356.94]  when i've talked to you about it you're always pretty humble like we had a chance to chat at
[356.94 --> 363.42]  lessconf and i was pretty cool to just riff about sass and some neat stuff and there's some there's
[363.42 --> 369.22]  some parallels to some feelings we have about the community and what can be done and um some likes
[369.22 --> 374.24]  and dislikes and stuff like that nothing in particular but just in general we have some parallels but
[374.24 --> 383.22]  i think what's neat about sass is is that people don't realize how uh how old it is really like a
[383.22 --> 388.32]  lot of newcomers maybe the last you know one to two years maybe three years i've started to use it
[388.32 --> 394.34]  and i've adopted it but this is like six and a half years old now maybe seven years old now i think
[394.34 --> 399.32]  november is gonna be the seventh birthday of sass the first right commit right that brings up the
[399.32 --> 403.86]  other thing i was was uh i think it was like november 5th i looked at the commit date and the
[403.86 --> 408.90]  hamlet gem because it was mixed with hamlet first right yeah yeah it was um it was kind of a
[408.90 --> 416.54]  side crazy idea i had to like just and i convinced nathan to help me right build it as like an add-on
[416.54 --> 423.14]  kind of thing um it's definitely eclipsed um hamlet generally um but yeah and actually on on november 5th
[423.14 --> 429.24]  so the company i'm at now uh move web we're actually going to throw a sass birthday party here in san
[429.24 --> 433.58]  francisco and so we're gonna be doing we're gonna like invite the community um who want to come so
[433.58 --> 438.46]  that's actually be pretty fun i think well you know that i'm the owner of sassday.com right
[438.46 --> 444.72]  we'll have to use that that'd be awesome that would be awesome it'll be sass day not not a sass birthday
[444.72 --> 450.66]  it'll be a birthday but it'd be sass day yeah it'd be pretty awesome yeah it actually when hamel is a
[450.66 --> 455.34]  year old i think before we start on sass maybe a year and a half so that's almost coming up on eight
[455.34 --> 463.30]  years i think so when i the reason why i bring up the the longevity there is that uh a while back
[463.30 --> 468.38]  i haven't done the talk in a while but for a bit there two years straight when and i um you know
[468.38 --> 473.02]  we started this podcast a while ago and we were doing this talk called design eye for the dev guy
[473.02 --> 478.36]  and gal so uh all you ladies out there we we were saying gal you can go back on the slides it's really
[478.36 --> 485.32]  neat we put a little slash there and gal but um uh we were one thing we were seeing in one of
[485.32 --> 489.00]  the slides we were doing this talk it was actually kind of training more than it was a talk it was
[489.00 --> 495.12]  eight hours of training um and we did this and it was like you know the primer into design theory and
[495.12 --> 502.14]  sass and compass and html5 and css3 and a bunch of other fun stuff but um one thing i was uh really
[502.14 --> 507.64]  reminding people of was that like you know you mentioned getting people to adopt it and that was
[507.64 --> 511.62]  part of the reason why you had said what you said in your book and keeping it short and kind of making
[511.62 --> 518.18]  it um you know like this beginner's guide for lack of better terms um was one thing that was hard to
[518.18 --> 524.52]  to convince people of was that sass wasn't new it wasn't like it was you know all they just heard
[524.52 --> 529.04]  about it but it this thing has been there for a while so it's a mature project with some mature
[529.04 --> 534.04]  people behind it that really have some very insightful thoughts and like there should be no reason why you
[534.04 --> 538.86]  shouldn't trust it you know that's why i kind of harp on the six and a half almost seven years old so
[538.86 --> 543.82]  yeah you know it's definitely like uh you know less being done in javascript but you know less
[543.82 --> 550.90]  being the kind of competitor um it came out you know it's relatively young um and you know it being
[550.90 --> 555.40]  in javascript when they did that port it kind of exploded in popularity because it hit right when
[555.40 --> 559.58]  you know javascript frameworks were kind of exploding and it's like oh this is in javascript too
[559.58 --> 567.40]  my whole world's in javascript man right um and uh so uh but i like it when i hear people say oh
[567.40 --> 573.20]  so sass is like it's it's like kind of like less right like you kind of copied what less did
[573.20 --> 582.20]  no i'm like oh yeah that's that's where you put your inventor hat on right yeah um no but uh
[582.20 --> 586.76]  so yeah i definitely talk about the age too because i think most people don't know how old it is i mean
[586.76 --> 592.50]  it lived for a long time it was only using the rails community it was part of a hamill project hamill is
[592.50 --> 599.08]  definitely a markup language that you either love or hate or love to hate um and uh just i i always
[599.08 --> 602.98]  try to tell this people if if i meet you at a conference uh i don't want to hear what you think
[602.98 --> 609.02]  about hamill let's talk about anything else i just don't need to know your opinion um are there a lot
[609.02 --> 614.72]  of negative opinions about hamill yes it's just always a whole talk that i have like three three
[614.72 --> 619.32]  times a conference are you upset if i have some questions around hamill then no because we have a
[619.32 --> 624.74]  whole audience of people who we can address all at once about it um that's right getting get them all
[624.74 --> 629.90]  done at once right yeah shoot me an email if you have questions uh no i actually the part that's funny
[629.90 --> 635.94]  is that people think i'm really sensitive about it um like i'm not like but they kind of come up to me
[635.94 --> 643.90]  oh you know i hate to tell you i really don't like hamill okay thanks all right i'm super sad
[643.90 --> 649.28]  no i'm just like you've ruined my day oh i'm uh that's cool the you know and then somebody's like
[649.28 --> 654.50]  uh somebody tweeted the other day they were like i have to admit sometimes i still use erb templates
[654.50 --> 661.26]  for some things and i'm like so do i like this isn't a big deal it's fine i have a confession i
[661.26 --> 666.20]  actually uh i'm working on a rails project just uh learning ruby and stuff like that and
[666.20 --> 672.80]  getting uh getting more in-depth at it and i actually stopped i got i've always been a big fan of
[672.80 --> 678.94]  hamill and so i hope you don't make you cry when i say this but i've gone back to erb how dare you
[678.94 --> 684.42]  how dare i he just got finished telling us how sensitive he is about hamill i'm gonna cry um
[684.42 --> 691.56]  no it's funny so you know a lot of times the stuff i work on um like i definitely tend to originate
[691.56 --> 697.54]  things and then let smarter people than me come in uh if they get traction and more responsible people
[697.54 --> 705.24]  than me also um but uh you know i'm always looking for those ideas that are kind of really challenging
[705.24 --> 711.50]  i definitely like i have a lot of opinions that don't necessarily always match what's popular as
[711.50 --> 717.54]  matter of fact some of my opinions will be based around um disliking what's really popular uh i had
[717.54 --> 721.20]  a really popular video that went around at some point about me just ripping into test driven
[721.20 --> 726.54]  development and uh like you know and that kind of i like that it kind of offends people and makes
[726.54 --> 731.58]  them have to take their position and uh like hamill's definitely if the people out there listening
[731.58 --> 740.56]  haven't seen it it's um very stark it's it's very concise it's a way to write html templates that's
[740.56 --> 747.66]  very heavy on semantic html so um it's kind of designed to be a pain uh to not write good classes for
[747.66 --> 753.52]  things um when it was you know it was designed in you know was it 2004 something like that um 2005
[753.52 --> 759.80]  and uh you know that's when you know i was the other developers i was working with weren't using
[759.80 --> 764.52]  classes and they was getting to our design team and they um were getting very frustrated because
[764.52 --> 769.44]  there were all these spans and divs randomly kind of on a template and an erb template and they
[769.44 --> 773.96]  weren't styled right and it just kind of looked all crazy and you know they just dumped data out
[773.96 --> 780.64]  um and i kind of wanted to design the language to kind of force people to do good habits for
[780.64 --> 788.34]  semantic html um and to really focus on structure and layout but like it's definitely not meant to be
[788.34 --> 792.72]  like a beginner tool and as a matter of fact when i first presented it i thought everyone was just
[792.72 --> 798.40]  going to hate it uh it was a total hairy like hail mary to give that out to the world i kind of just
[798.40 --> 803.02]  thought i was the only one who ever used it um so the fact it is still use this that you've been
[803.02 --> 807.34]  using it up till now is pretty amazing um but i was just kind of hoping it would stir a bunch of
[807.34 --> 812.58]  other innovation and i mean it took a while but i there's definitely a lot of kind of things that
[812.58 --> 818.96]  have taken similar approaches being kind of white space sensitive um you know kind of minimum like
[818.96 --> 825.04]  now it's like data attributes trying to make that more concise more simple um so i'm proud that that
[825.04 --> 830.78]  kind of happened uh that you know there's slim and stuff i think are now kind of gaining traction
[830.78 --> 836.22]  and that's awesome that's totally the natural flow of technology i'm just happy to come in with my
[836.22 --> 841.40]  crazy idea and you know push people to question what they were doing before i think it's cool though
[841.40 --> 846.10]  man to have uh and you know just a crazy idea and that's why i thought it was kind of neat like for a
[846.10 --> 852.66]  while i was like inventor huh and i was like oh inventor oh that makes sense i mean because i mean
[852.66 --> 859.02]  software is an art and it's not just uh you know propeller head kind of stuff it's it's you know it's very
[859.02 --> 865.32]  much a canvas and you know that is a pretty wild thing like even if it's not the most artistic
[865.32 --> 872.10]  code i mean the what it does is really unique and it it shifted a lot for people and it i would even
[872.10 --> 877.88]  say that hamill and sass uh i'm not sure if they're exactly responsible for but they definitely started
[877.88 --> 885.04]  a movement of pre-compiling and you know this meta level on top of something else so sass on top of css
[885.04 --> 891.56]  and hamill on top of html i mean i think it started this little movement so to speak i mean i hope it
[891.56 --> 896.62]  like that is the thing like if i'm most proud of myself or something it is that there are competitors
[896.62 --> 901.26]  and like seeing coffee script like i i kind of had proposed a thing called jabble years ago at a
[901.26 --> 907.38]  conference um and i never really got to finish up the project but it was kind of like a coffee script
[907.38 --> 914.38]  like thing um to like make just really straightforward event-driven javascript um it was a little i mean it's
[914.38 --> 918.34]  different but the you know it was kind of applying the same principle um so i mean if i had any positive
[918.34 --> 924.02]  effect in any of that stuff that's awesome because coffee script's really really cool um and uh yeah
[924.02 --> 930.74]  i mean i think inventor is kind of the way i think of myself to be honest but just because like i like
[930.74 --> 934.48]  to look at problems and i like to try to come up with solutions that other people haven't thought of
[934.48 --> 941.02]  that later when you look back you're like well that's obvious um that's my favorite like if i that's my
[941.02 --> 947.86]  main joy in life uh is it is now that like i feel like people do look at sass and go well okay yeah
[947.86 --> 953.98]  i mean that that must have existed like somebody did that right those are my favorite favorite products
[953.98 --> 961.00]  too is when you're like wait this doesn't exist oh um well people are pretty diehard fans too of
[961.00 --> 968.28]  both of these things we're talking about sass and hamel like those who love hamel really love hamel
[968.28 --> 977.36]  and those who love sass like really love sass in fact um a couple years back um me and john long and
[977.36 --> 984.58]  a couple others got together and started this i guess uh blog i guess on uh on sass called the
[984.58 --> 990.30]  sass way and it was a riff on the ruby way and the rails way and so you know they kind of set the
[990.30 --> 996.26]  track in terms of the name but we thought like there's some there's some positive graceful arrogance
[996.26 --> 1001.80]  when it comes to the sass way in quotes you know okay yeah because i think there's you know there's
[1001.80 --> 1006.34]  the way you'd write it in css and that's kind of like kind of stupid in a sense because why would you
[1006.34 --> 1014.68]  waste so much time you know handcrafting that css whenever you can let sass do the indentation for you
[1014.68 --> 1020.10]  and make your output beautiful or condensate and or you know to decompress or compress it down or
[1020.10 --> 1025.52]  whatever you know whatever your flavor might be sass could help you do that so there was this level of
[1025.52 --> 1032.24]  arrogance when it came to like to to this i guess just using this i mean how do you feel about
[1032.24 --> 1040.34]  people being so diehardly uh appreciative and and just stoked about using sass or ham when like
[1040.34 --> 1047.42]  almost fighting to the tooth and nail about it sometimes i mean clearly great like i mean it's
[1047.42 --> 1053.30]  pretty awesome i am looking for i haven't seen it my first sass tattoo yet but i'm sure somebody will
[1053.30 --> 1059.40]  get one one day um yeah no i mean it's really really cool to see people be so passionate um and
[1059.40 --> 1065.84]  i think the the iconoclastic kind of elements especially earlier on i mean these days you know
[1065.84 --> 1070.50]  especially sass it's just more accepted i think there's less you know bare knuckle fights required
[1070.50 --> 1075.34]  um you know here in the valley i just like linkedin's using i mean that's why chris epstein
[1075.34 --> 1079.22]  i recently got a job with linkedin they're they're kind of officially supporting sass uh
[1079.22 --> 1085.58]  um sorry i know yelp is using them as using it a lot of the big companies here just they'll kind
[1085.58 --> 1090.68]  of silently think they're the only ones doing it and are now internally using it um so i mean and
[1090.68 --> 1094.44]  that's just so cool to me there's like kind of these secret companies right now that are all using
[1094.44 --> 1100.28]  it internally not really telling anyone um and i mean i think because they're initially challenging
[1100.28 --> 1104.96]  ideas that's why people take it on as a as a belief you know and that's why they get so passionate
[1104.96 --> 1109.76]  about it because they don't understand why other people don't understand and that's i don't know i
[1109.76 --> 1116.46]  think it's really cool so uh there's tons of stuff we could talk about but i'm really curious about this
[1116.46 --> 1123.16]  and i've heard you talk about it elsewhere but uh sass and ham were both kind of iconified i guess in a
[1123.16 --> 1129.92]  sense by this imagery that came with it uh you got the dude with the with the muscles right you got the
[1129.92 --> 1135.06]  girl with the phone in her hand and uh especially when we did the sass with her like people new to
[1135.06 --> 1141.90]  sass are like why is your icon a girl talking on the phone you know and and and we're like and why
[1141.90 --> 1146.68]  is it you know this pinkish purple what's the tones and what are all these choices made you know
[1146.68 --> 1151.42]  why did you make these choices and i'm like well i'm just following the groove you know um i didn't
[1151.42 --> 1156.76]  choose the girl i mean she's sassy though right and then you got the dude who's hamley's kind of got
[1156.76 --> 1161.60]  this uh you know he's got his little muscles out there and he's he's flexing so what's what's the
[1161.60 --> 1166.46]  deal with the images where they come from so it definitely started with the the kid i had a photo
[1166.46 --> 1172.42]  that i found at a yard sale of this uh it was like a 1950s kid and he's on his pad like his porch
[1172.42 --> 1177.92]  and he's probably like eight years old he's got his dad's boxing gloves on and they're oversized and
[1177.92 --> 1183.78]  he's kind of like trying to pose at the camera like he's fighting and uh that was when i i just loved
[1183.78 --> 1189.18]  that picture i bought it immediately i still have it um because i just love this idea of kind of in a
[1189.18 --> 1195.36]  sense and having a weird idea like standing up for something and kind of i don't know i just thought it
[1195.36 --> 1201.56]  was really adorable and i don't know i felt like there was a lot of me in that picture um and so we
[1201.56 --> 1208.20]  were i was working with uh lucas dria who's a designer um color.me i think is the name of their
[1208.20 --> 1214.72]  uh his design firm in in toronto um and he he helped on the original design of the hamill site
[1214.72 --> 1222.10]  and he had like a bunch of um kind of open source or not open source uh was it public domain images
[1222.10 --> 1227.42]  and that was one of them and i was like oh that's that's what i wanted that's the that's the same
[1227.42 --> 1234.02]  spirit in that kid that i saw in the other photo um and i think actually the when i look at them
[1234.02 --> 1242.10]  uh the core thing is being mischievous um that's the idea to me like that that's the heart of that
[1242.10 --> 1248.96]  kid he's like he's kind of showing off but it's kind of like a cheeky um mischievous way um and then
[1248.96 --> 1254.12]  i don't know so yeah i also i picked the the woman's photo of her on the phone
[1254.12 --> 1262.02]  i honestly i've been asked this question a lot and i just really liked the photo i mean i it looked a
[1262.02 --> 1267.94]  little mischievous i thought she looked cheeky i thought it was kind of fun um i thought i didn't
[1267.94 --> 1277.00]  want to with a name like sass i i thought it would be kind of interesting to i don't know like play with
[1277.00 --> 1283.08]  gender roles maybe um it i definitely know some people have been offended by it it's it's i'm a
[1283.08 --> 1290.62]  pretty strong feminist uh i know guys can kind of be feminist um yeah so you know it's so funny to me
[1290.62 --> 1295.80]  when i hear people say oh i you know it's offensive to me um and you know that's definitely
[1295.80 --> 1299.66]  not the intention the new design doesn't have that it's not meant to kind of offend anyone
[1299.66 --> 1304.40]  but i just kind of thought like she seemed empowered to me she seemed like she kind of had a secret
[1304.40 --> 1308.62]  like there was something mischievous going on um she seemed kind of happy and friendly two at the
[1308.62 --> 1314.24]  same time and that's kind of what i thought um about sass itself and as far as the color i believe
[1314.24 --> 1319.70]  actually nathan picked um he just took the hamil site and then like picked a color and threw it on top
[1319.70 --> 1324.34]  of the photo that i sent him um so i don't really know why i went with that color i don't really like
[1324.34 --> 1329.12]  that color to be honest it kind of drives me crazy but that's that's why the the never-ending uh sass
[1329.12 --> 1335.12]  redesign is going on yeah so when is that gonna what does that look like for the sass redesign because
[1335.12 --> 1340.44]  the hamil you're not you i don't ever see the boy anymore on hamil no no that uh it's gone
[1340.44 --> 1345.84]  slingshot now so yeah that got redone um yeah so what about sass when's that gonna
[1345.84 --> 1352.62]  one second drop so there is i can send out the link i mean the main thing is uh so uh burman painter
[1352.62 --> 1358.86]  and gina bolton have been working uh really hard on it and basically they they did all this work to
[1358.86 --> 1364.68]  kind of flesh it out and uh i mean i think it basically as all kind of open source design projects
[1364.68 --> 1371.70]  happens people get distracted um and you know i think the initial version they were trying to do a
[1371.70 --> 1377.32]  lot more tutorials a lot more kind of interactive uh information share like it was they were trying
[1377.32 --> 1383.44]  to make it um not just a better design but better content is kind of a central place to go to learn
[1383.44 --> 1388.44]  about sass um and i think it's that content part that was the biggest struggle to actually get all
[1388.44 --> 1393.14]  that written and put in there um a couple weekends actually uh my husband michael and i spent
[1393.14 --> 1399.84]  like a weekend and we kind of went through and since we did the sass book and um we're also
[1399.84 --> 1404.02]  working on material we're working with treehouse right now actually uh to put together a sass module
[1404.02 --> 1410.42]  for that and uh so we're like okay fine we'll come in and help with some of the content um so hopefully
[1410.42 --> 1417.32]  soon uh i've been bugging gina about it we'll see um i mean honestly i even i think as it is right now
[1417.32 --> 1423.12]  not completely polished it's still better than uh the current site which we just need to kill
[1423.12 --> 1428.28]  that's kind of my position um and you know once you get something up there it's easier to iterate
[1428.28 --> 1434.22]  you know like kind of it forces you because people are looking at it but i think there's a lot of
[1434.22 --> 1439.54]  pressure because the site's been so ugly and the competitors have all had really nice websites
[1439.54 --> 1443.70]  that you kind of don't want to put up something that isn't just clearly better do you know what i
[1443.70 --> 1447.96]  mean right like oh all this weight and all this time we said we'd finally make it okay now we've done
[1447.96 --> 1455.30]  it oh yeah the pressure's there to like really deliver now right like you you can't yeah you can't
[1455.30 --> 1461.54]  put up your your draft number one and be like yeah we're gonna iterate yeah i mean it's it's
[1461.54 --> 1467.16]  still looking good though and i think anything better is better so so open source can we talk a
[1467.16 --> 1471.42]  little bit about the i guess maybe i wasn't trying to cut you off that you have more to say that you
[1471.42 --> 1476.60]  were done sorry go go go go um i just wanted to kind of paint a little bit of the history for those
[1476.60 --> 1484.02]  who haven't been closely watching i know you originally started um both of these projects we've
[1484.02 --> 1489.00]  been talking about the hamlin sass you kind of stepped away for a bit and then you came back
[1489.00 --> 1495.16]  we we talked a little bit about this um not last week but the week before we had uh phil up here
[1495.16 --> 1500.62]  from thoughtbot on he's the maker of bourbon maintainer of bourbon that's uh kind of i i'm not
[1500.62 --> 1504.76]  really sure if you would consider it a compass competitor it's just more of like a parallel to
[1504.76 --> 1510.26]  compass just in pure sass but we talked a little bit about just how you stepped away for a bit and
[1510.26 --> 1514.74]  came back so and it sounds like you're a bit more involved in the day-to-day of of sass now is that
[1514.74 --> 1523.02]  right um so the primary sass project um that is the kind of ruby engine and the new language features
[1523.02 --> 1530.38]  um today that's definitely still nathan and chris primarily um nathan has he's at google and he gets
[1530.38 --> 1535.76]  his 20 time to work on that um and you know i mean there's basically so many years of sweat equity
[1535.76 --> 1541.42]  and that and and they know so many of the edge cases um that you know like and and i'm not since
[1541.42 --> 1548.52]  i'm not a super super advanced sass user um you know i mean i try to pitch in on stuff in the forum
[1548.52 --> 1554.42]  but um you know when they're talking about super edge case things i might you know i'm like you guys
[1554.42 --> 1559.46]  are you know this stuff way better than me um but what i've kind of been trying to do so i mean
[1559.46 --> 1566.68]  yeah i left and basically have been um i did a bunch of iphone apps that this is one that got
[1566.68 --> 1574.74]  pretty successful um and uh i did the wikipedia mobile site i ran that for three years um and kind
[1574.74 --> 1579.52]  of was just doing random projects on my own and you know focusing on my career and stuff and you know
[1579.52 --> 1585.16]  they were doing such a good job with it i just kind of you know it was the wayward father um but about
[1585.16 --> 1591.16]  a year i think it's over a year at this point now yeah maybe a year and a half um so the company i
[1591.16 --> 1597.44]  work at move web uh we we're a software tool company and uh there we you know we have a whole
[1597.44 --> 1602.60]  framework for developing mobile sites and it's really a way to transform websites so imagine
[1602.60 --> 1608.96]  css zengarden but where you can actually change the html too um and you can do this on any site on
[1608.96 --> 1614.82]  the internet so um we can you can like redesign hacker news and mobilize it or change it to something
[1614.82 --> 1621.00]  else or make it ugly um it's one of the guys i work with just made a really ugly version um so we
[1621.00 --> 1625.66]  have this tool set and part of our tool set because it's a framework there's like you know you generate
[1625.66 --> 1633.50]  a project so we have uh sas in it and basically having sas we had to include ruby um and our core
[1633.50 --> 1639.34]  framework is no longer written in ruby so we you know ruby is like a 200 megabyte or 300 megabyte
[1639.34 --> 1644.48]  download now so we had this distribution where you know in and in our cloud servers too where we had
[1644.48 --> 1652.08]  this 300 megabyte executable i'm sorry 300 megabyte executable it's free actually um and just kind
[1652.08 --> 1656.70]  of for compiling these sas files and it was slow we had some really big projects and when we were
[1656.70 --> 1663.04]  using compass you know it could take up to 30 to 40 seconds to compile and um so we kind of as a you
[1663.04 --> 1669.24]  know well i kind of decided uh that we had a guy in house who wrote the parser for tritium which is
[1669.24 --> 1677.80]  the language that move web has uh and uh we decided to do the totally insane idea of writing a c and c plus
[1677.80 --> 1685.10]  plus implementation of sas um to basically take those seven years of development of edge cases of
[1685.10 --> 1692.60]  features and try to have one person um redevelop it um so move web has been sponsoring that for the last
[1692.60 --> 1698.96]  year and a half um and every build of our sdk and product has had it embedded for the last year
[1698.96 --> 1705.74]  um but so basically it's called so that's called lib sas and that's the actual c and c plus plus
[1705.74 --> 1714.52]  code um it's designed to be super ridiculously modular um so what you know higher picture when you look at
[1714.52 --> 1722.58]  pre-compiled css languages uh sas is still most people use the ruby version um and most people
[1722.60 --> 1728.34]  don't use ruby so you know at for instance for instance at linkedin they have you know a whole
[1728.34 --> 1734.94]  set of compilers and computers just meant for building sas um actually jonathan lambert there's
[1734.94 --> 1741.44]  this guy who his main one of his main jobs is to keep their compilation farm running of ruby servers
[1741.44 --> 1749.72]  um and it's like this whole infrastructure just because it's kind of slow and in ruby uh and so that's
[1749.72 --> 1754.18]  definitely a downside that people have to do this extra install um switch and get on the command
[1754.18 --> 1757.24]  line and stuff and there's there's apps to help with this but it's hard to have a real development
[1757.24 --> 1761.92]  team we can't just bundle this into eclipse right so they use java they can't just add this quick
[1761.92 --> 1769.44]  thing so you know unless had decided to do javascript which is a great idea because basically every
[1769.44 --> 1773.68]  browser can compile less you don't really have to install anything you can just do it in the browser
[1773.68 --> 1781.44]  so kind of i realized hey we have to do better than that like how do you go past that and that's
[1781.44 --> 1786.86]  by writing a library that has no dependencies that you can just drop into anything and compile it and
[1786.86 --> 1794.72]  it would have sas in it so um it's a collection of like 20 c and c plus plus files it compiles into
[1794.72 --> 1799.92]  something very small you could drop it right into firefox today and build firefox and it will compile
[1799.92 --> 1804.98]  in there doesn't need any dependencies it doesn't use any weirdness we wrote our own parser from from
[1804.98 --> 1810.62]  scratch to make sure that's possible um so the idea is you know what's better than javascript well let's
[1810.62 --> 1816.28]  try c um so that's the lib sas project when you actually look in this is where it gets confusing
[1816.28 --> 1823.90]  people when you go to hcatlin slash lib sas on github um it's just some c files um it's not an
[1823.90 --> 1828.92]  executable it can't actually do anything it's a library itself um and that's where you see uh
[1828.92 --> 1834.58]  aaron leung who's the the guy from moveweb who's a bit working on this um that's where he puts all
[1834.58 --> 1841.02]  of his time reworking that stuff coding it expanding it fixing bugs um and uh it's meant to be compiled
[1841.02 --> 1848.48]  into something else um so there's the other repositories called sas c and it's basically
[1848.48 --> 1854.70]  just a lightweight wrapper um that's an executable so you can actually type sas c when you install that
[1854.70 --> 1860.52]  on your command line and hey you know input output file just like the it's very similar to the um
[1860.52 --> 1866.86]  ruby sas executable that most people use um and they're using a different framework uh and then
[1866.86 --> 1872.54]  we also have some other there's node sas which is compiles into a node server so check we've even got
[1872.54 --> 1878.78]  javascript um so yeah uh andrew nesbitt works on that um and it's basically he just pulls in the
[1878.78 --> 1885.46]  lib sas repo puts the wrapper around it to make it execute within the and compile uh within node
[1885.46 --> 1891.58]  environment and then hey there you go npm module um so that's out uh we there's a ruby one i've kind
[1891.58 --> 1898.34]  of been working on um it's very complicated and i don't have much free time to work on it uh but the
[1898.34 --> 1902.38]  goal of that is eventually that it'd be a drop-in replacement so that you could go into your rails app
[1902.38 --> 1908.54]  comment out import sas and say import sas c and then it would kind of alias itself in and be able to
[1908.54 --> 1914.34]  compile sas files and you wouldn't really know the difference um and so that's there's still more
[1914.34 --> 1920.08]  work to do on that um especially to get full compass support uh because compass uh is not just a sas
[1920.08 --> 1924.86]  library that includes a bunch of sas files it also includes a lot of ruby functions uh that kind of
[1924.86 --> 1932.76]  extend core sas functionality um and you know as today lib sas fully supports bourbon um because bourbon
[1932.76 --> 1938.88]  doesn't do anything um crazy uh compass chris is definitely um part of his job at linkedin is
[1938.88 --> 1944.10]  going to be to help get compass running on lib sas um so at this point there's actually kind of
[1944.10 --> 1949.94]  three companies move web linkedin and google who are all kind of supporting sas development like with
[1949.94 --> 1956.66]  actual office hours and uh and move web it's pretty much a full-time person um so that's pretty cool and
[1956.66 --> 1962.28]  and at linkedin it's a full-time person so you took you have kind of these two divergent paths at this
[1962.28 --> 1967.72]  point right like the original sas path and this new one that you're kind of you know trailblazing
[1967.72 --> 1975.86]  with what is the what a what is the long-term plan for how these two would uh will these two both
[1975.86 --> 1981.48]  continue on indefinitely and if so how or if you know not how is the community of developers that
[1981.48 --> 1987.24]  are working on sas with nathan and those guys um handling the the thought of potentially that not
[1987.24 --> 1992.92]  continuing or you know any thought into that at all so i mean at the moment uh it's definitely
[1992.92 --> 1998.98]  ruby sas is going to continue to be the spec implementation um and they're going to continue
[1998.98 --> 2004.10]  to develop the language there and then the goal of lib sas is to stay um i mean honestly at this
[2004.10 --> 2011.14]  point sas development uh when it comes to features is pretty slow um i mean rightfully so it's seven
[2011.14 --> 2016.34]  years old when when i know when nathan and chris if you see in a comment uh in any of their pull
[2016.34 --> 2021.34]  requests when they're when they're debating whether or not to add a language feature is an extremely
[2021.34 --> 2028.02]  intense and detailed and long debate um going up to nine months worth of debate sometimes um you know
[2028.02 --> 2033.04]  sometimes somebody said something three years ago and then you know it's been still debating and
[2033.04 --> 2038.72]  they're kind of saying you know maybe probably no in that case um but you know it's they take a long
[2038.72 --> 2044.48]  time to consider new language features uh so i mean i i'm actually not too afraid about keeping the
[2044.48 --> 2051.70]  two projects in sync um i mean you know if i think i have a look at this i think there's basically a
[2051.70 --> 2056.92]  sas release every nine months on average i think something like that uh might be a little longer
[2056.92 --> 2064.16]  even um and you know having nine months you know our software product this is really important to it i
[2064.16 --> 2069.84]  have a full-time person we can totally do it um there's there's no plans here but of the the ruby
[2069.84 --> 2073.70]  version nathan and chris are going to continue to work on that chris is definitely um helping out
[2073.70 --> 2079.58]  with lib sas nathan is just sticking with the ruby implementation um and i mean you know as far as the
[2079.58 --> 2084.34]  future i i don't know um but i mean one thing that's really kind of important to me that i'm trying
[2084.34 --> 2092.72]  if you look in the sas c repo um it's hcatlin slash sas c that's with a c sorry s-a-s-s and then the
[2092.72 --> 2099.78]  letter c it's it's it's hilarious right sas c um so there's a big test suite in there and it's
[2099.78 --> 2106.64]  basically i copied all the the tests are in ruby for the sas repo the main one um like they're
[2106.64 --> 2111.36]  actually in a ruby class file there aren't like executable so it'd be impossible for us to run the
[2111.36 --> 2116.90]  test quickly um in a different implementation so i basically pulled those out into files we have all
[2116.90 --> 2122.24]  these input output kind of examples um and you know the goal is we're going to continue it'll
[2122.24 --> 2126.80]  eventually move out of that repo we just have it there because it's a quick place to test but you
[2126.80 --> 2131.64]  know the real goal is to have a whole test suite so that you know if somebody wanted to write a pure
[2131.64 --> 2136.48]  java implementation they'd really be able to you know know that they are behaving correctly and
[2136.48 --> 2143.76]  according to the spec um so that's that's a kind of ongoing bit of work and uh i know that kind of
[2143.76 --> 2148.78]  nathan and chris are definitely up for helping with that um and but we'll we'll eventually kind of
[2148.78 --> 2157.78]  unify everything um when uh when sas revs or gains new features what is it that um what does it look
[2157.78 --> 2162.64]  like to keep the two in sync when you say that like can you give us an example for those who don't code
[2162.64 --> 2166.96]  and see and don't know what you're doing with this but what it takes to keep those two in sync
[2166.96 --> 2176.62]  it takes erin lung um because uh you know c and c plus plus code is very intense and hand coding
[2176.62 --> 2184.08]  um a parser is very intense also um i definitely loop sas is more of a traditional parser
[2184.08 --> 2192.50]  than the the sas implementation i was sorry the ruby implementation uh but yeah i mean basically you
[2192.50 --> 2197.10]  know you end up having to add a feature like keywords to the parser you know if we're going
[2197.10 --> 2202.86]  to match on a new media query or a new you know behavior to extends you know you basically write
[2202.86 --> 2207.54]  the test function we all agree on what the input output should be and then you go into that actual
[2207.54 --> 2214.60]  parser and try to modify the parsing function or the output function to work with it um so it's pretty
[2214.60 --> 2222.18]  it's pretty um hand-holdy it seems like it's very hands-on it's not oh just uh you know import the
[2222.18 --> 2226.76]  new library and call new bindings or something like that and it's it seems like it's pretty
[2226.76 --> 2232.32]  well i mean our goal so we would you know if a new feature gets added it's actually we might
[2232.32 --> 2238.60]  if we see it coming out soon in a sas release we'd probably already be developing it um and then
[2238.60 --> 2242.76]  we'd probably just synchronously release a lib sas update and then all the
[2242.76 --> 2248.92]  try like the adapters that use it like node sas or whatever uh would then go out with the release
[2248.92 --> 2252.62]  and hopefully we're going to synchronize the version numbers on everybody so if you're using
[2252.62 --> 2257.56]  node and you look at your npm package you'll see it's you know 3.4 um and you can know that that's
[2257.56 --> 2265.52]  3.4 um compatible library so that's basically the idea one thing i don't know if you may have already
[2265.52 --> 2271.56]  said this but um with node sas and i think it was it's andrew nesbitt i've actually spoken with him
[2271.56 --> 2278.60]  before but um with node sas and they're kind of coming from the other side right so as things
[2278.60 --> 2285.26]  go into sas you have to kind of keep up with lib sas and keep that in sync uh have you spoken to
[2285.26 --> 2289.58]  andrew about like his experience with implementing node sas because i'm assuming that he's probably
[2289.58 --> 2294.84]  the first other than sas c to actually uh implement a wrapper for the bindings is that
[2294.84 --> 2300.46]  have you actually like heard about his experience or anything um i mean we've talked a little bit i
[2300.46 --> 2307.78]  mean at this point with lib sas you know there's definitely a lot like it's usable today um if
[2307.78 --> 2313.10]  you have a very large very complicated project um that was in pure sas there might still be a couple
[2313.10 --> 2319.14]  incompatibilities um where i mean right now actually we're finalizing a new release i was kind of hoping
[2319.14 --> 2324.70]  to be able to announce it on here but it looks like it's going to be a couple more days um but uh
[2324.70 --> 2330.98]  yeah i mean there's a ton of fixes coming out to kind of edge case stuff um yeah so i mean i haven't
[2330.98 --> 2335.36]  really talked to him the api is super simple though i mean what you actually have to implement
[2335.36 --> 2342.66]  the kind of base stuff um there is so we have uh move web we use go is our primary programming
[2342.66 --> 2349.26]  language so uh there's actually a thing called go sas and so we keep that up so that is implemented
[2349.26 --> 2356.46]  into our framework and kind of you can call go functions to to compile sas um i think there's a
[2356.46 --> 2362.98]  version of web.go which is one of the libraries that supports it kind of natively um so yeah uh
[2362.98 --> 2367.84]  no i mean we've kind of been in touch i know he kind of did as a weekend project and then uh i think
[2367.84 --> 2373.12]  he was looking to to pass the project on um but no i haven't heard wait have you have you heard
[2373.12 --> 2378.26]  something more specific no no i was just wondering what you were saying what you thought but as you said
[2378.26 --> 2382.82]  that i looked at the what i think is the go sas library under move webs github and you're not
[2382.82 --> 2388.70]  lying man that's a pretty simple uh api to to wrap around the whole thing it's like 100 lines of code
[2388.70 --> 2395.62]  yeah there's the the header file has like six functions there's like uh compile a folder compile
[2395.62 --> 2402.10]  a single file and then compile a string that you pass to it and then you know an options object or
[2402.10 --> 2407.46]  something but our goal was to make the simplest stupidest way to integrate where it gets harder is
[2407.46 --> 2414.20]  callbacks that's a thing we've been like so you know sas now in the ruby version allows you to
[2414.20 --> 2422.46]  define functions in ruby um and you know it kind of creates you get past this you know sas colon colon
[2422.46 --> 2428.76]  integer sas colon colon string you know color um and you can manually work with these kind of things in
[2428.76 --> 2434.44]  ruby land um the long-term goal and this is when you if somebody wants to make a super good adapter
[2434.44 --> 2442.98]  um you can actually kind of map the c objects into you know ruby objects or go objects um right now
[2442.98 --> 2448.76]  there's this kind of simple c focused callback library um where you can register custom functions
[2448.76 --> 2454.54]  and that's how we're probably going to get um initial compass support just actually go code it and see
[2455.18 --> 2460.86]  like why not um so you know there's that aspect but yeah so i mean that's when it gets more
[2460.86 --> 2464.30]  complicated but i mean if you actually you know if you're in job and you're like i just want to
[2464.30 --> 2469.58]  compile some stuff um or i want to write my own command line app it's super super super simple
[2469.58 --> 2476.62]  somebody asked in the well that's somebody is um scott killum he asked about
[2476.62 --> 2482.18]  i i guess it kind of becomes a tongue twister too so i'll preface it a little bit with
[2482.18 --> 2489.16]  the fact that uh there's two syntaxes for sas and i know that that's its own freaking debate and
[2489.16 --> 2494.66]  uh i don't even want to go there but sometimes you just have to but so there's there's the newer
[2494.66 --> 2500.08]  version which is more css like which is scss i'm not sure if other people have a different name or how
[2500.08 --> 2505.10]  to say it but i just say scss and then you have the you know kind of classic style right which is
[2505.10 --> 2514.70]  sas and that the the file types are dot s a s s for those listening and dot s c s s for uh sc s but uh
[2514.70 --> 2519.86]  when you did this we're talking about lip sass and the ins and outs of that and go sass and all
[2519.86 --> 2526.18]  that good stuff but um i'm not i'm not familiar with the details around this but the question he
[2526.18 --> 2532.92]  asked was uh you know ham was a simplified syntax and so is uh sas syntax and he's wondering why
[2532.92 --> 2544.04]  you decided not to support the dot sas syntax s a s s so um well first of all uh i hate the name
[2544.04 --> 2552.70]  scss very very much so you're only supporting the sas syntax not sss i hate the name in all caps
[2552.70 --> 2563.14]  scss okay um so uh you know so the initial conversations on sass we were going to make it
[2563.14 --> 2570.08]  more like css um kind of after testing the idea with people i knew like when we were kind of
[2570.08 --> 2573.32]  brainstorming like early you know before we actually started building it most of them were
[2573.32 --> 2579.26]  hamil users and so um since it was kind of part of hamil they were definitely people were like no
[2579.26 --> 2585.64]  no it should look like hamil keep it simple you know i want i want to have hamil in my css um so we
[2585.64 --> 2591.28]  kind of oh and so our then our initial idea was that uh we were going to try to support you know
[2591.28 --> 2598.48]  semicolons brackets and white space um and then kind of nathan came back you know shook his head and was
[2598.48 --> 2605.22]  like no way we were able to support that um so the time we kind of chose to go with a more hamil like
[2605.22 --> 2614.82]  syntax um and that's what you know kind of is the dot sass uh format um then you know we definitely
[2614.82 --> 2621.90]  that's like white space aware it's all space to nest uh you know a property or a rule set you're
[2621.90 --> 2626.16]  going to nest it underneath the previous one so just to make that clear for those listening it's not
[2626.16 --> 2631.36]  very visual well and and actually the thing people don't know so hamil's designed that there's a
[2631.36 --> 2638.38]  the first character on any line is the control character and it basically defines what's going
[2638.38 --> 2643.00]  to happen on that line and the idea is that you can read along the edge of the file and it's white
[2643.00 --> 2648.38]  space sensitive and kind of know what's going to happen um so that's why you know equals space you
[2648.38 --> 2653.58]  know my variable uh the idea is i can kind of look at it and on the left hand side as a developer i
[2653.58 --> 2659.36]  know what's going to happen i'm going to print something out um so actually the original version
[2659.36 --> 2667.44]  of sass it was colon attribute space 20 or you know colon width space 20 pixels um because it was
[2667.44 --> 2672.60]  trying to steal that concept that actually saying colon means i'm an attribute um starting with a
[2672.60 --> 2678.02]  control character um and basically over the years we kind of we heard more and more that you know
[2678.02 --> 2686.16]  having a jarringly different syntax confused people especially people who were not ruby programmers
[2686.16 --> 2693.54]  but were really more css developers um they were used to looking at css all day and when you saw a
[2693.54 --> 2700.14]  different syntax there was a lot more mental switching and learning required um sorry to uh
[2700.14 --> 2705.44]  to understand what sass was so you know at the time if if i was a developer at a company and i said
[2705.44 --> 2710.46]  hey guys i heard of this new sass thing i'm going to convert our project then what you would do is
[2710.46 --> 2715.52]  you know especially the very first version the file would look drastically different than it did before
[2715.52 --> 2721.68]  um and all the other developers and the company would be like hey hey whoa whoa what is this thing
[2721.68 --> 2728.12]  what did you just do um so over time it became very very clear that we had kind of in my opinion
[2728.12 --> 2735.06]  made uh the wrong decision on going make it more hamil-like um and then you know less definitely took
[2735.06 --> 2743.10]  the css-like approach and you know it dawned on us like oh man we've been so stupid here we have uh
[2743.10 --> 2748.86]  you know all the hard work isn't the syntax the hard work is like the engine how it functions the
[2748.86 --> 2754.92]  decisions the edge cases working those edge cases out and we're watching less grow very quickly um
[2754.92 --> 2759.80]  and struggle with the fact that they're a young project and did not they there's a lot of edge cases
[2759.80 --> 2765.40]  even today that less doesn't really cover um and it's kind of their focus is keeping it simpler
[2765.40 --> 2773.34]  uh where sass is really focused on um stability and predictability um like you don't file a sass bug
[2773.34 --> 2778.42]  and then we say oh sorry that's just a quirk we're not going to fix it um typically we're like oh we'll get
[2778.42 --> 2786.80]  to that um so uh you know at least from my perspective it became very clear that uh we needed to move to a
[2786.80 --> 2793.44]  css-like um syntax and uh nathan and chris were definitely on the same page um and this was probably
[2793.44 --> 2798.40]  you know honestly this was the last major interaction that i had with the core project
[2798.40 --> 2806.16]  um and i was proposing that we should just call it sass 3.0 and be like hey sorry after 3.0 the
[2806.16 --> 2812.14]  syntax is different sass 2 or something give it a name um just something you know kind of draw a line
[2812.14 --> 2816.52]  in the sand on something different um but i think their feeling definitely was that it
[2816.52 --> 2821.04]  since it's the same engine and we don't want to alienate our community uh we should kind of have
[2821.04 --> 2828.72]  two syntaxes um and uh i very much disliked the all caps scss as people who follow me on twitter know
[2828.72 --> 2834.34]  i'm the it's sass not sass guy uh it should yeah i can understand that though i mean who i think it's
[2834.34 --> 2842.14]  that's a crazy debate to have itself but i a lot of people do the all caps s a s s because of css being
[2842.14 --> 2849.62]  you know an acronym right yes um yeah i think it's just capital s in lowercase a s s i mean
[2849.62 --> 2855.46]  yeah it's a word but that's how it's spelled well it's a it's a backronym just to be clear so
[2855.46 --> 2862.24]  it there are letter syntactically awesome style sheets but really that wasn't like we weren't
[2862.24 --> 2867.92]  like that's the most logical name oh look it spells sass uh i just thought the word sass was funny i
[2867.92 --> 2874.78]  thought to have come to like an effeminate name uh for technology um isn't really common things are
[2874.78 --> 2881.32]  normally called like you know thor and rake hammer right you know so like hey let's just call it sass
[2881.32 --> 2886.24]  like why why is it bad to to call something like that um and i loved how when i was by the way i was
[2886.24 --> 2892.18]  first announcing it like people like you really called it sass are you kidding that's a terrible name
[2892.18 --> 2898.36]  um which made me like it all the more uh well that's no sorry to interrupt that's no worse than
[2898.36 --> 2908.00]  um what uh vagrant's original name was which was hobo oh boy yeah that was fun um yeah so yeah uh so
[2908.00 --> 2916.68]  sss kind of became this alternate syntax um uh it's definitely through the years uh sss is far far far far
[2916.68 --> 2922.08]  more popular um and so when i've kind of been reengaging over the last two years in the project and
[2922.08 --> 2930.36]  um at least with the community uh the pragmatic guide to sass and libsass uh they only use the css like
[2930.36 --> 2939.92]  syntax um and i don't really differentiate scss anymore uh in my mind scss is now just the extension
[2939.92 --> 2948.14]  on the file or sass sass css um or super css or something i don't know but yeah like that it
[2948.14 --> 2955.14]  stands for that um the language is still sass um i i i'm actually not a fan of having two uh syntaxes
[2955.14 --> 2959.86]  because i think it's it's kind of bad marketing to say well what you know oh is this i feel like it's
[2959.86 --> 2965.06]  been like a like an anchor to you guys and i don't mean like an anchor in a good way i mean like it's
[2965.06 --> 2970.82]  dragging you down that it's it's it was hard to get people to adopt when there was you know the
[2970.82 --> 2974.14]  older way because you know you talked about the different syntax and how different it looked and
[2974.14 --> 2977.88]  people didn't want to adopt it and they got to learn something new the same reason you know people
[2977.88 --> 2984.02]  don't want to use or people would resist hamil versus erb or html straight you know like it's
[2984.02 --> 2993.84]  it's it's just one more hurdle to to get over and um so when we were on the show um the most recent
[2993.84 --> 2998.74]  show 93 with phil up here from thoughtball we were talking and he asked me and i said well
[2998.74 --> 3004.50]  i know that nathan has said and uh from the sass point of view that it's going to continue to support
[3004.50 --> 3009.42]  both syntaxes but do you know or do you think that it would be just wise just to you just said it
[3009.42 --> 3015.06]  basically but you know it is the longevity of sass going to keep supporting these two syntaxes
[3015.06 --> 3019.54]  and i think it comes with a tail end to that question too by saying that
[3019.54 --> 3027.12]  it every time you have a conversation about sass and its syntax you have to have two conversations
[3027.12 --> 3033.84]  and it forks in it makes it confusing like even in the five by five uh rc room we got uh somebody in
[3033.84 --> 3038.26]  there asking questions about it and there's andrew thoroughly answered the question but they're still
[3038.26 --> 3046.46]  asking questions because it's a confusing subject yeah i should be in that room uh yeah i mean so i i
[3046.46 --> 3053.12]  definitely think the nathan is behind um and i believe chris is behind uh the kind of naming
[3053.12 --> 3061.82]  scheme that it is just sass the word sass refers primarily to or exclusively to um the css compatible
[3061.82 --> 3068.30]  version um which is awesome because with that you just point sass at your folder of css files change
[3068.30 --> 3072.58]  the extension and it just works you don't have to worry about anything you don't have to go backport
[3072.58 --> 3078.04]  everything you can use css libraries it all just works yeah um but that that's where you know it's
[3078.04 --> 3086.14]  really a killer thing so i think it's not you you can stop having two conversations uh as long as you
[3086.14 --> 3095.10]  feel comfortable with that um their sass is now css compatible its extension is scss um we try the
[3095.10 --> 3100.44]  the pragmatic guide to sass barely mentions the exist i think there's a little sidebar where they say
[3100.44 --> 3105.76]  there's an older syntax called indented sass um you know to find out more go here right that's
[3105.76 --> 3110.86]  basically we've changed all the examples what's on the website um so it's definitely people you know
[3110.86 --> 3117.32]  there's definitely i know a lot of diehard people who love the older syntax um and because it it is
[3117.32 --> 3122.30]  kind of more minimalist yeah we use it at pure charity so andrew and i both uh our full-time jobs
[3122.30 --> 3128.24]  we work together at this company called pure charity um and we use sass there and we use the indented
[3128.24 --> 3134.44]  version of sass uh yeah so the ruby version will before i went to pure charity i always use the
[3134.44 --> 3140.48]  scss version and um it took me a little bit to get used to it but now i actually do prefer the invent
[3140.48 --> 3146.50]  the indented version um so now it's like i but you know it's funny because you're you're bringing up a
[3146.50 --> 3152.42]  problem that i think kind of plagues the uh i don't know if it's every community but especially in
[3152.42 --> 3159.28]  the ruby community and and especially in the rails community um i think like four you know four years
[3159.28 --> 3163.02]  ago five years ago people wanted to get in and get started with rails and it was really easy
[3163.02 --> 3168.70]  like to get up and running you know like the zero to rails was so easy but now there's like
[3168.70 --> 3175.42]  so many choices you have to make and i think that when it when a potential developer is making these
[3175.42 --> 3179.64]  decisions on you know templating engine and how to do their style sheets and like how to do
[3179.64 --> 3184.12]  authentication there's like all these choices you have to make to get started then you get to you
[3184.12 --> 3188.30]  know you get to sass and you're like okay everyone uses sass but which version of sass should it's like
[3188.30 --> 3194.86]  more choices choices choices and i think the zero to you know rails is a lot harder now for people so
[3194.86 --> 3202.76]  you know i think that removing features or removing you know like if you removed the indented sass version
[3202.76 --> 3208.08]  you'd have a battle probably and the good and the bad of open source is guess what if you
[3208.08 --> 3212.40]  removed support from sass then somebody would fork it and get the old version back and people would
[3212.40 --> 3217.46]  start using it and it's like this thing that plagues the community but it choices are a good
[3217.46 --> 3221.98]  thing but they're hard for newcomers so i don't even know where i stand on that but yeah it is funny that
[3221.98 --> 3227.42]  you say about that because i always like i was a diehard about the scss version on all the projects i
[3227.42 --> 3233.94]  ever did before i came to pure charity come to pure charity it's all indented sass i like it was cutting
[3233.94 --> 3238.30]  teeth and i hated it and i had to spend time just like getting used to it again and now everything i
[3238.30 --> 3244.44]  do on the side i do indented sass with so i'm all screwed up no you guys are just spreading the chaos
[3244.44 --> 3250.86]  thanks um now look so indented sass is fairly popular within experienced rails programmer groups
[3250.86 --> 3257.52]  um if you look outside of rails which is where all the growth has been in sass usage um it's hands
[3257.52 --> 3264.32]  down scss um i don't they're really not aware that anything else exists to be honest um like it's
[3264.32 --> 3267.12]  that's when you look at the tutorials when you're learning when you're bringing it to your company
[3267.12 --> 3274.28]  you're using php but you have this sass you know your your framework supports an adapter it just is
[3274.28 --> 3280.90]  scss to you there's no concept so well it makes sense i mean sass is css compatible when you use that
[3280.90 --> 3285.12]  version and that alone is like the sales pitch that makes sense why you would do that you know
[3285.12 --> 3288.76]  you're you're zero to sass for lack of better terms you know just to put on what you just said
[3288.76 --> 3294.72]  there is it's super quick as a matter of fact what what got me to start the sass way with john
[3294.72 --> 3299.70]  long and others was um was just that because i was writing a tutorial because somebody was asking me
[3299.70 --> 3305.10]  how to get started with sass and i'm like well it's so easy nowadays like you literally just you
[3305.10 --> 3309.02]  know do what's necessary to get the ruby compiler you know before lib sass and others that are
[3309.02 --> 3315.00]  available but you know get the ruby compiler to your local machine and pretty much from
[3315.00 --> 3320.08]  there it's just renaming your file from css to scss like that was easy wasn't it like
[3320.08 --> 3324.34]  now go rinse and repeat in your projects and just start adding variables and incrementally
[3324.34 --> 3330.76]  just sprinkling you know sassy css to use your word hampton in there and boom i mean you're you're
[3330.76 --> 3336.06]  incrementally just stepping into this unknown world you never knew was there and that's that's that
[3336.06 --> 3340.40]  that's the magic sauce right there yeah i mean well that's definitely when you see like i mean we're
[3340.40 --> 3346.48]  it's it's really fun to teach sass i think because um i mean it's in pragmatic guide to sass and also
[3346.48 --> 3353.16]  the the stuff we're doing with treehouse um it is very much the first lessons like okay so this you
[3353.16 --> 3359.74]  know you show some css this is also sass you've now learned step one um and then you know you say
[3359.74 --> 3366.48]  try indenting try to put a sub selector and then you know i think you're like now you've done magic
[3366.48 --> 3370.76]  like right yeah this is like and then you can do a variable and it's yeah and then they're just like
[3370.76 --> 3374.34]  people's mind yeah people are just like doing css but haven't seen it before yeah they have a
[3374.34 --> 3378.38]  little aneurysm they're like wait what oh what i don't know what just happened you can do that now
[3378.38 --> 3383.18]  um can you talk a bit about what you're doing with treehouse just to kind of give that a little light
[3383.18 --> 3388.94]  yeah so i mean i'm working with michael and i are both working with treehouse to kind of we're
[3388.94 --> 3394.16]  currently working on the scripts um but we're going to be doing a whole module um you know treehouse if
[3394.16 --> 3398.76]  people don't know is the um training company that basically you log in and they have videos and
[3398.76 --> 3404.00]  tutorials to help beginners learn uh different web technologies and so sass is going to be one of the
[3404.00 --> 3410.24]  featured web technologies and have a whole uh unit and they've asked me to come in and do the videos
[3410.24 --> 3414.10]  and you're going to go there and record and be the person teaching i am i am going to be the person
[3414.10 --> 3419.16]  teaching wow that's awesome i got a friend that's uh working on there you'll have to i'll have to hook
[3419.16 --> 3424.00]  you two up when you go yeah it was actually it was uh all the other guys at less conf there was a
[3424.00 --> 3429.26]  a bunch of the treehouse guys and uh i know uh andrew chalky's been a friend of mine for a long
[3429.26 --> 3435.58]  time and uh they were just like hey wait you should come do it and i was like let's do it i'm not busy
[3435.58 --> 3441.08]  uh was it uh was it your your masquerade on the beach that uh got them to think that way or what
[3441.08 --> 3445.40]  we don't talk about that what happens at less conf stays at less that's the magic rule
[3445.40 --> 3455.90]  uh good one touche um so yeah let me yeah that's it i don't have a guess let's uh let's ask
[3455.90 --> 3463.26]  hampton our famous questions andrew yeah so i guess the first one um and the listeners to the show
[3463.26 --> 3468.86]  will know this but uh any newcomers we kind of have two questions that we ask to all of our guests
[3468.86 --> 3476.34]  and the first one is for who is your programming hero um i'd say tender love
[3476.34 --> 3484.10]  he's a he's a alumni of the changelog oh really those that don't know tender love is aaron patterson
[3484.10 --> 3493.62]  well-known ruby is out there and a funny guy on twitter yes he is um no i just i there's uh not only
[3493.62 --> 3500.36]  like uh his project uh nokogiri um was a major inspiration to the crazy stuff for doing a move
[3500.36 --> 3507.70]  web now and uh you know uh it's his coat is beautiful and uh he's the just the sweetest guy
[3507.70 --> 3514.04]  in real life just the most down-to-earth nice guy out there and uh he has an extreme in his surrealist
[3514.04 --> 3521.10]  sense of humor um and uh pictures of uh gorby puff his cat um just complete the whole thing for me um
[3521.10 --> 3525.48]  and i love when i see him at a conference and he's usually sitting down and actually just coding
[3525.48 --> 3530.06]  the whole time um you know i like to think of myself as a pretty passionate programmer but
[3530.06 --> 3536.96]  man like i'm just like hey when's lunch break like oh let me talk to some people uh i'll check twitter
[3536.96 --> 3540.50]  like he's just sitting there like hacking with somebody and building something really cool and
[3540.50 --> 3546.80]  amazing um and i just so much respect and then plus having the kind of weird surrealist sense of humor
[3546.80 --> 3555.40]  um and i do have a a um back on my laptop i have uh the i have a gorby puff sticker um of his crazy
[3555.40 --> 3566.06]  looking cat so he's winking awesome yeah he's a i think he's a if a lot of a lot of people try and
[3566.06 --> 3571.64]  get creative uh when they answer that question and they'll you know come up with some obscure you know
[3571.64 --> 3577.68]  unix developer from the 70s and you know like but i think if a lot of people that have been in the
[3577.68 --> 3581.46]  ruby community were honest he would be on that list for for a lot of people he's an inspiration
[3581.46 --> 3588.48]  to me i mean yeah big big fan of his so uh before we go on i just want to mention so those listening
[3588.48 --> 3592.68]  if um if you want to pick up another episode of the changelog to go back and listen to if you go to
[3592.68 --> 3597.70]  five by five dot tv slash changelog slash 44 you'll pick up the episode where we talk uh
[3597.70 --> 3603.44]  uh i think it was me and win that talked uh no it was just win on that show talked uh ruby19 so this
[3603.44 --> 3610.58]  is pre 2.0 obviously uh talked ruby19 nokagary and tender love making with aaron patterson so go back
[3610.58 --> 3616.08]  and listen to that show which is his website tenderlovemaking.com i think right can i throw in
[3616.08 --> 3622.00]  another answer too sorry that's really weird yeah go for it no because when donald me uh brad fitzpatrick
[3622.00 --> 3629.96]  i don't know uh he invented uh memcache and he works on go now um and uh we use go a ton and
[3629.96 --> 3636.58]  really love that language um and uh i just think that's really amazing to be on such two projects
[3636.58 --> 3642.98]  that i use all the time um yeah that's it yeah i think i saw his name i think he was associated with
[3642.98 --> 3648.88]  open id at one time or he started it i don't remember but i used to use open id to log into
[3648.88 --> 3654.82]  i want to say stack overflow yeah i believe he's in his name on that yeah he started open id i believe
[3654.82 --> 3663.60]  yeah yeah cool so our other question and this is for you to pick uh hampton the different libraries
[3663.60 --> 3668.06]  that you're working on we kind of asked for a call to arms so being that we do support open source and
[3668.06 --> 3672.80]  we love open source uh what would you like to see the community get involved with on any of your
[3672.80 --> 3682.00]  many projects that are out there okay so definitely hcatlin slash sass c um or uh ruby sass i believe
[3682.00 --> 3688.18]  is the name of it um both those need help and normal people have the ability to help on them um
[3688.18 --> 3694.82]  if you're crazy into compilers then you can try to dive into the lib sass stuff um but it's a little
[3694.82 --> 3701.10]  intense it's kind of hard to just like jump into uh but uh you know sass c especially the test
[3701.10 --> 3706.54]  framework area uh needs a lot of help um i mean that's the thing where the community if you're
[3706.54 --> 3712.12]  really passionate about sass and want to see sass go from even just being a ruby implementation to
[3712.12 --> 3716.48]  not just being a c implementation but being other things really being a language uh we really need to
[3716.48 --> 3721.58]  have a compelling spec um that kind of works for all implementations and can really help you know
[3721.58 --> 3726.86]  people and you know help solve projects that that work with it um so that's if i had a wish it'd be
[3726.86 --> 3731.42]  people to go in there and help write tests uh the tests are simple right now we don't have options
[3731.42 --> 3738.00]  yet we don't support you know some of the the different compile methods um and uh it's not
[3738.00 --> 3742.36]  its own project and i just absolutely love to have somebody um come in and pitch in and help with that
[3742.36 --> 3749.08]  um it's it's not always the sexiest thing in the world to work with a spec library um but it would
[3749.08 --> 3753.82]  make a huge difference to the overall community and the the you know the health of sass itself
[3753.82 --> 3759.80]  yeah i think you can uh you can make it the sexiest thing in the world by offering free ipads
[3759.80 --> 3764.54]  that's what i do at pure charity to get my code reviewed that's what he does he's like here's a
[3764.54 --> 3770.94]  pull request with a free ipad attached i mean no one ever gets free ipads but it seems to give them a
[3770.94 --> 3779.78]  shot i like this uh this one test you have in the sassy library uh huge.scss that's kind of cool
[3779.78 --> 3786.14]  well that's our that's our uh speed test so we we have a couple of ones we use for benchmarks
[3786.14 --> 3792.82]  yeah because definitely it's the like a really simple file is you know i mean especially ruby
[3792.82 --> 3796.24]  boot time is when you're doing performance differences but i mean i don't know about
[3796.24 --> 3801.90]  you guys how large your project is but um there's a lot of people with very very large sass projects
[3801.90 --> 3808.84]  and you know ruby is not so great with handling you know 100 million strings in memory all at once
[3808.84 --> 3813.06]  and then trying to write that out to disk uh and that's why you see really slow performance with
[3813.06 --> 3822.46]  ruby sass uh and big projects so um and lib sass it's super fast yeah i guess one question on the
[3822.46 --> 3826.54]  talking about this the the testing piece i'd never it never really occurred to me that these tests would
[3826.54 --> 3832.14]  be written in in sass i guess that kind of just makes sense but for those who are like uber sass
[3832.14 --> 3837.80]  enthusiasts that like you know write compass extensions and are like frameworking to the nth degree
[3837.80 --> 3843.02]  you know what uh what would you recommend for them to like dig into in some of these projects just
[3843.02 --> 3845.42]  to learn from some of the code you've written or you guys have written
[3845.42 --> 3856.08]  hmm that's a tough question um i mean definitely uh you know i mean compass is a crazy invention
[3856.08 --> 3862.50]  itself and has you know nice components that you can go look into uh lib sass is pretty challenging
[3862.50 --> 3868.90]  to look at and and the main sass repo itself it's very you know mature optimized code is typically
[3868.90 --> 3874.52]  ugly code to be honest not to it's sorry nathan it's not like ugly but there's just a lot of stuff
[3874.52 --> 3880.66]  you do to you know optimize and get around things uh it's not the it's not this kind of pure perfect
[3880.66 --> 3885.74]  you know ideal um it's not the kind of thing you do like a training on and this is how your coach
[3885.74 --> 3891.30]  look um yeah i don't know when people want to learn what to to work on i mean honestly like
[3891.30 --> 3896.26]  share your sass code go go look at some of the crazy mix-ins that people write um there's a ton
[3896.26 --> 3901.52]  of stuff on code pen i love to see that stuff floating by um just you know i'll randomly see a tweet of
[3901.52 --> 3910.28]  like oh look at what i built in code pen um uh was that the question okay no it's good i definitely
[3910.28 --> 3915.74]  think compass is a super good resource especially if you're working with compass you already know
[3915.74 --> 3919.88]  about that but you know definitely diving into the source code so like if people want to know how do
[3919.88 --> 3926.02]  i write my own you know mix-ins that do xyz you know they're going to go jump into into compass or
[3926.02 --> 3930.30]  bourbon or something like that or if they want to drop down into ruby and write some sort of ruby
[3930.30 --> 3935.66]  extension that does something that in addition to you know on top of sass or whatever then they can do
[3935.66 --> 3940.54]  those things but i just had it really hadn't really occurred to me that uh your tests will be
[3940.54 --> 3945.76]  written in sass so i was like that's kind of neat and like looking at some of your variables in there
[3945.76 --> 3952.42]  it's just i just didn't really think about them being written in in sass don't ask you why what would
[3952.42 --> 3956.50]  you write them in i don't know that's that's what i'm just i just don't even know i haven't done this
[3956.50 --> 3961.34]  kind of work like writing tests against this i just i don't know i just didn't think it would be
[3961.34 --> 3967.46]  written in sass well so uh you know tritium which is my newer language that's uh imagine it's like
[3967.46 --> 3974.18]  nokogiri kind of but a language or a really stripped down javascript uh and uh you know
[3974.18 --> 3981.54]  its test framework that i wrote is giant um because it's basically input html the tritium that you want
[3981.54 --> 3987.30]  to change on it and then what we expect to come out of that um and you you know every single build
[3987.30 --> 3993.76]  that we do internally the company you know goes and kicks off uh like i think it's near 2 000 tests
[3993.76 --> 3999.38]  at this point um anytime that we get a bug you go prove it out in one of those uh snippets and so
[3999.38 --> 4003.52]  that's basically what we're trying to do here um it's very early version though right now it's very
[4003.52 --> 4010.44]  simple um primarily what we're running though is we run the ruby sass and then we run sassy run them
[4010.44 --> 4014.38]  right next to each other and make sure they match um for ones that don't have expected output
[4014.38 --> 4021.46]  awesome well hampton i want to thank you for joining us today it was definitely a fun chat
[4021.46 --> 4027.80]  uh talking with you about sass hamil wikipedia mobile move web and all the crazy stuff you guys
[4027.80 --> 4034.90]  are doing there um definitely appreciate your your inventor hat and hope you keep wearing that hat and
[4034.90 --> 4042.10]  don't stop inventing i'm sure that you won't but uh i can't help it i can't help it stop me somebody
[4042.10 --> 4047.34]  exactly exactly and if you want to if you want to follow him you can follow him on twitter he's hcatlin
[4047.34 --> 4054.64]  both there uh as well as github this is episode number 94 show notes and this show will be available
[4054.64 --> 4064.10]  tomorrow at 5 by 5.tv slash changelog slash 94 uh next week we're andrew we don't have anybody lined
[4064.10 --> 4070.80]  up for next week do we uh we have some pending some pending so guests for next week has not been
[4070.80 --> 4077.00]  pinned down uh pinned down but nonetheless next tuesday at 5 we'll be broadcasting live again so thanks for
[4077.00 --> 4079.00]  tuning in and we'll see you next week
[4079.00 --> 4080.04]  you
[4080.04 --> 4082.04]  you
[4100.80 --> 4110.04]  you
[4110.04 --> 4112.04]  you
[4112.04 --> 4114.04]  you
[4114.04 --> 4116.04]  you
[4116.04 --> 4118.04]  you
[4118.04 --> 4120.04]  you
