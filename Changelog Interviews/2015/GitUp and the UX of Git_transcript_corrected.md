[0.00 → 15.76] welcome back everyone this is the changelog and I'm your host Adam stekowiak this is episode 172
[15.76 → 22.02] and on today's show we're joined by Pierre Olivier labour we dive deep into Pierre's history we
[22.02 → 29.12] joined this call to talk about git and his new open source project get up, but we had to go so
[29.12 → 34.90] deep in his history to fully appreciate uh what he's done and where he's going so we go back to
[34.90 → 40.62] his history at apple back to his uh product he developed called ever pix and went through all of
[40.62 → 48.54] that and then at the tail end of the show we start talking deeply about git get up and git UX and why
[48.54 → 58.52] you might love hate git we'll see, but we had four awesome sponsors code ship image digital ocean and
[58.52 → 62.62] sentry is a new sponsor for us love those guys thank you so much for supporting the show
[62.62 → 69.40] our first sponsor is codeship launched a brand-new feature called organizations a few
[69.40 → 74.50] months back everyone's been loving it now you can create teams you can set permissions for your
[74.50 → 79.02] specific team members, and you can improve collaboration in your continuous delivery
[79.02 → 85.02] workflows you can maintain your centralized control over your entire organization's projects and teams
[85.02 → 91.30] with this new feature it's super awesome, and you can save 20 off any premium plan you choose for
[91.30 → 97.98] three months by using our code the change law podcast again that code is the change law podcast
[97.98 → 104.72] 20 off any plan you choose for three months head to codeship.com slash the change law to get started
[104.72 → 110.78] and one more thing I want to tell you about Sean Devine is doing an API workshop called API first
[110.78 → 117.48] training and guess what he's going to use code ship as a demo tool the URL to learn more about that API
[117.48 → 121.04] training is in our show notes so check those out but now on to the show
[121.04 → 134.16] everyone we're here today with Pierre Olivier labour uh everybody in this entire world knows that I'm not
[134.16 → 140.48] the best with French names Pierre but how did I do you did pretty good um hello Adam thanks for
[140.48 → 145.92] having me with you today so Pierre we've been uh we've been chatting quite a bit here before we
[145.92 → 151.94] actually started hitting the record button and I've kind of gotten a little bit familiar with your past
[151.94 → 158.46] your passion for software development you got a deep history um everything from apple to companies
[158.46 → 163.78] you've started from ideas you've had while on vacation to you know you name it but what I love
[163.78 → 169.92] to do is sort of start the show-off with going deep into your history if we can, but before we do that
[169.92 → 176.26] can you kind of give the audience who may not know who you are a brief um introduction to whom
[176.26 → 182.88] you are sure um I'd be happy to um so like you mentioned um I'm actually French I'm not sure how
[182.88 → 189.28] relevant that is but I might explain some of my um accent and um I've been doing software development
[189.28 → 195.64] uh all aspects of it really from uh writing code of course a lot of that in multiple type of languages
[195.64 → 203.42] but software development of mobile apps of desktop apps of server-side code uh kernel drivers like this
[203.42 → 209.84] sort of things uh I've been doing that for almost for a little more than 15 years now uh in a might
[209.84 → 217.00] say professional way and what I mean by that is uh writing code uh that is for products that ship to
[217.00 → 222.82] consumers who pay for it right or to an extent sometimes use it for free uh so I'm not counting
[222.82 → 229.86] little safe projects done on the side this sort of things and I live in San Francisco in the silicon
[229.86 → 237.04] valley that is very close uh been working at some large companies um in the valley some startups I had my
[237.04 → 245.52] own startups over the year and so on um and yes my big thing is uh software in general um all aspects
[245.52 → 252.98] of it which I'm very interested in and I think when anybody looks at your history and sees this 15
[252.98 → 258.38] year of professional software development as you said they're going to see names like apple on it and
[258.38 → 264.38] apple obviously turns heads when anybody sees it on their resume so not to camp out there but how much
[264.38 → 270.32] further back in your life do we have to go to kind of figure out where you got this itch of software
[270.32 → 278.60] development where when did things begin for you to become a software developer um I do so one
[278.60 → 285.18] important uh background I guess information is I've always been uh tinkering to an extent um with
[285.18 → 291.64] you know electronics uh when I was a kid uh building uh radio control airplanes I call this sort of
[291.64 → 297.32] things and a logical evolution at the time was starting to do things with the personal computer
[297.32 → 304.10] my parents had a mac classic uh very old machine right and then I had some um Atari which was
[304.10 → 309.20] reasonably popular in France um there was also the Amiga which was pretty popular at the time
[309.20 → 315.72] and you know what you do on a computer is rapidly you want to create things, and so I played at the time
[315.72 → 321.26] quite a bit with I think it was hypercard and then started learning basic which we had actually at school
[321.26 → 326.48] to an extent we had some programming lessons already at that time we were learning if I recall correctly
[326.48 → 332.34] some basic, and then we did learn a bit of pascal and then I started creating things and then I started
[332.34 → 339.16] creating software based on ideas and then uh you know what I would like to do for me and then started
[339.16 → 344.54] distributing it and that's how the whole thing started a lot of the time that was slightly before
[344.54 → 351.22] internet when my first software was distributed commercially which just borderline where internet was
[351.22 → 358.26] starting to be mainstream and to an extent, and it was still a time when you had to put your
[358.26 → 365.10] sharewares and applications on things called if I recall correctly the info mark archive something like
[365.10 → 371.64] that which was um done by the MIT, and you know storage was very expensive at the time on servers to
[371.64 → 378.88] store the binaries of the apps and so on so uh you had all sort of ftp mirrors, and you had to
[378.88 → 383.72] distribute your software and CDs that came with magazines and lots of hoops to jump through that
[383.72 → 388.96] we don't have to do uh today anymore of course but so this is kind of how it started
[388.96 → 394.52] I just looked up the mark archive on Wikipedia because I got fast fingers
[394.52 → 399.04] and it says it's a computer related mailing list archive is that uh does that ring a bell
[399.04 → 408.54] yes, yes that's how at the time if you were doing uh not a professional uh you know commercially well
[408.54 → 414.18] not a professional software distributed by an official publisher in stores and this sort of things
[414.18 → 421.62] like photoshop for instance but if you're doing sharewares, and you wanted to be um to reach out
[421.62 → 429.74] to people this was how it was happening you had to send somehow your compressed file of your little
[429.74 → 436.16] app to that server and with a special text file where you were giving the right to that archive to
[436.16 → 441.54] redistribute your file under certain condition and then magazines around the world would grab that file
[441.54 → 447.82] if they liked the app and put it on their CDs which was coming with the magazine and um it was like i
[447.82 → 453.64] said jumping through hoops, but it was pretty cool because if you did not have instant gratification
[453.64 → 458.08] like you might have today it was really deferred you put your thing in there, and then you don't know
[458.08 → 466.42] what's going to happen and then one day you receive um a Japanese magazine a mac magazine you know I was in
[466.42 → 471.72] France coming all the way from Japan and because they had put your app on the CD that came with their
[471.72 → 477.08] magazine um which is, but it might have been two three months later or who knows and so this
[477.08 → 483.14] type of deferred gratification was pretty nice at the time I think uh your mention of the instant
[483.14 → 490.16] gratification is certainly a talking point because in today's world we really are instantly
[490.16 → 497.16] gratified with likes with tweets with followers on GitHub with forks with issues there's something
[497.16 → 501.88] there's like instant feedback loop to whatever we put out there whether it's the smallest thing to
[501.88 → 506.40] the biggest thing uh whether it's professional work or if it's side hobby fun stuff
[506.40 → 513.74] um what was it like to be in a know like let's say a slow-paced world uh as a software
[513.74 → 520.64] developer just kind of butting up back then that's been uh you know that's been quite a few years um
[520.64 → 523.10] I think it was
[523.10 → 532.50] it teaches you patience um you could not easily update your app like today most apps have most apps
[532.50 → 537.40] sorry are auto updating by definition it really started with the iPhone, and then it rolled on a
[537.40 → 541.98] desktop and then apps are self-auto updating even if they're not part of the app store and this is
[541.98 → 547.72] the way to go it's obvious to multiple um multiple reasons but at the time you did not really have that
[547.72 → 553.34] the latency between a new version the fact people would have it would be significant and so you had to
[553.34 → 557.62] I think pay a lot of attention to the Polish of your software and the quality of the code and all of this
[557.62 → 564.02] now at the same time um I think the software world was moving slower which means it was less likely
[564.02 → 569.32] that things were moved very fast under your feet meaning the OS would not be updated as often
[569.32 → 574.52] uh technologies you were relying on would not change as often and so on well today you know it's
[574.52 → 579.70] impossible I think that's one of the challenges with today's development is it's impossible to keep
[579.70 → 587.32] anything constant so you might have you know I'll use as an example a comic flow which is an iPad app
[587.32 → 593.56] I've done a few years back which is still you know quite popular today it's an app to read comics
[593.56 → 601.44] and um this is the same code base that was written I think five years ago for the original iPad if I'm
[601.44 → 610.86] not mistaken the exact same code and the problem is um when iOS 7 was released the whole UI changed
[610.86 → 617.10] and it's not a big deal because your app still works on it but if you want to fix one little bug because
[617.10 → 621.98] there was suddenly a change in behaviour in the OS and your app even if it works almost the same
[621.98 → 627.74] there's a little thing you need to fix well now you need to take your app and build it against the
[627.74 → 632.74] latest SDK you have no choice otherwise apple does not accept your app into the app store so suddenly
[632.74 → 637.08] you have to build your app against iOS 7 even though it was built originally and designed around
[637.08 → 643.14] iOS 5 and just the act of building it will expose a bunch of things that will break because they've
[643.14 → 647.40] changed the name of functions they've changed the behaviour of things they've changed how the UI worked
[647.40 → 652.72] a bunch of and so what would have turned into fixing and I'm not necessarily exaggerating a single
[652.72 → 658.56] line of code is now a whole project of changing your app and the thing is you don't have a choice
[658.56 → 663.44] because if you don't do that then your app is a little bit broken, so things are changing under your
[663.44 → 668.56] fit and I would say it's even worse uh in a way on the server side of things because you can write a
[668.56 → 674.34] beautiful piece of you know server code that is fully self-contained very clean and so on but guess
[674.34 → 679.28] what um now it's written in python a new version of python comes out you might say well that's okay
[679.28 → 683.50] I'm going to stay on the old one but then your whole software stack which is on Amazon is running
[683.50 → 689.78] obviously their own you know servers, and they have their own security rules and policies, and they say
[689.78 → 695.60] well guess what you cannot run that version of our OS anymore because it has security issues and we
[695.60 → 700.36] need to update, and now it's been x number of months we're going to force update all the machines
[700.36 → 705.20] the version of python you're relying on has to be updated as part of that and so you haven't changed
[705.20 → 709.64] anything on your side, but things have changed underneath you and then suddenly a bug appears
[709.64 → 716.54] well there was none before and so you know it's um it's a bit like Syria in a way right you keep
[716.54 → 721.88] pushing that that that um boulder above the mountain, and it falls, and you have to do it again and again
[721.88 → 728.32] and again um it was nice I think at that time because the pace was much slower and when you were
[728.32 → 735.24] writing something you were pretty confident it would stay the same for you know a couple of years more
[735.24 → 741.86] and so on um it was a different time now obviously today's time comes with its own set of
[741.86 → 750.96] advantages it's not all um negative of course you said you're a Frenchman so um, and you said that
[750.96 → 756.22] uh you know back in this day let's lets sort of not just paint the history let's sort of paint some
[756.22 → 763.38] timelines uh you said when the internet began when did the internet begin for you yeah that's a
[763.38 → 769.86] completely fair question because it was very different in Europe and in uh in the US um
[769.86 → 778.92] internet to me began when I guess i I cannot recall how it happened why it happened, but we did buy a
[778.92 → 785.86] modem um which at the time was probably 25 kilobits per second or something ridiculous like that and
[785.86 → 793.46] it was pretty expensive because you had to pay on the phone lines um and that's how that's how it all
[793.46 → 802.52] started I started using um internet yes what year was that roughly you know um
[802.52 → 808.10] um I'm thinking personally it might be like 95 97 but yes that's what I would say that's what I would
[808.10 → 814.18] say um my gut because you're around my age I'm 36 so I think you're roughly the same age yeah I'm 35
[814.18 → 822.66] same thing and I would say for me in France it was around 95 96 yes that's the best yes I can do
[822.66 → 829.32] now I did go to the US uh a number of times when I was a kid and then later on and in the summer of
[829.32 → 836.92] 97 or 96 I was in the US and yes you could see I mean uh going to a summer school there and the
[836.92 → 843.00] school slash university was very well-connected on internet and so on more than what I had access
[843.00 → 850.02] to um in France now France you may be aware of i had this whole thing um which was kind of pre-internet
[850.02 → 855.78] before internet right they called the mini tell uh which was a computer networked uh on top of the
[855.78 → 862.40] phone system with little computers that a lot of French households were having with a little keyboard
[862.40 → 866.30] and kind of text-based display but able to do graphics and whatnot and that lasted
[866.30 → 872.06] if I'm not mistaken that was the 80s um to early 90s, and then it disappeared when internet happened
[872.06 → 878.92] and it was uh, but it was uh definitely um omnipresent in the French household, and it was
[878.92 → 888.56] the yeah a distributed network of network terminals um it was surprisingly um ahead of its time in a way in a
[888.56 → 894.98] way but way more limited than internet because it did not have the big thing that um the hypertext was
[894.98 → 900.86] and HTML and all of this um but so our home did not have that however uh one of the few homes that
[900.86 → 908.38] did not have this system um so, but we did get a modem and all of this later on so for those who may be
[908.38 → 913.12] uh fellow Frenchmen listening they may go back in history and think a little bit of man when did
[913.12 → 920.90] uh mini tell kind of end, or you know what was the state of it and in 2009 based on Wikipedia because i
[920.90 → 927.32] got again fast fingers here uh still served roughly 10 million monthly connections back in 2009 but
[927.32 → 935.24] ultimately in june 2012 they decided to retire the service so yes and the unit as you mentioned
[935.24 → 942.50] it you know 10 million monthly connection is for a population of uh 70 million people close to that
[942.50 → 949.36] now which is probably around 25 30 millions um households uh is extremely littered uh at its peak
[949.36 → 955.40] I'm sure it was quite more than this um it was really um present in the vast majority of households
[955.40 → 962.40] it was uh very interesting so we mentioned roughly the time frame of when the internet began for you
[962.40 → 969.48] 95 97 somewhere that time frame there, and you mentioned getting a professional app which you
[969.48 → 976.64] describe as uh somewhat something that someone buys um you mentioned delivering something pretty early
[976.64 → 981.16] I think you even said your childhood if I remember correctly what was the first thing you built what
[981.16 → 994.08] was delivering it like what was the app I'm not sure i I recall um this is uh this is a while
[994.08 → 999.18] back right we're touching 20 years ago right um we're definitely tapping into the deep brain
[999.18 → 1006.16] here yeah yeah um it would have been utilities like little things little apps that would do
[1006.16 → 1015.76] one single function and I'm trying to remember I think one of them was to do patterns uh that you would
[1015.76 → 1022.04] use as to edit patterns or combine them I don't remember exactly um that you would set at as a desktop
[1022.04 → 1029.48] backgrounds now um it may sound strange today but um on computers at the time they had very limited
[1029.48 → 1035.30] video memory and regular memory as a matter of fact and so you weren't going to use a full image for
[1035.30 → 1039.86] your desktop background you were going to use a small pattern that you would simply repeat there
[1039.86 → 1045.06] wouldn't have been enough memory to necessarily store the entire a photo for instance filling the
[1045.06 → 1049.30] entire screen or if it had been possible then you would have used too much memory anyway to
[1049.30 → 1054.76] leave um enough available for the other apps and this sort of things so i I remember working on
[1054.76 → 1059.54] something like that and one of these utilities being the first app i would send to this
[1059.54 → 1066.60] archive of software and then that ended up on various CDs and all of that well that's interesting
[1066.60 → 1074.02] to the coming back to the CDs aspect you mentioned being in France getting an magazine from Japan or
[1074.02 → 1080.50] something like that and it's having your uh your software on it and how did they deliver it what was
[1080.50 → 1086.92] well I guess what was interesting about that was it like was it like um having a book published was it
[1086.92 → 1092.52] like the moment like the moment I think it's its a fine analogy um it's the type of gratification
[1092.52 → 1099.68] is very different uh like today there are millions of developers um on all sort of technology stacks
[1099.68 → 1108.04] um the most easy to use widely used tech stack is obviously the web tech stack right, and you can do a
[1108.04 → 1113.98] website an interactive website and then that's if it's online anyone in the world can go see if it's
[1113.98 → 1120.50] it's instant um it's very different from at the time suddenly writing a piece of software
[1120.50 → 1128.04] um uploading it super slowly to the ftp server uh or a mirror of it somewhere in the US on the MIT when
[1128.04 → 1133.48] you're in France and then crossing your finger putting your little text file with it describing the
[1133.48 → 1140.48] the app describing the uh some sort of license something like that just to say you know what were the
[1140.48 → 1145.22] conditions um under which you allow it through distribution on CDs and things like that and i
[1145.22 → 1150.88] I think I might have put something along the lines of please send me a magazine at this address if you
[1150.88 → 1157.06] distribute it, but some magazines would do it anyway um and then just wait and cross your figure and
[1157.06 → 1161.44] hope but at this point you know I'm not sure anyone at the time I can't say for sure but I would be
[1161.44 → 1168.56] skeptical a lot of people would necessarily go into the archive and just browse uh the way we got
[1168.56 → 1174.14] apps was through these CDs or before the CDs because it needs to go further than that um they
[1174.14 → 1180.86] were coming with little floppy disks right I mean not I mean the 3.5 the small disk um I'm looking for
[1180.86 → 1186.76] the exact term in English but the uh not the floppy ones the smaller version right and um you know
[1186.76 → 1190.96] it was exciting it's like you get your magazine once a month and then what apps am I going to get
[1190.96 → 1195.40] with it and type of freewares and sharewares and all of this, and they have to be very small because
[1195.40 → 1200.54] they have to fit on um 1.5 megabytes or whatever it was or less than two megabytes
[1200.54 → 1206.68] for a number of these little apps so that was pretty exciting, and you're correct using the
[1206.68 → 1212.80] analogy that it was equivalent to being published and then later on you had um I think it was download
[1212.80 → 1220.04] well CNET something and then download.com started to be uh the places where you had to be uh to
[1220.04 → 1225.72] uh I'm I will just want to be clear by the way that I'm talking about the mac side of things right
[1225.72 → 1232.12] um I cannot speak for the experience of publishing uh distributing software on the windows platform or
[1232.12 → 1236.52] Amiga or Atari or any of these I'm glad you made that uh mention because I was going to ask you about
[1236.52 → 1240.80] that because it seems like you said the very first computer that your parents had was an uh an apple basic
[1240.80 → 1247.92] right um uh mac classic sorry yes, yes well we had an apple 2 actually to be correct we did
[1247.92 → 1256.36] have an apple 2 um and I mean I have photos of me as a toddler like next to the apple 2 and
[1256.36 → 1262.96] this sort of things but so that's how i kind of recall um but we did have a mac classic later on
[1262.96 → 1269.40] and I guess we were from the start an apple house in a way and then when apple was kind of losing
[1269.40 → 1277.00] some steam um for some reason we had an Atari and then went back into the mac later on and just for the
[1277.00 → 1282.76] English speaking out there who don't have an accent and no poking fun whatsoever right I think you're saying Atari
[1282.76 → 1290.20] yes, yes okay just making sure Atari yes and uh it was a big deal in France along with uh Amiga
[1290.20 → 1297.00] I love the Atari I mean who didn't love the Atari right I mean that was that's that's when that's when like
[1297.00 → 1304.42] the light bulbs went off for so many people yeah, yeah well Pierre let's let's pause there for a
[1304.42 → 1309.70] minute since we talked about apple I do want to dive a bit into your apple history but let's take a quick
[1309.70 → 1315.66] sponsor break we'll come back, and we'll talk about apple for you and some things you've uh did in
[1315.66 → 1323.16] the apple space and continue to do obviously but uh we'll be right back image is a real-time image
[1323.16 → 1330.58] processing proxy and CDN and let me tell you this is way more than image magic running on ec2 this is
[1330.58 → 1339.02] way better it's everything your friend and developers have dreamt of output to PNG JPEG if JPEG 2000 and
[1339.02 → 1345.44] several other formats and if you're like me, you've ever argued with your boss or a teammate about serving
[1345.44 → 1351.18] retina images to non-retina devices you'll appreciate their open source dependency free
[1351.18 → 1357.66] JavaScript library that allows you to easily use the image API to make your images responsive to
[1357.66 → 1364.32] any device now all this takes a platform and the image platform is built on three core values
[1364.32 → 1371.10] flexibility and quality performance and affordability when it comes to flexibility and quality
[1371.10 → 1378.60] image has over 90 URL parameters that you can mix and match to provide an unlimited amount of
[1378.60 → 1384.30] transformations that you need for your images, and they take quality very seriously and because of
[1384.30 → 1390.50] their commitment to quality several top 1000 websites in the world trust them to serve their
[1390.50 → 1397.00] images now when it comes to performance image operates out of data centres filled with top of
[1397.00 → 1403.22] the line mac pros and mac minis, and they're set up for a completely streaming solution this means your
[1403.22 → 1411.78] images are served by the best SSD based CDM for delivery around the world anywhere extremely fast
[1411.78 → 1418.04] and while we're talking about speed almost all the image processing happens on GPUs this means
[1418.04 → 1424.44] transformations are superfast when compared to competing virtualized environments, and lastly it's
[1424.44 → 1430.74] all about affordability everyone wants to save a buck that's how the world works because image processes
[1430.74 → 1438.10] close to a billion with a b images per day they're able to make certain optimizations at scale and pass
[1438.10 → 1445.30] those savings on to you to learn more about image and what they're all about head to imgix.com
[1445.30 → 1453.70] slash changelog once again imgix.com slash changelog and tell the madam from the changelog sent you
[1453.70 → 1463.12] all right we're back with Pierre Olivier labour an uh an awesome French software developer with a deep
[1463.12 → 1469.90] passion for some really cool stuff and Pierre you said your household your mom and your dad yourself
[1469.90 → 1477.18] were apple you got a picture of yourself next to uh an apple a mac classic um, or it was an apple
[1477.18 → 1483.54] two apple two so I mean we're back as a toddler not too many people have that kind of history with
[1483.54 → 1490.22] with computers or even software development so you kind of go really, really far back and uh
[1490.22 → 1496.72] if anyone scans your history and learns a bit about you one of the things they sort of uh notice pretty
[1496.72 → 1503.78] early on is that uh you're an apple guy of course but that you also had the joy of selling a company
[1503.78 → 1509.62] or a product I'm not sure how you really phrased that to apple which ultimately became quartz composer
[1509.62 → 1515.82] can you speak to that a little bit um yes, yes um I certainly can um I think it's important
[1515.82 → 1526.44] to have a little bit of um history for the context um the while I was so I've always done um as you
[1526.44 → 1532.42] mentioned a number of software projects some of them personal some of them commercial and um
[1532.42 → 1538.58] um towards the end of um university I guess you would say that I was going to an engineering
[1538.58 → 1547.96] school in Switzerland at the time um I was working on um a video game startup that I co-founded with a
[1547.96 → 1552.22] few other people and mostly a lot of graphic designers as a matter of fact I think we were six graphic
[1552.22 → 1557.28] designers and a couple programmers and plus marketing and this sort of things, and so we worked
[1557.28 → 1562.76] more than two years on a video game that we um published and distributed in Europe and all of
[1562.76 → 1569.20] this, and it was actually a real-time 3d video game and that was the result of me starting to
[1569.20 → 1574.98] experiment a couple of years before with the real-time 3d graphic chips that were starting to appear
[1574.98 → 1580.88] on the mac and so you might remember at the time companies like 3dfx which were starting to build
[1580.88 → 1585.68] these uh these cards you could plug into your pc, and suddenly you were able to do 3d rendering in
[1585.68 → 1592.54] real-time uh incredibly faster than doing it on the CPU of course um and uh well on the mac you know
[1592.54 → 1597.24] it took a long time before 3dfx was compatible with the right drivers and whatnot but um there
[1597.24 → 1603.86] were definitely ATI chips starting to appear on some of the laptops and so on and there was what was
[1603.86 → 1611.56] called a quick draw 3d at the time and um and some games starting to appear real-time as 3d etc and to
[1611.56 → 1616.70] me that was a very interesting field um how you actually create 3d graphics on a computer
[1616.70 → 1622.08] and so I started learning a lot about this and doing wireframe rendering and all software rendering
[1622.08 → 1629.58] then starting to learn how to uh write um real-time 3d rendering but using the low-level drivers
[1629.58 → 1637.72] of the hardware acceleration cards video cards and all of that lent one thing to another and starting
[1637.72 → 1643.68] to build a game and having people drawing etc and so on of the things I did during these two
[1643.68 → 1650.30] years was obviously gained quite a bit of experience of building real-time 3d graphics and um one field i
[1650.30 → 1657.20] was always interested in another field I guess was you know just real-time graphics in general and music
[1657.20 → 1666.08] visualization and just creativity and I just wanted to um experiment with that and poking around and
[1666.08 → 1670.60] what you could do and how you would create motion graphics in a more intuitive way and there were a
[1670.60 → 1677.72] number of products obviously in this field at the time, but they were all to start with um having two
[1677.72 → 1683.00] fundamental limitations I would say the first one is uh was a user experience limitation where
[1683.00 → 1693.10] there were just very complicated to use or um felt not approachable at all um you know like this type of
[1693.10 → 1698.50] clunky very technical UI and so on and the second very important limitation is they were all software
[1698.50 → 1704.26] and so the rendering was as you can imagine very slow, or it had to be small windows and so on
[1704.26 → 1711.14] and I'm talking on the mac platform but the pc platform was not much better um and um so I started
[1711.14 → 1718.80] building prototypes of a 3d uh motion sorry a hardware accelerated motion graphics engine that was very
[1718.80 → 1726.60] very flexible based on open GL at the time, and it was highly modular combined with an interface that
[1726.60 → 1731.78] was not best where you connect you know nodes each not doing a single function and this sort of things
[1731.78 → 1736.90] and then writing a hundred or so of these nodes and starting to have interesting creations and that was
[1736.90 → 1742.46] called pixel shocks, and it was distributed as a public beta it had a website it had a community
[1742.46 → 1748.28] motion graphic artists you know artists in general people doing installation people in the video industry
[1748.28 → 1758.56] uh people doing um animated graphics during um shows uh DJs this sort of uh of events so a niche
[1758.56 → 1764.54] community you could say but uh very interested and active around the such a product that that was
[1764.54 → 1772.52] really um unique at the time and enabled a lot of creativity and freedom in creativity and somehow this
[1772.52 → 1780.76] um got up to uh the attention of uh various people at apple in graphics and imaging and all the sort of
[1780.76 → 1788.34] things, and it happened that at the time I was lucky to be doing my um master's thesis at um at Stanford
[1788.34 → 1797.72] which is about a 10 minutes drive away from uh the apple campus in Cupertino, and so I met with uh you know
[1797.72 → 1803.82] various um directors executives and so on at apple, and then they were really interested in
[1803.82 → 1810.56] this tech and um, and they ended up uh acquiring the all the technologies the IP and all of these things
[1810.56 → 1815.98] and I joined apple and then I built a team there and that product became uh quartz composer which was
[1815.98 → 1823.40] the and still to an extent the standard way of doing motion graphics on OS 10, so the technology was
[1823.40 → 1835.42] distributed with I think well every mac since um 10 4 which OS 10 10 4 I mean which was in 2004 if i
[1835.42 → 1842.14] recall correctly and um yeah all over the place wherever you needed motion graphics on OS 10 if it's simple
[1842.14 → 1852.48] things like screen savers to iTunes visualizers to all the effects in iMovie in into in I mean the
[1852.48 → 1858.46] original time machine uh some of the apple TV the version one uh was running it for a
[1858.46 → 1864.90] number of the animations the um uh the Apple stores reservation system at the time like all the
[1864.90 → 1871.36] animation with the cure that stuff was running it um really like final code pro uh motion like a bunch
[1871.36 → 1878.84] of places were leveraging its power um and big clients of it were internally the hi team which is
[1878.84 → 1884.42] the human interface team, and they were using that as a replacement for director micrometer director
[1884.42 → 1892.16] because it let them be um a lot more creative and do things in real time and um so a lot of the
[1892.16 → 1899.34] prototyping for the um use OS 10 user interface was done on quartz composer a lot of prototyping for
[1899.34 → 1905.98] the iPad you know the iPhone like this sort of things and um and then today even you know
[1905.98 → 1911.98] companies like Facebook still use it extensively for prototyping and creating um interactive mocks
[1911.98 → 1918.38] of um of their products as well as ideal to an extent and so on so it ended up being used
[1918.38 → 1926.38] you know really all over the place um the most um funny or original I should say example I heard of
[1926.38 → 1936.08] its use was um after the iPhone launch an official uh presentation by Steve Jobs um the director of the
[1936.08 → 1942.16] graphics and imaging group kept to me and said um oh I learned that the whole display system to
[1942.16 → 1946.32] you know display the iPhone on a gigantic screen on stage and all of that was actually built on
[1946.32 → 1951.60] um course composer which I thought was cool uh obviously I wasn't in the know of the time for this sort of
[1951.60 → 1957.24] things nor um did I have to be disclosed on this but I thought it was kind of neat that it was also
[1957.24 → 1962.92] used for that that's so interesting to hear this kind of history I think that one of the things i
[1962.92 → 1968.56] love doing about this show is that you know just to paint a little bit of the future of this show we're
[1968.56 → 1973.38] doing here today is you know we're having you on here to talk about get up which uh we'll get into
[1973.38 → 1979.22] much deeper later but as I started to dig into who you are I was like wow this guy's got a lot of
[1979.22 → 1986.96] history in software development and you were at apple in a pivotal time for the company which
[1986.96 → 1992.66] was when they launched the iPhone and that was in like what I think it was 2008 or was it 2007 it
[1992.66 → 1998.74] wasn't yes I think it was announced in 2007 I don't remember exactly yeah like it was at least teased it
[1998.74 → 2004.12] wasn't released I think it was 2008 released yeah there was a gap of a few months before the announcement
[2004.12 → 2009.72] and then the official release uh six months maybe I don't I don't recall exactly yeah it was
[2009.72 → 2016.32] certainly a very interesting time it was a great time to be at apple it was after I joined in um i
[2016.32 → 2023.86] think it was June 2003, so after the turnover had started uh Joe uh Steve Jobs had joined a few years
[2023.86 → 2028.36] before he had done already the iMac and then the iPod and consolidated the product lines
[2028.36 → 2035.74] and he was starting to get you know the seeds were in place um but it obviously significantly
[2035.74 → 2040.70] accelerated later on with um the iPhone and the app store and everything else that came along
[2040.70 → 2046.42] um it was yes a very, very interesting time because apple was not too big I think when I was there it
[2046.42 → 2052.60] was about 14 000 employees total now it's its probably 30 40 000 I mean don't quote me on that but i
[2052.60 → 2058.12] think these are the numbers right a lot of sales people that was when I joined it was just before
[2058.12 → 2065.12] the Apple Store if I'm not mistaken or barely um, so now apple is a ton of sales people um huge workforce
[2065.12 → 2071.64] uh much larger engineering teams and all of that, but you know it's um the department I was at graphics
[2071.64 → 2080.42] and imaging was actually very small it was about 50 people and um minus you know the people who
[2080.42 → 2085.92] were managers even though engineering managers um like I was been definitely coding a lot not just
[2085.92 → 2093.70] managing but still um not coding as much shall we say um a few you know a couple QA people um administrative
[2093.70 → 2101.88] assistant and so on so maybe 45 effective engineers and that small team was responsible for all
[2101.88 → 2108.72] graphics and imaging on the OS excluding uh QuickTime which was a separate team and that means um all the
[2108.72 → 2114.18] 3d graphics so that mean quartz um all and PDF all of that that means all the hardware acceleration
[2114.18 → 2122.08] uh all the Windows server all the 3d graphics um all the colour management system all the image capture
[2122.08 → 2128.64] all the printing um you know everything that touch pixels and so that's so crazy man yeah i mean
[2128.64 → 2138.54] history it's yes it's its unheard of and um in terms of productivity right and apple
[2138.54 → 2144.44] was um i can't come on how true that still is um having been out of the loop for some time
[2144.44 → 2150.96] but apple was um exceptional in terms of and a software engineering division in terms of productivity
[2150.96 → 2157.30] per engineer um it was the results were there, so these are facts right you look at the number of
[2157.30 → 2161.12] engineers you look at the output and the quality of the output and the creativity and all of
[2161.12 → 2170.16] the uh to give you an example my couple examples my immediate neighbour um office space wise was the
[2170.16 → 2179.90] uh creator of core animation right which um was the foundation for uh UI kit which was the foundation
[2179.90 → 2186.76] for the whole UI for the phone, and it would not have existed without it right, and it's that's it that's
[2186.76 → 2194.62] one person extremely talented of course uh my other neighbour was the uh the engineer behind
[2194.62 → 2201.92] core video um and again which was a foundation for uh all the video tech all the modern video pipeline
[2201.92 → 2207.68] that was done on OS 10 and the phone and all the quick time 10 and all of these things
[2207.68 → 2216.60] absolutely critical um he was also the writing a number of drivers uh secretly for um OS 10 running on
[2216.60 → 2224.06] windows boxes was a different story and so it's just that it's just like you walk 10 foot 10 feet and
[2224.06 → 2229.74] you're in the office of the person who writes you know like the two people who write the entire
[2229.74 → 2236.08] um quartz uh engine for 2d rendering on OS 10 and that's if it's things like that so the the the
[2236.08 → 2244.70] magnification um is the leverage magnification was just insane um between people and output and uh the
[2244.70 → 2250.08] ability to learn and so on so that was a very that was a perfect place to be at this department
[2250.08 → 2254.94] specifically because graphics are everywhere so we were having prototypes one of the rare groups
[2254.94 → 2259.90] at apple to have access to a lot of prototypes because you know a new mac comes out well guess
[2259.90 → 2265.84] what it comes with a new um hardware video card that's pretty much always the case and so well guess
[2265.84 → 2271.60] what new drivers things to test and all of this so we would have access to them um or when the camera
[2271.60 → 2276.38] was um eyesight was added to max like all this sort of things then you have to build things for
[2276.38 → 2281.92] that and guess what it's graphics when you have a new app if it's a new iPhone or new i movie well
[2281.92 → 2286.88] guess what they leverage a lot like quartz composer and any other techs and so you need you disclose
[2286.88 → 2292.96] because you need to work with them um so that was a great place to be exposed to a gathering thing
[2292.96 → 2299.30] that were going on and also learn because um i was one of the youngest in that um team at the
[2299.30 → 2305.68] time a number of people were coming from next uh and were definitely veteran of the industry right
[2305.68 → 2312.78] another neighbour of mine was um the creator of painter for example um you know that that that
[2312.78 → 2320.38] very big painting app um like about 10 years ago or so 10 15 years ago um on the mac and then pc
[2320.38 → 2326.58] um so it's like you were tapping into a body of knowledge that was just phenomenal in terms of ability
[2326.58 → 2335.28] to learn, and it's very um, um it was unique on a number of levels and i have not seen that to
[2335.28 → 2340.42] this extent um at other places afterwards in my career and i don't know if that's still the case
[2340.42 → 2345.50] at apple today because you know people move on and then now it's much bigger a lot more engineers
[2345.50 → 2349.84] uh the recruiting bar might have been lowered because you know there is no miracle if you want to
[2349.84 → 2352.82] hire a thousand engineers you can't be as selective as if you want to hire a hundred
[2352.82 → 2358.64] this sort of things when you say painter do you mean Corel painter yeah, yeah okay well before it
[2358.64 → 2365.90] was built by Corel if i remember correctly i think it's just interesting to see that um
[2365.90 → 2373.22] you know a budding software developer decides to really get interested in 2d and 3d graphics uh
[2373.22 → 2379.54] tinkers as you said before and i know that uh, uh tinkering means a lot of things up to a lot of
[2379.54 → 2384.12] people, but ultimately you created pixel shocks which was renamed to quartz composer and then you
[2384.12 → 2390.78] have this history at apple and one of the most pivotal moments of their history and I'm assuming
[2390.78 → 2395.88] only just based on what i see of your resume that it could have been a pivotal moment in your history
[2395.88 → 2401.16] as well um but i think why i say that is that there are so many listeners out there thinking
[2401.16 → 2407.36] well here i am tinkering on x y and z you know here's something I'm interested in whether whatever it
[2407.36 → 2414.62] might be and to see your life and the way that your career has played out and who you worked for
[2414.62 → 2420.66] because of just some true passion and some true interest and you and you followed it and ultimately
[2420.66 → 2426.36] it got you to the places you've been in that time period i think it's just so interesting and so also
[2426.36 → 2431.32] so inspirational to those out there who are like I'm tinkering on this little thing here it's probably
[2431.32 → 2436.96] nothing and it and it's a big deal it could be a big deal it could be a big deal but we all have to
[2436.96 → 2444.10] be to be honest here um commitment is of the utmost importance or importance and um you know
[2444.10 → 2452.26] i think we all start by tinkering on things uh and software um programming is especially
[2452.26 → 2458.78] fit for this it's a lot easier to tinker and experiment obviously in a non-tangible world
[2458.78 → 2463.80] than trying to do that in hardware and so that that enables a lot of creativity and there is pretty
[2463.80 → 2470.20] much no cost uh in terms of money uh if you scrap um scrape a project right and cancel it or
[2470.20 → 2479.50] this sort of things um contrary to hardware again, but you know you have to keep doing it and all the
[2479.50 → 2488.00] way and like bring the project uh to completion and then ship it and then get it to users and so on
[2488.00 → 2498.32] and so on um big shell shocks was um well discovered by apple to an extent right because it was public at
[2498.32 → 2505.16] the time and and and it was functional, and it was um it was a piece of technology truly it was not
[2505.16 → 2510.34] a few things put together like that there was an engine layer and there was an editing layer and it
[2510.34 → 2514.44] was clean separations the way it was built and a bunch of things that i learned through years and of
[2514.44 → 2520.52] course after i joined apple i rewrote the whole thing i think it was twice at least um because you
[2520.52 → 2524.68] learn a lot more, and you're like oh it's suddenly it's a big deal it's a system technology it's going
[2524.68 → 2532.16] to ship as part of every freaking machine uh that apple ships so you have to be careful when you were
[2532.16 → 2538.32] um opening your Mac for the very first time, and you boot it the very first time there's this thing
[2538.32 → 2544.36] that appears that's called mac buddy which is that setup assistant and the very first animation
[2544.36 → 2549.36] mac buddy is running course composer um i can't say if that's still the case anymore, but it was the
[2549.36 → 2554.74] case for a number of years for instance so you have to make sure your thing works and when you start
[2554.74 → 2561.08] having a piece of technology that is pervasive um among all these products um well you know what
[2561.08 → 2566.06] they say with great power come great responsibility so i learned a lot of things there in terms of not
[2566.06 → 2571.46] what to do uh when your technology is everywhere and not like modifying this piece of code uh too fast
[2571.46 → 2577.04] without being careful like this sort of things um but the point i was the main point i was
[2577.04 → 2586.90] making is that tinkering and being enthusiastic and all of that is um is the start um after that
[2586.90 → 2595.24] you do need to follow through and just bring the project to completion that's very important um
[2595.24 → 2601.82] yes that to me that that's critical because otherwise you know the various opportunities that i had
[2601.82 → 2610.60] through the years um would not have had the um uh you know the substrate to appear if each product had
[2610.60 → 2617.42] been like half done or not really functional or not well-defined or this sort of things it's a ton of work for
[2617.42 → 2623.54] each of them well this is a good chance to take another pause when we come back i want to talk about ever pix it's not
[2623.54 → 2629.76] exactly the next thing uh unless uh for some reason you would like to talk about the very next thing
[2629.76 → 2636.68] in your lineage and your in your resume cool iris um i want to jump into some of the things you
[2636.68 → 2640.14] did at ever pix when we come back from this break is that cool with you do you want to go from there
[2640.14 → 2645.06] or do you want to talk about cool iris a little bit uh to kind of wrap up some timeline for yourself
[2645.06 → 2653.58] um you know cool iris was a couple of years after um after apple um I left apple in 2009 um so I worked
[2653.58 → 2660.42] on the I built and led the course composer team at the time we did a couple releases um as part of
[2660.42 → 2665.64] the OS then I figured you know um I'm pretty happy where things at wanted to tackle something new the
[2665.64 → 2673.36] iPhone had just been released um the SDK was announced by Steve Jobs out of nowhere um i very few
[2673.36 → 2678.38] people knew about that at apple so it surprised a lot of engineers like oh by the way in six months
[2678.38 → 2683.02] there's going to be a SDK for people to write native apps with and so it was kind of scrambled
[2683.02 → 2689.12] putting engineers together starting to put that SDK together and at the time like I said it was
[2689.12 → 2695.54] roughly after I think 10.5 had shipped or 10.6 I can't recall exactly and um and and and I figured
[2695.54 → 2698.98] okay well that's a good transition point and the iPhone is going to be big I should probably do
[2698.98 → 2705.12] something in that space, and so I joined the iPhone team and um helped um with the SDK and all the
[2705.12 → 2712.74] the media side of things and graphics and whatnot and um and after the SDK release I ended up um
[2712.74 → 2723.20] leading and well managing um a team that did the web technologies uh and specifically hardware
[2723.20 → 2728.12] acceleration uh in the web browser which was very new at the time and that appeared originally on
[2728.12 → 2735.24] safari on mobile safari to be precise and um you know this idea that you can take your um HTML
[2735.24 → 2741.18] DIVS and blocks and so-and-so on and animate them and have other acceleration for that so CSS transform
[2741.18 → 2747.42] CSS animations hardware acceleration and so that was a dedicated team very senior team and um so I managed
[2747.42 → 2752.28] that team for a year or so if I recall correctly I learned a bunch of things about the web and then i
[2752.28 → 2758.08] figured um okay it's been six years at apple five and a half something like that I would like to
[2758.08 → 2763.34] do something else and I took a sabbatical joined the scholars startup for a couple of years uh that's
[2763.34 → 2769.50] where I started building uh mobile apps um the one that some of your listeners might have used at the
[2769.50 → 2776.46] time was called discover which uh got pretty popular it was um an interesting way uh innovative way of
[2776.46 → 2784.28] browsing and exploring really Wikipedia and done for iPad launched very soon after the iPad was launched
[2784.28 → 2790.46] and uh the main idea there was that um what if we take the Wikipedia content which is encyclopedic
[2790.46 → 2796.16] content so kind of boring and make it like a magazine and uh very nice presentation layout
[2796.16 → 2800.94] the whole thing dynamic and it was completely different from any other Wikipedia clients who were
[2800.94 → 2806.24] just taking the web pages and possibly styling them a little bit with CSS and that's it um it was built
[2806.24 → 2812.46] from scratch and doing a number of um interesting things in terms of innovative in terms of user
[2812.46 → 2818.64] experience and search abilities and um and so yeah the app got pretty popular for some time
[2818.64 → 2824.04] um and so it was a very interesting experience for me, I was in Japan at the time for a couple of years so
[2824.04 → 2828.68] I worked with Japanese designer to build this app, and they bring a completely different perspective on
[2828.68 → 2835.26] design as you can imagine I'm sure very, very interesting experience we built some um uh yeah I mean the
[2835.26 → 2840.48] the templates the style of the app and so on now it would look seriously dated because you know
[2840.48 → 2844.54] six seven years old right it was a different aesthetic then I mean yes, yes but on the original
[2844.54 → 2849.20] iPad you got to imagine like this big screen that's tactile and for the first time you have something
[2849.20 → 2854.48] that looks really, really pretty and uh Flipboard was launched roughly at the same time um like I think
[2854.48 → 2861.92] it was just after or just before and um, and it was you know this idea of presenting content on tablets
[2861.92 → 2868.72] as magazine which became uh quite popular afterwards that was this app was part of the
[2868.72 → 2874.24] like Flipboard of really um kicking the trend I guess or was it the right time at the right place to
[2874.24 → 2880.12] an extent um and so yeah I built a few I mean a couple iPad apps and some other stuff for Clarín
[2880.12 → 2886.96] and um and then ever pix happened yes well cool let's let's pause there for just a minute we're
[2886.96 → 2894.12] going to touch a bit on ever pix when we come back and dive deep into get up the uh the troublesomeness
[2894.12 → 2901.68] I guess of the user experience of using git from the command line uh but we'll be right back so
[2901.68 → 2909.38] hang out I have yet to meet a single person who doesn't love digital ocean if you've tried digital
[2909.38 → 2915.92] ocean you know how awesome it is and here at the changelog everything we have runs on blazing fast
[2915.92 → 2922.12] SSD cloud servers from digital ocean and I want you to use the code changelog when you sign up today
[2922.12 → 2929.06] to get a free month run a server with one gig of ram and 30 gigs of SSD drive space totally for free
[2929.06 → 2936.08] on digital ocean use the code changelog again that code is changelog use that when you sign up for a
[2936.08 → 2940.76] new account head to digitalocean.com to sign up and tell them the changelog sent you
[2940.76 → 2949.14] all right everybody we're back once again uh Pierre it's been so much fun having this conversation
[2949.14 → 2956.22] with you obviously we're here to talk about some of your deeper roots ever pix being a recent company
[2956.22 → 2961.66] that you started based on an idea that you had while you were on vacation and I'm glad you mentioned
[2961.66 → 2966.30] your uh your stint in Japan because that sort of led you to some travel and whatnot and that's where
[2966.30 → 2972.36] this idea came from when you were on this trip but also I'd love to dive deep into get up and
[2972.36 → 2978.64] what's happening there so let's let's talk a bit about ever pix I mean what was this idea to you
[2978.64 → 2984.44] what was it like was this your first company that you built or I guess kind of but not really it wasn't
[2984.44 → 2989.48] your first no it was the second company the uh the very first one was uh that game company
[2989.48 → 2994.96] I think I mentioned a little bit earlier uh which lasted um I think about three years um back in
[2994.96 → 3002.68] 98 or so and um yeah that was a completely different type of company different product
[3002.68 → 3008.92] by far different time frame too yes, yes absolutely very, very different world yeah and uh completely i
[3008.92 → 3014.78] mean the other one we did raise some money, but it was not um it was completely different um
[3014.78 → 3022.74] ever pix was a true startup as you would define it in the Silicon Valley right um in terms of uh how
[3022.74 → 3028.38] it happened in terms of um how it was capitalized in terms of uh what happened at the end in a way
[3028.38 → 3036.74] all this sort of things so ever pix um I guess the easiest way to open this one up is how did it
[3036.74 → 3041.78] come about you were on a trip you were taking photos sharing photos what was the situation what
[3041.78 → 3048.34] where did this idea come from um well you know like a lot of people when they start projects and I'm no
[3048.34 → 3059.00] exception um do it because they have a frustration and ever pix started from that and um the frustration
[3059.00 → 3067.68] was very simple is um we were travelling quite a bit while in Asia and I just wanted to have all my
[3067.68 → 3076.88] photos in one place um on the cloud obviously and having a perfect way to browse them and share
[3076.88 → 3082.36] them, and you know really basic stuff and I figured I tried all the service at the time that's
[3082.36 → 3090.38] back in 2011 uh, so obviously the big ones like flicker and two more esoteric ones, and they were
[3090.38 → 3096.96] not working period um if you wanted to have your photo collection online, and it would work magically
[3096.96 → 3102.64] to use that overloaded term then there was truly nothing everything was a massive pain everything had to
[3102.64 → 3109.12] be done by hand one photo at a time like all this sort of things and um figured okay well in 2011
[3109.12 → 3114.66] with the technology we have and the powerful computer we have we can do much, much better than this and so
[3114.66 → 3122.20] first thing I wrote was really uh um efficient thinking system between photo and I mean aperture
[3122.20 → 3130.20] I was using aperture at the time and the cloud and um you know even things um that little utilities
[3130.20 → 3134.90] that were attempting to do this at the time with to send all your photo library to flicker or things
[3134.90 → 3140.18] like that um they were far from doing it as efficiently as the approach I had taken like
[3140.18 → 3145.14] for instance I was doing some reverse engineering of the photo and aperture databases to directly
[3145.14 → 3150.92] grab everything efficiently rather than requiring people to kind of export the XML and all of this and
[3150.92 → 3158.36] it was a lot more reliable and transparent and um and so a simple problem that you solve right and um
[3158.36 → 3163.60] what happened is I figured okay well that's pretty cool i I want to keep going with that and then
[3163.60 → 3169.12] Kevin poison who I knew from my time at apple because he was on the course composite team
[3169.12 → 3176.02] um turned out to be um not only brilliant in terms of image analysis and software engineering and all of
[3176.02 → 3181.22] that but also be pretty interested in this problem and then I searched for a designer and I met um
[3181.22 → 3185.78] when fan who was at a turning point is carrying away and looking for a next opportunity and so
[3185.78 → 3190.02] the three of us were pretty interesting and that's interested in this space and decided to
[3190.02 → 3194.26] you know iterate and start building something more advanced and that's where like when I said earlier
[3194.26 → 3201.10] it's its a typical in a way Silicon Valley startup is that then um we applied to tech crunch
[3201.10 → 3208.02] disrupt which is one of the big events to uh big startup competitions right and um uh to our
[3208.02 → 3214.02] surprise in a way we got selected and um so they have hundreds and hundreds if not a thousand I don't
[3214.02 → 3219.58] even remember startup supplying and this they pick like 10 or 11 and um so hundreds and hundreds and
[3219.58 → 3223.76] they picked 10 or 11 yeah it's its even more than that, but that was why you were surprised not
[3223.76 → 3227.88] because you were really awesome but because there were so well you know we were very early and yes
[3227.88 → 3235.12] and there were so many and we were kind of rushing to do the application and um and in any case
[3235.12 → 3241.52] um it was selected which definitely gave us a boost, and we completed the company and rushed uh
[3241.52 → 3246.52] before the doing the before the event to make sure everything was aligned and transferred the IP and
[3246.52 → 3255.32] all of this and uh raised a little bit of money um and um and then from there you know we were able to
[3255.32 → 3260.72] present it starts getting attention raise more money iterate learn a lot and so on and so on and
[3260.72 → 3270.62] to not dive too deep into the story um the startup lasted a couple of years and a half and it not it's not a
[3270.62 → 3277.66] pivot but it we all gained a ton of understanding and about the photo space from a consumer perspective
[3277.66 → 3284.48] um I would say a lot more than the competition at the time, and we realized that there was a lot more
[3284.48 → 3289.70] than just a thinking problem and having the same photos everywhere on all your devices that was actually just a
[3289.70 → 3295.32] prerequisite to tapping and addressing the real problem and the real problem as we discovered it
[3295.32 → 3303.76] was what we later called the photo mess and this idea that um people have tens of thousands of photos
[3303.76 → 3308.68] now at least 10 000 it's close to that that was the matrix at the time, and you know suddenly they're
[3308.68 → 3314.28] all over the place among your computers and mobile phones etc, but it's not it's their mess because
[3314.28 → 3318.58] people don't organize them anymore, and you can't blame them for that you can't organize photos out there
[3318.58 → 3323.56] I mean I right it doesn't work my iPhone has 16 000 photos on it, I don't organize those things
[3323.56 → 3333.34] right, and it's not um but so it is a mess and if you like that well sorry I like that term by the
[3333.34 → 3339.80] way photo mess yes well it took a long time to um to uh figure out that term we had to work with
[3339.80 → 3345.42] a seems so natural honestly a pretty talented uh marketing slash positioning expert for that
[3345.42 → 3350.22] and um and to really put because to you as a founder it's clear what you're trying to do but
[3350.22 → 3355.50] you have to convey these concepts to not only the consumers but the investors and um they have all
[3355.50 → 3360.88] sort of patterns and bias and whatnot so it's very important to position your product properly
[3360.88 → 3366.54] and um in any case the know a lot of startups pretty much all startups they were just looking at
[3366.54 → 3370.76] the surface and say well okay it's a mess we all get that let's put everything together in one place
[3370.76 → 3375.30] but now you have one mess instead of multiple messes, and you haven't solved anything and so
[3375.30 → 3382.96] the photo mess to us was more than that is it was the lost opportunity of having this incredibly
[3382.96 → 3389.60] valuable uh treasure of emotion that connects to you personally because it's your photo life
[3389.60 → 3395.42] to a degree that nothing else can touch and not Facebook and your friend status and post and
[3395.42 → 3403.80] no it's your life and having that scattered and out of reach on all these devices and whatnot and
[3403.80 → 3413.66] not connected to you anymore and so the big thing that ever picks focused on is having a very, very advanced
[3413.66 → 3420.70] technological stack uh in terms of image compression in terms of uh syncing in terms of image analysis and
[3420.70 → 3425.40] uh semantic understanding of the content of photos and things that were really advanced at the
[3425.40 → 3431.86] time and that's all tech and so what you do with that is that lets you have very efficiently
[3431.86 → 3438.36] the entire life photo collection of each user in the cloud, and it lets you understand what it is made of
[3438.36 → 3442.80] uh to a degree like these are photos of this you know these are photos of people these are photos of
[3442.80 → 3447.78] trees these are photos taken in cities like all of that based on image analysis uh not even metadata so
[3447.78 → 3454.72] a lot more powerful and uh combined with um insanely accurate deduplication algorithm so that you never
[3454.72 → 3460.18] see twice the same photo independently of recompression artifacts and colour uh shifts in uh due to colour
[3460.18 → 3465.54] space changes between Facebook and the original photo and all of that but what you do with that is you now
[3465.54 → 3471.96] have this unified live photo collection, and you can understand you can understand it, and you use that
[3471.96 → 3480.86] knowledge to uh surface the photos back to the user and this is where the power and the is where it
[3480.86 → 3487.62] clicked for people and this is why ever pix had such a high rate uh of subscription um typical freemium
[3487.62 → 3494.00] products are happy when they get you know three four percent of conversion we had 12 so vastly out there
[3494.00 → 3500.96] right um three times and yeah so that's why the product definitely was a hit with a category of the market
[3500.96 → 3510.42] and um because suddenly you had all this photo life uh being connected I mean it's not exactly the
[3510.42 → 3515.86] best term because on technical, but it's uh you are recreating these emotions when people see again
[3515.86 → 3519.18] their photos, and you can only do that you present the right photos, and you have the entire life photo
[3519.18 → 3524.30] collection etc, etc so the technology stack you need to have underneath to achieve this simple result
[3524.30 → 3530.40] is massive, and it took us you know a year and a half to build everything um to the scale that
[3530.40 → 3534.04] could handle what we were building because we had the live photo collection of each user
[3534.04 → 3540.86] and that was unique at the time um the average user had you know 10 000 photos like I said that is
[3540.86 → 3546.80] massive so ever pix when it know shut down at the end had 400 million full resolution photos
[3546.80 → 3555.14] um we were having peaks um at I think it was eight million photos a day like regularly things like
[3555.14 → 3559.28] that and to give you an idea like flicker was getting at the same time around four million photos a day
[3559.28 → 3565.32] according to their um on numbers so you know a small team of like six engineers was handling a
[3565.32 → 3571.40] huge amount of photos combined with um state-of-the-art uh semantic analysis running on like I think 80 100
[3571.40 → 3579.96] servers I mean massive stuff uh to build that and um, and it did resonate very, very well with a
[3579.96 → 3586.82] category of the market um the trick thing uh the tricky thing is that it is a highly, highly competitive
[3586.82 → 3593.48] space where success is measured in millions of users and um especially which you can only attend
[3593.48 → 3598.18] if you have virality if you look at if you think photo space people are going to immediately say
[3598.18 → 3603.04] photo sharing, and they're going to meet at least they're going to say Instagram and whatnot and ever pix
[3603.04 → 3608.08] was absolutely not a photo sharing I mean you could share photos by definition, but it was not a social
[3608.08 → 3613.22] photo sharing app system it was very personal so it's an it's a different thing, but you get
[3613.22 → 3620.42] um pulled in with the same in the same bucket as a bunch of other startups and so highly competitive
[3620.42 → 3626.68] the bar is very high and so on, and it was very difficult for us to convince investors that we
[3626.68 → 3631.62] were onto something that would go really, really big because they would say well yeah all your metrics are
[3631.62 → 3637.28] incredibly impressive except one which is the total number of users and while some little photo
[3637.28 → 3643.64] app might have like a million active users we had like 50 000 something uh registration and signups
[3643.64 → 3650.34] and all of this and um even if all the reviews were uh really, really good on the app store like all over
[3650.34 → 3654.94] the place and people absolutely love the product and the press, and we got a really high amount of
[3654.94 → 3661.86] price coverage as a matter of fact and um it was just not enough to alleviate the concern of
[3661.86 → 3667.66] of large investors when you're at the series a stage where you typically raise like at least five
[3667.66 → 3673.58] millions and um, and we are raised by then like 2.5 million, but you know the money was gone it was
[3673.58 → 3680.84] spent on payroll on infrastructure and all of these things and uh so ever pix was kind of cut short
[3680.84 → 3687.74] and we would never know if it would have um become something very, very big, or it would have kind of stalled at
[3687.74 → 3693.62] I don't know 100 000 users or something like that because it never really had a chance to um really
[3693.62 → 3698.52] fly after it was built the product was I mean the company had to shut down about six months eight months
[3698.52 → 3705.10] at most after you know 1.0 was really released and uh and things were starting to pick up if you
[3705.10 → 3712.34] um you know a lot of the data pretty much all the data related to the startup um was released as open
[3712.34 → 3718.54] source uh data on GitHub you can just look for ever pix intelligence that's the name of the repository
[3718.54 → 3725.74] and it's all in their like every freaking data set uh reports like it just I had to redact a few
[3725.74 → 3731.98] little things for um obvious um reasons I think there is no data whatsoever from the users as you can
[3731.98 → 3737.48] imagine uh, but there are things like the raw feedback from all the famous investors and VCS in the valley
[3737.48 → 3743.54] except I don't give the names, but it's all in there unedited the uh all our metrics all the um
[3743.54 → 3752.24] um all the data like a ton of data and um because nobody had done that before like to that
[3752.24 → 3759.00] extent like no startup not making it had had released all the data raw unedited for people to
[3759.00 → 3763.68] make their own opinion and look at it and so at the time in the startup world like when I did that i
[3763.68 → 3773.84] think it was very early 2013 um it was um yeah it was very uh popular in the startup world and
[3773.84 → 3780.44] discussed because like I said it had not happened before to see suddenly inside um having such an
[3780.44 → 3788.96] inside view of all the data and before there had been a very uh good and well-written
[3788.96 → 3796.46] article and pretty much unbiased on what happened with ever pix on the verge and um uh which was
[3796.46 → 3801.84] actually um the writers and journalists were a fan of our product and um you know telling the
[3801.84 → 3806.14] story in a very interesting way talking to the various actors the VCS and all of that and that was
[3806.14 → 3811.34] also an article that got very, very popular in the startup world because it was an inside looked at
[3811.34 → 3817.12] what exactly happens when a startup fails like how you get there where you get so good reviews
[3817.12 → 3822.42] from your users, and you raise that money, and you get great investors and this and that and then
[3822.42 → 3826.36] suddenly it's like well it's not gonna work well you know we have to shut down in two months because
[3826.36 → 3832.30] we run out of cash and um so that was definitely a very interesting experience the team was
[3832.30 → 3839.58] very happy with the product and all the insight we get on the photo space, and you know um if you look
[3839.58 → 3846.02] at Google photo for instance today it's it is extremely close to whatever pics was at the
[3846.02 → 3849.48] time and of course they do a number of things better, and we had things we were doing better
[3849.48 → 3856.24] but um it is very, very close a number of concepts you know the um Dropbox um whatever our
[3856.24 → 3860.70] key feature was called flashbacks and Dropbox a year later called released a feature that is the same
[3860.70 → 3866.10] thing and called flashback uh after ever pix shut down um we released what was called uh same feature
[3866.10 → 3870.52] right what was called inside um sorry highlights took us some time to find the term and everything
[3870.52 → 3877.34] this idea of using the uh all our um semantic analysis of the photos to provide a summary of
[3877.34 → 3882.46] your photo life and so that you can navigate very fast and then dive in, and it was all dynamic in the in
[3882.46 → 3887.48] the iOS app and it's things flying around in a very intuitive way, and you know three months later it's
[3887.48 → 3892.70] like google photo came up with what was called highlight, and they define it as finding the most
[3892.70 → 3898.88] representative photos uh which was exactly the same thing uh it was pretty funny and um same
[3898.88 → 3903.60] definition same word uh three four months later whenever that was when they announced google photos
[3903.60 → 3910.22] so we were definitely like um on the right track yeah yeah and a number of things like we're the first
[3910.22 → 3917.08] one to recompress photos and all the VCS were freaking out um like you can't do that people are
[3917.08 → 3921.94] not going to understand that and because we are our own image compression technology that let us do
[3921.94 → 3929.46] 5x close 4 to 5x settings in terms of space at the same quality perceptually right on screen and so
[3929.46 → 3937.94] a photo that used to be one megabyte was now on average 200 um 200 um sorry kilobytes and these are
[3937.94 → 3942.80] massive settings instead of storage so that's the size again you said one five you know four to five
[3942.80 → 3950.52] settings okay at full resolution um the full resolution and and and uh you know complete colour
[3950.52 → 3955.42] correctness everything, and you had to really look at more than 100 to see the differences on the edges
[3955.42 → 3960.50] and so on because you know this is one of the other thing we did we said well photos are taken in JPEG
[3960.50 → 3964.98] JPEG is a very old technology based on you know fast four year transform and all these things and
[3964.98 → 3970.22] goes back like dozens of years, and we can do much, much better today so we build everything on top of
[3970.22 → 3974.84] a variant of JPEG 2000 and wavelets and all custom conversion pipeline all these things and
[3974.84 → 3980.04] the results you know spoke for themselves we had the fastest thinking by a factor of four to five x
[3980.04 → 3984.82] compared to the competition and our storage costs were four to five x lower I mean like I said we have
[3984.82 → 3992.86] 400 million full-res photos it's insane and for a very reasonable storage cost and um but at the time
[3992.86 → 3999.26] people were very concerned about this, but the truth is none of the users cared because we weren't
[3999.26 → 4004.20] hiding it at all we're saying you know we're optimizing the photos and so on, but suddenly they were able to
[4004.20 → 4008.54] have the entire photo life in the cloud which was not even possible before unless you were willing to
[4008.54 → 4013.70] wait an entire month for them to upload right and google photos does exactly that today they optimize
[4013.70 → 4018.52] your photos they don't tell you how but by default with the free tier they cap to 16 megapixels and
[4018.52 → 4024.70] they optimize the photo which means recompressing and um so it's its going to be the standard because
[4024.70 → 4030.02] it's not it's not really scalable otherwise in terms of storage cost and so on so we suddenly did
[4030.02 → 4035.12] pioneer a number of uh of ideas and as a matter of fact google photo released uh in a few days ago
[4035.12 → 4040.46] something the equivalent of flashback excel they call that uh photos to this day or I don't remember
[4040.46 → 4045.14] exactly how to phrase it, but it's exactly what flashback was doing um whatever pics you know at
[4045.14 → 4050.74] ever peak so we were definitely on the right track for a number of these things and um that doesn't mean
[4050.74 → 4054.38] it would necessarily have been a massive success or anything like that because there are a ton of other
[4054.38 → 4062.04] factors um, but it's its at least that's a good outcome that um we did um understand where things
[4062.04 → 4068.46] were going and had uh build the right insight as a team right and managed to execute on a lot of that
[4068.46 → 4072.60] so that was a perfect experience and people are very happy with the outcome even though
[4072.60 → 4079.16] it's a bittersweet outcome for obvious reasons it's clear to see that you're a pioneer that's for sure I mean
[4079.16 → 4086.68] i I mean I'd love love love to dive deeper into ever picks but I do want to move on here in a minute
[4086.68 → 4093.94] to some other topics but of course just to tap on that topic just a bit is I feel like you've been a
[4093.94 → 4098.66] pioneer in so many different ways and what I gathered, and hopefully the listeners may have gathered this
[4098.66 → 4105.24] too and um you know on Twitter or if you're a member in member chat on Slack uh chime into this but
[4105.24 → 4111.08] as you're listening but um I'm thinking like there's a separation between technology and product
[4111.08 → 4117.24] right like from a technology standpoint we're kicking some major butt and also on a product side
[4117.24 → 4124.58] because you had 12 whereas others had 3 subscription rate you know on the free tier, but there's a there's
[4124.58 → 4131.32] a separation of advancement and technology which clearly you're good at and there's an advancement on
[4131.32 → 4138.06] on uh product which is what investors are actually investing in right they don't always see technology
[4138.06 → 4143.52] and they're not always excited about technology they're excited about product and sales and millions
[4143.52 → 4150.40] and metrics and money and revenue that's where the big money is it's really on technology
[4150.40 → 4155.94] only on technology I mean it does happen of course, but it's often you have to package it into a product
[4155.94 → 4163.78] and to solve a problem someone has well this is episode 172 for so for those listening out there we do have
[4163.78 → 4175.14] a link to the ever pix intelligence GitHub repo ever pix e-v-e-e-r-p-i-x is the GitHub user or sorry the GitHub org
[4175.14 → 4182.50] um so we'll have links to that we'll have links to the verge article that uh that you've mentioned Pierre and
[4182.50 → 4189.08] we'll also link up i kind of like even the sparse everpix.com site and I think it's kind of neat i
[4189.08 → 4195.64] think this is a really graceful beautiful way to fail I guess and not in a bad way but like you
[4195.64 → 4203.40] know hit an end of a road and uh and leave the community the consumers whomever might come after
[4203.40 → 4210.00] it with a link to a very clear story from the verge and also all this business data on GitHub I think it's
[4210.00 → 4214.78] a really classy way to do it and I commend you on that um let's let's go ahead and take this
[4214.78 → 4219.68] opportunity to give one more pause here from an awesome sponsor when we come back we're going to dive
[4219.68 → 4226.50] deep into the heart of this conversation which is got UX get up this cool new tool that hopefully it
[4226.50 → 4231.24] seems like you know it's your future we'll see what you say but let's take a break when we come back
[4231.24 → 4238.74] we'll dive deep into that so here we come back century is logging the way it should be a brand
[4238.74 → 4244.00] new sponsor here at the change log we met these guys at gopher con love what they're doing they're
[4244.00 → 4249.28] Gooding their own product, and they're doing some awesome stuff well century is a real-time
[4249.28 → 4254.42] error logging platform that gives you the insight you need into the errors that affect your customers
[4254.42 → 4259.88] they surface your errors helps you gauge severity and frequency and then gives you the information you
[4259.88 → 4268.12] need to get them fixed it works on nearly every platform including JavaScript ruby iOS go python
[4268.12 → 4274.60] and many more and the best part is century is open source you can install and host it yourself
[4274.60 → 4281.28] or you can make your life easier and start a hosted plan at get century.com once again that's get
[4281.28 → 4290.78] century.com all right we're still here with Pierre uh Pierre I feel like I can call you a brother man
[4290.78 → 4297.06] like I feel like I've learned every bit of history I could from you and I thank you so much for this uh
[4297.06 → 4304.44] this deep dive into your history I mean everything from you as a toddler next to an Apple computer
[4304.44 → 4310.82] uh all the way to your history through apple being there when Steve Jobs announced the iPhone and the
[4310.82 → 4317.84] sdk that all the engineers were surprised by on through to uh creating a startup and sadly
[4317.84 → 4325.46] failing at it uh but in a graceful way now what you're doing what are you doing now I'm assuming what
[4325.46 → 4332.86] you're doing but what are you doing now um yeah so after ever pix you know I worked for um, um a car
[4332.86 → 4340.12] actually startup so yet another um still related to software of course but um a different space within
[4340.12 → 4346.64] software uh called automatic which is uh building fascinating uh devices that you plug in
[4346.64 → 4352.54] your car and the whole platform behind it to get the metrics and the real-time data and do
[4352.54 → 4356.88] analysis on that and help you become a little drive a better driver sorry and so on, so there's
[4356.88 → 4363.54] um that's a big deal because cars are not connected to the cloud as of today or barely and so these are
[4363.54 → 4369.12] computers on wheels that are not tapped into internet and there are so many things you can do
[4369.12 → 4375.08] there and so that startup is tackling that that big space uh problem big opportunity problem and um
[4375.08 → 4380.68] so I worked there for some time um help them with engineering this sort of things uh product all of
[4380.68 → 4389.70] this and then um then for personal reason um I quit and um because uh like I was saying for um on a
[4389.70 → 4395.12] personal level you know we're going to have our first uh child and I wanted to uh take a bit of time off
[4395.12 → 4401.46] before that with my wife travel a little more like this sort of things and then uh um and then be you
[4401.46 → 4407.46] know having certain peace of mind when uh when she was born etc uh, but that said I have a problem in a
[4407.46 → 4412.42] sense that it's very difficult for me to stay idle, and so I always poke around with things and
[4412.42 → 4418.88] look at projects and this and that and uh one thing that did puzzle me for some time um both as an
[4418.88 → 4428.94] engineer and as a manager is the is git which is fascinating because it is the standard obviously
[4428.94 → 4434.64] to do today to do uh version control systems, and it has won the war for the time being until
[4434.64 → 4440.28] something better comes it's probably going to be five ten years away at least and um so it's its
[4440.28 → 4449.88] pervasive, but it's its tough for a lot of engineers uh they really have problems with gits um engineers
[4449.88 → 4453.92] who might be junior or engineers who might be very senior, and they get stuck on these things because
[4453.92 → 4462.76] the way you interact with git is very puzzling to say the least um you want to do a sudden
[4462.76 → 4467.50] operation it's one command you want to do the exact same operation but with a slightly different
[4467.50 → 4473.04] variation, and it's complete a completely different command or things are not symmetrical, or it's
[4473.04 → 4478.16] it's weird it's really strange and so you have to build muscle memory, and it takes some time and if
[4478.16 → 4482.58] you don't use git for you know a few months or whatever you might forget how do I do again this
[4482.58 → 4488.36] this specific thing I want to achieve, and then you don't remember and so to me git is kind of the
[4488.36 → 4495.02] the stack overflow uh version control system because what people do in practice is apart from doing a
[4495.02 → 4500.96] commit uh and pushing and maybe fetching every time they want to do something a tiny bit more advanced
[4500.96 → 4507.90] you go to stack overflow you enter your query and so on and so that's that's a fact the among the five
[4507.90 → 4515.16] stack overflow is obviously the um the one place where programmer exchange knowledge uh in the
[4515.16 → 4521.30] entire world by far and so it is very representative in my opinion of the state of things and so among
[4521.30 → 4528.04] the five most voted question of all time on stack overflow three are git questions for basic stuff
[4528.04 → 4533.00] like how do I edit the commit message how do I undo a commit or this sort of things really, really basic
[4533.00 → 4538.58] and I think it's clear by this time the people behind git truly owning it right the git project
[4538.58 → 4547.88] um are not going to tackle this um they add um when you type a command, and it's not very clear what it
[4547.88 → 4554.02] does, or it's a bit confusing they add various prompts and guides and help to tell you maybe you mean this
[4554.02 → 4560.06] or if you want to cancel this operation you just did enter this command, but they're not gonna touch
[4560.06 → 4564.66] the way it works and rename the comments for example and do a clean pass and make it
[4564.66 → 4570.34] a lot more consistent in terms of what the verbs are and how they work and the options and all of
[4570.34 → 4577.26] these things and uh McCready is a lot more consistent in that aspect for instance um, and so I understand
[4577.26 → 4582.34] if is you were to do something like that not only do you need the right people to build a new type
[4582.34 → 4588.08] of command line interface um, but you need to deal with breaking in a way the compatibility with
[4588.08 → 4594.22] everything else and so it's um I certainly don't throw a stone at them for not tackling a
[4594.22 → 4601.48] challenge like that um, but the fact remains that this is far from an ideal situation and uh there's
[4601.48 → 4607.98] a lot of wasted time for my observation with git um and that results in lost productivity for engineers
[4607.98 → 4612.42] and that results in frustration and that results in having typically in the team you know one person
[4612.42 → 4617.20] who's very good at the at git and everyone's going to go bother that person every time there's a
[4617.20 → 4627.24] problem and which is often and so um to me this is frustrating and like I was thinking uh we should
[4627.24 → 4634.74] do something better in the way to interact with git and so um I figured you know the way what's very
[4634.74 → 4643.26] interesting with git is that the the the way people tackle a problem when they're stuck in the
[4643.26 → 4649.10] repository is they ask that person who knows git on the team and that person is very often going to
[4649.10 → 4654.04] go on a whiteboard and draw the thing the state of thing with the branches and say you are here and
[4654.04 → 4658.52] you're trying to do this so you need to do this operation it's going to do that and then that other
[4658.52 → 4663.98] operation and so on, and you see what I mean and then the person go you know do it applying the
[4663.98 → 4667.34] commands, and it works like okay that's cool and then the next day the same thing happens and cannot
[4667.34 → 4672.38] possibly remember anyway because the commands are so esoteric so back to square one, but the point is
[4672.38 → 4678.88] it's about a visual representation and so of course every git client comes with you know little branches
[4678.88 → 4684.14] on the side next to the list of commit that shows you roughly what's happening and so on and um but
[4684.14 → 4694.34] that's that's not the same um, so my idea was okay um instead of manipulating commits per se let's
[4694.34 → 4700.64] manipulate a graph so you see the graph of the repository which is its topology right and how
[4700.64 → 4704.52] the commits are related and the branches and all of that and if I want to delete a commit I select
[4704.52 → 4709.54] the commit and I hit delete, and it works if I want to edit the commit message I click on the commit and
[4709.54 → 4715.46] I somehow trigger an edit option and edit the commit message, and it works um if I want to do rebase I can
[4715.46 → 4718.84] see visually what's happening if I want to do merge I understand it you know this sort of things
[4718.84 → 4726.14] and it's a lot more intuitive because you see the branches um you see what is happening before and
[4726.14 → 4733.78] after and so on, and so I figured um well that would probably work I guess that would work um I should
[4733.78 → 4739.14] try to build that thing and um it should make it a lot easier because a number of times on my own
[4739.14 → 4743.64] personal project I ended up in frustrating situation where I know exactly what I want to do with git in
[4743.64 → 4749.00] terms of merging this there and rebasing and whatnot and I have to then decompose the result into all
[4749.00 → 4755.12] these command line operations what it would be so easy to just have the graph click on the commit in
[4755.12 → 4762.52] question and do that thing yeah so much it gets magic and beauty is hidden behind an um
[4762.52 → 4771.30] uh i I don't want to say just, just complicated but in some ways just very a mysterious way of doing
[4771.30 → 4776.74] things it is and I want to be very clear on one thing which on one thing which is the
[4776.74 → 4784.42] git architecture and design is extremely elegant it's very simple and extremely elegant the way
[4784.42 → 4789.22] the references work the way the commit are done the trees all of that the database format like it's
[4790.04 → 4794.72] it's designed to be it's one of these technologies where the beauty is it's in simplicity and that's why
[4794.72 → 4799.82] it's its really successful and pervasive uh despite you know the terrible command line interface and
[4799.82 → 4804.50] than the existing Mac apps uh can come on well actually Windows apps pretty much same state of
[4804.50 → 4811.06] things but um the existing uh guy clients what they do is they take the command line interface and it
[4811.06 → 4816.04] just wrap it anyway which means you take the clunkiness of the command line interface, and then you wrap
[4816.04 → 4822.48] it into a bunch of dialogues, and you expose every possible option and you put some nice polish on
[4822.48 → 4828.00] top of this and make it look clean, but that's really lipstick on a pig to be brittle it's not solving
[4828.00 → 4833.34] anything you know and you're just compounding problems now not only have the clean efficiency
[4833.34 → 4838.62] because of the way it's its designed, and then you have all these dialogues and check boxes and things
[4838.62 → 4843.14] and sometimes you look at these clients, and they ask you a question do you want to enable this option
[4843.14 → 4847.84] when you do this operation, and you don't even understand what the heck this means um because it's not
[4847.84 → 4856.08] using git proper terms, and it's not clear either I mean so to me, it was just not solved and so
[4856.08 → 4863.12] that's why um I started working on building this concept this proof of concept if you wish and
[4863.12 → 4870.04] there is a really, really good um open source project called libgit2, and it's a c implementation
[4870.04 → 4875.70] of core git um because git itself is not designed as a library you can embed if it's a bunch of it's a
[4875.70 → 4880.44] bit of c code and a bunch of shell script on top of that, and it's not really designed to be used
[4880.44 → 4888.18] by um you know all apps embedding it and so libgit2 is a c API and everything is very clean doesn't do
[4888.18 → 4893.78] everything but uh it does a number of things pretty well and provides a great uh foundation to build on
[4893.78 → 4900.74] top of that and so um git up is built entirely on top of a subset actually of libgit2 where I just use
[4900.74 → 4907.76] libgit2 for say commit parsing and um the merge engine and the diff engine and this sort of things and
[4907.76 → 4915.02] but everything else is rebuilt on top of that subset uh which gives me a much better um I would say
[4915.02 → 4919.54] consistency in the way things work because libgit2 is an open source project that's been going on for a
[4919.54 → 4924.86] few years so it's not um it's not truly spec'd if you see what I mean so you have some parts that work
[4924.86 → 4929.54] a certain way some other parts that work slightly differently and some things that should really be
[4929.54 → 4935.88] subclasses of other things uh from a hierarchy perspective actually not and so on and so on it has a few
[4935.88 → 4940.88] esoteric things and some little his bugs etc, etc so you really need an abstraction layer in my
[4940.88 → 4949.54] opinion and so that you know the GitHub kit in a way that's what I called it um is this it takes
[4949.54 → 4955.02] subset that's very solid of libgit2 and then rebuild everything on top of it in terms of git functionality
[4955.02 → 4962.52] from checkout to uh to merging branches and all of that on top of the subset and then add a bunch
[4962.52 → 4970.66] of layers to do um unique features like unlimited under redo which no other git client has to um you
[4970.66 → 4976.40] know snapshots with like time machine for a git repo which is very, very cool and life-saving um and
[4976.40 → 4983.42] other features like um splitting commits uh just without touching any file on this just select a commit you
[4983.42 → 4989.60] can split the commit and the lines between these files like in a completely fluid way and then just
[4989.60 → 4996.50] commit the result and that's done or um you know unified reflow and a bunch of things that become
[4996.50 → 5000.80] suddenly buildable because you have the right foundation there, and you're not limited by
[5000.80 → 5008.40] the binary git tool that you're trying to wrap you just use you just deal with the git database
[5008.40 → 5014.94] directly and then also gazillion things um yeah that's and so it's a big deal there yeah yeah I mean
[5014.94 → 5019.12] it's not simple when you describe the database directly it's a big deal I think I mean yeah and
[5019.12 → 5024.64] so it doesn't try to call the command line it doesn't I mean git up works even if you don't
[5024.64 → 5028.16] have git installed at all it doesn't really get it doesn't touch it doesn't mess with your config
[5028.16 → 5033.12] settings it doesn't it's a very, very safe app uh and now that it's entirely open source you can see
[5033.12 → 5041.08] how it's done so you can have even more trust in a way um and so the um git up it been a bet in terms
[5041.08 → 5049.30] of saying what if you write a git client that is dealing directly with the database not adding the
[5049.30 → 5055.42] overhead of going through the git command line interface and the clunkiness and has an interface
[5055.42 → 5061.58] that lets you manipulate directly the topology of the repository right um that makes it would that
[5061.58 → 5066.08] make it a lot easier to do all these common operations and people understanding what is happening
[5066.08 → 5070.30] and of course you know the whole thing has unlimited under redo like I said, and it's built modern right
[5070.30 → 5076.28] and it's completely live so you can work in a common line tool alongside uh git up and then your
[5076.28 → 5081.60] changes so show in the graph within like one second latency right you can use them you can use the two
[5081.60 → 5086.22] in parallel and in fact you can sort of like you are that's so that's a very important point that you
[5086.22 → 5094.56] raised with I would consider myself a git power user and i the last thing I would want is um you know
[5094.56 → 5101.48] a play school type of app um it is not what it's about it's a tool done for professional git users
[5101.48 → 5106.36] that is as fast if not faster than the command line if you do rebase in GitHub it's actually
[5106.36 → 5114.20] very often quite faster than a command line and um and um it's faster than a command line very reliable
[5114.20 → 5120.72] and it just gets out of the way at the same time, and it doesn't force you to adopt the whole thing
[5120.72 → 5126.44] it's not a full buying experience so you can use git up purely as a viewer of your graph so if you use
[5126.44 → 5130.24] the command line all the time you open the window next to your terminal you can see what's happening
[5130.24 → 5134.36] in real time in your repo you do your operations, and you can verify at a glance that you're doing it
[5134.36 → 5138.52] right and if you did it wrong go to get up and roll back to the previous step just by using a
[5138.52 → 5143.52] snapshot the whole thing is you know it's very friendly you can use it as little as you want to as much as you
[5143.52 → 5151.02] want um and I also spent a lot of time on building the designing a commit view for um git up
[5151.02 → 5159.80] and the I really wanted a commit view that was faster um than the command line, and so I spent a lot of
[5159.80 → 5165.26] time figuring out a good layout taking obvious inspiration from um existing clients and whatnot but
[5165.26 → 5171.00] also making it very fluid in terms of it's completely keyboard driven so you can very fast select lines
[5171.00 → 5174.92] and press return and stage them and an option returns commit the whole thing, and it sounds simple
[5174.92 → 5183.76] like that, but it's its really fast um in terms of workflow and um if you look at the
[5183.76 → 5189.92] feedback on Twitter I guess that's the primary channel for that but git up it's uh it's been really
[5189.92 → 5196.40] really positive because a number of people realize oh uh it's really fast, and it gets out of the way and
[5196.40 → 5200.44] that's pretty neat, and it gives them a little more comfort the fact they can see all these things
[5200.44 → 5205.46] visually and of course it's not a tool that should do every possible thing in git but um it should
[5205.46 → 5212.60] cover the vast majority of usage scenarios and uh and let you switch to it if you want to or as like
[5212.60 → 5216.46] I said earlier as much as you want which is pretty neat you can or even also a lot more complex
[5216.46 → 5221.50] operations where you're like man i have to google that again going back to yeah like you don't have to
[5221.50 → 5225.92] worry about that or something exactly you want to edit a commit message you select the commit you type
[5225.92 → 5231.60] e edit the message return you're done I mean it's like it beats everything else like it's so faster
[5231.60 → 5238.64] than the command line there's nothing um and um so that that's very different like I said it was a
[5238.64 → 5245.82] bet in terms of user interface uh in tech to an extent how it was built um so I realized it I think
[5245.82 → 5251.64] publicly slowly uh the beginning of the year if I'm not mistaken it took quite a lot of time to
[5251.64 → 5257.44] write there was a lot of code um Gila if you look at the source code is about 30 000 lines of code
[5257.44 → 5262.36] first party code uh which means um you know I mean I'm not counting third party libraries and any of
[5262.36 → 5268.00] this it's just code written for the app exclusively um it's significant like there's a ton of things to
[5268.00 → 5272.70] write in terms of foundation layer and technology stack and all of that stuff to manipulate the commits
[5272.70 → 5277.88] and build the under redo system properly and an atomic transform of the repository references and
[5277.88 → 5284.36] whatnot so um a lot of experiment back and forth a lot of time making the graph very fast it's it is
[5284.36 → 5290.68] GitHub is not designed you know that's one of the things where it has clear limitations um if you try to
[5290.68 → 5296.42] use GitHub on a massive repo which means repo with like hundreds of thousands of commits and dozens of
[5296.42 → 5302.52] thousands of branches and 80 000 files or whatever uh per tree it's it will be slow it is absolutely not
[5302.52 → 5311.20] designed for that um I designed the app for um for the typical repo and uh with a usual like an order
[5311.20 → 5316.94] of magnitude margin which is usually how I do technologies meaning if people uh have like in
[5316.94 → 5321.62] the case of aerobics the average photo collection is 10 000 okay we're going to design a technology
[5321.62 → 5327.50] and our stack to handle 100 000 and that gives us plenty of margin, and we're fine and so
[5327.50 → 5331.92] yes and someone who comes in and has a million photos not going to work that well although at
[5331.92 → 5337.06] ever pics we did have someone with 700 000 photos, and it worked fine and a few extreme cases like
[5337.06 → 5342.34] that um but still so that's not sweet the vast majority yeah yeah it's fine so you know a basic
[5342.34 → 5347.98] rule there um we learned actually discovered in a way but obviously not the first ones at um
[5347.98 → 5354.20] well building ever pics was you just look at the distribution um and you take you say I'm going
[5354.20 → 5359.62] to shoot for the 75th percentile and that's it so I can tell you that from the data I gathered and
[5359.62 → 5366.56] everything that the 75th percentile of repos is definitely around a few thousand commits uh less
[5366.56 → 5373.62] than 10 000 for sure and so by far and so um you build an app that can handle 100 000 commits which
[5373.62 → 5380.56] is what GitHub is, and you know the 75th percentile of branches is going to be maybe 100 at
[5380.56 → 5385.52] most I don't remember the exact number at the top of my head, but it's not like thousands and so again
[5385.52 → 5389.96] if you have a repo uh with a few thousand branches they're going to start getting slow at a few
[5389.96 → 5395.56] places and so on and so on so it was designed to be really really really fast for the 75th
[5395.56 → 5402.08] percentile of repos which is the vast majority of them and um and um that was released early this
[5402.08 → 5408.24] year um I think it got to the top on hacker news and then what featured by uh product hand and
[5408.24 → 5413.96] things like that when it got um a little bit more mature yeah people were intrigued by it and so on
[5413.96 → 5419.82] because it was definitely a departure um and if you know a certain category of people I can't, it's i
[5419.82 → 5424.70] don't it's a bit tricky to measure the adoption um I have a rough idea of the number of downloads
[5424.70 → 5430.24] it's around last time I checked around 50 000 50 80 I mean it's more than 50 000 but I don't know
[5430.24 → 5436.78] exactly because it's with caching and CDN and all of that I only have like a baseline and um, but it's
[5436.78 → 5444.66] not a million right and um, um yeah it has definitely uh thousands of um active users for sure
[5444.66 → 5451.62] at the bare minimum and a very good um feedback on Twitter that resonated to a certain category of
[5451.62 → 5457.40] of git users for sure um I don't know where the project's going to go in terms of adoption you
[5457.40 → 5462.30] know is that going to be a big thing is that going to kind of find its sweet spot and remain at
[5462.30 → 5468.70] a user base of dozens of thousands or something like that and uh or go bigger it's its very
[5468.70 → 5477.38] difficult to say um, um, but we'll see you know it's uh I'm pretty happy with where it's at um I got help
[5477.38 → 5483.86] um in terms of design and some of the user interface um with uh Penang who was my co-founder at
[5483.86 → 5491.32] ever pix and designer um and I also worked with um uh Jason Eberle who was my um who was our web
[5491.32 → 5495.54] engineer at the time with ever pix, and he helped with some of the website and all of that so it was
[5495.54 → 5499.84] a bit of a collaborative process but not as much as something like ever pix of all the projects that
[5499.84 → 5504.88] work on because it was still a very personal project when I've done the vast majority of the
[5504.88 → 5511.18] the coding and stuff um as like I said first um as an experiment but also really a tool that
[5511.18 → 5517.22] I wanted to have for myself a way of dealing with git repositories on a side note of mentioning Jason
[5517.22 → 5523.52] uh it's kind of funny because we don't do the reads for our sponsors live when we actually do
[5523.52 → 5531.10] this show recorded with you but image was actually a sponsor of the show and Jason works at image and
[5531.10 → 5537.24] absolutely was a contributor to the imagex.js library which helps uh this repository you know that
[5537.24 → 5544.88] that's a library there to work with the image API to allow your app or site to uh to work with the
[5544.88 → 5550.74] image API and deal with responsiveness on your app or your site yeah absolutely
[5550.74 → 5558.38] yeah well you know that's one of the thing you um you have in the Silicon Valley as a whole is
[5558.38 → 5562.52] it is a small world yeah it sounds like cliché when you say that, and you don't necessarily believe it
[5562.52 → 5567.42] when you arrive because it takes a long time to build connections unless you're at the
[5567.42 → 5571.64] right time at the right place right, but that's totally by happenstance to that Jason was part
[5571.64 → 5575.56] of this and when I was doing my research I'm like ah that's cool Jason was a part of this yeah and i
[5575.56 → 5581.02] meet people you know, and it's always you end up meeting people you met years back again in under
[5581.02 → 5586.70] completely different circumstances, and you realize people are you know there is this this this um
[5586.70 → 5591.70] mathematical proof that people are only six degrees away or seven I don't remember but
[5591.70 → 5597.08] you know Silicon Valley I'm suspecting it's like two because you always end up talking to people
[5597.08 → 5601.44] who are one degree away from uh people you know and this sort of things there 's's really an
[5601.44 → 5606.44] ecosystem there it's um it's fascinating and Pierre that's exactly why I thought it would be
[5606.44 → 5611.64] interesting to like uh this show is probably a little bit different from our normal shows but
[5611.64 → 5619.14] just dive deep into our guest past because I think it paints a unique position to get up
[5619.14 → 5624.32] and what you're doing with it because of your history in software development like everything
[5624.32 → 5630.30] from all the history we painted during this show to now that this is your interest you know so
[5630.30 → 5638.44] given the success that you've had in the past given the bets as you said on technology um I feel like
[5638.44 → 5643.74] it was really important to sort of dig deep into your past to really get an idea of how serious to
[5643.74 → 5650.28] take get up you know because sure there's get tools out there that promise things like uh the
[5650.28 → 5654.60] get interface you've been missing all your life has finally arrived that's what you say for get up
[5654.60 → 5661.34] right and a lot of a lot of people could promise that, but you've got the history to say that you can
[5661.34 → 5667.00] truly make that statement for get up and the fact that you've got um let me go back to my notes here
[5667.00 → 5674.34] the get-up kit um piece that sits on top of this that interacts directly with the get database you
[5674.34 → 5678.70] know I think that you're taking some unique approaches towards solving this problem and maybe
[5678.70 → 5684.98] you're not far enough now so for the listeners out there thinking ah this is a pretty you know a good UI
[5684.98 → 5689.60] I love how it works they could use some work well you just started in November you know so it's not
[5689.60 → 5694.38] like you've been doing this for a very, very long time yes it's an it's a very young product I mean
[5694.38 → 5703.68] absolutely and uh but it is has it implements the concept I had in mind to a truthful degree
[5703.68 → 5711.16] um in terms of user experience and how it's built and yes it's not you know this is in terms of
[5711.16 → 5718.02] of complexity in terms of engineering and whatnot this is like one two orders of magnitude smaller than
[5718.02 → 5724.36] something like ever pix of course and or course composer and whatnot um, but you know it's
[5724.36 → 5730.64] through the years obviously um like in any trade you learn, and you learn how to do things better
[5730.64 → 5736.84] and more efficiently and so on so get up is yes I apply um a lot of years of learning in terms of
[5736.84 → 5741.82] software development and all of this so it is much better code and architecture than what I would have
[5741.82 → 5747.80] done you know 10 years ago etc so some of that uh hopefully does reflect in the way it works and
[5747.80 → 5755.96] and um the way it's built and um, but it is um yeah it is hopefully going to help that's also what i
[5755.96 → 5761.58] figured you know open source is probably the best for that I was debating for some time is that a
[5761.58 → 5767.66] product you can build um a sustainable business around it and so on there are some examples so it is
[5767.66 → 5774.46] doable uh but what's going to be the scale of it and so on, and it's something where um I did it you
[5774.46 → 5778.34] know selfishly for me obviously first because I wanted to have something I would qualify better
[5778.34 → 5785.94] at least for my pattern of work uh my workflow uh with git and then uh figure out well okay it helps
[5785.94 → 5790.00] other people interest other people can you make a business out of that how many people is that going
[5790.00 → 5794.48] to be, and then you weight that against the amount of work that's needed and support and all these
[5794.48 → 5799.62] other things that come along and opportunity cost etc and I figured you know I like the product
[5799.62 → 5803.36] how it is I'm going to keep working on it but I want to do that in my spare time without
[5803.36 → 5810.06] pressure because I'm pretty happy with it so um open source is probably the best because uh it lets
[5810.06 → 5815.10] it gives it's an active open source project it gives a degree of confidence to people that they
[5815.10 → 5820.20] can use the app because uh it is open source and you check it out, and you build it, and you run
[5820.20 → 5827.28] it on your own so it's not going to go away and disappear and um, and you can judge yourself uh how
[5827.28 → 5831.52] well it's built or not according to your opinion, and you can customize it and all of that to a
[5831.52 → 5837.32] reasonable degree and the um and and and for free it comes with this thing that I called um
[5837.32 → 5843.94] very innovative innovatively you could say a GitHub kit to rapidly find a name right so uh which is just
[5843.94 → 5850.14] all the pieces to make your own GitHub and if you look at the repository there are a couple examples
[5850.14 → 5856.32] in there uh that show in um in a few lines of code really like 20 less than 100 lines of code so
[5856.32 → 5863.30] how to build like two little um git clients uh that leverages all the power of the pieces that
[5863.30 → 5870.14] GitHub has in terms of undo redo in terms of um it has its own text def sorry diff rendering uh engine
[5870.14 → 5877.52] um based on cortex for speed like a lot of a lot of work went into performance um the diff rendering is
[5877.52 → 5882.18] very fast because it's directly on top of cortex for instance um and that makes a difference when
[5882.18 → 5886.30] you deal with uh reasonably large diff, and you scroll through them like all this sort of things
[5886.30 → 5893.18] it's um quite faster than alternative uh git clients in a number of places and because to me that was
[5893.18 → 5899.22] you know it's always satisfying of course to make things go faster um, but it was also required because
[5899.22 → 5903.48] you want the tool to get out of the way you don't want to have to wait for it and I'll give you an
[5903.48 → 5911.56] example there well yes but um I go far with that I'll give you an example um the there are a number of
[5911.56 → 5915.72] dialogues right model dialogues in git ups like if you say I want to create a branch it needs to
[5915.72 → 5921.70] prompt you for a branch name now every possible Mac app is going to show you a dialogue we enter that
[5921.70 → 5928.88] branch name or so that it looks proper in terms of UX you know um a sheet that falls down off the top
[5928.88 → 5935.50] of the window right the title bar these sheets take i the animation is like half a second to say
[5935.50 → 5939.58] whatever by the time the thing is actually on-screen you can start typing it's not too far from a second
[5939.58 → 5945.30] and so to me this is friction that brings nothing, and then you need to wait another half a
[5945.30 → 5952.62] second or so for the sheet to just close and um so if you look at git up the model dialogues are
[5952.62 → 5959.34] actually completely custom um so they're in line in a way so if you type uh b to create a branch or
[5959.34 → 5965.98] e to edit a commit you have this in inline view uh in the map that appears in standardly without
[5965.98 → 5970.44] animation, and you type directly there, and you hit return, and you don't so it's in and out extremely
[5970.44 → 5977.06] fast uh to me that was that's a small thing, but it's its representative of uh the philosophy in
[5977.06 → 5983.24] terms of user interface behind GitHub it's like get you want it to get out of the way really it's like
[5983.24 → 5989.32] go do your operation spend and immediately get it you get it wrong you can undo you can redo and then go
[5989.32 → 5993.08] back to your code this is where you should be spending time right creating things building things
[5993.08 → 6000.18] not fighting git um which is the case for an unfortunate number of of of engineers um
[6000.18 → 6007.42] and so um of course some very advanced people do not need anything like this or uh do not won't see
[6007.42 → 6012.70] the point or some other people uh would prefer a very polished interface like GitHub is still a pretty
[6012.70 → 6018.50] rough interface because that did not put time into um it's clean, but it's not polished in the sense that
[6018.50 → 6026.10] it doesn't have like nice um very polished icons and um, um you know pixel perfect things all over
[6026.10 → 6031.12] the place like it's its pretty much flat plain colours and so on because I put function over form
[6031.12 → 6038.58] there and um there's definitely room to do a pass to make it up to par with uh what you would expect
[6038.58 → 6045.66] from a modern Mac app in terms of you know polish in the UI layer um, but that cannot come at the
[6045.66 → 6052.50] expense of the UX which is the speed and the intuitiveness so yeah there is room for things
[6052.50 → 6057.28] there and some people might definitely prefer something that's more polished even if it's slower
[6057.28 → 6063.88] because it's it makes them feel more comfortable or more mac like app and so on um so it's not for
[6063.88 → 6071.66] a1 I would certainly not pretend that but um it has found its um market fit so far um for certain user
[6071.66 → 6078.02] bears, and so we'll see where that goes from here so it's its open source and I guess anybody who may
[6078.02 → 6085.38] fork it and contribute back needs to know that it's GPL version 3 so anything you contribute um for one
[6085.38 → 6090.50] it's being used by a lot of people so uh which is a notice you give in the README uh it's being used
[6090.50 → 6095.92] by a lot of people so keep in mind that any contribution you make is you know can't be breaking
[6095.92 → 6103.02] um and then that also any work you contribute is GPL version 3 um I think it was kind of interesting
[6103.02 → 6110.06] for us because we run an email that we ship out nightly so every single night we are shipping out
[6110.06 → 6117.18] top star repositories and basically the um you know the things that are happening on GitHub
[6117.18 → 6124.70] um jarred says on steroids I said on crack uh the last episode accidentally, but you know get a changelog
[6124.70 → 6131.34] nightly is essentially what's happening on GitHub every single night top star repositories and uh
[6131.34 → 6137.20] GitHub has been on the top star repositories for us on the charts since August 19th that's the first
[6137.20 → 6142.98] time I noticed it so that was what hit our radar and I say that because there's so many
[6142.98 → 6147.54] people that listen to this podcast and there's so many people that might hear us week to week talk
[6147.54 → 6153.98] about changelog weekly or changelog nightly being our open source radar and in fact that's where this
[6153.98 → 6159.04] show came from and that's where everything you just heard this last hour of me and you talking
[6159.04 → 6166.78] came from us monitoring our own emails you know, so changelog nightly was every bit our open source
[6166.78 → 6172.16] radar when it came to finding GitHub finding you diving deep into your history um and I think it's
[6172.16 → 6180.54] interesting also that um just your history and what you've done for software so far and the fact that
[6180.54 → 6187.26] git is your next focus I'm kind of encouraged by it because I'm expecting big things from GitHub
[6187.26 → 6193.60] um I think it's interesting that you also have the GitHub kit framework where anybody out there
[6193.60 → 6199.48] listening could go and build their very own git UI on top of this now I didn't see that the GitHub kit
[6199.48 → 6205.48] had its own repo is there a plan to break that off into its own repo anytime soon no not at this point
[6205.48 → 6210.18] I mean I'm I'm always worried of moving things around for the sake of moving them around or
[6210.18 → 6217.08] splitting things and whatnot um it's not at this point I mean if it becomes like ridiculously popular
[6217.08 → 6221.84] or something like that they would, it might make sense uh but today I mean they would not really
[6221.84 → 6226.32] be any benefit except now you have two repos you have to look for things in two places, and you have
[6226.32 → 6231.68] dependencies and submodules or subtrees and all of this it's like there's no real benefit honestly
[6231.68 → 6237.56] um but the yeah the GitHub kit is kind of a fun thing it's like well guess what you don't like uh
[6237.56 → 6242.50] how the commit view is structuring in GitHub well you can build your own and it's not
[6242.50 → 6248.66] rhetorical you know um you know it's often like that with open source projects where people say well
[6248.66 → 6255.00] you can always go and modify it yes, but sometimes it's pretty hard to get in and GitHub kit is designed
[6255.00 → 6260.42] as a multi-layer thing where you have some very low level components, and then you have medium level
[6260.42 → 6264.78] components built on the lower level ones, and then you have high level components so you can just use
[6264.78 → 6269.86] the component at the level you want if all you want is a d view that display or stash view that
[6269.86 → 6273.96] display all the stashes, and it's all live and everything just want to put that in some UI for
[6273.96 → 6283.10] your git repo that it's it is uh literally a few lines of code because it's just UI um I mean GI uh stash
[6283.10 → 6288.74] view controller and just instantiate that add it to your window add the view to your window, and you're
[6288.74 → 6294.90] done, and it's all live, and it works and everything um uh but if you want to dive way lower and say i
[6294.90 → 6302.64] want to you just use the diff um rendering uh component well there's a view called uh GI road
[6302.64 → 6307.50] view and that's the low level the lowest level thing it just renders the diff within a view and then you
[6307.50 → 6312.92] have to put it in your own scroll view to scroll and all of these things and um and so that's
[6312.92 → 6319.22] that's a very uh flexible approach where uh you can just yeah rearrange some high level views or
[6319.22 → 6325.18] dive as low as you want and so the two examples that come in the repository in the examples' folder
[6325.18 → 6332.68] show uh some of that uh they use different levels of GitHub kit to demonstrate uh mini apps you can
[6332.68 → 6340.14] build with and uh GitHub kit actually has some uh directory inside GitHub so it's easy yes to sort of
[6340.14 → 6345.52] dive deep into that code if you want to it's not it's not hidden it's easy to find you know the only
[6345.52 → 6350.86] question I have I guess turning uh towards the close of the show um and this is you know not
[6350.86 → 6356.70] prompted from the feedback I got from you on this show but beforehand so some assumptions come
[6356.70 → 6364.40] from this question um and that question is will this and this being got up will this turn into a paid
[6364.40 → 6370.04] product or will it remain free will it remain open source what is the stage what is the plan
[6370.04 → 6376.50] for this um it will remain open source i I cannot imagine a reason why it would change I have a
[6376.50 → 6381.58] number of uh projects that are open source and to me, it's a philosophical commitment when you do that
[6381.58 → 6387.62] uh I've never turned an open source project into a closed source one um I have open source projects
[6387.62 → 6394.06] that are actually paid um I mean sorry that uh are sold or have in-app purchase like coming flow
[6394.06 → 6398.02] is one, and it's entirely open source so if you don't pay for it, you can always download it and build it
[6398.02 → 6403.04] yourself as well as a couple Mac apps on the Mac App Store and so on these two are not however
[6403.04 → 6414.52] incompatible but today I don't see I don't see um a reason to monetize git up right now or uh you know
[6414.52 → 6422.50] in a way that that would be um not be artificial um the comic flow was uh an app that's quite popular
[6422.50 → 6428.58] on iPad to read comics and exists like I mentioned has been existing for a few years uh was free for a
[6428.58 → 6432.14] long time because I built it for myself and I figured well maybe it's going to help some people
[6432.14 → 6439.24] and that's it at some point however uh it gained quite a bit of traction and I rewrote a big section
[6439.24 → 6444.68] of it um all the web server stuff uh which was a core component of the app so that you can, you know
[6444.68 → 6449.10] connect to your iPad running a web server and upload files, and it has web DAV and an interface
[6449.10 → 6452.64] so you can do it from your browser as well if you don't want to use web DAV client
[6452.64 → 6459.56] um it was a significant piece of work and um that became a separate project it was called GCD web
[6459.56 → 6467.56] server which is probably now the most popular um web server for iOS and Mac apps and um, and it's open
[6467.56 → 6472.94] source, and it's BSD or something equivalent so not even GPL it's all good and uh but I figured you
[6472.94 → 6478.64] know that's a lot of work so I'm going to make it that um make that sorry yeah in-app purchase, and it was
[6478.64 → 6483.30] I think it's three dollars or four dollars I don't recall and so uh, but there was a
[6483.30 → 6489.38] real um it was a much better web server than before and the entire app is completely usable
[6489.38 → 6496.16] without buying the same uh you just copy the comics using iTunes directly or through Dropbox or
[6496.16 → 6502.26] something like that so it's not crippled where, and it's just a little enhancement that makes your
[6502.26 → 6507.68] life a bit easier, and then it's an in-app purchase, so maybe something like that will happen
[6507.68 → 6513.50] one day for Rita um, but it's there's nothing like this on the roadmap whatsoever at this point
[6513.50 → 6519.08] all right well we're uh we're definitely coming to the close of the show we have a couple questions
[6519.08 → 6523.22] I'm only going to ask one I know I gave you four different options, but we're going to ask one
[6523.22 → 6529.38] um I think this one is going to resonate a lot with the listeners which is if they've listened to
[6529.38 → 6535.70] your thoughts on you know everything through your history on now to get up and to get up kit and
[6535.70 → 6541.72] what you're doing with that you know what is a what we call a call to arms you know what is if you
[6541.72 → 6547.02] have the ear the listenership of the entire open source world right now, and you want to say hey this
[6547.02 → 6551.90] is what I'm working on if you're interested in this here's how you can contribute what would that be for
[6551.90 → 6567.54] um I think it would be um come explore um and try out an experiment to change the way people interact
[6567.54 → 6578.02] with git and um see if it fits for you and make it become being by continuing to iterate on the
[6578.02 → 6584.44] initial concept and I think it would be it would be like this really to me, it's still an
[6584.44 → 6590.78] experiment in a way I mean if it were to reach a large uh user base then the experiment is valid
[6590.78 → 6596.66] is validated um it is validated right now to an extent because it has a user base, but it's not
[6596.66 → 6603.54] validated at scale and um uh yeah it's so that's why I define it still as an experiment because there's
[6603.54 → 6607.38] nothing else like this it's its a completely unique way of interacting with your git repo
[6607.38 → 6613.88] and there is no client that does this uh from the way it's built to the way it is actually uh it's used
[6613.88 → 6622.08] I can remember um talking to I'm trying to remember it was Tim Caswell I believe and he if you go back in
[6622.08 → 6625.76] our archive I'm going to find I can't recall right now but I'm just gonna talk about it quickly
[6625.76 → 6630.54] there's and there's an episode it was the most recent episode because we've had Tim on the show a
[6630.54 → 6636.80] couple times when he was talking about an uh a Chromebook app that he was building that worked
[6636.80 → 6644.42] with uh building basically a better IDE for um for git and software development a better code
[6644.42 → 6650.74] editor basically, and it was editing the git database directly and the conversation we had
[6650.74 → 6656.12] reminded me a lot of Tim Caswell's work so i I wouldn't doubt that Tim's done some things or is
[6656.12 → 6660.20] doing some things or has some interest in what you're doing so it'd be kind of interesting to see if
[6660.20 → 6668.00] you guys end up collaborating somehow um big fan of Tim his work but um yeah man I mean it was such
[6668.00 → 6674.12] a great time to have you on this show uh to just dive deep into your history and I think
[6674.12 → 6679.24] it was a pleasure thank you what you're working on is very, very interesting so for those listening
[6679.24 → 6688.26] um get up is also a repo, but it's also a web address so if you go to get g-i-t up dot co
[6688.26 → 6694.24] you'll uh you'll find a website with a 90-second video that encourages you to try to get up for free
[6694.24 → 6701.74] this is open source it's free uh this 90 second screencast kind of goes through some three core
[6701.74 → 6708.02] features of get up that that everybody really uh has questions which is editing incorrect commit
[6708.02 → 6712.84] messages who don't do that like you said it's the number two stack overflow question of all time
[6712.84 → 6720.42] undo redo I wish every single day i I had undone and redo on git and also snapshots and then also
[6720.42 → 6726.12] articulating perfect commits because the UI is uncluttered you're able to highlight certain lines
[6726.12 → 6730.12] of code you like to commit and stage, and it's really, really interesting so if you're is you're
[6730.12 → 6735.42] out there, and you're listening to this go to get up dot co there's a nice little map there and then
[6735.42 → 6740.50] down at the very, very bottom of the page there is a button that says download latest release
[6740.50 → 6746.40] and uh maybe you can speak quickly to this which is this right now, and obviously you're a mac developer
[6746.40 → 6752.60] you've been you've said this the whole show not a windows' developer any plans to make this available
[6752.60 → 6758.34] for those windows folks or Linux folks or anybody else besides those who are blessed to use an apple product
[6758.34 → 6766.38] um i not personal plans um, but obviously you know the concepts are not rocket science right and so
[6766.38 → 6771.94] uh if they catch on and get good traction on the mac then um I can certainly imagine there's going
[6771.94 → 6779.08] to be some uh some iteration on the ideas on other platform uh git up itself is not in practice portable
[6779.08 → 6785.10] you know it's its like I was saying earlier it's about 30 000 lines of Objective-C code uh highly well
[6785.10 → 6790.90] except the lower level uh highly tied to the way the mac UI works and core graphics and all these
[6790.90 → 6795.78] things for the rendering and cortex and a bunch of things so it's its one of these things where
[6795.78 → 6802.18] it would probably take as much to rewrite it from scratch and trying to port it um and so it's not
[6802.18 → 6809.88] it's not going to happen on Windows unfortunately it was not intended to be built as um as a cross
[6809.88 → 6814.96] platform app using a toolkit like um qt kit or this sort of things it's um
[6814.96 → 6820.08] it would not have made uh GitHub possible as a matter of fact I think because it's a really
[6820.08 → 6826.54] performance sensitive app when you use it, and you know all these little things matter and so you
[6826.54 → 6832.32] really have to sit on top of the native on top of the metal right the lowest the low-level
[6832.32 → 6839.56] graphic API to uh you know if you draw a graph with um 10 branches and 100 commits it doesn't matter
[6839.56 → 6844.20] what technology you use it's always going to be fast but if you wanted to handle a graph like um
[6844.20 → 6849.02] like I don't know the git repo 40 000 commits and so on and everything loaded in memory and rendered
[6849.02 → 6854.42] and 60 frames per second when you scroll in all possible direction all of this it starts to matter
[6854.42 → 6861.32] um unless you want the GitHub to be only usable if you have like a tower with like an outscore GPU or
[6861.32 → 6869.40] this sort of things so uh unfortunately no, no no plan for a Windows version of GitHub as is
[6869.40 → 6877.04] okay well I figured that uh that might be the exact answer you'd give but I had to ask of course
[6877.04 → 6881.62] and given that this is an experiment I mean this is still like you said an experimental stage
[6881.62 → 6888.12] it makes sense to have that answer um but Pierre I know this has been a long time to sit here and
[6888.12 → 6893.56] grill you on your history and get up and all this uh wealth of software knowledge you share with the
[6893.56 → 6900.38] world I thank you the audience thanks you the sponsors of this show thank you those sponsors are
[6900.38 → 6907.30] code chip I mentioned earlier image a new sponsor of ours digital ocean and another new sponsor of ours
[6907.30 → 6914.24] century uh definitely thank you for your time to sit here and chat with us um for those out there
[6914.24 → 6919.84] listening you can subscribe to this show at changelog.com we're on iTunes we're syndicated
[6919.84 → 6924.78] through five by five we have an awesome weekly email called changelog weekly and another email
[6924.78 → 6930.02] called changelog nightly uh you can get both those respectively at changelog.com slash weekly
[6930.02 → 6935.88] or slash nightly um subscribe to those emails if you want to keep on the open source radar as we do
[6935.88 → 6941.66] but uh Pierre is there any closing thoughts you want to share before we tail off to close the show
[6941.66 → 6948.34] um, um I think I ran out of things to say at this point uh you've been very thorough in your
[6948.34 → 6952.48] questions and everything no I mean uh well thank you very much for having me I mean it was a great
[6952.48 → 6960.76] experience uh it was um my first um uh audio podcast um as an as an interviewee and so it was
[6960.76 → 6966.48] really uh yeah it was a pleasure thank you no problem at all well we do have a ton of links for show
[6966.48 → 6974.28] notes so if you want to learn more about Pete uh Pierre his work his past episode 172 go to
[6974.28 → 6980.86] changelog.com slash 172 we publish all the links all of our notes there so don't feel like you have
[6980.86 → 6986.22] to pull over or wreck if you're driving or whatever to get the links they're all on the web for you
[6986.22 → 6993.54] or right there in your uh podcast client but uh check that out thanks you so much Pierre for
[6993.54 → 6998.08] for joining us and at this time lets uh let's go ahead and call it an in and say goodbye so goodbye
[6998.08 → 6999.00] goodbye
[6999.00 → 7001.38] you
