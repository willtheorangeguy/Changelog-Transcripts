[0.00 --> 14.80]  welcome back everyone this is the change log and i'm your host adam stekowiak this is episode
[14.80 --> 29.98]  166 and on today's show we got an awesome show about javascript javascript in the wild as a
[29.98 --> 37.20]  in omaha nebraska today we're talking to zach leatherman nick nisi and also co-host of the show
[37.20 --> 43.54]  jared santa who is doubling as an organizer of this awesome conference we have three awesome
[43.54 --> 50.42]  sponsors for the show coach ship top towel and hip chat our first sponsor is coach ship and they've
[50.42 --> 56.42]  launched a brand new feature called organizations now you can create teams send permissions for
[56.42 --> 62.58]  specific team members and improve collaboration in your continuous delivery workflows maintain
[62.58 --> 67.24]  centralized control over your organization's projects and teams with coach up's new
[67.24 --> 73.32]  organizations plans you can save 20 off any plan you choose for three months by using the code
[73.32 --> 79.66]  the changelaw podcast again that code is the changelaw podcast and you'll save 20 off any
[79.66 --> 85.46]  plan you choose for three months by using that code head to codeship.com slash the changelaw to get
[85.46 --> 97.88]  started and now on to the show all right we were back we got a great show lined up today it's all
[97.88 --> 104.36]  about javascript today as a matter of fact it's not just javascript it's javascript in the wild we have
[104.36 --> 112.34]  three of six of the organizers uh making any js conf 2015 happen so we got jared on the on the line we got
[112.34 --> 118.32]  nick on the line and we got zach on the line everybody say hello wow hey how's it going all
[118.32 --> 124.86]  right so who's excited about about this this conference whoo everybody yeah i think we're
[124.86 --> 130.16]  all excited i think that we're all nervous we're kind of going into the last couple of weeks here so
[130.16 --> 134.92]  everything's kind of starting to come together i'm glad you mentioned that so today's record day is
[134.92 --> 142.74]  july 21st the release date so the air date is planned to be july 24th and the conference so
[142.74 --> 147.42]  everybody's listening and potentially clicking a button to go buy a ticket if there's some left
[147.42 --> 156.62]  is august 7th it's friday um so we got what roughly 150 people 200 people coming is it fully sold out yet
[156.62 --> 163.12]  what's the what's the what's the state i think we got about 30 or 40 tickets left so if people want
[163.12 --> 169.90]  to get on board they gotta buy their tickets soon okay so just to start this show off right let's get
[169.90 --> 175.86]  to know everybody here so everybody knows jared right jared you're known you're you're you're normal
[175.86 --> 181.76]  i don't know if i'm normal but uh i'm normally on the show so you're normally on this show people
[181.76 --> 186.96]  know who you are so jared santo you live in omaha nebraska correct these fellas here and some
[186.96 --> 192.32]  others on organizing this conference uh you want to give an intro to yourself for those who may not
[192.32 --> 199.48]  know who you are who me yeah you yeah jared santo i live in omaha nebraska um helping organize this
[199.48 --> 206.72]  conference uh co-host of the changelog that's right um what else you want to know adam object lateral
[206.72 --> 213.82]  yeah so i'm a software developer uh on contract object lateral is my company i also do some teaching
[213.82 --> 222.64]  at web dev boot camp called interface school um four kids a wife see nobody knows this about you on
[222.64 --> 226.88]  this show i'm gonna get to talk about your your details too often yeah those are your details
[226.88 --> 232.38]  it feels strange the the light has is you know uh shining on me now i don't like this the veil just
[232.38 --> 236.64]  being pulled back a little tiny bit and the i prefer to ask the questions i prefer to ask the
[236.64 --> 240.92]  questions all these jared santo secrets are being exposed let's well let's we'll leave you alone
[240.92 --> 247.18]  for a bit then zach how about you zach leatherman by the way i'm zach leatherman i also live in omaha
[247.18 --> 254.50]  i uh i'm one of the co-organizers of nebraska js i'm one of six organizers for the conference
[254.50 --> 260.84]  i work for filament group which is a small design and development consultancy in boston
[260.84 --> 271.08]  um i think that's about it what is nebraska js uh nebraska js is the meetup from which the nebraska
[271.08 --> 281.02]  js conference was born from so nebraska js started as a meetup i think in 2009 and it kind of fizzled
[281.02 --> 287.20]  out in 2012 and that's when i kind of took over um from three people that were kind of looking to get
[287.20 --> 294.14]  rid of it um and we made a couple changes to it uh started publishing all the talks and meetup videos
[294.14 --> 300.22]  online um getting a bunch of different speakers to come in and just kind of grew the meetup from that
[300.22 --> 308.36]  so zach's also a frequent uh conference attendee and speaker he's spoken at smashing conf velocity
[308.36 --> 314.12]  nice that's conf he even spoke at the white house recently what are you kidding me he's being humble
[314.12 --> 319.94]  but i won't be humble for him come on tell us about that uh yeah so they invited a bunch of
[319.94 --> 326.74]  meetup organizers to go to the white house to speak um just kind of highlight people that were
[326.74 --> 334.58]  doing things to get people involved with technology in their communities so i was probably the most
[334.58 --> 341.66]  underqualified person there uh but there were just there was a ton of very talented and very amazing
[341.66 --> 347.96]  people doing uh crazy things in their development communities to get people involved with technology
[347.96 --> 353.64]  so um people that were doing code schools people that were trying to help people get out of poverty
[353.64 --> 362.36]  by learning to code um and humble meetup organizers like myself so um well you did revive it though you
[362.36 --> 367.46]  said it was dying in 2012 you took it over and and it's now i'm sure it's blossoming because you got a
[367.46 --> 375.38]  conference coming from it yeah that was kind of one of the big goals that i had when um i took it over
[375.38 --> 381.62]  or that was kind of one of the long-term goals that we wanted to do um and now it's it's finally
[381.62 --> 388.78]  happening so cool i'm really excited about it and uh silent so far is nick neesey so nick you're a
[388.78 --> 396.86]  software engineer at site pen yes intro the this awesome audience to yourself um i want to hear more
[396.86 --> 406.30]  about jared i said i want to hear more about jared actually no um i'm you know i'm a software
[406.30 --> 412.36]  developer at site pen uh i work remotely it's a 100 remote development consulting team mostly doing
[412.36 --> 421.00]  javascript and typescript these days and i'm also a co-organizer of nebraska js and of the nejs comp for
[421.00 --> 425.94]  nebraska js comp anybody else on your team guys that you want to give a shout out to that's that's not
[425.94 --> 433.56]  present here definitely yeah we have uh matt steel who works for union pacific it's one of our
[433.56 --> 442.22]  organizers we have sandy bar um and we also have john hobbs very cool and so you got six people this
[442.22 --> 448.78]  year uh putting on the very first version of this conference so this is august 7th uh so it's not very
[448.78 --> 452.22]  far away the change law will be there we're shooting our fourth season of beyond code there
[452.22 --> 457.70]  we'll also be shooting some video for the for the actual conference itself and just kind of
[457.70 --> 463.14]  being a part of the mix there but uh as a first time conference what what were some of the biggest
[463.14 --> 467.96]  challenges that you faced or some of the biggest things you were most excited about actually doing
[467.96 --> 472.90]  this conference being its first time we kind of had no idea what we were doing starting out
[472.90 --> 478.22]  that's usually the case isn't it yeah yeah so everybody was in over their heads i mean
[478.22 --> 486.04]  or has someone had some experience um doing this stuff well i mean it just kind of started from
[486.04 --> 495.22]  the meetup i think uh actually the the original idea probably came from jsconf in florida a couple of us
[495.22 --> 501.54]  went down there to the javascript conference um they had an amelia island it's pretty big javascript
[501.54 --> 507.62]  conference um and chris williams the organizer down there really encouraged people to sort of
[507.62 --> 513.24]  start things in their own development communities and get things growing from grassroots to try i
[513.24 --> 521.32]  think to try and probably get more tickets sold for for the big jsconf there so um yeah i think it
[521.32 --> 527.26]  was just kind of born out of an idea just kind of sitting around drinking on the beach at amelia island
[527.26 --> 532.94]  at a resort we're like hey we could we could do something like this having no idea what we're really
[532.94 --> 539.02]  getting ourselves into but um a couple of years after that we finally decided to pull the trigger
[539.02 --> 546.90]  and uh and organize it so well i think you've done pretty well here so far with your first time i i've
[546.90 --> 552.92]  never been to a conference that's been at a zoo uh which which does sort of lean towards the subtitle
[552.92 --> 559.44]  which is javascript in the wild so i mean why why a zoo it's the henry dorley zoo and aquarium
[559.44 --> 564.32]  there in omaha and jared you've talked about this a couple times too on the private side just you
[564.32 --> 571.60]  know when we're talking about this conference what's unique about the zoo well i mean in omaha
[571.60 --> 578.88]  there's not too much to do um we probably have a worse reputation nebraska has a more boring and
[578.88 --> 584.90]  yawney reputation than perhaps it deserves maybe it's accurate um but you know omaha is a decent
[584.90 --> 590.36]  size metropolitan and um there's actually kind of a burgeoning creative and technology scene
[590.36 --> 597.14]  even a small startup scene uh here in omaha and in the midwest but we really wanted to highlight like
[597.14 --> 603.50]  one of omaha's main attractions and have something that's different um than a lot of conferences that
[603.50 --> 610.04]  you typically go to so the henry dorley zoo is huge uh it's one of uh the best zoos in the world
[610.04 --> 614.32]  in fact trip advisor calls it america is it america's number one zoo or the world's number one zoo
[614.32 --> 621.50]  the world's in the world wow so take take that world it has the largest cat complex indoor jungle
[621.50 --> 627.92]  indoor desert and i think that's it and also largest aquarium that's also attached to a zoo
[627.92 --> 633.12]  for a long time we played second fiddle to san diego i think just because they had raw square footage
[633.12 --> 638.98]  over us um but sometimes at some point in the last couple years we've taken we've overtaken them
[638.98 --> 646.66]  and are now number one um so yeah it just seemed like a really cool unique place to have a
[646.66 --> 650.70]  conference about javascript will we see any animals by any chance
[650.70 --> 660.66]  yeah absolutely we're gonna have uh some live animal demos animals roaming around um
[660.66 --> 665.38]  the play code yeah we're gonna have some zookeepers come in and bring in
[665.38 --> 670.62]  show some animals around in in the conference venue so it should be pretty unique pretty cool
[670.62 --> 675.98]  cool and also the the conference venue itself is a conference center that's attached to the aquarium
[675.98 --> 683.12]  and includes a 24 foot 10 000 gallon reef uh aquarium so there will be a lot of fish in there as well
[683.12 --> 688.50]  oh we love fish fisher fisher very welcome here on the changelog
[688.50 --> 697.64]  speaking of fish we have a single track conference so this is a single day single track small group so i guess being born from a meetup
[697.64 --> 701.52]  it would make sense to start out you know in the smaller scale so i think
[701.52 --> 707.42]  some of my favorite conferences to go to are 200 people or less because they just feel a little more intimate but
[707.42 --> 711.52]  coming off the the heels of gopher con i also enjoy
[711.52 --> 714.34]  12 to 1500 it just kind of depends on
[714.34 --> 716.78]  what place you're you're doing it in so
[716.78 --> 720.28]  being this this first year what was some of the things that you focused on as
[720.28 --> 723.50]  as i guess from a speaker standpoint and also just
[723.50 --> 728.42]  um making everyone feel comfortable i mean conferences are a lot of work so what was the focus
[728.42 --> 730.32]  initially placed on when setting it up
[730.32 --> 739.04]  well i think we wanted to keep it or i wanted to keep it single track just to make it simpler logistically
[739.04 --> 747.60]  um it just it makes it simplifies things a lot for the organizers but i also really enjoy single track
[747.60 --> 753.24]  conferences more um because i you always get that fear of missing out when you have a multiple
[753.24 --> 759.84]  track conference um you don't know what's going on in the other track or you don't know what you're
[759.84 --> 767.50]  missing um and we really want to minimize the number of like decisions that that attendees have to make
[767.50 --> 775.20]  we don't want to have people have to choose um between talks and i think it um i don't know
[775.20 --> 780.50]  i i just like it a lot better i just like single track a lot better i don't know if nick do you have
[780.50 --> 788.02]  an opinion on that yeah i think mace basically it's a lot simpler to to do that with the vet it works out
[788.02 --> 794.64]  well at the venue to have just a single speaker at a time um at least for this this first one and
[794.64 --> 800.86]  being our first conference like i've been to some multi-track conferences and it just it seems like
[800.86 --> 805.70]  it's a lot more work to make sure that everything's coordinated and everything's synchronized and and so
[805.70 --> 811.12]  it just seemed like a a lot easier of a place to start and it also gives us the opportunity to
[811.12 --> 816.36]  highlight all of the speakers that we're inviting to come in and we've got speakers coming in from
[816.36 --> 822.20]  all over the world and even a couple of local speakers to kind of highlight the local talent that we
[822.20 --> 827.56]  have as well yeah i think that's a that's a good point nick because one of the reasons that we wanted
[827.56 --> 833.94]  to do a conference and the reason that we uh do the meetup is that we're trying to expose more local
[833.94 --> 839.94]  developers to the community um and i think a single track helps do that as well people that are kind of
[839.94 --> 845.98]  not quite as well known um can get a little bit better exposure with the single track conference
[845.98 --> 854.20]  do you guys know the the ratio of local speakers to out-of-towners yeah i think we have three local
[854.20 --> 863.02]  speakers out of nine what was the the process like i guess to to you know one obviously it's a single
[863.02 --> 868.82]  track so it's got to be you know the topics have got to be enough closer to like a middle barrier where
[868.82 --> 873.76]  it's not too new but it's not too senior and then you're sort of in the middle there what was the
[873.76 --> 878.92]  process like coming up with some topics you know the call for proposal what was the selection like
[878.92 --> 885.84]  and actually choosing some of the speakers i i think the i mean the talk selection process was
[885.84 --> 895.14]  pretty grueling uh yeah it was like a we spent the whole night at the bar um i don't know maybe
[895.14 --> 904.02]  you're seeing an organizing theme here but um fighting over what talks we wanted um and it got
[904.02 --> 909.08]  a little i want to say it got a little dirty did it really some politics came up anybody get any beer
[909.08 --> 914.70]  tossed uh no that's dirty well we don't want to yeah we don't want to go that extreme we don't want
[914.70 --> 923.08]  to waste any of uh don't be wasting any liquids but yeah well i think we we did have a bent and um this
[923.08 --> 931.42]  is something that zach promotes heavily at the meetup which is um practicality so the nebraska
[931.42 --> 941.12]  js meetup tries to highlight topics and speakers who are using javascript um in a practical real world
[941.12 --> 948.98]  take it home and use it kind of way and so even the the subtitle javascript in the wild is kind of a
[948.98 --> 953.20]  play on words because it's of course you know in the zoo but it's also like these are things you
[953.20 --> 957.48]  can actually take these are things javascript is doing out there every day running websites
[957.48 --> 963.66]  um and businesses and these things and so we wanted to balance that with also fun and like enjoyable
[963.66 --> 969.56]  and interesting things and so um speaker selection was difficult because you know we care about the
[969.56 --> 974.30]  speakers and we also care that these topics kind of like played into that ballpark and so that's
[974.30 --> 980.78]  where a lot of the rub kind of focused are these titles uh in stone that are on site because i
[980.78 --> 986.68]  was gonna read a couple off if y'all don't mind yeah i think so oh yeah so we got uh somebody helped
[986.68 --> 991.42]  me with some names i think it's uh i'm gonna say celly pam celly is that right believe in streams
[991.42 --> 998.92]  i think it's pam cell so all right the e may be silent uh isaac murchie you and the temporal dead
[998.92 --> 1004.22]  zone es6 variables for fun and profit uh i'll just read the titles from here on out because
[1004.22 --> 1010.26]  i might put some names and offend people but add a tool to your development suites army knife
[1010.26 --> 1018.70]  using custom elements today architecting communities is the next one svg animation with snap svg high
[1018.70 --> 1022.50]  performance in the critical rendering path which i think we've talked about recently jared a little
[1022.50 --> 1028.32]  bit here on the show and then also reacting to the isomorphic buzz i'm assuming that's a play on
[1028.32 --> 1034.10]  words too because react's got to be in there somewhere yep right so that's right more play on
[1034.10 --> 1042.70]  words more fun from bruce good job bruce so i mean was it a real fight when it came to choosing some
[1042.70 --> 1048.00]  of these speakers and some of the the talks we just talked over i really think so um i think we had
[1048.00 --> 1055.56]  78 total submissions wow and i mean we only had seven speaker slots and then two keynote slots
[1055.56 --> 1061.88]  and so we had to whittle it down from that and it was really really hard uh so we all kind of looked
[1061.88 --> 1069.58]  at at the um submissions kind of on our own and started to prioritize the ones that we really liked
[1069.58 --> 1074.86]  all of them were really fantastic so it was really hard to do that but then we came together and
[1074.86 --> 1080.54]  um shared our lists with each other found the ones that were a common theme across all of the
[1080.54 --> 1087.92]  organizers and then um kind of got a a first pass with maybe one or two and then the rest of the
[1087.92 --> 1091.94]  night was just arguing about the other ones reprioritizing the list and going on and on
[1091.94 --> 1097.84]  so what's the total people count and total hour count going into making the selections
[1097.84 --> 1108.48]  oh that's a good question um i mean when when it came down to doing the final talk discussion
[1108.48 --> 1114.78]  we decided to limit that to only one night because we could have done that for weeks and weeks and weeks
[1114.78 --> 1124.70]  i'm sure um but when i i mean i think we spent probably a good solid week on um individual talk
[1124.70 --> 1130.50]  selection and then group selection as well so what were some of the things that uh when you were
[1130.50 --> 1136.98]  discussing the talks and topics and uh was it did uh what were some of the things you could do i
[1136.98 --> 1142.58]  remember jared i'm thinking back um to the to the show we had with sarah may when she said they
[1142.58 --> 1147.48]  purposefully hid people's names and genders and things like that so they wouldn't be biased against it
[1147.48 --> 1153.20]  what was some of the process y'all used to to sort of be have an unbiased opinion towards your selections
[1153.20 --> 1160.68]  yeah i definitely did that and i i hit it looked at the just the titles and the um descriptions of
[1160.68 --> 1165.50]  the talks to begin with and that's kind of how i started with with my side of the list and then
[1165.50 --> 1171.16]  from there i started looking at um you know i i got my list from there on the things that i thought
[1171.16 --> 1175.64]  were most interesting and then i started thinking about things like you know wanting to have a good
[1175.64 --> 1183.14]  mix of local um local developers and and more known developers as well and so it kind of went
[1183.14 --> 1192.60]  from there on tech talks versus uh more soft skills talks yeah good point is there any uh talk here
[1192.60 --> 1199.28]  even just a maybe not a person named but just the the topic or title named that one of you guys
[1199.28 --> 1207.20]  fought over hardcore and didn't make the cut for whatever reason that's a good question i don't
[1207.20 --> 1213.22]  really remember the talks that we didn't select because that process i think took place i don't
[1213.22 --> 1220.16]  know i want to say like a couple months ago okay um so i think that you're really excited about them
[1220.16 --> 1228.10]  that's in the list yeah i mean i think all of them are going to be great um i think that nicholas
[1228.10 --> 1233.76]  vakwa's talk on high performance and the critical rendering path is one of the ones that i really kind
[1233.76 --> 1239.98]  of pushed hard for because i think it's a very important topic especially with uh the number of
[1239.98 --> 1244.86]  sort of client-side mvc frameworks that are kind of slowing down the critical performance
[1244.86 --> 1252.56]  aspect of websites today so yeah i'm excited for that one as well i think uh i wasn't aware of
[1252.56 --> 1257.46]  nicholas vakwa previous you know prior to that i think he submitted like was he the guy that submitted
[1257.46 --> 1262.78]  like four or five like he just he just had talks is that him yeah yeah i think he had at least three
[1262.78 --> 1268.24]  and he was just throwing them in there which is like okay this person's excited somehow he found
[1268.24 --> 1273.24]  our cfp before it was even before we even publicized i don't know how that happened
[1273.24 --> 1281.34]  they're not usually hard to find is it slash uh cfp yeah there you go see that yeah he's probably got a
[1281.34 --> 1286.04]  javascript bot just out there submitting his talks to all these there's a life hack right there
[1286.04 --> 1290.42]  conferences here's a couple here's a couple of tips that i could give to people who are submitting
[1290.42 --> 1296.58]  cfps and like hoping to get selected just as people who have recently done this um and these are
[1296.58 --> 1301.74]  these should be they shouldn't be had to be said but i guess they do because we ran into this over and
[1301.74 --> 1309.28]  over so the first thing you need to do is spell your talk title correctly um if you misspell your title
[1309.28 --> 1315.88]  you're you're not giving yourself much of a chance to get selected um then to proofread
[1315.88 --> 1322.80]  your your synopsis um have somebody else read it for you read it out loud make sure that the
[1322.80 --> 1328.52]  sentences make sense because there's a lot of competition out there and even if your conceit
[1328.52 --> 1334.44]  is really good it's hard even as a person who's like i i think there was one that was had some bad
[1334.44 --> 1339.26]  grammar that i was like rooting for and i was arguing for and i just couldn't get over the hurdle of
[1339.26 --> 1345.00]  yeah but they did not take the time to to make sure their words are spelled correctly in their
[1345.00 --> 1352.14]  synopsis and so we can't trust them as a speaker so um those are just a couple of tips which sound
[1352.14 --> 1358.26]  like common sense but apparently not uh for people who are submitting uh proposals to cfps and then
[1358.26 --> 1363.56]  that's an awesome tip is uh go to whatever the conference is slash cfp and see if you can get in early
[1363.56 --> 1369.72]  and bombard us with multiple submissions because yeah he he was immediately on our radar because he
[1369.72 --> 1375.98]  had three talks in there before anybody did it's like wow this guy's serious um so anyways just a few
[1375.98 --> 1384.44]  a few small tips that i couldn't believe we ran into so many um almost lazy submissions and how
[1384.44 --> 1390.64]  even though on a few of those they seem like great talk ideas i just couldn't get over the hurdle of
[1390.64 --> 1396.14]  you know slow down take the time do it right yeah any other thoughts uh zach or nick on
[1396.14 --> 1401.80]  on any feedback to to those that are listening thinking man i want to submit a talk to a conference
[1401.80 --> 1406.94]  sometime soon or or i've done it and i've never gotten selected some some feedback or some tips
[1406.94 --> 1414.42]  yeah i would say um get involved the organizers um i'm i would have been happy to review any number
[1414.42 --> 1420.62]  of submissions before the before the deadline went but i never heard anything like no one asked
[1420.62 --> 1425.20]  me any uh questions and i i think we put on the website even hey we'll help you with your
[1425.20 --> 1433.34]  submission if you if you uh want our feedback up front um and yeah i think that can help quite a bit
[1433.34 --> 1439.28]  um just to even refine your ideas um with them before you even put in a submission i think could
[1439.28 --> 1445.82]  help your chances quite a bit another big piece to any conferences is obviously sponsors and
[1445.82 --> 1452.72]  what equates to cash flow really so i mean it seems like in jared only because you and i've talked
[1452.72 --> 1456.64]  uh outside of this i've kind of been following a little bit of what's going on here but it seems
[1456.64 --> 1460.92]  like as a first-time conference you've got some sort of trick up your sleeve or something like that
[1460.92 --> 1467.86]  because you're doing okay on you know finances from what i can tell in terms of your your home page
[1467.86 --> 1473.80]  you got plenty of sponsors so what was it like going out and seeking out either local or you know
[1473.80 --> 1478.64]  industry known sponsors what was the process like and who was in charge of that yeah i think that was
[1478.64 --> 1487.68]  kind of a team effort between me and nick um nick is a lot better at emailing that i am so um for sure
[1487.68 --> 1493.84]  he took the reins on a lot of the sponsor context but i think the the running the meetup really was the
[1493.84 --> 1501.16]  biggest thing we were already exposed to a lot of companies uh in our community because uh their
[1501.16 --> 1506.00]  developers were attending our meetup and our and we've been going strong for three over three years
[1506.00 --> 1514.08]  now um when i took over so um everyone kind of knew about the meetup already and because we sort of
[1514.08 --> 1521.14]  transitioned from meetup to conference there was a very clear uh line between the two and people are
[1521.14 --> 1529.06]  excited to get involved and we we've actually had um companies kind of fight over us to get uh to
[1529.06 --> 1534.00]  provide us with venues for the meetup or to provide us with food i mean we've never had a problem
[1534.00 --> 1540.72]  getting sponsorship for the meetup um and i think the the conference was kind of a continuation of that
[1540.72 --> 1547.12]  um the the support that we see from companies is just i think kind of a unique thing in omaha
[1547.12 --> 1554.52]  just because there isn't a ton of um i want to say bigger development communities
[1554.52 --> 1561.28]  uh in our area um we've had a lot of meetups but i think they kind of i don't i don't want to say
[1561.28 --> 1572.98]  come and go but um they haven't really united uh different development uh aspects like javascript can
[1572.98 --> 1580.68]  uh sort of everyone is exposed to javascript in some way um so that's also helped us grow the meetup too
[1580.68 --> 1586.56]  we have a lot of a lot of support coming out of that just as zach said and it was really when we
[1586.56 --> 1593.32]  were going to get sponsors and we actually had you know more pressure to get like a an information
[1593.32 --> 1598.48]  document out about sponsoring because we had sponsors just lining up immediately that wanted to
[1598.48 --> 1603.64]  to contribute they wanted to help out they wanted to to make sure that this conference sees the light
[1603.64 --> 1608.28]  of day and and we really couldn't do it without them so it's been really great what are some of the
[1608.28 --> 1615.42]  biggest uh questions you guys can think of when it comes to a sponsor um and asking questions back
[1615.42 --> 1620.16]  to the conference like what are their biggest concerns what are their biggest uh questions that
[1620.16 --> 1626.76]  that took you time to get over or just get questions back to get them to to commit to the support or even
[1626.76 --> 1634.48]  lack of support oh we did have a little bit of a problem with the sponsor that i won't name
[1634.48 --> 1644.24]  um but yeah they kind of promised us um some funds and then went dark so we never really heard back from
[1644.24 --> 1654.12]  them um and we had kind of made some decisions monetarily based on um assumption of those funds and
[1654.12 --> 1660.78]  we're going to be fine um monetarily but um certainly that didn't help the conference
[1660.78 --> 1667.10]  that we kind of had that that check sort of disappear out from under us right i just wonder
[1667.10 --> 1672.84]  because you know a lot of the you always have levels so i'm assuming you had levels i'm thinking
[1672.84 --> 1681.54]  about typical levels as like you know premium gold platinum you know pick your metallic uh material
[1681.54 --> 1686.86]  and then and then you know apply the level to it or whatever but i'm wondering yeah we actually did
[1686.86 --> 1693.60]  animals oh you did yeah so top level is lion i'm assuming elephant elephant there you go well
[1693.60 --> 1697.68]  that makes sense what we do is we we pick a metaphor and then we just beat it into the ground
[1697.68 --> 1703.12]  so right right this whole animal thing like we're just gonna kill it until it's dead and then we're
[1703.12 --> 1708.58]  gonna bring it back and kill it some more any whales because i like whales i thought that was a little
[1708.58 --> 1714.66]  too on the nose you know and when it comes to like big things and money you know you hear man i got a
[1714.66 --> 1720.96]  whale on the line here elephant that's kind of why we picked elephants the elephant in the room okay
[1720.96 --> 1727.56]  gotcha yeah i'm just wondering about the the process there because i know that um you know even for this
[1727.56 --> 1733.74]  show right it's a sponsored show so we get questions all the time about you know the the podcast and what
[1733.74 --> 1738.84]  it's about and you know all these different things so i'm just wondering like when a sponsor comes to a
[1738.84 --> 1743.10]  conference or a conference goes to a sponsor and says hey we'd like to see your support in this
[1743.10 --> 1748.32]  conference because of this this or this you know what are some of the things that uh that are like
[1748.32 --> 1754.00]  getting them involved or seeking you to them is it is it purely a financial benefit or is it like
[1754.00 --> 1759.76]  uh they're getting involved in the community they're already there a lot of them are already there they're
[1759.76 --> 1765.70]  already sponsoring us helping us out uh or at least trying to uh you know because we can only have so
[1765.70 --> 1772.26]  many venues that we can host to that each month um and and things like that but also you know looking
[1772.26 --> 1777.04]  like like one of the biggest questions that i got when when communicating with sponsors was
[1777.04 --> 1782.88]  kind of not not in like specific detail but like what are you going to use the money for how is it
[1782.88 --> 1787.88]  how is it going to go to helping the conference and uh you know if you have money left over what are
[1787.88 --> 1792.36]  you going to do with it things like that and and really just making sure that their investment is
[1792.36 --> 1798.00]  going into the community and it really is it's either going into this conference or feeding back into the
[1798.00 --> 1805.78]  the meetup um that we have every month or going into immediate planning for next year's conference
[1805.78 --> 1809.96]  should we decide to do that so just to be clear this isn't a get rich quick scheme
[1809.96 --> 1815.44]  no right but it's the worst one ever it's the worst one ever get rich never
[1815.44 --> 1820.76]  so that makes some perfect sense you know what are you using the money for and
[1820.76 --> 1823.90]  you know will you give some of it back if there's some left over
[1823.90 --> 1830.34]  did anybody ask you that one no one asked me that one no no they just wanted to make sure that we
[1830.34 --> 1836.06]  weren't doing it as a profit gotcha yeah that seems to be the case we're going to take a break here in a
[1836.06 --> 1840.46]  second because i got a couple things i want to bring up on that no but we got to break first and come
[1840.46 --> 1846.22]  back because we have awesome sponsors who make this show possible and we need to feature them so let's
[1846.22 --> 1851.22]  take a quick break we'll do that and we'll come back and talk a bit more about why the conference exists
[1851.22 --> 1856.18]  and uh you know what we can expect for it uh from it in the future so let's take a break
[1856.18 --> 1863.00]  you've heard me talk about top towel several times in this podcast but today is different i've got a special
[1863.00 --> 1869.78]  treat for you i went out and spoke with a listener who a year ago had never heard of top towel he
[1869.78 --> 1875.08]  listened to the show just like you're doing right here right now today and heard us talk about top towel
[1875.08 --> 1880.16]  and what they're all about and he decided to get in touch and now he's living the dream as a
[1880.16 --> 1885.02]  freelance software developer with top towel his name is daniel alzon and i sat down and i talked
[1885.02 --> 1891.62]  with him i said hey what is it that you love most about top towel take a listen well for me the the
[1891.62 --> 1897.72]  thing about top towel which i thought would be very hard for me personally as i transitioned to a more
[1897.72 --> 1904.66]  consulting role uh was the way i would have access to new clients and what quality of those would be
[1904.66 --> 1910.82]  so i found that i have had access to awesome clients through top towel and it hasn't been that
[1910.82 --> 1916.22]  hard to find because they have a lot of choice and even more than that uh there's enough choice and i
[1916.22 --> 1922.74]  i can actually be a little selective about what kinds of things i want to be working on so i use that as a
[1922.74 --> 1928.74]  way to sort of hone my skills and you know go towards the technology that i think are worth investing in
[1928.74 --> 1934.32]  for the future so whether it's you know including you front-end frameworks or doing a little devops
[1934.32 --> 1940.36]  work on the side i i usually am able to find clients who are have the needs of the things i want to get
[1940.36 --> 1946.86]  better at so that's been that's been truly useful all right that was daniel alzon a listener of the
[1946.86 --> 1953.74]  change log and also a freelance software developer with top towel if you want to follow in daniel's
[1953.74 --> 1963.48]  footsteps go to top towel.com slash developers that's t-o-p-t-a-l.com slash developers to learn
[1963.48 --> 1967.44]  more about what top towel is all about and tell them the change log sent you
[1967.44 --> 1974.32]  well let's talk about why this conference exists i know that it's its first year obviously it's a
[1974.32 --> 1981.24]  single track we're looking at you know roughly 100 150 to 200 people uh attending uh we know it's at a
[1981.24 --> 1988.46]  zoo and we're playing the animal puns to to the end you know and and and we won't stop um ever
[1988.46 --> 1995.96]  no um so why you know what what made this why finally this year why finally 2015 you know why
[1995.96 --> 2001.84]  did it take so long and why does it exist so that is a that is a very good question why it's happening
[2001.84 --> 2008.04]  this year i think that the final impetus kind of came out of jared's goading me into it because i
[2008.04 --> 2014.26]  had promised so we had a meetup i want to say probably a year and a half or two years ago where
[2014.26 --> 2019.86]  we announced everyone that one of our stretch goals or one of our big goals for the meetup was
[2019.86 --> 2025.04]  to do a conference eventually and so that was kind of on everyone's mind that that was going to be
[2025.04 --> 2034.62]  something we were going to do um but it just kind of sat there nothing ever happened um and i think it
[2034.62 --> 2039.52]  was jared that finally said hey are we going to do this conference ever is this going to happen
[2039.52 --> 2047.50]  and i think that was the the straw that broke the camel's back as it were it's jared's goading us
[2047.50 --> 2053.06]  into uh organizing so i'm actually laughing behind the scenes here too and i'm trying not to put it on
[2053.06 --> 2057.64]  air because that's how a lot of things get started right here at the change law too i'm like i tell jared
[2057.64 --> 2062.60]  these ideas and and he's he gets excited about the ideas and then it's like well are we ever going to do
[2062.60 --> 2070.34]  these fun ideas adam yeah and i'm like i suppose sure let's do it and we do it so jared it's nice
[2070.34 --> 2075.76]  to see that you uh you you uh impact others as well in the same way this is why i have no free time
[2075.76 --> 2085.32]  because i'm constantly filling it with i i go to people you say goat or goat zach i said goad okay i just
[2085.32 --> 2092.52]  wasn't sure if that was another pun uh i i just bug people until we do things and then i'm like oh
[2092.52 --> 2097.20]  dang now we have to do that now we have to do it really just kind of jabbing at them but now we're
[2097.20 --> 2101.06]  put on a conference i guess and i told my wife i'm like well i guess i'm gonna help put on a
[2101.06 --> 2106.34]  conference she's like that sounds like a big thing i'm like is it there's six of us turns out it is
[2106.34 --> 2111.48]  even with six even with six i was gonna say so how does this did we answer the question though first
[2111.48 --> 2117.28]  why it exists i mean jared goading you and not goading you goading you but uh you know what
[2117.28 --> 2121.12]  about the local community what's what's the meetups like you said it came from a meetup so
[2121.12 --> 2126.78]  what was attendance like was it getting bigger is is javascript exploding there as it is everywhere else
[2126.78 --> 2134.54]  yeah i think it is uh the the meetup has grown we have i think over 700 some people on our meetup
[2134.54 --> 2143.88]  uh group on meetup.com slash nebraska js if anybody's interested um and yeah it's just kind
[2143.88 --> 2149.80]  of grown and grown and grown and i think the biggest uh biggest meetup event that we've had
[2149.80 --> 2158.46]  i think had around 80 some attendees and jared was speaking and jared spoke at that one um
[2158.46 --> 2166.14]  yeah so i guess jared was kind of our headliner whoa jared and angular i thought maybe you'd be
[2166.14 --> 2170.40]  talking about react or something like that to get a crowd like that well this was back when angular
[2170.40 --> 2176.78]  was blowing up last year and a half ago pre 2.0 angular right okay right yeah no no hurts against
[2176.78 --> 2184.38]  them just you know bias well as we say open source is hard and right um everybody's out there trying
[2184.38 --> 2190.30]  to do awesome stuff and um yeah kind of the the trends come and go and angular is definitely on a
[2190.30 --> 2197.60]  downtrend as far as overall popularity um or maybe mind share but uh still out there doing cool things
[2197.60 --> 2204.56]  and people right using it in mass so everybody seems to be if you if you put react uh in the title
[2204.56 --> 2213.56]  or if uh if you go the routes of uh of bruce reacting you know a little sleight of hand there
[2213.56 --> 2221.28]  with the title there hold on bruce it's gonna get some so big meetup it got to as many as 80 at one
[2221.28 --> 2227.80]  point jared that was a couple years ago on jared's point um so it got to a point where it just naturally
[2227.80 --> 2234.42]  made sense to put on a conference and this is middle america um one thing i liked about some notes here
[2234.42 --> 2239.84]  which aren't exactly um easy to find for every conference number one you have a shuttle going to
[2239.84 --> 2243.54]  and from the airport which is free which is awesome so anytime i go to a conference i'm like
[2243.54 --> 2248.50]  you know where do i have to like spend money to get to and from because people always assume okay
[2248.50 --> 2254.44]  i'm going to a conference and the airport is gonna be right next door no no that's not always the case
[2254.44 --> 2260.76]  like in denver it was 60 to get to and from the airport oh wow back to like the conference land so
[2260.76 --> 2266.28]  it was it was quite expensive and then you got to do it twice right to and to and from so it's 120
[2266.28 --> 2272.20]  bucks just on uh just on taxi to and from the airport and then you got the walking distance the
[2272.20 --> 2275.88]  after party and things like that so it seems like you guys have done some planning around this to to
[2275.88 --> 2281.70]  to also kick it off yeah we're kind of trying to make it like an all-inclusive resort in omaha
[2281.70 --> 2290.44]  like a sandals as it were yeah at the zoo yeah go to the airport get the shuttle to the hotel we're
[2290.44 --> 2296.44]  gonna have a shuttle to the zoo and back we're gonna have two meals i think it sounds like uh we're
[2296.44 --> 2303.22]  talking about finalizing the evening meal as well so live band live band that's neat yeah yeah that'll
[2303.22 --> 2309.44]  be really cool is that eight bit at the after part that's the live band time yep who is the uh the
[2309.44 --> 2319.48]  band name the super bites super bites that's cool is it a local band or yeah it is um all of them are
[2319.48 --> 2326.56]  local i actually went to high school with two of them the super bites yes all right i just found
[2326.56 --> 2332.90]  them on band camp we'll link this up in the show notes because they are rocking the super mario
[2332.90 --> 2339.90]  style graphics eight bit all the way yeah i think that uh nick don't they do some sampling with
[2339.90 --> 2349.24]  some unique hardware yeah they use a nintendo and a game boy um on stage and they have pre-setup
[2349.24 --> 2356.26]  tracks that they they created on those devices um so it's a really unique experience so that's the
[2356.26 --> 2361.78]  after party and we got all this time so far and we haven't talked about two of the two of the names
[2361.78 --> 2367.44]  i think almost anyone listening to the show might know ethan marcotte and christian i always want to
[2367.44 --> 2372.48]  say it's helman or heelman anybody know the correct pronunciation of christian's last name
[2372.48 --> 2378.92]  i do not what do you think jared i was i will say helman though oh man i was going to go that's what i
[2378.92 --> 2387.58]  all right code poet code poet those are um you know i never read that as code poet jared i i just
[2387.58 --> 2395.96]  took it as code po eight me too all right nice we're learning that's why they pay me the big bucks
[2395.96 --> 2400.28]  that's that's it so ethan marcotte he's doing the closing and christian's starting it off
[2400.28 --> 2406.86]  um what was getting these two involved like i mean how how did it happen did somebody email them was it
[2406.86 --> 2413.04]  you know you bumped into another conference how'd this work out uh so ethan has actually done some
[2413.04 --> 2418.04]  work with uh filament group which is the company i work for so they did the boston globe sort of
[2418.04 --> 2424.98]  redesign which was a huge or one of the biggest responsive web design uh redesigns a few years ago
[2424.98 --> 2429.54]  so they kind of worked together and that's how i kind of got that connection to ethan
[2429.54 --> 2437.68]  and did he come just with uh with open arms or did he have to be coerced uh no he was super excited to
[2437.68 --> 2446.34]  be involved um i did not have to coerce him at all no blackmail uh not that i could say on air
[2446.34 --> 2453.82]  no i'm just kidding there's there was no blackmail at all yeah he's he's uh super excited to come out and
[2453.82 --> 2460.28]  come to the zoo and yeah come to the zoo i like it hang out at the zoo what about christian i mean
[2460.28 --> 2464.16]  he does love for the javascript world and he's he's done all sorts of cool stuff always been a fan of
[2464.16 --> 2473.74]  his so uh you got connections there as well yeah well not quite as tight i would say but uh i i don't
[2473.74 --> 2477.96]  know how it how i got connected to christian originally but i've just kind of followed him
[2477.96 --> 2485.18]  online since i started blogging like back in 2006 or 2007 so i've just kind of been connected
[2485.18 --> 2492.14]  through twitter and blogs online and i saw that he was going to be in the country because he's from
[2492.14 --> 2499.04]  london originally or currently i should say um and so he was going to be in the country and he actually
[2499.04 --> 2504.08]  rescheduled one of his flights back to london so that he could come out and speak so
[2504.08 --> 2511.04]  very very accommodating for us you know one of the things that um that people always get most
[2511.04 --> 2516.92]  concerned about when putting out a conference is one will anybody show up uh two will i get quality
[2516.92 --> 2522.88]  speakers or anything that's worthwhile for people to actually show up for and if they do show up and
[2522.88 --> 2529.96]  the speakers show up too will everybody enjoy it um so i mean knowing all those those three kind
[2529.96 --> 2534.80]  of pillars of fear so to speak when it comes to a conference i just coined that just now by the way
[2534.80 --> 2542.60]  the pillars of fear three pillars of fear you should work at local news i i do work in local news
[2542.60 --> 2549.86]  right here in houston myfox houston.com um no but on on a serious note though so like
[2549.86 --> 2557.34]  around the topics around the keynote speakers was there any it was anybody like you know throwing up
[2557.34 --> 2562.54]  or getting upset or just like really just like ruining their day over just the worry the anxiety
[2562.54 --> 2571.14]  that comes from those three things definitely oh for sure yeah i mean there's a huge amount of stress
[2571.14 --> 2577.50]  that goes into running a conference and we sort of had ethan from the beginning which was uh very good
[2577.50 --> 2583.56]  because that helped us i think get us more exposure and so we had ethan published before we even did the
[2583.56 --> 2589.80]  cfp which i think helped us helped us get a lot more submissions sort of legitimized us as a conference
[2589.80 --> 2598.48]  before we even started um and then we got christian a few weeks ago um but getting the speakers there i
[2598.48 --> 2607.36]  think is just one small piece one small pillar in the pillars of fear as it were um there's yeah there's
[2607.36 --> 2614.28]  just so many other things that uh are going on that you have to worry about as well so um logistics are
[2614.28 --> 2619.54]  kind of a nightmare when it comes to conferences what about financing and receding and things like
[2619.54 --> 2625.02]  that how does that play out with the six organizers you have how does the responsibility and the financial
[2625.02 --> 2630.00]  responsibility and things like that play out and like who ponies up the first dollar how does it work
[2630.00 --> 2636.36]  that's my biggest like how do you actually do a conference so i mean though all the organizers
[2636.36 --> 2644.68]  sort of ponied up a fixed sum to get the because we formed an llc um to get it started and then
[2644.68 --> 2649.84]  uh sponsorship and sponsorship dollars started rolling in and we started doing ticket sales and so
[2649.84 --> 2657.40]  we've been able to sort of stay ahead of the game in terms of uh paying receipts or paying invoices
[2657.40 --> 2662.54]  so a legitimate business was set up to to sort of be the crux of this thing not just
[2662.54 --> 2669.20]  not just hey you're you know you're like in jared's case like object lateral or any of your guys
[2669.20 --> 2674.82]  businesses like it didn't mix you created your own organization and and took some ownership in it to
[2674.82 --> 2681.20]  a degree right yeah i don't know if i'd throw around the word legitimate that lightly but um certainly
[2681.20 --> 2688.58]  uh an llc was formed the state of nebraska thinks we're legitimate that's yeah that's correct we can go
[2688.58 --> 2694.24]  okay yeah well that's all you gotta have right there yeah okay so this is very much like setting
[2694.24 --> 2697.96]  up a you know a real live business basically i mean you're gonna at the end of the year you're
[2697.96 --> 2703.80]  gonna have uh you know you're gonna have pass through tax to somebody uh somebody's on the
[2703.80 --> 2707.78]  hook for some of this money if there's any profit right that's the goal that's why i said no profits
[2707.78 --> 2712.64]  there's your goal right there right no profits is the goal yep okay i'm just thinking like yeah
[2712.64 --> 2719.36]  insurance is a concern um you know we set up an llc because uh there's some guard you know
[2719.36 --> 2727.38]  personal protections there against things going wrong um yeah cash flow actually for us i've been
[2727.38 --> 2732.16]  surprised i thought cash flow would be a big problem uh aside from that one sponsorship thing that zach
[2732.16 --> 2737.30]  talked about we've actually been pretty cash flow positive as far as the down payments we have to put
[2737.30 --> 2745.72]  to reserve things and that this and that um i think had sponsors not stepped up um so generously
[2745.72 --> 2750.58]  right away i think it would have been a lot harder sledding because we would have make tighter decisions
[2750.58 --> 2756.20]  and wait on things and you know hope rely on ticket sales so we've been really fortunate that there's so
[2756.20 --> 2763.66]  many great sponsors here locally that hopped on board like right away yeah the sponsors were just like
[2763.66 --> 2767.64]  i feel like they were waiting for something to come around like this so they could jump on board
[2767.64 --> 2775.00]  really because it it took very little coaxing to get sponsors so was it sponsors first speakers second
[2775.00 --> 2780.20]  is that i mean because just thinking from a cash flow standpoint you think about sales to a degree and
[2780.20 --> 2785.44]  you got to get sales to put a product out there and the product is the conference you can't put the
[2785.44 --> 2790.18]  conference until you get sponsors to commit and speakers to commit and things like that so
[2790.18 --> 2795.36]  and you got to have a place to call home so you can't get that until you put some money down so
[2795.36 --> 2800.48]  it seems like this never-ending chicken chicken and egg scenario for at least for a first-time
[2800.48 --> 2806.80]  conference you know first year yeah well luckily a lot of our speakers have deferred reimbursement until
[2806.80 --> 2815.44]  the day of the conference um so that kind of helped us in the beginning but uh i mean our sponsors
[2815.44 --> 2822.88]  really were so excited to get involved that we had we had a pretty good uh sum to get start start paying
[2822.88 --> 2829.08]  our bills very early and i think it also helped that we refused to put people on the website until we
[2829.08 --> 2835.02]  got payment so we wouldn't put anybody's logo on there until we got money so that's a good rule to
[2835.02 --> 2841.58]  have right there yeah yep we're getting uh close to the end of the show let's take one more break uh
[2841.58 --> 2846.30]  while we have some time to hear a word from one of our awesome sponsors making this show possible
[2846.30 --> 2851.30]  when we come back we're going to talk about some closing topics like uh collaboration tools for
[2851.30 --> 2856.60]  the team uh i like that little note there jared didn't quite think about the collaboration necessary
[2856.60 --> 2861.62]  behind the scenes and then you know the other thing i mentioned which was the fear of nobody showing
[2861.62 --> 2866.04]  up i'm kind of curious what y'all think about that so let's pause here uh listen to this awesome
[2866.04 --> 2869.96]  sponsor and then we come back we'll talk about those things so right back
[2869.96 --> 2877.92]  hip chat is a game changer for team communication it helps you and your team get the information you
[2877.92 --> 2883.90]  need faster than email and reduces meaningless meetings teams that use hip chat are able to make
[2883.90 --> 2891.48]  faster decisions and get more work done with group chat video chat and file sharing hip chat is a great
[2891.48 --> 2895.88]  solution for distributed teams by letting you take the office with you no matter where you go
[2895.88 --> 2904.28]  iphone android mac os it's all there hip chat is easy to use and gets everyone working in real time
[2904.28 --> 2910.96]  and right now hip chat is offering listeners of the changelog 90 days of hip chat plus totally free
[2910.96 --> 2917.06]  get premium features like unlimited file storage unlimited message history and guaranteed support
[2917.06 --> 2925.84]  totally for free for 90 days visit hip chat.com slash changelog again that's hip chat.com slash changelog
[2925.84 --> 2932.94]  get your team started using hip chat plus today go and check them out all right we're back to close
[2932.94 --> 2941.28]  up the show with nick zach and jared talking about javascript in the wild here in the middle america
[2941.28 --> 2946.70]  nebraska man i mean i'm excited to get there for one jared i haven't visited yet so that's you know
[2946.70 --> 2952.62]  i'm so excited to finally come out to omaha uh i've already done some business with local places around
[2952.62 --> 2958.70]  there ink um what's it uh the ink tank there yeah i've done some business with them you know
[2958.70 --> 2964.50]  work with you and stuff like that but not hadn't visited this this uh fabulous place and there's
[2964.50 --> 2969.54]  finally a reason to go which is this javascript conference we're talking about here and i guess
[2969.54 --> 2976.68]  since we're talking about showing up nick did you have any concerns yourself like did you you said yes to
[2976.68 --> 2982.32]  the anxiety earlier but you didn't elaborate so can you elaborate a bit on this idea of no one's
[2982.32 --> 2986.14]  showing up the fear of nobody's showing up for a conference and and you being an organizer of it
[2986.14 --> 2992.60]  sure i i guess now at this point i'm not worried too much about people showing up just seeing the the
[2992.60 --> 2997.22]  ticket sales and the the positive comments that we've gotten but that was definitely a concern going
[2997.22 --> 3002.88]  into it just i'm not sure you know if anybody will think that this is a good idea but as as zach
[3002.88 --> 3009.24]  mentioned getting ethan on board right away really helped to as he said legitimize it um the thing
[3009.24 --> 3016.78]  that's really scary now is we're you know we're 16 days away from it at this point and there's so much
[3016.78 --> 3023.88]  left to do um we have all of these tickets and things kind of these plates still spinning um and then
[3023.88 --> 3029.24]  you know we'll get all of that settled in and be ready for the conference the day of and then you know
[3029.24 --> 3035.46]  i'm just my biggest fear is waking up in a cold sweat that morning and realizing we forgot microphones
[3035.46 --> 3042.58]  or something like you know something so necessary and so yet so small that we just kind of overlooked
[3042.58 --> 3047.92]  it i'm really scared of of that but i think that will be will be fine it's just a a terror thing that
[3047.92 --> 3054.72]  i have i guess uh but then finally just will people have fun will they enjoy the talks uh will there be
[3054.72 --> 3060.08]  technical problems there that we have to deal with on the spot will there be um yes there will be
[3060.08 --> 3066.10]  yeah yes every time is somebody going to get mauled by one of the animals that we have
[3066.10 --> 3071.38]  coming into the conference like uh hopefully not i don't even know what kind of animals we're having
[3071.38 --> 3079.76]  but elephants hopefully a porcupine yeah elephants porcupines lions kitty cats no i mean i think we
[3079.76 --> 3085.58]  porcupine is one of the animals that we might have so yeah i've heard that tarantulas possible maybe
[3085.58 --> 3093.16]  i need to increase that insurance deductible talk about that offline glad it's an llc yeah all right
[3093.16 --> 3098.26]  so let's something that you quite kind of mentioned there nick it seemed like just this organization
[3098.26 --> 3107.10]  process behind the scenes with the rest of the six so you got six people that joined the nejs team to
[3107.10 --> 3113.10]  to put this conference on this year what are some of the things that you've done who spearheaded it
[3113.10 --> 3119.10]  was it anyone was there like a a distinct leader was it sort of like all self-managed to come up with
[3119.10 --> 3124.52]  checklists and like or did you sort of divide up in teams how did the how did y'all work to collaborate
[3124.52 --> 3129.04]  i guess since you don't work in the same office obviously because this is not like a legitimate
[3129.04 --> 3134.04]  business as you've said this is a conference and you got your own things to do how did you you know
[3134.04 --> 3139.64]  collaborate day to day to to make these things happen over time i think that we all kind of
[3139.64 --> 3145.58]  we're all very self-driven and can work autonomously on things we kind of knew what things at a high
[3145.58 --> 3150.68]  level we needed to tackle uh if there is a distinguished leader it'd definitely be zach
[3150.68 --> 3156.22]  um he kind of you know started putting things together organizing things organizing ways that we
[3156.22 --> 3161.80]  can communicate and i think it was either zach or jared that recommended using trello for
[3161.80 --> 3167.94]  organization so we've been using that and just adding having lists of things to do and different
[3167.94 --> 3172.14]  stages for that and having everything as a card in there and it's it's been working out pretty well
[3172.14 --> 3178.20]  yeah trello is amazing i don't i don't think we could have organized a conference without it
[3178.20 --> 3186.52]  yeah well we uh we're in trello all day long we use it to do change law weekly so i know we can
[3186.52 --> 3193.22]  high five you on that one there uh i could tell you more stories about trello and agree with you
[3193.22 --> 3197.92]  but i'll just leave it that that i agree that trello is super awesome uh there isn't a tool out there
[3197.92 --> 3204.82]  that quite meets what it does for organizing for organizing people and the whole agile process whether
[3204.82 --> 3209.74]  you're doing software or not it's just really flexible to however you want to work yeah in addition
[3209.74 --> 3214.52]  to that you know we've i've been taking cues as adam and i have traveled around to conferences this year
[3214.52 --> 3221.14]  um we're at space city js in the spring and y'all know we're at gopher con a few weeks back so as i
[3221.14 --> 3226.26]  go to these conferences i'm very cognizant of like how they're running things because i'm involved and
[3226.26 --> 3230.26]  one of the things that space city did which i think was cool and i think more conferences will start
[3230.26 --> 3235.64]  doing is to open up a slack team for the entire conference so all the attendees can hop in there
[3235.64 --> 3241.22]  and so we did that recently uh for any js in addition to that we have kind of an organized
[3241.22 --> 3247.00]  private room and a room for speakers and um one thing about trello is it's not great for just
[3247.00 --> 3254.24]  discussion you know uh it can get a little bit cumbersome for that yeah and we didn't realize it
[3254.24 --> 3258.20]  but we were doing too much just like chatting inside trello because we didn't have an auxiliary tool
[3258.20 --> 3266.08]  and so in the last month or so zach sent up a slack team and that has really um balanced out where we
[3266.08 --> 3272.32]  have kind of your immediate needs quick feedback you know paste a stupid gif in their chat room
[3272.32 --> 3277.62]  and you have trello which is all about the organized you know assigned things that need doing i think
[3277.62 --> 3285.14]  that's really been a good combination of tools for us slack is the party in the front and uh
[3285.14 --> 3289.80]  trello's the business in the back yeah really rounding out the any js mullet that we're going for here
[3289.80 --> 3299.92]  i like it another important topic which i which we saw you know jared since you mentioned go for
[3299.92 --> 3307.58]  gone um i loved their idea of a diversity scholarship did the jaw take some cues from that or was it
[3307.58 --> 3312.40]  somewhere else but you seem to be focused on the inclusivity and the accessibility of the conference
[3312.40 --> 3318.64]  so what was this diversity scholarship about and and what were some i guess has there been anybody to
[3318.64 --> 3327.70]  take the the free ticket how was that process like yeah so we uh we are doing diversity scholarships um
[3327.70 --> 3334.50]  we're through a local company called big wheel brigade they've offered 10 free tickets um for people
[3334.50 --> 3342.70]  underrepresented in tech uh whether that be gender sex sexuality race or veteran status or any number of
[3342.70 --> 3350.80]  other things um and we've had i think people i think we've redeemed almost half of those tickets um and
[3350.80 --> 3358.54]  they are confidential so uh to other attendees that your badges are going to be different or anything
[3358.54 --> 3365.94]  it'll you'll the ticket will be identical to any other attendee ticket um but i think we've only uh
[3365.94 --> 3372.14]  redeemed half of those so far are there any caveats to that like what's what's the criteria to
[3372.14 --> 3378.94]  to meet the is it even you guys that take care of this or is it is it totally through a big wheel brigade
[3378.94 --> 3383.80]  that that they handle that i see beth's name here i'm just wondering if she is totally taking over that
[3383.80 --> 3389.90]  at all at all points yeah she is the point of contact for that so she actually will go out and buy the
[3389.90 --> 3394.68]  tickets on our website using a special coupon code that we have for her um and so
[3394.68 --> 3400.58]  yeah that's kind of how that sponsorship works and there's really they really aren't doing any
[3400.58 --> 3408.34]  question or interrogation involved with that they just will hey you want a ticket okay here's you
[3408.34 --> 3415.40]  um here's the information that we need and we'll buy it for you so it's not like a formal thing that
[3415.40 --> 3421.76]  you have to go through like an application process it's really just hey i would like to go to this
[3421.76 --> 3427.82]  conference they'll get you a ticket so i like the the paragraph here under that form too because i
[3427.82 --> 3435.36]  think this is everybody approaches this um this topic you know sort of on their tippy toes because
[3435.36 --> 3439.70]  no one wants to offend anybody but i like this bolded text you have here if you would like to take
[3439.70 --> 3445.66]  advantage of this offer but are hesitant to publicly self-identify as belonging to an underrepresented
[3445.66 --> 3451.18]  group please be assured that you will be that we will receive your request with acceptance
[3451.18 --> 3455.76]  and respect and will keep it confidential so i think it's it just going the extra mile to
[3455.76 --> 3462.18]  one be inclusive and accepting of of everyone and giving everyone an opportunity to be there
[3462.18 --> 3466.42]  especially underrepresented so that's really neat that that the way you've handled this and even
[3466.42 --> 3472.16]  having an outside company sort of uh one sponsor it and pay for those tickets and then just have a
[3472.16 --> 3476.88]  process for it seems like you really thought this through so i like it yeah i think it worked pretty
[3476.88 --> 3483.48]  well they actually ran a little like seminar not too long ago on um sort of running uh inclusive
[3483.48 --> 3491.86]  events and dealing with sort of problems that can arise when you're an event organizer right which has
[3491.86 --> 3496.50]  been really helpful and that's kind of where we got the idea to do something like this so so we got five
[3496.50 --> 3503.08]  more of these diversity scholarship tickets available so if you're listening and you're a part of one of
[3503.08 --> 3510.60]  those groups uh i just read that uh that that text there you'll be uh it'd be accepted and respected
[3510.60 --> 3517.18]  and more importantly confidential so uh feel free to get in touch and take advantage of this if you're
[3517.18 --> 3524.06]  in one of those groups um cool what's uh what's some closing thoughts jared help me out here with some
[3524.06 --> 3528.10]  closing thoughts i know we normally have some closing questions and you're sort of not playing
[3528.10 --> 3533.76]  interviewer yeah i mean i think closing thoughts is um obviously there's still a handful of tickets
[3533.76 --> 3540.74]  available uh omaha is a really cool city um centrally located so if you're anywhere in the midwest it's
[3540.74 --> 3545.68]  actually pretty easy to get over here we'd love to have you changelog will be there especially at the
[3545.68 --> 3551.92]  after party and shooting our awesome film series beyond code so um you'll get to meet adam and myself
[3551.92 --> 3559.34]  and dk our video guy um yeah we just hope it's a good time where we've been uh trying to line up
[3559.34 --> 3566.72]  all our ducks in a row and um so far you know we've had a few uh freak out events but i think we've
[3566.72 --> 3575.00]  pulled together as a team and are uh feeling pretty good about how it's going to uh to turn out i think
[3575.00 --> 3580.16]  one one thing we didn't talk about which i forgot until just now is the hardest part of the whole
[3580.16 --> 3586.32]  conference for us was probably naming it um and maybe that was why it took so long for us to come
[3586.32 --> 3592.86]  up with the conference because we went through dozens and dozens of names trying to be witty and
[3592.86 --> 3601.02]  cool yeah and uh around and around and around we went and eventually we realized we're not witty and
[3601.02 --> 3607.68]  we're not cool so we're just gonna know we're just gonna name it with our using our need our meetups name
[3607.68 --> 3612.40]  um i don't know maybe nick can you remember any of the names that we had on the table i know the
[3612.40 --> 3618.20]  the one that was kind of a front runner for a while was flyover js um because we're you know
[3618.20 --> 3622.22]  the brass is kind of one of those flyover states but we had tons of them can you think of any others
[3622.22 --> 3631.72]  oh man um that was the one that really came to mind that was my favorite for a long time um we also had
[3631.72 --> 3638.28]  well there was one that that we wanted right off the bat but it was taken as there's another
[3638.28 --> 3646.62]  conference with the same name right um yeah i can't i can't remember exactly we had bullseye js
[3646.62 --> 3655.46]  central standard js heartland js bug eater js bug eater yeah that's kind of a thing i think a thing
[3655.46 --> 3659.72]  that people outside of nebraska will have no idea what a bug eater little web on the prairie
[3659.72 --> 3666.78]  that was one of yours zach there was oh yeah there were spreadsheets and talking about arguments
[3666.78 --> 3673.92]  um you know nothing quite as argumentative as your favorite name not liked by your by your co-patriots
[3673.92 --> 3677.36]  so so what about the subtitle then will that remain
[3677.36 --> 3684.42]  each year will it i mean will it always be at the zoo i guess you'll probably know more after this year
[3684.42 --> 3691.56]  if if things go badly but somebody gets eaten for example um we come back with one less javascript
[3691.56 --> 3696.72]  drop there because uh the lion got hungry but i mean will it always be javascript in the wild or do
[3696.72 --> 3702.42]  you think you'll kind of keep mixing it up each year i think we'll probably try a different venue next
[3702.42 --> 3707.22]  year i don't know it depends on how it goes obviously but i didn't expect that we would do
[3707.22 --> 3712.48]  uh at the zoo every year so okay well it's nice to show some love to different areas
[3712.48 --> 3720.34]  well i guess uh i don't really have any more questions myself um i'm used to always asking
[3720.34 --> 3726.16]  some of the the the famous questions at the end does anybody feel totally strong on on answering the
[3726.16 --> 3731.70]  who's your programming hero question jared you never get asked that question you're always on the other
[3731.70 --> 3740.48]  and how about you i want to have a hero i'm gonna pass this one on to nick he's your hero or no i want
[3740.48 --> 3742.26]  i want to know nick's hero oh fine
[3742.26 --> 3750.78]  i mean i can answer it if you don't want to nick that's fine i'm going to to pass it along to zach
[3750.78 --> 3757.44]  and also just name zach that's my oh wow zach wow that's a low bar nick
[3757.44 --> 3765.88]  um i i want to say john rezik i think that not in terms of necessarily like i mean he's a very
[3765.88 --> 3773.78]  super talented programmer obviously but i think the way he ran the the jquery community is just kind of
[3773.78 --> 3780.30]  an amazing thing and he definitely grew a very uh inclusive and welcoming community and i think a lot of
[3780.30 --> 3788.86]  that was just because of his personality um and yeah maybe that dates me a few years but i don't
[3788.86 --> 3794.36]  think it dates you i mean i think uh if i had to put if i had to make a list of many heroes john would
[3794.36 --> 3799.80]  definitely be in the list because of the same reasons he sort of came out of the cut too with
[3799.80 --> 3805.64]  jquery he just shared it one day in boston at a meetup which is sometimes how the best software comes
[3805.64 --> 3812.76]  out out into the open source public and then you know you know there was several other ways that
[3812.76 --> 3818.32]  you could do what jquery did uh well there weren't that many but jquery sort of made it a really easy
[3818.32 --> 3823.42]  to learn and then even the way like you said the community sort of sprouted up around it it seems to
[3823.42 --> 3830.58]  just grow really really fast yeah so and then john is always he's never really backed down from
[3830.58 --> 3834.56]  giving talks and organizing and speaking in front of people and stuff like that i know that
[3834.56 --> 3841.08]  we've never had him on this show because never emailed him but nonetheless um we would like to
[3841.08 --> 3846.94]  have john the show at some point we just never have i guess with that uh is there anything else you
[3846.94 --> 3852.50]  want to cover about the the conference or heroes or anything else that might be on anyone's mind that
[3852.50 --> 3858.36]  we can maybe a particular sponsor i did want to say one thing i guess not related to sponsorship but
[3858.36 --> 3864.64]  the the the thing that i think i've learned the most about running a conference has been how difficult
[3864.64 --> 3870.58]  it is and you definitely see when you attend conferences you see those in a new light and i i guess
[3870.58 --> 3879.30]  i would encourage everyone out there to uh the next time you go to a conference if personal space is not
[3879.30 --> 3885.98]  an issue for you hug your conference organizer because it is a ton of work it's a ton of work and it's
[3885.98 --> 3892.06]  sometimes very thankless work um and people are doing these development community conferences
[3892.06 --> 3896.94]  not for money there's a lot of conferences that are just sort of community driven
[3896.94 --> 3902.86]  um and people are doing them sort of as a labor of love just to grow their local development community
[3902.86 --> 3910.20]  and sort of give them give the community uh more exposure in a wider sense so definitely give some
[3910.20 --> 3918.34]  love to your organizers if if you uh see them i'd just like to thank the the local community you
[3918.34 --> 3923.80]  know omaha has a great development community and uh they're very inspiring everyone is always
[3923.80 --> 3929.08]  passionate about what they're working on and you know aside from jared motivating us to get this
[3929.08 --> 3936.44]  started uh you know it's really the community that that was doing it too just the the number of
[3936.44 --> 3940.92]  people here that that just do great things is is huge and we want to be able to share that with
[3940.92 --> 3946.68]  the world well i think uh i can agree on on jared's help there he's helped me out a lot quite a bit
[3946.68 --> 3952.02]  making things happen whenever i'm like himming and hawing so jared you seem to seem to seem to do it
[3952.02 --> 3959.46]  everywhere man so good for you on that part uh so just to just to summarize uh any js conf is on a
[3959.46 --> 3965.82]  friday august 7th there are still tickets available if you're in a marginalized or underrepresented group
[3965.82 --> 3975.46]  there is there is is is uh five more confidential tickets uh that you will be respected so um submit
[3975.46 --> 3980.80]  your information for that if you'd like to take advantage of that uh for those of you out there who
[3980.80 --> 3986.08]  are thinking about this awesome conference it's it's all about animals elephants at the zoo
[3986.08 --> 3991.78]  uh javascript getting wild so it's it's going to be in the wild javascript in the wild
[3991.78 --> 4005.42]  so exciting exciting times here so um the website to go to is what nejsconf.com correct i'm noticing uh
[4005.42 --> 4009.58]  i'm noticing like an ssl issue on your site is there an ssl issue on your site i hope not
[4009.58 --> 4019.04]  no so it should be subdomainless so it should be just nejsconf.com not www that's right yeah we don't
[4019.04 --> 4025.16]  like that stuff that's that's uh that's the way the four extra characters you gotta take yeah nobody
[4025.16 --> 4030.14]  needs that nobody needs that so if you're interested in this conference the changelog will be there
[4030.14 --> 4036.28]  we'll see you there uh hop on camera say some things for beyond code uh jared i didn't tell you this
[4036.28 --> 4042.06]  we're we got a new piece of equipment we're bringing uh with us that everyone's gonna love
[4042.06 --> 4049.78]  so no drones no drones not yet that's that's maybe sometime soon uh but the equipment we're
[4049.78 --> 4055.52]  bringing this time is a steadicam so we're pretty excited about this because we'll be able to walk
[4055.52 --> 4063.04]  and like follow people or like you know just move lightly with the camera they call it flying
[4063.04 --> 4067.50]  with the camera but nonetheless excited about that new piece of equipment so every time we go to a
[4067.50 --> 4073.86]  conference we go with something that uh is some sort of new toy that dk likes to play with um so
[4073.86 --> 4080.78]  this would give dk a chance to fly his uh the camera around and get some good shots and have some fun so
[4080.78 --> 4088.80]  we're excited about that so anygsconf.com go there and get your ticket we'll see you there on august 7th
[4088.80 --> 4094.56]  it's a friday at the zoo with the elephants and the rest of the jobs community and uh with that
[4094.56 --> 4098.46]  everybody let's let's close the show out and say goodbye see ya thanks see you guys
[4098.46 --> 4100.46]  you
[4118.80 --> 4130.46]  you
[4130.46 --> 4132.46]  you
[4132.46 --> 4134.46]  you
[4134.46 --> 4136.46]  you
[4136.46 --> 4138.46]  you
