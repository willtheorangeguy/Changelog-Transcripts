[0.00 → 15.32] welcome back everyone this is the change log and I'm your host Adam stekowiak this is episode 134
[15.32 → 22.28] jarred and I talked to the core team behind dot net core that's Microsoft dot net core effects
[22.28 → 28.32] can't believe it we have Microsoft on here talking about open source of all things we were surprised
[28.32 → 34.28] to definitely a great show we have rich lander Emma land worth and Arun Gupta on the show great
[34.28 → 39.06] great conversation about Microsoft and open source and lots and lots of fun we had some
[39.06 → 45.76] awesome sponsors for this show code ship top towel and rack space helping us make this show possible
[45.76 → 50.84] we'll talk about top towel and rack space a bit later on the show but our friends at code ship
[50.84 → 57.74] always amaze us continuous integration and delivery as a service you can release more frequently get
[57.74 → 63.00] faster feedback and build the product your users actually need a simple push to a repo runs your
[63.00 → 68.40] automated test suite and configure deployments from a simple deployment to Heroku to a complex
[68.40 → 74.38] deployment pipeline set up for large infrastructures all that can be set up with ease using code ship
[74.38 → 78.92] it integrates easily with GitHub or Bitbucket you can get started today with their free plan
[78.92 → 85.06] setup takes just three minutes make sure you use the code the changelog podcast again the changelog
[85.06 → 92.40] and with that code you'll get a 20 discount for three months on any plane you choose head to
[92.40 → 98.08] codeship.io slash the changelog and tell them we sent you and now on to the show
[98.08 → 111.60] all right everybody we're joined back today we got a fun show lined up today we got myself here got
[111.60 → 117.62] jarred here we got rich lander we got emo land worth we've got maroon Gupta uh those guys are from the
[117.62 → 124.40] dot net core team over there at Microsoft and I tell you this is maybe an unprecedented day
[124.40 → 129.36] for us because in the history of this show we've only had one show on dot net and that was on nougat
[129.36 → 134.68] um we didn't expect to ever have anyone from Microsoft on the show talking about dot net being
[134.68 → 139.50] open source so I guess that's uh hands in the air on that one but um let's let's go around the table
[139.50 → 144.16] here real quick and give some intros so rich let's start with you emo and then maroon uh after that in
[144.16 → 154.94] no particular order sure um I'm rich lander as uh jarred said and or sorry Adam um and uh I've been at
[154.94 → 164.12] Microsoft since 2000 I've been on the dot net team since uh 2003 and I've shipped each version of dot net
[164.12 → 170.22] since 2-0 it's uh been fascinating being on the team and building all the technology that we've
[170.22 → 176.16] been shipping to customers that whole time but uh this last little bit where we've been uh getting
[176.16 → 181.88] our open source project ready has been definitely the most exciting time in that that whole period
[181.88 → 194.50] all right, and we got uh emo yeah so I joined Microsoft in 2010 and uh I was a customer for a
[194.50 → 202.78] very long time I was basically on the first on the first beta is basically since 2002 I believe
[202.78 → 208.32] and uh so when I joined the uh the team I had a very much uh you know focus on dot net from a customer
[208.32 → 212.42] perspective and I'm super excited to see some of the things happening that we did over the last
[212.42 → 216.92] two years in particular releasing more stuff on new bit as well as open source that we're doing now
[216.92 → 224.38] so it's really great times for me as well gotcha all right maroon how about you uh hey guys I've been
[224.38 → 232.10] in Microsoft for the last 10 years mostly around dot net um I'm part of the dot net team which is doing
[232.10 → 238.30] the open source work around dot net core interestingly I'm also part of the team that's helping set up
[238.30 → 245.40] dot net foundation so it's very exciting for me from both fronts uh you know seeing back last 10
[245.40 → 251.18] years definitely very exciting and a new path um, but it's you know something we're all very excited
[251.18 → 258.26] about so jarred I guess I'll open this uh this show up with probably the most important question we have
[258.26 → 264.50] here and to you guys too I mean congrats on taking this shift towards open source I think you'll probably
[264.50 → 270.34] see, and you probably have seen already the benefits of just the open source community
[270.34 → 275.40] interacting with you know a wider developer base maybe than you're typically used to with feedback
[275.40 → 280.72] and issues and GitHub and pull requests and all this you know collaboration that goes into building
[280.72 → 286.26] open source software these days so let's let's maybe ask the biggest question here which is why
[286.26 → 292.78] open source and maybe even a tail-off question which is why now uh how about I'll answer the first
[292.78 → 300.38] question I think this is rich right yeah sorry this is rich uh I think the big um key motivation behind
[300.38 → 309.66] um why open source is that um we want to just reach developers who um we can't typically reach
[309.66 → 317.18] with a pure kind of closed source uh offering and um there are plenty of folks out there that uh open
[317.18 → 324.30] source is a key requirement and uh we want to make them uh our customers as well um so that that's
[324.30 → 331.24] really that's really the big piece do you want to tackle the second one email why now yeah so the so
[331.24 → 336.54] why now question is interesting so like in the blog post that we published uh two weeks ago we basically
[336.54 → 344.76] uh sketched open source as effectively two pieces the first piece is uh cross-plaid which is uh if you think
[344.76 → 349.02] of any sort of serious cross-plaid projects, and they all have one thing in common in their open
[349.02 → 354.56] source, and it's not that open source is the only way to do cross-plaid work, but it's uh probably the
[354.56 → 360.52] most um sustainable way of doing it because you can very easily incorporate other people that care
[360.52 → 364.82] about certain things that you either can't repo yet or you just don't care about this yet so a good
[364.82 → 369.00] example is if you look at Linux for example when Linus to was started this whole project he
[369.00 → 374.00] still didn't care about 160 architectures uh for him to target right but over the years
[374.00 → 378.44] certain people jumped in that cared about certain architectures, and then you know the breadth of the
[378.44 → 383.20] project significantly increased over time right and that's that's why it cross-plaid I think of uh
[383.20 → 389.22] if you look at botnet the mono community is a very strong um force there so it would be very
[389.22 → 394.86] you know idiotic from our side if you wouldn't um uh you know incorporate those communities and make
[394.86 → 399.54] it is easier for them to work with us the second part of it is uh if you look back there for the last two
[399.54 → 403.44] years we're basically doing more and more agile delivery and uh from our point of view
[403.44 → 408.00] agile delivery is really the key of uh you know making sure that the right things happening
[408.00 → 412.96] uh in a reasonable amount of time because the more complicated the project is and the more
[412.96 → 417.66] design up front you perform the higher the chances are you get something wrong at some point right and
[417.66 → 422.64] our project is now you know almost 15 years old if you consider the initial work time before it
[422.64 → 428.06] went published uh public, so there's a lot of complexity in the product itself so by us being able to
[428.06 → 433.06] deliver things in an agile fashion that also means we get customer feedback way quicker uh we also
[433.06 → 437.66] have happier customers because when you file a bug you live long enough to actually see the bug being
[437.66 → 442.14] fixed as well so if you consider this you know in the previous time having like three years release
[442.14 → 447.10] cycles uh it was often very frustrating for customers and as I said I was a customer for a very
[447.10 → 454.94] long time so I filed a bug in 2004 that got uh closed as uh loan fixed in like 2009 or something so
[454.94 → 459.68] I can totally relate to this uh, uh problem that you just you know don't get feedback from Microsoft
[459.68 → 464.30] so agile really gives us this way of doing it, and we ship uh packages on you get for over two years
[464.30 → 469.30] now on our team and from our point of view open source is really just the ultimate version
[469.30 → 474.02] of being agile right because you're essentially every time you commit something it's immediately live
[474.02 → 479.78] and in theory it's consumable uh modular any bugs so we get feedback pretty much in real time so
[479.78 → 484.54] instead of having a customer discussion every two years, and we ship a beta we can actually have a
[484.54 → 488.48] discussion with the customer in real time and that's why open source now makes a lot more sense
[488.48 → 494.56] than it did you know maybe 10 years ago seems like quite a sea change from you know Microsoft's
[494.56 → 501.04] previous stance um as you guys said in your blog post it was you know kind of you open source to
[501.04 → 507.92] universal acclaim trending on GitHub anything Microsoft does makes a big splash but I'm interested in
[507.92 → 515.84] how this change came about inside the company because uh it seems like such a change in strategy
[515.84 → 521.88] that usually those things have to be sold up a chain um whose idea was it and how long has it been
[521.88 → 528.02] like you guys trying to convince people or are you the ultimate decision makers it's clearly all emo's idea
[528.02 → 529.16] definitely
[529.16 → 536.80] good one yeah so I think on our side we're all very interested right now that basically say open source
[536.80 → 542.52] was my idea yeah but I think that you said like it's a strategy change I would agree that the strategy
[542.52 → 546.90] changed but I don't think it should be you know a massive surprise I mean if you look over
[546.90 → 552.42] the over the last I don't know probably longer years I mean dot net open source is not this you know
[552.42 → 556.20] the first open source project that Microsoft did right the very first open source project was
[556.20 → 561.26] the windows installed the XML and that's not you know fairly long time ago uh asp.net is open
[561.26 → 566.50] source for quite a long time now and uh they've managed c sharp and BB compilers was in open source
[566.50 → 571.82] six months ago, so there 's's clearly a progression where Microsoft became um I think
[571.82 → 576.08] better at realizing what open source actually means right I mean there's like you know these bad quotes
[576.08 → 580.76] from balm alike 10 years ago or something about GPL but if you realize like how we run with
[580.76 → 585.66] open source now I think uh it's clear that it's not a shift that happened overnight um and there's
[585.66 → 591.76] for example the shift designer of c sharp he had a lot of experience with open sourcing uh as part
[591.76 → 597.02] of the typescript initiative that was open source from the first day, and he really absolutely liked
[597.02 → 601.40] the experience that that open source designing the open interacting with people in real time
[601.40 → 605.74] was ringing because you could reach developers that we just could never reach before right it's really
[605.74 → 611.28] about the conversation and the you know the sheer innovation speed of which you can
[611.28 → 615.38] take the feedback and make something out of it um and I think in general like if you look at
[615.38 → 620.24] Microsoft around I mean uh you know Alma had this uh vision statement of devices and services for
[620.24 → 625.26] example and especially when you look at services, and we are in the same work that delivers uh azure as
[625.26 → 630.06] well, so there's this uh NTFS and both are services now, and so they're both in a very aggressive
[630.06 → 636.54] uh timeline as far as you know releasing uh you know small increments of uh functionality and then
[636.54 → 641.50] getting customer feedback on it and from our point of view the developer stack is uh something
[641.50 → 645.18] that you really have to give people's hand very early on in order to get meaningful feedback but
[645.18 → 650.00] we can't just ship faster you know the framework itself on Windows because that just doesn't scale
[650.00 → 654.58] to 1.8 building machines you really have to have a way where we can give it to developers faster and
[654.58 → 658.76] so on that point of view I think that that open source is also just the continuation of you know
[658.76 → 663.04] DevOps or some of the other you know keywords that you have probably heard so you mentioned
[663.04 → 668.14] Palmer and as we all know you guys have had a change in leadership here recently uh is the timing
[668.14 → 675.80] there uh coincidental uh or was that change in leadership kind of leading to this this this new
[675.80 → 683.60] stuff uh this rich again um I do not think it was coincidental uh if we look at the fact that um
[683.60 → 692.28] botnet supporting Linux and office supporting iOS happened in the same year um I think uh that's
[692.28 → 700.98] clearly showing that we're trying to reach out to um uh you know to our customers and provide products
[700.98 → 709.22] on the OS's where that they're using so uh i I think you're just seeing a shift in strategy
[709.22 → 716.90] at a fairly broad um level in Microsoft I have to give you guys credit too because when you're
[716.90 → 724.56] embracing it you guys really are embracing open source um on GitHub uh MIT licensed stuff taking
[724.56 → 728.78] pull requests you know I always compare apple and Microsoft when I'm looking at strategies because
[728.78 → 733.14] I just enjoy watching you guys do things apple's still kind of just like throwing their open source
[733.14 → 739.36] over the wall and just like here you go you know they're not really embracing it as a thing as much
[739.36 → 744.76] but you guys seem like you're really going for it yeah I think that's something that we
[744.76 → 748.26] learned over the years is I mean my team in particular we did open source or should say
[748.26 → 753.12] source open for a lot longer than uh than just the know the current open source strategy like
[753.12 → 757.00] there was the managed sensibility framework that we published on code black a while ago
[757.00 → 761.82] but the challenges that we always had that we basically did that you know source open where we
[761.82 → 766.50] basically give you the source, but then there are a lot of challenges around us keeping the community
[766.50 → 770.68] around alive because it's not really the real thing might we give you like every once in a while
[770.68 → 774.92] the drop of the source and so the one thing that we learned over the years is that first
[774.92 → 779.82] that's just not sustainable from our side because if you think of Microsoft as a company that delivers
[779.82 → 785.66] um uh you know a bunch of products then you always have these massive release cadences where
[785.66 → 790.78] you know towards the end game you are focusing on fixing bugs stabilization all of that and then the
[790.78 → 795.38] first thing that you stop doing is you know things that don't directly contribute value towards that
[795.38 → 799.68] goal and so from our point of view like maintaining an open source site somewhere as a
[799.68 → 804.58] as a site project it's just not maintainable it's the first thing that gets it's cut when you know
[804.58 → 810.12] people have to focus so the only way you can sustain open source is if is what you see on GitHub is the
[810.12 → 814.26] real deal because that's something we can't cut right like when we stabilize then you know, and we have to
[814.26 → 820.04] commit to the same repository everybody sees then there's really no option for us uh to discontinue that
[820.04 → 824.12] work and I think that's also something that the community really appreciates because I think in open
[824.12 → 828.64] source in general and I think that's true in any community it's definitely true in marriages right that
[828.64 → 833.84] people don't want to get surprised right you basically want to have a trusted relationship
[833.84 → 838.14] with each other so if you get the impression that Microsoft is holding something back because we go
[838.14 → 842.88] dark for half a year like even if we don't do anything bad it still has this very bad taste of us
[842.88 → 846.70] not telling me everything right and I think that's something that I think we learned very you know
[846.70 → 851.56] the hard way over the years and uh but I totally agree with your sentiment that you know I was a customer
[851.56 → 856.58] for a long time I pitched about Microsoft like everybody else and uh one thing I realized internally is that
[856.58 → 860.58] you know things if they change they really change I mean people really embrace it and then go
[860.58 → 864.92] wholeheartedly with that vision and that's why I'm so excited about open source because I think
[864.92 → 870.52] you know we normally have like any way to back off from that like now we are all in and I think that
[870.52 → 875.56] this trend will continue I like the term all in too especially for you because like you said when you
[875.56 → 883.42] make a turn, or you make a change it tends to be pretty drastic, or you know it's not an easy shift you
[883.42 → 889.26] sort of make quick decisions when it comes to big turns like that one thing you said that I'd like
[889.26 → 894.06] to camp out on for just a second was the flip side of open source i never really thought about and maybe
[894.06 → 898.96] this is a new term to me or just a new term in general but source open versus open source being
[898.96 → 904.86] pretty much the exact opposite where open source is focused on uh like jarred said not pulling an apple
[904.86 → 908.94] where you're just throwing the code over the wall and hoping for the best and not really
[908.94 → 914.16] embracing the community and where can you talk a little bit about that shift particularly with
[914.16 → 919.22] source open versus open source, and maybe I guess maybe you've already done that to a degree but
[919.22 → 924.44] feel free to ramble on source open versus open source for a bit do you have any thoughts on that maroon
[924.44 → 931.06] yeah I think we had a reference sources up there for a while they were under the reference source
[931.06 → 939.08] license um, but it was you know basically one way so what we this time it's very different we have
[939.08 → 945.02] resources up there and there's a lot of activity, and we are basically two-way it's basically the real
[945.02 → 950.40] way I mean what you were referring with apple is probably what we were doing earlier but the current
[950.40 → 957.80] effort is really about getting our stuff open source in a meaningful way and as you know your question
[957.80 → 962.84] earlier the mood in the botnet team, and you know how we're looking at it, you know i I would actually
[962.84 → 969.70] put it this way there's a lot of excitement within the team and that's reflecting on the repo uh
[969.70 → 975.04] basically every day we have you know stand-ups and hallway meetings and stuff like that and chats
[975.04 → 980.32] uh and everyone is super excited like we are talking about you know what's the next full request
[980.32 → 985.56] coming, and we're discussing those and having a good time about it, I think all of that is kind of
[985.56 → 991.16] reflecting on you know GitHub the all the energy in the team in general is very excited about
[991.16 → 999.10] it excited about the open source aspect what um when you say team maroon um beyond you rich and emo
[999.10 → 1006.16] um who is the botnet team you know how big is that I mean obviously it's probably large but
[1006.16 → 1013.14] you know how give the audience a example of how big your team is and the excitement size well I'll just
[1013.14 → 1021.70] cover the team size we have a lot of people working on like on botnet in general um in the division so
[1021.70 → 1027.58] we're in developer division, and so we have a ton of people working on you know Visual Studio on botnet
[1027.58 → 1033.34] framework on compilers but I think your question is more maybe the size of the team that is working
[1033.34 → 1039.98] on botnet core itself that's certainly well with the team that released the framework libraries that
[1039.98 → 1045.80] you saw there are tens of people that are working on that and then the runtime will come later there's
[1045.80 → 1052.32] some other set of tens of people working on that uh, so all told I think you're probably looking at
[1052.32 → 1058.28] about 100 people working on uh the code base that's going to ship in um that's going to be available on
[1058.28 → 1064.26] GitHub that's actually a lot of investment if you're wanting to you know make it bet on botnet
[1064.26 → 1070.02] um you can see that there's a lot of people working at Microsoft to provide you with a quality code base
[1070.02 → 1077.16] so let's talk about exactly which pieces of code are out there right now because let's face it you all
[1077.16 → 1082.90] have a lot of software over there and there are distinctions between botnet core botnet framework
[1082.90 → 1088.18] entity framework so on and so forth if you go to your guy's Microsoft's GitHub page which I think is
[1088.18 → 1095.36] just Microsoft dot GitHub dot Io um tons of repos kind of highlight the big ones and kind of show us
[1095.36 → 1101.74] tell us maybe what's not there yet well yeah so basically if you look at botnet core what you see
[1101.74 → 1107.50] today on GitHub is a very small number of libraries we have immutable collections we have the metadata
[1107.50 → 1113.32] reader that rosin is using we have XML, and we have our vector library that uh enables sim the
[1113.32 → 1117.82] intrinsic, and you know the question is why did we pick these four and not some other random slice and
[1117.82 → 1122.76] the the the reason is as I said earlier like from forest number one priority is to make open source
[1122.76 → 1127.76] real is that the thing that you see on the website is the thing that we can actually build uh ourselves
[1127.76 → 1133.34] and actually you know use the know the actual source to deliver the actual product and so
[1133.34 → 1137.48] there's some engineering initiative that we have to do internally to decouple our built
[1137.48 → 1142.22] infrastructure from the libraries themselves and as you can imagine like dev is super large and
[1142.22 → 1147.40] we have you know tens 10 years of like you know code base uh and built infrastructure that we have to
[1147.40 → 1150.96] decouple in order to make that work so that these four libraries that are out there on GitHub right
[1150.96 → 1155.78] now and botnet core are essentially just you know the libraries that you know we could easily extract
[1155.78 → 1160.26] because they're the know the most recent ones we did um XML is certainly not the most recent one
[1160.26 → 1164.28] but it was right you know one of our or few libraries that we could just say okay this is the one we can
[1164.28 → 1169.50] decouple very quickly and so what you will see over time is that um the entire botnet core stack
[1169.50 → 1175.08] which basically includes the runtime includes the BCL layer includes networking uh and uh also
[1175.08 → 1180.66] includes hpl.net on top as the app model will be open sourced and so as right now as I said there's
[1180.66 → 1185.34] a smaller segment in it so you can basically watch us as we add more libraries and I think you know
[1185.34 → 1189.16] over the next couple of weeks there's like I think three or four libraries being scheduled for being
[1189.16 → 1194.14] added uh console is being one of them data flow is another and so that you know there's certainly more
[1194.14 → 1199.16] growth if you look at the other repos as I said that if you look at botnet core it's you know one way to
[1199.16 → 1205.04] think about the core FX repo is it's essentially the BCL and so the BCL is basically the libraries
[1205.04 → 1210.58] that everybody has to use right, and then you have asp.net which is uh essentially the um the modern
[1210.58 → 1216.10] web uh framework that's just on top of botnet core as well as the full framework as a runtime
[1216.10 → 1221.12] option, and then you have entity framework, and you have uh the know the most and compilers which
[1221.12 → 1225.72] are not on GitHub, yet they're on complex still and so the all these things in combination are
[1225.72 → 1231.54] effective with the botnet platform and um asp.net basically when they started developing uh asp.net
[1231.54 → 1236.58] five they already knew that they would go open source entirely so they started pretty much uh you
[1236.58 → 1241.12] know working on GitHub from day one versus on our side as I said we know botnet core is still
[1241.12 → 1247.08] something that is in our internal servers, and we're extracting it as we go and so um I think that
[1247.08 → 1251.96] should cover what's on GitHub now as far as the botnet framework goes we essentially have two stacks
[1251.96 → 1257.34] and right now if you go to the botnet uh blog I just published a blog post about botnet core and
[1257.34 → 1261.90] how it relates to the full framework so you can think of botnet essentially our side as being two
[1261.90 → 1267.18] stacks one of them is the botnet framework which is the you know full flavoured stack
[1267.18 → 1272.32] that we shipped you know 15 years ago uh and uh that is the one that actually includes you know
[1272.32 → 1276.82] desktop scenarios it includes web scenarios it includes uh pretty much every scenario the developer ever
[1276.82 → 1281.44] wanted and then on the other side you have botnet core which is essentially a fork
[1281.44 → 1285.78] and so the question is why do we have a fork and the the the reason really is it has to do with
[1285.78 → 1291.62] our ability to evolve that stack so that in core is essentially a stack where factoring concerns and
[1291.62 → 1297.40] modularity was a key concern from day one versus botnet framework was never a concern as far as
[1297.40 → 1301.20] deployment goes because you know the botnet framework was designed to be deployed with windows
[1301.20 → 1306.70] as one monolithic entity, so factoring was never really a concern but now when you think about the
[1306.70 → 1313.22] know the breadth of devices and uh the scale that it has to um, um has to do than the question
[1313.22 → 1317.18] really becomes how do we ensure that we have the same architecture and can evolve this thing over
[1317.18 → 1320.96] the time and so when we did botnet core we really focused on that and that's why we have two stacks
[1320.96 → 1326.96] today and uh as far as open source goes one of the one of the key things that we need to focus
[1326.96 → 1331.80] on is being able to not just release source on a regular cadence but also take contributions back
[1331.80 → 1335.84] and I think an open source product isn't really an open source product unless you can really involve
[1335.84 → 1340.44] the community which obviously involves you know bug fixes and spec reviews, but it also involves
[1340.44 → 1345.12] actually taking code and so the botnet framework because it ships with windows it's you know pushed
[1345.12 → 1350.32] out by Windows update there's a super high compact bar for that and the problem is once you ship on 1.8
[1350.32 → 1356.00] billion machines it's really no longer about whether you fulfill your contract it's also about the fact
[1356.00 → 1360.72] that do you fulfill the implied contract because when you have apps running in that you know at that
[1360.72 → 1366.16] you know sheer size then there's a lot of like implicit dependencies so even for us, it's very
[1366.16 → 1370.48] hard to evolve the full framework at this point because every time you make a change there's this
[1370.48 → 1375.38] trade-off between oh did this break somebody or not and the botnet core stack is completely designed
[1375.38 → 1381.56] to be app local so from our point of view it's very easy to actually take contributions to on botnet core
[1381.56 → 1386.40] because it's very easy to reason about what happens if we take that source code and so that's why
[1386.40 → 1390.48] botnet framework um you know we released parts of it that corresponds to all
[1390.48 → 1395.92] core stack as open source on GitHub in the sense that it's an open source compliant license so it's
[1395.92 → 1400.56] all using the MIT license, but we don't run it as an open source project so we don't take
[1400.56 → 1405.60] contributions back on the full framework stack uh from our point of view the real open source
[1405.60 → 1411.76] strategy is on botnet core and that's where the focus of attention is all right let's pause the show
[1411.76 → 1415.92] just a minute give a shout-out to a sponsor I want to thank top for their support of this show
[1415.92 → 1421.68] you know besides my personal experience with top pure charity uh as many of you know who've
[1421.68 → 1426.88] been listening to the show a while and those who are new uh I work at a non-profit called pure charity
[1427.44 → 1433.52] and earlier this year we had a huge need for uh several ruby developers and within a matter of
[1433.52 → 1438.40] weeks top to helped us find some of the best, and we still have them on our team some of the best
[1438.96 → 1444.08] Ruby on Rails developers we could ever find this show in particular we're talking about botnet we're
[1444.08 → 1448.88] talking to the team at Microsoft behind botnet core effects being open source and what they're
[1448.88 → 1453.60] doing with the botnet framework but even you as a developer or someone out there who's trying
[1453.60 → 1459.44] to hire a developer uh to join their team go to top.com they'll take great care of you can
[1459.44 → 1464.80] freelance this developer you can hire botnet developers the full gamut top.com tell them
[1464.80 → 1472.24] the changelog sent you so botnet core you said the term BCO I translated as his base class license
[1472.24 → 1477.92] or sorry um base class library my bad I was uh stuck on your word of license back there for a
[1477.92 → 1483.52] second but am I right to assume that when you say base class library okay so you use the term BCL there
[1483.52 → 1490.08] to talk about botnet core um, and you use the word forked too so to slow down a bit for the listeners who
[1490.08 → 1494.96] are like just probably like I am like asking a bunch of questions as they're listening to you or um
[1494.96 → 1503.20] um is botnet core then a fork of the framework then and will there be will there be a second
[1503.20 → 1506.88] version of the framework that's sort of open source and the botnet framework that's sort of
[1506.88 → 1513.92] proprietary and closed source that you control that's that's kind of the model except that uh you
[1513.92 → 1518.32] know as I said the botnet framework is super large, but it also has client technologies like informs and
[1518.32 → 1525.20] path on top, but there's certainly also the BCL part in the full framework as well and so when we
[1525.20 → 1529.60] when I said fork I mean you can think of it we took the sources in the full framework and just
[1529.60 → 1534.80] packaged it slightly differently for botnet core and so on thing we did for example is uh changing the
[1534.80 → 1539.84] assemblies themselves or the know physical files that actually contain the binary code and
[1539.84 → 1544.24] that is basically done in order to support the new factoring goals and that required some changes to
[1544.24 → 1550.96] the source so um from that point of view there are some differences in the API sets but we
[1550.96 → 1556.16] still are fully committed on keeping a story where you can basically create libraries that run on either
[1556.16 → 1560.72] side so you can only create a library that runs on full framework as well as botnet core, so there is
[1560.72 → 1568.00] a compatibility story between the two stacks but as far as evolution goes you can think of it as similar to
[1568.00 → 1572.88] the know to open source in general where you basically have uh you know the latest hot
[1572.88 → 1576.72] stuff is you know whatever the latest commit in the repo is people can download this build it locally
[1576.72 → 1582.56] and run it then the next step on our side is we release open source uh pre-packaged as a bunch of
[1582.56 → 1586.72] new get packages, and so we ship these package every once in a while when the team that owns the particular
[1586.72 → 1591.76] component you know test that component and signs off of that, but that's a know per component thing
[1591.76 → 1596.48] and then the next step is basically we take a bunch of new get packages and effectively do the same thing
[1596.48 → 1600.24] that open sources with distributions, and we basically take a bunch of packages together
[1600.24 → 1605.44] and say this is the next version of botnet core and so a fourth step conceptually is it's porting
[1605.44 → 1610.24] these you know this you know the innovation that happened on botnet core back to the full
[1610.24 → 1615.76] framework and that is like just from a machine engineering if yeah effort that is always somewhat
[1615.76 → 1620.88] lacking behind because as I said touching full framework is hard we take our responsibility on
[1620.88 → 1626.64] compatibility extremely seriously so we don't just roll the latest build out and so that that requires some
[1626.64 → 1631.60] some some some delay essentially and so from that point of view the core pieces of it are
[1631.60 → 1634.80] available as open source on the full framework but not everything is
[1636.48 → 1641.04] do you have that written down somewhere because uh my head's spinning a little bit it sounds like a lot
[1641.04 → 1646.56] of process maybe your direct customers probably follow that a little better than I did, but it seems like
[1646.56 → 1652.48] um perhaps some clarity on exactly how it all works do you guys have that documented anywhere or
[1652.48 → 1656.96] somebody who wanted to get involved could go and say okay here's how here's what I can contribute with
[1656.96 → 1662.56] with here's the stuff I can't here's how it all gets shipped is that anywhere yeah so as I said like
[1662.56 → 1666.96] there's basically two blog posts on our side that basically summarize them up there's one on
[1666.96 → 1672.80] botnet core open source which is uh about two weeks old and then just today I published a blog post on
[1672.80 → 1677.44] what is botnet core and how it relates to the full framework um, and you know what are what are
[1677.44 → 1682.24] the differences between the two and how do we think about that gotcha awesome now I'm sitting here you
[1682.24 → 1687.68] said the word forked and this might be a fun tangent um you guys got some forks out here
[1687.68 → 1694.96] on your guy's Microsoft page you forked Regis you forked node you forked docker uh safe to assume that
[1694.96 → 1700.96] you guys are building technologies on top of these open source projects uh in-house uh well this is rich
[1700.96 → 1706.64] again there's probably a little bit of clarification that'd be useful here okay uh, so there's actually two
[1706.64 → 1714.64] GitHub well actually there's multiple GitHub orgs okay um that we're using Microsoft the Microsoft
[1714.64 → 1723.44] org is the main GitHub organization that Microsoft is using um as you might guess and so there are teams
[1723.44 → 1729.76] that we're like we don't even know anything about necessarily that operate in that org and so you said
[1729.76 → 1737.92] you know someone for Regis um we actually have no clue um about that yeah I mean obviously we could
[1737.92 → 1743.52] find out kind of thing but um we have like zero insight into that I'm seeing now at the bottom of
[1743.52 → 1749.76] that page there's other hype Microsoft GitHub orgs and you guys have man double digits yeah we actually
[1749.76 → 1756.56] have like 20 or 30 or 40 orgs we're actually trying to move more people over to the Microsoft org to make
[1756.56 → 1765.68] it is a little bit easier to navigate but um the thing um is our work is actually in the botnet org
[1765.68 → 1771.20] gotcha yeah that's where botnet core lives uh actually Verdun can speak to this piece what
[1771.20 → 1780.72] the botnet org is and why um botnet core is in there right so basically botnet repo is actually the
[1780.72 → 1786.16] repo for botnet foundation the open source effort um you know the open source community effort
[1786.16 → 1794.24] around botnet in general with the community so botnet core became open source it joined the
[1794.24 → 1800.72] community as well botnet foundation community so they were setting up a new repo um so basically
[1800.72 → 1808.00] uh you know we had a lively discussion, and they actually set it up the repo directly in the foundation
[1808.00 → 1815.60] so that org uh in the GitHub you know organization is botnet foundation organization and botnet core
[1816.16 → 1823.68] has joined uh the organization and is basically doing all the open source work in the open, and you know
[1823.68 → 1830.32] rich can talk about how mono is also in there um you know basically actively participating in the
[1830.32 → 1837.36] discussions and the efforts yeah what vroom was mentioning is there we have a botnet foundation
[1837.36 → 1847.20] dot org website and there are some forums on that at forums dot botnet foundation dot org and for those
[1847.20 → 1852.64] of you um who know about botnet open source you'll probably know about the mono project, and so we're
[1852.64 → 1861.36] very much um collaborating with that project both in a code sense and um collaborating together
[1861.36 → 1867.04] and talking together in these forums and if you take a look at the forums you'll probably get a sense of that
[1867.36 → 1875.60] okay and for those who are unaware can you uh give a brief rundown of mono sure mono is essentially um
[1876.40 → 1885.60] a clone of um the botnet that um Microsoft built it's I don't know the exact date of its inception
[1886.24 → 1894.08] but um it's in the early 2000s for sure and uh it's headed by a guy named uh Miguel de CASA
[1894.08 → 1901.36] who actually had worked on some other open source projects I think he'd worked on the gnome uh window
[1901.36 → 1910.08] manager oh I'm correct on that point and um anyway it's its a project that uh a lot of people have
[1910.08 → 1917.20] used um more recently it's actually been used to target iOS and android as part of the uh a tool set
[1917.20 → 1925.44] built by Xamarin who Miguel actually works for he's actually a founder of that company and um
[1925.44 → 1931.20] the thing I think is fascinating right now is Microsoft like the botnet team at Microsoft and
[1931.20 → 1939.28] the mono project are now working closely together to um kind of deliver coherent and consistent botnet
[1939.28 → 1947.04] implementations for all um botnet users on the planet essentially, and we didn't quite have that
[1947.04 → 1953.92] kind of arrangement before so uh I think it's really, really positive and uh you'll see that i
[1953.92 → 1959.52] think you'll really see that come together probably next year right now we're just kind of trying to get
[1959.52 → 1966.64] everything laid out you know this news of us open sourcing is also new to Miguel so I think by the time
[1966.64 → 1972.48] we get say to you know the middle of next year I think we'll have a much more a much better sense
[1972.48 → 1976.80] of what it is that the two projects are doing together we're very much you know still trying
[1976.80 → 1981.60] to figure that out that's awesome I mean I think the cross-platform aspect of this is going to be a
[1981.60 → 1988.48] huge win for developers everywhere i fact-checked your uh your gnome there, and you drilled it uh
[1988.48 → 1993.60] okay awesome so just uh while you're talking there I was like I looked it up yeah yeah I do I mean we
[1993.60 → 1998.80] we know Miguel personally so uh but I just wanted to yeah make sure that was correct
[2000.72 → 2005.44] can we uh maybe camp out there for just a sec on the cross-platform thing and maybe just the
[2005.44 → 2009.20] the fork thing and the open source thing I think it's sort of the summary of what we've been
[2009.20 → 2014.96] talking about for the last 20–30 minutes but um you know what's the true goal here you know maroon
[2014.96 → 2020.72] you mentioned earlier uh cross-platform as an is a nice advantage of going open source
[2020.72 → 2026.40] um it mentioned embracing the community embracing actually open source versus source open
[2026.96 → 2031.52] what's what do you think what can you share about the true goal the overall goal of
[2032.16 → 2037.92] open sourcing.net core versus keeping a closed source and not embracing community
[2039.12 → 2045.12] so I think you meant me not maroon but that's okay um so I think from the the other
[2045.12 → 2054.88] um maybe I have a light sound so soon was it MO yeah oh sorry you know you take it I think the
[2055.84 → 2061.52] one of the one of the challenges is as I said is that you know Microsoft is as which mentioned now
[2061.52 → 2065.92] certainly going you know out of more devices I think the general realization that everybody
[2065.92 → 2070.96] in the industry is now uh making is that you know there's no longer like true monoculture so
[2070.96 → 2075.68] there there there's many like you know device ranges and like they all have certain market
[2075.68 → 2081.68] segments but in order to be successful uh as far as an application experience skills those span
[2081.68 → 2085.68] devices now right like you can even if you're said even if Microsoft would say you want to focus on
[2085.68 → 2090.32] windows the reality is there's so many other devices and experiences out there that you kind of
[2090.32 → 2095.12] have to integrate into that's expected from an app standpoint that basically requires you to
[2095.12 → 2100.08] support not just one thing you can still say as an application developer you know I provide you know
[2100.08 → 2104.48] the best experience, or you know most of my features in a certain in a certain vertical, but you know
[2104.48 → 2109.60] the integration points are the ones that you still have to your know deal with somehow and uh dot
[2109.60 → 2115.92] net was pretty much from the get-go designed to become to have a single experience on a variety of
[2115.92 → 2120.48] scenarios so if you look at the original design of win forms and web forms for example somebody really
[2120.48 → 2124.32] made sure that they are pretty much the same no I would argue that for that that was a mistake
[2124.32 → 2129.04] because it's not an event-based paradigm but that you know in the spirit of making things similar I think
[2129.04 → 2133.84] that that's still very much uh an important scenario for for for many people because if you think from
[2133.84 → 2137.76] a just on an epic from an architectural layering perspective there's always pieces of your code
[2137.76 → 2142.48] that you want to reuse across the devices right some business logic you know some you know some
[2142.48 → 2148.40] logic that does something in your app and you know from it from a scenario standpoint dot net
[2148.40 → 2152.48] wants to enable those scenarios and that that has to that certainly means that we have to go
[2153.04 → 2157.52] effectively where the app has to go and in today's world as I said like there's mac there's iOS there's
[2157.52 → 2162.00] android there 's's Linux, and so we have to enable the stack to go there from that from
[2162.00 → 2166.64] that point of view I think that open source is really about increasing the breadth of dot net
[2167.36 → 2172.48] and making it easier for people to just stick to one technology if they chose to do that but
[2172.48 → 2176.24] you know, but they'd always had great availability with native code so if you want to do something
[2176.24 → 2181.60] else uh you know providing a native UI for example uh, and then you know call into dot net or the other
[2181.60 → 2185.92] way around there's certainly stories for that as well so when we talk about cross-platform i just one
[2185.92 → 2190.24] question here for the listeners who are thinking like okay so what does this thing work on what
[2190.24 → 2196.16] can I if I'm hacking today could I pull it down start working on it today what platforms are currently
[2196.16 → 2201.84] supported by dot net core dot net uh framework that's the word I was looking for
[2201.84 → 2210.24] the other f word the good f word uh I could take that one that's rich um right now both dot net core and
[2210.24 → 2217.36] dot net framework support only windows so just to back up a little bit we've we've clearly stated that
[2217.36 → 2225.68] um for dot net core we're going to um uh support it on Mac and Linux as well, and so we kind of had a
[2225.68 → 2232.56] decision to make which was should we wait until we've done all the engineering work at which point
[2232.56 → 2239.36] we support Linux and mac as well as windows and then open source or should we open source with our
[2239.36 → 2247.76] windows implementation start to build a community and then build the uh Linux and mac support in the
[2247.76 → 2254.88] open and so as you can guess we chose this latter option and i I like that option yeah I really feel
[2254.88 → 2260.00] like it was the right option especially given the response that we saw I think it's just been
[2260.56 → 2266.40] hugely validated that it was the right option that's essentially what we're doing so we do not yet have the
[2266.40 → 2271.68] the Linux and mac support, but we're uh we've started already started working on it um we have
[2271.68 → 2277.68] people who that's their main job is building Linux and mac support into dot net core and uh you're going
[2277.68 → 2283.60] to see that um start to arrive pretty soon now it's its it's not going to all appear on one day
[2284.48 → 2287.76] it's going to be very iterative is there one that's first before the other
[2289.20 → 2296.32] that's a good question I don't think we've made a plan uh quite like that yet well what I would say is
[2296.40 → 2299.76] in general like if you look at how dot net works I mean there's certainly things that are
[2299.76 → 2303.92] innovative platform independent right I mean all the collection libraries like immutable collections
[2303.92 → 2308.88] probably works today as it is already on any environment you know things that interact with
[2308.88 → 2313.44] the operating system like file systems and other things are obviously a bit more involved and then
[2313.44 → 2319.20] as you go to the lower stack uh you know we have this very you know thin layer that basically ties the
[2319.20 → 2324.48] the actual framework towards runtime and so you know on our side we basically have two different
[2324.48 → 2329.44] runtime strategies today we have a legit based runtime, and we have an ahead of time compiled runtime
[2329.44 → 2333.76] and so we also make investments to make the runtimes available cross-clad, but that's obviously
[2333.76 → 2338.48] something that is more like an all-in or nothing because you need the entire runtime uh up and running
[2338.48 → 2343.60] before you can actually run any managed code, so there's certainly some um you know some investment
[2343.60 → 2348.56] there as well but as far as libraries go I mean you can probably already compile some of our libraries
[2348.56 → 2353.04] there that are in GitHub I would say that the metadata reader probably uh in some way or the other
[2353.04 → 2358.64] already works on mono because there was a demo that we gilded where uh the majesty shop BB compilers
[2358.64 → 2364.88] we use that component already run on mono new collections should just work and so uh I think the very first
[2364.88 → 2369.52] thing we probably do is on our side uh you know add the build scripts we can actually build on a non-windows
[2369.52 → 2374.56] machine and then set up a CI system so we can actually uh you know validate for requests across the
[2374.56 → 2378.96] different platforms but as far as the ability goes to just take the source from one of it today you should
[2378.96 → 2383.36] be already be able to do that the one thing I want to add is that you know it's always true that
[2383.36 → 2388.08] botnet was you know cross-platform if you screen hard enough right because the mono was around for a
[2388.08 → 2392.64] long time now but I think the real difference is now that we normally have a fourth community you know
[2392.64 → 2396.72] where you know one side does the windows' thing which is Microsoft and then this is other community that
[2396.72 → 2402.56] does the Linux implementation the intent of botnet core is really to have one unified code base that runs on
[2403.12 → 2408.72] you know Linux windows and mac and not just that also on top of that Microsoft actually says we support
[2408.96 → 2412.88] these three things so it's no longer the case that you know there's a Microsoft distribution that is
[2412.88 → 2416.80] windows and then there is let's say a mono distribution that does Linux and mac it will
[2416.80 → 2421.92] actually be coming from your know from from from one corporation so to speak you know as far as baking
[2421.92 → 2426.64] goes but as far as the community goes it's really just one big community where Microsoft plays one
[2426.64 → 2431.20] part in it, and then you know the mono community plays another part and whoever else wants to join in
[2431.20 → 2436.48] plays their part all right let's take a break from the show real quick we got to mention a sponsor
[2436.48 → 2443.12] that sponsor is rackspace loves open source they love supporting their community and
[2443.12 → 2447.28] just one of the ways they're doing that is by sponsoring this show right here that you're listening
[2447.28 → 2452.32] to and that's why they're giving you and everyone else who wants it fifty dollars a month in credit
[2452.32 → 2457.84] for 12 months to explore their open cloud get a free developer plus account today to get started
[2457.84 → 2463.28] you get dev to dev support so if you get complex questions you can talk directly to their developers
[2463.28 → 2468.96] they're the same experts who write their SDKs and their APIs and get access to all their services
[2468.96 → 2477.44] monitoring DNS auto-scaling orchestration private networking message queues and more all for free
[2477.44 → 2482.64] there's no usage limits whatsoever so use their services as much as you want you're only billed
[2482.64 → 2488.00] for the usage above fifty dollars a month they have open source libraries to support any language of
[2488.00 → 2493.68] your choice and for those listening today they do support dot net go to the change law dot com
[2493.68 → 2500.16] slash Rackspace to get started and now back to the show earlier on you guys mentioned I think uh
[2500.80 → 2508.00] was it Emma who made the marriage analogy I want to get I want to get back to that here uh
[2508.80 → 2513.76] yeah that was all about his personal life was laughing his butt off so if runs got something up his
[2513.76 → 2518.56] sleeve I think well I want to get back to that for a second because uh I love you guys excitement
[2518.56 → 2523.92] and this is a really cool stuff the community was you know jumped on it everybody even Microsoft haters
[2523.92 → 2528.40] were like wow that's really awesome um, and you mentioned how excited you guys are for pull requests
[2528.40 → 2533.04] and stuff and I would say you're very much in the honeymoon phase of open source where everything's
[2533.04 → 2537.84] exciting you know I've had that situation where I get a bug fixed to my repository and I didn't have
[2537.84 → 2542.48] to do it myself and that was awesome um we spoke with a lot of people over the years when
[2543.12 → 2548.00] they've been maintaining open source projects for a time and started off exciting, and they got you
[2548.00 → 2554.64] know a lot of press or whatever and uh it was fun and then over time it became hard work um obviously
[2554.64 → 2560.40] you guys are doing this as part of you know your jobs but running open source project can be difficult
[2560.40 → 2567.76] it can be taxing it can have moments where um you know this pull request you know is excellent
[2567.76 → 2571.52] but it actually goes against our business goals, so there's all these different concerns were these
[2571.52 → 2577.04] things you guys thought about as you decided open source yeah I can take this one this is Baron
[2578.16 → 2582.56] yeah I think uh here the culture of the team kind of comes into play uh you know that's what I was
[2582.56 → 2589.04] talking about earlier so you know when I look at the team our engineering team you know all of them
[2589.04 → 2595.12] are really excited about you know open source they feel like uh they're not just doing it you know as
[2595.12 → 2600.32] part of their jobs I mean if you look at the GitHub repo you know how it looks and everything folks are
[2600.32 → 2606.56] truly excited the only difference is they're getting paid for it uh you know, so basically that's why i
[2606.56 → 2612.80] think the excitement around open source uh you know will continue here there are you know obviously the
[2612.80 → 2617.60] kind of things you mentioned you know we have to think through you know how we are going to process
[2617.60 → 2623.68] you know full request in a democratic way uh you know moving forward uh you know how do we know
[2623.68 → 2629.52] work on some of the contentious things you know obviously you know as engineers we tend to get into
[2629.52 → 2635.36] our discussions and stuff like that and how do we kind of handle them uh you know with a broader audience
[2635.36 → 2640.24] so all of those challenges are true but I think the true uh you know thing that makes me excited
[2640.24 → 2645.04] about this whole thing is the culture on the team that's that's unique uh you know I was
[2645.04 → 2651.92] telling this to you know IMO the other day that you know it doesn't feel like that I am uh you know
[2651.92 → 2657.04] working in a team which my friends think you know I am you know probably working as you know
[2657.04 → 2660.96] my friends are not from Microsoft they think they're probably wearing suits or something but
[2662.24 → 2669.28] here I think the culture of the team is very, very different truly excited, and you know basically
[2669.28 → 2674.96] uh you know if I use the phrase living in GitHub you're not wearing suits then uh no we're not
[2674.96 → 2681.28] wearing suits t-shirts shorts flip-flops or what uh in the summer we'd be wearing flip-flops um it's
[2681.28 → 2686.48] pretty cold in Washington right now that's true yeah it's just about freezing so um yeah we're skipping
[2686.48 → 2692.00] the shorts uh well I've heard the rule is if it's above 30 even flip-flops are okay yeah I thought you
[2692.00 → 2695.84] kept it so warm there as you wore your cold clothes on the way to work and when you got there you changed
[2695.84 → 2702.08] into your warm clothes totally yes i I just like to comment on a question that you guys were kind
[2702.08 → 2708.16] of asking earlier back to the motivation piece so we talked a lot about the motivation for open source
[2708.16 → 2715.68] but we didn't um really address the motivation for cross-plat quite as much and um from a corporate
[2715.68 → 2722.40] customer standpoint we actually do get a lot of customers coming to us that say uh you know really
[2722.40 → 2728.48] love botnet love c sharp it's very productive we can build the apps we want to with it, but we've got
[2728.48 → 2734.08] a bunch of Linux machines um that we've been using, and you know we're trying to consolidate
[2734.72 → 2743.12] our dev platform across everything we do we want it to be botnet um, so please build a Linux version for
[2743.12 → 2750.96] us you might be surprised at how often that question comes through uh another one is that uh that's
[2750.96 → 2759.28] fairly similar in nature is um I think we've publicly stated that about 20 of the VMS in azure are Linux now
[2760.00 → 2768.24] and um we very much want to be able to give a consistent um offering of developer platforms that
[2768.24 → 2776.16] work on both Linux and Windows server in azure you know azure will continue to have the model of you
[2776.16 → 2782.24] you know it's your VM run what you want on it um so we're certainly happy to have people running Linux
[2782.24 → 2789.68] VMS that run java on them or whatever but um from like a first class offering standpoint we want
[2789.68 → 2796.80] to make sure that people can run uh botnet apps on Linux on azure and so that those two kind
[2796.80 → 2804.24] of things are really the cross-plat motivation for us on the server side you mentioned uh your corporate
[2804.24 → 2808.16] friends so that's a good lead into the question we told you we were going to ask you about
[2808.72 → 2816.24] just the change that this imposes to your corporate users who either didn't use open source
[2816.24 → 2820.96] purposefully because they wanted to use something that was proprietary and had support or had something
[2820.96 → 2825.84] to blame basically if something went wrong you know how does this change things for those corporate
[2825.84 → 2832.48] users who may not embrace open source or who purposely didn't embrace open source for whatever the reasons were
[2832.48 → 2840.00] first I think there's our first answer which is we're not really changing much about what it is we do
[2841.12 → 2847.36] as you can imagine we've always had source control and so really all we're doing is taking our source
[2847.36 → 2855.84] control system and hosting it on GitHub and changing the license to something much more liberal so that's the
[2855.84 → 2862.16] open source thing, but we're not changing anything about our internal processes for how we go about
[2862.16 → 2869.84] shipping quality commercial software um there's nothing really about that that's changing uh and
[2869.84 → 2875.28] that's definitely a strong message we want to send our corporate customers the other side of it is if
[2875.28 → 2880.56] you're an uh you know uncomfortable with open source or just don't care about it, you don't really have to
[2880.56 → 2886.32] think about it because you don't have to participate in the open source community if you don't want to
[2886.32 → 2893.92] do and what we ship at the end of the day is still commercial software most uh for the foreseeable future
[2893.92 → 2900.24] most of the code base is still going to have been written by Microsoft engineers I mean we certainly want
[2900.24 → 2907.04] to get to the case that a very high percentage of pull requests come from the community but um you're
[2907.04 → 2914.16] fundamentally still getting a product that was vetted by Microsoft and is supported by Microsoft
[2914.16 → 2920.96] um support so I think for corporate customers you can still think of this very much as Microsoft
[2920.96 → 2928.72] commercial software and call it good awesome well as you guys know we usually close out uh with a
[2928.72 → 2935.68] question about a programming hero now all three of you feel free to answer um but I know at least one of you
[2935.68 → 2941.36] have somebody in mind so uh who is your guy's programming hero yeah so from my point of view
[2941.36 → 2946.64] I already mentioned I was a customer for a long time for Microsoft and um the reason I really jumped
[2946.64 → 2952.48] on botnet when it came out was the fact that I used Delphi quite a bit before and uh I was I found
[2952.48 → 2957.60] that Delphi was an amazing experience and then the guy who did pretty much Delphi went to Microsoft and
[2957.60 → 2962.72] did c-sharp and that's Andrew Heidelberg so from that point of view like he's he's somewhat my hero in
[2962.72 → 2968.16] the sense that you know it set my career and uh influenced my decision to join Microsoft as I said
[2968.16 → 2973.28] many people here I didn't join Microsoft I joined the team that owns botnet and uh that happened to
[2973.28 → 2978.80] be Microsoft but if that would be any other place that's where I would have been awesome anybody else
[2979.68 → 2987.04] uh that's good enough for me personally I don't know if maroon has uh an answer Bill Gates anybody
[2987.04 → 2989.92] I'd say modern more than
[2993.52 → 2998.72] you heard it here first another question that we tend to ask which I think probably is apropos for
[2998.72 → 3003.92] you guys yeah is a call to arms uh for the open source community you're speaking directly to the
[3003.92 → 3009.04] open source developers here today what would you say what how can they help you or what would you love
[3009.60 → 3013.44] uh for the open source community to do with regard to your new you know botnet open source stuff
[3013.44 → 3018.48] yeah i can take that one so the one thing you just mentioned is like the honeymoon phase where
[3018.48 → 3023.60] everything is awesome right um we will certainly like my team although like we certainly talked to
[3023.60 → 3028.08] a bunch of other teams around here that did open source, and you know already way past the honeymoon phase
[3028.48 → 3032.72] like you know everything is different every requirement is different so that's some of the
[3032.72 → 3036.08] stuff that we're working on are things like you know how do we do API reviews what do we decide
[3036.08 → 3040.40] something is good or not transparently and so it is very likely that we will do mistakes
[3040.40 → 3045.04] we will do not be as transparent as we promised we would be, or we will miscommunicate certain
[3045.04 → 3049.52] things, or we will just annoy somebody by closing their pull request so if one of those things
[3049.52 → 3053.92] happen then we absolutely do want to get feedback from the community, and we want to have a conversation
[3053.92 → 3059.60] about that and if you go to the forums uh at the net foundation.org there's already a bunch of
[3059.60 → 3063.92] like people talking about how we do open source what we do well what we don't do well what we could
[3063.92 → 3070.32] improve on what we should uh do differently and that's really for me like the primary uh
[3070.80 → 3074.24] feedback that I am looking for I mean there's always people that want to do pull requests but
[3074.24 → 3079.20] it's its it's from all the people that we reach it's the minority, but you know a lot of people
[3079.20 → 3084.16] you know benefit from the transparency and so that's the thing I really want to get
[3084.16 → 3086.16] I get a handle on whether we do a good job or not
[3088.64 → 3094.32] so you mentioned botnet foundation a couple of times in the show uh it makes sense to mention here at the
[3094.32 → 3100.16] end that um that we do plan to have you and Beth or sorry maroon and Beth on upcoming show to talk
[3100.16 → 3105.60] about the botnet foundation and what that is but can you talk a little bit about just a snapshot of
[3105.60 → 3111.52] what the botnet foundation is you mentioned earlier that uh core effects is uh granted to I think is
[3111.52 → 3116.88] the word you used to the botnet foundation what does that mean what is it uh what is that foundation
[3116.88 → 3125.20] yeah that's a great question so basically botnet foundation you know is an effort uh which is to
[3125.20 → 3130.88] aggregate the botnet community kind of basically together there are a lot of projects that are happening
[3130.88 → 3136.16] in process like some of the new ones that are coming on board like botnet core, so the idea is to
[3136.16 → 3141.60] kind of have you know common place where we can, you know kind of advance the community uh you know at
[3141.60 → 3147.76] the same time together it is uh you know community driven effort it is being bootstrapped by Microsoft
[3147.76 → 3156.00] at this point uh but uh it is going to be a community driven it's its own entity separate from Microsoft
[3156.00 → 3164.08] its advisory council will also have people from the community so the whole idea behind botnet foundation is
[3164.08 → 3170.56] that like botnet core has joined the foundation many other projects have you know joined the foundation
[3170.56 → 3176.40] and they're actively contributing you know working with each other in the foundation so for all the
[3176.40 → 3181.44] new open source developers or the current open source developers botnet developers are exploring open
[3181.44 → 3187.44] source is a great place to kind of bring your projects work together and kind of contribute in existing
[3187.44 → 3193.20] projects, or you know make your new ones with the community together there are a lot of advantages that
[3193.20 → 3199.12] you know come from working together and growing a community so botnet foundation is that one
[3199.12 → 3205.04] one attempt in the upcoming you know podcast that we'll do we'll talk more about you know the exact
[3205.04 → 3210.16] specifics but in terms of call to arms I'll recommend you know request everyone to visit the botnet
[3210.16 → 3216.88] foundation dot org website and learn more about it uh there is an email address where you can get in
[3216.88 → 3222.00] touch with us uh, and you know talk about your existing projects some of the new ideas you're thinking about
[3223.04 → 3228.56] and I want to mention too um only because it's timely we don't usually time stamp our shows that much
[3229.12 → 3234.08] to a degree but uh you've got as jarred mentioned you've got some change happening in several open
[3234.08 → 3239.28] source large open source communities where uh you've got corporate partners and sponsors that have
[3239.28 → 3245.04] sort of been paving the way, and we asked a couple questions around your choices with botnet core and some
[3245.04 → 3250.08] of the future we can expect in open source but I think it's worth mentioning just because of this tail off
[3250.08 → 3257.84] the botnet foundation the fact that at least what I see now is that your approach towards um the foundation
[3257.84 → 3263.92] a lot of good open source is built around a foundation versus a corporate entity sort of open governance and
[3263.92 → 3268.32] the community is what you mentioned there so I think from what I'm hearing it sounds like you guys are taking
[3268.32 → 3275.44] the right steps to go towards Linux and mac uh adoption for development platforms uh open sourcing the
[3275.44 → 3280.72] the platform itself or open sourcing you know botnet core and the BCL as you mentioned
[3280.72 → 3286.80] before so congrats definitely on that can you maybe mention anything else on that fact that uh you know
[3286.80 → 3293.12] it's about community that there's nothing um that's sort of like Microsoft and then versus the
[3293.12 → 3298.24] community it's sort of just based on this foundation absolutely and maybe tease the fact we're going to have
[3298.24 → 3303.84] this upcoming show with that you know tease the fact um I completely agree with you know the summary uh
[3303.84 → 3309.44] around that it's very important to build open source projects around a community rather than a corporate
[3309.44 → 3316.48] entity and that's what foundation aims to be um and I think it'll go a step further the idea is to
[3316.48 → 3322.32] you know bring together all the other you know basically cool botnet projects that are going on and
[3322.32 → 3327.20] you know uh you know aggregating them at the same place so that they can connect with each other
[3327.20 → 3332.24] and sort of you know cross-pollinate, and you know participate in various projects and this kind of should
[3332.24 → 3340.16] uh you know accelerate the whole botnet community as a whole uh you know as IMO said you know previously
[3340.16 → 3346.72] we are all in into this um and the only way we'll be all in if you know all the community works together
[3346.72 → 3348.64] then you know some you know guides from here
[3351.12 → 3355.60] well i uh I know that jarred and I are definitely excited to have you guys on the show we appreciate uh
[3356.24 → 3359.36] you coming on the show Beth sorry you couldn't make, but we'll definitely catch up with you and
[3359.36 → 3364.48] maroon on botnet foundation dive deeper so for those listening with bait of breath on that one
[3364.48 → 3368.40] stay tuned that might happen in the new year I'm not sure if it'll happen before Christmas or not
[3368.40 → 3373.12] we'll definitely we'll definitely do our best to try but rich emo and maroon thank you so much for
[3373.12 → 3378.32] joining us today on this show and thank you to everyone behind you your team behind you making
[3378.32 → 3382.32] your appearance here on this show and talking about botnet core and what's happening there
[3382.32 → 3387.84] possible I know you've got a lot of excited people that are part of your team that are you know
[3388.32 → 3393.84] lifting you up and you know doing lots of great stuff so really appreciate all the effort that
[3393.84 → 3401.20] goes into making your appearance here today um come true for us, and we're excited about it so um I do
[3401.20 → 3405.52] want to mention before we tail off we got a couple sponsors that make the show possible code ship top
[3405.52 → 3410.96] top towel and rack space um some really great uh sponsors we have on the show so we very much
[3410.96 → 3415.92] appreciate their support um and with that unless there's anything else lets uh let's all say goodbye
[3416.48 → 3421.84] so goodbye from me goodbye from rich uh thanks for the opportunity to be on the show
[3421.84 → 3426.96] no problem guys thanks for having us yeah, thanks guys this is maroon uh it was exciting to talk to
[3426.96 → 3429.04] you guys thanks for having us thank you
[3429.04 → 3438.48] this is
[3441.12 → 3454.96] you
[3459.04 → 3489.02] Thank you.
