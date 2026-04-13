[0.00 --> 16.32]  welcome back everyone this is the changelog where a member supported blog podcast and weekly email
[16.32 --> 21.40]  covering what's fresh and what's new in open source check out the blog at the changelog.com
[21.40 --> 27.84]  our past shows at five by five dot tv slash changelog and you're listening to episode 123
[27.84 --> 33.10]  jared and i we caught up with chad whittaker the founder of gidip and we talked to him about what's
[33.10 --> 37.30]  new this year with gidip and the directions they're taking today's show is sponsored by our
[37.30 --> 43.04]  friends at rackspace code ship and top tile we'll tell you a bit more about code ship and top tile
[43.04 --> 48.34]  later in the show but our friends at rackspace they continue to dedicate themselves to support
[48.34 --> 53.88]  the open source and developer community and they're doing it even more so with their developer
[53.88 --> 59.94]  discount now you can go make something awesome on them people who listen to the show you're makers
[59.94 --> 64.54]  each day you get up thinking of something new awesome and amazing and you want to put your
[64.54 --> 69.72]  imagination and your skills to work and rackspace would like to give you something special just to
[69.72 --> 75.16]  say thank you so sign up today for their developer discount and get three hundred dollars in free
[75.16 --> 80.74]  cloud services on your rackspace cloud account this discount applies to new products like their
[80.74 --> 87.08]  performance cloud servers and cloud queues as well you're even eligible for early access to new
[87.08 --> 91.68]  features and products that they roll out so that's that's pretty cool make something awesome and get
[91.68 --> 98.10]  started today go to developer.rackspace.com slash dev trial and now on to the show
[98.10 --> 106.20]  we're joined today by an awesome friend previous uh previous person that's been on the show before
[106.20 --> 112.54]  chad whitaker founder of get up uh i'm adam stakovic and we also have the managing editor jared santo on the
[112.54 --> 117.54]  show so we got uh three people on the call today a fun show lineup it's kind of like a
[117.54 --> 123.10]  uh it's definitely like a reconvening right chad because you were on the show almost to the day this time
[123.10 --> 130.52]  last year absolutely and our annual may call our check-in yes and and you got a birthday coming up soon not
[130.52 --> 137.30]  personally but get it all right yep get it get it is gonna be two years old on june 1st june 1st wow
[137.30 --> 145.54]  couple weeks here scary right you know this has been a really big milestone in my mind since i started
[145.54 --> 152.40]  i've kind of thought two years is is the amount of time i've given myself to work on this and see if
[152.40 --> 158.08]  this is going to go anywhere so we're coming up on that milestone so it is scary maybe yeah uh kind of
[158.08 --> 162.82]  definitely a chance to reflect uh you know on what's happened the past couple years and where
[162.82 --> 170.18]  we are so when you say that uh does that does that mean there may be no future in get up or are you
[170.18 --> 174.90]  thinking about quitting it i mean what's that was the question right okay right the question what's the
[174.90 --> 182.88]  answer yeah the the answer is full steam ahead uh that's the good news uh yeah i mean i i kind of
[182.88 --> 186.76]  said all right i'm gonna be heads down and i'm gonna just go for it right and i'm not gonna pay
[186.76 --> 192.50]  attention to you know how fast we're growing or you know how well we're doing or what's going on
[192.50 --> 198.44]  with it i'm not i'm gonna kind of like stay heads down and just work and plow ahead on it and then
[198.44 --> 204.68]  at that two-year mark that's when i'll come up for air and say all right where are we you know is this
[204.68 --> 210.20]  thing uh you know is this thing gonna work is this going anywhere do i still love working on it do i
[210.20 --> 215.74]  not love working on it um you know and make a decision and you know the bottom line is i still
[215.74 --> 222.96]  love working on it and we're growing for how deep we've set the plow i'm pretty encouraged by our
[222.96 --> 229.06]  growth um when i compare myself to others i get discouraged but when i look at get up itself and
[229.06 --> 233.90]  realize that it's something i still believe in and love doing uh you know that i'm encouraged so
[233.90 --> 238.84]  you know the short answer is yes we're we're moving ahead full steam ahead on get it so chad for
[238.84 --> 243.20]  those of us who weren't around last may i think that was episode 87 if anyone wants to go back and
[243.20 --> 250.08]  listen can you just give us briefly the get up uh elevator pitch yes get it is a way to give money
[250.08 --> 257.48]  every week to people and teams you believe in so the mission of get it is actually to enable an
[257.48 --> 264.36]  economy of gratitude and generosity uh and practically what that means the way we're instantiating that is
[264.36 --> 268.56]  giving money every week to people you believe in right so you're using somebody's open
[268.56 --> 272.90]  source libraries and you really appreciate the work that you're that they're doing and you want
[272.90 --> 277.50]  to show your appreciation and gratitude and you want to support them get up as a way to do that
[277.50 --> 283.60]  uh by setting up a weekly recurring donation to them as small as a penny up to a hundred dollars a week
[283.60 --> 289.30]  and it's a no strings attached gift that's uh that's one of the that that's where get it is on the scale
[289.30 --> 295.80]  of crowdfunding from like investment through you know kickstarter i'm getting a sticker i'm getting a
[295.80 --> 301.08]  product you know get it is on the far end where this is really uh this is really a gift so you
[301.08 --> 304.74]  don't tell them i'm funding you towards this goal and as long as you're working on that goal
[304.74 --> 310.56]  yeah exactly it's really like a patronage model it's like i believe in the work you do and i want
[310.56 --> 313.80]  you to do more of it you know i trust that you're going to take this money and you're going to do
[313.80 --> 319.22]  awesome stuff with it you know so it's really trying to yeah trying to dial in on that like i believe
[319.22 --> 324.48]  in you keep doing awesome stuff right uh yeah so that's what that's what that's what we're doing
[324.48 --> 331.18]  and we've been um so i guess to uh to recap where we're at we've got we're coming up on 3 000 active
[331.18 --> 337.48]  users and i guess we could check so it was a year ago was it yeah let's check our charts real quick
[337.48 --> 343.30]  most of the day yeah okay so we've got uh let's check the charts real quick so right now we've got
[343.30 --> 350.48]  28 000 or you know 2 887 so we're coming up on 3 000 weekly users that's people who either give or
[350.48 --> 359.84]  receive or both on the site and we moved uh 13 400 you what was it yesterday so we're up over 13 000
[359.84 --> 365.40]  let's go back let's dial it back a year um so that would be week 50 i'm looking at the
[365.40 --> 373.90]  get it.com slash about slash charts html and two years or a year ago we were at 1 000 users
[373.90 --> 382.40]  and what about three thousand dollars wow yes so we've grown we've grown it looks like uh 1800 users
[382.40 --> 388.60]  so you know almost 200 and then uh and it looks like a thousand dollars or ten thousand dollars we've
[388.60 --> 394.56]  grown ten thousand dollars which would be what quickly uh you know 4x 5x over a year ago you know so
[394.56 --> 400.12]  that's not nothing um that's huge man i mean it's not quite a hockey stick but like i said for as
[400.12 --> 404.48]  deep as we set the plow i'm i'm pretty encouraged for where we're at so i'm looking at these charts
[404.48 --> 409.94]  here on your slash about slash charts you have a withdrawal it looks like the weekly gifts like
[409.94 --> 415.58]  you said is 13 444 and your withdrawals is at 78 60 so the rest is that differential just what's
[415.58 --> 420.44]  being traded inside of get up or not traded but given escrowed yeah we would say escrowed inside of
[420.44 --> 426.44]  get it so yeah get up is like this bubble within or this loop or this uh circle within the larger
[426.44 --> 431.54]  economy right so you move money into get it uh you shuffle it around inside of get it and then
[431.54 --> 436.30]  you pull it out the other side uh right so there is an amount of money which is actually if you click
[436.30 --> 441.72]  on the stats link that's at the top of that page i think we're at like 100k escrowed within get it right
[441.72 --> 449.12]  now something like that it's kind of a little over 100k escrowed and get it yeah so you know we we
[449.12 --> 457.02]  doubled we doubled three times last year uh every four or five months and then looking at these charts
[457.02 --> 461.86]  we've kind of slowed the past month or two but i don't know it's it's hard to read these things
[461.86 --> 466.80]  sometimes but yeah the the past the past month or two it's started to flatten a little bit and
[466.80 --> 471.92]  kind of scratch our head a little bit about that i mean the way the way i'm seeing it is that last
[471.92 --> 478.68]  year okay so the for the first for the first year 2012 started the middle of the year and the name of
[478.68 --> 484.42]  the game was you know we came out of the gate pretty fast it was encouraging and then it was all about
[484.42 --> 489.66]  transitioning from uh working on get it as a side project to me personally working on a full-time
[489.66 --> 495.72]  that was 2012 so by the end of 2012 i was working on get it full-time so when i talked to you guys last
[495.72 --> 501.88]  year uh in may there's no transition yeah well i i i pretty much transitioned into get it full-time
[501.88 --> 509.54]  but then the challenge in in 2013 was let's go from just chad working on it to a team working on it
[509.54 --> 517.40]  right because you know you know zuckerberg isn't the only one working on facebook right um you know it
[517.40 --> 522.96]  it takes a team to build a product right and that's no different for an open product than for anything
[522.96 --> 527.86]  else or any other company uh you know so that was that was really the name of the game in 2013 was
[527.86 --> 532.98]  let's go from just chad you know i'm not building get it i'm building a team that's building get it
[532.98 --> 537.08]  is something that i think i think kenneth wasn't kenneth on the call last year i believe so yeah
[537.08 --> 541.72]  yeah he was he brought up that quote i'd put out there that yeah this year we're you know i'm not
[541.72 --> 546.10]  building get it i'm building a team that's building get it and so that's what 2013 was about
[546.10 --> 555.78]  and it worked um in january of this year so january 2014 we had our first annual get it company retreat
[555.78 --> 562.06]  which i hosted here at my house in pittsburgh outside of pittsburgh during the polar vortex
[562.06 --> 568.04]  so nice time the middle is yeah exactly it's more of a winter we um we convinced we had a dozen
[568.04 --> 574.10]  people fly in uh is that your team 12 people that's the that's the folks that traveled to pittsburgh
[574.10 --> 580.28]  right so we had a wider team because i mean it's like any open source project you've got uh you've
[580.28 --> 583.86]  you've got a core of people that are really committed and then you've got this much wider
[583.86 --> 589.30]  cloud of people that are interested you know it's a long tail right it's like so i think at that point
[589.30 --> 596.68]  we probably had 60 or 70 people quote unquote on the team uh which specifically means that they're
[596.68 --> 603.86]  uh they are they're listed on the team on get it get it is funded on get it and we have this
[603.86 --> 608.96]  team's feature where when you give money to get it the question is how do we split that so we split
[608.96 --> 614.58]  that 70 ways and so those 70 people are are kind of our wider our wider base and then out of that 70
[614.58 --> 622.58]  people a dozen of them came to pittsburgh uh for our meetup in january um yeah so you know that was
[622.58 --> 627.26]  that was kind of a that was a milestone for us that was a success right like yes we've got a team this
[627.26 --> 632.24]  is real you know my wife's like wait there's people besides you that are working on get it right
[632.24 --> 635.94]  because like you know i do it all on the internet you wouldn't see it in real life right it's like
[635.94 --> 642.16]  here's all these people in my house all of a sudden um you know chad yeah they're real
[642.16 --> 648.30]  besides chad yeah people believe in this besides chad yes exactly i've always wondered at what your
[648.30 --> 653.38]  wife thinks of it because um you're really public so last year we kind of made fun of you in some degree
[653.38 --> 660.88]  for sharing your address and your uh phone number and you know the security issues that may come up from
[660.88 --> 667.60]  that especially as you get more and more infamous with i mean and to some degree you're pretty open
[667.60 --> 675.00]  about your very opinionated ways and some don't agree with you right yeah absolutely um yeah i mean
[675.00 --> 682.22]  there haven't been any disasters as far as that goes this past year knock on wood i guess uh yeah i mean
[682.22 --> 689.58]  look there's risks in life you know and yeah you can be you know i always think of the nickel mine uh
[689.58 --> 693.98]  wasn't that the the amish shooting wasn't that nickel mine pennsylvania or whatever right it's like
[693.98 --> 697.90]  you can be amish you can be living out in the countryside you know totally disconnected like
[697.90 --> 704.66]  not sharing you know like the least uh connected in public person right all right and still some
[704.66 --> 708.98]  nut job is going to bring a gun into your school and shoot all your kids you know so it's not like i
[708.98 --> 715.90]  don't know i'm not a statistician by training but i don't know i i don't think
[715.90 --> 724.24]  my gut says it's not safer uh than not right it's like there what are the chances of of having uh you
[724.24 --> 729.94]  know having somebody do you harm you know what what what causes that what makes you more likely to
[729.94 --> 737.88]  to be hurt than not um and you know this is this is a point at which i need to pause uh in the light of
[737.88 --> 745.78]  a conversation i've especially been having last night i mean there you know i'm a rich white male
[745.78 --> 753.26]  i enjoy lots of privilege and that's uh that's my experience of being open on the internet
[753.26 --> 765.18]  is absolutely what's the word uh shaped uh by by that right um you know if there's this man we're
[765.18 --> 769.80]  getting in deep right off the bat so one of the things happened one of the one of the unexpected
[769.80 --> 775.00]  turn of events over the past year is that get up is for activists right like we came out of the gate
[775.00 --> 779.52]  and we're like get up is for open source and we're going to fund open source on get up and we're doing
[779.52 --> 784.42]  some of that but the the largest receivers on get up and everybody you know everybody but uh you know
[784.42 --> 791.32]  the the the top receivers board on get up is activists uh gender activists and uh feminist
[791.32 --> 797.60]  activists right uh so that that was a left turn from uh you know from my point of view it's it's it's
[797.60 --> 802.16]  kind of a head scratcher for me it's like you know all right uh cool this is one of those cases
[802.16 --> 806.50]  where it's like you know you don't know how your product's going to be used you know it's like your
[806.50 --> 812.12]  users drive your product right right and and there's always those surprises in building a product it's
[812.12 --> 815.70]  like oh my gosh like i never anticipated it would be used this way but here it is be used this way
[815.70 --> 821.80]  you know and i have anticipated that you know i've always wanted for get up to grow beyond uh just
[821.80 --> 828.14]  open source right and uh and and it's done that you know so that's that's definitely a success
[828.14 --> 833.88]  um but what it means is that i'm learning a lot right i'm i'm getting lots of feedback because
[833.88 --> 838.32]  now and we're actually last night was kind of where it started coming to a head like there's
[838.32 --> 844.48]  been this mounting tension a little bit uh you know because there's all these activists and using
[844.48 --> 851.60]  gidip and being funded on it there's been a little bit of a disconnect um you know because i'm not a
[851.60 --> 855.78]  feminist i'm not an activist you know what i mean it's like that's that hasn't been my uh you know
[855.78 --> 863.30]  driving concern on gidip and so yeah so i feel like we're just starting to not just starting but
[863.30 --> 871.20]  um i'm i'm looking for how to establish a relationship with those users right those people
[871.20 --> 876.36]  those users of mine on gidip it's like all right um let's talk let's get to know each other let's
[876.36 --> 880.12]  get to know one another let's get to know each other um you know let me understand where you're
[880.12 --> 884.48]  coming from and how you're using the platform what your needs are on it and whatnot and you can get
[884.48 --> 890.56]  to know me a little bit because as you said i am uh you know leading a fairly opinionated online life
[890.56 --> 896.64]  in this uh way of doing open things right open companies and open calls you know i love that we're
[896.64 --> 902.98]  live streaming this here and and i'm very comfortable with that um you know but i'm i'm hearing a lot of
[902.98 --> 909.14]  uh different feedback i'm trying to take that on board and that's that's part of the adventure right now
[909.14 --> 914.06]  yeah it was interesting i saw some i think there was some retweeting going of some gidip i think even the
[914.06 --> 919.64]  getup account perhaps retweeted some criticism coming your way and then i was surprised to find
[919.64 --> 924.34]  that the criticism was coming from one of the top receivers on your home page i love it right yeah
[924.34 --> 929.20]  and i was kind of like oh well that's interesting that's i think it's great you know i mean shanley
[929.20 --> 936.70]  was uh the one i was talking to last night and yeah she is one of the top receivers um and right and
[936.70 --> 943.58]  she's you know a very opinionated person in her own right and has uh you know a fairly brusque
[943.58 --> 951.28]  approach to online conversation and i don't know though it's i don't know oh it felt yeah
[951.28 --> 958.58]  it it's i don't know well you get into a situation where you can really you know like you you know you
[958.58 --> 963.60]  had said you started get up and even let's maybe rewind a tiny bit to kind of give some foundation to
[963.60 --> 968.64]  some of the conversation we're having right now which is and to my understanding you you've started
[968.64 --> 973.12]  this to fund open source to some degree so that's also a reason why it's called gidip and some people
[973.12 --> 980.56]  call it get tip yeah so it stemmed from you know get github you know open source movement um uh-huh
[980.56 --> 986.30]  yeah to definitely to an extent uh you know it started when i first bought the domain i was like oh
[986.30 --> 991.40]  my gosh we need tip jar for github you know i was thinking i was sitting in my in my nice cushy
[991.40 --> 995.62]  corporate job you know totally bored out of my mind and it was like oh i would love to just
[995.62 --> 1000.20]  work on my web framework all day long you know this aspen web framework that i've got like
[1000.20 --> 1004.78]  what would i need to do like why you know what if there were a tip jar on github and then i would
[1004.78 --> 1009.68]  be freed up to work on open source stuff all day long so that was the that was the uh beginning of
[1009.68 --> 1016.02]  it and how i named it get it get tip exactly it was how it started really quickly i mean i think i
[1016.02 --> 1021.54]  invented it in right around this time okay may 11th and then launched it three weeks later was the
[1021.54 --> 1029.16]  zero with payday and you know within those three weeks even uh it it changed from being just uh just
[1029.16 --> 1033.46]  to tip jar for github to you know what this is a lot bigger this could be a lot bigger i actually
[1033.46 --> 1042.70]  almost named it logstown yeah so logstown is the name of the indian village that i that is now
[1042.70 --> 1048.76]  present day ambridge where i live right uh you know so it's just a a local thing here and so i
[1048.76 --> 1053.90]  bought the domains a few years ago logstown comnet norg and you know had those domains sitting around
[1053.90 --> 1057.92]  so i was like well maybe i'll use this i'll use logstown then my brother-in-law's i don't know
[1057.92 --> 1062.86]  funny side story my brother my brother-in-law's like no man that that makes me think i'm going to
[1062.86 --> 1067.58]  the washroom he always calls me washroom it's like it makes me think i'm going to the washroom he's
[1067.58 --> 1072.30]  like just stick with git tip git tip is nice because it has like the itti it's like very
[1072.30 --> 1077.32]  parallel and everything says a nice name you know he's not a geek at all he's a he's a scientist and
[1077.32 --> 1082.36]  a musician but he's not a programmer uh necessarily not an open source guy uh yeah so he was like just
[1082.36 --> 1087.28]  call it git tip it's okay this is like all right well you know he didn't know anything about github or
[1087.28 --> 1092.16]  anything right he just thought the name was you know cool and memorable or whatever yeah and didn't
[1092.16 --> 1098.54]  like logstown so so right but my point is that even even by the time we launched uh you know i was
[1098.54 --> 1103.56]  already thinking that this is going to be bigger than open source uh you know but that's you're
[1103.56 --> 1109.32]  right that's where it started so now i like to say that that git tip is related to github in the same
[1109.32 --> 1115.50]  way that wiki leaks is related to wikipedia yeah you know in other words they're not really connected
[1115.50 --> 1120.76]  at all but through this historical accident uh you know there's some a little bit of brand confusion
[1120.76 --> 1124.54]  going on there but i think there's some you have some signal signaling uh towards that end on the
[1124.54 --> 1129.16]  home page where it's who inspires you and there's a form and it's enter a twitter username yeah that's
[1129.16 --> 1134.24]  what you start and github is in the select box but it's not the first thing right right right yeah
[1134.24 --> 1139.98]  yeah exactly you know so so it's awesome that um you know that shanley and ash and everybody else
[1139.98 --> 1147.08]  uh you know not that they're not all programmers but you know more folks dot activism i mean that's
[1147.08 --> 1150.54]  great that's perfect that's what we want we want but you know i want it to expand
[1150.54 --> 1155.80]  uh beyond open source and it's done that so that's you know that's a that's a a win in my
[1155.80 --> 1160.20]  view from the past year um but yeah we are having some interesting conversations around
[1160.20 --> 1168.12]  you know the whole open company idea and what that means uh you know how how you balance
[1168.12 --> 1173.70]  okay so my goal with open companies get if we call it an open company meaning we share as much as
[1173.70 --> 1179.08]  possible we charge as little as possible and then we're funded on a pay what you want basis on
[1179.08 --> 1187.34]  get it itself and you know my driving motivation open company is not an end in itself for me open
[1187.34 --> 1194.94]  company is part of uh this vision of living a life of gratitude and generosity you know i don't i don't
[1194.94 --> 1198.74]  want to hide my stuff i don't i don't want to i don't want to work on proprietary things i want to
[1198.74 --> 1204.04]  share the stuff i work on i want to give this stuff away for free that i work on you know um it just
[1204.04 --> 1208.78]  as a matter of principle and how i want to live my life i want to i want to share what i have um as
[1208.78 --> 1215.56]  much as possible and you know so that's where i'm coming from with open companies but then uh you know
[1215.56 --> 1220.66]  what shanley was feeding back last night and i've heard from others is you know it's really threatening
[1220.66 --> 1224.48]  if you experience a lot of harassment online to think about i have to sneeze one sec
[1224.48 --> 1233.32]  the first super loud sneeze on the changelog that was an epic sneeze wasn't it i did manage to get
[1233.32 --> 1240.56]  my microphone away from my face that's awesome like a looney tunes cartoon yeah there you go um
[1240.56 --> 1249.72]  right so uh so what i'm hearing is you know there's there's people for whom uh you know the internet is
[1249.72 --> 1254.78]  a very much more threatening place than it is for me right and you're getting lots of death threats
[1254.78 --> 1262.52]  and rape threats and whatnot and that's really you know uh terrible right that's horrible like uh you
[1262.52 --> 1272.36]  know goodness sorry um and so you know for someone like that the idea of putting even more online and
[1272.36 --> 1279.48]  you know exposing yourself even more uh you know obviously comes across as like a wtf right
[1279.48 --> 1285.46]  yeah um yeah you know but that that's the conversation we're having i think we're dancing
[1285.46 --> 1290.74]  on this idea of radical transparency i think that's really what the the phrase that was being used and
[1290.74 --> 1296.66]  it's uh we even said you know you're infamous to some degree because not only have you had maybe some
[1296.66 --> 1301.84]  abrasions here but also with journalists that don't really appease to the way you want to operate
[1301.84 --> 1308.02]  of being open so you've kind of had some angst and some um abrasions with other people too so it's not
[1308.02 --> 1312.78]  just your user base it's it's others too because you want to be radically transparent about who you
[1312.78 --> 1318.08]  are and what you do with your company what you're doing for the community yeah yeah i mean i don't
[1318.08 --> 1324.52]  okay so i don't experience it as abrasions right i i mean it's an opportunity cost when i um turned
[1324.52 --> 1329.84]  down tech crunch that was kind of kicked a lot of this off you know i got an interview uh opportunity
[1329.84 --> 1335.40]  with tech crunch and i had just been starting to experiment with uh i think i'd started using the
[1335.40 --> 1339.90]  phrase open company at that point but uh you know hadn't started really pushing open calls and
[1339.90 --> 1345.08]  whatnot and you know decided to heard from tech crunch and you know said all right i'm gonna go
[1345.08 --> 1350.00]  for it let's do this as an open call and it's an opportunity cost right because like i know that
[1350.00 --> 1354.64]  there's a pretty good chance they're gonna say no right and it's my decision to live with the
[1354.64 --> 1360.72]  consequences they say no and i don't get an interview in tech crunch and so like i'm fine with
[1360.72 --> 1366.54]  that right like i'm fine not getting an interview in tech crunch so i don't you know i'm not and then
[1366.54 --> 1373.14]  more recently um jason calacanis reached out to me on email uh the the angel investor uh reached out
[1373.14 --> 1378.84]  to me on email and and podcaster in his own right etc entrepreneur he reached out to me on email and
[1378.84 --> 1382.66]  said um you know would you like to have you know i'm interested in having a conversation with you and i
[1382.66 --> 1387.12]  said all right great let's do it as a hangout right and you know i was i was working with this uh
[1387.12 --> 1391.32]  person another person setting it up and kind of got the ball rolling and then jason was like whoa
[1391.32 --> 1397.94]  you know not cool you know it's like all right crap i i just shot myself in the foot again right
[1397.94 --> 1402.88]  it's an opportunity cost and it's an opportunity cost that i do feel uh but at the end of the day
[1402.88 --> 1407.86]  it's a decision that i'm making you know in full knowledge that it's you know this is the path i've
[1407.86 --> 1413.52]  kind of chosen for myself kind of painted myself in this corner uh you know but you know gidip is still
[1413.52 --> 1418.90]  growing well enough and and we're still doing well enough that you know i haven't felt fundamentally
[1418.90 --> 1424.78]  that it's the wrong decision yet um yeah i think it's it's it's still the way i'm i'm going you
[1424.78 --> 1429.20]  know but i'm i am trying to hear these other voices like uh shanley's especially in and that side of
[1429.20 --> 1435.82]  things because it's not an absolute it's not an end in itself the the purpose you know in my mind
[1435.82 --> 1443.40]  what i'm trying to do with open companies is is is bust open governments and corporations like i look
[1443.40 --> 1446.42]  at government and i look at corporations i look at snowden right that's something that happened in
[1446.42 --> 1452.42]  the past year you know since we talked last i look at snowden i look at the nsa um and you know
[1452.42 --> 1458.22]  and wikileaks you know in their own time and and you know that's crappy i don't like that right so
[1458.22 --> 1462.70]  what am i going to do about it um you know my activism in this regard you know i i see that and
[1462.70 --> 1470.32]  my answer is um i'm going to try and and live my own life in a way that's you know that that's not
[1470.32 --> 1476.04]  closed in secret right i'm going to try and live i'm going to try and create the system in that
[1476.04 --> 1483.22]  i don't know in in which snowden is a moot point right you know in which there's nothing to leak in
[1483.22 --> 1489.24]  the first place pretty much you know what i mean yeah so you know which isn't for everybody and
[1489.24 --> 1492.72]  that's fine but like that's that's where i'm coming from with this right it's not transparency for
[1492.72 --> 1497.74]  its own sake and it you know it can come across kind of cartoonish on the internet because that's the
[1497.74 --> 1502.36]  internet right like that's uh you know that's memes it's like boiling stuff down to their you
[1502.36 --> 1507.38]  know caricatured essentials but you know obviously it's more sophisticated than that right like i've
[1507.38 --> 1513.80]  got people on my team that don't do video calls for one reason or another you know well we have a
[1513.80 --> 1520.58]  daily stand-up every day at noon uh you know that we use google hangouts for we live stream right so
[1520.58 --> 1529.28]  i've got this you know quite apart from kind of the high level abstract level discussion i was having
[1529.28 --> 1533.94]  with shanley last night like there's real concrete realities in in my life and running my business
[1533.94 --> 1539.12]  that are already uh you know that have already called into question the absoluteness of this open
[1539.12 --> 1544.60]  ideal and and and you know have been forcing not forcing because i want it right it's like we're
[1544.60 --> 1549.62]  trying to nuance this i don't want no open company isn't a cartoon it's a reality right i want it to be
[1549.62 --> 1555.72]  real and that means taking into account uh you know the the sophistication of it and the nuance of
[1555.72 --> 1561.00]  it um and we're already dealing with that so we so in the case of the stand-ups and people not wanting
[1561.00 --> 1569.30]  to be on video for for various reasons um that's fine so we just we we take their stand-up report in irc
[1569.30 --> 1575.94]  and we read it uh you know we read it on the video and they watch the video from wherever right and so
[1575.94 --> 1582.38]  then you know it's not violating uh their uh the their own what i want to say
[1582.38 --> 1589.08]  their own terms of privacy that they've negotiated with the internet you know because we each have to
[1589.08 --> 1593.10]  negotiate our own relationship with the internet and that looks different for different people
[1593.10 --> 1599.74]  and you know gidip and open companies are not about railroading people into one single right way
[1599.74 --> 1606.08]  dogmatic way to do it um i'm saying look i am privileged and as much as possible i'm going to
[1606.08 --> 1610.96]  share my privilege with as many people as possible you know that's what i'm trying to do here and you
[1610.96 --> 1614.14]  know if you're coming out from a different point of view i'm going to respect you i'm not going to
[1614.14 --> 1618.62]  violate your confidentiality your privacy we do have private channels support at gidip.com is a
[1618.62 --> 1623.28]  confidential channel um you know my phone number that's a confidential channel well except for the
[1623.28 --> 1631.00]  you know they listen to their users you got to give them credit yeah right right yeah but you know
[1631.00 --> 1637.52]  i don't violate confidentiality you know and and what i do that's a bug and i try to apologize for it
[1637.52 --> 1643.16]  let's pause the show for just a minute give a shout out to our sponsor code chip code chip is a hosted
[1643.16 --> 1648.44]  continuous deployment service that just works you can easily set up continuous integration for your
[1648.44 --> 1653.28]  application today in just a few steps and automatically deploy your code when all your tests
[1653.28 --> 1659.18]  pass code chip has great support for lots of languages test frameworks as well as notification
[1659.18 --> 1665.20]  services they easily integrate with github or bitbucket and can deploy your code to cloud services
[1665.20 --> 1672.74]  like coroku aws nojitsu google app engine or even your own servers setup takes only three minutes and you
[1672.74 --> 1677.58]  can get started today with their free plan and make sure you use the code the changelaw podcast
[1677.58 --> 1685.64]  to get a 20 discount for three months on any plan you choose again that code is the changelaw podcast
[1685.64 --> 1692.28]  and you're going to get a 20 discount for three months on any plan you choose head to coachship.io
[1692.28 --> 1698.16]  and tell them the changelaw sent you so you know i have to admit on on that front there because there
[1698.16 --> 1705.22]  was at least two times i probably like you i have i'm an idea guy i try and think and jeremy you can
[1705.22 --> 1709.46]  back me up on this i try to think outside the box i try to be a dreamer to some degree and my wife is
[1709.46 --> 1713.58]  probably if she's listening to this which she's not live but maybe she listens to it later i don't
[1713.58 --> 1719.12]  know why but uh she's she's probably thinking like absolutely he's a dreamer but there's been several
[1719.12 --> 1725.00]  times that i'm like i want to align what we're doing with the changelaw and open source and support
[1725.00 --> 1730.24]  and just in general encouragement to the community and the beautiful things that are coming from it
[1730.24 --> 1735.16]  there's been several times i want to chat with you and i'm like yeah i don't i don't mind making
[1735.16 --> 1741.08]  it open it's just it's so early the idea is so fresh it you know i'm just not quite oh you know
[1741.08 --> 1745.30]  cool with being so open like you are and i hesitated to reach out because i thought you know you'd be
[1745.30 --> 1750.76]  like yeah we can't have that conversation because i have to do it on google hangouts oh this just got
[1750.76 --> 1755.80]  real adam it's just got real stack this is great because you're right yeah you and i we've interacted a
[1755.80 --> 1759.64]  bit i i don't remember the you probably remember the email i'm like hey can we talk and i never
[1759.64 --> 1764.12]  responded because i was like we got to do it open i'm like i just i just couldn't get past it and i
[1764.12 --> 1770.06]  got busy again so you know there's that span of time there so i can appreciate someone extreme like
[1770.06 --> 1775.38]  like shanley in her case where she's getting threats and obviously there's certain like you said
[1775.38 --> 1779.84]  negotiated privacy terms you have with the internet for someone like her in her position and someone even
[1779.84 --> 1785.14]  like my position still having reservations you know yeah yeah and what i want to say is
[1785.14 --> 1790.38]  dude i love you you know and like i'm i'm not out to force you to do anything that you're not
[1790.38 --> 1799.02]  comfortable doing right and you know it seems like where that leaves us is a bit of an opportunity
[1799.02 --> 1805.24]  cost on on both of our sides right it's like um and there's so there's some you know there's some
[1805.24 --> 1809.42]  sadness on my end for that it's like well you know yeah it would be nice to work together right but
[1809.42 --> 1813.80]  yeah i've i don't know we have similar interests i would say don't you think
[1813.80 --> 1817.82]  yeah absolutely right so there's there's a lot of there's a lot of overlap and so
[1817.82 --> 1826.42]  um you know i but look it's a tricky thing all around right like and you know we've each got our
[1826.42 --> 1830.76]  life outside the internet too right like there's plenty of stuff that you're not finding out about
[1830.76 --> 1837.04]  me on the internet you know like like i'm i'm bigger than wit 537 and you know you're bigger than
[1837.04 --> 1842.22]  adam stack like we've all got these fuller richer lives and you know part of where i'm coming from is
[1842.22 --> 1849.94]  like uh you know i i want to i want to privilege that a little bit too you know it's like look like
[1849.94 --> 1856.72]  it's it's maybe okay if you know if if we don't get to pursue this together because we've each you
[1856.72 --> 1861.14]  know our lives are abundantly rich right it's like we've all got plenty of relationships and plenty of
[1861.14 --> 1865.92]  things to work on plenty of projects on the internet and fun stuff to do and then you know families and
[1865.92 --> 1872.82]  and and kids and you know and dogs and cats and you know just like stuff we love doing right and
[1872.82 --> 1880.58]  i don't know life life is abundantly rich and uh i don't know i can only feel so bad for so long for
[1880.58 --> 1886.24]  like for losing an opportunity over that because it's you know because life is so rich and because
[1886.24 --> 1890.80]  it's i don't know those are those are kind of the terms i've negotiated for myself is like
[1890.80 --> 1895.50]  part of it is that it is a limiting factor right i think i actually say this i posted a
[1895.50 --> 1900.74]  a blog post about my interview policy or a web page i put it up on my website right so here's my
[1900.74 --> 1906.90]  interview policy and in there i say you know maybe i'm being narcissistic like we all have to manage
[1906.90 --> 1913.34]  our time somehow and this you know this turns out to be one way to do it right it's like it it's
[1913.34 --> 1920.40]  i don't know man if there was if there's something if there's like a real if there's a real safety
[1920.40 --> 1926.48]  concern or a security concern of course i'm going to take any phone call and keep it private and
[1926.48 --> 1933.90]  confidential right so uh you know if you if you really you know if anybody i don't want to i don't
[1933.90 --> 1938.30]  want anyone to get the impression that's a baseline right i'm talking out loud i'm glad don't worry
[1938.30 --> 1942.26]  about it good it's okay am i going to the right direction you know there's like so so it has to be
[1942.26 --> 1948.24]  there have to be these tiers to it right it's like so fundamental foundational if there's if
[1948.24 --> 1952.96]  there's a security concern or a safety concern or a personnel issue in the case of people actually
[1952.96 --> 1958.54]  working on giddup like a sensitive personnel issue i'm handling that private privately like no questions
[1958.54 --> 1964.54]  asked give me a call you know private message me you know show up my house i mean i've had you know
[1964.54 --> 1969.46]  yes yeah giddup collaborators show up my house right and like you don't hear about that on the internet
[1969.46 --> 1975.44]  until just now right like and that's like in a bed we're in a good way uh good way like hey can we
[1975.44 --> 1980.02]  hack sure okay come on in well yeah like so i don't want to get into too much detail right but like
[1980.02 --> 1987.46]  the the point is that there is this baseline um i am willing to do private conversations for that
[1987.46 --> 1994.06]  kind of stuff that kind of really sensitive stuff um then you know then there's this middle ground which
[1994.06 --> 2000.16]  is like like the kind of stuff that uh you know you and i are talking about right like you know
[2000.16 --> 2007.04]  projects would be fun to do together you know your uh you know your own relationships with privacy on
[2007.04 --> 2010.82]  the internet that you negotiate for yourself is is different than mine like you've got the setting
[2010.82 --> 2016.70]  you know you've got the dial tuned to a different place than i do um you know but it's it's not like
[2016.70 --> 2020.64]  you're in danger it's not like you're like chad somebody's coming after me on giddup and i i need your
[2020.64 --> 2028.42]  help right um you know so in that case yeah man i'm i'm a little sad about it but it's you know
[2028.42 --> 2033.78]  it's an opportunity cause i'm sorry man so like release early release often he's not gonna budge
[2033.78 --> 2039.48]  i know right but that like that's the hard thing is like i love you right like i want to work together
[2039.48 --> 2043.96]  with with you and with everyone else and you know this is this is what i'm bringing to the table you
[2043.96 --> 2049.36]  know it's like uh it you know the reason i'm doing it this way like you know i've got my reasons for
[2049.36 --> 2053.14]  doing it this way just like you have your reasons for doing it that way so it i don't know i guess i
[2053.14 --> 2056.58]  guess at the end of the day there's an agree to disagree you know and i and i can respect that
[2056.58 --> 2060.10]  that's that's where i was like you know what i don't want to i could have responded and said no
[2060.10 --> 2065.08]  you're a jerk come on let's just talk offline but i didn't want to force you because i know what
[2065.08 --> 2068.44]  you're trying to do i know your mission with get up and i know where your heart's at so i didn't
[2068.44 --> 2073.28]  i didn't want to question why you were doing it i figured uh yeah you know we can delay the
[2073.28 --> 2079.06]  conversation potentially and you know no harm no foul i'm not upset with you i just wanted to point that out that
[2079.06 --> 2083.82]  you know you've got direct users of get up that have an issue with uh to some degree with you know
[2083.82 --> 2087.12]  from a security standpoint like you mentioned then you have someone like me who's you know maybe from
[2087.12 --> 2091.00]  a business standpoint or maybe from just a community standpoint how can we work together and i don't
[2091.00 --> 2094.88]  want to air out the laundry like right away i wouldn't mind obviously making everything open we're
[2094.88 --> 2101.08]  about open source and this yeah this show goes on air once a week and this one in particular live so
[2101.08 --> 2105.34]  we have no problem with what we say going out to the internet and being documented forever
[2105.34 --> 2111.04]  right right right yeah so one of the things we've discovered is that the real world is kind of a
[2111.04 --> 2117.26]  pain in the ass for open companies you know because it's like unless everybody's wearing google glass
[2117.26 --> 2123.72]  you know how are you going to record your your meeting that's face to face right um it's i don't know so
[2123.72 --> 2131.04]  but at the same time that that that scopes it or there's you know there's only so much real life
[2131.04 --> 2136.64]  interaction that you can do and that provides i don't know like if you and i run into each other
[2136.64 --> 2141.64]  at a conference or something we end up going out for drinks or you know going out and talking like
[2141.64 --> 2149.02]  that's great that's perfect right um i'm not you know i don't not go to conferences because they're
[2149.02 --> 2153.94]  not broadcast live on the internet you know the whole time i'm there right your preference is reality
[2153.94 --> 2161.98]  tv and if not if it's not available then no problem well i i've sort of i like the balance
[2161.98 --> 2168.50]  right i don't you know kind of what i've come to is like i'm not going to be able to make any
[2168.50 --> 2175.64]  decisions about stuff um you know in a in an offline face-to-face conversation right um you know
[2175.64 --> 2179.28]  that that's part of what it comes down to is like anything that's actually going to move the needle on
[2179.28 --> 2183.46]  get it anything that's actually going to be a decision that we make like i might have a conversation
[2183.46 --> 2189.10]  with you about it privately um but if it's actually going to manifest as something real on the internet
[2189.10 --> 2193.80]  on giddip then it's going to have to go through the public vetting process in a github issue or
[2193.80 --> 2201.06]  whatever you know what i mean so it's kind of yeah i don't know i see a distinction there between
[2201.06 --> 2206.66]  the interpersonal level where it's like i can only interact with so many people in a day because i'm like
[2206.66 --> 2212.60]  a you know a bony gut bag that like walks around in meat space right and like that that puts its own
[2212.60 --> 2218.52]  limits on what you can accomplish in gut bag space and that's uh that's appropriate right
[2218.52 --> 2222.48]  you know because phenomenologically like i am a person i want to interact with other people
[2222.48 --> 2227.52]  um you know and the the internet's this sort of weird ether where you can interact with you know
[2227.52 --> 2234.74]  a billion people very tenuously um and and kind of both of those together are are part of uh or i
[2234.74 --> 2238.88]  don't know or they're both part of the equation for me you know and i don't know this is where it
[2238.88 --> 2243.86]  gets more nuanced right it's like it's not it's not a it's not a simple open companies everything
[2243.86 --> 2249.58]  has to be open transparency radical transparency like i don't know yeah i don't know this is where
[2249.58 --> 2254.40]  it gets more interesting right right and it's so the i think we've been on this particular topic for a
[2254.40 --> 2258.80]  bit and it's not not in a bad way but it's it's so the reason i think it's really important is because
[2258.80 --> 2263.26]  it's at the heart of you and you're at the heart of giddip so it's at the heart of your story so
[2263.26 --> 2268.74]  anyone who's listening to this knows that you're to some degree radically transparent you have a
[2268.74 --> 2272.74]  open company initiative you're leading the charge in some way in some ways you're in uncharted
[2272.74 --> 2277.90]  territories i mean in many many ways right this is brand new i think you had absolutely open
[2277.90 --> 2283.14]  company.biz which now redirects to some other domain that is the i think so the ideas evolved
[2283.14 --> 2289.04]  to opencompany.org and i think you've even merged some relationships and and whatnot so
[2289.04 --> 2295.48]  yeah so we launched this open company initiative uh with balance payments and a couple others and
[2295.48 --> 2300.56]  and it's it's small and we're just kind of you know seeing where it goes but the idea is let's
[2300.56 --> 2306.04]  get together companies that are interested in these kind of themes and uh you know and just talk to one
[2306.04 --> 2311.00]  another and and share experience and whatnot so it's manifesting as an annual looks like it's going
[2311.00 --> 2315.78]  to manifest as an annual event uh you know we did it a couple months ago in in san francisco and
[2315.78 --> 2321.78]  we'll probably do it again next year um yeah it's a pretty light touch there but yeah so there's
[2321.78 --> 2326.10]  there's two you have two kind of tenants of an open company the second of which which you said is
[2326.10 --> 2331.06]  charge as little as possible and i guess that is the one that that to me doesn't seem as so much as
[2331.06 --> 2337.08]  open in the sense of transparency right maybe it's open in a different way can you speak to why that's
[2337.08 --> 2341.80]  you know number two on the list of things a company should do yeah so one of the things uh we've
[2341.80 --> 2347.88]  been saying in the open company conversations is transparency is sharing information and openness
[2347.88 --> 2358.50]  is sharing control okay so so when i publish um you know when buffer publishes their salaries
[2358.50 --> 2367.02]  publicly that's sharing information that's transparency right right when i open up my issue tracker
[2367.02 --> 2372.84]  uh you know to your feedback and you can come and create issues on my issue tracker like balance
[2372.84 --> 2378.96]  does with their dashboard for example right that's sharing control that's letting users uh you know
[2378.96 --> 2383.54]  yeah in some ways this is stuff that's done you know with like user voice and get satisfaction
[2383.54 --> 2389.68]  whatever that kind of stuff too right but sharing control and so for me the um the charge as little
[2389.68 --> 2394.66]  as possible thing is part of sharing control because really you know from that initial blog post like
[2394.66 --> 2399.02]  year and a half ago or two years ago or whatever when i put out the initial blog post get up as an
[2399.02 --> 2403.78]  open company i said it was three things share as much as possible charge as little as possible and
[2403.78 --> 2408.78]  don't compensate employees so that's kind of it's evolving and we haven't you know come up with a
[2408.78 --> 2416.14]  really clear articulation of uh of how it's evolved but um but but basically the idea around money is like
[2416.14 --> 2424.38]  i'm even giving i'm giving the users control over my money too right it's like not only not only can you
[2424.38 --> 2427.90]  determine which way the product is going but you're going to determine how much money you make
[2427.90 --> 2431.72]  from it worth to yeah exactly you're gonna determine how much it's worth you you're making
[2431.72 --> 2437.16]  your full living on get up right pretty much man yeah so that that was like that was part of this
[2437.16 --> 2442.30]  two-year window is like all right is get up going to reach the bottom rung of sustainability
[2442.30 --> 2450.12]  within two years you know so my runway is about done um you know the the good news is we do have
[2450.12 --> 2455.88]  ash dryden who's you know up to like 800 bucks a week now and you know advertises on her profile that
[2455.88 --> 2463.48]  she's 95 like 95 percent of her income comes from get up so clear answer yes you can make a living on
[2463.48 --> 2470.12]  get it no questions asked done ash is doing it um there's other people that are that are trying as
[2470.12 --> 2477.00]  well you know obviously not as successfully as ash um yeah i i pull what four or five hundred bucks a
[2477.00 --> 2482.52]  week from it between what's given to me personally what i take from the get up team um which is almost
[2482.52 --> 2486.56]  enough it's not quite i was gonna say you have four kids and a wife i have four kids and a wife and a
[2486.56 --> 2493.10]  mortgage yes i've been burned down so i've been living off of uh get up and savings and welfare uh for
[2493.10 --> 2499.34]  the past couple years and the the savings are about done and uh yeah so we're i we still have a week or
[2499.34 --> 2503.90]  two to figure out a week or two what happens are you being serious with a week or two or you are you is
[2503.90 --> 2508.64]  that a joke oh no no no that's that's not well i was saying a week or two to that one year that
[2508.64 --> 2513.58]  june 1st two-year deadline but uh yeah that's that's definitely a conversation i'm having with
[2513.58 --> 2517.86]  my wife right now is all right you know i you know the one question is do i still want to work
[2517.86 --> 2523.44]  on get up and the answer is yes right like i believe in this i think it's going well um and you
[2523.44 --> 2527.30]  know the second question is all right how do we make that work for you know for the next few years
[2527.30 --> 2533.16]  uh and you know so we're sorting that out we we listed our house on airbnb so i've got a you know
[2533.16 --> 2538.50]  our first visitor is showing up tonight and so but but then i but then i'm like all right but i want
[2538.50 --> 2543.16]  to do pay what you want i don't want to you know if i'm gonna get some money from outside of gidip
[2543.16 --> 2548.78]  i don't want it to you know like i don't want to charge people anymore for stuff that this is i just
[2548.78 --> 2554.94]  wrote uh an exposition of our mission statement which is on the building gidip website there's so many
[2554.94 --> 2559.30]  things to catch you guys up yeah so these are topics we want to hit so don't don't i mean i
[2559.30 --> 2563.98]  want to i wanted to pause us for one second before we go there if you don't mind absolutely um two
[2563.98 --> 2570.36]  years ago when july 12 2012 when you first launched gidip you read a post i believe in gidip and in there
[2570.36 --> 2575.40]  you said you know you said lots of stuff obviously but one of the key things i pulled out to to earmark
[2575.40 --> 2579.62]  for the show is just to kind of just put some truth there and some fact and this is a good time to
[2579.62 --> 2586.90]  mention that is your goal at the time was 2000 a week you're at just under 500 a week and we're
[2586.90 --> 2591.60]  obviously having this conversation so everyone's kind of caught up but you know you know that was a
[2591.60 --> 2598.82]  goal of yours and you're kind of you're you know you're 25 there but by this time next year so when
[2598.82 --> 2606.10]  did i post this july 12 2012 yeah so i didn't hit that july 12 2013 we're coming up on july 2014
[2606.10 --> 2616.42]  um right so one of the things we've learned is that gidip is a market for caring what i mean by that
[2616.42 --> 2627.16]  is you know i was making whatever at my old job but i had to do my old job you know and so the question
[2627.16 --> 2634.68]  is how much would the internet have to pay you to quit your job and just not do anything like do
[2634.68 --> 2642.18]  whatever you wanted right like is it 50 of what you were making before is it 80 of what you were
[2642.18 --> 2647.82]  making before you know like what's the difference between your salary now and what the rest of us
[2647.82 --> 2654.48]  would need to pay you to just quit your job and do whatever you wanted right be unfettered so for me
[2654.48 --> 2662.86]  that's turned out to be a fairly high percentage you know like about 80 percent um you know i'm making
[2662.86 --> 2669.32]  20 of what i was making at my old job roughly speaking and i love it like i wouldn't go back
[2669.32 --> 2676.30]  you know so that two thousand dollar figure i put out uh two years ago that was i was actually still
[2676.30 --> 2681.30]  i think i was still employed i think i i finished up at that job at the end of july um so i was still
[2681.30 --> 2685.42]  employed at that old job and that's that was i was driving that number you know but then the question
[2685.42 --> 2690.26]  has become like what's it worth to me you know what's it worth to me to not to have that no strings
[2690.26 --> 2695.00]  attached i could wake up in the morning and work on stuff because i want to work on it and not
[2695.00 --> 2699.06]  because i'm chasing a paycheck because there's there's value in that too i mean let's pause there
[2699.06 --> 2704.88]  for a second because you can make an income and be strapped to a job and be not fruitful for your
[2704.88 --> 2709.26]  family not fruitful for the you know the internet or the rest of the world however you want to pitch
[2709.26 --> 2716.18]  that and but there's some extreme flexibility there's some extreme um freedom in the lifestyle
[2716.18 --> 2722.08]  you've chosen that is separated from money and i think you know from a first world country
[2722.08 --> 2727.10]  standpoint there's many many listeners to the changelog third world countries uh first world
[2727.10 --> 2731.48]  countries with many different hardships that i can't even imagine but i'm in a privileged lifestyle
[2731.48 --> 2737.76]  and this is how it is but they don't always pin back to just money you know our economy in this world
[2737.76 --> 2744.10]  we all interact around money and that's what we sometimes derive value from identity from
[2744.10 --> 2748.98]  and you've chosen a different lifestyle that has some freedom in it that maybe you don't make as
[2748.98 --> 2753.30]  much money which is what the rest of the world thinks is value and we need to make your lifestyle
[2753.30 --> 2758.46]  but you've chosen a different path yeah that's that's true man and that's that's that's what i
[2758.46 --> 2761.88]  mean that's what it's a market for right it's like that's the question get it puts to you is like
[2761.88 --> 2765.48]  what would we have to pay you or the rest of us have to pay you would we have to pay you the
[2765.48 --> 2769.04]  two hundred thousand dollars you're making right now at your you know at your silicon valley
[2769.04 --> 2774.80]  you know job or you know or could we pay you fifty thousand and you'd you know you'd be happy and
[2774.80 --> 2781.00]  and productive whatever yeah it's so yeah that's that that's how that's evolved so i'm no longer
[2781.00 --> 2785.88]  expecting two thousand dollars a week from get it well i just the reason why i wanted to put up there
[2785.88 --> 2792.62]  is because you're a dreamer right and that that was that was probably a goal but it was a wish
[2792.62 --> 2797.62]  and and now we're at some reality and you're making some serious choices for your family as
[2797.62 --> 2801.86]  well as for get up so i just wanted to absolutely put that uh that out there to see what your thoughts
[2801.86 --> 2808.00]  are on you know to reflect back on what your wishes and dreams were originally yeah yeah absolutely i
[2808.00 --> 2812.36]  mean so you know so we're asking those questions right now we're trying to figure out you know it's
[2812.36 --> 2815.98]  it's hard to lower expenses from where we're at right now you know so we're trying to figure out how
[2815.98 --> 2822.38]  to up the income um you know so we my wife's been working uh the past couple couple months uh
[2822.38 --> 2828.86]  you know just doing stuff for a friend nothing long term but maybe you know maybe maybe she needs
[2828.86 --> 2833.62]  to get a job in the fall when the kids go back to school you know our kids are starting to get older
[2833.62 --> 2839.36]  i mean this is all this is all this is all the personal stuff that uh i don't usually talk about
[2839.36 --> 2845.68]  on twitter constantly but you know i'm happy to to discuss it um you know like i said we're we
[2845.68 --> 2849.78]  we're renting out rooms on airbnb okay so the thing i wanted to say about that is that
[2849.78 --> 2855.52]  i have the rooms listed at the airbnb minimum and i'm saying pay what you want right so like
[2855.52 --> 2866.32]  i'm still i'm looking for ways another thing that gidip has gotten into or as has evolved into
[2866.32 --> 2872.76]  is this idea of the pay what you want model right humble bundle is really good at it um you know
[2872.76 --> 2878.82]  they've kind of proven that it can work uh and there's definitely you know there's there's people
[2878.82 --> 2883.10]  studying it right like this is a this is a thing panera has tried opening a few pay what you want
[2883.10 --> 2887.12]  stores so they're experimenting with it so i think pay what you want is a real thing that's going to
[2887.12 --> 2895.16]  happen um you know gidip with individuals is very much patronage right so i kind of think of gidip
[2895.16 --> 2901.92]  as being segmented into individuals and then companies groups uh you know organizations whatever like
[2901.92 --> 2907.68]  that's two two segments so for individuals it's patronage you know i love you i love what you're
[2907.68 --> 2911.20]  doing take this money and run with it you don't need you know you don't need to know it's from me
[2911.20 --> 2919.02]  it's anonymous go um but then you've got like the gidip team or you know these hackerspaces like sudo room
[2919.02 --> 2925.06]  that are using it now or model model view culture shanley's uh publication you know there there's these
[2925.06 --> 2930.42]  teams there's these aggregations that are using gidip and they're i don't know i think we're gonna end up
[2930.42 --> 2936.12]  seeing that a that evolves uh you know it evolves into something a little different than the patronage
[2936.12 --> 2942.72]  model is with individuals you know um even the open company org you know the open company initiative
[2942.72 --> 2947.80]  you know if we want to fund that on gidip well it'd be nice to know who the people are that are giving
[2947.80 --> 2951.08]  money to the open company initiative you know because then you can call them your members right
[2951.08 --> 2956.08]  um so we might need to relax some of those constraints around you know who can see who's giving
[2956.08 --> 2962.42]  what to whom um but then also i think we want to find ways to use gidip to support a pay what you
[2962.42 --> 2972.02]  want model shields shields io the little read me badges um i ended up uh acquiring did we talk did
[2972.02 --> 2976.86]  this happen last time no but i acquired the shields yeah you acquired i was wondering it was her i didn't
[2976.86 --> 2981.38]  pay attention to the finer details but i know that you had some kind of batch this goes back to what
[2981.38 --> 2985.38]  you said a little bit earlier in the show where you kind of had some maybe some to some degree
[2985.38 --> 2989.70]  private conversations and then you had an open call about the merge and i think you even did like
[2989.70 --> 2999.10]  a fist bump virtually right yes yes yes yeah olivia and i we met at waza uh last year at heroku's
[2999.10 --> 3005.70]  developer conference uh at the beginning of 2013 and didn't really you know i found out that he was
[3005.70 --> 3010.78]  working on shield but we didn't really have any conversation about it but then people wanted it for
[3010.78 --> 3016.90]  gidip you know people wanted a little gidip badge to put on their readmes um you know and shields
[3016.90 --> 3022.86]  shields at that point was just some photoshop files and a design spec uh there was nothing dynamic there
[3022.86 --> 3029.28]  was no server uh server implementation no server api no web api forward or anything and get it for our
[3029.28 --> 3033.82]  implementation we needed something dynamic because we don't have just three states of badges you know
[3033.82 --> 3038.60]  pass fail build pass fail kind of thing we wanted it to be more complex we wanted it to be dynamic so i
[3038.60 --> 3044.46]  ended up getting involved in writing an implementation of that uh and then finding out i don't know it was
[3044.46 --> 3051.10]  it was interesting because it was an exercise in cat herding you know what's what's an easier project
[3051.10 --> 3057.50]  what's an easier weekend project than hacking together an api server for readme badges you know i mean
[3057.50 --> 3062.72]  it's like you know it's something that you know any of us could do in an afternoon pretty much and so
[3062.72 --> 3068.64]  a lot of us did and so we ended up with all these different uh implementations cropping up
[3068.64 --> 3076.72]  and the the genius thing we found to do and it was nathan youngman i think his name is uh nathan uh
[3076.72 --> 3086.92]  he's he's up in canada and his uh he's he's a go hacker and whatnot and somehow we had the org
[3086.92 --> 3092.76]  badges the github org named badges one of the you know somebody had somebody had grabbed this
[3092.76 --> 3099.80]  and nathan talked to this fella and agreed this fella agreed to let us use this badges organization
[3099.80 --> 3104.78]  and we just started gathering all of the different repos you know so i think we have like 10 or 12 in
[3104.78 --> 3110.92]  there now if you go to github org slash badges let's see what's on there now um you know one two
[3110.92 --> 3118.28]  three four six yeah so there's like over a dozen of these uh repos a lot of them duplicated effort
[3118.28 --> 3125.80]  you know but uh when we the pattern was we brought somebody in and we didn't take control of their
[3125.80 --> 3130.32]  project because of course the permissions don't change on any of those right like it's just now
[3130.32 --> 3135.22]  it's under the badges repo you know badges uh you know org instead of your personal github account
[3135.22 --> 3138.74]  but it's still yours and you're still in charge of it you're still running it however you want
[3138.74 --> 3145.22]  you know but it's shown to be part of this bigger effort and that really was a key step in bringing
[3145.22 --> 3151.02]  everyone to the table and then saying all right here's the range of possibilities you know who
[3151.02 --> 3155.24]  actually has the energy to do this and which way you know and what's you know now that we've seen what
[3155.24 --> 3159.00]  all the possibilities for implementing this are like what's going to be our way forward and it's been
[3159.00 --> 3166.98]  a success as far as that goes um you know there's a fella espadrine is his um is his github handle um
[3166.98 --> 3171.24]  and he's running with it so he's the day-to-day maintainer uh you know he wrote the current
[3171.24 --> 3176.28]  implementations and node implementation and he runs and maintains that project um you know but it
[3176.28 --> 3181.50]  had an input from uh the rest of the community and kind of i don't know it was interesting i had never
[3181.50 --> 3186.32]  had an experience before like that and and you know i want to hear i mean have you do you have other
[3186.32 --> 3189.80]  examples of when that kind of thing has happened because i thought it was pretty remarkable just the
[3189.80 --> 3195.02]  way that we brought together lots of different effort and it's kind of got it funneled in one direction
[3195.02 --> 3202.16]  like do you know of other uh other projects that have evolved like that nothing that come to mind
[3202.16 --> 3208.24]  for me you know i was just thinking yeah you know me neither you you guys are the open source uh you
[3208.24 --> 3212.22]  know you've got the the lay of the land in front of you uh i don't know i thought i thought it was
[3212.22 --> 3215.52]  really interesting we're keeping up just like everybody else i mean there's there's i was actually
[3215.52 --> 3220.50]  just talking to a listener yesterday daniel i was on and he's uh from ottawa canada and he
[3220.50 --> 3225.66]  told me about famous this javascript front-end framework that's making you know interfaces
[3225.66 --> 3228.46]  easier and i'm like dude i didn't even know about that and he's like i thought you would have known
[3228.46 --> 3233.50]  about it because you know i'm like we literally are just keeping up just like you no we just happen
[3233.50 --> 3238.82]  to be a part of making sure everyone's kept up for lack of better terms yeah blogging about it yeah
[3238.82 --> 3244.90]  podcasting um let's pause the show for just a minute give a shout out to our sponsors top towel
[3244.90 --> 3249.56]  uh we've been working with top top for quite a while and i'm thrilled about this relationship i
[3249.56 --> 3256.10]  think they have one of the most coolest most unique ways to basically connect businesses who need
[3256.10 --> 3262.94]  really awesome elite engineers and also connect really awesome elite engineers to companies who have
[3262.94 --> 3270.16]  awesome work to do so uh i mean that's the biggest uh biggest statement i can even give for them but
[3270.16 --> 3274.56]  we thought it would make sense to take some time to circle back and talk to some of our listeners
[3274.56 --> 3279.88]  who have applied to top towel and have been accepted because only about two to three percent of the
[3279.88 --> 3286.52]  engineers who apply actually make it past their strict elite engineering process uh because they
[3286.52 --> 3293.08]  want the best simply that so daniel lauzon a longtime fan and listener of the changelog is now living the
[3293.08 --> 3298.76]  dream as an elite engineer at top towel and i say living the dream because he's now able to have
[3298.76 --> 3304.50]  100 control of the types of projects and technology he's working on as well as the rate he wants
[3304.50 --> 3311.46]  to charge so daniel earns 100 of his income as a top towel engineer and wanted me to pass on his
[3311.46 --> 3317.12]  seal of approval so to speak of the top towel experience and for those of you out there who are
[3317.12 --> 3323.50]  freelancing or would like to test out freelancing or try out a no risk freelance like project while
[3323.50 --> 3327.18]  you maintain your full-time position to kind of mitigate that risk you can you got to check out
[3327.18 --> 3334.00]  top towel t-o-p-t-a-l.com if you think you have what it takes head to top towel.com slash developers
[3334.00 --> 3342.02]  to get started and tell them the changelog sent you um right so the you know shield relates to get it
[3342.02 --> 3347.66]  in that the idea was let's fund this on get it you know this is going to take some amount of effort
[3347.66 --> 3351.18]  going forward so let's figure out a pay what you want model right so like everybody's got these get up
[3351.18 --> 3358.12]  you know these github read me badges they're all over the place every developer uses them you know
[3358.12 --> 3363.18]  what if everyone who used one of these chipped 10 cents a week in to the maintenance of the service
[3363.18 --> 3370.16]  that's behind it right as one uh user uh you know segment and then the other is the vendors such as
[3370.16 --> 3376.92]  travis and coveralls and etc etc the ones that are actually uh you know providing the the badges the
[3376.92 --> 3381.34]  services the badges relate to you know maybe they chip in 100 bucks a week or something you know
[3381.34 --> 3384.58]  what i mean so it's like you've got the the companies coming together and giving you've got
[3384.58 --> 3390.44]  the users coming together and giving a lot a little and uh and then you know we've got this funded so
[3390.44 --> 3394.46]  now asperdrine is freed up to work on this and make it even better and maybe we can bring some
[3394.46 --> 3400.82]  other people to the mix and make it happen even faster uh so that that we haven't gotten over the
[3400.82 --> 3405.12]  hump on yet i haven't i haven't really put a lot of effort into that just because i've been
[3405.12 --> 3407.88]  traveling and doing other stuff and that hasn't been a priority for me but it's kind of on the
[3407.88 --> 3413.08]  back of my mind you know so now that we've kind of settled the technology side of it like let's
[3413.08 --> 3418.92]  figure out the funding side of it um but that i don't know so that gets into a couple other things
[3418.92 --> 3424.12]  let me frame this by saying and we're we're at 11 53 how long are we going today we're i'm gonna
[3424.12 --> 3427.92]  think we're gonna skip the final questions besides the call to arms so we're gonna skip the normal
[3427.92 --> 3432.76]  questions we do which takes about 15 minutes so we let's let's say another 12 minutes is that cool for
[3432.76 --> 3443.88]  you jared okay yep okay um right so what i've been learning i think one of the themes is over the
[3443.88 --> 3450.92]  past two years i come out of the open source world i come you know come at this with an open source
[3450.92 --> 3459.72]  mindset and that's a very definite culture right building a company and building a product means
[3459.72 --> 3470.06]  integrating and working with people coming from much different cultures right so for example visual
[3470.06 --> 3479.00]  designers right um related to open source related to development but it's kind of its own thing you
[3479.00 --> 3486.76]  know so i've you know i've been on this uh effort this year to try and bring design into gidip right to
[3486.76 --> 3491.64]  try and uh breathe with both lungs is how we've been thinking about it you know like so we can
[3491.64 --> 3496.74]  we can really deliver a world-class product it's been challenging to interface with designers and to
[3496.74 --> 3503.78]  figure out how do designers fit in an open source culture that's been a challenge you know um same
[3503.78 --> 3509.28]  thing same thing with journalists you know how how does this open model uh relate to journalism
[3509.28 --> 3517.42]  we actually on the open company initiative uh uh we we did an experiment where we tried to bring in
[3517.42 --> 3524.94]  journalists so we had um a woman named bronwyn clune who's a uh columnist for the guardian and we're
[3524.94 --> 3529.86]  like all right let's try this experiment where you're writing content for us um but somehow you know
[3529.86 --> 3535.84]  it's it's funded through gidip and so you know it was this little experiment in open journalism or
[3535.84 --> 3542.92]  whatever right um didn't really go anywhere and and part of that was um you know i i saw it as kind
[3542.92 --> 3548.88]  of a culture clash right like the culture of journalism is not uh you know it's not the culture
[3548.88 --> 3556.98]  of open source necessarily that's two number three is um you know shanley and you know everything we're
[3556.98 --> 3564.46]  hearing about last night not necessarily a fit with the open source culture i come from um you know
[3564.46 --> 3569.38]  perhaps corrective to it in some ways and then a fourth one that i'll bring up is investors
[3569.38 --> 3574.56]  this is tying you know so tying together a few themes here uh
[3574.56 --> 3583.18]  we started talking very early two years ago uh had a conversation with um andy weissman who's from
[3583.18 --> 3590.30]  union square ventures we had a long conversation pretty early after uh gidip launched where do
[3590.30 --> 3596.14]  investors fit right if gidip is funded on gidip we'd charge as little as possible uh you know we
[3596.14 --> 3602.36]  don't compensate our employees like what what's the role of the investor in this new uh you know this
[3602.36 --> 3607.92]  this trail that we're blazing didn't have an answer uh for a couple years and then actually when i heard
[3607.92 --> 3614.02]  from jason whenever it was last week i guess maybe it wasn't this week last week it occurred to me that
[3614.02 --> 3618.62]  now our teams feature which i forget i don't know we were maybe just launching it a year ago but
[3618.62 --> 3623.20]  we've got this teams feature now which is a whole nother thing and we'll have to talk about that next
[3623.20 --> 3626.76]  year because it's too big for now but it's it's awesome it's actually one of the most important
[3626.76 --> 3631.56]  things we're doing on gidip because it's how we say um you know it's not just about being a rock star
[3631.56 --> 3636.34]  with you know 20 000 twitter followers that's not the only way to make money on gidip you know you can
[3636.34 --> 3641.68]  be somebody who just does really good work and is you know um you know behind the scenes you can join
[3641.68 --> 3649.70]  a team and the team is pulling the money in on the pay what you want model right and then you know and
[3649.70 --> 3656.26]  you get a part of that um so you know because we've got that teams feature now we may have a way to
[3656.26 --> 3660.16]  you know to bring investors into it but then you're getting you know then it's then it's business
[3660.16 --> 3664.46]  i don't know then you're talking about marketing again right it's like how do you bring marketing
[3664.46 --> 3667.66]  into this how do you how do you i mean that's where we're at with shield it's like so now we need
[3667.66 --> 3672.30]  the marketer to come in and say here's the website we're going to build you know and and and drive
[3672.30 --> 3678.32]  that end of it the business side of it um which just i don't know yes we've so i feel like all of
[3678.32 --> 3685.04]  these roles that we're used to uh you know all these roles that we already have have uh have some
[3685.04 --> 3691.44]  future in this uh you know thing that we're discovering together right um and i don't know exactly
[3691.44 --> 3697.64]  what those look like yet but we're having a lot of fun finding out as we go
[3697.64 --> 3706.50]  you seem to be every new hurdle you get past or every new um i guess roadblock blocker uh you
[3706.50 --> 3712.08]  find a new one you know from the like you know all these it just seemed like each new challenge gets
[3712.08 --> 3718.64]  uh you know has another challenge right behind it and i don't want to be discouraging what to say
[3718.64 --> 3724.32]  this but i i sometimes wonder in myself how much more steam you particularly have left in your engine
[3724.32 --> 3731.68]  because you're 80 of the fuel behind getup you know yeah i have a lot of steam man i have tons of
[3731.68 --> 3736.98]  steam what i need is a little more money you know if i had you know if we can figure out how to get an
[3736.98 --> 3742.74]  angel investor in here and you know give us a little breathing room yeah i don't know maybe like one of
[3742.74 --> 3748.26]  our guys working on the team moved to nicaragua so he he quit his job and moved to nicaragua so he
[3748.26 --> 3753.00]  could lower his burn rate and you know work on get it full time that's commitment right there that's
[3753.00 --> 3757.96]  for sure yeah right that's humbling that's like so it isn't just chatted yeah like that's the exciting
[3757.96 --> 3762.88]  thing it's like we do have people i'm not the only one working on full time in fact we're supposed to
[3762.88 --> 3768.00]  have a stand-up in a couple minutes here right with with the team so it's not um the good news is
[3768.00 --> 3774.30]  it's not just chad um we do have a team i have people handling support you know frontline support
[3774.30 --> 3777.90]  and then they escalate to me if we need to so so the pieces are coming together it's just
[3777.90 --> 3782.74]  you know it's it's chicken and egg and we're boiling the ocean and that just takes a little
[3782.74 --> 3788.32]  longer than usual you know let me ask you a quick yeah let me ask you this sure give me a moment to
[3788.32 --> 3792.76]  set this up because it might be kind of just a long setup but uh are you familiar with patreon
[3792.76 --> 3798.22]  which seems to be oh my gosh i was just about to bring patreon into this and i was like i don't need
[3798.22 --> 3802.68]  to do that but uh okay yeah let's go there let's go there okay i'm gonna go there briefly um just
[3802.68 --> 3805.92]  because you know you're talking about the patronage model and i just remember there was another
[3805.92 --> 3810.82]  website doing patronage and i've been on their website kind of comparing contrasting patreon and
[3810.82 --> 3816.76]  get it yeah and they seem to have more steam they have uh you know a few bigger names in the arts
[3816.76 --> 3822.14]  especially in podcasting and kind of online media people making eleven thousand dollars a month
[3822.14 --> 3826.82]  via the patronage model right um and i'm trying to think to myself what's the difference between
[3826.82 --> 3830.32]  where you're at and i don't know their whole backstory maybe they're older i'm guessing they're not
[3830.32 --> 3834.80]  they're not they're younger funding they're they have funding so they're they're not setting the
[3834.80 --> 3839.88]  plows deep they're not funded on their own platform they skim off the top right so they're not setting
[3839.88 --> 3845.74]  the plows deep so they're you know it's not making it easier on themselves um well yeah another way to
[3845.74 --> 3850.78]  say that it would be another way to say it you know so you know their background is um you know jack
[3850.78 --> 3860.16]  conti we did a call jack and i and uh and uh and len kendall from sent up and lena's from uh from
[3860.16 --> 3865.28]  flatter we did a call the four of us uh it was like two weeks after patreon launched or something
[3865.28 --> 3869.84]  right so it was it maybe it hadn't even launched yet it was like really early in their cycle
[3869.84 --> 3877.34]  in their life cycle and uh i don't know right and then and ever since and i've been watching uh
[3877.34 --> 3881.42]  google trends you know i'll go to google trends and look at get up in patreon it's like all right
[3881.42 --> 3887.98]  so that's what a hockey stick looks like god damn it right and so i get so burned man it's like why
[3887.98 --> 3893.76]  why is that not us and and i get really discouraged when i look at it from that point of view right
[3893.76 --> 3896.28]  this is i think i mentioned this at the beginning of the call and this is what i had in mind right
[3896.28 --> 3900.22]  like i get really discouraged when i look at the google trend search for patreon and get it because
[3900.22 --> 3904.00]  patreon is hockey stick right and people are coming to me and being like hey do you know about
[3904.00 --> 3906.90]  patreon like my non-tech friends are like you know about patreon it's like yes i know
[3906.90 --> 3911.18]  yes i know right well i didn't yeah i didn't i didn't bring it up in order to do that to you
[3911.18 --> 3915.40]  well so look sorry but let me ask you yeah the other thing i noticed on their home page is like
[3915.40 --> 3919.06]  featured in tech crunch and i started thinking about your situation with yeah and then i asked
[3919.06 --> 3923.88]  that game man they're playing that myself they got two million dollars of capital right they took
[3923.88 --> 3928.00]  investment like the the they have two founders the one guy is jack who's the front man that everybody
[3928.00 --> 3933.18]  sees because he's the youtube star right so he's already plugged into this scene like youtube stars have
[3933.18 --> 3938.78]  fans open source programmers don't have fans you know so it's like he's already plugged into a scene
[3938.78 --> 3943.64]  and tapped into a market and like speaking the language of a culture of you know this crew that
[3943.64 --> 3949.78]  has fans and has reach beyond what i do right so that's what jack's bringing the table and his friend
[3949.78 --> 3954.76]  sam i think it is i don't remember but you know his co-founder is the technical co-founder who's a
[3954.76 --> 3960.30]  serial co-founder who's you know already had you know two previous companies that he's done they're in
[3960.30 --> 3963.78]  silicon valley they're in san francisco you know they're playing the game straight down the middle
[3963.78 --> 3968.64]  you know what i mean it's like you know and they're yes and so featured in tech crunch and wired and
[3968.64 --> 3974.42]  blah you know etc etc etc right like and this is what it looks like so i don't know so i kick myself
[3974.42 --> 3979.40]  because i'm like do i really i hit this a week or two ago i was like do i really believe in get up again
[3979.40 --> 3985.40]  you know like it's coming back is more is more uh i'm now hypothesizing that perhaps you know you would
[3985.40 --> 3988.78]  have been in tech crunch maybe you would have had an investment if it wasn't for the open strategy
[3988.78 --> 3994.86]  and so my question framing all this is yep is get up success more important or is your open
[3994.86 --> 4001.58]  uh the radical transparency more important to you chad good question i mean just oh boy it's really
[4001.58 --> 4005.68]  hard that that's what's holding it back it might not be what's holding it back but so so to me they're
[4005.68 --> 4013.18]  the same right like get up is it is open company you know like get it get it for me is um is this
[4013.18 --> 4020.22]  idea that i can wake up in the morning and i can give i can give um i can live out of a place of
[4020.22 --> 4027.22]  gratitude and generosity and i can give freely of my labor and my resources without asking anything
[4027.22 --> 4033.14]  in return right and that is not what patreon is building and so we're not even competitors when you
[4033.14 --> 4037.98]  look at it that way like so in my view it's like we're not even competitors you know like if if
[4037.98 --> 4041.80]  patreon wants to compete with me then they need to be funded on their own platform and it needs to
[4041.80 --> 4047.42]  be no strings attached gifts you know and then i'll just go you know work on their platform like
[4047.42 --> 4052.30]  i can't work on their platform they could come work on mine because i'm totally open i couldn't go work
[4052.30 --> 4057.12]  on their platform like i that's that's it's apples and oranges when i really get down to it you know
[4057.12 --> 4062.82]  so yeah i i don't separate there is the open company thing from from get it yeah that's where we're
[4062.82 --> 4068.60]  going i don't know yeah who knows maybe a year from now i'll just be well so this is what we need to
[4068.60 --> 4073.32]  get uh so what would what would i have done instead of we'll do these quickly what would i have done
[4073.32 --> 4080.48]  instead of gidip what would i be doing if i wasn't doing gidip yeah oh man i was so ready to just
[4080.48 --> 4088.96]  give up on the internet and go move in with the amish um yesterday but we worked through that i would i
[4088.96 --> 4094.82]  would be amish if i could that's what i would do short answer there my hero is still guido van rossam
[4094.82 --> 4102.62]  the creator of pycon python and pycon i guess by extension um i i got to actually with kenneth um
[4102.62 --> 4107.64]  i texted kenneth uh i hadn't seen him you know hadn't really sat down with him for for a couple
[4107.64 --> 4111.98]  conferences and i said kenneth let's get together for supper he said okay cool let me see if that
[4111.98 --> 4118.98]  works out with the other folks i'm with and it ended up being me and kenneth and uh and and mike and
[4118.98 --> 4125.30]  maddie from ottawa and guido the five of us went out to dinner together right and so nice i ended up
[4125.30 --> 4129.30]  like getting to have dinner with guido and it was like hi i'm chad i'm guido and so i got to actually
[4129.30 --> 4135.00]  meet him after a decade of doing python stuff which is pretty special so he's and he's still my hero i
[4135.00 --> 4141.26]  like that guy he's doing great call to action ha go fund somebody on patreon
[4141.26 --> 4152.80]  go go yeah you know go work for the go work for the the man the crowd man i don't know yeah yeah you
[4152.80 --> 4157.84]  know go go give your labor away but only in response you know only only because other people
[4157.84 --> 4163.62]  give you money for it don't give your stuff away for free that's not the future hold on don't share
[4163.62 --> 4168.72]  oh am i being bitter are we ending on a bitter yeah i was gonna say don't end like that be given
[4168.72 --> 4172.72]  honest call to arms i mean okay think about it like this you got a lot of listeners that are thinking
[4172.72 --> 4179.04]  i want to support get up i don't know how to do it how can i do it so this is where i'll bring in
[4179.04 --> 4186.94]  building get up we have a new site um called building.getup.com and that site is is new this year
[4186.94 --> 4192.82]  and it's our documentation site for our team for people working on get up right so you go there
[4192.82 --> 4196.34]  and it starts with a big picture it says here's what our mission is here's where we're going
[4196.34 --> 4202.00]  and then it zooms in and says here's the process we use here's our brand guidelines here's how we
[4202.00 --> 4205.94]  understand our audience and who we're working towards it answers all those big questions and
[4205.94 --> 4211.48]  then it hopefully gets you plugged in uh to the issue tracker and understanding how we work and
[4211.48 --> 4217.24]  get you into github and into irc so that is the place to start if you want to help us hack on get it
[4217.24 --> 4226.10]  and if you want to use get it then use get it get it.com uh for you know support think here's the
[4226.10 --> 4232.10]  question who inspires you who is the one person that you love what they're doing and you want to
[4232.10 --> 4238.36]  give them a quarter week go to get it.com and set that up now even though that funnel is pretty leaky
[4238.36 --> 4245.02]  but go do it anyway how about that you can also support get up directly on there as well as wit
[4245.02 --> 4251.42]  537 which apparently would also support get up directly i believe yeah if you like what we're doing
[4251.42 --> 4257.44]  we're there awesome but get up will work for me because it's working for everybody you know so
[4257.44 --> 4263.18]  do that there were uh i want to circle back with you maybe some other way i i feel like when we get
[4263.18 --> 4267.22]  to the end of these calls sometimes we don't get all the things and there was the some stuff with dhh
[4267.22 --> 4271.22]  and open source specific to listeners that are going to be close to their heart they're thinking like
[4271.22 --> 4277.42]  why don't you talk about his call with dhh and funding open source uh so i think while the dude i
[4277.42 --> 4282.04]  love that i love when you sit down and talk to somebody for 45 minutes they're a real person
[4282.04 --> 4287.44]  you know that was a cool conversation honestly i love that i think it's really powerful i'd love
[4287.44 --> 4290.90]  to see more of that i'll tell you what we'll do if you don't mind we'll we'll put a post on the
[4290.90 --> 4297.06]  change log uh with that video in it and i'd like to just maybe even do something different break our
[4297.06 --> 4301.74]  normal mode of like maybe do another follow-up call i mean who says you can't be on here twice in
[4301.74 --> 4304.68]  one year doesn't really matter to me i just want to have i think you're doing some pretty cool
[4304.68 --> 4309.46]  stuff and people need to know about it it's a long story short you know really and i i don't want
[4309.46 --> 4314.72]  you i mean almost is cool and all but don't go do that keep doing the get up thing well yeah everybody
[4314.72 --> 4320.34]  who's listening go to get up right now give to teams you love give to people you love um you know
[4320.34 --> 4324.34]  whether they're activists whether they're open source it doesn't matter figure out who's on there
[4324.34 --> 4328.14]  and if they're not on there get up has a way to bring them on there easily for you so go and
[4328.14 --> 4333.10]  figure out who inspires you and truly give and and maybe even become a receiver yourself
[4333.10 --> 4339.28]  and if you're a company go in there too and give yeah hopefully we'll make it easier we'll improve
[4339.28 --> 4344.40]  the product it'll be easier for everybody we'll do it together well you know chad i'd love to keep
[4344.40 --> 4348.56]  you on the show for as long as we we we love to kidnap you and just talk to you for for years on
[4348.56 --> 4354.72]  end honestly but um you know as much as we can be we want to be an encouragement to you we want to
[4354.72 --> 4361.10]  be encouragement to the contributors of get up um whatever we can to support you in the future now
[4361.10 --> 4365.80]  and and in the future let us know we'll be there for you we're we're uh brothers and sisters in
[4365.80 --> 4370.30]  arms so to speak so don't don't feel like you're an island you're not an island where we're we're the
[4370.30 --> 4376.42]  tree on your island so um before we close i want to give a little shout out to um our sponsors we got
[4376.42 --> 4382.36]  rack space code ship and uh top towel who support this show so thank you for their support and as a
[4382.36 --> 4387.52]  matter of fact all three of those are not only sponsors of the change law but they're also partners
[4387.52 --> 4391.52]  with the change logs that's that's really neat they they care about our long-term future so
[4391.52 --> 4396.80]  they've put roots in the change log and they care so that's uh that's super awesome and if you
[4396.80 --> 4402.86]  haven't yet we shoot out a weekly email it's been a little on a small hiatus but uh tune in you know
[4402.86 --> 4407.40]  because we got some some fun stuff coming up so the change all.com slash weekly to get updates
[4407.40 --> 4414.12]  on fresh and new open source in your email inbox every week uh chat again thank you so much for
[4414.12 --> 4418.50]  for coming and talking to me and jared it's been an absolute pleasure listeners thank you for
[4418.50 --> 4424.86]  listening tuning in live if you're tuning in live uh next week uh we're getting better at making sure
[4424.86 --> 4429.44]  our schedule is full so next week we have felix guys and over coming on the show talking about
[4429.44 --> 4436.66]  robotics uh node copter if you're into drones of any sort tune into this show it's going to be a blast
[4436.66 --> 4441.78]  but uh that's the topic uh for next week but until until then let's uh let's say goodbye
[4441.78 --> 4447.40]  uh very cool thanks for having me on the show you guys yep thanks for coming bye bye everyone
[4447.40 --> 4449.40]  you
[4471.78 --> 4479.40]  you
[4479.40 --> 4481.40]  you
[4481.40 --> 4483.40]  you
[4483.40 --> 4485.40]  you
[4485.40 --> 4487.40]  you
[4487.40 --> 4489.40]  you
[4489.40 --> 4491.40]  you
[4491.40 --> 4493.40]  you
