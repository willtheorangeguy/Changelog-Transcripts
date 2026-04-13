[0.00 --> 15.42]  welcome back everyone this is the changelog and i'm your host adam stikowiak this is episode 180
[15.42 --> 22.50]  and on today's show jared and i are joined by mitchell hashimoto vagrant fame auto fame
[22.50 --> 27.90]  hashi court fame and it's so great having a guest like mitchell back on the show
[27.90 --> 33.30]  this is mitchell's third time on the show as a matter of fact and what's most interesting about
[33.30 --> 38.82]  this is that mitchell has built his company on top of his open source and it's so nice to have
[38.82 --> 43.82]  guests like mitchell back on the show to share all they're doing to share all their learning
[43.82 --> 49.00]  and to just keep sharing what they're doing in open source so it was awesome having him back
[49.00 --> 55.84]  we had four awesome sponsors for the show code ship braintree backblaze and also linode
[55.84 --> 62.82]  our first sponsor is code ship a long-time supporter and huge fan of the changelog head
[62.82 --> 68.60]  to codeship.com slash the changelog to check out what they do in continuous delivery continuous
[68.60 --> 74.46]  integration check out their blog we feature every single week in changelog weekly you can easily set
[74.46 --> 79.38]  up continuous integration for your application in just a few steps and deploy your code when your test
[79.38 --> 85.54]  passes and code ship get started today with their free plan when you upgrade to a premium plan use our
[85.54 --> 91.54]  special code the changelog podcast that will get you 20 off any plan you choose for three months
[91.54 --> 97.62]  head to codeship.com slash the changelog to get started and now on to the show
[97.62 --> 110.04]  welcome back everyone we're here with mitchell hashimoto founder of hashi corp and mitchell you have to
[110.04 --> 114.86]  forgive me because i know sometimes people say hashi and some people say hashi so you can probably
[114.86 --> 121.76]  correct me or us on that but you're the creative auto and vagrant and packer and surf and console
[121.76 --> 128.40]  you're an o'rally author and a developer that's obsessed as you say with automation so this is a
[128.40 --> 133.82]  three-peat for you welcome back to the show thanks thanks again for having me and we of course got
[133.82 --> 139.50]  jared santo on the line jared say hello hey everybody happy to be here happy to this might
[139.50 --> 145.76]  be our third three-peat guest which would be the triple three-peat which is i think he should win
[145.76 --> 152.00]  something don't you think i wish we had something more than t-shirts to give away i did get a t-shirt
[152.00 --> 158.30]  from from you at uh gopher con i think so all right cool well we can uh i'm gonna send you three more
[158.30 --> 163.34]  we'll send you three more so yeah this is this is a three for you mitchell if you didn't know
[163.34 --> 171.02]  uh third time on the change log first one was with win back in episode 72 that was february 9th 2012
[171.02 --> 178.90]  so that was not very long after you uh founded hashi corp or hashi corp and uh episode 88 was your
[178.90 --> 184.06]  second one so not far after that that was may 15th 2013 that was me and andrew talking to you then
[184.06 --> 189.26]  and like i said for reference this show we're doing today that everyone's listening to is episode
[189.26 --> 196.76]  180 so big uh you know 72 episodes later so lots changed since uh since the last time you've been on
[196.76 --> 202.54]  the show but i guess for those who may not have gone back and listened to 72 or 88 what's a good way
[202.54 --> 209.12]  we can intro intro you to the to the audience of the change log uh i think i think it matters if you're a
[209.12 --> 215.38]  developer i think that the the most like uh the most well-known thing would be as the creator of
[215.38 --> 221.56]  vagrant um could be the most interesting and since then i've just been working on a lot more stuff
[221.56 --> 229.44]  spent a few years uh basically focusing uh moving along from developers more towards operators and
[229.44 --> 234.94]  security and it and like that side of things um and i think very relevant to what we'll talk about today
[234.94 --> 242.40]  uh most recently have been swinging back full force to developers so uh yeah that's that's sort of it
[242.40 --> 250.44]  right now at a very abstract sense in uh the intro i said hashi hashi which one is it well if you're
[250.44 --> 258.34]  speaking japanese it's uh hashi but if i mean either way is really fine it's it's phonetically fine to me
[258.34 --> 264.58]  okay i always wonder if i'm like because i know you would it's it extends from your last name so it's
[264.58 --> 270.06]  you know it's kind of rooted in your identity who you are so i didn't want to like you know say your
[270.06 --> 274.14]  name correctly or say your name incorrectly also your company name incorrectly so if there was a
[274.14 --> 281.54]  right way let's uh let's establish that so we can not deviate um sure i mean it's the correct way
[281.54 --> 287.56]  is hashi corp okay i think maybe developers were used to or even influenced to say hashi corp because
[287.56 --> 293.34]  we're used to doing things with hashes so oh yeah that could be it you know and then and i guess if
[293.34 --> 298.94]  they didn't know you or your last name they might even think that uh your name is a play on a hash for
[298.94 --> 306.14]  for some reason maybe yeah i haven't personally gone back and re-listened to 72 or 88 in prep for
[306.14 --> 312.30]  this call just because i think me i was lazy um but i can't imagine we did a great job of sharing some of
[312.30 --> 318.24]  your history and just while preparing for this call i still belong to this article from business insider so
[318.24 --> 323.48]  i thought it'd be kind of interesting to start this show with a bit more depth on not so much just
[323.48 --> 328.44]  what you produce and what you and your team and your company produce but a bit about who you are
[328.44 --> 333.60]  first um and i think this this is an interesting article because the title of the article is
[333.60 --> 340.00]  a 25 year old coding genius was making half a million dollars a year in college and he just raised
[340.00 --> 345.82]  10 million for a startup and i mean that's a bold title for one but i read this article
[345.82 --> 351.76]  and i was just like wow man what a rich history you have getting into computers right like you got
[351.76 --> 355.82]  your parents opposition and just some things that happened when you were young i mean the first
[355.82 --> 362.72]  tech startup you did was in when you were 12 so someone can go read that article and get the same
[362.72 --> 368.24]  thing but i was just hoping you can share some some thoughts and some history of who mitchell is to
[368.24 --> 373.94]  the audience sure um i want to start by making if you do go back and read that article i want to
[373.94 --> 381.76]  start by making a few corrections uh the the article article portrays uh my parents sounding a lot
[381.76 --> 389.28]  uh meaner or disapproving than they were um so it's it's it's harsher than it should be let's just put
[389.28 --> 396.90]  it that way but um sort of yeah i mean i started i picked up programming when i was 12 and uh i don't
[396.90 --> 402.88]  consider myself a genius by any means but i you know i've been doing it a long time so i have sort of
[402.88 --> 408.44]  that uh behind me and and one thing i noticed going back in my history is that i've always been
[408.44 --> 413.30]  passionate about automating things i mean i got into programming because i like to automate things
[413.30 --> 421.42]  that when i was 12 i was automating uh video games so not cheating them in the sense of pretending the
[421.42 --> 427.84]  human was playing versus you know circumventing uh certain things so i was actually playing the game
[427.84 --> 435.46]  but using a computer code i guess and uh that's how i sort of gotten into trouble as the article i
[435.46 --> 441.32]  think mentions um i was automating games and and some game publishers game makers didn't like that so
[441.32 --> 448.10]  i got into some trouble there uh stopped doing that but i sort of moved on into uh legal things after
[448.10 --> 455.16]  that and and created a small business that automated the setup of php forums i created
[455.16 --> 464.28]  um a small business in college that automated getting you into classes you want um i for fun
[464.28 --> 470.52]  created continue to create sort of like game bots but just for myself just for fun um and it sort of
[470.52 --> 475.38]  led to where i am today where if you look at um all the all the stuff i've built it's around
[475.38 --> 482.80]  uh better automation around developers operators uh data centers that sort of stuff um and you sort of
[482.80 --> 491.18]  alluded to it but uh yeah i mean i i sort of uh wasn't sure if like computer programming was going
[491.18 --> 496.08]  to be the thing i did professionally it was really just something i love to do um i sort of viewed it
[496.08 --> 501.88]  uh with concern of whether it was a real career or not compared to like a doctor or a lawyer or the
[501.88 --> 508.94]  more traditional you know quote unquote real careers um but i got really lucky my freshman year in college
[508.94 --> 515.54]  um i got a pretty for a freshman i got a really good uh job as a developer at a consultancy and
[515.54 --> 522.90]  uh i think that really proved uh not only to to people around me but to myself that this could be a
[522.90 --> 529.64]  pretty good career you know as a naive 18 year old i i had no idea you know how uh how good of a job
[529.64 --> 535.62]  being a programmer could be was it really a half a million dollars no so that's a great one uh it
[535.62 --> 540.58]  wasn't half million dollars a year uh it made quite a bit of money but it wasn't quite that much
[540.58 --> 547.06]  uh it was i guess i would just say it's it was low six figures per year and uh i eventually sold that
[547.06 --> 553.32]  business yeah can we camp out on the game cheats for a second because that that that has my interest
[553.32 --> 559.92]  uh yeah so when you said that i usually thought like game genie back in the day i don't know if
[559.92 --> 565.24]  that but this was like web games can you explain how how are you cheating the games and how did you
[565.24 --> 569.72]  like as a 12 or 13 year old how'd you figure out you could do this and how'd you get into that
[569.72 --> 575.14]  yeah so it wasn't cheating like game genie although i i certainly had a game genie and that was fun but
[575.14 --> 581.84]  that wasn't what i was doing um i was cheating in the sense of botting um so i was i i wanted i wrote
[581.84 --> 587.88]  programs that would play the game for you as if you were as if it were a person um and that fascinated me
[587.88 --> 595.66]  in a lot of ways and so uh the game i was cheating at the time primarily was neopets um not because i
[595.66 --> 601.30]  cared about it in any particular way i don't even know that game what is it it's just like a web game
[601.30 --> 606.54]  that you it's sort of like you know you get a pet you play games you get virtual currency you buy
[606.54 --> 611.78]  things i don't know it's you live like a it's like a really weak second life wasn't there also like a
[611.78 --> 616.26]  device you can take with you that was part of the neopet it's tamagotchi not what i played maybe they
[616.26 --> 621.32]  went that direction eventually not what i played uh but i mean i wasn't that interested interested in
[621.32 --> 626.92]  the game itself actually like i found it because uh it seemed like an interesting target so to speak
[626.92 --> 635.02]  uh of of botting um so i just wanted to see if if using bots could i make a ton of this virtual
[635.02 --> 640.82]  currency and and win the game basically uh and and i had a lot of fun doing that did someone teach
[640.82 --> 645.92]  you how to bot or would you just figure it out were what could javascript how were you coding then
[645.92 --> 653.58]  i was coding in visual basic and uh i found it by so my first google search ever i remember googling
[653.58 --> 660.16]  for it was how to not google search ever but google search related to this ever um was how to make an
[660.16 --> 665.60]  exe i was on windows at the time and i just wanted to know i mean i had this weird realization
[665.60 --> 671.72]  when i and i was 12 at the time that you know i was double clicking these exes and using them on
[671.72 --> 677.84]  my windows computer and i was like wait a minute someone made this and so i suddenly became curious
[677.84 --> 682.08]  where i was like if someone made this then how did they make it and why can't it be me to make
[682.08 --> 689.18]  something like this so i started googling uh how to make an exe which i remember also had awful results
[689.18 --> 695.28]  like didn't really solve anything for me but i just kept poking around at google searches until i started
[695.28 --> 704.08]  finding a little bit more um it led to visual basic eventually and i used visual basic i'm also
[704.08 --> 711.68]  kind of curious about the the business that you were running or starting in uh unless jerry unless
[711.68 --> 714.94]  you got more on the on the games piece you want to dive into i don't want to take away from that
[714.94 --> 723.06]  no i i got my fill thanks okay i'm curious in college um i'm reading back in the quotes it actually
[723.06 --> 729.78]  says um i was pulling in about a half a million a year he said so that's you saying that so that's
[729.78 --> 733.30]  what you told business inside when you're doing this uh doing this thing but what was the business
[733.30 --> 738.32]  like what what was the business you were doing and what kind of eyes and ears and what kind of
[738.32 --> 742.26]  thoughts did it evoke for you to like produce this business and then like move on to what you're
[742.26 --> 747.66]  doing now where were what was that business about yeah yeah um well the correction is i told i i the
[747.66 --> 752.32]  what i the quote i gave them was it was making about half a million uh over its lifetime so that
[752.32 --> 759.18]  helps answer yeah the business insider they're not exactly known for their accuracy uh yeah it's
[759.18 --> 765.16]  certainly made for a flashy headline though so uh props to that but yeah it's not correct i wish i wish
[765.16 --> 770.96]  i had multi millions of dollars right now but i don't um and uh yeah so the business i made was
[770.96 --> 777.42]  basically uh and again i was scratching my own itch uh which will be a theme throughout everything
[777.42 --> 783.80]  but i was scratching my own itch uh to uh the university i went to had a really terrible um
[783.80 --> 789.56]  registration system so if a class was full then there was no wait list uh you just couldn't get in
[789.56 --> 794.62]  um you could try to get in by like going to the class once it started but that was pretty risky
[794.62 --> 801.60]  um so basically what students would do is refresh the page every day like i'll just check every day
[801.60 --> 808.10]  when i am bored to see if there happens to be an opening and then i'll pick it up and um i didn't
[808.10 --> 814.22]  like that so i wrote a program for myself to do that for me to refresh the page for me and then get me
[814.22 --> 821.12]  into the class and i was in a dorm at the time i was a freshman and uh the door my floor suddenly
[821.12 --> 827.50]  like was gossiping that i had uh i had this technology and so i would get knocks on my door
[827.50 --> 833.46]  being like so i hear you have a way to get into full classes and then i was like hmm and so i gave
[833.46 --> 838.74]  it to everyone on my floor for free that asked and then while i was doing that uh i sort of built it
[838.74 --> 847.60]  into a self-service website thing um and charged people uh five dollars per class uh to register a
[847.60 --> 853.74]  listener basically to notify them when there's an opening and i did this my freshman sophomore year
[853.74 --> 860.92]  and then uh sort of the i guess the change that happened which was uh the pivotal moment from a
[860.92 --> 866.88]  business perspective is that uh there was this critic this critical mass when students suddenly
[866.88 --> 873.98]  realized that if they didn't pay this website five dollars there was a they felt at least i don't
[873.98 --> 878.38]  believe this is necessarily true but they felt that there was a zero percent chance that they would
[878.38 --> 884.76]  get into the class because uh there's my thing was checking thousands of times a day students only
[884.76 --> 890.90]  check randomly like there's no there's a very low chance that they could get in versus the robot so
[890.90 --> 896.60]  um ended up there was a very huge growth period where suddenly students were just paying me five
[896.60 --> 902.14]  dollars to hedge a bet basically um to to give them a chance and so that that's sort of how the
[902.14 --> 908.92]  business progressed and then uh i ended up selling it uh when i started hashi corp because i wanted to
[908.92 --> 914.86]  focus uh full-time on hashi corp i didn't want to be distracted by a side business so yep so when you
[914.86 --> 919.22]  sold it were you still in college had you graduated i'd graduate i'd been out of college for a couple
[919.22 --> 924.76]  years okay so you continue to run it and i mean were you yeah let me ask another question on that part
[924.76 --> 931.78]  were you inspired by that business were you like uh not really like i can see with your output now
[931.78 --> 936.80]  you've been inspired by hashi corp right everybody can tell that but were you inspired by that business
[936.80 --> 944.20]  no it wasn't a very inspiring business i think i was very proud of it and i'm very proud that i was
[944.20 --> 948.42]  able to like get it to the point it was and i learned a lot um but i wouldn't say i wouldn't
[948.42 --> 957.38]  describe it as inspiring um it was it was a nice secondary income maybe uh now's a good time to
[957.38 --> 961.70]  maybe share a few updates since the last time you've been on the show like we said this is a
[961.70 --> 969.06]  three-peat for you episode 72 episode 88 and the last time you're on episode 88 that was may 15th 2013
[969.06 --> 975.20]  so lots changed lots happened since then just a little over oh wow a little over two years uh two
[975.20 --> 980.32]  and a half years roughly so maybe catch us up with hashi corp with yourself uh maybe some
[980.32 --> 984.50]  influences to the business what's what's changed in the last couple years for you with hashi corp
[984.50 --> 989.94]  oh wow yeah uh so much actually i didn't realize it was that long ago so it's been a bit
[989.94 --> 998.60]  yeah wow um so since 2013 i mean i i guess i'm best known for creating vagrant but since 2015 we've
[998.60 --> 1005.08]  as a company uh created um eight open source projects and one commercial product and
[1005.08 --> 1009.74]  um the eight open source projects which are probably the most interesting for this podcast
[1009.74 --> 1015.90]  are uh ranging from vagrant which is very developer focused to something like terraform which is more
[1015.90 --> 1021.16]  uh operator focused perhaps and then to things like console and vault which are
[1021.16 --> 1026.52]  um things that run in your data center that run in production so they're more uh reliability focused
[1026.52 --> 1032.54]  in terms of like a reliability engineer would probably be looking at those uh as well so i i sort of
[1032.54 --> 1038.92]  built this range of tools that span this whole thing uh and since then sort of the the adoption
[1038.92 --> 1045.50]  of all of them have been really awesome so uh i guess the the party trick that i have now is is
[1045.50 --> 1052.60]  you know name name five semi-popular like five websites that are that are not esoteric and
[1052.60 --> 1059.38]  i could confidently predict that three of them will be using our software um which is a pretty cool
[1059.38 --> 1063.98]  place to be so i'd say that's the that's what's developed over the past couple years what about
[1063.98 --> 1072.10]  as uh as the company itself uh the internals the the people what's changed since since then sure um
[1072.10 --> 1078.06]  the the big thing has changed is we've started hiring a lot more so we just crossed the 30 person mark
[1078.06 --> 1084.84]  but uh 12 i guess like 18 months ago there was only three of us so we went from three to 30 in about 18
[1084.84 --> 1091.76]  months and uh we've been hiring from the community primarily so core committers people like people that
[1091.76 --> 1095.94]  maybe aren't core committers but contribute a lot uh people that are on the mailing list a lot we've
[1095.94 --> 1100.66]  been hiring out of our community uh it gives us a high degree of you know confidence that we already
[1100.66 --> 1105.36]  know how they work and and they already like what we do and things like that so uh that's what we've
[1105.36 --> 1111.04]  been doing so we have now uh at least one full-time person per project um but most have a couple that
[1111.04 --> 1115.56]  are overlapping on multiple projects so full-time person that might be working on terraform but
[1115.56 --> 1121.00]  also working on packer or something um that's been the big thing and then this year the major focus
[1121.00 --> 1126.96]  um since the summer so not too long a few months has been uh really working on the commercialization
[1126.96 --> 1134.86]  angle so we uh announced our commercial product atlas and uh we we more or less completed our initial
[1134.86 --> 1138.32]  open source portfolio with our conference we had a conference last month
[1138.32 --> 1144.24]  um so we have the eight open source projects and and now we're really ramping up on the sales and
[1144.24 --> 1149.54]  marketing side and and getting that going i recall seeing word about that conference and i totally had
[1149.54 --> 1157.00]  fomo when i saw it i was like man i didn't even know about it so uh next year did you i mean maybe i
[1157.00 --> 1161.10]  don't follow you close enough i mean we are the change log around here so we keep our ear pretty close
[1161.10 --> 1166.56]  to the ground but how do we miss it i don't know i don't know i don't know i would tweet about it here
[1166.56 --> 1171.88]  and there did you hear about it jared i heard about it while it was going on right prior to it to where
[1171.88 --> 1177.26]  i could have attended yeah yeah i felt like i was like man i i felt kind of slighted because i was
[1177.26 --> 1181.46]  like i if i'd have known about it maybe because we've been trying to go to conferences more like
[1181.46 --> 1185.86]  you'd mentioned earlier uh mitchell that you got a change law t-shirt from us when we were at gopher
[1185.86 --> 1191.82]  gone so we're trying to do a better job of uh of supporting conferences and going to conference and we
[1191.82 --> 1197.46]  can't uh you know as jared and i two people we can't go to every single conference but um we might
[1197.46 --> 1201.82]  have gone might have gone yeah sorry sorry i don't know i i tweeted about it here and there i definitely
[1201.82 --> 1209.20]  didn't like shout it off the rooftops uh but yeah we we announced it back i guess i don't know maybe
[1209.20 --> 1215.00]  early summer like june maybe just before june we started ticket sales around june and uh we sold out
[1215.00 --> 1221.02]  uh in late july early august so yeah it sounds like you it was a success because you're talking about
[1221.02 --> 1226.56]  next year yeah i think it went really well it was it was the first conferences are always fun
[1226.56 --> 1231.90]  um i've gone to a few first conferences for open source projects uh just a few just i think three
[1231.90 --> 1237.84]  and they're always really fun because the projects at least the conference usually isn't mainstream
[1237.84 --> 1242.50]  enough that you get like a thousand people there it's usually pretty small you just end up meeting
[1242.50 --> 1249.66]  people from the community uh early users really passionate users and it's just really a fun vibe and i think
[1249.66 --> 1255.94]  that over time a lot of these conferences uh they gain if they they remain really really fun and
[1255.94 --> 1261.54]  entertaining and and valuable but they lose some of the initial like it's weird to say this when it's
[1261.54 --> 1268.28]  like 300 people but they lose the initial like small family feel of of people that have been through
[1268.28 --> 1273.58]  this for a while together and they're sort of uh meeting each other for the first time you sort of lose
[1273.58 --> 1280.92]  that more for the uh the more feeling of mainstream success and things like that and i think i hope
[1280.92 --> 1284.60]  that's where we're heading because because that's where you want to get to but at the same time the first
[1284.60 --> 1289.54]  conference is always a special one they kind of resisted a little bit so september 28th and 29th if you
[1289.54 --> 1296.00]  missed it will it be roughly the same uh same month roughly next year what's the plan there do you have
[1296.00 --> 1302.64]  any details you can share uh probably but i i i really we really have no so just maybe just late year
[1302.64 --> 1307.34]  late in the year yeah probably not earlier just because we're not planning it and i learned i
[1307.34 --> 1312.62]  learned a lot about planning conferences and uh takes takes quite a while well maybe if you don't
[1312.62 --> 1316.64]  mind we gotta take a break here in a second but maybe when we come back we can talk a bit about
[1316.64 --> 1322.56]  this wasn't on my list the rundown but uh you'd mentioned commercialization so i'm wondering if
[1322.56 --> 1327.00]  i'm sure at some point through our conversation around auto and vagrant which is pretty much what we're
[1327.00 --> 1331.80]  going to camp out on during this show although we can take lefts and rights as we need need to do
[1331.80 --> 1336.38]  um i'm wondering if maybe when we come back from this break if we can talk about commercialization
[1336.38 --> 1340.34]  a little bit what do you think is that all right with you that's good with me yeah cool all right
[1340.34 --> 1344.38]  well let's take a break real quick listen to a word from one of our sponsors that support this show
[1344.38 --> 1349.20]  when we come back we're going to talk a bit about commercialization of open source software and how you
[1349.20 --> 1357.32]  are making money there at hashi corp and we'll be right back braintree is all about making developer
[1357.32 --> 1363.32]  live simpler with code for easy online payments if you're searching for a simple payment solution
[1363.32 --> 1370.86]  check out braintree for mobile app developers out there the braintree b.0 sdk makes it easy to offer
[1370.86 --> 1378.72]  multiple payment types start accepting paypal apple pay bitcoin venmo traditional credit cards and
[1378.72 --> 1384.52]  whatever's next all with a single integration enjoy simple secure payments that you can integrate in
[1384.52 --> 1388.80]  minutes and developers they've got you don't worry about taking days to integrate your payments
[1388.80 --> 1394.28]  but braintree is done in minutes and if you don't have time give them a call and they'll handle the
[1394.28 --> 1400.68]  integration for you and walk you through it braintree supports android ios and javascript clients
[1400.68 --> 1409.52]  they have sdks in seven languages dot net node.js java pearl php python and ruby and their documentation
[1409.52 --> 1415.48]  is comprehensive and it's easy to follow to learn more and for your first fifty thousand dollars
[1415.48 --> 1421.02]  in transactions fee free go to braintreepayments.com slash changelog
[1421.02 --> 1430.02]  well we're back from the break um and mitchell you know i know when you said before
[1430.02 --> 1436.96]  commercialization and i i read into that and i think sustainability i think building a company
[1436.96 --> 1441.66]  so obviously that's what you're doing you you know when we started the show we talked about the
[1441.66 --> 1446.64]  article from from uh business inside that said you just raised 10 million dollars for a startup i
[1446.64 --> 1453.00]  imagine that startup was hashi corp so you got some some money there but you're also trying to learn
[1453.00 --> 1459.62]  how to commercialize software so what have you learned that you can share with us today well yeah
[1459.62 --> 1465.84]  this is my first time you know actually commercializing uh uh this kind of software i mean like
[1465.84 --> 1473.48]  software for engineers um but i guess the thing i've learned since starting hashi corp is that
[1473.48 --> 1478.72]  people want to pay for software uh you know open source is really really popular but that doesn't
[1478.72 --> 1483.94]  mean people don't want to pay for things uh i think open source is a lot more about um depending who
[1483.94 --> 1488.14]  you ask i mean this is going to be true or false depending who you ask but it's you know it's a lot more
[1488.14 --> 1496.06]  about um legal protection it's a lot more about uh vent avoiding vendor lock-in it's um the ability
[1496.06 --> 1502.92]  to uh security like ability to audit things in the open um obviously community is a big aspect being
[1502.92 --> 1507.68]  able to ask for help from people other than the vendor itself um so i think like that's what it's
[1507.68 --> 1515.78]  about it's really very rarely about i just want something free um at a certain level like even small
[1515.78 --> 1520.34]  companies like even people that have uh companies that have 10 employees or something they're
[1520.34 --> 1526.12]  very very willing to pay for software and i think that good evidence of this is actually like sasses
[1526.12 --> 1531.12]  like every small company pays for a sass somewhere like they they're open to spending money uh github
[1531.12 --> 1535.94]  actually they're definitely paying for github so uh that's that's what i've discovered and and at the
[1535.94 --> 1542.28]  bigger the sort of enterprise level um they're not only comfortable paying for software but they don't
[1542.28 --> 1549.08]  they're comfortable paying a lot for software that works well and solves their problems because
[1549.08 --> 1557.40]  it might seem like a lot to you know an outsider but it's it's it's very reasonable in terms of like
[1557.40 --> 1564.94]  what that software is doing for them uh uh what one our our um sort of senior director of marketing
[1564.94 --> 1570.26]  here like what he likes to say is is like we want to be able to go to tesla for example i'm just using
[1570.26 --> 1574.86]  them as an example they're not uh they're not necessarily a customer so using them as we want
[1574.86 --> 1582.22]  to be able to go to tesla and be like just focus on building great cars and let us handle all the
[1582.22 --> 1586.30]  infrastructure and deployment stuff for you like we don't want you to even think about it we want it to
[1586.30 --> 1591.20]  just work for you and let you focus on building cars and like imagine all the engineers you have
[1591.20 --> 1597.28]  hired right now to um worry about stuff that isn't your core business like what if they were instead
[1597.28 --> 1605.10]  building your car software like that's way more valuable so um that's sort of where uh commercialization
[1605.10 --> 1610.80]  comes in people want to pay for that piece of vine they want to pay for um knowing they do have a phone
[1610.80 --> 1616.76]  number if things go wrong they want to pay for features that they know don't make sense for
[1616.76 --> 1621.74]  non-enterprise companies and things like that and that's where we're focusing our commercialization
[1621.74 --> 1627.72]  effort so you you got your roots for your company in open source it was founded what was the very
[1627.72 --> 1632.96]  first i think vagrant was your very first thing right and that was open source first successful
[1632.96 --> 1637.66]  thing there was a lot of failures okay yeah so let's maybe let's skip the the failures but like what was
[1637.66 --> 1643.78]  the first thing you guys commercialized and what was that process like and what have you learned from it
[1643.78 --> 1648.18]  um so the first thing we commercialized was we made the vagrant vmware plugin which is still
[1648.18 --> 1653.44]  available today and it does very well so the vagrant vmware plugin pays for a number of salaries and it
[1653.44 --> 1660.58]  does well and the thing i've learned is that there's the there's a difference between doing something
[1660.58 --> 1665.62]  that'll make a small business work well and then there's a difference between doing something that
[1665.62 --> 1672.44]  will build you a large business and it's neither are wrong it just matters what you want and so when
[1672.44 --> 1678.08]  we did the vagrant vmware stuff i was still very much unsure what i what my ultimate business
[1678.08 --> 1683.30]  goals were with with hashi corp um i had a lot of technical goals but you know was was hashi corp
[1683.30 --> 1688.44]  going to be like the business i had in college where it made a good amount of money it could pay a few
[1688.44 --> 1698.02]  salaries we could um just sort of do what we want and build it or did i want to build a company that
[1698.02 --> 1705.98]  could potentially you know be a multi multi-million dollar company maybe towards you know even towards
[1705.98 --> 1712.96]  the size of something like vmware or something like a very large company and um i think the the main
[1712.96 --> 1722.82]  motivator for for me there was that i had sort of an audacious goal of wanting to build software that
[1723.20 --> 1731.54]  would change the way people manage data centers and deploy software and and you can't that's really
[1731.54 --> 1737.46]  like that goal is a big goal and that goal is it's not enough to convince you know every hobbyist
[1737.46 --> 1743.76]  developer to do it differently i wanted to convince um banks i wanted to convince you know amazon i wanted
[1743.76 --> 1749.56]  to convince these like big giants to like change the way they're doing some stuff um and it's sort of
[1749.56 --> 1754.38]  like a naive view of the world like i there's obviously a lot of stuff i didn't know then that i've
[1754.38 --> 1759.74]  learned since then but with that goal like i didn't have a chance of talking to these people or
[1759.74 --> 1765.22]  convincing them or at a much smaller chance let's say than if i go the route of raising money building
[1765.22 --> 1771.08]  a larger company i mean even the fact of just having money in the bank will get people to talk
[1771.08 --> 1778.38]  to you i i a very eye-opening moment was before we raised the series a um we were talking to a telco
[1778.38 --> 1784.08]  and they were going to deploy i think it was console and they were going to deploy console which came out
[1784.08 --> 1789.18]  before we raised our series a and uh we had to fill out this form and it was the first time i'd ever
[1789.18 --> 1795.82]  seen it a risk assessment form so we filled it out and they came back and they were like console's
[1795.82 --> 1801.90]  great it's fantastic we really want to use it but you failed risk assessment and we were like how did
[1801.90 --> 1806.66]  we fail risk assessment and they're like well we only work with companies that either have this much
[1806.66 --> 1811.54]  in revenue or have a bank account with this balance and you have neither so we just can't work with you
[1811.54 --> 1818.26]  as a policy and like that was a pretty eye-opening moment where i was like okay we need to that wasn't
[1818.26 --> 1823.26]  what motivated me to like raise money but that was another factor where i was like okay we're gonna
[1823.26 --> 1828.36]  fail risk assessments for companies because we're so small well it's like you said you're looking for
[1828.36 --> 1834.96]  ways to to commercialize right and so these are hurdles you're getting over it totally makes sense on
[1834.96 --> 1839.40]  like yeah we couldn't even charge them money yeah they they were they wanted to pay us and we they
[1839.40 --> 1845.20]  couldn't pay us because we were so small um so we needed to sort of raise money that was a factor we
[1845.20 --> 1851.28]  needed to raise to to prove to them um that we had intentions of sticking around and growing because
[1851.28 --> 1856.30]  it makes sense you don't want your vendor to be like a four person in a garage like when you call the
[1856.30 --> 1863.16]  phone it's going to like their cell phone sort of thing you want a real dependable large company sort
[1863.16 --> 1869.60]  to to depend on when you buy software i wouldn't mind talking a bit more about raising money jared i
[1869.60 --> 1873.28]  know you got a question on your side and i know you're waiting to ask it on the transitional piece
[1873.28 --> 1879.56]  but i i wouldn't mind talking a bit about you learning to raise money did you get some influencers did you
[1879.56 --> 1885.60]  have a a mentor like how who who guides you through what you're doing and how did you learn what you're
[1885.60 --> 1893.64]  doing to to build this company uh sure so i lived in san francisco i moved to san francisco after college
[1893.64 --> 1900.64]  and worked here for a number of years and a few years and uh i used that time in san francisco to
[1900.64 --> 1907.38]  um you know meet a lot of people network a lot um and inevitably sort of working in the startup world
[1907.38 --> 1914.40]  just learning how these things work and uh meeting other founders meeting venture capitalists um
[1914.40 --> 1922.04]  just yeah just really being in the thick of it even as a developer just being exposed to a lot of it
[1922.04 --> 1929.86]  so um i was really lucky when i went to go raise i uh uh just reached out to a bunch of people that
[1929.86 --> 1937.30]  had done it before and asked uh for advice and a lot of them introduced me to uh to venture capitalists
[1937.30 --> 1941.96]  and to to other folks that could give me advice to press and things like that and that's just how i
[1941.96 --> 1946.50]  got started i think past that it's a lot of stumbling like i've just been stumbling my way
[1946.50 --> 1952.30]  and hoping you know i make a few mistakes during the process like inevitably will but that's that's
[1952.30 --> 1957.48]  i think the nature of doing something for the first time so was it before the before the i guess abrasion
[1957.48 --> 1962.94]  with the company who you filled the risk assessment with was that was that what kind of like motivated
[1962.94 --> 1969.98]  you to raise money or before were you just like we'll organically grow no it was uh no we were we were
[1969.98 --> 1975.04]  getting motivated over time so yeah that wasn't the single factor but i think uh i think what
[1975.04 --> 1980.74]  actually really motivated us was that uh when we started hashi corp we we did it because we cared a
[1980.74 --> 1988.04]  lot about this problem and ops in particular wasn't you know wasn't a uh i guess attractive industry you
[1988.04 --> 1993.56]  know it wasn't it wasn't really this jewel that that vcs wanted to invest in or anything we just did
[1993.56 --> 1998.16]  it because we wanted to solve problems there um and then you know thanks to companies like docker
[1998.16 --> 2006.00]  and things like that uh suddenly ops became this really fast moving uh thing and i we were contributing
[2006.00 --> 2010.76]  you know in a small part to that by coming out with things like console and pushing people faster than
[2010.76 --> 2016.98]  they had been before um but it suddenly became very fast moving and we wanted to raise in order to
[2016.98 --> 2023.62]  realize sort of our goals and dreams of of the software we wanted to build uh faster because
[2023.62 --> 2029.60]  we were we suddenly saw the industry speed up and we didn't want other people to come and swoop in and
[2029.60 --> 2034.18]  do something differently than than we sort of philosophically believed in and mess up our goals
[2034.18 --> 2039.60]  so one more businessy question before we get to the to the subject matter which is vagrant and auto
[2039.60 --> 2045.40]  uh i've been looking at your contributions graph here while you guys have been talking because you said
[2045.40 --> 2051.54]  you went from three to 30 employees at hashi corp in the last 18 months so now you have you know
[2051.54 --> 2060.18]  you're the boss of 29 people and yet you have uh 49 commits you know publicly this week uh you've
[2060.18 --> 2065.40]  merged six pull requests uh you had a streak of 27 straight days contributing to open source
[2065.40 --> 2073.36]  this year how do you be someone's boss and yet still get to code so much uh we so my particular role
[2073.36 --> 2081.24]  in the company um is really sort of currently being in charge of all the product stuff so uh i don't
[2081.24 --> 2088.70]  have 29 people reporting to me thank goodness um i i sort of i sort of work with a lot fewer teams that
[2088.70 --> 2093.38]  are working on these open source projects and our commercial product and guide that um but i still
[2093.38 --> 2101.82]  love programming so um i just sort of work where i can and uh yeah i i think that for me that's the role
[2101.82 --> 2106.94]  that i'm trying to carve out for myself is i still think that there's work that i could do
[2106.94 --> 2114.50]  on the programming side so you know the traditional uh viewpoint of a startup is you have your your sales
[2114.50 --> 2120.78]  guy and your technical guy um does hashi corp have that style and are you the you the technical side
[2120.78 --> 2127.62]  of a of a team or are you just everybody no so well with 30 people you stop being everybody which is
[2127.62 --> 2133.32]  which is awesome that's nice but you you yeah you definitely i definitely was everybody for a
[2133.32 --> 2143.10]  a long time um but um to answer your question uh the hospital is a unique not unique company but
[2143.10 --> 2150.42]  i think that like it devops like where vmware is like this it's we're selling we're creating software
[2150.42 --> 2156.40]  for other engineers and it's highly technical so your sales people really need to be have engineering
[2156.40 --> 2161.16]  backgrounds as well and and there's a number of i mean i've learned this i've discovered this so
[2161.16 --> 2167.26]  there's just a number of sales people like they've been doing sales for 15 years that have cs degrees
[2167.26 --> 2174.10]  and code for on the side excuse me code on the side and um and understand this stuff and you need to
[2174.10 --> 2183.14]  because at least for us a core part of our culture is is trying to be genuine so trying to go into
[2183.14 --> 2189.22]  uh a company and and be honest with them and and some customers have told us this where we've gone
[2189.22 --> 2193.80]  in for a meeting and they've uh the sales type meeting and they've asked us like well we sort of
[2193.80 --> 2197.64]  want to do this with your product and this and we've just told them like this is not the right product
[2197.64 --> 2203.72]  for you this won't do that well um and they were and and some people are taken aback by it because
[2203.72 --> 2210.74]  they're like did you just say no in a way and and that's just kind of what we do because because i
[2210.74 --> 2217.62]  think our first principles are as engineers and as engineers we believe in the right solution and so
[2217.62 --> 2225.42]  we need sales people who are engineers that also believe that that it's more valuable for a potential
[2225.42 --> 2230.86]  customer to like you than it is to close the deal no matter what because our viewpoint is if we're
[2230.86 --> 2234.96]  talking to them they'll probably need us we hope that they'll need us eventually anyway we have a
[2234.96 --> 2239.24]  broad enough set of tools that uh maybe that solution doesn't solve something for them but
[2239.24 --> 2242.60]  we're certainly not going to walk out of there without showing them the rest of what we have and
[2242.60 --> 2247.04]  trying to find something else that works so there's still an aspect of you know trying to get to say
[2247.04 --> 2254.68]  yes in there but there's also um a goal of being honest the worst sale too though is is the sale where you
[2254.68 --> 2260.80]  implement the wrong solution you know like you said you have a broad enough product line that
[2260.80 --> 2266.74]  you're working towards that eventually uh you may or you will uh have a solution for them really
[2266.74 --> 2271.90]  fits and if you lose that trust early then you know regardless of what you produce in the future
[2271.90 --> 2276.34]  they're gonna be like yeah they they kind of they didn't give us the right advice early on and yeah
[2276.34 --> 2281.68]  you know i mean yeah and maybe we're lucky that way given that we have so many different
[2281.68 --> 2287.48]  things i mean i imagine it's a lot harder if you're like a database company and the data doesn't
[2287.48 --> 2294.26]  really fit your model but there's other you know sort of unlikely to change their data model so you
[2294.26 --> 2299.18]  might not have a chance to come in again so you might be more inclined to say yes somehow um whereas
[2299.18 --> 2305.86]  we're a lot less concerned or offended or anything if it's like if we're more ready to admit like okay
[2305.86 --> 2311.52]  the console isn't right for you but maybe vault is so let's take a look at that and stuff like that
[2311.52 --> 2318.14]  you mentioned you got many things but we are only here really to talk about our beloved tool vagrant
[2318.14 --> 2323.80]  uh getting getting succeeded by auto and it's it's an interesting topic and for the listeners out there
[2323.80 --> 2327.94]  we have a couple breaks during our show we're probably gonna have to do a break during the main
[2327.94 --> 2332.38]  conversation we try to time it so that we don't have to like put a break in there but we're gonna have
[2332.38 --> 2337.44]  to break in like 11 minutes so uh give us some forgiveness there but auto is really interesting
[2337.44 --> 2342.86]  uh we obviously loved vagrant when we had you on the show before back in 72 i know andrew and i went
[2342.86 --> 2350.98]  deep on what vagrant was then but for the listeners out there that are are maybe unfamiliar uh let's
[2350.98 --> 2356.76]  open this up maybe with what vagrant is to a degree and what auto is i guess that's probably would you
[2356.76 --> 2361.62]  say jared is the best way to open this conversation up just to sort of describe what vagrant is yeah i think
[2361.62 --> 2366.18]  you can't really understand auto without understanding vagrant as it builds on top of it so let's start
[2366.18 --> 2370.70]  there and then he can differentiate auto from there maybe paint some history too of like when it
[2370.70 --> 2376.10]  i think during this conversation we pinned it back to the origination of hashicore but give us some
[2376.10 --> 2382.62]  timelines and help us understand what vagrant is before we go into auto uh yeah cool so vagrant is a
[2382.62 --> 2389.20]  six-year-old open source project um that is uh in one sort of sentence still it's the one sort of
[2389.20 --> 2395.62]  phrase development made easy so the goal of vagrant is to run one command and get a complete
[2395.62 --> 2401.06]  development environment for whatever application you're working on um the problem it was solving was
[2401.06 --> 2406.04]  uh you know i was switch i was with does developer to consultancy and i was switching between a lot of
[2406.04 --> 2413.16]  different customers and uh different technology stacks and getting that all to work together nicely
[2413.16 --> 2417.88]  on my laptop which is a very different environment than what they were ending up on you know in a
[2417.88 --> 2424.28]  server um was was a pain to say the least so uh vagrant was a solution to that where everything
[2424.28 --> 2429.74]  a sandbox and a virtual machine um you run vagrant up every single project you have gets a separate
[2429.74 --> 2435.30]  virtual machine it's completely isolated so you could have different versions of web servers and
[2435.30 --> 2443.14]  libraries and databases all coinciding uh co-mingling i guess on your own machine um and not causing any
[2443.14 --> 2447.32]  conflicts and when you're done working with that project you could destroy the environment and it's a
[2447.32 --> 2451.96]  clean slate you know you don't you're not left with cruft on your machine you're not uh using any more
[2451.96 --> 2456.70]  resources actively it's just gone completely and but you can make it again very easily so
[2456.70 --> 2463.78]  that was vagrant it's been growing sort of over the past six years uh to effectively be our our
[2463.78 --> 2468.02]  flagship open source project at hashi corp it it gets millions and millions of downloads
[2468.02 --> 2476.12]  um a month and it's it's kind of a monster on its own and uh so six years ago that was created and and
[2476.12 --> 2483.12]  i guess what what problems were out there that made auto be a solution to succeed over vagrant because
[2483.12 --> 2488.70]  the yeah the blog that was put out how long ago was the successor to vagrant is is auto so this is the
[2488.70 --> 2493.32]  successor so vagrant will go away eventually or we'll sort of i don't know maybe you can help us
[2493.32 --> 2501.28]  understand that too yes okay so um yeah so the it's great we did the backstone hashi corp because that
[2501.28 --> 2505.96]  gives a good idea that over the past three years we've been focusing a lot on operations and making
[2505.96 --> 2512.54]  deployment easier managing servers easier um and so we've been during the same process we've been
[2512.54 --> 2520.54]  consistently releasing new vagrant versions adding features iterating um but we haven't focused on
[2520.54 --> 2525.26]  developers in a few years like they haven't been the the focus of our company in a few years and
[2525.26 --> 2531.12]  and we don't want to feel like they're neglected and one but we also felt that vagrant was at a really
[2531.12 --> 2537.18]  good spot it was very stable it worked really well but after three years we we we use vagrant
[2537.18 --> 2543.58]  obviously every day here at hashi corp and and we were sort of discussing uh sort of a year ago i guess
[2543.58 --> 2550.22]  we're like so we've done all this work to make all these other people's lives uh better we hope we hope
[2550.22 --> 2557.16]  that's our goal um like is there any like sort of revolutionary new things we could bring to the
[2557.16 --> 2561.92]  development angle have we learned something that we could significantly change vagrant to make it
[2561.92 --> 2569.08]  better and so the conversation started with what would we do if we could start vagrant from scratch
[2569.08 --> 2575.74]  like how would things be different today and the three sort of things um i picked up on from and this
[2575.74 --> 2582.46]  is sort of based on you know working with vagrant for six years and and uh and walking into companies
[2582.46 --> 2587.30]  and seeing how they use it and and and just seeing thousands of users really the three things i
[2587.30 --> 2594.32]  picked up on was uh one um development environments are really really similar to each other uh i think
[2594.32 --> 2599.10]  it was funny because on hacker news someone commented that they think this statement's false but
[2599.10 --> 2604.34]  but i mean i i really believe it's true i've seen it in the wild like if you're a ruby developer and
[2604.34 --> 2609.26]  you go to another company in another country and they're a ruby developer your development
[2609.26 --> 2615.70]  environments are 90 plus percent similar you have some version of ruby you have bundler you
[2615.70 --> 2619.48]  probably if it's a web application you're going to have a database you're going to have something like
[2619.48 --> 2626.32]  passenger um and they're just really similar the last 10 is like differing versions or passenger versus
[2626.32 --> 2631.70]  unicorn or something like that and and they're really details that don't matter too much in a
[2631.70 --> 2637.60]  development environment um so what and and it's hard to solve this at the vagrant layer because
[2637.60 --> 2644.58]  vagrant is so uh low level uh relative to auto which we'll get to but it's it you describe sort
[2644.58 --> 2649.12]  of the machine it runs on you describe what server to install you describe what database to install
[2649.12 --> 2655.72]  you do this from scratch on your own so it's hard to get to get rid of this uh duplication so that was
[2655.72 --> 2659.64]  sort of the first thing and then the second thing and we could cover you could ask questions about
[2659.64 --> 2663.98]  these in a second let me just sort of try to say all three sure um the second thing was that
[2663.98 --> 2670.80]  uh developers wanted to deploy so this is really no surprise to anybody um vagrant had a issue i think
[2670.80 --> 2676.12]  for five years uh well it's probably it's probably been closed for a while but it an issue opened five
[2676.12 --> 2682.06]  years ago at least that people wanted to vagrant up to production it vagrant up is a really nice
[2682.06 --> 2687.08]  really frictionless way to get a development environment and they were like why can't deployment
[2687.08 --> 2695.72]  be just as easy as a vagrant up and and honestly we yes please so honestly we tried for a bunch of
[2695.72 --> 2700.54]  years at various different points to fit this into vagrant we tried a bunch of different things um
[2700.54 --> 2707.72]  and it just never really worked well um and i and the realization i made was very similar to number one
[2707.72 --> 2714.00]  which is that the vagrant file itself is just fundamentally not the right approach to describe
[2714.00 --> 2719.46]  a deploy i do think it was it is continues to be a great way to describe a development environment
[2719.46 --> 2724.56]  but it's not a great way to describe a deployment environment because they're so different you run
[2724.56 --> 2728.98]  multiple web servers you run a load balancer in production you have monitoring systems in production
[2728.98 --> 2735.06]  um you have different security requirements like it's so different from development that you can't
[2735.06 --> 2740.64]  safely map a vagrant file to what goes up in the production so that just needed to be thought out
[2740.64 --> 2746.76]  um and then the third and final thing is that you know we live in a world with with microservices now
[2746.76 --> 2750.78]  we live in a world with containers we live in a world with really lightweight applications that are
[2750.78 --> 2756.54]  all working together to do one bigger thing um and that's really different from the world that existed
[2756.54 --> 2762.48]  six years ago when i made vagrant um six years ago when i made vagrant um you know the best practice
[2762.48 --> 2768.40]  or the standard practice at least was to just make a giant monolithic rails application or php application
[2768.40 --> 2774.12]  that does everything that has everything and over the past six years uh that's slowly been changing
[2774.12 --> 2780.04]  back to more of a service-oriented model of uh smaller services that communicate together to mitigate
[2780.04 --> 2786.32]  failures you could use smaller servers you could um you could develop faster you know they have all
[2786.32 --> 2792.40]  these other promises i'm sure you have or will talk about microservices like as its own podcast at some
[2792.40 --> 2798.10]  point um but as its own episode at some point but um these are coming and i talked a bit about that
[2798.10 --> 2803.08]  with uh peter bergon microservices oh yeah that's that's that's a great person to talk to about
[2803.08 --> 2809.22]  that yeah so microservices i don't claim i i really don't claim their mainstream today at all but i i do
[2809.22 --> 2813.80]  think it's inevitable that they will become mainstream so the third thing i really thought of was like
[2813.80 --> 2820.54]  vagrant is not a good tool for microservices it's it's build one vm describe one directory of of
[2820.54 --> 2826.62]  application files it's really hard to describe dependencies and how to install them and or it's not hard so
[2826.62 --> 2832.38]  much as it's very manual and very tedious and so again it was like how do we fix that and so those
[2832.38 --> 2838.64]  were the three things identified with vagrant that we that we went on to address in in auto well i think
[2838.64 --> 2844.06]  that's actually a really good setup let's take that break now hear from one of our sponsors when we get
[2844.06 --> 2851.02]  back we'll find out how auto solves these three problems and probably more uh we'll talk about that
[2851.02 --> 2856.56]  on the other side of the break if you've ever restored data from a hard drive you know it's
[2856.56 --> 2862.42]  complicated you know it's messy and it's probably something you never want to do again and backing up
[2862.42 --> 2869.52]  is just so much easier backblaze a new sponsor to the show offers online backups for your documents
[2869.52 --> 2876.58]  your music your photos even videos and so much more go to backblaze.com slash changelog to start your
[2876.58 --> 2882.78]  free two-week trial you might be using an external usb hard drive and that's a good start but it's
[2882.78 --> 2888.46]  better to be safe than sort of safe put your mind at ease knowing your data is backed up securely in
[2888.46 --> 2892.86]  the cloud you get online access to your files from anywhere in the world you have an internet connection
[2892.86 --> 2899.14]  they have android and iphone apps for mobile access and backblaze runs natively on mac and pc
[2899.14 --> 2904.80]  including your external hard drives there's no add-ons there's no gimmicks or additional charges
[2904.80 --> 2911.76]  it's just five dollars a month literally five dollars a month per computer for unlimited
[2911.76 --> 2918.80]  unthrottled backup and changelog listeners get a free two-week trial by going to backblaze.com
[2918.80 --> 2926.70]  slash changelog all right we are back speaking with mitchell hashimoto about vagrant and auto so
[2926.70 --> 2931.70]  before the break you said vagrant had three not necessarily problems but three things that are
[2931.70 --> 2936.00]  different now than when you first started six years ago uh developed environments are really
[2936.00 --> 2940.62]  similar to one another at least you've noticed that since then developers wanted to deploy to
[2940.62 --> 2946.18]  which i say amen and number three was that we live in a world with containers and microservices and
[2946.18 --> 2952.74]  vagrant really can't solve these three problems hence auto so can you lead us into auto give us the
[2952.74 --> 2961.16]  elevator pitch and tell us how it succeeds vagrant yes so the the elevator pitch of auto is that
[2961.16 --> 2968.90]  whereas vagrant is development made easy um auto is development and deployment made easy um and the
[2968.90 --> 2976.58]  key difference we made in auto was sort of moving uh i i would say is in its configuration format
[2976.58 --> 2983.00]  actually so instead of a vagrant file with vagrant you have an app file with auto and it's it's you
[2983.00 --> 2988.54]  might be able to tell from the name how it's different already so uh the fun exercise i like
[2988.54 --> 2992.72]  to do with uh with vagrant users is like what's the first thing you do when you make a vagrant file and
[2992.72 --> 2998.54]  and the answer is is choose the box that you're going to use whether it's always the same or not you
[2998.54 --> 3003.22]  write down the box you're going to use and that right there is fundamentally the difference between
[3003.22 --> 3006.94]  vagrant and auto with auto the first thing you do with an app file if you even write one and i'll
[3006.94 --> 3011.68]  get to that in a second but the first thing you do with an app file is specify what application type
[3011.68 --> 3017.00]  it is it's a ruby application it's a rails application or it's node or it's just a custom
[3017.00 --> 3023.38]  other thing um and that sort of gives you a hint of the difference auto cares a lot more about the
[3023.38 --> 3029.92]  application and a lot less about the underlying details of that application which i which sort of goes
[3029.92 --> 3033.82]  back to the first thing i mentioned with with how i would improve vagrant which is that your
[3033.82 --> 3038.64]  development environments are just very similar um it's it's less important for you to tell auto
[3038.64 --> 3043.84]  how to install and set up a go environment when they're all similar auto might as well just know
[3043.84 --> 3048.82]  on its own how to set it up and that's what we've done so it kind of moves up a level of the
[3048.82 --> 3055.54]  abstraction chain up one level yeah instead of specifying you know ip addresses and my sql server
[3055.54 --> 3062.54]  or whatever you're just like hey i got a ruby on rails app so you're just yes exactly exactly and
[3062.54 --> 3070.24]  and so the way uh and i mentioned earlier that app files are even you know optional you might not write
[3070.24 --> 3077.84]  one so if you run auto um in a directory with a bunch of ruby files it'll actually detect it'll be
[3077.84 --> 3081.80]  like well this looks like a ruby project to me so i'm just going to assume it's a ruby project so
[3081.80 --> 3087.72]  um one thing that's really cool is as we've been using auto more at hashi corp is our designer
[3087.72 --> 3095.46]  um went into one of our go back-end um services and was and ran auto dev to get a development
[3095.46 --> 3101.46]  environment and he was like whoa like this just worked like i got a go development environment
[3101.46 --> 3107.24]  i have no idea how to install go i have no idea how to compile things and auto auto not only set it
[3107.24 --> 3112.18]  up for me with zero configuration it also told me how to compile the project and he was like i didn't
[3112.18 --> 3115.46]  know once he got it running he was like i don't know how to run it because i don't know how to run
[3115.46 --> 3120.96]  it but he wanted to see if it worked um and then the flip side he he also had like some really old
[3120.96 --> 3125.30]  ruby projects from years back that he hasn't touched and he went back into those and was like
[3125.30 --> 3130.28]  what's this going to do if i auto dev here so he auto dev'd and he was like yep set up a development
[3130.28 --> 3135.66]  environment ruby bundler um auto bundled my things like set it all up he was like it just worked
[3135.66 --> 3140.70]  with zero configuration that's awesome so that's the direction we're really heading the zero
[3140.70 --> 3146.40]  configuration thing really isn't a gimmick um it's it works and and we intend to make it even better
[3146.40 --> 3151.46]  going forward we want you to be able to go into a project with no configuration uh and not only
[3151.46 --> 3157.02]  develop which i've been talking about but deploy um so that's that's the thing and then the sort of
[3157.02 --> 3161.08]  last major difference uh obviously auto could deploy so we could talk about that in a second but
[3161.08 --> 3167.06]  um the the philosophical difference between vagrant and auto because people ask me i guess
[3167.06 --> 3171.88]  why did you make a completely different project why didn't you just make a vagrant like 2.0 that
[3171.88 --> 3177.66]  has a different config format or something um for a lot of reasons but the major major reason is that
[3177.66 --> 3184.82]  auto has a really big philosophical difference in vagrants so if you take a vagrant file from five
[3184.82 --> 3190.08]  years ago and you run vagrant up today it'll probably work we worked really hard to make sure that that
[3190.08 --> 3196.10]  works but what you get is exactly what you configured five years ago you'll get the same version of
[3196.10 --> 3200.90]  uh apache you configured you get the same version of the language you'll get the same operating system
[3200.90 --> 3206.42]  version you specified um and what we call this is a fossil so what vagrant files are are a form of
[3206.42 --> 3213.94]  fossilization so you fossilize and snapshotted what the state of the world was five years ago and vagrant
[3213.94 --> 3219.02]  gives you that today and that's that's sometimes a good thing um but the approach we've taken with
[3219.02 --> 3224.76]  auto is instead of codification or codification depending how you want to pronounce it the idea
[3224.76 --> 3230.26]  is that the app file itself is just declarative of the type of application you're deploying but the
[3230.26 --> 3235.16]  knowledge of how to create development environment and how to deploy is centralized in auto itself so
[3235.16 --> 3240.32]  not in the vagrant file but it's in the core of auto itself so that when you run auto deploy today
[3240.32 --> 3245.20]  you're going to get something but if you run auto deploy five years from now it'll probably it'll
[3245.20 --> 3249.82]  hopefully very likely be very different but the end goal is your application will run but with best
[3249.82 --> 3255.36]  practices from five years from now not from today and so the security patches and and technology
[3255.36 --> 3262.58]  changes and things like that um and and the people making this happen as the community so it's a it's
[3262.58 --> 3268.04]  a centralization of knowledge so the we want the person who's a professional ruby developer to tell us
[3268.04 --> 3273.82]  to contribute to auto and tell us how the best practices of ruby development are and we'll encode that
[3273.82 --> 3280.42]  into auto so that um you get that and and sort of the my favorite example is that our our uh our the
[3280.42 --> 3287.32]  person who set up the aws integration with auto used to manage a top 10 um by size infrastructure on
[3287.32 --> 3293.32]  aws and now if you're just a hobbyist that's running auto deploy in aws you're actually getting an
[3293.32 --> 3300.26]  infrastructure designed by somebody who was uh the lead infrastructure person for a top 10 aws property
[3300.26 --> 3305.22]  but you're getting it for your side project um and we want that to eventually be true for every
[3305.22 --> 3310.84]  technology in auto if this work if this works as advertised i think i want to kiss you this is
[3310.84 --> 3317.62]  amazing when you said that mitchell i was like i know jared likes that oh man i like all of this
[3317.62 --> 3325.28]  mitchell this sounds spectacular so and it's this works right now like zero config fire it up yeah
[3325.28 --> 3330.78]  okay yeah you can go download auto right now it'll work um so the the only part that's like not
[3330.78 --> 3336.00]  it'll work as a demo but isn't ready for like production is the deploy the the maintenance
[3336.00 --> 3341.16]  part of deploying so okay um we eventually want auto to completely replace how you deploy things
[3341.16 --> 3347.02]  but for now it'll deploy it once but it's not good at deploying it multiple times we we purposely are
[3347.02 --> 3354.00]  focusing on making auto a better development experience experience first and then uh we're targeting
[3354.00 --> 3361.36]  auto 0.3 as the major uh super production ready deployment stuff and uh and the main reason for
[3361.36 --> 3367.52]  that is just that it's complicated um but we believe from the beginning given the fact that vagrant was
[3367.52 --> 3371.98]  never designed from the beginning to deploy from the beginning auto is designed to deploy so we believe
[3371.98 --> 3377.30]  we have the fundamentals right and uh can make this happen in a really nice way so let's stick with
[3377.30 --> 3382.38]  the develop first um because i mean i'm super excited about the deploy stuff but we need to clarify
[3382.38 --> 3387.32]  vagrant a little bit here because it says like on your guys's auto getting started that you first
[3387.32 --> 3393.84]  you run this auto command auto compile um and it says the first time you run it you may be asked for
[3393.84 --> 3399.30]  permission to install vagrant which it uses under the covers in this case it probably also downloads a
[3399.30 --> 3405.00]  base image for your environment so it's a successor to vagrant but vagrant's still in the mix you want to
[3405.00 --> 3411.86]  speak to that for us yeah yeah i'd love to so there's so we didn't want to reinvent the wheel like uh
[3411.86 --> 3418.92]  vagrant is is really mature uh the bugs it has uh generally are very esoteric today they're usually
[3418.92 --> 3425.30]  not very mainstream um and so it works really well and we don't want to rebuild all that for auto so
[3425.30 --> 3432.74]  auto actually uses vagrant under the covers for a lot of um the final bring something up but it does
[3432.74 --> 3438.00]  a lot more on top of it to make things nice so the best example i could give is actually the upcoming
[3438.00 --> 3445.28]  version of auto um auto 0.2 where we focused a lot on development experience so for a go development
[3445.28 --> 3453.08]  environment with auto 0.1 uh or vagrant it's just a vagrant file so or or vagrant 1.7 is uh it takes
[3453.08 --> 3458.48]  about five minutes to get a complete development environment it's pretty slow um and and take some
[3458.48 --> 3463.90]  time because it's installing go it's installing a bunch of other stuff um so it takes time and with
[3463.90 --> 3471.10]  auto 0.2 um we're able to make the go development boot up in 30 seconds so five minutes to 30 seconds
[3471.10 --> 3477.26]  and the way we were able to do that is we still use vagrant under the cover for parts but auto is
[3477.26 --> 3482.62]  starting to offload some of the stuff vagrant used to do and do more clever things due to its architecture
[3482.62 --> 3488.88]  um that would have been difficult to do in pure vagrant so that this is starting to move more logic
[3488.88 --> 3494.96]  away from vagrant into auto uh and and you i guess you'll you'll start seeing this over time is that
[3494.96 --> 3502.24]  uh we could do fancier things in in auto so another example is uh people who use vagrant are i mean
[3502.24 --> 3507.90]  have complained and and rightly so that vagrant ssh is pretty slow so a lot of this is ruby of course but
[3507.90 --> 3512.92]  if you run vagrant ssh um the time it takes the ssh in the machine is sometimes multiple seconds
[3512.92 --> 3517.68]  and even with auto 0.1 with if you were to download auto right now and get a development environment
[3517.68 --> 3523.56]  auto dev ssh which is the equivalent to ssh into the development environment um is a couple hundred
[3523.56 --> 3527.14]  milliseconds so we went from a few seconds to a couple hundred milliseconds and the reason we're
[3527.14 --> 3532.96]  able to do that is uh auto is the sole controller of that development environment so it knows that your
[3532.96 --> 3539.84]  ssh information isn't changing um so it caches the ssh information and just executes ssh in process
[3539.84 --> 3546.32]  directly um so it's just a lot faster whereas what vagrant does is um there's a lot of other commands
[3546.32 --> 3550.10]  that could affect the ssh information so what vagrant does is every time you run vagrant ssh
[3550.10 --> 3555.72]  actually inspects the virtual machine inspects various things to try to detect the right ip
[3555.72 --> 3560.50]  detect the right password detect the right key um and that just that's all in ruby and that so that
[3560.50 --> 3565.80]  all takes a bunch of time and then subprocesses into ssh so we got rid of all that and now we're just
[3565.80 --> 3571.96]  going directly into ssh uh and so it's a lot faster so these improvements will continue over time
[3571.96 --> 3579.84]  um to make auto just a a lot better development experience than vagrant was so speak to the
[3579.84 --> 3588.22]  the virtualization environment that auto uses on your machine same as vagrant or different yep
[3588.22 --> 3593.36]  yep same same and that was a lot of the reason why we didn't want to um sort of rewrite those aspects
[3593.36 --> 3599.40]  yet at least in auto because uh vagrant has a great community around it with support for virtualbox
[3599.40 --> 3606.88]  vmware parallels hyper v um you know uh kvm all these different providers and you get all that
[3606.88 --> 3611.16]  same stuff with auto so it's immediately going to work on your system that way but what if i don't
[3611.16 --> 3617.24]  care like i just want to run auto compile what's it gonna so this is the kind of cool part we did
[3617.24 --> 3621.48]  with auto is that auto kind of like you said in the getting started guide it installs and manages
[3621.48 --> 3626.50]  vagrant for you so if you don't care then when you run auto it'll just ask for permission because
[3626.50 --> 3631.66]  it's going to download like an 80 megabyte thing um but it asks for permission and then uh it just
[3631.66 --> 3636.64]  manages it for you so if you're just like sure just do something like sure then then it'll install and
[3636.64 --> 3640.66]  the one improvement we're making is it'll actually the next version will install virtualbox for you
[3640.66 --> 3648.38]  um if you don't have a hypervisor on your system so that's the idea is you only need to install auto
[3648.38 --> 3653.88]  ever and it'll do the rest for you how does it play with uh containers and docker and whatnot
[3653.88 --> 3661.36]  uh well um so the idea behind auto is that if the best practice is containers which i would say for
[3661.36 --> 3665.94]  a lot of things is right now then we're going to use containers um more on the deployment side and
[3665.94 --> 3671.10]  less on the development side and i'll talk about that in a second but um so yeah when you auto deploy
[3671.10 --> 3677.50]  um it's uh it builds a container and actually will use docker to run a bunch of things not everything
[3677.50 --> 3684.44]  right now but a bunch of things um and then on the development side um containers are just they
[3684.44 --> 3689.50]  were just we we worked with a bunch of people who use containers for development and they're fast which
[3689.50 --> 3698.14]  is the nice part but you lose the um sort of save reload you know review sort of cycle of development
[3698.14 --> 3705.32]  the mutability like containers on their own are usually a pretty uh um or the immutable sort of thing
[3705.32 --> 3708.90]  um and you could set up shared volumes with containers and things like that you could work
[3708.90 --> 3713.80]  around these things but um with auto since we have so much more control over development environment
[3713.80 --> 3719.90]  we could just set that all up for you and the the containerization part of a container uh isn't as
[3719.90 --> 3724.84]  important so the development environment currently just isn't in a container because it doesn't give
[3724.84 --> 3729.14]  you a lot and most people are developing on non-linux systems so you would need a virtual machine
[3729.14 --> 3733.66]  anyway to run the container right so instead of starting the virtual machine then starting the
[3733.66 --> 3737.88]  container like we'll just start the virtual machine and run it there um the main improvement
[3737.88 --> 3744.04]  we made over vagrant for this is that um even for projects with a ton of dependencies and other
[3744.04 --> 3749.76]  you know multiple services we're sort of uh creeping on the microservice part of auto right now but
[3749.76 --> 3755.34]  for things with a bunch of services auto basically installs all those for you onto a single virtual
[3755.34 --> 3759.20]  machine whereas with vagrant you might have tried to use multiple virtual machines which would have been
[3759.20 --> 3766.30]  much slower um so auto handles this complexity for you so you're always each each environment is only
[3766.30 --> 3771.82]  one virtual machine for for everything you're working on and that brings a lot of the the benefits as well
[3771.82 --> 3776.30]  without having to use containers for development so what do you say to the people out there right now
[3776.30 --> 3782.98]  thinking i don't want your shiny new auto i love vagrant i love vagrant files i just want to use them
[3782.98 --> 3788.16]  i don't we didn't need a successor to vagrant uh yeah you're the worst what do you say to them
[3788.16 --> 3795.36]  uh who said that i would hypothetically hypothetically yeah i would i would be a little bit sad but at the
[3795.36 --> 3803.10]  same time um vagrant's not going away so uh vagrant 1.8 is coming out uh next month and it's going to be
[3803.10 --> 3809.04]  a huge awesome release we get linked clone support we get snapshotting support stuff like that um you know
[3809.04 --> 3815.52]  vagrant is a really mature project and and auto i i there's very few people out there because i know
[3815.52 --> 3818.62]  because i said i know the download numbers from back then but there's very few people out there who
[3818.62 --> 3825.78]  use vagrant 0.1 but vagrant 0.1 was awful and uh it came a long way since then to be the product it is
[3825.78 --> 3832.58]  today and likewise i think auto 0.1 is definitely a lot better than vagrant 0.1 was but i think we'll
[3832.58 --> 3837.82]  look back and and say even in a year being like oh well auto 0.1 was pretty bad compared to where we're
[3837.82 --> 3842.74]  going to get to and uh for the people who want something that they know is going to work that
[3842.74 --> 3847.70]  they don't want to be early adopters or risk takers then they should use vagrant and we're going to keep
[3847.70 --> 3854.32]  bug fixing vagrant releasing vagrant um especially because auto still uses vagrant um and the long-term
[3854.32 --> 3860.20]  plan for auto is that that yeah like we'll phase we we hope that 90 plus percent of developers using
[3860.20 --> 3866.50]  vagrant over the next few years will shift to auto um but there's also use cases for vagrant that auto's
[3866.50 --> 3872.34]  never going to attempt to cover so it also just can't disappear completely so a good example is
[3872.34 --> 3877.62]  for ops people people who use people ops people who use vagrant for testing um chef and puppet and
[3877.62 --> 3883.82]  things like that um that's really not a goal of auto currently it's it doesn't give you the same
[3883.82 --> 3889.76]  control of i want this specific operating system and this specific state to test this stuff um it's a
[3889.76 --> 3893.34]  lot more opinionated about setting things up so it's it's really not going to be great for that
[3893.34 --> 3898.34]  and then the other thing that vagrant will continue to to reign king and very similar is
[3898.34 --> 3906.72]  uh just sort of custom uh really custom environments so um maybe you're doing something with a really
[3906.72 --> 3912.88]  strange os or you're doing embedded development or uh actually i know a company that does game
[3912.88 --> 3919.44]  development in uh in vagrant so they spin up windows machines uh on really beefy hardware um and
[3919.44 --> 3923.76]  actually do 3d game development in a vagrant environment and and that sort of stuff like auto
[3923.76 --> 3929.36]  is not really going to touch so we're super motivated we have people uh working full-time
[3929.36 --> 3935.84]  on vagrants and and we're going to keep it that way for for years one question i think that you
[3935.84 --> 3939.84]  could probably speak to a bit is you talked about microservices earlier how they weren't really a
[3939.84 --> 3943.94]  part of the the world really when vagrant was around when vagrant first came out
[3943.94 --> 3950.38]  and auto is built to do that on its own so it's built for microservices can you speak to the built
[3950.38 --> 3957.92]  for microservices part yep um yeah so in the app file itself uh you could specify dependencies of
[3957.92 --> 3962.34]  your application so um these dependencies might be things like a database but they could also be other
[3962.34 --> 3967.66]  services and and what you point to in that and to specify the dependency what you actually do is
[3967.66 --> 3975.02]  specify where that dependencies app file is so you you create this chain of dependent app files
[3975.02 --> 3979.40]  um and so what you could do for the source that practically is you know give it a github address
[3979.40 --> 3987.34]  or give it a http address or even s3 or something um and what auto manages for you is fetching that app
[3987.34 --> 3993.60]  file um compiling that app file figuring out how to install that thing um and and the practical
[3993.60 --> 4001.14]  benefit of this is is that the app developer only needs to worry about how to install develop and
[4001.14 --> 4006.42]  run their application and they just specify what they depend on and auto manages how to get that
[4006.42 --> 4012.84]  into the environment so as an example if you have a web service and you depend on a billing service
[4012.84 --> 4017.56]  then when you run auto dev uh you don't specify anything about the billing service except that you
[4017.56 --> 4022.48]  depend on it and when you run auto dev when you go in there we'll have the billing service running for
[4022.48 --> 4029.14]  you we'll have fake data already in it um it's just sort of ready to go um and the onus of how to
[4029.14 --> 4033.24]  install that billing service like how did auto know how to do that goes on the billing services app
[4033.24 --> 4038.04]  file um so auto might just know implicitly by being like it's a ruby application here's how i'm
[4038.04 --> 4042.76]  going to set it up for development or you might customize auto and say this is exactly how you get
[4042.76 --> 4048.70]  your fake data into this thing and auto will do it for you um so that's a big difference i think today
[4048.70 --> 4054.02]  uh i don't think anyone would say microservice development is easy today um but some of the
[4054.02 --> 4059.98]  practices that are emerging today are for example using um using docker for uh microservice development
[4059.98 --> 4065.40]  um and the main pitfall i found there is that while docker does have a really nice thing called
[4065.40 --> 4070.92]  compose in order to start a bunch of different containers and link link them as needed as a single
[4070.92 --> 4077.62]  unit basically in one file the problem is like as a developer you still need to know all your
[4077.62 --> 4081.98]  dependencies but not only all your dependencies you also need to know all the dependencies dependencies
[4081.98 --> 4087.70]  and you just need to flatten the tree in that in every file um and so that's really brittle if an
[4087.70 --> 4092.90]  upstream just changes what they depend on then it affects every downstream um the other thing is you
[4092.90 --> 4097.34]  not only need to know them you need to know how to install and configure them and so it pushes all
[4097.34 --> 4103.54]  this effort out to the edge uh to the the final application um and the approach auto takes instead
[4103.54 --> 4107.46]  it's more of a pointer like approach it's like i depend on this thing and it'll tell you how to set
[4107.46 --> 4112.52]  itself up and it'll tell you what it depends on um and so this is what this is the complexity that
[4112.52 --> 4118.70]  auto now manages for you this is uh probably a good place to break we got the this is our final break
[4118.70 --> 4124.88]  before we clear this show but we got jay we got a couple more topics for for mitchell on auto so we're
[4124.88 --> 4129.62]  gonna keep going so let's break real quick hear from a sponsor and when we come back we'll go even
[4129.62 --> 4136.60]  deeper into auto and then close out with mitchell so we're back we're excited about our new sponsorship
[4136.60 --> 4141.82]  with linode they're huge fans of the show and are excited to support what we're doing here and they
[4141.82 --> 4147.68]  want to invite every single listener of the changelog to try out one of the fastest most efficient ssd
[4147.68 --> 4154.26]  cloud servers on the market get a linode cloud server up and running in seconds with your choice of
[4154.26 --> 4159.60]  linux distro resources and node location they've got eight data centers spread all the
[4159.60 --> 4165.58]  across the world north america europe and asia pacific plans started just ten dollars a month
[4165.58 --> 4171.90]  with hourly billing and a monthly cap on all plans and add-on services like backups node balancers
[4171.90 --> 4177.58]  longview and even linode managed and for those who are already familiar with linode they recently
[4177.58 --> 4184.14]  switched from zen to kvm and the latest unix benchmark showed a plus 300 performance increase
[4184.14 --> 4189.02]  we'll drop a link in the show notes for those benchmarks for you to check out get forward access
[4189.02 --> 4195.52]  for more control run vms run containers or even a private git server enjoy native ssd cloud
[4195.52 --> 4203.08]  storage a 40 gigabit network and intel e5 processors use the code changelog10 with unlimited
[4203.08 --> 4209.10]  uses tell your friends it doesn't expire this year it expires the end of next year so use it as much
[4209.10 --> 4215.54]  as you want again that code is changelog10 head to linode.com slash changelog and tell them
[4215.54 --> 4223.80]  the changelog sent you all right we're here again with mitchell uh and jared earlier you kind of
[4223.80 --> 4229.68]  amen and you laughed and you were excited about uh giggled maybe you giggled something you were
[4229.68 --> 4236.60]  excited say it i giggled you giggled you were excited about mitchell's promise of auto simplifying
[4236.60 --> 4241.36]  deployment for developers so uh mitchell maybe you can lead us into what auto is doing for deployment
[4241.36 --> 4247.92]  sure so um if you recall sort of when i talked about why vagrant wasn't good at deployment it was
[4247.92 --> 4252.56]  that you couldn't your your description of a development environment just wasn't a good
[4252.56 --> 4257.34]  description of a production environment and the difference that auto makes is that since we've
[4257.34 --> 4263.72]  moved up to this application level of abstraction um we could change things for you in production we
[4263.72 --> 4270.86]  could we know what the app is so we could do different things so uh as an example uh when you uh
[4270.86 --> 4277.46]  deploy a php application i'm sorry ruby application um we do support php but i'll use ruby as an example
[4277.46 --> 4283.38]  just because i'm more familiar with it uh when you deploy a ruby application uh we set up uh on amazon
[4283.38 --> 4289.68]  uh currently only amazon uh we can support other infrastructures but later so um on amazon we'll set
[4289.68 --> 4296.92]  up a server we install uh we install fusion uh passenger we configure all the permissions we we bundle your
[4296.92 --> 4302.48]  application for deployment uh we do all this stuff and then get it up and running um we'll there's
[4302.48 --> 4308.70]  also knobs to set up load balancers deploy multiple server counts like i want three behind a load balancer
[4308.70 --> 4315.52]  um and then with the microservice stuff we actually configure automatically for you we configure our
[4315.52 --> 4321.10]  other project console so uh consoles our service discovery tool uh that's sort of all you need to know
[4321.10 --> 4326.46]  it'll tell you where your services are so you can find them uh we automatically install and configure
[4326.46 --> 4332.14]  that so that when you deploy your web application uh the billing you know api for example is always
[4332.14 --> 4337.62]  going to be at billing.service.console as a dns like entry and you don't need to worry about where that
[4337.62 --> 4343.02]  is like auto manage that for you but it's always there for you and uh that's sort of the idea behind
[4343.02 --> 4348.64]  deployment currently in its current state we get a lot fancier uh in some upcoming versions around
[4348.64 --> 4356.04]  auto scaling and uh and doing some other things but for now the idea is that we will get that
[4356.04 --> 4361.72]  application into production you can go to a url and see it running uh and yeah that's the idea
[4361.72 --> 4365.88]  that sounds like a good opportunity for community involvement are you guys ready for you know
[4365.88 --> 4370.14]  different infrastructure people to come and get involved or is it still too early days for that
[4370.14 --> 4376.80]  kind of help yeah we're super ready um so we're focusing on different the ways the right way to set up
[4376.80 --> 4381.44]  an application when you deploy right now we're not we're we have actually already pull requests for
[4381.44 --> 4387.12]  um open stack support and something else and it's just we're not going to merge those yet we're holding
[4387.12 --> 4392.58]  back on those because we want to make one infrastructure really really good uh before we
[4392.58 --> 4398.48]  move on to others so the main focus right now is and i'll give you a real example the php community
[4398.48 --> 4406.30]  noticed that we were deploying php with apache and mod php and apparently the best practice today again
[4406.30 --> 4412.92]  i'm not a php developer so of course i messed this up but the best practice today is nginx um and a
[4412.92 --> 4419.86]  longer living process not not like mod php so um they made a pull request which is to change it to
[4419.86 --> 4424.96]  nginx and and so the next version of auto will use nginx for php which is the right way to do it
[4424.96 --> 4430.42]  and and sort of like i mentioned before auto's deployment stuff isn't ready for maintenance yet it's
[4430.42 --> 4436.46]  not ready for redeploys and stuff like that but uh once we get auto 0.3 out there the idea is that
[4436.46 --> 4441.24]  you will have already deployed your application you download the new version of auto um you recompile
[4441.24 --> 4446.12]  uh your app file that that's the safety mechanism so that every update like things don't change but
[4446.12 --> 4452.54]  uh you you recompile your app file you redeploy and then auto will minimal or zero downtime will
[4452.54 --> 4457.14]  you know spin up new servers with nginx rather than apache and slowly spin drain and spin down the other
[4457.14 --> 4462.88]  ones for you so that your infrastructure just became better um by upgrading auto which is the
[4462.88 --> 4467.88]  the long-term idea so here's the point where i make you really uncomfortable by asking you to tell me
[4467.88 --> 4474.88]  when auto deploy is going to be ready for me to put it into production uh yeah so you i do want to make
[4474.88 --> 4479.00]  clear that like auto deploy definitely works today you could download auto right now you could deploy
[4479.00 --> 4484.60]  something it'll run your application you can visit it in a browser it works um what it isn't good at
[4484.60 --> 4489.04]  and just again just trying to be super clear i know i've said it is is maintenance so redeploying
[4489.04 --> 4493.14]  an application changing your infrastructure how do we do that with minimal downtime that sort of stuff
[4493.14 --> 4500.74]  uh and that's the major focus of auto 0.3 so 0.2 is going to come out next month um and 0.3 i hope i
[4500.74 --> 4505.54]  could do before the end of the year um but if not it'll i would i would commit to sort of january next
[4505.54 --> 4511.76]  year it's we're pushing really hard to get it out there because we want this dream to be completely real
[4511.76 --> 4518.08]  for people some folks adhere to semantic versioning and they they want to see a 1.0 is there a roadmap
[4518.08 --> 4523.02]  to 1.0 or do you consider 0.3 is going to be production ready what what's your thoughts on
[4523.02 --> 4531.84]  versioning yeah so um at hashi corp we don't follow semantic versioning for our end user products um i
[4531.84 --> 4536.38]  think we follow semantic versioning for all our libraries i think it's really important but um sort
[4536.38 --> 4542.56]  of for any user stuff we just we just maintain backwards compatibility really heavily so uh we
[4542.56 --> 4548.30]  probably won't break app file compatibility and uh 0.3 is around the point for all our projects where
[4548.30 --> 4553.84]  uh if you're an early adopter um but you want things to work like that's the release that will
[4553.84 --> 4559.32]  that you should be comfortable with um and we hopefully will come out with a 1.0 of a lot of
[4559.32 --> 4565.24]  stuff next year but probably not auto uh but a lot of our other stuff real quick before we wrap up
[4565.24 --> 4571.42]  here getting started what do i do you just uh go to autoproject.io and go through the getting
[4571.42 --> 4577.38]  started guide which will uh in simple steps is download auto find a project you care about
[4577.38 --> 4582.34]  run auto compile auto dev and you got a full development environment uh next step run auto
[4582.34 --> 4587.34]  deploy and it'll deploy it for you that sounds too easy is there anything harder we can do it
[4587.34 --> 4592.58]  sounds like 10 minutes to not even uh yeah most of your time is just waiting for you know cloud
[4592.58 --> 4598.66]  platforms and things like that so pretty pretty relaxed process okay last question before we go
[4598.66 --> 4606.58]  to our closing questions is vagrant six years old now is a ruby project written in ruby auto the brand
[4606.58 --> 4616.16]  new project from you is written in go your thoughts um also all our projects since vagrant have been in go
[4616.16 --> 4621.82]  and uh and i don't regret at all writing vagrant and ruby it was the right choice at the time but i
[4621.82 --> 4627.74]  i do think that if go had existed uh in a in a stable production ready form like six years ago
[4627.74 --> 4634.62]  then i probably would use it um go is just uh i i really like the language a lot and i think that
[4634.62 --> 4640.82]  ruby itself is a good language but for writing end user applications that run on multiple platforms that
[4640.82 --> 4647.26]  you want to be performance and uh sort of you want lower level control over things go is a much
[4647.26 --> 4653.88]  better way to do it um also a lot of our projects not auto as much it's it's certainly in there just
[4653.88 --> 4659.66]  not as prominently but a lot of our projects uh care a lot about concurrency and parallelism and
[4659.66 --> 4665.52]  uh go just makes that you know it being natively part of the language uh makes it quite a bit better
[4665.52 --> 4671.76]  and i don't think anyone in ruby would argue that point too much i guess jared kind of lied it's not
[4671.76 --> 4678.46]  exactly the last question um and it won't make you fun comfortable either um but i was wondering if
[4678.46 --> 4684.10]  you can share some stories or just any anything you can share on who's using auto right now that
[4684.10 --> 4691.00]  is noteworthy and any noteworthy ways they're using auto uh i would say like i would just honestly say
[4691.00 --> 4696.68]  that nobody noteworthy is using auto right now a lot of people are playing with it and uh i'm actually
[4696.68 --> 4701.92]  glad to say nobody noteworthy is using it right now i i i like early adopters to be more you know
[4701.92 --> 4708.86]  tinkerers and and things like that so uh from the auto side of things nobody yet uh but i don't
[4708.86 --> 4715.56]  consider that a bad thing gotcha but i guess on the flip side you know auto from a vanity metric um
[4715.56 --> 4722.24]  auto got almost 3 500 stars uh it got 3 000 stars sort of in less than a week of it being released so
[4722.24 --> 4726.50]  there's a ton of people interested in it um i could see the download numbers and they're doing really
[4726.50 --> 4731.52]  well um but i i think uh rightfully so it's a bunch of experimentation right now and it'll probably
[4731.52 --> 4738.56]  be that way until auto 0.3 just to go back to the semantic versioning 0.3 is what we think
[4738.56 --> 4744.34]  production ready will be uh yeah yeah well mitchell it's obviously been a ton of fun having you back
[4744.34 --> 4751.52]  on the show and uh we we close the show with some interesting questions sometimes we ask the hero
[4751.52 --> 4757.24]  questions but since you're a three pete we won't ask those questions again and uh early in this show
[4757.24 --> 4763.22]  before we even start recorded we we cleared asking you this question which is this question actually
[4763.22 --> 4769.74]  has some history with me personally because i i began podcasting probably late 2006 early 2007 and
[4769.74 --> 4774.98]  this show we had this question at the end of the show called the super secret question and i can't
[4774.98 --> 4780.46]  even take onus of it i didn't begin it but i like the question so i figured it would make sense to ask
[4780.46 --> 4787.42]  you this so what is something super secret that no one knows about that either you hashi corp your
[4787.42 --> 4791.74]  team something you're building something that's happening it can be big can be small but whatever
[4791.74 --> 4795.26]  what's something super secret that no one knows about that you can share with the audience here today
[4795.26 --> 4800.88]  i'll just share something personal that's super secret that i think will entertain people um
[4800.88 --> 4808.08]  it's super secret in the fact that i think just nobody realizes it or or i've only ever in in the
[4808.08 --> 4814.38]  entire my entire time of like visiting community speaking had one person ever figure this out um
[4814.38 --> 4823.92]  but i used to be a uh core committer um and worked for a while for um zend the php company uh and i worked
[4823.92 --> 4830.22]  on zend framework uh the php framework php web framework like the enterprise php web framework uh and i did a
[4830.22 --> 4837.04]  lot of blog posts on php development and they got a good amount of traffic so i guess my super secret
[4837.04 --> 4845.14]  is that i i came from a pretty heavy php background that uh nobody realizes that's interesting that's
[4845.14 --> 4852.48]  super secret too you ever go back and just read your old articles and laugh uh i i went back last year
[4852.48 --> 4856.86]  and found my commits and i was curious if that code still existed in the project which it doesn't but
[4856.86 --> 4863.16]  uh i did that uh but yeah only at one conference ever i gave a talk and after the talk someone was
[4863.16 --> 4870.68]  like so are you the same mitchell that did php articles and i was like what how did you know
[4870.68 --> 4878.10]  you're the person that read them yeah and uh our other favorite question that we like to ask it's not
[4878.10 --> 4882.76]  always the same question but uh it seems to be a good question to ask someone like you which is
[4882.76 --> 4888.36]  someone that's a thought leader someone's a visionary um we're curious to know what's on
[4888.36 --> 4891.60]  your open source radar so it could be a project it could be a technology it could be just something
[4891.60 --> 4896.72]  out that's that's happening in the developer space uh what's on your radar if you had a weekend
[4896.72 --> 4904.32]  to hack on something what would it be um i think the thing that is most interesting i don't think i
[4904.32 --> 4908.38]  would want to hack on it on a weekend uh but what i would want to play with i guess what i'm most
[4908.38 --> 4915.50]  interested in is all the uh sort of monitoring like startups that are popping up right now or
[4915.50 --> 4920.88]  not startups but like they're usually starts by an open source project so i'm just super interested in
[4920.88 --> 4926.62]  in the mature like when these projects become mature so to give a couple examples like influx db
[4926.62 --> 4934.54]  for storing time series data seems really interesting to me uh and uh much younger project sysdig i think
[4934.54 --> 4942.80]  it's sysdig like i think that's really cool um i'm just sort of as hasha group's not in the in the
[4942.80 --> 4951.00]  metrics or telemetry or time series sort of business and we don't plan to be anytime soon but uh it's still
[4951.00 --> 4956.30]  a really interesting technical problem and i just like playing with these tools like i still think that
[4956.30 --> 4963.62]  finding you know anomalous data out of you know time series like my how do we teach computers to
[4963.62 --> 4971.78]  just detect for us that our request per second is abnormally low right now like that sort of stuff
[4971.78 --> 4976.52]  is really fascinating and i want it to get some more interesting so i gave you a couple projects but uh
[4976.52 --> 4980.70]  the whole field is pretty popular right now so i'm just paying attention to that all right just a couple
[4980.70 --> 4989.08]  of uh promotional items that are related uh changelog.com slash 168 we uh had uh julius volson speaking
[4989.08 --> 4993.70]  about prometheus and service monitoring we're kind of related to that mitchell as well as
[4993.70 --> 5000.86]  170 which was ben johnson talking about bolt db and influx db so a couple of episodes if those are
[5000.86 --> 5010.00]  things that also uh on your radar cool and we use bolt for a lot of stuff at hachicorp so cool project
[5010.00 --> 5015.40]  nice well mitchell as much as it pains me to say that is uh pretty much all we wanted to talk to you
[5015.40 --> 5021.06]  about i mean i'm sure we can keep going on i mean you're you're a deep fella and it's easy to to pull
[5021.06 --> 5026.30]  things out of you but it's been a blast having you on thank you so much too for just uh sharing so much
[5026.30 --> 5030.86]  that you do share with the community and then coming back on this show three times i mean you're always
[5030.86 --> 5035.42]  welcome back so we look forward to uh more success for you and your team in the future but thank you
[5035.42 --> 5041.32]  so much for all the work you do in open source and all the uh insights you give and just all the ways
[5041.32 --> 5047.12]  that you serve uh the the men and women out there hacking on software so cool thanks for having me
[5047.12 --> 5052.56]  it's fun it's always fun i like you know your changelog is definitely one of the highest quality
[5052.56 --> 5057.38]  sort of uh thing that does this so it's always fun to come on here awesome man appreciate you seeing
[5057.38 --> 5063.38]  that too and to our listeners out there we have listeners we have members and without you it would
[5063.38 --> 5069.10]  not be possible uh because who would listen to the show right that that wouldn't happen so thank you
[5069.10 --> 5074.48]  for listening and to our sponsors we have sponsors that make the show possible sponsors of this show
[5074.48 --> 5081.56]  are code ship brain tree backblaze and linode brain tree backblaze and linode are new sponsors
[5081.56 --> 5088.02]  code ship obviously huge fans of the changelog and longtime supporters of the show but gotta say thanks
[5088.02 --> 5093.02]  to all those sponsors making this show possible but uh mitchell's been awesome having you back on the
[5093.02 --> 5098.06]  show but for now fellas let's say goodbye bye goodbye goodbye
[5098.06 --> 5107.84]  you
[5107.84 --> 5110.90]  you
