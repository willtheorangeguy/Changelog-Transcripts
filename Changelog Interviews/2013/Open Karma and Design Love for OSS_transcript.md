[0.00 --> 11.74]  welcome back everyone this is the changelog
[11.74 --> 15.76]  we're a member supported blog podcast and weekly email that covers fresh and what's new
[15.76 --> 20.94]  in open source check out the blog at the changelog.com our past shows at 5by5.tv
[20.94 --> 25.58]  slash changelog and subscribe to the changelog weekly it's our weekly email covering everything
[25.58 --> 29.62]  that hits our open source radar you do not want to miss it ships on saturday subscribe at the
[29.62 --> 34.90]  changelog.com slash weekly the show is hosted by myself adam stakovak as well as andrew thorpe
[34.90 --> 42.96]  andrew say hello yo yo what's going on this is a lucky episode 109 man 109 so today's show is
[42.96 --> 46.52]  sponsored by digital ocean and if you're not familiar with digital ocean they've been sponsoring
[46.52 --> 50.40]  the show for a little bit now we've partnered with them we love what they're doing they're doing some
[50.40 --> 54.76]  really awesome stuff for the community and we want to tell you about them pretty much every week
[54.76 --> 59.42]  because they got some really cool stuff happening but they're a simple cloud hosting provider dedicated
[59.42 --> 63.94]  to offering the most intuitive and easy way to spin up a cloud server you can create a cloud
[63.94 --> 70.76]  server in 55 seconds pricing plans are at five bucks per month and with that you get 512 of ram
[70.76 --> 77.62]  20 gigs of ssd drive space one cpu on one terabyte of transfer they have data center locations in
[77.62 --> 82.78]  amsterdam new york as well as san francisco and they recently celebrated something pretty cool which is
[82.78 --> 89.56]  600 000 that's right 600 000 cloud servers out there in the cloud and you can get started with
[89.56 --> 94.98]  digital ocean today for free using our promo code it's the changelog october which will give you a
[94.98 --> 99.38]  ten dollar hosting credit basically two months free spin up your cloud server today with digital
[99.38 --> 106.92]  ocean at digitalocean.com and without further ado we're joined today by justine ariche designer at
[106.92 --> 112.66]  travis sorry travis ci and sebastian gressel he's a freelance web developer and together
[112.66 --> 117.76]  they are the creators of open karma a tool to help bridge the gap between developers
[117.76 --> 126.60]  and designers welcome to the show guys hello so design in open source it's a problem right
[126.60 --> 132.66]  it's a huge problem uh i was unaware of it that it was even a problem until recently
[132.66 --> 137.56]  and i guess before we kick off the show officially justine why don't we start with you
[137.56 --> 142.60]  give a quick introduction to who you are and kind of what you do and sebastian follow up from her
[142.60 --> 150.40]  all right um so yeah i'm justine and i work for travis ci as their lead designer and basically
[150.40 --> 159.20]  what i do is i've worked in everything from print shops to consultancies and software and uh lately
[159.20 --> 164.88]  my big passion has been trying to get involved with open source projects which i found out quickly
[164.88 --> 170.80]  were lacking in design always looked terrible didn't function and pretty much needed as much design help
[170.80 --> 179.20]  as they could get and sebastian how about yourself hi i'm sebastian i'm working as a developer for
[179.20 --> 187.08]  almost uh eight years now and currently i'm freelancing doing some smaller projects for clients and
[187.08 --> 193.96]  trying to get money and also on the site working on open source projects and trying to contribute to
[193.96 --> 201.34]  as much as possible awesome so you guys kind of met somehow uh once you kind of give us a little bit
[201.34 --> 206.86]  of a introduction as to how you guys came about and and you decided to to start this who came up with
[206.86 --> 214.10]  the idea and where did it come from um sebastian and i met at your camp this year uh i was speaking and
[214.10 --> 220.10]  he was attending i met him the first night i got to berlin and we just kind of hit it off and hung out for
[220.10 --> 227.08]  pretty much the rest of the conference and just kind of uh palled around for a while and then a couple
[227.08 --> 233.36]  months ago i think it was maybe about two months ago i sent out a tweet saying that i was a designer
[233.36 --> 242.82]  and if you had an open source project that needed design love to ping me and um it is currently at 907
[242.82 --> 248.56]  retweets and i've gotten hundreds of emails from developers all over the world and that's kind of when
[248.56 --> 254.48]  i started talking to sebastian i was just like dude i cannot do all of this by myself and i feel really
[254.48 --> 261.56]  bad like i can't keep turning people down and so then i kind of got this idea that what if we made a
[261.56 --> 268.56]  service that would kind of pair up designers like myself that are qualified and want to work in an
[268.56 --> 274.70]  open source development atmosphere um what if we like found a way to put them together with
[274.70 --> 280.56]  open source projects and so we just kind of started brainstorming with that like sebastian would
[280.56 --> 286.06]  ping features off of me and i would kind of like say okay yeah that's good and like pretty much what
[286.06 --> 291.08]  we settled on for now at least is that as long as your open source project isn't making any money
[291.08 --> 297.12]  all of the design work will be free as well so it's kind of just a mutual helping of the community
[297.12 --> 302.46]  between you know designers that are willing to work for free as well as open source projects that
[302.46 --> 306.62]  aren't making any money and just need some tender love and care in the design department
[306.62 --> 312.82]  awesome so so essentially you notice like a glaring deficiency in the open source community open source
[312.82 --> 318.84]  while the open source code out there tends to be some of the most beautiful code that you can find
[318.84 --> 324.74]  most of the interfaces not most a lot of the interfaces you find um for the the projects that have an
[324.74 --> 330.58]  interface are are struggling pretty bad why do you think it is that you know you guys i don't know
[330.58 --> 334.12]  like what do you think that the open source community has not really been that welcoming
[334.12 --> 338.28]  to designers traditionally or what do you think the reason is behind that and why your tweet i mean
[338.28 --> 345.74]  just a little tweet got so much attention um i have a personal theory on it there's like two things
[345.74 --> 352.86]  behind it and it's one that a lot of developers don't know designers like i'm one of very few designers
[352.86 --> 359.76]  that ever go speak at conferences and so always those people try and like hit me up and say like
[359.76 --> 363.62]  hey maybe you could take a look at this and give me some suggestions and that's how i even got
[363.62 --> 368.56]  involved in travis i lost my passport in berlin i was stuck an extra couple days and ended up hanging
[368.56 --> 375.26]  out with josh and he just asked if i could put an extra pair of eyes on travis's ui and i said sure
[375.26 --> 380.36]  and that just kind of ended up being a full-time gig but i just don't think developers know a lot of
[380.36 --> 386.44]  designers and then also i know a lot of designers and they either have never worked in software or
[386.44 --> 391.68]  anything tech related other than coming up with like a fake mobile ui that's really just a photoshop
[391.68 --> 398.42]  mock or like a lot of designers selfishly like they just want to make money and so i don't think a lot
[398.42 --> 403.50]  of them are willing to put themselves out there for free but there can't just be me there has to be
[403.50 --> 409.16]  more designers willing to kind of lend a helping hand for the greater good of open source right so
[409.16 --> 414.10]  open karma is essentially going to be a tool that helps to connect the two right so developers and
[414.10 --> 418.92]  designers both will sign up for this service or you guys are still in just kind of gathering
[418.92 --> 422.84]  information and getting people excited but whenever this thing launches which we'll get into later
[422.84 --> 428.98]  um you'll you'll be able to basically just connect designers to developers you said that as long as
[428.98 --> 433.54]  the open source project is not making any money then the designers that are willing to do this will
[433.54 --> 438.76]  have to do it for free or you know according to open karma is is does that mean that you won't
[438.76 --> 445.62]  support like any exchange of funds or anything like that through open karma um well sebastian i
[445.62 --> 452.98]  talked about this before and it's kind of i think at least for like first launch of the of the site
[452.98 --> 458.34]  like it just makes more sense to make sure that everybody's not making any money on it if you want
[458.34 --> 464.28]  to go ahead and like um donate to someone's get tip that's your prerogative we can't really enforce
[464.28 --> 469.48]  you not doing that and sure everybody likes to get tipped but more importantly i don't want to deceive
[469.48 --> 474.34]  anybody hopping on thinking that they're going to make money off the bat if you get tipped in the
[474.34 --> 479.06]  end that's great you did a great job and somebody obviously felt that you did but don't feel like
[479.06 --> 482.84]  you're going to make any money out of it that's not what it's about and that's kind of where the name
[482.84 --> 488.66]  open karma came from it's it's more like karma points like you're just going to get paid in kindness
[488.66 --> 494.56]  well this is one of the things one of the things about just open source development is you you kind
[494.56 --> 498.38]  of get in there and and you get your name out there you start to contribute to some projects
[498.38 --> 503.64]  and you start to help out and it and it comes back around when you are you know when you're in a
[503.64 --> 507.46]  situation and you've open sourced your own project and you need help well that's the community right
[507.46 --> 512.46]  the community is there because because you started to insert yourself into this community and and you
[512.46 --> 517.06]  know you have a project that people love so they will give back to you to you so this is something i don't
[517.06 --> 522.92]  think designers necessarily traditionally have um you know i don't know i don't know what the right
[522.92 --> 528.98]  way to say it is but if you look at a lot of the old design uh you know procedures or policies or
[528.98 --> 533.40]  standards or however you want to put it it was kind of like hoard it and hold on to it for yourself
[533.40 --> 537.32]  right i mean it was like yeah don't share this with people because it's your time and money that
[537.32 --> 543.70]  went into it so you need to be compensated for it and you know there's no it doesn't take a genius to
[543.70 --> 549.52]  to realize that design and development are growing together right they need each other because as as
[549.52 --> 554.96]  the the develop as the tools grow the design and the ui around them need to be nicer need to be
[554.96 --> 559.18]  easier to use so they're going to grow together so i look at this as an opportunity for designers to be
[559.18 --> 564.70]  proactive and start to jump into the community and then when you have an idea down the road and you
[564.70 --> 571.14]  want developers to help work on this idea it literally has given you karma points right you have
[571.14 --> 575.82]  your name out there and people will help you because you helped them yeah i mean that was
[575.82 --> 580.78]  something else we talked about down the line that for right now it's really just about helping open
[580.78 --> 587.10]  source projects get a designer on board but we talked about down the line that you know say i have an idea
[587.10 --> 591.92]  like for example open karma and i don't know how to build the back end then i can be paired up with
[591.92 --> 597.42]  the developer who maybe saw that you know i got some karma points on my side like i've helped out the
[597.42 --> 602.92]  community and like he can help me out or she can help me out so right that's kind of just like i think
[602.92 --> 608.70]  maybe because i worked in a consultancy for two and a half years and i knew developers that were either
[608.70 --> 613.18]  contributing to open source or there were a few projects we were allowed to you know make open
[613.18 --> 619.46]  source um i kind of got thrown into a community i wasn't really aware existed and through that i just
[619.46 --> 624.62]  kind of saw the power of open source and you know like i pull stuff down all the time that like i need
[624.62 --> 630.70]  help with you know i can't really write that much back end code by myself so i'm just as guilty of you
[630.70 --> 637.46]  know uh kind of not mooching but like you know kind of partaking in the open source community is like
[637.46 --> 644.32]  partaking is a good word to use partaking yeah i'm i've been nomming on the open source community for a
[644.32 --> 651.40]  while so that's kind of where it came from i wanted to help out on on that note um justine on your home
[651.40 --> 656.40]  page uh you got a number of other projects that you've got listed there so like ruby conferences
[656.40 --> 662.58]  get immersion and a number of other things like are these things that you worked on as kind of like
[662.58 --> 669.54]  the predecessor to what open karma has become or is this things you did for uh for money or is this
[669.54 --> 675.48]  i'm just wondering like red car editor and some other things you've worked on it's a mix um so
[675.48 --> 682.42]  because i did work with mostly all developers for the last two and a half years um three years um
[682.42 --> 689.24]  some some of my like co-workers or friends would need help on projects like red car um and so i just
[689.24 --> 693.94]  kind of said hey yeah like i'll work on that i'm looking for a reason to illustrate a new icon but then
[693.94 --> 701.10]  other things like um get immersion and ruby conferences those are all um sponsored by my former
[701.10 --> 708.16]  employers and so they were either like get immersion was a complete redesign of the tutorial ui and then
[708.16 --> 713.64]  the ruby conferences were just things that i volunteered to kind of help out on when i had
[713.64 --> 720.18]  slack time at work did get immersion release or just launched recently this version this updated version
[720.18 --> 725.90]  um i would say it was about a year and a half two years ago i was thinking for some reason it was like
[725.90 --> 729.74]  in the last couple months for some reason i thought i'd saw it come across my
[729.74 --> 736.28]  stream but i guess i was wrong there but you were wrong i was wrong so i've got go ahead go
[736.28 --> 740.02]  to andrew all right i was gonna say i this is kind of like a almost off topic question but
[740.02 --> 746.26]  to get sebastian into the mix that's what i was gonna do as somebody who quiet yeah hey start talking
[746.26 --> 751.68]  all right as somebody who like has worked in open source worked in development you know done a lot of
[751.68 --> 757.42]  stuff what does it feel like i don't even necessarily know how to ask this question but obviously i have
[757.42 --> 762.34]  someone like justine who's a very talented designer and she's trying to build a tool to attract uh
[762.34 --> 768.82]  developers to other designers so it seems to me pretty important that the design of open karma is
[768.82 --> 774.42]  uh executed almost perfectly do you feel pressure like that like is that a weird kind of pressure that
[774.42 --> 779.10]  you ever feel when you're working on this thing that you're the only developer that is almost gonna like
[779.10 --> 782.66]  try to attract designers and developers to this thing
[782.66 --> 792.10]  i don't know uh not necessarily i just i do the back end justine does the front end i trust her with
[792.10 --> 801.16]  doing uh awesome design and she does and essentially developers are not different from other people they
[801.16 --> 809.34]  are looking at what looks pretty or what does not look pretty um the only difference is that
[809.34 --> 819.96]  if you're looking at a piece of software design becomes secondary if you know that the stuff below is
[819.96 --> 827.80]  extremely good right so so the it's almost like this these layers you have the design the usability in
[827.80 --> 831.68]  the back end and if you're if you're confident that it's all solid then then it's all solid
[831.68 --> 837.16]  exactly i mean for example audacity which we are using to record the show
[837.16 --> 842.46]  the interface the icon is oh my terrible yeah they can totally use open karma
[842.46 --> 851.22]  no offense i wasn't gonna say anything that's for sure yeah but if you're using it it's actually a
[851.22 --> 855.44]  super nice piece of software and you have a lot of filters and you can work with it
[855.44 --> 864.72]  but if you are just the user not a developer or you're just uh i don't know just recording for fun
[864.72 --> 873.10]  you don't really know if it's good or bad you have to dig a little deeper and it's just a face that
[873.10 --> 880.90]  you see first but you have to do really look at it to know that it's good we're also in a world
[880.90 --> 887.84]  i mean today i mean this this show tends to be more timeless than it is timely um but today you
[887.84 --> 893.24]  know apple had some announcements they announced some new ipads new macbooks and and obviously the
[893.24 --> 900.06]  world i guess the tech world and i guess becoming more consumer too is a lot more focused on the
[900.06 --> 905.42]  design and usability and the aesthetics of something so the more beautiful something becomes or the more
[905.42 --> 911.44]  aesthetically pleasing something becomes that you know the the inherent uh value it tends to have
[911.44 --> 917.28]  because oh it looks good it must be good right i would say i would kind of agree with that that's
[917.28 --> 922.34]  something i usually touch on when i'm speaking at conferences on design it's kind of like if you open
[922.34 --> 928.72]  up a website and it looks shitty then i'm kind of less inclined to trust the website but you can
[928.72 --> 933.20]  recognize if something's good right off the bat you won't you won't really know it's good you'll just
[933.20 --> 938.88]  kind of have this inherent trust and added value to it and so um that's one thing that i just kind of
[938.88 --> 944.46]  feel bad about for open source projects is that like you like you don't know that you're looking
[944.46 --> 949.66]  shitty but you kind of like anybody who opens it's gonna like know that it kind of is lacking
[949.66 --> 954.32]  aesthetically but as soon as you open up something and it's both as sebastian touched on like really
[954.32 --> 960.06]  well done on the back end but as an added bonus like has a cool icon and a great user interface like
[960.06 --> 966.72]  it's just like all this added value and kind of uh wow yeah it's like you just kind of you can kind
[966.72 --> 970.60]  of feel it it's something that you just you inherent like you said you inherently trust but
[970.60 --> 977.88]  let me ask something the developers love um refactoring they love like improving right so you
[977.88 --> 983.58]  write something once it works it gets the job done and but like i don't know open source developers
[983.58 --> 987.16]  especially seem to just like fall in love with refactoring their code and just making it always
[987.16 --> 992.66]  better and always better and designers i mean i can't speak for designers here but it seems like
[992.66 --> 999.20]  the the tendency for a for something like open karma would be for somebody to create a design one time
[999.20 --> 1003.92]  and then because developers you know they love iterating their software but i don't know that
[1003.92 --> 1010.34]  they necessarily love iterating design um so let's say designer comes and developer they meet up and
[1010.34 --> 1015.48]  and you know designer works on the project for him and then the developer executes that how do you
[1015.48 --> 1019.84]  prevent it from just sitting in that sitting in that design forever and not like iterating on the
[1019.84 --> 1026.36]  design and improving that part of it too i mean you you really can't like there's no way to like
[1026.36 --> 1031.76]  force someone to continue to work on a project what i would hope is that many of the designers that will
[1031.76 --> 1036.96]  be signing up for open karma will be people like me who create long-lasting relationships with the
[1036.96 --> 1042.66]  developers they're pairing with and instead of spreading yourself like thin and working on 10 different
[1042.66 --> 1048.20]  projects just like shipping a ui shipping an icon or a logo and just be like okay bye like i would
[1048.20 --> 1053.30]  kind of hope that maybe you get involved with a couple projects and then keep up with like long
[1053.30 --> 1059.44]  lasting relationship with that developer and like hopefully that's what comes to be but in all reality
[1059.44 --> 1065.78]  i can't really like tell designers that they have to keep iterating on the product as long as as the
[1065.78 --> 1071.06]  developers are interested in you know it could be they've maybe in like some open source projects
[1071.06 --> 1076.74]  really just all they want is an icon and they just need like kind of a you know a foot in the door
[1076.74 --> 1082.80]  and there could be a designer that has like that extra slack time to help them out with that and then
[1082.80 --> 1088.72]  there's other projects that are going to need like complete uis and and just like wireframing and stuff
[1088.72 --> 1093.60]  like that so like that's kind of one of the features we are hoping to implement in open karma is that
[1093.60 --> 1099.46]  designers will sign up and they'll kind of have these check boxes of what they're willing to kind of dive
[1099.46 --> 1105.38]  into and it might change based on their availability maybe they got on a new project but um so you know
[1105.38 --> 1110.56]  if you only have the availability or desire to work on icons or logos you just check check that off and
[1110.56 --> 1115.50]  so that when a developer open source team comes on and they're looking for something specific we'll be
[1115.50 --> 1119.88]  able to filter those results so you're not getting paired up with a designer that has no interest in
[1119.88 --> 1125.52]  working on like what you need right so it's almost like and i think the goal of open karma is not
[1125.52 --> 1132.56]  necessarily just to like elicit somebody to to work on this one thing for you it's like how to
[1132.56 --> 1136.50]  actually build it's like almost a tool to help developers and designer build relationships with
[1136.50 --> 1141.96]  each other because i've been kind of calling it match.com for designers and developers like kind
[1141.96 --> 1147.48]  of like making these these pairs these pairings and hopefully you fall in open source love or
[1147.48 --> 1152.74]  something like that yeah i mean i think it would be awesome if if through open karma designers because
[1152.74 --> 1158.34]  actually one of the things that that i talk about a lot is is um like people are afraid to get started
[1158.34 --> 1162.62]  in open source i think a lot of developers are afraid to get started in open source because
[1162.62 --> 1168.44]  you know they they not an inferiority complex but just like i don't if you've never put your code out
[1168.44 --> 1173.82]  there for other developers to review then it can be scary to think of you know to to people who are
[1173.82 --> 1178.10]  comfortable it's like community and comfort but to people who have never done it it's it's scary and
[1178.10 --> 1183.88]  it's unfamiliar to to have people like look at your code right and i think that developers in general
[1183.88 --> 1187.90]  and i don't know i mean i have a lot of friends that are designers and i feel like my developer
[1187.90 --> 1192.50]  friends can tend to be kind of clicky right and almost like hey let's get together and i'll talk
[1192.50 --> 1198.60]  about you know like just a bunch of developer stuff and oh yeah it's like a little in in like click
[1198.60 --> 1202.90]  that we have where it could be hard for a designer unless they're like super extroverted and super
[1202.90 --> 1208.72]  confident to like inject themselves into that group right and so yeah open karma has the potential to
[1208.72 --> 1213.08]  to bring down that barrier a little bit and i think to me that's like the biggest win that you guys can
[1213.08 --> 1218.98]  get i don't know how do you feel about that i mean that's what i'm really hoping for i mean i am an
[1218.98 --> 1224.50]  extrovert but it's still really hard for me to participate in conversations at conferences where
[1224.50 --> 1231.24]  or even like around like the lunch table when i used to have like an office team like just listening
[1231.24 --> 1236.98]  to all the developer babble can kind of become overwhelming for people who don't speak ruby or
[1236.98 --> 1241.46]  closure or anything like that like as soon as i start hearing anything about prams i'm just like i
[1241.46 --> 1245.96]  don't know what you're talking about can we talk about like the next game or something and i could
[1245.96 --> 1250.96]  care less about the next but i at least would understand more right and so it is kind of hard for
[1250.96 --> 1257.66]  designers to plunge into that unless they're used to it and a lot of designers might shy away from
[1257.66 --> 1263.62]  those kinds of situations because you know they might not feel like included or they might feel
[1263.62 --> 1269.26]  like they're not going to understand anything and you know that's kind of i think a problem that i
[1269.26 --> 1274.84]  would hope developers would kind of work on is when you do encounter people like me or other designers
[1274.84 --> 1281.36]  like at least if you're going to talk about like tech kind of include me in it or explain things to me in
[1281.36 --> 1286.52]  a way that i understand and you know that's kind of like a whole nother side tangent i could get
[1286.52 --> 1291.56]  involved in but you know be a little bit more inclusive of designers because we're not going
[1291.56 --> 1295.74]  to want to help you on your projects if you feel like if we feel like you're excluding us from
[1295.74 --> 1301.20]  your culture as well yeah i also feel like there's a an opportunity here too to kind of like trade
[1301.20 --> 1306.42]  in a sense you know we're and i guess you know karma is kind of part of it and maybe some kickback is
[1306.42 --> 1310.60]  kind of part of it as well but not so much in terms of dollars but just in terms of connections and
[1310.60 --> 1315.36]  opportunities but i'm thinking like if i wanted to learn a bit more about ruby i might pair up with a
[1315.36 --> 1321.64]  rubyist who knows a lot about ruby you know offer my design chops offer some of my skill sets and
[1321.64 --> 1328.44]  abilities to their project and in trade offer some you know kind of pairing session or mentoring you
[1328.44 --> 1332.96]  know it kind of seems like an opportunity to even connect at a personal level and kind of trade or
[1332.96 --> 1339.20]  cross train for for example yeah like no yeah i mean that's how i ended up uh going even to like
[1339.20 --> 1346.52]  ruby conferences is i gave quite a few times a talk on um like design for developers and kind of
[1346.52 --> 1352.28]  breaking it down in ways that developers can understand and that kind of spun off into a
[1352.28 --> 1357.96]  couple other talks and like how can you better pair with your designer and one thing i always harp on is
[1357.96 --> 1363.66]  like take the opportunity to learn from each other like sit down and pair with me or virtually pair with
[1363.66 --> 1368.58]  me because there's a lot i can learn from you and there's you know just as much you can learn from me
[1368.58 --> 1373.68]  and the better we know about what each other has to do the better we can make awesome things like
[1373.68 --> 1378.38]  it's that easy yeah i think a lot of developers struggle with like because if you think about it
[1378.38 --> 1383.80]  the semantics around development right developers have this like and we talk about this a lot but
[1383.80 --> 1387.70]  kenneth writes was on the show and he called it tribal knowledge so developers have this like tribal
[1387.70 --> 1392.96]  knowledge of this you have the the just the problem solving the the semantics of the language you're
[1392.96 --> 1396.82]  comfortable with the you know the just the stack and all this stuff and it's just all this knowledge
[1396.82 --> 1401.64]  that you you pick up over time and the language is very different from just like your typical you
[1401.64 --> 1406.62]  know normal everyday english and i think designer designers speak a language that's a little bit
[1406.62 --> 1411.80]  easier to understand just for like uh you know a joe schmo like myself with design so when i when i
[1411.80 --> 1416.18]  talk to my friends that are designers they the language they're speaking is very very easy for me to
[1416.18 --> 1419.60]  understand i mean as long as i understand like what gradients and drop shadows and stuff are
[1419.60 --> 1425.80]  then the language is easy to understand so i think that like there's this there's this tendency for a lot of
[1425.80 --> 1430.78]  developers to think that they almost like not that they know design but that there's nothing there
[1430.78 --> 1437.14]  to learn right because they know the words and it's like the knowledge is is is there it's this
[1437.14 --> 1442.68]  very intense knowledge that designers have just like developers and so if there's a way to get them to
[1442.68 --> 1448.30]  share that knowledge with each other now you're probably never you're probably never going to
[1448.30 --> 1454.16]  convert a you know someone that's just purely a designer into like a systems developer and you're
[1454.16 --> 1459.04]  probably never going to convert vice versa a systems developer into a designer right but if you can
[1459.04 --> 1464.60]  help to like bring down the barriers of knowledge between them then i think they work better together
[1464.60 --> 1469.28]  like i can work better with the designer when i'm when i better understand and respect what they're
[1469.28 --> 1473.84]  doing and vice versa and so that's something that open karma can really help with i think that's
[1473.84 --> 1478.38]  something i'm really hoping for because there's a tendency for and this is kind of a generalization
[1478.38 --> 1485.34]  but something i've picked up on a lot is the tendency for developers to define my job as making
[1485.34 --> 1490.92]  things look pretty which actually really pisses me off because i don't think it's fair to sebastian said
[1490.92 --> 1497.00]  that by the way yeah sebastian said that um and that's why he's he's being quiet because he's getting
[1497.00 --> 1504.02]  yelled at yeah um but then i find it to be really insulting because that would be like me telling a
[1504.02 --> 1510.22]  like you know introducing my developer friend and saying like this person types on keys really hard
[1510.22 --> 1515.90]  like i don't know um it's like i worked really hard to learn what i know and still continue this to
[1515.90 --> 1521.22]  this day to like make sure i'm understanding user experience properly and like there's all these
[1521.22 --> 1526.74]  things about color theory and there's so much more to design than just you know oh i i like blue
[1526.74 --> 1532.74]  so i made this button blue there's real science behind it there's science man with the cones and your
[1532.74 --> 1539.34]  eyeballs and like the psychology um so like that's kind of another thing is hoping to again and it
[1539.34 --> 1544.72]  it really depends on the people participating you have to be open to communicating in the same way
[1544.72 --> 1549.78]  that like me and sebastian have to communicate just to work on this project and as long as you're
[1549.78 --> 1553.40]  willing to do that you guys can learn like so much from each other and it's only going to help
[1553.40 --> 1558.76]  developers understand design more and i'm you know gonna have to learn more and i don't know pretty
[1558.76 --> 1562.00]  cool i'll feel like that's the barrier right there though is like if you like you had said the
[1562.00 --> 1568.34]  kind of hurdle was for the other person the developer not to really understand you know
[1568.34 --> 1572.18]  andrew you keyed off this which was like to not really understand design but you know know some
[1572.18 --> 1577.02]  of the language and lingo and kind of feel like they've got they've got it but i feel like as a
[1577.02 --> 1585.16]  as a designer myself you know whenever i help the other side um understand that i know about user
[1585.16 --> 1591.60]  experience i understand about usability i understand the psychology behind why a button is is so and so or
[1591.60 --> 1596.60]  why copy works a certain way once i help them understand that i've got more than just the
[1596.60 --> 1601.50]  ability to make things look nice i feel like there's this exchange in this aha moment because
[1601.50 --> 1607.64]  they realize that i've got such care for my craft the same as they do for understanding that a method
[1607.64 --> 1612.78]  you know should be a certain way or the there's certain idioms in ruby or whichever language they're
[1612.78 --> 1618.36]  working with and understand that we both have similar paths and and focuses are just in different genres of
[1618.36 --> 1624.86]  of things yeah i totally agree and i don't think there's ever going well you know i'm sure there's
[1624.86 --> 1631.04]  a few like special unicorns out there that can do both design and development like super well but like
[1631.04 --> 1636.20]  i work really hard to make sure that like you said i'm putting a lot of care and attention into the
[1636.20 --> 1642.52]  things that i'm designing and there's a reason why i'm making the line height a certain height and why
[1642.52 --> 1648.92]  i don't make a paragraph line exceed a certain amount of characters and so like i just hope that
[1648.92 --> 1653.90]  developers will have the opportunity to see that designers like you said kind of like have their own
[1653.90 --> 1659.28]  craft and we need to work together but i'm not just sitting around like screwing around on photoshop
[1659.28 --> 1663.98]  just to make something look nice there's kind of that mutual respect you need to have and i get that
[1663.98 --> 1670.14]  from most developers that i either sit down and talk with or who see me speak at conferences they kind of
[1670.14 --> 1676.08]  flip you know like you said like oh you do know things you know things like i know things we just
[1676.08 --> 1681.46]  know different things but we need our things to come together yeah exactly you're in the ruby community
[1681.46 --> 1686.90]  mostly right so that what i've found is and i can't speak for other communities but the ruby community
[1686.90 --> 1694.10]  specifically is very very um i don't know appreciative and open to to design and usability i think that's
[1694.10 --> 1698.92]  something that for whatever reason has kind of gotten a hold of the community i think that's a good
[1698.92 --> 1703.80]  thing and i honestly think that's why you find a lot of like you know justine i i didn't know that
[1703.80 --> 1707.96]  you were doing all the front-end development on open karma but that's a that's a trend that i think
[1707.96 --> 1713.74]  is a good one that a lot of designers are doing a lot of like not just necessarily front-end development
[1713.74 --> 1721.36]  but also um you know like mock-ups in html and stuff like that which i think helps to uh not that
[1721.36 --> 1725.66]  designers need to earn the respect of developers but speaking as a developer i think we can be pretty
[1725.66 --> 1731.82]  stubborn and we can be pretty uh you know pretty standoffish so i think that that designers are
[1731.82 --> 1736.58]  being more proactive than developers are in that area and i think that overall i mean like we keep
[1736.58 --> 1740.06]  harping on i guess but there's these barriers between them and anything that can make these
[1740.06 --> 1745.16]  barriers come down to to help the the respect and communication between these two sides that that
[1745.16 --> 1749.84]  are working together is a good thing right we're the same but different comes to mind for me like
[1749.84 --> 1754.82]  we're the same but we're different right and we're the same that yeah i care about design i care about
[1754.82 --> 1758.92]  using the right tools and the right tools might be designing the browser the right tool for me might
[1758.92 --> 1763.96]  be photoshop it might be some other tool that i've found that works really well for my flow but it's
[1763.96 --> 1769.22]  saying it's somehow getting past that point of we're the same but different so right like once you get
[1769.22 --> 1775.90]  there you're okay yeah so justin you and sebastian kind of are the first example of this working you guys
[1775.90 --> 1781.60]  had a chance meeting at a ruby conference or i think that's what you said and um uh if it wasn't for
[1781.60 --> 1786.66]  that meeting you guys might not be able to work on this together but what has your experience been
[1786.66 --> 1791.62]  like just to kind of work in one-on-one with another developer and and working on this project
[1791.62 --> 1796.46]  together and what would it have been like i mean do you think there was a bunch of other developers
[1796.46 --> 1800.50]  out there waiting to work on it with you or what would it have been like if you would not have had
[1800.50 --> 1807.14]  that you know chance meeting do you think um well sebastian i have the really fortunate i guess
[1807.14 --> 1812.16]  part of our relationship where we are really good friends and like i didn't like i could talk
[1812.16 --> 1816.82]  to sebastian about anything and i've known him for such a short time so i think that's where it kind of
[1816.82 --> 1823.26]  helps us like have that mutual respect and like he trusts me with the front end and the design and
[1823.26 --> 1829.94]  and like i trust him with the back end because we are close friends but um i definitely have more
[1829.94 --> 1834.98]  developer friends and i have designer friends and i'm sure someone else could have like helped me out
[1834.98 --> 1839.28]  with it but i find myself to be really fortunate that i have a really good friend working on it
[1839.28 --> 1844.98]  with me so that when we're up late like we can be hacking on this while at the same time having like
[1844.98 --> 1851.30]  a relaxed conversation so it's a really like good position to be in for this kind of intimate project
[1851.30 --> 1857.10]  like we kind of call it our creative child because like it's just something we're kind of working on
[1857.10 --> 1861.56]  and like you know i don't know he's just a good friend so i think it works out really well that way
[1861.56 --> 1866.32]  and probably wouldn't have worked out as well if i was just doing it with some developer i met on
[1866.32 --> 1871.50]  the internet you mean you guys actually are building a relationship working together yeah we're getting
[1871.50 --> 1879.96]  pretty serious i wouldn't be surprised if people thought we were in a relationship via our twitter
[1879.96 --> 1886.14]  status updates oh yeah well people make a lot of assumptions and you know you know what they say
[1886.14 --> 1894.26]  that's for um so so awesome so sebastian yeah what do you want to see happen with open karma
[1894.26 --> 1906.64]  well i think i just hope it works out somehow and um i think the most important part is to actually
[1906.64 --> 1913.52]  get designers excited about open karma and get involved and i think that can be achieved by
[1913.52 --> 1922.48]  going ahead and showing examples of designers working in open source for example john from ghost
[1922.48 --> 1930.32]  because essentially that's how he started he got involved in a open source project and now he's doing
[1930.32 --> 1937.88]  his own open source project and yeah actually we're gonna interview him as well so awesome so let's
[1937.88 --> 1942.54]  talk a little bit about open karma uh the future what you guys are in i don't know if you would call
[1942.54 --> 1947.08]  this it's not beta you guys are just like collecting information and getting people excited
[1947.08 --> 1951.56]  what is like the roadmap for you guys you're gonna have any kind of beta or when are you gonna launch
[1951.56 --> 1956.94]  or has any of that been talked about um we've been talking about a little bit like i'm in the process
[1956.94 --> 1964.06]  of moving and so is sebastian and we're both moving to berlin um so hopefully once things settle down a
[1964.06 --> 1969.92]  bit we can kind of finalize some of the wireframes i've been working on like i think the most important
[1969.92 --> 1975.46]  thing that i at least want to focus on before we even launch is making sure that we have a good like
[1975.46 --> 1981.26]  workflow we don't want anybody to get frustrated trying to you know pair up with the designer you
[1981.26 --> 1988.24]  know vice versa on this so i think planning is even more critical than kind of how it turns out as
[1988.24 --> 1992.98]  if i spend more time planning it then it's going to end up being a really good tool to use and
[1992.98 --> 1999.00]  kind of what sebastian said is i really would like to start generating more designer interest because
[1999.00 --> 2005.76]  i've had tons of developers just like you know sign up or like speak up and you know really reach out
[2005.76 --> 2012.48]  and that's great but i don't want to have a flood of like 900 developers start logging on to this site
[2012.48 --> 2017.58]  and have five designers on board and like you know that's kind of something else we're going to have
[2017.58 --> 2022.60]  to predict is this is there going to have to be a waiting list and like you know that just that kind of
[2022.60 --> 2027.08]  gets into what we talked about earlier where designers have to kind of like design and ditch
[2027.08 --> 2035.04]  and that's not a good like scenario to be in either so we'll see i mean like hopefully you know i can't
[2035.04 --> 2040.58]  be the only designer out there who is interested in working with open source and i know i'm not i've
[2040.58 --> 2045.78]  reached out to a couple people i used to work with and so we've got a few on board definitely but
[2045.78 --> 2051.32]  it's going to take a little while before we get even more designers so that we kind of have a one
[2051.32 --> 2056.32]  to one ratio or i would even be happy with like a one to five ratio or something yeah yeah of course
[2056.32 --> 2061.58]  developers are flocking to this oh yeah free design give it i'll hear it yeah i mean that's pretty much
[2061.58 --> 2067.30]  like my twitter just like blew up in the last two months and i was like jesus yeah you guys are coming
[2067.30 --> 2072.42]  off real desperate take me out to dinner first so we need to find designers we need to get get
[2072.42 --> 2077.34]  designers excited so you you don't want to obviously say a date you're going to launch but but is that
[2077.34 --> 2080.68]  kind of the milestone you're looking for you're you want to even out the designers before you guys
[2080.68 --> 2088.06]  even really consider like launching this or um that's my personal preference is to kind of have
[2088.06 --> 2093.80]  more designers on board um otherwise i feel like there's going to have to be some kind of feature
[2093.80 --> 2099.68]  where we only allow a certain amount of developers in at first and kind of test that and see how that
[2099.68 --> 2106.20]  goes and do like you know we'll probably have to like reiterate on some workflow things but um that
[2106.20 --> 2111.50]  might be a solution as well it's just like i would really hate to have all you know maybe we get 10
[2111.50 --> 2117.16]  designers on board get inundated with requests in the same way that i was and like you know it would
[2117.16 --> 2122.94]  just flop again so maybe it could be kind of even like mailbox where they only let a certain amount of
[2122.94 --> 2129.70]  people in at a time and then like just progressively let more people in as as they had right kind of
[2129.70 --> 2134.56]  bandwidth for yeah i mean they're the designers are out there that want to get involved we just it's like
[2134.56 --> 2138.88]  the the struggle the predecessor for you guys is going to be to to figure out the channels to to
[2138.88 --> 2143.10]  get in touch with all those designers and i think this is a common problem that actually a lot of
[2143.10 --> 2147.80]  services that are kind of coming up are dealing with and that is like how do you how do you get in
[2147.80 --> 2151.94]  touch with your target audience the people you need to get in touch with without it just looking like
[2151.94 --> 2158.32]  you know just another request in my inbox you know what i mean like um how you got you know i don't
[2158.32 --> 2162.32]  even know what the answer to that might be i don't know i mean i got some i got i don't know if it's time to
[2162.32 --> 2167.46]  share ideas but i got some ideas if you're looking for ideas on how to work it um let me share some
[2167.46 --> 2173.30]  ideas i mean this is a show right so yeah yeah this this is in fact a show i think the way that
[2173.30 --> 2178.46]  and uh we've had sasha grief i don't know if you're familiar with him um but we've had him on the show
[2178.46 --> 2185.04]  before he uh recently wrote a book on meteor and has even done some design in open source i think he's
[2185.04 --> 2192.44]  done stuff with ruby um i think it was locomotive the open source uh thing there and then he also
[2192.44 --> 2197.40]  did some stuff with ruby motion and then now he's doing some stuff with uh meteor and he's even kind
[2197.40 --> 2201.86]  of getting into more of a developer side than but he uh you know he says he's a designer and i know he's
[2201.86 --> 2206.80]  a designer but that's not the point the point is is that sasha runs this thing called folio
[2206.80 --> 2213.50]  and essentially it's a list and you could probably ask him but i think the same the model is free and
[2213.50 --> 2219.82]  open but in fact you know in the way that you can describe it but just having a list of designers
[2219.82 --> 2225.18]  and somebody who has an open source project so let's say the developer is essentially the client
[2225.18 --> 2230.56]  for lack of better terms right you've got a list of designers that get an email from you know whoever
[2230.56 --> 2236.18]  and you know they they email it into open karma you guys vet it approve it look at it make sure it
[2236.18 --> 2242.72]  meet your criteria and then you pass that along to your list of approved and ready to work uh
[2242.72 --> 2247.96]  designers and they say hey i'll take that and first to grab it is first to get it and it's essentially
[2247.96 --> 2252.04]  like that way you can have a list and they're not on the hook to like do whatever you don't have to
[2252.04 --> 2255.58]  manage schedules they take it whenever they want and then the open source developers they can just
[2255.58 --> 2259.74]  simply just say hey here's my new project i'm planning to launch next month or i've got some design
[2259.74 --> 2264.56]  needs here's the details and you can work with them back and forth justine and you and sebastian and
[2264.56 --> 2269.52]  can just make sure it's good to go and then pass that along once it's made it past your barrier
[2269.52 --> 2274.54]  and that's what sasha does with folio where he kind of acts as that buffer between both parties to make
[2274.54 --> 2279.84]  sure that the designers aren't seeing anything that isn't vetted by him that isn't blessed by him in
[2279.84 --> 2285.16]  fact that it's and the fact that it's something good for the community right and then you know the
[2285.16 --> 2290.24]  developers who are on the side you know the client for lack of better terms is uh is making sure that
[2290.24 --> 2294.46]  they've got their information in front of the right kind of eyeballs the right kind of people who want to
[2294.46 --> 2300.38]  help them and that's you're helping curate both sides of the list yeah that's something that like
[2300.38 --> 2307.00]  also i've i've brought up in brainstorming sessions is the last thing i want to do is pair up um you
[2307.00 --> 2312.02]  know a good open source project that's really you know i think is a you know good project last thing i
[2312.02 --> 2316.12]  want to do is pair them up with a designer who's kind of clueless and i think that there are a lot of
[2316.12 --> 2322.06]  designers out there that might want to help out but maybe aren't quite ready yet you know maybe
[2322.06 --> 2327.58]  they're they haven't been involved in tech that long maybe they you know don't know that much about
[2327.58 --> 2334.04]  ux um there are a lot of print designers out there trying to get tech jobs because there isn't a lot
[2334.04 --> 2340.00]  of print and i think that's where a lot of designers keep getting um like a bad rap like i feel like when
[2340.00 --> 2344.54]  people meet me they're not quite sure and kind of like what you said i have to prove myself is like
[2344.54 --> 2351.40]  knowing my shit and that i'm like not just someone who hands off flattened psds and you know tells you to go
[2351.40 --> 2357.18]  develop it i really would hate to see anything like that happening and so how do we kind of manage
[2357.18 --> 2364.34]  making sure that where you've got quality designers on board and not you know not just anybody out there
[2364.34 --> 2371.56]  it's not going to be craigslist yeah so to anyone who kind of is interested in you know applying as a
[2371.56 --> 2379.28]  designer what what should they do just go to it's open-karma.com open-karma.com and um
[2379.28 --> 2385.92]  if you sign up for like our mailing list um it would be nice if at if you scroll all the way to the bottom
[2385.92 --> 2392.24]  there's kind of like sign up to i think it's like sign up to keep in touch or something like that but
[2392.24 --> 2398.90]  there's um there's a form and if you fill out the form there's a couple of fields and if i don't know
[2398.90 --> 2403.76]  if it's your first name your last name just maybe say like hey you're a designer because that's really
[2403.76 --> 2409.22]  what i'm kind of focused on we've got so much dev outreach i really want to like ramp up the designer
[2409.22 --> 2416.02]  right aspect of it and it's uh be nice to know the people signing up kind of which side they're on
[2416.02 --> 2421.36]  right so how about if we just encourage people to reach out to you on twitter if they're signing up as
[2421.36 --> 2426.42]  a designer that'd be great so what is your what is your twiddle twiddle what is that twitter your
[2426.42 --> 2433.70]  twitter handle i think i combined those into one word it's um saltine justine like
[2433.70 --> 2439.76]  saltine like the cracker saltine at saltine justine so if you're a designer that is interested
[2439.76 --> 2446.78]  uh sign up for the newsletter or sorry sign up for the sign up and i say newsletter because it's a
[2446.78 --> 2451.76]  mailchimp sign up i don't know if it i guess it's not really a newsletter so much as when we launch
[2451.76 --> 2457.30]  we're gonna be like hey yeah it's a list sign up for the list and reach out to at saltine justine
[2457.30 --> 2463.22]  um and and say you're a designer and you're interested in helping out the more designers the more people
[2463.22 --> 2468.46]  that reach out as a designer i think the sooner we'll see this incredible project uh get going
[2468.46 --> 2475.52]  definitely so i think that we are gonna have you guys back on the show when this thing is launched
[2475.52 --> 2480.50]  and you have tons of awesome open source projects kind of spawning out of this thing and it's going
[2480.50 --> 2484.70]  to be real cool to see um you know on that note andrew i kind of feel like are you a fan of oprah
[2484.70 --> 2489.34]  this is kind of a side note but i think it's a funny one are you a fan of oprah the the host
[2489.34 --> 2494.86]  the oprah right yeah the oprah i'm like what i guess what else is there she's uh she's got this
[2494.86 --> 2498.62]  uh show where it says where are they now and i feel like that's what we need to do you know
[2498.62 --> 2502.10]  because we've had people on the show we need to have them back on the show where are you now
[2502.10 --> 2508.18]  yeah yeah well we've been getting a lot really sad sorry go ahead unless it's really sad and you
[2508.18 --> 2513.86]  don't want to see where they are yeah where are you now uh you know move along um no the uh
[2513.86 --> 2519.20]  we've had a lot of people on the show for some reason recently i feel like where the projects
[2519.20 --> 2523.56]  haven't launched yet and that's kind of cool right so we can kind of kind of be there for like
[2523.56 --> 2527.54]  the release parties and i think that's a neat thing so no we definitely uh we're coming up to
[2527.54 --> 2531.56]  a few months before i i throw that out a lot there but it's probably been a couple months now
[2531.56 --> 2534.88]  since the first time i said we'll have to have you back on the show so we need to go through
[2534.88 --> 2539.92]  the archive and find people that are are uh that have some success stories i know ghost launched
[2539.92 --> 2545.44]  and we need to talk to people again yeah but i do think we could go on but for the sake of keeping
[2545.44 --> 2550.52]  it under an hour um unless you guys have anything else say we'll kind of go ahead and jump into our
[2550.52 --> 2557.38]  interview questions do it so we ask same three questions for our new listeners to our guests
[2557.38 --> 2563.78]  on every show and we have two guests here so that means six questions so uh for you justine first
[2563.78 --> 2569.70]  question is for a call to arm so i can assume what you're gonna say but uh for for the community
[2569.70 --> 2575.10]  that's listening what do you want them to do to to kind of get involved um well if there are any
[2575.10 --> 2580.52]  designers listening please reach out but also for developers who work with designers if you work
[2580.52 --> 2586.04]  in a shop or you personally know designers who have worked in tech before and might be interested
[2586.04 --> 2591.38]  please ask them to reach out because they might not be listening but you might know that they're there
[2591.38 --> 2597.38]  and they would be interested so kind of hit up all aspects of it gotcha sebastian what about
[2597.38 --> 2604.58]  yourself same thing or got anything extra i i would second that and say if you know any signer grab
[2604.58 --> 2611.44]  him and make him sign up sit him down at the desk or her yeah and make him sign up for open karma.com
[2611.44 --> 2618.48]  exactly awesome uh justine if you weren't doing uh maybe not open karma but if you weren't doing
[2618.48 --> 2622.90]  you know working at travis or just doing what you're doing now um what what would you rather be doing
[2622.90 --> 2631.36]  um i would probably oh i don't know i'd probably either be a vet or just a regular artist
[2631.36 --> 2638.08]  nice starving artist or a vet that's awesome nice definitely the starving artist kind that's the best
[2638.08 --> 2641.82]  kind of artist when people talk about art that's the only kind that i like even think about i'm like
[2641.82 --> 2645.70]  that's the best kind of art that's the real art yeah well yeah once you stop eating for long
[2645.70 --> 2651.84]  enough you start hallucinating and that's when the real art happens uh what about you sebastian
[2651.84 --> 2662.26]  uh i probably would do much more mountain climbing and travel a lot and not sit like 16 hours a day in
[2662.26 --> 2669.00]  front of the computer nice just rotting away yeah exactly awesome that might be the first mountain
[2669.00 --> 2672.64]  climbing answer we've got a lot of outdoor answers but maybe the first time that anyone's ever said
[2672.64 --> 2679.08]  mountain climbing so i got respect for that uh the last one justine is for like a programmer hero is
[2679.08 --> 2683.04]  what we call it but really just somebody in your life that has kind of influenced you to to get you
[2683.04 --> 2690.74]  to the point you're at now um leon gersing i used to work with him um at edge case and now he works at
[2690.74 --> 2696.46]  github leon was really instrumental in making me believe that i could understand development programming
[2696.46 --> 2703.02]  terms and he always had a like a way of explaining things to me in a way that i could understand like
[2703.02 --> 2709.02]  when i asked him uh leon what's a kernel and i was like like not the popcorn kind like the kind you guys
[2709.02 --> 2714.38]  were talking about today and he's just really good at uh explaining that to me and so he really got me
[2714.38 --> 2720.66]  kind of confident and involved and i owe a lot of thanks to leon and leon gersing you said is a
[2720.66 --> 2727.20]  githubber is that right yeah awesome and sebastian what about yourself uh i would say jeffrey zeldman
[2727.20 --> 2734.22]  oh nice oh yeah everyone knows him uh i think the god was the first book
[2734.22 --> 2743.36]  exactly i mean that was the first book i ever read about uh developing html and css and it's been
[2743.36 --> 2752.04]  the bible for me ever since and yeah yeah you're talking about uh what was his book the uh
[2752.04 --> 2758.10]  uh designing with web standards web standards yeah that's right yeah awesome and he's he is still
[2758.10 --> 2763.72]  steering the the developers or especially from the developers in the right direction which is pretty
[2763.72 --> 2771.96]  nice yeah he's a i think he's a good guy i think that uh well i think he's had his uh he's had his
[2771.96 --> 2777.80]  his mark in the industry that's for that's for sure he's a fellow five by five or two he's got uh
[2777.80 --> 2783.42]  he's got the big web show here on five by five very popular show um man he's done lots of cool stuff
[2783.42 --> 2789.70]  i mean just around podcasting in the community he's got a list apart a book apart uh a thing apart i
[2789.70 --> 2795.96]  don't know he's got all sorts of an event apart yeah everything apart yeah jeffrey is uh is a good
[2795.96 --> 2799.90]  guy i wish uh wish we had the type of show where it would make sense to have him on but
[2799.90 --> 2808.90]  yeah it doesn't doesn't show for some reason bummer bummer um let's see so yeah i think that was
[2808.90 --> 2812.32]  that was the questions i like your answers on mountain climbing that's a that's a good one for
[2812.32 --> 2816.22]  sure i was thinking about mike param for some reason when he said that because mike works at
[2816.22 --> 2820.34]  outdoors company yeah climb.com yeah yeah i was kind of thinking about that one but yeah
[2820.34 --> 2825.98]  well i'm pretty happy it was sitting on my ass all the time so whatever other career i would have
[2825.98 --> 2831.66]  it would still involve that yeah a vet and what was your other one an artist yeah it's a lot of
[2831.66 --> 2838.84]  yeah i mean yeah vets can be somewhat they can walk they stand oh yeah yeah we need the vets man i love
[2838.84 --> 2845.30]  our vet for our dog yeah well that's it for this uh this show um i want to thank both you guys for
[2845.30 --> 2849.62]  for coming on the show justine and sebastian you guys have a really cool thing you're doing here
[2849.62 --> 2854.64]  whatever support we can give you uh as the change log as individuals as well let us know we'll do
[2854.64 --> 2859.20]  whatever we can uh we definitely um wanted to have you on the show to kind of talk about what
[2859.20 --> 2864.56]  it means to have design more baked into development and open source and lifting up that's certainly what
[2864.56 --> 2871.14]  we uh appreciate here on the show and on our blog as well um want to thank our sponsor digital ocean
[2871.14 --> 2875.90]  one more time for uh you know just just showing us some love and at the same time showing the
[2875.90 --> 2881.22]  community some love and a couple things i want to mention is um i definitely want to mention the
[2881.22 --> 2885.54]  hosting credit so you can get a ten dollar hosting credit whenever you sign up use our coupon code
[2885.54 --> 2893.44]  the changelog october again that's the changelog october um one other cool thing they're doing to
[2893.44 --> 2899.38]  kind of help lift up the community is to pay you fifty dollars to write tutorials and write articles for
[2899.38 --> 2905.24]  their community um it could be a tutorial on how to use your open source project doesn't even have to be
[2905.24 --> 2910.70]  something that is for digital ocean or it can be something that is on digital ocean for example
[2910.70 --> 2915.88]  a couple examples that are already out there is how to install lamp stacks or how to install a lamp
[2915.88 --> 2921.32]  stack with wordpress on ubuntu or how to use i mentioned earlier in the show or i guess before the show
[2921.32 --> 2925.50]  how to use digital ocean's official ghost application if you haven't heard about this
[2925.50 --> 2931.90]  go back to episode 105 we talked to john and nolan about ghost um it's a node-based uh open source
[2931.90 --> 2937.24]  blogging platform digital ocean has an official one click application you can use um that's pretty
[2937.24 --> 2944.20]  neat um and they also want to send stickers around the world so it doesn't matter if you're in vienna
[2944.20 --> 2951.32]  u.s japan wherever you're at uh email barry at digital ocean and he'll ship out some uh some
[2951.32 --> 2956.48]  stickers to you digital ocean stickers to you so um one more thing for them is if you want to be a part
[2956.48 --> 2962.52]  of their team they are hiring in new york city so uh that's the nyc check out their open source or
[2962.52 --> 2968.34]  sorry their open position they got open source in the brain check out their open positions at
[2968.34 --> 2974.08]  digitalocean.com slash jobs but uh justine sebastian thanks again for coming on the show and
[2974.08 --> 2977.82]  for all that you're doing we definitely want to support you however we can to you the listeners
[2977.82 --> 2984.96]  and uh andrew for rocking out this show so let's say goodbye see y'all later bye
[2984.96 --> 2985.40]  bye-bye
[3014.96 --> 3015.46]  you
[3015.46 --> 3015.96]  you
[3015.96 --> 3016.00]  you
