[0.00 → 13.58] welcome back everyone this is the change log where remember to support a blog podcast and
[13.58 → 18.30] weekly email that covers what's fresh and what's new in open source you can check out the blog at
[18.30 → 24.28] thechangelog.com our past shows at 5by5.tv slash changelog, and now you can subscribe to the change
[24.28 → 28.58] log weekly it's our weekly email covering what's fresh and what's new in open source we send them
[28.58 → 33.68] out every Saturday subscribe at thechangelog.com slash weekly this show is hosted by myself Adam
[33.68 → 39.46] static I almost said Andrew Thorpe and also Andrew Thorpe say hello man hey how's it going
[39.46 → 46.68] it's a good day man and this is uh this is episode 103 man it is good day yes it's good stuff we're
[46.68 → 54.46] we're joined by a case state broader cc Brody sorry about that case he's he's the uh co-founder
[54.46 → 59.14] of git lab with uh with Demetre so they've got a fun thing going on over there they just versioned
[59.14 → 67.22] the 6.0 so uh case welcome to the show my friend thank you no problem honoured to be on the show and
[67.22 → 72.38] and uh Andrew congratulations on your birthday man yeah thanks yeah you can virtually wish
[72.38 → 78.14] Andrew a happy birthday because today Thursday I think this will air on Friday but uh you'll be in
[78.14 → 84.90] the future but today's his birthday good stuff big day and before uh before we kick off the show I want
[84.90 → 91.86] to pay some homage to our sponsor digital ocean super awesome cloud hosting server so uh, uh cloud
[91.86 → 96.82] hosting provider digital ocean is a simple cloud hosting provider dedicated to offering the most
[96.82 → 103.88] intuitive and easy way to spin up a cloud server users can create a cloud server in 55 seconds which is
[103.88 → 112.78] super quick and pricing starts at five bucks only for uh a half a gig of ram 20 gigs of SSD uh drive
[112.78 → 118.46] space one CPU and one terabyte of transfer which is pretty awesome for five bucks they feature 99
[118.46 → 126.08] percent uh actually it's 99.9 correction uptime uh SLA on their services they have data centres
[126.08 → 131.68] here in the U.S. in New York and San Francisco as well as in Europe not very far from case in Amsterdam so
[131.68 → 138.02] pretty neat their interface they have to manage it all is intuitive it's superfast and power users
[138.02 → 141.92] can actually replicate it on a larger scale because they have an awesome API to go with it
[141.92 → 148.54] digital ocean uses KVM virtualization and additionally hosts a library of helpful walkthroughs and tutorials
[148.54 → 154.26] that cover server config and optimization so it's pretty easy to get your services set up we have a
[154.26 → 158.86] pretty awesome promo with them 10 bucks off so when you sign up you enter your credit card information
[158.86 → 164.88] on the billing page there's a promo uh promo code filled there go ahead and pop in our coupon code
[164.88 → 171.58] changelog that's not the changelog it's just changelog to use our 10 off promo so thanks much to
[171.58 → 179.70] digital ocean for their support go to digitalocean.com and uh that's kind of neat though Andrew we have a
[179.70 → 184.36] friend at pure trade that works with us that uh is about to move to their services Kelly you know
[184.36 → 189.44] his service get portly yeah he uh he's been using Linde and I think one thing that was
[189.44 → 193.78] pretty enticing about digital ocean for him was the fact they have private IPS now so he was like
[193.78 → 200.30] oh that's nice and yeah plus it's on SSD so it's superfast too but uh yeah he likes Linde but I think
[200.30 → 204.26] that he always kind of knew that um it was good to get started with, and he was going to have to migrate
[204.26 → 211.04] eventually, so yeah digital ocean loves it yeah it's a pretty good move oh yeah digital oceans uh
[211.04 → 215.72] one thing I've heard about is like it's just fast because it's a SSD but
[215.72 → 223.48] anyway let's get this really neat we use it to uh git lab is hosted partly on another provider but
[223.48 → 228.44] we all the new servers are on digital ocean we're really happy with them is that right, and it's nice
[228.44 → 233.24] yeah it's neat that they're sponsoring the show too of course double sponsor yeah double I mean
[233.24 → 239.48] yeah well we don't get a discount I guess, but it's its amazing price and value anyway so oh yeah
[239.48 → 243.94] yeah and the five bucks I mean they're they're basic plans so we get 10 bucks off it's basically
[243.94 → 249.48] two months free you know the easy way to say that I mean that's a super extended uh promo for
[249.48 → 254.72] digital ocean but we certainly appreciate the support of the show but uh um that's cool that you
[254.72 → 259.00] guys are using them too but uh let's get off the show Andrew you want to take the lead my friend
[259.00 → 264.96] yeah, yeah so uh cc why don't you kind of go ahead and give us so I don't we mentioned it before but
[264.96 → 269.50] we had a little sponsor so uh you're with git lab so why don't you kind of give us an intro
[269.50 → 278.34] the history or why don't you start with what git lab is why don't we go there git lab is a code and
[278.34 → 285.18] project management system um so you manage your git repositories in there's an issue tracker
[285.18 → 292.10] there's a wiki system you can manage users and all kinds of permissions and the whole goal is to
[292.10 → 299.94] collaborate as software developers um to do code reviews to communicate stuff um to work together
[299.94 → 306.78] more efficiently and to do a continuous delivery of your software supported by this management in
[306.78 → 314.68] git lab, so obviously that makes go ahead no does that make sense yeah it does and obviously for
[314.68 → 320.08] anyone that's listening that is familiar with it um I'm sure you have to answer the question with how
[320.08 → 324.56] you guys relate to GitHub and other you know those providers Bitbucket and those guys so we'll get
[324.56 → 330.94] into that a little bit later on in the show but um so basically git lab is uh just do you only
[330.94 → 337.30] support git or do you support other uh other version control systems to no we're uh git only
[337.30 → 345.98] obviously some people use it uh with SVN uh things, but there's no support in git lab for that
[345.98 → 351.12] gotcha why don't you go ahead and give us a little bit of a history um I think you guys are starting to
[351.12 → 356.76] gain some real traction, but you've been around for quite a while uh you're definitely not a brand new
[356.76 → 360.78] service, so there's some history behind you guys so why don't you kind of give us a little peek into that
[360.78 → 369.34] sure uh git lab was created in September 2011 by Dimitri marabout and Valerie CIO
[369.34 → 375.78] Dimitri continued with the project and is still the lead author, and he's a co-founder of me
[375.78 → 386.08] um a year after Dimitri uh made the project I started gitlab.com to uh also offer commercial
[386.08 → 393.50] services around git lab but then uh git lab was already out for a year, and it already gained some
[393.50 → 400.96] traction mostly from people who want to run their own uh yeah their own uh hosting service so
[400.96 → 407.36] on-premises within their company they uh or organization they want to be in control of their
[407.36 → 416.98] own repos and access and backups and git lab enables them to do so um a big step in the development
[416.98 → 425.76] of git lab in my view was uh version 5.0 when we got rid of all the dependencies on Tito light
[425.76 → 433.64] which is an awesome piece of software, but it allowed git lab to scale a lot better and to support like
[433.64 → 439.76] many thousands of users on one installation, and it's uh it's been open to source the whole time
[439.76 → 446.74] it's MIT licensed, and we got an awesome community around in contributing and helping people out
[446.74 → 454.42] I guess you mentioned uh being 5.0 is the last milestone you said you know kind of a shift for you
[454.42 → 460.14] but uh you recently celebrated 6.0 I think it was about like a week or two back week and a halfback
[460.14 → 471.04] yep it came out on the 22nd of the month of uh previous month uh it since 2011 it's always come
[471.04 → 478.46] out on that date so you can expect a new major or minor release on the 20 22nd of each uh month so
[478.46 → 484.88] that's something the whole community is always looking forward to uh 6.0 was also a major release
[484.88 → 492.66] um we added uh lots of awesome features most importantly the ability to combine groups of
[492.66 → 498.78] people and groups of projects so you can now have a group where you have a couple of developers in
[498.78 → 506.14] and then if you add projects to that group all the developers get their uh authorizations on the
[506.14 → 514.02] project automatically and vice versa and this makes managing uh bigger enterprise installations
[514.02 → 520.74] a lot easier but also for smaller companies like 50 people or 20 people or five people it's nice to
[520.74 → 527.72] be able to group uh projects and access and among of course there were many other changes and
[527.72 → 532.90] improvements uh as well, but this was the biggest one in the 6.0 release
[532.90 → 536.96] so the enterprise edition is new in the 6.0 release is that right
[536.96 → 545.98] yes we also introduced uh enterprise version um the difference from the community edition is that it
[545.98 → 555.62] has support for uh LDAP groups so you normal GitLab can sync to your company uh LDAP server for
[555.62 → 563.26] permissions and authorizations um, but this can also sync with your LDAP groups so everyone who is in your
[563.26 → 570.98] company LDAP server can also gain access to uh a certain group in uh GitLab it's its more feature
[570.98 → 579.02] for bigger organizations with more than 50 users and um this time this version is only available
[579.02 → 587.82] to subscribers of gitlab.com so that's our business model we make uh two books uh a month for every
[587.82 → 593.64] user uh that is using an enterprise edition so with that we've become a sustainable company
[593.64 → 603.20] and uh if we were really glad it was positively received in the community, and we're uh yeah we're
[603.20 → 610.42] trying to build on that to to to uh grow as a company and do even more improvements to GitLab
[610.42 → 618.22] the GitLab though sorry Andrew the I wanted to make this point because um the enterprise edition
[618.22 → 623.48] though is only available to subscribers of gitlab.com though right so like you got the community edition
[623.48 → 630.02] which you mentioned is open source and GitLab uh EE or enterprise edition is subscriber based is that
[630.02 → 639.42] right exactly okay so you, and you announced 6.0 on August 22nd and since then you've had
[639.42 → 644.14] a few weeks now so you kind of said that the reception has been pretty good with the enterprise
[644.14 → 648.94] edition but what does that mean how has the reception been you know specifically
[648.94 → 659.38] um we got a major increase in the number of subscribers um people who wanted the new features
[659.38 → 664.52] but also people who saw like we were really serious about it and that it's becoming a sustainable company
[664.52 → 673.52] um there were already lots of organizations using GitLab over 25 000 is our estimate and now all kinds of
[673.52 → 678.88] organizations came to us and said okay we'd like the enterprise version, or we'd like to support
[678.88 → 688.52] um so um we didn't have like multiple companies signing up every day before, and now we have that and uh
[688.52 → 697.80] um it was starting to gain major traction around the release uh the release some of the features in 6.0 were
[697.80 → 706.20] um made uh in discussions with some major enterprises, and we now have like three fortune 100 companies
[706.20 → 713.84] being paying customers of uh gitlab.com so that that was a major milestone for us signing up these big
[713.84 → 721.36] companies uh and working with them to make GitLab even better you kind of alluded uh in a
[721.36 → 726.56] conversation we had that uh there was a quite a bit of discussion that actually went around the licensing
[726.56 → 737.84] of the enterprise edition yes obviously making two versions is a major step and uh you can do it the
[737.84 → 747.56] wrong way or the right way and um obviously what oracle is doing to my SQL is is is not the way we
[747.56 → 754.38] wanted to do it um, and we thought the best thing would be just to talk to our community about it what
[754.38 → 761.14] our plans were and how we were going to do it so on gitlab.org uh about a month before the release we said
[761.14 → 766.32] okay these are our plans and this is how we're going to do it and then all the hard questions came
[766.32 → 774.04] about how are you going to license it um and that was a main point, and obviously we were thinking
[774.04 → 779.86] about a commercial license um all the extra code would be commercial code, and you couldn't copy it
[779.86 → 786.32] etc and some of the people in the community said well why don't you just put your faith in the
[786.32 → 792.72] community and just make it open source that's what we all believe in and people are going to be okay
[792.72 → 799.76] like the GitLab community is pretty awesome and nobody's going to be uh mean and and and redistributed
[799.76 → 806.00] uh why should they if we're being a good member of the community we can expect the rest of the
[806.00 → 812.40] community to be cool so that was a pretty convincing argument so we MIT licensed the
[812.40 → 821.12] enterprise edition which I think is pretty unusual for uh enterprise software uh you see it sometimes
[821.12 → 828.72] in smaller plugins and everything but this is a bit of an experiment uh and so far it's going really
[828.72 → 835.12] well and uh very positive response to it so I'm I'm proud that together with the community we could do
[835.12 → 843.12] this, and you saw it in when we released 6.0 that there was no everybody was happy about it how we
[843.12 → 849.92] approached it and and and the end results so really feeling good about the discussion we had
[849.92 → 857.44] especially with a user called bean in uh in the uh then uh the pre and uh pre-announcement let me ask
[857.44 → 861.04] a question here because there's some there I was reading some of the comments on your six-way release
[861.04 → 866.64] and then the link out to your enterprise edition and Andrew this kind of keys off of something we asked
[866.64 → 873.44] uh mike parameter when he was on about you know sidekick and sidekick pro which is like and the question in
[873.44 → 878.24] that I'm going to ask is basically from one of the uh comments here is like you know if the community
[878.24 → 886.64] develops your EE uh LDAP groups feature, and they want to push that into the CE edition uh I think you
[886.64 → 892.32] eventually had kind of a response too, but it was pretty much just um it would be appreciated so what was
[892.32 → 896.32] your official stance on like it seemed like there's some sort of divide there between the
[896.32 → 904.40] editions even though you were graceful and offered it as MIT yeah obviously um the the the that's a
[904.40 → 910.72] hard question to answer so what happens if somebody contributes a feature to the community edition that
[910.72 → 919.36] is already in the enterprise edition would uh would we merge that um I think the first question we're
[919.36 → 926.24] going to ask ourselves is why do people want this are we because we promised that
[926.56 → 932.48] any features we put in only the enterprise edition would be features that would be mainly useful for
[932.48 → 939.52] larger organizations and the fact that someone is contributing it to the community edition kind of
[939.52 → 945.20] indicates that maybe we're wrong maybe this feature is really useful for smaller organizations because
[945.84 → 951.92] we have pretty affordable pricing so if you're in a large organization you should have no trouble convincing
[951.92 → 959.68] uh the management of actually purchasing a subscription so so so why is this happening that that will be the
[959.68 → 964.40] first question, and we might be mistaken we might think about a feature that's only for large ones
[965.28 → 971.44] but it's also good for smaller organizations in that case we're wrong, and we'll just merge that code or
[971.44 → 979.36] enterprise code into the community edition if that's not the case I think it's its what would be important
[979.36 → 987.84] is the seriousness some of these features are non-trivial to make is the code that is contributed is
[987.84 → 993.76] that of a high quality did someone take it really serious to try to add this feature or is it just like
[993.76 → 1000.00] hey i I saw that this feature is missing and i i I tried to whip something up, but it's not that functional
[1001.04 → 1010.08] so if someone is serious that makes it uh more likely that will include it uh obviously if is the code
[1010.08 → 1018.32] was directly nicked from the um the enterprise edition that would be legal, but that would not be
[1018.32 → 1025.36] very cool yeah yeah yeah somebody it seems like one of your interests is like that uh I was just
[1025.36 → 1029.36] reading through is that you know some features can be kind of bottled up into because someone somebody
[1029.36 → 1033.92] suggested a plug-in system and then kind of making it where you know these enterprise features could be
[1033.92 → 1038.64] bottled up in plugins and just kind of added on like through some sort of subscription that you've already
[1038.64 → 1044.32] mentioned but that some of them are just kind of bigger interfaces to the application that
[1044.32 → 1052.80] it's just not easy to bottle up into a plug-in yeah there might be we have services we call them but
[1052.80 → 1057.36] they're the kind of function like plugins so we might have some enterprise things that will be able to
[1057.36 → 1065.20] package as a service that would be neat I like what for example vagrant is doing in this regard where their
[1065.20 → 1073.44] VMware plugin is paid and the rest of vagrant is open source but some of these features we would have
[1073.44 → 1080.64] to build a whole special interface into the community edition just to be able to build on top of that
[1081.36 → 1086.80] and what we don't want to end up is with a worse open source worse community edition because we want
[1086.80 → 1093.04] to build on top like that shouldn't be the goal so it's not always feasible to abstract something as a
[1093.04 → 1099.68] plugin so we'll do it if it's easy, but we're not going to complicate the codebase too much with git it's
[1100.64 → 1107.68] very easy to just keep two separate versions in existence so we'll rather do that then than then
[1108.32 → 1115.04] build all kinds of extra non-functional stuff that everyone has to maintain so speaking about the
[1115.04 → 1120.32] codebase um and i and again I want to kind of get into this a little bit but I'm sure you answer this
[1120.32 → 1126.32] question a lot um or kind of have conversations about this a lot but GitLab itself is hosted on
[1126.32 → 1133.12] GitHub, so why don't you kind of give a little bit of an insight into that decision and if is that's going
[1133.12 → 1138.72] to be a long-term solution or if you eventually would move GitLab over to GitLab, or you know whatever
[1138.72 → 1147.68] you would say to that yeah um we're we're trying to be really pragmatic about everything so pragmatic
[1147.68 → 1154.48] that sometimes it hurts so if it's about making something an awesome new feature for that people
[1154.48 → 1163.04] can use or building something just to serve our pride then we built an awesome feature that people
[1163.04 → 1171.92] can use, so the thing is we haven't gotten around to making public repositories so on a GitLab server
[1171.92 → 1177.36] everything is private and for most people running a GitLab server this is why they're running GitLab because
[1177.36 → 1185.60] they want unlimited private repositories um so most of the people are really happy with that and um
[1187.20 → 1193.60] building we wanna we're not against uh public repositories so we're accepting merge requests for
[1193.60 → 1200.16] that but um it would be a big change you have all kinds of problems like you don't know longer have
[1200.16 → 1205.76] a current user, so lots of code needs to be adapted, and we want to do it in the right way so that all the
[1205.76 → 1212.40] security uh tests and everything it doesn't become brittle uh so we haven't gotten around to it um
[1213.52 → 1220.88] if is somebody commit uh contributes it will a perfect code will merge it if there's a customer
[1220.88 → 1226.24] that really insists on it, we'll do it uh but so far everyone's really happy with the private stuff
[1227.52 → 1231.44] um but I think it's a question of time because there are people right now building
[1231.44 → 1240.56] uh fedora packages there are people building Debian packages um there's discussion on the Drupal mailing
[1240.56 → 1248.40] list about using GitLab so the pressure is on to uh to start supporting public repos so I think
[1248.40 → 1256.48] it's a question of time but uh yeah we're trying to be pragmatic about that does that make sense yeah so
[1256.48 → 1261.28] so basically right now just to kind of summarize and make sure I understand this correctly right now
[1261.28 → 1269.12] just because GitLab is itself open source and maybe gitlab.com the cloud is not the best solution
[1269.12 → 1275.04] for an open source project right now because there are no public repositories but eventually if that
[1275.04 → 1282.40] happens you would consider moving GitLab itself into GitLab to be hosted there uh yeah exactly, and we might
[1282.40 → 1291.76] have open uh open public repositories even before we move so we're just going to stay where the people are
[1291.76 → 1300.16] and right now uh GitLab is where the contributors are so we're not going to force anything on anyone
[1300.16 → 1306.96] just to be more proud our pride is in building something that people can use and that's stable and that's
[1306.96 → 1314.00] that's affordable and that's that's open and free and that that's our pride and yeah if we have to
[1314.00 → 1319.28] host somewhere else that's that's that's really fit for the purpose then that's okay yeah and that's
[1319.28 → 1324.16] a really cool attitude I think you know your kind of speak about the pride thing and I think that's
[1324.16 → 1330.00] something that in open source a lot of times kinds of takes over, and you know some projects not all i
[1330.00 → 1336.16] mean that thankfully not most, but you know there are some projects that seem like the maintainers of the
[1336.16 → 1340.48] project are very proud and it's their way it's its what they want to do not what the community
[1340.48 → 1345.44] wants and that's kind of anti-open source so it's really cool to see you know that at a company level
[1345.44 → 1350.40] you guys are all saying you know it's not about our pride it's about delivering what people want and
[1350.40 → 1357.84] I think that's really cool um have you kind of received any attention from GitHub itself the company
[1357.84 → 1364.88] or any of the team members about this uh no we haven't I think that maybe it's a matter of time
[1364.88 → 1368.96] before you would hear something as you guys continue to grow I mean you guys are getting
[1368.96 → 1375.60] very big over 10 000 stars on GitHub so uh the scope of this project seems to be exploding and
[1375.60 → 1382.64] it's real fun to watch it I'm sure they are I'm sure they are aware of us yeah definitely and I did want
[1382.64 → 1387.84] to so I was just going to point out their URL so while the listeners are listening and maybe go
[1387.84 → 1395.36] hang out there it's GitHub.com slash GitLab HQ yeah and there's lots of stuff more you know GitLab a lot
[1395.36 → 1401.68] of you guys that contribute back to the open source community a lot in areas other than just on GitLab
[1402.40 → 1406.80] uh and that's cool right so what other projects have you guys contributed back to the
[1406.80 → 1417.04] community besides just uh gitlab.com um besides the GitLab thing uh the other main project is GitLab CI
[1417.60 → 1425.04] so it's a very basic continuous integration server I think the cool thing about it is that
[1425.04 → 1430.08] it's really user-friendly so it's very easy to set up your projects you don't have to do
[1432.80 → 1438.72] set up new user accounts or new permissions it communicates with GitLab over the API, and it gets your
[1438.72 → 1445.52] existing projects, and you can set up a new project in under a minute the other thing that's really cool
[1445.52 → 1455.36] about it is that it's distributed by nature so your um your tests do not run on the CI server they can
[1455.36 → 1461.36] run somewhere else and this is the default setup so what we commonly see with people they set up a CI
[1461.36 → 1470.56] server, but the tests run on the server so um any project that runs on the server can access uh the whole CI
[1470.56 → 1478.72] server and that's a bit of a security concern and also maintenance and everything is complicated
[1478.72 → 1485.20] and the GitLab CI is distributed by nature and I think that's a pretty cool if you want to know more you
[1485.20 → 1493.60] should check out the architecture GitLab CI architecture uh blog post awesome so GitLab git is
[1493.60 → 1500.16] a so kind of to go back I read an article from one of the founders of GitHub about grit and how you know
[1500.16 → 1504.32] it kind of I don't remember if it was tom but one of them was talking about how they just were in a bar
[1504.32 → 1510.72] one night sat down decided to start writing the git bindings for ruby and so grit came about you guys
[1510.72 → 1516.40] have written a wrapper around that called GitLab git and uh kind of can you elaborate on what that is
[1516.40 → 1523.76] and why you decided to do that and and and how you chose to kind of use that architecture um
[1524.56 → 1534.88] I think it's a pretty minimal wrapper um it's uh it's because the grid project is a bit well there are
[1534.88 → 1540.24] lots of uh pull requests waiting to be merged in the grid project and I think that's why we have our
[1540.24 → 1551.36] own fork of the project um the thing that uh we built on that with a thing called uh GitLab shell yeah
[1551.36 → 1557.92] maybe that's that goes a bit too far now but uh it's its it's more of a fork with some additional
[1557.92 → 1565.84] fixes and things that we need than a replacement so yeah we're really grateful for uh the grid
[1566.56 → 1572.00] project that was uh contributed uh by GitHub yeah just to add some numbers to the mix here for
[1572.00 → 1578.48] for those listening uh I'm assuming this is the canonical repo which is uh tom press and Warner's
[1578.48 → 1586.56] uh username on GitHub which is majumbo uh that's majumbo right yeah slash grid and there are 63 pull requests
[1586.56 → 1591.68] uh waiting to be merged I think without throwing stones what do you think the reasons why there's
[1591.68 → 1596.32] so many pull requests waiting is it just that they're they're opinionated and maybe these
[1596.32 → 1602.24] pull requests don't really represent where they want to take grit no I'm I'm not sure I'm not yeah
[1602.24 → 1607.52] you'd have to ask him okay yeah it's a hard it's a hard question to answer the oldest pull request
[1607.52 → 1612.64] is from three years ago yeah so you would think that some kind of action would have happened on
[1612.64 → 1616.40] that pull request by now, but you know they got their reasons and why things are happening yeah
[1616.40 → 1620.32] not trying to throw stones just trying to see because you said one of the reasons why you did
[1621.36 → 1626.56] uh git lab git was that uh was that you know because of those being stacked up and obviously
[1626.56 → 1632.08] you had some motivation and inertia of where you wanted to take it so some vision for what grid could
[1632.08 → 1637.04] be so you had to essentially you know fort from where it was at and wrap around it and do some other
[1637.04 → 1642.56] things uh in addition to it so it sounds like you know just you can't wait for other community
[1642.56 → 1646.80] members to move if you're trying to move ahead of they are you know ahead of where they're at
[1648.00 → 1654.48] yeah and on the same time it's we know how hard open source is and keeping up with the issue
[1654.48 → 1660.80] tracker yeah is really hard, and you cannot expect the same people who write software to always keep
[1660.80 → 1668.48] maintaining it and investigating everything and our git lab grid is mostly for stuff we need so we're
[1668.48 → 1674.24] not trying to be a better project or something like that we're just trying to merge in stuff that
[1674.24 → 1679.44] we need yeah solve your own problems I think that's the problem I make was like is it you know what's
[1679.44 → 1684.48] the is it solving your own problems or is it you know I don't know just easy question answer
[1685.68 → 1694.24] well it's kind of so it's solving our own problems and I think um one thing infrastructure-wise that we
[1694.24 → 1702.16] did try to contribute that has some pretty unique functionality is git lab shell it is uh it uses
[1702.16 → 1713.52] the git lab API so it's a bit specific but it um it's a code that allows you to um host an ssh session
[1713.52 → 1719.84] and to have people download the code and clone the code and push the code so basically what Giotto light
[1719.84 → 1727.20] is doing with pearl this is doing with ruby code in a nutshell and I think that's uh that's a that's
[1727.20 → 1734.32] a pretty neat piece of work, and it might be a good reference for other people trying to do this so
[1734.32 → 1740.96] Giotto light is what you guys were using and that's what you said you replaced at git lab 5.0
[1740.96 → 1747.92] and that was with git lab shell is that right yes exactly okay awesome well you kind of talked about
[1747.92 → 1754.00] this a little bit I wanted to maybe shift gears a little bit um one of the things that we've kind
[1754.00 → 1758.00] of hit on a little bit now is and I've said a little bit quite a few in those sentences a little
[1758.00 → 1763.68] bit a little bit a little bit one of the things that we've talked about a small amount uh in the last
[1763.68 → 1768.88] couple minutes is building commercial company around open source yeah um, and you talked about
[1769.84 → 1775.68] you just mentioned something about uh issue trackers and how they can be hard to be hard to kind of
[1775.68 → 1781.92] keep up with as one core maintainer so at git lab you guys have a specific team of two people
[1781.92 → 1787.44] dedicated to the issues is that right can you talk about that yeah there are two people but
[1787.44 → 1793.60] they're not part of git lab.com they're part of the community so right I want to shout out to Ben
[1793.60 → 1801.92] bode miller and Robert chilling they're doing an awesome job on um keeping the issue tracker as clean as
[1801.92 → 1807.44] possible so trying to help people they're trying to close duplicate questions, and they're doing that
[1807.44 → 1814.16] in their spare time, and we really appreciate if it's one of the the most important things in
[1814.16 → 1820.00] open source, and we're really grateful if people step in to help out on the issue tracker and I think that
[1820.00 → 1825.92] that comes from a mindset of and you guys have it which is when you're very open to the community and
[1825.92 → 1830.56] and what the community desires I think your community that your specific community that
[1830.56 → 1836.56] comes up around you is open to giving back and I think with Ben and Robert that are obviously
[1836.56 → 1841.44] committing I mean the one thing that you don't you know you can't buy more of is time right you've
[1841.44 → 1845.92] heard that before, and so they're taking more of their time from whatever their regular jobs are to
[1845.92 → 1851.12] commit back to git lab and that's something that you get from a mindset of you know being open to the
[1851.12 → 1855.76] community and when you're truly open to what the community wants and willing to kind of shift in
[1855.76 → 1861.68] the direction that the community wants to take you I think you kind of uh can you know gain a
[1861.68 → 1869.52] lot of the joys of the community would you agree with that yeah but I think the community is
[1869.52 → 1875.84] doing a way better job than we are like I'd like to hang out a lot more on the the the campfire
[1875.84 → 1882.00] rooms and everything uh to to to help the community so we're not doing as good of a job as we could
[1882.00 → 1890.48] doing that we had some help from eve sen who is uh also working on the rails core, and he helped us
[1890.48 → 1898.40] well set up campfire rooms and help coach some people to become better contributors and better
[1898.96 → 1906.16] issue team maintainers um so yeah we just have awesome people in the community it's not
[1906.16 → 1915.52] it's its it's um it's not because of us but uh but because of the community that it's going so
[1915.52 → 1923.44] well yeah so what is the what's it like building a commercial you said that you've recently become
[1923.44 → 1930.88] sustainable is that right yeah with the introduction of uh git lab enterprise edition we've
[1930.88 → 1938.48] become a sustainable company and before that uh we took on uh consulting assignments to make ends meet
[1939.20 → 1944.08] and you're going to be working full-time at the end of the month on git labs is that right yes I'm
[1944.08 → 1950.00] finishing up the last consulting work and I can't wait uh to start working full-time I think it's an
[1950.00 → 1955.52] important point to camp out on for I know we talked a little bit about some comments we um heard back from
[1955.52 → 1961.92] those on the announcement of git lab 6o and then also the enterprise edition just like asking questions
[1961.92 → 1968.32] of why fork it or why have this divide or why have these separate uh options and I think you know maybe
[1968.32 → 1974.48] you can say this on your own but I think generally speaking to be sustainable um you know at some point
[1974.48 → 1980.32] you have to be able to sustain yourself through money and not do additional consulting and focus
[1980.32 → 1985.28] fully on git lab so that seems to be the answer to the question which is that's why you've done it
[1985.28 → 1993.44] to be sustainable yeah we've done it to be sustainable and because we saw there was a lot of demand for
[1994.16 → 2003.04] features that only larger companies would use and like there's we had um already for half a year uh
[2003.04 → 2010.96] git lab.com hired uh Dimitri as a co-founder to work on git lab full-time, and he's working all these
[2010.96 → 2019.52] uh awesome features but yeah the money has to come from somewhere and uh we need to uh um yeah
[2021.52 → 2029.28] having a paid product is a great way to make ends meet um and I think it's its uh there are also
[2029.28 → 2035.04] other things like donations we did that as well, and we're really happy with all the people who donated
[2035.04 → 2040.64] uh we also had a software as a service product so for some people that might be the best way to
[2041.52 → 2047.92] uh generate income, but we thought this was the best way for uh git lab.com yeah it's something we talk
[2047.92 → 2053.04] about a lot on the show because you know unfortunately if you get a pizza delivered to your house you can't
[2053.04 → 2059.92] pay it with contributions right you have to have money to pay bills so we talk about you know
[2059.92 → 2068.64] well let me respond to that um Dimitri called it ice cream money uh when he started but we
[2068.64 → 2075.92] had some very, very generous contributions come in we had uh companies donate uh a thousand dollars
[2075.92 → 2083.20] six hundred dollars like pretty big amounts so it's not that the community is not willing to uh pay up
[2083.20 → 2090.00] oh when I say contributions I meant uh like to the code itself like commit oh yeah
[2090.00 → 2096.24] sure I was confusing it with donations yeah no, no well that's the point is you know you unfortunately
[2096.24 → 2101.12] you can't pay your bills with code right you have to somehow make money whether it's through
[2101.92 → 2107.52] donations or you know some sort of business model or something, and so we talk about a lot on the show
[2108.16 → 2112.72] different business models that people have and this is one I don't know I mean maybe I'm just
[2113.52 → 2119.68] making this up but I have nothing to back this, but it seems like this type of business model where
[2119.68 → 2124.80] you have liked your open source product and then you kind of extend it for like an enterprise edition or a
[2124.80 → 2130.56] paid version or something like that this is kind of growing in popularity, and it seems that this model
[2130.56 → 2138.56] is growing in popularity specifically when your target um you know your target customer is a
[2138.56 → 2143.60] developer right because I think developers understand that this stuff isn't free that the people that
[2143.60 → 2149.60] are doing this still have lives they have families and bills and all this and that and so the I think
[2149.60 → 2156.48] that it's an it's a model that is lent to be successful because you know myself like I'm more than willing
[2156.48 → 2163.20] to give money to a project that I rely on to get my job done because I know that this guy has to do
[2163.20 → 2169.52] his job and the only way he can keep going is if he makes money and if he can't keep going then I don't
[2169.52 → 2176.00] have this project anymore to work with does that make sense yeah absolutely totally and what also
[2176.00 → 2182.08] comes into play is that uh many times the benefactor of the open source project is a company
[2182.88 → 2190.24] and in a company it's really normal to pay for software it's not so normal to do a donation yeah
[2190.24 → 2196.72] so for a lot of people who wanted to donate it was a much easier if we just said it was for software but
[2196.72 → 2202.80] yeah we can only do that if it really is for software so that's also why it's good to
[2202.80 → 2210.56] uh well to have a commercial offering so let me ask you this if so GitLab itself is open source and
[2210.56 → 2215.92] you guys are kind of reaching out to companies to start using this have you gotten any
[2215.92 → 2220.64] flack from companies that maybe a little more old-fashioned that aren't comfortable with the fact
[2220.64 → 2229.28] that your software is open source um no we haven't, but maybe that's because we're not reaching out that
[2229.28 → 2237.28] much I think the whole community around uh GitLab is doing the promotion and just we have enthusiasts
[2237.28 → 2242.64] and champions within companies that started using GitLab and saw it's a great fit for their organization
[2242.64 → 2249.52] and that's that's they reach out to us maybe when we become more active in doing outbound sales that we
[2249.52 → 2256.48] get that reaction, but most people are really comfortable with open source and yeah people see I think the
[2256.48 → 2264.16] benefit of having more eyes on the product right and maybe they like that there's a commercial
[2264.16 → 2270.96] company that has a lead developer that is like inspecting every last line of code that comes into
[2270.96 → 2277.20] the project maybe that helps, but we haven't had any negative reactions to GitLab being open source
[2277.20 → 2283.12] and it's again you have the community kind of or the clients are coming to you, you you mentioned to me
[2283.12 → 2287.20] that um GitLab is actually looking to hire and some of the roles you're looking to hire for
[2287.20 → 2293.28] our support and sales so do you said this already but you could see that happening a
[2293.28 → 2298.64] little bit if you're starting to reach out and do outbound sales and what is your response to that
[2299.20 → 2304.96] if that starts to happen if somebody says I like what you guys are doing i I like that it's all private
[2304.96 → 2309.92] but I don't like that the code itself is open source do you say they're not a good fit for you or how
[2309.92 → 2315.52] would you handle that oh I would ask why they say that like what is their concern are they concerned
[2315.52 → 2322.00] about security or about copyrights or what is their concern about people inserting back doors
[2322.64 → 2328.40] and all these questions I think have different answers and I think they all have a good answer
[2329.68 → 2335.68] but yeah it will be about the specific concern do you want me to go into the concerns no, no i just
[2335.68 → 2340.16] wonder if you guys have put any thought into that as a company you know and the only reason I bring
[2340.16 → 2346.56] it up is because you say you are looking to hire sales which I think is unique I think that companies
[2346.56 → 2351.44] that are open source with an enterprise edition don't often do much outbound selling I think that's
[2351.44 → 2355.04] a unique thing that you guys are going to do so I wonder if you guys have had those conversations at
[2355.04 → 2359.28] all, and you know if those questions come up or let you hire a salesperson are you going to want to
[2359.28 → 2365.60] train that salesperson on these questions and stuff like that yeah I think we'll see what we get for
[2365.60 → 2373.12] questions, and then we'll start answering them and and and and making notes um I think the the the sales
[2373.12 → 2379.20] vacancy we have at the moment is going to be inbound so just keeping up with all the requests that are
[2379.20 → 2384.96] coming in and making sure people have all the information and following up on all the questions they
[2384.96 → 2390.88] asked and all the wishes they have so uh we're hiring for that, and we're hiring for support making
[2390.88 → 2398.00] sure that uh you help people with their environment setting everything up making sure the backups are
[2398.00 → 2404.64] okay and and and doing high availability configurations so right now we're hiring for that and outbid sales
[2405.36 → 2411.60] that that's that's still in the future we just have trouble keeping up with the growth we're currently
[2411.60 → 2418.72] having so although I'd like to do even more sales let's let's first uh we're still doing a great job
[2418.72 → 2426.48] at servicing our customers but we need to hire in the very near future so if you're interested please
[2426.48 → 2433.20] let us know because we need you to grow further and keep doing a good job so on the on that note
[2433.20 → 2438.16] then what's your knowing what are some of the biggest challenges you face then I mean so if you
[2438.16 → 2444.72] you are it manpower is it you know we just talked about you becoming sustainable with
[2444.72 → 2451.20] with the enterprise edition what is the biggest challenge you face right now yeah good people are
[2451.20 → 2458.96] always are the challenge um and I think we've been able to hire some amazing people because they
[2458.96 → 2465.52] like being an open source uh but for example getting a person that wants to do inbound sales and is
[2465.52 → 2471.04] enthusiastic about that are not the people who come into contact with open source projects
[2471.04 → 2481.76] so i I think that maybe we should do some more marketing and uh PR in uh non-developer channels
[2481.76 → 2491.12] some outbound sales to get some inbound sales yeah yes but um yeah it's a very positive problem to
[2491.12 → 2499.84] have so that's uh that's okay and um I don't yeah that so far no, no major problems just keeping up with
[2499.84 → 2505.28] all the extra demands after we announce the enterprise edition that's right now the focus for the next few
[2505.28 → 2512.40] weeks yeah so you can look at GitLab's jobs at gitlab.com slash jobs let's shift from where we're at now
[2512.40 → 2517.52] with GitLab to what we can expect coming up um specific I know that you said that you guys don't
[2517.52 → 2521.36] have like a big road map so we'll get on we'll, we'll talk about that in a second but specifically
[2521.36 → 2528.08] for 6.1 what is going to come out with this release we have three big features coming out the first
[2528.08 → 2536.24] thing is issue referencing so when you uh commit in git you can write a commit message you can say
[2536.24 → 2546.48] something like fixes number 27 which means fixes my issue number 27 and all this kind of comments and
[2546.48 → 2553.52] links are all detected by GitLab and the appropriate uh comments are closed, and we normally work with
[2553.52 → 2558.80] feature branches which means that if you're going to solve a ticket you're going to make a new feature
[2558.80 → 2565.36] branch for it and then when you accept this feature runs there's a big nice green button that says accept
[2565.36 → 2571.12] and then right on top of there it will say well this will fix issue this and this and that, and it got
[2571.12 → 2577.12] that from the commit message you did earlier fancy stuff like that is now possible the other thing
[2577.12 → 2584.00] that was a popular demand for we call them sudo API calls which means that as an administrator you can
[2584.00 → 2592.56] do API calls um, and you can do them as another user so for example if you need to comment or move someone's
[2592.56 → 2599.20] project you can do it as that user so that you don't have any weird users showing up in the history of
[2599.20 → 2609.60] of stuff and the third major thing is project specific IDs like now if you open an issue for a project
[2609.60 → 2616.64] it gets a global I'd so suppose you have on your entire GitLab installation you have 100 issues it gets
[2616.64 → 2623.20] number 101 while on the project you just have 10 issues so it's not really logical that it's
[2623.20 → 2630.64] than number 101 when you have only 10 issues oh so we're gonna we're going to fix that and make sure
[2630.64 → 2638.08] you have project specific IDs and merge request IDs, so every project starts at issue one exactly gotcha
[2638.64 → 2642.88] awesome so that's coming out for six one I think it's interesting that you guys have no
[2642.88 → 2648.72] and you kept when we talked you kept talking about we have no road map we have no big you know
[2648.72 → 2654.88] audacious goal or no big you know private plan of where we're going so that kind of means that your
[2654.88 → 2659.68] your site and your vision is very close to what you're working on right now once you talk about
[2659.68 → 2663.76] like that I don't know if that was a decision or if you guys just naturally kind of you know
[2663.76 → 2669.60] organically grew into that but why don't you guys have some big road map why don't you have a
[2669.60 → 2677.68] a long-term plan we used to have this road map file in the repo um, but it wasn't maintained any
[2677.68 → 2685.84] longer so we deprecated it, and we found that normally when we when an um a release is almost done so most
[2685.84 → 2691.76] of time it's a few days before the 20 seconds Dimitri kind of knows what he wants to work on the
[2691.76 → 2697.84] community knows what they want to work on um, but you just figure it out then right there and then so
[2697.84 → 2703.04] you're done the stress is gone, and you think oh I'd like to work on this or that or I heard so many
[2703.04 → 2710.00] people complain about this or that and these things you cannot predict them two weeks or a month in
[2710.00 → 2715.36] advance sometimes you can, but sometimes you can't, and we want to be working on the things that inspire
[2715.36 → 2724.00] us and that are important to the community and to the clients of gitlab.com so why work on something less
[2724.00 → 2730.08] important just because you said so a month ago so we don't want to end up in that situation and
[2730.08 → 2736.48] I think David Heinemeier Hansson said it very eloquently when he said inspiration is perishable
[2737.68 → 2743.52] if you're inspired by something just go work on that, and we try to keep that alive that's true because
[2743.52 → 2748.96] I mean you hit that moment whenever you I mean especially as ingrained in the communities you're
[2748.96 → 2755.04] trying to be considering you know you're so grassroots in your efforts that you know you
[2755.04 → 2760.48] can't operate off of a road map if the inspiration comes from your know like this conversation we're
[2760.48 → 2765.52] having today like you might be inspired by something we suggest or the part of the conversation that
[2765.52 → 2769.76] reminds you of something you're not going to want to wait two months to go and work on that you're
[2769.76 → 2776.80] going to want to take care of it like at that moment because it'll perish exactly and if it's
[2776.80 → 2784.40] important it will come back and last but not least many new awesome features such as the sudo API
[2784.40 → 2792.48] calls they're contributed by people so we couldn't have protected predicted that um that comes up and
[2793.12 → 2799.20] at a certain point they're ready, and we can merge them, and then they're in the next release so uh um it's
[2799.20 → 2805.04] it's its it's useless to try to predict a community we just have to go with their flow
[2807.20 → 2813.76] yeah I think that this is something and this is something that I think about a lot working uh as a
[2813.76 → 2820.64] developer full-time it's incredibly I don't know if the word the right word but stressful to think about
[2820.64 → 2827.60] like long term like you know in six months we're going to want to do this feature and to me when we
[2827.60 → 2831.92] start and Adam knows like I think he could probably laugh because he actually when he starts
[2831.92 → 2835.84] talking about features that are like more than today's work he says Andrew's going to kill me
[2835.84 → 2841.36] for bringing this up, but you know it's funny because I think as developers we do like to be inspired and
[2841.36 → 2848.24] work on what is current and what is currently important right so it's its like I want to know what
[2848.24 → 2854.16] I'm working on right now so I can, you know my thoughts and my brain cycles are not unlimited and I want to be
[2854.16 → 2859.04] able to devote it to what's important and when I have to spend a ton of time thinking about you know
[2859.04 → 2863.84] does this match the roadmap does this match the six-month plan that's just overwhelming right it's
[2863.84 → 2868.88] stressful and I don't think it really I don't how often do companies actually stick to their roadmap
[2868.88 → 2876.08] you know and so when you have the open source community that's very um I don't know active with
[2876.08 → 2880.00] your project I feel like a roadmap would lock you into something that maybe wouldn't be
[2880.00 → 2886.96] the best idea you know all the energy you spend on the roadmap it's wasted um so you'd have
[2886.96 → 2892.96] uh before feature branches you'd have people at companies who are called release managers like
[2892.96 → 2899.28] most companies still have them if you do uh server software as a service product you don't need a
[2899.28 → 2905.04] release manager you can do continuous delivery, and you can just deliver the features as they are completed
[2905.04 → 2911.60] there's no need to do a release there's no need for git flow please use feature branches and just
[2911.60 → 2918.96] release what's ready, and you can that the release manager can do something else and be productive and no one
[2918.96 → 2925.68] has to stress out or fight about which features get in which release which is not adding anything so
[2926.40 → 2934.32] yeah I feel really strongly about this as you maybe notice and I'm really glad we're able to practice what we preach
[2936.00 → 2942.48] what were you going to say Adam I was just going to say on the idea of roadmaps um something that
[2942.48 → 2949.84] that I heard from somebody pretty respected actually from 37 signals um a while back I had Ryan singer on
[2949.84 → 2955.60] a different show I hosted for a while called the entry radio show, and you know it clicked when he
[2955.60 → 2960.32] had mentioned this thing this idea because he's a product manager at 37 signals so he tries to know
[2960.32 → 2963.84] where they might want to go, but he doesn't let that impact how he works today
[2964.96 → 2970.40] and i kind of lament on how he said it in its trajectory like knowing where you want to end up
[2970.40 → 2976.80] potentially but being able to kind of deviate along the path along the way you know based on this
[2976.80 → 2981.44] perishable resource called inspiration, or you know feedback from the community or whatever but you kind
[2981.44 → 2985.44] of have an idea where you want to go it's not exactly a road map it's like an idea of where you might
[2985.44 → 2991.44] want to be i kind of think of it like that well I mean yeah if git lab for instance like git lab is
[2991.44 → 2998.08] not going to switch from doing you know like version control hosting to you know playing music
[2998.64 → 3004.72] right like they there's no road map they know in a year they there are some things that they
[3004.72 → 3010.08] know right they still want to be a company so yeah that's a given they want to still be doing git and
[3010.08 → 3015.36] you know but that what they don't know is you know what if the community comes up and starts
[3015.36 → 3021.44] saying like we really want support for x whatever that feature is well that feature could
[3021.44 → 3025.52] be a huge thing a small thing whatever but as long as they have the mindset that they're being flexible
[3025.52 → 3031.04] and they're willing to you know go in that direction then that could drastically change the
[3031.04 → 3036.08] road map right so if there was a road map it could be altered greatly if you have a flexible
[3036.08 → 3041.76] mindset and I think that's what's scary is if you are road map driven, and you're not willing to
[3041.76 → 3048.32] uh move drastically away from that road map you know I guess there are two extremes right you could be
[3048.32 → 3054.16] kind of chasing every little rabbit trail of every little potential feature but when you think of it that
[3054.16 → 3059.76] way those rabbit trails tend to be bigger features yeah you have your core product and your core product
[3059.76 → 3067.44] it doesn't change that much it can change your in the feature set but as long as you're you're not
[3067.44 → 3073.52] chasing down you know core rabbit trails where your core changes drastically I don't think you want that
[3073.52 → 3077.92] road map I don't think you want to know where you want to be at maybe where you would like to be at
[3077.92 → 3084.40] business wise but to sit down and say I mean how I think that we all can understand and all can admit
[3084.40 → 3089.44] that if you try and sit down and talk about features and where you want your feature set
[3089.44 → 3098.32] to be in 12 months that you're you're not you're not going to accurately estimate or predict what's
[3098.32 → 3101.44] going to happen that's the exact same thing I was going to say it was you're not going to accurately
[3101.44 → 3106.64] depict the future like that it's going to be a rough estimate yeah totally with you on that one for
[3106.64 → 3112.16] sure yeah and I think that the problem is a lot of companies invest a lot of time trying to figure
[3112.16 → 3117.76] how they can accurately predict 12 months down the road, and it's like why if the sooner that you can
[3117.76 → 3122.16] embrace the fact that you can't predict 12 months down the road the more that you can realize that
[3122.16 → 3126.40] you're wasting time and money on trying, and you can invest that time and money into what's happening
[3126.40 → 3134.48] right now and that's important yeah I totally agree and great quote of Ryan as a product manager I think
[3134.48 → 3141.68] what you're trying to do if you're making a road map you're drawing roads on a piece of paper that
[3141.68 → 3148.00] doesn't that doesn't have a map it doesn't it doesn't list the terrain you're in yeah so you're
[3148.00 → 3154.80] drawing this this this path you will take, but you're not taking into account the train
[3154.80 → 3160.64] because the terrain like it's hard to see how much effort stuff will be or what's important or what
[3160.64 → 3167.44] what's the weather going to be so you don't want to draw exactly which path you'll take you need a direction
[3167.44 → 3172.88] like we're going over there northeast because that's yeah that's our goal, and then you'll figure out
[3172.88 → 3179.68] how to get there and which streams to cross and which uh which route to take along the way
[3179.68 → 3187.12] and you know your direction, and we also know our direction we want to polish GitLab CI a bit more
[3187.12 → 3194.64] because right now it's a bit rough around the edges we want to package GitLab better because right now
[3194.64 → 3200.48] you have to install it by hand we have a perfect installation manual but still if we make it
[3200.48 → 3207.36] easier to install then more people would install it which would be awesome, so these are things you know
[3207.36 → 3214.00] okay this is the direction we want to go, but we'll see how we get there right and what tomorrow brings
[3214.00 → 3220.72] and we'll just look look look up look around and see which is uh what pull requests are coming in from
[3220.72 → 3230.56] people gotcha so what's on the roadmap for uh it's cool no I think that that's a man it's almost like
[3230.56 → 3235.12] you could do a whole nother talk a whole nother not even just talk a whole nother show about you know
[3237.76 → 3242.40] I don't know if procedure is the right word but you know what's the solution right I mean you
[3242.40 → 3247.44] kind of talked about knowing the direction you want to head well you know how do you know the direction
[3247.44 → 3253.84] you want to hit how can you accurately talk about a direction without talking about goals and i
[3253.84 → 3257.20] think that there's a there's something there and whoever can figure it out and bottle it up I think
[3257.20 → 3262.64] you'll become you know a billionaire on figuring that out because there's obviously been companies
[3262.64 → 3268.56] that have been I mean that's what release managers do that's what you know that's what these people do
[3268.56 → 3272.24] and so there have been companies that have been investing tons of money and time into trying to be able to
[3272.24 → 3277.92] figure this out and I think if you can figure it out and figure out not just you know it's not just
[3277.92 → 3283.20] figure out what I want to do in 12 months, but it's figure out how can I get us going in a direction and
[3284.08 → 3289.84] maintain the mindset that we're going to be flexible but at the same time I don't want to jump ship on this
[3290.48 → 3295.84] value because it hasn't panned out in the first two weeks so I need to give it you know give it its due
[3295.84 → 3300.96] diligence right so if you can figure all that out then you know more power to you and bottle it up and sell
[3300.96 → 3308.40] it and then hire me at your company to just collect a paycheck yeah it's its it's really
[3308.80 → 3316.16] good product managers are really, really valuable I think uh at git lab we just talk
[3317.76 → 3324.08] within the company but also with the community and we just um see where we're going, and we're
[3324.08 → 3329.76] driven by Dimitri's dream to give awesome tools to developers yeah and I think that the mission
[3329.76 → 3337.44] is a bit expanding into just collaboration in general I think git is an awesome tool to collaborate
[3337.44 → 3345.20] and to be flexible like people used to send an email with an attachment, and then you edit something
[3345.20 → 3349.92] and you send it back, and they send it to three other people, and now they have a problem and these
[3349.92 → 3355.20] things are going away and version management is going to solve it, but it's really hard to do it in a
[3355.20 → 3362.40] user-friendly way and there's uh there's a whole wide open space about working together on code but
[3362.40 → 3368.80] also on technical documents legal documents and eventually everything that's digital will be
[3369.44 → 3375.76] version controlled and people are starting to figure that out but I think it will be as important
[3375.76 → 3382.96] as web servers uh these collaboration servers and I think there should be a perfect free one
[3384.08 → 3392.32] that uh everyone can use in freedom and then that's that's that's what i how I see git lab but
[3392.32 → 3398.00] Dimitri might say something else, and we have to figure that out as we go along and listen to our users
[3398.00 → 3404.56] and to the people in the community yeah so it's been two years and you guys are at 6.0
[3405.44 → 3411.76] do you would you say that you put out another major release you know you bump the version in a major
[3411.76 → 3418.16] number um every four months or so is that proven to be pretty accurate yeah that's pretty accurate
[3419.84 → 3424.48] cool so we can expect to see 7.0 coming out in the next three or three months or so that's exciting
[3424.48 → 3431.20] Christmas yeah it'd be Christmas present huh oh that would be nice yeah yeah all right so we
[3431.20 → 3435.36] I think that we could uh there's plenty more we could talk about, but we do try and keep the show under
[3435.36 → 3441.92] an hour or to an hour I think we're we're about reaching that point now uh we ask our guests the
[3441.92 → 3448.00] same questions at the end of every show, and so I'll uh go ahead and ask you now since I didn't prep you
[3448.00 → 3455.92] with these so don't kill me for putting you on the spot with these um, but our first question is and
[3455.92 → 3460.96] I'm drawing a blank right now on what the question is called arms yeah so first question
[3460.96 → 3465.20] for the community you guys obviously have a very active community so I'm not sure that you know
[3465.20 → 3471.84] there's anything specific but what would be something that you would like to see the community kind of
[3471.84 → 3479.04] rally around and work on or even better way to put it is there a feature specific feature
[3479.04 → 3483.12] that you think is missing from GitLab that you would like to see somebody kind of get involved with
[3484.88 → 3492.24] well if i I'd have to do a call to arms I would say help people out using GitLab, so there are IRC
[3492.24 → 3498.48] channels there's an issue tracker there's a mailing list and people are asking loads of questions trying to
[3498.48 → 3506.56] figure out the problem trying to see how they have to configure something if you want to help GitLab
[3507.20 → 3515.04] please help out these people um it's its it needs to be the community is doing awesome job helping
[3515.04 → 3523.04] these people, but there is a lot of room for further improvements not there's room for better answers and
[3523.04 → 3529.52] and yeah just pick your favourite medium if it's tech overflow on our RC channel but help out these
[3529.52 → 3536.64] people with uh with GitLab questions that's that's that will be my call to arms and of course yeah if you
[3536.64 → 3544.48] if you need an awesome feature yourself please make it and contribute it, but there's no need to go
[3544.48 → 3551.12] go around looking for something uh something to make something you want to don't make somebody something
[3551.12 → 3557.28] somebody else wants that's the most important thing so you're inspired to do a good job, and you know
[3557.28 → 3564.88] what you want that's good advice yeah what about um so if you weren't doing what you're doing now and
[3564.88 → 3570.00] and I asked that question let's say assuming it's a month from now, and you're working on GitLab full-time
[3570.00 → 3575.60] and if you weren't doing that what would you like to be doing instead I would like to learn
[3575.60 → 3585.44] uh JavaScript and play with node I listened to your episode with Isaac the uh uh rpm and the NPM
[3585.44 → 3592.16] maintainer yeah um that sounds awesome I'd like to know more about that and play with it, I'm a ruby
[3592.16 → 3600.16] developer I love ruby but um it would be good to learn a second language in a good way so I do that
[3600.16 → 3606.80] awesome and our last question is a programming hero or somebody that you have been influenced
[3606.80 → 3612.64] by greatly in your life that you would like to give a shout-out to I want to shout out to Yehuda cats
[3612.64 → 3623.84] um he's uh core on mere rails jQuery amber making skylight application but also making a
[3623.84 → 3633.68] Tōkaidō application and that is to help people install uh Ruby on Rails easily on their uh max um
[3634.24 → 3642.56] it's just amazing how much he has given to open source um I don't believe he's actually one person
[3642.56 → 3649.52] there must be three more in a basement somewhere many Yehuda but yeah many Yehuda it's its just
[3649.52 → 3657.20] amazing what he has done and I greatly respect that, and we cannot stand in even near him compared to
[3657.20 → 3663.52] our contributions um I think uh that it is it's really awesome that there are people like him and
[3663.52 → 3670.48] he's a great inspiration to me personally I'm always uh I'm always inspired by some of his tweets
[3670.48 → 3674.48] where he's like hey I'm hacking on this anybody going to have any anybody that knows something about
[3674.48 → 3678.80] this like he's still humble even though like as you said you don't deserve to stand next to him
[3678.80 → 3685.04] compared to contribution I think he's a pretty uh humble person and speaking of Yehuda as your
[3685.04 → 3692.32] hero Andrew are we still in talks about getting him on to talk about uh the latest ember release and
[3692.32 → 3698.88] whatnot like a couple of weeks yeah we're still trying to work it out but hopefully um uh yeah hopefully in
[3698.88 → 3703.44] the next few weeks we'll be talking with him about ember and uh yeah it'll be a good one yeah that's good
[3703.44 → 3711.12] stuff well yeah uh we definitely um appreciate you coming on the show see it say I mean the work you
[3711.12 → 3717.12] guys are thanks for having me yeah absolutely I mean the work you guys are doing is really
[3717.12 → 3721.12] inspiring um definitely the way you're leading the community and listening to the needs the community
[3721.12 → 3727.84] is super inspiring so uh appreciate you coming on the show um want to give another shout out to our
[3727.84 → 3733.20] sponsor digital ocean definitely cool that you guys actually use them for one uh and two that
[3733.20 → 3737.76] they're sponsoring the show because it helps us uh sustain so I mean that's that's what helps us
[3738.56 → 3743.68] make sure that Andrew and I can show up here every week and talk to people uh like zits about what
[3743.68 → 3748.72] they're working on and give shout-outs to people like Yehuda and others on the work they're doing so
[3748.72 → 3756.64] you can go to digitalocean.com and plug in our coupon code changelog to get 10 10 bucks off
[3757.60 → 3762.40] your subscription so do that whenever you feel like but to the listeners thanks for tuning in
[3762.40 → 3769.60] we'll be back uh next week not uh that's that's kind of a neat show we'll put something in the email
[3769.60 → 3773.76] so if you're not subscribing to uh the changelog week that you've got to go to the changelog.com
[3773.76 → 3778.56] slash weekly it's where we're putting uh our updates as well as tons and tons of other stuff
[3778.56 → 3783.12] that hits our radar that we don't always have time to hit uh hit up on the blog so definitely a huge
[3783.12 → 3789.76] Saturday read uh and that's pretty much it so lets uh let's say goodbye guys thanks so much again man
[3790.64 → 3795.20] goodbye thanks for having me awesome that you're doing this show on open source great work
[3795.20 → 3801.76] thank you we'll uh we'll see you everyone next week later later later
[3803.76 → 3824.80] Allen
[3825.52 → 3827.52] you
