[0.00 → 13.90] welcome back everybody this is the change log we're a member supported blog and podcast
[13.90 → 17.80] that covers what's fresh and what's new in open source you can check out the blog at
[17.80 → 23.38] thechangelog.com and our past shows at 5by5.tv slash changelog this show is hosted by myself
[23.38 → 31.02] and also Andrew Thorpe Andrew say well hey how's it going fabulous I just want to see it on there
[31.02 → 37.94] that's so awesome you can tune in live to the show every Tuesday at 5 p.m Central Standard Time
[37.94 → 43.88] right here on 5 by 5 and today uh we're joined by two awesome fellas this is episode number 99
[43.88 → 50.62] whoa and we're yeah 99 right yeah, and we're joined by Jeff Lindsey and Jonathan Rosenberg
[50.62 → 56.20] Jeff has worked on projects like local tunnel request bin and get creative or sorry get
[56.20 → 60.72] receive not get creative but I'm sure that's creative Jonathan is one of the two designers
[60.72 → 66.48] behind tent protocol, and together they are building Flynn which is an open sourced platform as a
[66.48 → 70.24] service which is powered by docker so if you've listened to what was that episode number Andrew
[70.24 → 75.80] I think it was 94 but I could that's could be wrong could be wrong could be wrong to don't hold us to that
[75.80 → 79.84] but nonetheless welcome to the show guys yeah thanks great to be here
[79.84 → 86.28] yeah I'm a big fan that was the most dramatic crazy intro ever on the changelog
[86.28 → 91.06] it was a long-winded intro I don't like them I'm never doing it again
[91.06 → 98.48] so Jeff Jonathan you guys have kind of teamed up on this new project it's kind of unique the way
[98.48 → 104.48] you've uh you've done it uh we the changelog gave a little bit of money to we didn't quite give as much
[104.48 → 109.44] as some of the suggestions, but we did give a little bit um but I think it's pretty neat so
[109.44 → 114.32] yeah we want to have you guys on the show talk about what uh an open source platform as a service
[114.32 → 118.56] means and I guess maybe key off of some of the conversations we had around docker too
[118.56 → 123.34] it might make sense uh if you guys just kind of wanted to give us a
[123.34 → 129.04] kind of intro to whom each of you are and your background um then we can talk about some of the
[129.04 → 138.24] other projects you worked on and jump into Flynn sure I'll let Jeff go first oh um I am sort of
[138.24 → 146.36] a rogue engineer um consultant now I've uh I worked at Twilio for a little while but that was sort of my
[146.36 → 154.58] only full-time job um most of the time I'm doing open source stuff um I popularized webhooks uh back in
[154.58 → 163.44] the day and uh um I've done a startup I've done all kinds of stuff mostly writing lots of open
[163.44 → 169.28] source software that nobody knows about your program on Twitter yeah if people don't know the
[169.28 → 175.90] name Jeff Lindsey it probably more familiar with program so on GitHub you have a lot of uh open
[175.90 → 181.16] source kind of behind your name so we'll definitely want to jump into that but Jonathan why don't you
[181.16 → 188.14] give us a little intro yeah um so I've been a developer for a while I started at Shopify in my
[188.14 → 191.88] like professional career before that I did a little bit of like rails consulting here and there
[191.88 → 200.32] and um than i kind of moved to doing this thing called tent uh which is actually a protocol not a
[200.32 → 205.74] piece of software there's reference software uh that implements it and I'm largely interested in
[205.74 → 215.06] all things um related to servers and um and more on the like server side stuff so I built lots of
[215.06 → 220.78] random open source software on GitHub um a while back I did this thing called mailman which is a ruby
[220.78 → 228.98] gem that uh essentially handles incoming email um so doing ruby and go lately oh you wrote that yeah
[228.98 → 235.64] nice why don't you give us a little bit of an intro to tent I think this is neat um not something we
[235.64 → 240.44] talk about a lot on the show uh protocols and things like that but why don't you kind of give us the
[240.44 → 247.62] intro to what tent is and where it came from sure so tent is a protocol for personal data storage
[247.62 → 254.82] and decentralized communication um so it presents just as like a Jason uh protocol on top of http
[254.82 → 259.56] um just kind of using restful verbs etc and essentially what you do is you pass around
[259.56 → 265.06] posts so you have a server that represents you as a user, and then you have applications that talk to
[265.06 → 270.26] that server similar to how you'd like to authenticate an app with twitter you just use OAuth and then your
[270.26 → 275.96] applications can create these Jason posts on the server and your server sends those posts to other
[275.96 → 281.04] people's servers, or perhaps they're private, and it just stores them on the server, and then you can
[281.04 → 286.26] create anything with tent from like Twitter to Facebook you can even do Dropbox because you can
[286.26 → 291.56] store binary attachments along with the posts uh so it's essentially just vented data in a server
[291.56 → 298.52] very simple like restful access to it um, and it's it ends up being really flexible we created it as
[298.52 → 305.44] a sort of alternative to all the centralized platforms um that exist these days think google twitter
[305.44 → 313.78] Facebook etc is it have you seen any you know big projects kind of adopt this protocol so it's its
[313.78 → 321.86] still very new um we are uh we're on coming up on version 0.3 of the protocol um, and we haven't been
[321.86 → 325.68] really doing an adoption push yet because we're still like developing the protocol and sorting out
[325.68 → 332.72] what should be in the 1.0 um so we have like a microblogging app that we've hosted um, and we do like
[332.72 → 339.06] uh tent hosting kind of I've kind of started a startup um on the side uh myself and a few others
[339.06 → 346.40] who work on the protocol and um so we're doing that as tent hosting and then um and others have built
[346.40 → 351.42] uh some like mobile apps and desktop apps that mostly just do microblogging at this point but
[351.42 → 357.48] there's cool new stuff coming what goes into like uh I don't know when you're you know if you're working
[357.48 → 362.16] on a piece of software, and you sit down, and you think you have feature requests or features and bugs and
[362.16 → 367.36] you know different pieces that you have to plan out and build what goes into like an I don't know
[367.36 → 372.96] planning session when creating a protocol um it's a lot of like brainstorming on a whiteboard
[372.96 → 379.74] essentially just kind of like talking through use cases and sorting out it's we try to do lately
[379.74 → 384.24] we've been trying to do like use case driven development where uh we don't actually add a feature to
[384.24 → 391.12] the protocol unless um we actually have an application that either like has a need for it or we are like
[391.12 → 396.84] about to make an application that needs it because otherwise you end up with like weird things that
[396.84 → 401.52] you think you're going to need but that you don't actually need uh and so it's just it requires a lot
[401.52 → 406.60] more thought than your typical software project because you can like to slash out features really
[406.60 → 410.82] easily but with a protocol it's really hard to take features out uh 0.3 was actually a completely
[410.82 → 417.08] breaking release um we were changing just about everything about the protocol from what we learned with the
[417.08 → 422.22] the past I don't know eight months or so of the protocol being in kind of production with
[422.22 → 428.42] a bunch of uh nodes on the network kind of talking to each other the thing that I liked about the
[428.42 → 434.44] project uh when I first heard about it was how kind of it took the vented web ideas and like web hooks
[434.44 → 439.98] as like a core concept in it um because other than things like pub sub hubbub I hadn't really seen
[439.98 → 446.18] those kinds of http callbacks used in um you know more of a standard
[446.18 → 453.70] yeah it's entirely push driven so when you uh create a post like for instance like a status post
[453.70 → 460.44] which is our equivalent to like a twitter post um it actually your server will then push that uh post
[460.44 → 465.68] out via web hooks to all of your subscribers that are permitted to see the post uh so it's its kind of
[465.68 → 470.06] like near real time you wouldn't want to do I am over it necessarily, but you know within
[470.06 → 476.06] a few seconds all of your followers have gotten the posts yeah so it's interesting kind of you can
[476.06 → 482.52] see you know where you two kinds of got together and you both have an as you said uh Jeff you both have a
[482.52 → 488.38] kind of passion for like the vented web so you kind of you wrote the or you I don't know what
[488.38 → 493.58] the best way to put it is but you basically you know popularized the web hook pattern and you know
[493.58 → 500.72] it's been kind of adopted by google GitHub you know like everybody um what kind of sparked you to
[500.72 → 506.84] create that when did you write about that and where did that come from um I was doing a startup
[506.84 → 515.70] at the time called déjà vu, and it was basically a hosted track and SVN but as a product so it wasn't
[515.70 → 521.80] like here's some free hosting or here's like shared hosting with like track and SVN tacked on it was
[521.80 → 531.98] like as a product um and i during that time I was trying to figure out how to expose um SVN hooks
[531.98 → 541.26] uh via http, and it just made sense to do hooks as http, and you put in a URL and then when the hook
[541.26 → 548.16] triggers it would call that URL and then just all of a sudden I realized wow you know i I guess there
[548.16 → 553.46] was one reference before that that was kind of popular which was the PayPal IPN so that was the
[553.46 → 558.54] real only good example I had to go from because nobody else was really doing it and I was like
[558.54 → 562.80] well you can do all kinds of stuff with this you can do you know all kinds of real time it wasn't just
[562.80 → 568.58] that you get real time and that you get push it was that any web developer can handle it like if you
[568.58 → 575.90] can write a PHP script you know you could handle a web hook and um so I started kind of raving about it
[575.90 → 580.08] to everybody and nobody really got it and I just kept doing it um and eventually people started
[580.08 → 586.48] getting it and started using them and seeing oh this is actually really cool um so and then I made
[586.48 → 591.48] a bunch of adapters um I made the first I think one of the first things that I wrote was called
[591.48 → 597.94] mail hooks or mailhook.org I think it's still online, but it doesn't work, but the idea was
[597.94 → 606.86] again kind of like mailman it would do http uh SMTP to http so incoming you'd get you'd go to the site
[606.86 → 613.42] get an email address associate with a URL and then we when email comes in it would do all the parsing
[613.42 → 619.26] for you and post it to your URL like it was a form post which is makes handling incoming email
[619.26 → 624.86] super trivial um no matter what language you're using um you just have to be a web developer and
[624.86 → 631.68] handle a post yeah it's hard to imagine the like modern software development world without web
[631.68 → 635.78] hooks when I mean all the services that you know your typical developer uses are all integrated
[635.78 → 640.96] through these web hooks and I mean it's its pretty cool that you kind of pioneered that that road and
[640.96 → 647.42] you can kind of see then is that you know the idea of that intent is that how you two kinds of got
[647.42 → 651.78] together and started talking about Flynn or did you guys meet each other some other way
[651.78 → 658.62] uh we met through a mutual friend uh who's actually uh one of the co-designers of the tent protocol and
[658.62 → 664.20] um we share a lot of similar interests we've been talking about past stuff for I don't know quite a
[664.20 → 671.40] while now um kind of like we want to do something that looks like Flynn uh and just recently we decided
[671.40 → 680.24] to actually go in and do it yeah Daniel um and I think I met him either at a super happy dev house I think
[680.24 → 686.96] it was a dev house event which don't do really happen anymore, but it used to be big back in the
[686.96 → 695.68] day yeah so uh Jeff real quick we don't have a ton of time to talk about each individual project um
[695.68 → 700.60] and then also talk about Flynn but why don't you give us a little kind of I don't know maybe an intro
[700.60 → 705.20] and just a little bit about a few of these projects um local tunnel being the first
[705.20 → 716.68] um, so a lot of my work revolves around making developer tools um which is an interesting
[716.68 → 721.68] kind of place to be in especially when you kind of have this sort of desire to create
[721.68 → 728.22] consumer-like products you know and where you consider uh ease of use and simplicity and all
[728.22 → 733.54] this stuff and most developers just want to solve a problem um because when I came out with local
[733.54 → 739.02] tunnel um there was really nothing like it now there's a bunch of stuff, but the idea was
[739.02 → 744.60] well you know I do this a lot using ssh tunnels wouldn't it be great if I could just say local
[744.60 → 750.68] tunnel 8000 and expose that port to the internet um I did a bunch of prototypes and finally got a
[750.68 → 757.72] version that worked um and uh it is just kind of slowly started taking off and now there's all
[757.72 → 761.14] you know people building businesses around similar ideas and stuff like that
[761.14 → 768.22] but uh it was just about taking that um a lot of what I do is about usually making
[768.22 → 775.00] a more complicated uh thing simpler and more accessible to people its kind of seems to be
[775.00 → 780.08] like a common pattern like docker I was involved in docker for a little bit in there really early
[780.08 → 785.52] before it was open source, and you know in a way it's sort of about making containers more accessible
[785.52 → 791.56] and more useful to people yeah one of our co-workers actually at uh Adam and mine day job
[791.56 → 795.96] at pure charity is working on something similar to local tunnel called portly, and it's you know
[795.96 → 802.66] same idea being able to publish your local uh you know what you're working on locally so the two me the
[802.66 → 808.02] big probably thing that sticks out about local tunnel and one of the reasons why i never actually
[808.02 → 812.72] covered it on the changelog we talked about we went back and forth a lot is from version one to
[812.72 → 819.44] version two you went from ruby to python yeah would you actually explain well yeah the server was
[819.44 → 825.90] always in python the server was written in it sort of bootstrapped off of SSHD and then had a twisted
[825.90 → 832.44] um kind of server-side component, but the client was ruby, but the client was really just like an ssh
[832.44 → 842.14] client like all I did was wrap an ssh library um and uh I'm I'm not too much of an um I really like
[842.14 → 849.20] building tools that are kind of community agnostic um so you know a lot you know http is something that
[849.20 → 857.52] you know every community knows how to work with um and so it was kind of a weird thing to have like
[857.52 → 863.12] the client in ruby and the server in python um to me, it didn't matter but now I've kind of seen
[863.12 → 868.20] that it is makes a big difference you know when you start a project what language you use and what
[868.20 → 873.66] effect that has on what kind of um responses it gets and what kind of people are willing to contribute
[873.66 → 881.50] to it um so the yeah I started version two that was written entirely in python just because I sort
[881.50 → 888.16] of use python more and I had to write more code because I wasn't I didn't want to depend on SSHD
[888.16 → 892.94] anymore because it was kind of this big complicated black box and people would create tunnels and
[892.94 → 899.06] sometimes it would the SSHD processes would hang and I have no idea what's going on so um I wanted
[899.06 → 904.76] to create a simple protocol and so running more code i you know wrote it in python um and that's kind of
[904.76 → 910.82] been in this weird kind of active development uh stage for a while and a couple of people are running it
[910.82 → 916.54] um it's not actually running right now uh, but a couple of people run their own instances like run
[916.54 → 923.90] scope um they actually recently took one of my projects uh request bin and are sort of taking it
[923.90 → 929.42] to the next level while keeping it open source so it's I'm glad it has like a new home um but what's
[929.42 → 935.02] what's happened actually is a friend of mine has written you know I eventually wanted to rewrite a
[935.02 → 940.02] local tunnel and go so I told a friend of mine that I wanted to do that, and so he went off and kind
[940.02 → 945.72] of wrote a go version of it while we were both working at Twilio, and he kept hacking on it um
[945.72 → 951.00] and eventually he released it as grok and so it's basically the exact same kind of architecture
[951.00 → 958.00] and model as the new local tunnel um except it's actually a lot better so very recently we actually
[958.00 → 961.80] um when people complain about like local tunnels not running, or it's not working for me, I say
[961.80 → 968.34] well go check out grok um because it's what local tunnel should be and we actually just recently um
[968.34 → 972.84] have decided we're actually creating like there's actually a v3 branch in local tunnel now that is
[972.84 → 978.62] basically just going to be grok we are more or less merging projects gotcha so now it'll be
[978.62 → 987.88] written in go so you're a language uh you're a dynamic language adapter yeah I mean I usually pick uh
[987.88 → 993.16] stick with one thing but I'm pretty flexible gotcha you talked about request bin a little bit uh that's
[993.16 → 1000.90] another project you worked on what is request bin so uh you know thinking about webhooks and this
[1000.90 → 1006.20] ideal of like the vented web led to a lot of stuff like local tunnel you know because that was the
[1006.20 → 1010.98] idea is if I write a webhook script it has to be accessible on the internet so if I want to develop
[1010.98 → 1016.26] it locally I need to expose it to the internet so that led to local tunnel another thing was is if i
[1016.26 → 1024.12] use a site that has um you know takes URLs for um for webhook requests I want to um it's actually
[1024.12 → 1028.78] pretty easy to you know they don't really need to document their payload if I can just see some
[1028.78 → 1036.76] examples, so the idea was if I create a site where I can just get a URL to use um and give them that
[1036.76 → 1041.92] URL and they post to it and then I can go to a similar URL to see what they posted in sort of
[1041.92 → 1048.20] nicely formatted way that would become a very useful debugging tool for webhooks it turned out to be a
[1048.20 → 1054.44] more generally useful tool just like local tunnel to just inspect http requests like if you want to
[1054.44 → 1060.00] try client and see what kind of headers it sends by default you can just point it to a request bin
[1060.00 → 1067.58] um and so and I think there's been some similar clones of that too but uh but I'm excited about
[1067.58 → 1071.56] what run scope's going to do with it because they've given a new design and all this great stuff so
[1071.56 → 1077.10] yeah it's cool so it seems like your kind of I don't you may have alluded to this a little bit
[1077.10 → 1082.14] before, but it seems like your kind of write uh the first version of software and then someone else
[1082.14 → 1085.44] takes it and runs with it as the full-time thing when you move on to the next thing
[1085.44 → 1089.48] yeah I mean you kind of have to it's even worse though with services because
[1089.48 → 1095.78] um when you're writing open source software uh like a library or an application you can kind of
[1095.78 → 1100.32] you know write it and get to maybe a stable point, and maybe you've developed a community, and you can
[1100.32 → 1105.00] kind of you know let somebody else become a maintainer and move on um but when you run something
[1105.00 → 1111.84] as a service like a free local tunnel server or request bin or these things um it starts to get
[1111.84 → 1118.04] very difficult because somebody has to run operations on it and pay for it and actually this
[1118.04 → 1123.92] this is actually the very start of the kernel of the idea for my how i sort of started thinking about
[1123.92 → 1130.76] what Flynn is finally was back in 2008 when I was thinking about webhooks and building this kind of
[1130.76 → 1135.64] lightweight adapter services like mail hooks and I made a bunch of other ones one called click hooks
[1135.64 → 1140.44] where um and I think this still works because it's I'm running on app engine click hooks.org
[1140.44 → 1145.90] it's like a URL shortener where you put in a URL to redirect to you, and then you get another URL but
[1145.90 → 1151.92] when you click that URL it also triggers a webhook so for a while I was using that to i wrapped my uh
[1151.92 → 1157.90] subscribe to my blog link in that and then had it post to a service that I previously used to run
[1157.90 → 1162.62] called notify Io that would give me a growl notification when anybody click that link um
[1162.62 → 1170.84] so i um the idea though was I want to run a lot of these services but unlike a regular open source
[1170.84 → 1176.40] project I can't just like hand it off like there's money involved and all this stuff and so the idea
[1176.40 → 1181.18] was things like app engine just blew me away because I was like okay it's a lot easier operations is now a
[1181.18 → 1187.60] lot simpler um the cost model is a lot simpler um you know and more efficient effective cost-effective
[1187.60 → 1193.62] and uh so I was in love with app engine and then I was in love with Heroku and so that led to this
[1193.62 → 1201.16] this love of platform services and then when I was at Twilio we kind of realized the thing was I was
[1201.16 → 1206.42] always butting heads against like what they would let you do for example I say Heroku would be 10 times
[1206.42 → 1210.48] more useful if they just didn't have their http router because then you could run anything you could
[1210.48 → 1215.34] run mail servers you could do all kinds of stuff um because it's a very general platform at its core
[1215.34 → 1224.46] and so that's a lot of these ideas and actually I was hired by uh some friends at NASA um when they
[1224.46 → 1229.52] were working on what became open stack to basically build the original vision for open stack was actually
[1229.52 → 1236.64] not just like an ec2 clone and s3 clone these things it would actually have a platform as a service layer
[1236.64 → 1241.78] but it turned out that it's really difficult to do that first lower level layer and so i never actually
[1241.78 → 1246.10] got to building it but I spent a lot of time thinking about it while I was there so I've just
[1246.10 → 1254.28] been thinking about this platform stuff for years um for a lot of different reasons and uh so i you
[1254.28 → 1259.38] know when I got to the end of my time at Twilio i kind of had some good ideas like I had basically
[1259.38 → 1264.68] sketched out the idea of docker and I just happened to run into Solomon he's like oh you know we're we're
[1264.68 → 1269.80] doing the same so we collaborated on that and um and that was just like a means to building something
[1269.80 → 1277.98] like Flynn yeah Flynn is uh is a pretty neat thing I mean coming from the love of Heroku and
[1277.98 → 1284.96] obviously uh app engine and that I mean getting that experience with a platform um and then I guess
[1284.96 → 1291.80] just serendipitously being involved with Solomon and in the early days of docker um when did Flynn
[1291.80 → 1295.18] come around than I guess when did you guys actually start collaborating on it and thinking things
[1295.18 → 1300.32] through and starting to I guess even flesh out the idea of raising money to make this
[1300.32 → 1306.20] you know kind of community supported but still open source so we started talking about it, I guess
[1306.20 → 1313.12] last year sometime, but it was like this is something we need to do soon um it was we didn't really have
[1313.12 → 1320.20] time to do it at the time and uh just recently uh I was talking to my former employer Shopify
[1320.20 → 1327.52] and I was like hey I really want to do this thing do you want to sponsor it and um Toby CEO of Shopify
[1327.52 → 1334.20] was actually yeah totally um we'd love to sponsor it um, and then we were talking about it more and uh
[1334.20 → 1338.34] we thought that there might be some other companies that would be interested in sponsoring we didn't
[1338.34 → 1343.78] think there'd be that many that would just up and give us cash right out without knowing us um
[1343.78 → 1349.20] we put up a site with the stripe button, and it turned out to get way more money than we were
[1349.20 → 1357.70] expecting um without doing much sales I guess yeah I know right now you're sitting at 108 funded so
[1357.70 → 1362.98] that's eighty thousand seven hundred thirteen dollars of the seventy-five thousand you guys
[1362.98 → 1369.08] intended to raise what was the I guess the impetus around determining how much money to raise um it's
[1369.08 → 1375.10] kind of lowball estimate of what it would cost for us to spend six months building Flynn myself
[1375.10 → 1382.34] mostly full-time and Jeff um close to full-time yeah part-time so you mentioned Shopify you got
[1382.34 → 1388.56] quite a few other um, and we can name them all if you want to but uh just some logos that look nice
[1388.56 → 1394.60] that stand out to me like lab division nebula local web are these friends of yours or they just
[1394.60 → 1398.96] kind of come out of the woodwork and like hey yeah we'll support Flynn a few are friends most of them
[1398.96 → 1404.06] just like found it through the hacker news article and twitter and just out of the blue decided to
[1404.06 → 1409.34] support Flynn I guess after reading the docs, and you know shooting a few emails talking in IRC etc
[1409.34 → 1414.96] yeah, yeah one of the things we talk about on the show a lot is sustainability so I noticed that you
[1414.96 → 1421.32] um you kind of have you know seventy-five thousand dollars it was the goal and uh when will it be
[1421.32 → 1429.56] ready frequently asked question kind of says it's like six months so after six months um in terms of
[1429.56 → 1436.10] you know funding or next steps what's the what's the kind of like the goal for Flynn at that point
[1436.10 → 1442.62] um so in six months we hope to have something that's like runnable as like an internal service
[1442.62 → 1448.96] at companies for perhaps running their internal services like um most of the companies I've interacted
[1448.96 → 1455.20] with um of any size have a bunch of tiny little internal apps um from things like dashboards to
[1455.20 → 1460.76] like employee directories and the whole gamut of other stuff um so it should be able to run those
[1460.76 → 1467.06] types of services basically like your Heroku like 12 factor apps um and then after that well it's just
[1467.06 → 1474.62] one step at a time do you think do you foresee yourself working on this full-time or would you
[1474.62 → 1479.92] you know go to another project type of thing um, so my time is split between this and tent and
[1479.92 → 1484.46] that's all I've been working on and will be working on for the foreseeable future
[1484.46 → 1490.02] gotcha it's cool the second frequently asked question is it open source and your answer is
[1490.02 → 1497.36] 100 it's its really cool to see um how passionate you are to like you know ensure that this is going
[1497.36 → 1502.42] to like to be and remain open source what's the driving reason for that for you
[1502.42 → 1509.68] um the thing is that from what I've seen there are a lot of companies that either need this or are
[1509.68 → 1515.30] building a version of this right now and for it not to be open source for it just to be like one
[1515.30 → 1520.24] company's internal tool really sucks for the rest of us because then we have to build it so I think that
[1520.24 → 1525.86] if a few people step up to build something that everyone needs then that just saves everyone a lot of time
[1525.86 → 1532.82] you mentioned that uh you guys I guess had early relationships with Solomon and docker and
[1532.82 → 1541.10] and since we're talking about FAQs it says how is it related to docker and uh you say that uh you've
[1541.10 → 1545.46] been working with the dot cloud team on docker since before its public launch to make sure it was suitable
[1545.46 → 1551.24] for this project so it sounds like you know maybe early days of docker you knew about Flynn
[1551.24 → 1560.66] yeah I mean so when I was and you know docker has become so much more than I could have ever
[1560.66 → 1566.10] hoped, and you know it's really part of Solomon's vision um, and it just so happens that our visions
[1566.10 → 1572.80] align so much for that tool but i you know really what I wanted when I was at Twilio and I was trying
[1572.80 → 1578.94] to think well we're trying so my second year at Twilio became focused on what we call the platform team
[1578.94 → 1586.88] which we wanted our ideal product of that team to basically be an internal uh platform that the
[1586.88 → 1591.52] rest of the developers could use to build all these services Twilio is actually a very highly
[1591.52 → 1599.66] service-oriented architecture with 200 different types of services um and uh so trying to make uh that
[1599.66 → 1605.96] experience for developers and operations um both consistent, and you know an enjoyable experience
[1605.96 → 1611.36] we wanted something like Heroku we couldn't use Heroku um because we're doing more than hip and
[1611.36 → 1615.90] we want to have control over how the scheduler works because of you know various whatever our SLA
[1615.90 → 1622.72] policies are and stuff like that um so it really became clear we needed to build our own and since
[1622.72 → 1628.08] then I've heard lots of companies um uh like Jonathan was saying that want to do the same thing
[1628.08 → 1633.72] and uh so at the end of my time there I was like well the really first component is probably
[1633.72 → 1639.52] like a Dino manager like something the equivalent of the Heroku Dino which is more or less a high
[1639.52 → 1644.88] level container made for mostly made for services but really once you have that primitive you can do a
[1644.88 → 1650.72] lot of different stuff with it and uh so i kind of sketched that out with the idea that it is part of
[1650.72 → 1658.36] this bigger uh puzzle of this platform um really a framework or like I really like building tools that
[1658.36 → 1664.36] are sort of really kind of independently useful components sort of that Unix philosophy of doing
[1664.36 → 1671.68] one thing that works well um that does one thing well and works with other components and so that was
[1671.68 → 1677.32] kind of differentiating concept that we had going into Flynn is making a system that you know is
[1677.32 → 1685.78] components but isn't just a monolithic set of components um but is actually uh basically a set of
[1685.78 → 1691.26] independently useful components so for example if we get received which is sort of an early version of
[1691.26 → 1697.86] uh you know the type of thing that we would have for like a git front end for Flynn um that's
[1697.86 → 1703.28] independently useful because you can use it to wrap you know any other kind of git based workflow type
[1703.28 → 1709.94] of thing you can push a repository to it, and it'll run a shell script um and so you can use that to do
[1709.94 → 1715.18] all kinds you can use it to put git in front of app engine and be able to deploy to app engine via git
[1715.18 → 1722.72] um, so docker was one of these many components um it was just one of the most important ones
[1722.72 → 1728.72] and so I did go into working with Solomon to make sure that it met these requirements and i you know
[1728.72 → 1734.66] continue to push um still to make sure that docker meets the requirements for this sort of things
[1734.66 → 1740.42] for a system like Flynn and um I hope that that can be replicated for all the components so we can
[1740.42 → 1744.86] find you know if we're building it for Flynn we can get somebody else to use the component for
[1744.86 → 1750.82] something completely different to ensure that it is you know general enough um and simple enough
[1750.82 → 1757.40] you know but simple enough to satisfy both uses so lets kind of fill in the blanks real quick why
[1757.40 → 1762.56] don't you give us like the pitch for Flynn you know the what Flynn is in a sentence for
[1762.56 → 1771.40] somebody that's never heard of it um Jonathan sure uh so Flynn uh is a set of building blocks that
[1771.40 → 1775.98] when uh put together in their default configuration presents a lot like Heroku so you're just doing
[1775.98 → 1783.80] like git pushing apps and then a build pack deploys it but at a lower level it's um managing just
[1783.80 → 1789.62] containers with Unix services in them across a cluster and then each of the building blocks that
[1789.62 → 1796.86] are used Flynn uh used to build Flynn can be um uh replaced or reused um so it's a modular system
[1796.86 → 1803.42] it's extensible um, and it doesn't uh doesn't require you to use it in its default configuration
[1803.42 → 1810.32] so Flynn out of the box you could think of like a Flynn distribution is all these components made
[1810.32 → 1816.62] together made to come out of the box work like your own private Heroku but for example like I said
[1816.62 → 1823.08] Heroku you get you know an http router and maybe that http router supports things like web sockets or
[1823.08 → 1829.64] and maybe it doesn't ours will um but you might want to remove the router completely because
[1829.64 → 1833.18] you're going to be doing other stuff, or you might want to replace the router with your own router
[1833.18 → 1839.34] um, and so we really want to make sure that this is very you know again that component philosophy is
[1839.34 → 1844.92] you can recombine these things or replace things and a lot of these components are running in sort of
[1844.92 → 1852.68] core uh Flynn um you know lower level platform and so a lot of these components run in Flynn itself
[1852.68 → 1857.20] and so you can replace them and deploy them and in the same way you would your apps that you run on
[1857.20 → 1864.10] it got you do you have like a high level you know from 20 000 feet like what the where do you make
[1864.10 → 1870.74] the separation of the modules and you know the like your default set uh you like you said the
[1870.74 → 1874.84] router is interchangeable you can put a different router in there you can take it out or whatever do
[1874.84 → 1879.26] you kind of have the plan for like where what pieces are interchangeable and where you make that
[1879.26 → 1886.04] distinction at we have uh sort of this high level architecture of the problems that we need to
[1886.04 → 1893.26] solve things like the router the scheduler um, and you know the get front end and the management API
[1893.26 → 1897.40] and all these things but um when you get into actually solving those problems you end up realizing
[1897.40 → 1903.92] oh well this can be solved with a simpler component or um, or you know a set of these components and so
[1903.92 → 1909.74] really as you go into those problems try and break them down um into smaller simpler components and
[1909.74 → 1917.36] and problems that you're trying to solve um and so it's kind of an iterative discovery process um
[1917.36 → 1923.28] and so there's both high level and low level kind of concepts of how this breaks down into components
[1923.28 → 1930.88] you know one of our I mentioned earlier in the show that we supported Flynn and we kind of
[1930.88 → 1936.94] immediately blogged about it and featured it on the change log and uh one of the followers of the
[1936.94 → 1942.78] change log mark Helen who is also a platform as a service advocate kind of tweeted back to us and
[1942.78 → 1948.56] said that I guess just the way we worded our tweet like support Flynn to help make it uh pass open
[1948.56 → 1955.64] source, and he replied uh there are at least two perfectly good open source platforms as a service uh
[1955.64 → 1962.94] projects why do you act as there's none and then also on your uh on your FAQs there's a
[1962.94 → 1967.72] mention of cloud foundry open shift and a couple others that are mentioned and can you just
[1967.72 → 1972.86] kind of contrast what the differences are I guess between what Flynn aims to do and what others have
[1972.86 → 1982.10] tried to do or are doing um so from the beginning like for example app engine it came out, and it was
[1982.10 → 1989.10] super useful, but it's very constrained so this paradigm of web apps and Heroku and dot cloud
[1989.10 → 1995.26] actually because they kind of in parallel um sort of follow the same development path in a lot of ways
[1995.26 → 2002.78] generalize that so it's really about just running a Unix process as a service um, but they're still based
[2002.78 → 2008.96] on deploying web apps and all their conventions, and you know the http router and all this and um
[2008.96 → 2014.86] and even though they've made progress app engine is still you know very much focused on web apps and
[2014.86 → 2019.76] they've kind of hacked a bunch of extra features to make it a little bit more, but it's still like
[2019.76 → 2025.02] the way it was designed originally is still focused on web apps and I think a lot of the open source
[2025.02 → 2032.96] projects that are trying to solve this platform service uh problem are sort of similar you know they
[2032.96 → 2041.82] are still geared a little bit too much um towards web applications um to be useful for me um another
[2041.82 → 2048.70] one because I've done cloud foundry consulting and um you know there's just you know they uh I don't
[2048.70 → 2055.02] want to speak you know for all of them, but you know many of them are uh they try and break them down
[2055.02 → 2061.14] into components, but they're still this sort of monolithic uh beast that's very complicated, and you know each
[2061.14 → 2066.16] of the components isn't very well documented, and it becomes very difficult to deploy the thing and so
[2066.16 → 2072.66] that kind of user experience is something that we want to um you know try and make uh much better so
[2072.66 → 2077.92] the out-of-the-box experience is much better, but you still have that hackability you can drill down
[2077.92 → 2084.08] and actually you know pretty easily kind of see how everything works together and start hacking it and
[2084.08 → 2091.04] taking it apart um and doing whatever you want with it and so to me actually it's not
[2091.04 → 2097.14] so much about building a platform service um it's about building uh tools for building your own
[2097.14 → 2102.12] platform or your own district really it's a toolkit for building distributed systems it sounds like the
[2102.12 → 2106.64] the keywords that you're saying is like a set of like and you just to use your words in your FAQ
[2106.64 → 2112.16] best you say a set of modular components it seems like you're really like you'd mentioned you're more
[2112.16 → 2117.56] focused on the individualized components and how that makes up what actually is a platform as a
[2117.56 → 2123.60] service much like Heroku without the um you know some of the pieces that have kind of upset you or
[2123.60 → 2128.04] didn't kind of put some blockers in front of you with using Heroku like you wanted to before
[2128.04 → 2133.60] yeah so it's really taking a lot of the technology that was developed in building platform services
[2133.60 → 2140.44] and um making them more accessible, but then you know decoupling them so that you can use them for
[2140.44 → 2147.04] different things like container technology was really uh I think developed by platform services
[2147.04 → 2152.00] companies like ROK and dot cloud, but it turns out when you break that out into a component like
[2152.00 → 2156.92] docker it's immediately useful for all kinds of other stuff that has nothing to do with running a
[2156.92 → 2162.90] platform service and so there's all this great stuff in there that's useful for um for building your
[2162.90 → 2170.86] systems that we want um people to kind of you know take advantage of so right now just the spec
[2170.86 → 2177.08] is on GitHub and I know you're past 100 mark in terms of meeting your minimum funding goal but
[2177.08 → 2182.94] um you know we talked earlier too about six months a certain time frame and whatnot but
[2182.94 → 2190.02] when should the community begin to see a repo pop up and commits happen and uh I guess start
[2190.02 → 2195.82] seeing progress for uh towards what flint's going to be within the next few weeks for sure um
[2195.82 → 2200.04] we're currently just kind of talking through some like high level stuff just getting our bearings and
[2200.04 → 2205.20] then we're going to start diving into components really soon talking about the flint spec um is that
[2205.20 → 2210.78] written in sand or written in stone oh uh sand that's actually just like a bunch of bullet points we put
[2210.78 → 2217.34] together like even before we put the flint.io site together um it's pretty old at this point
[2217.34 → 2225.14] so when people kind of started to support this project financially what do you think it was well first
[2225.14 → 2231.10] this we've talked about like we said sustainability, and we've had people talk about different you know
[2231.10 → 2238.02] uh funding models or revenue models for open source projects whether it's you know we've talked
[2238.02 → 2243.18] about we had GDP on the show at one point or we've had you know people like sidekick like mike
[2243.18 → 2247.72] Perrin with sidekick where he releases it open source but then build some you know professional
[2247.72 → 2255.06] features on top of it and charges for like a monthly um like a monthly rate what did
[2255.06 → 2260.16] drive you to kind of go with the pay up pay ahead almost the kickstarter-issue without the minimum
[2260.16 → 2270.42] goal model for flint so funding open source is a really hard problem um most projects are small
[2270.42 → 2274.94] and some ask for donations but most don't see more than twenty dollars maybe a year or something
[2274.94 → 2281.80] um so we looked at we looked to the kickstarter model um there's been a few open source projects
[2281.80 → 2286.62] that were funded quite successfully, and we decided that there are actually companies that were
[2286.62 → 2291.96] interested in funding rather than individuals we've had lots of um individuals uh sponsor flint but the
[2291.96 → 2297.88] the vast majority of the money came from corporate sponsorships companies that want to use flint um
[2297.88 → 2304.96] so that's that's what we targeted essentially yeah I think the lowest tier was actually fifteen hundred
[2304.96 → 2310.76] dollars um so it's very clearly targeted towards um companies um wanting to sponsor
[2310.76 → 2317.06] and that sort of makes sure that you know we're solving a problem for business so that all our
[2317.06 → 2322.86] sponsors are sort of going to be and be able to participate in conversations about and I've actually
[2322.86 → 2328.54] been going out to a lot of uh companies and just talking to them in person um to learn about
[2328.54 → 2334.46] their requirements and stuff like that so I can, we can kind of continue to refine um the design of
[2334.46 → 2338.70] this thing and make sure that we're building something that's uh simple but is able to
[2338.70 → 2344.32] satisfy all these requirements so since we're I guess on the subject of sustaining I guess in
[2344.32 → 2350.86] in some capacity you've got the funding you guys requested I guess what's the plan in the future for
[2350.86 → 2356.44] I guess sustaining this past this point like is it go back to these original sponsored
[2356.44 → 2362.02] companies or back to the community and say yeah I guess what's the plan to I guess sustain
[2362.02 → 2370.98] um I mean so we uh we could raise more sponsorship um we actually have talked to a lot of companies
[2370.98 → 2377.66] um much more actually uh you know much more in depth about the technology than some of the people that
[2377.66 → 2383.18] have sponsored so far um that are very willing to sponsor and were about to, but we were sort of
[2383.18 → 2389.08] like well you know we reached our goal we'll come back to you later um, but they're the and they
[2389.08 → 2393.46] were very willing to you know let us know you know they're just very excited about the project and the
[2393.46 → 2399.12] approach and all this stuff to be able to help us out because they're seeing all of these
[2399.12 → 2405.20] problems and I'm just I'm super surprised just how many companies um internally are sort of realizing
[2405.20 → 2411.00] that what they want is sort of an internal platform service um you know and again that's sort of
[2411.00 → 2417.30] one of the things that differentiates us is a lot of these open source platform services uh passes
[2417.30 → 2424.94] are made to be run as a pass you know service um not you know they've got billing and quotas and you
[2424.94 → 2430.08] know all this stuff kind of built-in so that it's made for someone to kind of deploy and resell or
[2430.08 → 2436.22] something like that, and we expect that at some point people might add that to Flynn, but really we want
[2436.22 → 2442.10] to um you know a lot of internal use cases don't need any of that so we're just kind of avoiding
[2442.10 → 2448.26] all that for Flynn um and so it's kind of a different use case um yeah our target customers
[2448.26 → 2454.18] are the operations teams at the medium startup medium to small size startups that are kind
[2454.18 → 2459.96] of struggling with just the amount of work that it takes to deploy each new application um so
[2459.96 → 2465.76] it's an it's almost like the project has a different customer than the existing um projects in
[2465.76 → 2470.68] the same space right look can you pause there for a second because uh there's one quote I guess
[2470.68 → 2474.80] another praise for Flynn that I think needs to mention and I guess it kind of maybe expands a
[2474.80 → 2479.76] little bit more on this which is uh from Tobias at Shopify he said the future of operations is to
[2479.76 → 2485.10] function like a product team that services the developers of the company as a client so when you
[2485.10 → 2492.04] kind of flip down and says it's like um you know you're targeting towards I guess the Shopify's and
[2492.04 → 2495.42] people like that are wanting to support you guys, but it's in an effort to help their
[2495.42 → 2500.14] development teams and their operations teams better interface between DevOps and developers
[2500.14 → 2509.84] yeah I think um and at Twilio that was the idea was we wanted the platform team to basically
[2509.84 → 2519.22] build a self-serve platform in much the same way that so many startups use ec2 where you just have
[2519.22 → 2525.12] this great you know layer of abstraction um, and they take care of like people kind of you know
[2525.12 → 2531.42] are you know arguing about the value of the cloud and stuff like that um but the stuff
[2531.42 → 2539.06] that they do and abstract away for you is incredibly amazing um and so the thing is though is that
[2539.06 → 2544.72] there's no kind of layer of abstraction between ec2 and a Heroku, and so we kind of want to open up
[2544.72 → 2552.46] that spectrum um of you know abstractions and capabilities for operators and um to the benefit
[2552.46 → 2557.10] of both operators and developers because Heroku is a great developer experience right
[2557.10 → 2563.90] kind of talking about Heroku you have another project called dock that you worked on um I noticed
[2563.90 → 2571.58] yeah or Dou I want to say dock because of docker but yeah it's OK uh so I noticed I think Flynn
[2571.58 → 2577.58] kind of came about what would you say like a month ago maybe is that right yeah and then the initial
[2577.58 → 2584.92] commit on Dou was two months ago so what was the kind that was this was Flynn already in mind when
[2584.92 → 2591.76] Dou was started, or you know kind of how does that relationship work out well you know like I said I've
[2591.76 → 2599.84] been thinking about this for ridiculously long time and since even before docker existed and uh i actually
[2599.84 → 2607.38] gave a talk with Solomon at I think gluecon and I wanted to give an example of how you could use
[2607.38 → 2612.66] docker to build a platform service and by then docker had been developed enough that it did actually do
[2612.66 → 2619.88] most of the work um to actually make a pretty simple kind of Heroku like service so uh in six hours I was
[2619.88 → 2627.06] spent like the day before the talk actually building the first version of Dou and um the idea was that it
[2627.06 → 2634.18] was super simple right because docker does mostly heavy lifting and trying to just like uh do the
[2634.18 → 2638.52] the simplest thing possible that works with the constraint that it's you know it only works on a single host
[2638.52 → 2644.66] you know it's not a distributed system um, but it turns out that actually is pretty useful a lot of
[2644.66 → 2653.82] people want like their own little mini Heroku and uh so Dou started um I released Dou uh a little
[2653.82 → 2658.18] while after that because I had added virtual hosts because that makes it a little bit closer to
[2658.18 → 2664.32] like Heroku where you have a subdomain for your app and um and I just started working on that on the
[2664.32 → 2671.32] side for fun, and it got a lot of attention and uh that sort of uh it was happening separately
[2671.32 → 2678.18] slash in parallel to uh talking with these guys about working on Flynn and uh so a lot of the same
[2678.18 → 2683.34] philosophies and actually a lot of the components that we would be using for Flynn will be pulled into
[2683.34 → 2689.54] Dou and Dou kind of um gives us an idea of some of the components that you know we need for
[2689.54 → 2698.46] Flynn for example Dou uses get receive to handle um pushing via get, and so we know that we uh get
[2698.46 → 2705.38] receive is not ideal for building a distributed scalable system, but it solves the problem well in Dou for a
[2705.38 → 2711.82] single host however if we take that same component and re-implement it in go um, and you know make it a
[2711.82 → 2717.28] little bit more general and fitting for uh for a distributed environment um it's more or less the
[2717.28 → 2721.78] same component but works for Flynn, and then we can run it on a single host, and it works for Dou
[2721.78 → 2728.26] so Dou for me is just is going to continue to be a single host more or less like a single host
[2728.26 → 2734.34] distribution of Flynn um and so for me, it's kind of a prototyping ground for ideas for Flynn
[2734.34 → 2742.34] um but yeah it's kind of different goals single host gotcha so this is going to be
[2742.34 → 2750.80] uh kind of I don't know maybe like supercharged version of Dou or the Dou plus
[2750.80 → 2757.04] yeah actually and the read me for Dou i sort of when I was telling explaining what it's not you
[2757.04 → 2762.54] know it's not multi-host it's you know not made for a multi-tenancy sort of thing it's its uh
[2762.54 → 2769.02] I said maybe those are features for super Dou and then um it just so happened that uh Flynn is
[2769.02 → 2774.74] more or less what super Dou would have been there's actually some other great projects um
[2774.74 → 2780.66] built around docker, and it's on hacker news today somebody told me um Deus which I actually saw
[2780.66 → 2784.92] quite a bit before because they're sort of in the docker community um they're released and so
[2784.92 → 2792.22] they're another platform service um built on docker um, and already we're sharing components
[2792.22 → 2799.14] like I wrote for build step for uh for Dou, and we'll use it for Flynn is this piece called
[2799.14 → 2804.50] build step which is maybe more accurately something like Heroku stack because it's basically a builder
[2804.50 → 2810.46] and runner for Heroku build packs in docker, and so they're using that for their platform service
[2810.46 → 2817.96] and I'm using it for Dou, and we'll be using it for Flynn can I ask maybe uh not so much an I guess uh
[2817.96 → 2822.72] I'm not really sure how this question will be sounding I guess, but you say things like uh in
[2822.72 → 2830.58] the areas of I guess for Dou ideas for improvements where you say Heroku-ish commands I mean I know
[2830.58 → 2834.46] Heroku is a for-profit company, and they're doing some awesome stuff in open source too but
[2834.46 → 2840.78] does any of this cross lines does anybody call you and be like hey stop doing what you're doing
[2840.78 → 2844.58] we don't really want to support that because maybe Heroku wants to protect their market share
[2844.58 → 2855.24] well I've been friends with a lot of the Heroku uh engineers um for a while and I use them you
[2855.24 → 2860.72] know I'm sort of a power user so I go to their offices fairly frequently when I do stuff like um i
[2860.72 → 2865.58] made an I made a web service that you actually put on app engine that lets you register new Heroku
[2865.58 → 2870.12] accounts because I was working on a project that needed to let you create like infinite number of
[2870.12 → 2876.18] apps so I needed to be able to create you know a bunch of user accounts and uh I do stuff like that
[2876.18 → 2884.12] or one time I made a script that uses um Heroku's ability to run arbitrary commands with their run uh
[2884.12 → 2890.32] with their run command and use that to deploy uh something to itself so it could kind of self-deploy
[2890.32 → 2895.16] I'm doing just all these weird things with Heroku and so very often they'll kind of like pull me in and
[2895.16 → 2899.66] and want to talk about it or see what's going on I've actually been you know a lot of the times
[2899.66 → 2904.20] there will be like product uh development discussions like you know you're trying to do
[2904.20 → 2908.78] this so you know how does this sound you know, and we actually have this kind of useful conversations
[2908.78 → 2916.32] but um I've heard though that some people in Heroku is pretty big or sort of like um are very
[2916.32 → 2921.88] kind of curious about uh some of the stuff that I'm doing but the majority of them actually don't know
[2921.88 → 2927.58] so I think it's possible potentially I know this is just being hypothetical of course but
[2927.58 → 2932.72] um maybe that Heroku will be like oh man I love what you guys are doing with Flynn
[2932.72 → 2935.96] will acquire you and I know you're not really a company yet but like
[2935.96 → 2944.02] the thing to remember is that and support it is that Flynn is um is targeted to run internally so
[2944.02 → 2949.72] Heroku is kind of this service that you pay for and runs on ec2, and you have no control over
[2949.72 → 2954.42] whereas we're targeting Flynn at companies that need to run something internally for whatever
[2954.42 → 2960.40] reason there's a variety of reasons from security and control to you know just um like latency reasons
[2960.40 → 2965.64] not Heroku's not in a data centre that they want to be in etc so we're we're making Flynn for
[2965.64 → 2971.48] essentially the people that don't use ROK or can't use ROK for whatever reason they're adjacent
[2971.48 → 2977.30] they're not in direct competition I don't think it's actually the same story as open stack um because
[2977.30 → 2983.48] open stack came from NASA and it basically our group of people uh like a ragtag team were trying
[2983.48 → 2989.64] to like make NASA cool again we're doing all this kind of neat web apps for missions to have um more
[2989.64 → 2996.26] participatory kind of um citizen science sides to them, and we want so we kept thinking well we want
[2996.26 → 3000.86] that we want more people to do this in NASA so it'd be great if we had a platform for them to do this
[3000.86 → 3005.80] or even just use existing stuff like app engine the problem is its government stuff and the
[3005.80 → 3011.04] government requires you to uh to use your own you know they have to use their own hardware so that
[3011.04 → 3015.98] basically forced us if we want to do this cool stuff into building more or less our own ec2 and
[3015.98 → 3022.36] that's sort of where um nova came from an open stack that's I guess it's no different from saying
[3022.36 → 3026.38] you know GitHub enterprise versus GitHub uh GitHub is not gonna they're not competing their
[3026.38 → 3035.68] their different markets I get it now yeah so when the flynn.io launched um it said that
[3035.68 → 3041.16] the minimal viable product will be ready in two to three months I'm not exactly sure of the timeline
[3041.16 → 3045.36] but when can we expect uh a MVP for Flynn this fall
[3045.36 → 3054.46] cool yeah and then so once that comes out are you going to give a lot of time for feedback or is
[3054.46 → 3061.20] you just plowing right through towards the production version no we definitely um
[3061.20 → 3066.08] uh love feedback, and we get a lot of feedback already just kind of architecturally in the
[3066.08 → 3072.08] approach from the various companies that we talk to and are sponsoring um but we definitely
[3072.08 → 3077.54] have kind of a set and actually a kind of more philosophy behind a lot of this, and so we're
[3077.54 → 3083.20] trying to in the process of documenting sort of our um you know the philosophies on the decisions
[3083.20 → 3088.68] that we make you know about all this kind of componentized philosophy and as well as a set of sort
[3088.68 → 3094.84] of like technical guidelines that we're going by and once we publish those then um hopefully it'll make
[3094.84 → 3100.42] um suggestions and stuff like that a lot more productive because we can easily say well we're
[3100.42 → 3106.28] not we can't do that because you know we've decided philosophically that that's you know not for us
[3106.28 → 3112.50] um that the cool thing is that you know if people don't like the main Flynn distribution how we're
[3112.50 → 3117.24] organizing things hopefully that a lot of the components can be used for them to sort of remix it into
[3117.24 → 3125.48] something that you know is more what they need gotcha I think it's like interesting almost funny that
[3125.48 → 3131.80] just the spec which is like this one little read me you said just bullet points has like 520 stars and
[3131.80 → 3142.04] nine forks yeah I mean like do you get I don't know I don't see any but do you get like do people take
[3142.04 → 3146.56] this and say here's a know I see this as one of the general features, but you should change
[3146.56 → 3153.48] it to that or why are they forking this um there's people who have opened issues I don't I haven't seen
[3153.48 → 3160.20] any pull requests yet that would be entertaining yeah that's that's interesting cool well it's a
[3160.20 → 3166.72] definitely a product that we will be keeping our eyes on because this is something that um you know
[3166.72 → 3173.34] we talk about a lot that we have like well you know for instance we have pre-processors we have
[3173.34 → 3179.70] sass right which like boils down to you know a cool way to do CSS or a powerful way to do CSS and
[3179.70 → 3186.88] and at some point you think um you know you the levels of abstraction will seem to stop but
[3186.88 → 3192.28] I don't know Flynn just it gives you another use case of a higher level abstraction to you know
[3192.28 → 3197.74] one step further than docker and I think that maybe this is where it stops at, but it's an it's an
[3197.74 → 3204.36] exciting interesting product that we will be watching for sure me too hey well hopefully you're
[3204.36 → 3211.92] watching it the uh so if you're so if you're new to the uh new to the changelog then we just want to
[3211.92 → 3217.56] let you know that we ask these three questions and seeing as we have uh two guys on the show with us
[3217.56 → 3222.56] this time we'll give a little extra time, but we have three questions every week to our uh guests
[3222.56 → 3229.32] and so we'll go ahead the first question and I'll ask you Jeff is um for a call to arms for Flynn
[3229.32 → 3236.32] as obviously right now Flynn is not in um you know uh it's not on GitHub so it's not necessarily
[3236.32 → 3242.32] something that the community can actually contribute code to but what would you like to see people or
[3242.32 → 3252.46] your sponsors or anybody kind of do Flynn related right now um well I'd, so there is Dou which is
[3252.46 → 3259.08] sort of in a sense kind of it's very different project but um there's still a lot of the same
[3259.08 → 3264.54] philosophy behind it so if you're interested in this sort of thing definitely check out Dou and play
[3264.54 → 3271.30] with it and uh definitely I think preparing people because everybody should be able to take
[3271.30 → 3278.70] advantage of this um Flynn and so it'd be great to have more people involved and contributing and so
[3278.70 → 3285.14] one of our um one of our sort of technical guidelines is to most of our components are written in go for
[3285.14 → 3292.40] various reasons that we'll document so um and docker itself is written in go and so if you need an excuse
[3292.40 → 3299.04] to learn go, and you want to participate in this grand vision of Flynn um definitely uh take advantage of it
[3299.04 → 3304.02] and start playing with go and some of the components that we already have out there are you know
[3304.02 → 3308.62] open source, and you can start playing with them and learning go but go is really awesome so
[3308.62 → 3314.54] maybe that can be my call to arms yeah talking about go we're actually going to have Andrew from
[3314.54 → 3320.40] google on next week to talk about go so it should be a pretty fun show what about you Jonathan
[3320.40 → 3330.00] um I'd say uh pretty much the same as Jeff for Flynn uh also uh tent uh if you um take a look at the
[3330.00 → 3335.60] protocol docs and find it interesting love always love to see new like applications being built and
[3335.60 → 3342.46] we're we're always around in IRC to answer questions etc so um have a look at tent and um start thinking
[3342.46 → 3347.98] about what you can build when your communications platform is decentralized instead of centralized
[3347.98 → 3356.88] and you have a nice platform like Flynn to build those on yeah um kind of new question that we've
[3356.88 → 3363.72] been asking and I'll ask you first Jonathan if you weren't doing this now this is pretty new so this
[3363.72 → 3368.04] might be meaningless to you but what would you be doing if you weren't doing what you're doing right
[3368.04 → 3373.20] now if I wasn't doing open source I would probably be a film editor I actually went to school for a few
[3373.20 → 3380.14] years um for filmmaking and TV broadcasting that kind of thing so I like that stuff too okay what
[3380.14 → 3387.42] about you program I have I struggle with this idea that I have too many interests and one of them
[3387.42 → 3394.66] is film so uh I'd love to start doing film but i sort of prioritize based on how well it fits into my
[3394.66 → 3400.64] lifestyle so um outside of programming stuff I do a lot of music stuff and I'm trying to make more time
[3400.64 → 3408.12] like producing music I actually do like um metal and hard rock and stuff like that and um but
[3408.12 → 3412.66] otherwise I'm really into indie games um but I can't do indie games right now because it's just more
[3412.66 → 3420.56] programming so I don't want to like to spend my time not programming gotcha yeah one of our uh
[3420.56 → 3425.24] one of our friends of the show that we have on the show a lot Kenneth writes he's uh he is also into
[3425.24 → 3431.44] music it seems like that's a kind of popular trend right now is for uh developers who are who
[3431.44 → 3436.64] kind of do some release on the side with music which is kind of a neat little you know thing that's
[3436.64 → 3443.94] going on yeah I told Kenneth we should start a band that's awesome um I want to give you a chance to
[3443.94 → 3449.46] kind of give us an uh a shout-out to someone personal or somebody that you look up to so we call it the
[3449.46 → 3457.56] programming hero on the changelog so who is your programming hero Jeff um I have a ton but if i
[3457.56 → 3462.90] were to pick one to give a shout-out to right now it'd probably be uh Brett victor um so I met him
[3462.90 → 3468.00] recently, and he gave he's given a lot of amazing talks and is doing a lot of really amazing work
[3468.00 → 3475.62] and um he's he definitely falls into the realm of the type of person that inspires me so shout out
[3475.62 → 3483.68] to Brett victor gotcha and what about you Jonathan um I have to pick one uh shout out to rob pike uh
[3483.68 → 3491.10] co-creator of the go pro ring language and uh he made utf-8 which is also a really nifty encoding
[3491.10 → 3497.82] thing that everyone uses um I'm a huge fan of his no nonsense uh design aesthetic for the software that
[3497.82 → 3504.46] he makes and uh his one-liners on mailing lists are hilarious yeah that's good choice um funny story
[3504.46 → 3509.84] go is really you know like 20 years old because he wrote a language called new squeak that is
[3509.84 → 3515.64] basically go with kind of more FORTRAN looking syntax you can look up a Google tech talk on him
[3515.64 → 3521.68] talking about concurrency it's actually he shows new squeak and pretty much everything in it is the
[3521.68 → 3528.52] exact same thing in go yeah he's been contributing to the uh to the community for quite some time I think
[3528.52 → 3534.00] he was one of the designers on limbo that's right too yes that's correct yeah he's a good guy cool guy
[3534.00 → 3538.14] yeah it's kind of a huge throwback to our early days but rob pike was on the show on episode number
[3538.14 → 3546.22] two so we whoa oh yeah I heard that yeah that was like uh the super early days I guess not really
[3546.22 → 3549.84] uh early days of go because you know you just mentioned what you mentioned so
[3549.84 → 3555.96] not really early, but it was like around the same time the release of go as it is now
[3555.96 → 3561.28] yeah he's a he's a good example of a programmer that works with um sort of great
[3561.28 → 3568.28] sort of philosophy behind his work yeah um so well cool yeah I know we can certainly go
[3568.28 → 3573.00] on for quite a while talking about this a lot of fun conversations and topics we can
[3573.00 → 3577.74] certainly dive deep into, but we do have to wrap we try to keep this show to around an hour so
[3577.74 → 3580.78] sometimes we go over sometimes we're a little under but either way
[3580.78 → 3587.96] um I do want to mention two things before we do go so uh we're just launching an every Thursday
[3587.96 → 3591.54] newsletter from the changelog so if you want to sign up you can go to the changelog.com slash
[3591.54 → 3596.10] newsletter uh every Thursday in your inbox you'll get the latest from the changelog we're also ramping
[3596.10 → 3602.16] up um our contributors as well so expect more on the blog uh we do have our t-shirt in so you can
[3602.16 → 3607.72] hack in style with your very own changelog t-shirt you can go to the changelog.com slash store as well
[3607.72 → 3614.14] so if you don't have that t-shirt you are wrong but uh Jeff Jonathan thank you so much for
[3614.14 → 3618.20] the awesome work you're doing an open source and taking the time to come talk about it on this show
[3618.20 → 3623.32] today uh let's say goodbye thank you it's great being here see you all later see ya
[3623.32 → 3625.32] you
[3625.32 → 3627.32] you
[3627.32 → 3629.32] you
[3629.32 → 3631.32] you
[3631.32 → 3633.32] you
[3633.32 → 3635.32] you
[3635.32 → 3637.32] you
[3637.32 → 3639.32] you
[3639.32 → 3641.32] you
[3641.32 → 3643.32] you
[3643.32 → 3643.38] you
[3643.38 → 3643.46] you
[3643.46 → 3643.88] you
[3643.88 → 3643.90] you
[3643.90 → 3643.94] you
[3643.94 → 3643.96] you
[3643.96 → 3644.02] you
[3644.02 → 3644.10] you
[3644.14 → 3645.18] you
[3645.18 → 3649.14] you
[3649.14 → 3649.22] you
[3649.22 → 3649.78] you
[3649.78 → 3650.18] you
[3650.18 → 3650.28] you
[3651.24 → 3651.72] you
[3651.72 → 3652.80] you
[3652.80 → 3653.54] you
[3653.54 → 3654.02] you
[3668.36 → 3668.90] you
[3668.90 → 3670.02] you
[3670.02 → 3672.00] you
[3672.00 → 3672.02] you
[3672.02 → 3672.08] you
[3672.08 → 3673.18] you
[3673.18 → 3674.02] you
[3674.02 → 3674.10] you
[3674.10 → 3674.12] you
