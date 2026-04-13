[0.00 → 16.60] let's do if it's go time welcome to go time your source for wide-ranging discussions from all
[16.60 → 24.30] around the go community find us on the web at gotime.fm on the Fediverse at go time at changelog. Social
[24.30 → 31.54] and on x at gotime.fm thanks to our partners at fly.io the home of changelog.com launch your app as
[31.54 → 37.68] close to your users as possible find out how at fly.io okay here we go
[37.68 → 49.30] our friends at fire hydrant offer modern engineering teams less stress from ring to retro
[49.30 → 57.60] full end-to-end incident management alerting on call and of course streamlining every aspect of
[57.60 → 65.24] your incident process from webhook to alert trigger to notifications to incidents open to retro tasks to
[65.24 → 72.62] meantime to x analytics everything is inside fire hydrant for modern engineering teams and what
[72.62 → 77.40] you're about to hear are real reactions from pager duty users when seeing signals from fire hydrant
[77.40 → 83.20] for the first time pager duty I don't want to say they're evil, but they're an evil that we've had
[83.20 → 89.06] to maintain I know all of our engineering teams as well as myself are interested in getting this moving
[89.06 → 95.78] the correct direction as right now just managing and maintaining our user seats has become problematic
[95.78 → 100.88] that's all that's that's perfect actually this is a consistent problem for us and teams is
[100.88 → 106.48] that covering these sorts of ad hoc time frames is very difficult um you know putting in like
[106.48 → 113.24] overrides and specific days and different new shifts is quite onerous oh, and you did the most
[113.24 → 118.10] important piece which is didn't tie them together because that's half the problem with pager duty
[118.10 → 123.86] right is I get all these alerts and then I get an incident per alert and generally speaking
[123.86 → 130.64] when you go sideways you get lots of alerts because lots of things are broken, but you only have one
[130.64 → 136.40] incident yeah I'm super impressed with that because being able to assign to different teams is
[136.40 → 141.54] an issue for us because um like the one alert fires for one team, and then it seems like to
[141.54 → 146.78] have to bounce around, and it never does uh which then means that we have tons of communication issues
[146.78 → 153.26] because like people aren't updated any I mean to be open and honest uh when can we switch
[153.26 → 160.90] okay the next step is to go to firehydrant.com slash signals assemble the team and work the problem
[160.90 → 166.54] without a single swivel of the chair fire hydrant delivers end-to-end incident management and on-call
[166.54 → 173.66] learning for the modern software teams get started for free once again firehydrant.com slash signals
[173.66 → 198.74] my name is Natalie and I'm joined again by the three mosquitoes uh Roland Nicola and Filippo how are you
[198.74 → 205.48] doing well we are fine thanks what is your favourite fencing style speaking of musketeers
[205.48 → 212.96] can be instead of the unpopular opinion yeah the only thing I know about fencing is the term
[212.96 → 219.38] pay EP because it's used in the crossword all the time but I have no idea what it actually means
[219.38 → 226.94] so my answer is karma but I don't actually know if that's the that's that English in English you
[226.94 → 233.96] also use the same name or not yeah the one with swords I think that's probably three types of those
[233.96 → 240.80] there's one where you can only uh stab in like specific parts of the body there are ones where
[240.80 → 245.60] you can only get points if you attack and one is all the rest we can consider switching the
[245.60 → 252.30] unpopular opinion for that part fun trivia I used to be a fencer all the way all through high school
[252.30 → 260.28] I love talking about that plus it's all for one three for one or something yeah third episode so
[260.28 → 267.62] exciting things will come with go 123 when you said uh part three in my head I thought oh maybe it's
[267.62 → 273.08] part three or five, and then we'll be done, and we'll not need to make any changes any more right
[273.08 → 282.50] the security trilogy ends but yes as Ron was saying earlier work is never ending
[282.50 → 289.90] yeah that's probably a good thing though you know provides a level of job security that is
[289.90 → 294.96] or we're not supposed to talk about this in public
[294.96 → 303.04] anyway yes go on 23 lots of nice stuff coming there's a bunch of crypto TLS things
[303.08 → 310.26] coming from Roland so you know I'm getting you started yeah we can start with that yes crypto TLS i
[310.26 → 317.22] think we it's you know probably one of the most used packages that we have in the crypto subtree
[317.22 → 323.12] whether people kind of know that they're using it or not you know if you're using a net http client
[323.12 → 330.78] you probably use crypto TLS without ever knowing which is nice this hasn't been many major
[330.78 → 336.86] protocol changes for a while kind of the big thing that is coming down the road now is what's referred
[336.86 → 344.04] to as encrypted client hello which is not a particularly great name if you have no idea about
[344.04 → 351.50] the semantics of TLS handshaking uh and used to be used to be there was a precursor effort that was
[351.50 → 360.40] called encrypted SNI encrypted server name indication which is um when you handshake when you do a TLS
[360.40 → 368.78] connection because in you know most modern web servers now you have a single server serving a lot
[368.78 → 374.96] of different websites you could have there's a little field that happens during the TLS handshake that
[374.96 → 381.38] says which server you're actually trying to connect to you know you're connecting to 1.1.1.1 but actually
[381.38 → 387.92] you want to connect to you know dns.cloudflare.com I forget what the host name they actually use is
[387.92 → 393.30] but um so you provide that little piece of information that lets the TLS stack know this is
[393.30 → 398.44] who I'm actually trying to talk to, but privacy people quite rightly brought up the fact that this
[398.44 → 405.28] kind of leaks in plain text who it is that you're trying to talk to so you know we have the network
[405.28 → 410.86] stack has slowly been trying to get rid of these privacy blind spots, and we have you know we now have
[410.86 → 415.68] secure DNS so someone who is just watching your network traffic cannot see that you're looking
[415.68 → 422.94] up the IP address for cloudflare.com but as soon as you do a TLS handshake you're leaking this
[422.94 → 428.96] information saying actually hey this is exactly who I'm looking for so the idea was to change TLS to
[428.96 → 435.18] allow you to kind of mask this information, so this is what is now called encrypted client hello
[435.18 → 440.40] which i I won't get into the details of the actual protocol changes because it's not particularly
[440.40 → 446.46] interesting, and it's very complicated but I think this is a really nice change that will for
[446.46 → 453.66] most people be completely transparent I think the idea is that once we have support for it in go we will
[453.66 → 460.14] be able to wire up the net http clients and everything that relies on that so that assuming that you are
[460.14 → 467.40] using secure DNS which is another problem that while there is a solution for it, you know who knows
[467.40 → 473.90] how many people are actually using it there will be kind of we're slowly reducing the kind of privacy
[473.90 → 481.56] leakage that happens when you try and connect to servers which is nice, and you know for 99 percent of
[481.56 → 487.58] users this will just they will get this win transparently you won't have to do anything there will be some
[487.58 → 494.62] you know people doing strange things with TLS will probably need to make some changes, but they are
[494.62 → 502.72] thankfully in the minority of people yep there's an also an interesting API angle there because each
[502.72 → 511.78] uses a different specification called oh I pronounce it wrong every time uh hike yeah hybrid public key
[511.78 → 520.16] key encryption yes and each is encrypted client hello hike is something that will probably end up
[520.16 → 527.60] wanting to maybe I'm not committing to anything exposed in the standard library and so Ron's first
[527.60 → 533.36] iteration is a useful starting point to figure out what the API should be because hike is one of those
[533.36 → 540.94] things where you can combine everything with everything else, and we hate exposing those in the standard
[540.94 → 547.64] library so we should, we'll have to figure it out typically we try you know this may sound kind of mean
[547.64 → 554.18] but typically we try to give people as little options as possible turns out that making things highly
[554.18 → 562.20] configurable is often what leads to extremely painful bugs so you know we try and provide APIs that are
[562.20 → 568.90] very easy to use and don't require a huge amount of thought problem with hike is that it provides you
[568.90 → 576.48] a huge amount of options and how you know how to use it is complicated so if we are lucky that we are able
[576.48 → 583.20] to kind of land a first try implementation get some experience and actually using it inside the standard
[583.20 → 590.50] library ourselves and then see you know how could you use this incorrectly and then slowly file
[590.50 → 596.62] away those edges before we publicly propose an API that that everyone else will have to use because
[596.62 → 601.10] once we land something in standard library it's kind of set in stone so we really want to try
[601.10 → 607.10] try and get it right the first time as much as possible the other thing that's coming to crypto TLS
[607.10 → 614.64] in 123 is post quantum connections uh did we talk about post quantum last time I don't think we
[614.64 → 621.58] talked about it in the first episode six months ago yes so yes you know alongside hike and the elliptical
[621.58 → 627.86] curves right so I'll keep relatively short what post quantum is it's just maybe quantum computers are
[627.86 → 634.86] coming maybe not the maybe yes is a little too big to ignore it uh and if they can, they will be able to
[634.86 → 641.50] decrypt everything retroactively and we kind of don't like that so symmetric encryption is fine so
[641.50 → 649.28] you know the ciphers uh are fine as is fine cha-cha 20 poly 1305 is fine the thing we need to do
[649.28 → 658.08] something about are the key exchanges which right now is p2 elliptic curve uh Diffie-Hellman so p256 or
[658.08 → 665.28] curve 25519 and so on, so there are these new things these new algorithms the're called chems
[665.28 → 673.54] what happens since the six months ago is that NIST put out drafts for uh how the specification of the
[673.54 → 681.28] one they selected should work, and we landed an internal implementation yesterday I think something like that
[681.28 → 688.02] yeah yeah two days ago maybe two days and yesterday there was uh you sent a performance optimization
[688.02 → 693.52] if I remember correctly yeah because I figured there should always be a cl waiting for Roland's review
[693.52 → 700.48] uh just to keep him on his toes uh and yeah so we have an implementation in standard library
[700.48 → 708.48] I went specifically only for 768 which is one of the parameter sizes which I'm hoping everybody will just
[708.48 → 713.26] use that and I'm hoping we'll get away with only supporting that for as long as possible which is
[713.26 → 720.62] probably like a year or two, but anyway we're not exposing that in the standard library in 123 the plan
[720.62 → 728.96] is to wire it into crypto TLS uh so that if you connect to an another TLS peer that also supports
[728.96 → 736.78] these post-quantum hybrids by the way uh that use both the new stuff and the old stuff so that you know
[736.78 → 744.24] if we get the new stuff wrong it's not worse than uh using the old stuff and this is a whole debate by
[744.24 → 752.08] the way uh which we're going to elide here, and we're going to use the uh to implement this and
[752.08 → 759.48] it does make handshakes a little chunkier a little bigger which hopefully is not too much of a problem
[759.48 → 764.48] hopefully it's something that we can just turn on people don't notice and suddenly their connections
[764.48 → 770.74] are sometimes post-quantum secure but yeah we're rolling it out just as an experiment initially
[770.74 → 778.02] just like uh hike uh then thinking about what the right API to expose it is going to be
[778.02 → 784.58] are you collecting some metrics or feedbacks about that metrics that would be great it would be great
[784.58 → 791.68] to have those, but we don't get to have those so you're looking for feedback yes, yes it you know
[791.68 → 796.54] it works like we put things in the release candidate, and we tell people to test the release
[796.54 → 800.90] candidate and nobody tries the release candidate, and then we make the release because we say great
[800.90 → 806.00] we did not break anybody and then the release comes and everybody comes out and says that we broke them
[806.00 → 811.04] so you're asking now security people anybody who has like extra focus on security in their
[811.04 → 816.92] tools to try the release candidate no, no that's the thing it's not about security focus I don't need
[816.92 → 821.66] anybody to like I mean if they also want to review the security of it great but no, no we just need
[821.66 → 828.16] people who use crypto TLS which like Roland was saying is everybody to try the release candidate
[828.16 → 833.82] anybody who uses net http to try the release candidate yes everybody should always try the
[833.82 → 838.22] release candidate because we are so happy when you show up with bugs during the release candidate period
[838.22 → 845.96] and so not as happy when you show up with bugs like a month after the release and not every bug can be
[845.96 → 851.42] found in you know canary but consider that the release candidate is what google uses internally
[851.42 → 860.64] for production so you can stick it on a lab machine or to check if I don't know it still connects to your
[860.64 → 867.38] old I don't know firewall that's been living in a closet with no power and nobody really knows how
[867.38 → 874.18] it's still running and everybody's afraid to ask but somehow that one rejects handshakes with the new
[874.18 → 879.52] post-quantum stuff, and we would like to know before a large part of testing for this is really
[879.52 → 885.90] just be interoperability with other implementations of ml chem I think you know chrome has landed an
[885.90 → 892.76] implementation I think Firefox has an implementation open SSL almost definitely has an implementation so
[892.76 → 899.38] it's more just figuring out is there some corner case between the go implementation and one of the
[899.38 → 905.60] multitude of other implementations out there that will cause something to explode spectacularly
[905.60 → 911.46] we will be using the go the bugs that I think we talked about in one of the episodes so whether we
[911.46 → 917.80] turn it on by default or not will depend on the go line in your go mod which is something I feel like
[917.80 → 921.92] we should communicate much better because you can install the release candidate, but you will still
[921.92 → 926.98] not be testing the thing unless you change the go mod line but on the other hand to test the
[926.98 → 936.18] release candidate it's as easy as writing go 1.23 rc1 in your go mod file and go will automatically go
[936.18 → 944.02] fetch the new thing from the modules proxy and will automatically run the new version we
[944.02 → 949.20] really should write more about how all of that works because I see Roland being like is that how it
[949.20 → 956.04] works and I was going to say there is an I think Russ cox wrote a whole long blog post about this I was
[956.04 → 962.14] just I was trying to figure out can you put rc1 in your okay interesting I didn't know that
[962.14 → 969.16] yeah it's a thing you can do you can just you know change that line in the mod uh kick off CI
[969.16 → 975.90] and in theory should just run the RC yeah I mean this probably also tells you about how much i
[975.90 → 981.70] write actual go modules rather than I might kind of my day is spent in the standard library in such a
[981.70 → 985.70] way that I'm slightly ignorant of how a lot of the tool chain works for normal people
[985.70 → 1000.46] what's up friends and party people I'm here with my good friend over at speakeasy founding engineer
[1000.46 → 1006.36] George Hadar speakeasy is the complete platform for great API developer experience they help you
[1006.36 → 1012.92] produce SDKs terraform providers docs and more George take me on a journey through this process
[1012.92 → 1020.66] help me understand exactly what it takes to generate a SDK for an API at the quality level required for
[1020.66 → 1027.48] good user experience good dev experience the reality is the larger your API becomes the more
[1027.48 → 1035.38] you want to support users that want to use your API and to do that your instinct will be to ship a
[1035.38 → 1040.46] library a package and what we've been calling a SDK there's a lot of effort involved in taking
[1040.46 → 1045.92] an API that lives in the world and creating a piece of software that can talk to that API
[1045.92 → 1052.50] building SDKs by hand is a significant investment and a lot of large companies might pour a lot of
[1052.50 → 1058.48] money into that effort to create something that's like approaches good developer experience
[1058.48 → 1066.38] and then another group of a more growing group of companies will rely on tooling like code generators
[1066.38 → 1072.04] and so they're very interested in like once you make the decision to use a code generator you're
[1072.04 → 1077.62] kind of forfeiting some of your own opinions and what you think a good developer experience is because
[1077.62 → 1083.32] you're going to delegate that to a code generator to give you a SDK that's that you think users will
[1083.32 → 1089.40] enjoy using, so there's various open sources tooling out there that can do a version of what you do
[1089.40 → 1095.28] how much research have you all put into doing it at a quality level that is enterprise API ready
[1095.28 → 1100.14] a lot of the customers that we've spoken to didn't have that experience so they went to
[1100.14 → 1104.92] to code generators they tried to point them at their APIs and tell them give me a SDK
[1104.92 → 1110.02] and the outcome wasn't great like it didn't support some of the features in open API
[1110.02 → 1116.42] or the code that it was generating was not idiomatic typescript we didn't boldly think we're
[1116.42 → 1121.62] we're gonna we're going to solve this better than everyone else the reality is that that's where we
[1121.62 → 1126.44] came in we surveyed all the things that have happened in JavaScript over the last few years all the
[1126.44 → 1133.06] incredible projects like God for example and the web platform APIs that are now like broadly supported
[1133.06 → 1138.92] like the fetch API the web streams API we kind of saw this and said there's a great opportunity to mix
[1138.92 → 1145.14] all these together and create a best experience you can get out of a code generator for users
[1145.14 → 1149.40] okay so paint a picture what's a good next step what can people expect when they go to
[1149.40 → 1156.52] speak easy api.dev if you're coming across speak easy today, and you want to use it you will go through
[1156.52 → 1162.32] the onboarding flow and at some point you're going to give us an open API document that's your description
[1162.32 → 1168.36] of your API, and we're going to take that document and turn it into a SDK of your choice you're going to
[1168.36 → 1172.58] get to pick which language is your first language that's the one you'll get for free and at that
[1172.58 → 1179.50] point you can publish that package to for the world to use that's going to be yours it's uh you get to
[1179.50 → 1185.18] license that however you want and then carry on from there the way you iterate now is you keep
[1185.18 → 1190.76] changing your ap open API document so as you develop your back end you're going to produce alongside that
[1190.76 → 1196.34] the open API document with any updates over time and evolve that and as you're evolving that we're
[1196.34 → 1202.34] generating the SDKs and publishing them for you and that also includes rich documentation that goes
[1202.34 → 1208.88] with them so we're asking you to put a lot of effort just into describing your API, and we're going to do
[1208.88 → 1215.92] a lot of the heavy lifting that follows from that okay so as George mentioned go to speak easy api.dev
[1215.92 → 1222.90] you get your first SDK for free, so cool once again speak easy api.dev
[1222.90 → 1244.80] is there also a plat speaking of ml chem is there a has had the ssh people specified using
[1244.80 → 1252.60] ml chem in open ssh is that something we have thought about I think this will be added later
[1252.60 → 1263.56] uh currently uh I'm I know about AWS in it saws transfer family for SFTP already supporting
[1263.56 → 1273.72] post quantum algorithm but open ssh still not does not ship this support and uh we have spoken about
[1273.72 → 1280.52] this with Philippe some time ago, and we will, we'll try to support a post quantum algorithm
[1280.52 → 1290.04] post quantum case exchange after open ssh ship with uh with the release or uh ship to their uh gap
[1291.48 → 1303.08] today gap repository for the portable open ssh, and it's also since uh this new uh crypto algorithm
[1303.08 → 1308.36] uh is also very important to uh it's also very important to uh it's also very important to uh
[1308.36 → 1318.92] move a crypto ssh from crypto to go itself so it can use the internal import to use this new
[1318.92 → 1327.72] algorithm it would be an interesting development and uh also for ssh it would be interesting to
[1327.72 → 1335.24] check the interoperability with other implementation mainly, mainly open ssh the leading implementation
[1335.24 → 1343.96] but also AWS and other implementation that will add post quantum support in the meantime yep by the way
[1343.96 → 1351.40] uh open ssh I think has a different algorithm that's post quantum uh because they picked it way before
[1351.40 → 1358.28] NIST made their choice, and they did not pick what NIST ended up picking so we're not implementing you
[1358.28 → 1366.76] know the other one and then cyber or ml cam which is just you know the boring name for cyber because we
[1366.76 → 1373.64] can't have nice things so NIST renamed it yeah did they pick one of the lattice based ones or yeah uh cyber
[1373.64 → 1381.08] being the lattice based uh oh sorry open ssh yeah open ssh had uh NTRU okay which is
[1381.08 → 1386.36] another one of the lattice based ones so really there's no good reason to use one or over the
[1386.36 → 1394.60] other it's just a historical yeah they just got there first yeah uh and regrettably yeah I think
[1394.60 → 1403.32] it's already there since two years it's a long time it's not uh recent as addition and has anyone
[1403.32 → 1409.64] other than open ssh implemented this key exchange or I'm not aware of any other implementation but
[1409.64 → 1419.72] okay not shocking but indeed but Nicola mentioned something about x crypto and crypto which is a
[1419.72 → 1426.36] thing that we have two proposals out to get to, and you know maybe we'll start doing some of that in
[1426.92 → 1435.40] 123 maybe not but my proposal is about deprecating a bunch of packages because I still like to go around
[1435.40 → 1442.12] we've made the predation hammer I'm not done yet and there are a few things left in x crypto that I did
[1442.12 → 1449.40] not get last time around and I am getting this time around and after that cleanup it's partially aimed to
[1449.40 → 1456.60] making your proposal possible Roland yeah so the other big proposal we have is there's kind of this
[1456.60 → 1465.48] long history of the golang.org slash x crypto module which everyone seems extremely confused about
[1465.48 → 1473.56] what the purpose is it kind of exists as a historical artifact of people on the team at the time just
[1473.56 → 1480.68] needing a place to put code that they were working on and over time it has slowly morphed into a selection
[1480.68 → 1486.84] of incredibly important packages that the standard library relies on and then a handful of things of
[1487.56 → 1493.96] let's say dubious quality that we have slowly been trying to deprecate or freeze or kind of pretend like
[1493.96 → 1501.56] do not exist the last couple of years so we've proposed that we will to try and make this a slightly less
[1501.56 → 1508.92] confusing module we will just move all the code in golang.org slash x crypto that is important into the
[1508.92 → 1514.84] the standard library so you will no longer need to make the determination of you know should I be
[1514.84 → 1522.52] using this thing from this slash x repository you know does slash x mean experimental no it doesn't but
[1524.52 → 1531.56] but you know it also what it does mean is not particularly clear, so there are things in x crypto like
[1531.56 → 1541.88] x crypto ssh and x crypto CSP and x crypto crypto crypto byte that are all things that we kind of rely
[1541.88 → 1547.80] on heavily in the standard library and because of that there seems like there is no good reason not to
[1547.80 → 1555.48] have them there, so the idea is that we will slowly start to move packages out of x crypto SSA or x crypto
[1555.48 → 1561.32] into the standard library, and we will leave those packages in x crypto, but they will eventually just
[1561.32 → 1567.48] become wrappers around the packages that exist in the standard library so this won't break anyone
[1567.48 → 1573.96] who is still relying on you know those APIs never changing or that code never moving, but they will just
[1573.96 → 1580.92] transparently start using actually the standard library without knowing it and we'll get all the benefits
[1581.64 → 1589.24] of that but at the same time we have also for example for crypto ssh to refactor several things
[1589.24 → 1597.96] so the wrapper will be not one-to-one exactly one-to-one but because we need to improve some things before
[1597.96 → 1605.48] joining with the standard library and this is the reason this will not happen for one uh immediately but
[1605.48 → 1611.80] for the next go release if all goes goes goes away yeah, and we plan to do this as in kind of
[1611.80 → 1617.48] piecemeal process it will not necessarily all happen in a single release there are some things that we
[1617.48 → 1623.72] can just kind of copy and paste you know the APIs are solid and we kind of don't necessarily need to
[1623.72 → 1629.56] make any changes but like Nicola said there are things that you know had a hard life in x crypto and
[1629.56 → 1635.00] you know have developed the way they have and kind of when we move them into the standard library we're
[1635.00 → 1640.28] kind of getting a second chance to think like is there a better way that we can design this API
[1640.28 → 1648.12] which I think for many things there are we can learn from the experience and from all the bug reports we
[1648.12 → 1654.44] receive and so uh we'll do something better for we'll try to do something better for the community
[1654.44 → 1662.60] always will be something unhappy from the change, but this is inevitable we will try our best
[1663.40 → 1668.28] yeah and one of the great things about go modules is if people are really upset about
[1668.28 → 1673.56] something that we do they can just use an older version of the module unless we do unless we it
[1673.56 → 1679.16] turns out there is some massive security vulnerability in which case they may be on their own but
[1680.04 → 1684.20] try to push that thought to the back of my mind yeah you know we
[1684.20 → 1687.72] can remove all stuff like old hash functions that
[1690.12 → 1691.80] sounds like an internal joke is coming
[1693.16 → 1698.20] this is me teasing Roland about a fact that we've been uh I'm actually teasing both of them
[1698.20 → 1704.76] simultaneously because Roland has been working on getting Shawn out of crypto x509 which is the
[1704.76 → 1711.48] certificates verification library and Nicola has been working on getting Shawn out of crypto ssh
[1711.48 → 1722.84] and they have both been extremely painful yeah I think in when was Shawn signatures in x509
[1722.84 → 1730.44] certificates have been quoted unquote banned in public certificates in i.e. certificates trusted by browsers
[1731.24 → 1738.20] for must be five years now something like that it's been quite a long time people kind of saw the
[1738.20 → 1744.76] downfall of Shawn coming and started trying to replace them with more modern variants, but it turns
[1744.76 → 1748.84] out that you know and when it was kind of announced that this would happen and most certificate
[1748.84 → 1755.72] authorities had transitioned to using sha256 based signatures we decided oh well we can just get rid of
[1755.72 → 1761.80] Shawn signatures we can just remove support in the go x509 library for this you know it will cause no
[1761.80 → 1767.32] problems I'm sure uh which we did and then immediately got a lot of people shouting at us
[1768.04 → 1775.48] because it turns out that people rely on private public key a lot of private public key infrastructure like enterprise
[1776.12 → 1784.28] certificates still use Shawn, or you know they were connecting to people using point of sale terminals that had been
[1784.28 → 1791.00] designed in the 1990s and hadn't been updated since that were relying on Shawn signatures and stuff like that
[1791.00 → 1798.52] uh so we ended up adding a go debug flag that let you opt in to Shawn still verifying Shawn signatures
[1798.52 → 1805.16] 19 you know 99 of people transparently just stopped needing to support them and had the support removed and
[1805.16 → 1811.64] then we offered this flag and say if you really need this we will allow you to opt into retaining this
[1811.64 → 1817.80] behaviour and I think we added that flag about three years ago and I believe at the time when we added it
[1817.80 → 1825.08] we said oh we will remove this in one or two major releases I believe it's been about six major releases
[1825.08 → 1833.08] since we said that we have finally got to the point where as far as we can tell there is no
[1833.08 → 1841.96] major either organization or software projects still relying on this behaviour so the goal is that in 121 we
[1841.96 → 1847.64] will make it we won't make any code changes, but we will make an announcement that in 124 we are going
[1847.64 → 1854.76] going to remove this flag finally, and you will no longer regardless of what you do be able to verify
[1854.76 → 1860.44] Shawn signatures that's technically not true if you write a bunch of code you can verify Shawn signatures
[1860.44 → 1867.40] yourself but I'm not encouraging anyone to do that if you need to do that you need to go and think
[1867.40 → 1875.72] hard about what you're doing and then in 124 we will just access support, and it will be the end of a
[1875.72 → 1882.20] very long journey can you get ISO compliance using Shawn or do you have to show you're not using that
[1884.20 → 1895.40] it's possible so for FIPS uh Shawn is not an approved algorithm anymore uh it's allowed for legacy
[1895.40 → 1903.32] purposes when you're verifying existing signatures so if you have like a thing that's already signed you
[1903.32 → 1912.36] can use Shawn to verify it which means it's not disallowed from being in a module but if you still
[1912.36 → 1922.36] sign things with Shawn that is not okay any new signatures in ssh instead we already we still have
[1922.36 → 1931.72] uh Shawn as default enabled as default there are also in SSS there are very old devices relying on it
[1932.36 → 1943.48] and one of the point to move a crypto ssh within the standard library is to allow to i to disable uh
[1943.48 → 1952.12] Shawn using an environment variable so we can make the same transition described by Roland so in
[1952.12 → 1964.12] the first time there will be in the first time there will be an environment variable allowing to re-enable it and then after some release we'll remove this environment variable
[1964.68 → 1976.12] anytime after the recent development in crypto ssh we now allow to completely disable Shawn but users need to configure
[1976.12 → 1984.36] themselves in some pending work we have to be able to configure the supposed algorithm and we
[1984.36 → 1993.88] divided the algorithm in secures and in support supported and in secures if you have to explicitly enable in
[1993.88 → 2002.60] secures algorithm to have Shawn so if you import the supposed algorithm you will have uh Shawn and
[2002.60 → 2010.04] and other and other unsecured algorithm disabled we also work at to improve the things in other way for
[2010.04 → 2019.64] example we are working on exposing negotiated and supported algorithm so our user can see what device
[2019.64 → 2027.32] need to be updated before disabling an algorithm so they can plan the update, and we also simplified
[2027.32 → 2035.88] finding the algorithm by exposing in algorithm negotiation error with the algorithm negotiation error you
[2035.88 → 2044.12] will exactly know what algorithm negotiation failed what are the supported algorithm and what are the
[2044.12 → 2051.80] requested algorithm from the client or from the server and this information before this change that
[2051.80 → 2060.92] we are still working on where available as a string within the error message now instead are more structured
[2061.56 → 2073.48] the error will expose the list proper list that our user can search and match with the algorithm we exported
[2073.48 → 2083.64] so it will be much easier to understand what device what clients or server need to be updated and
[2083.64 → 2092.76] report the error to our users yep also I know that we just recently managed to fully round out support for the new
[2092.76 → 2101.80] hashes because ssh used to say oh if you're using RSA you must be using Shawn that's that's just completely
[2101.80 → 2108.12] tied, and you know ssh is a protocol that has 20 years we've learned a few things about how to do
[2108.12 → 2113.64] protocols since, and it's actually very impressive that it's still secure and still going well after
[2113.64 → 2121.32] 20 years but one of the problems it had was that you had to use Shawn to use RSA so then they split it
[2121.32 → 2128.04] and they said okay so you can use a key of type RSA but that you can use with different algorithms it
[2128.04 → 2136.12] can be with Shawn or with SHA 56 and so on and that turned out so many bugs because all over the place
[2136.12 → 2142.68] things that were supposed to send the algorithm were sending the key type and mixing them up or when
[2142.68 → 2149.00] some a certificate was in use hitting edge cases we think we hit the last one today
[2149.00 → 2158.68] uh yes hopeful the hopeful the last one will be merged in the next few days and uh it was
[2158.68 → 2168.20] a last problem when a client needs to validate the server response for the for a public key and it
[2168.20 → 2177.24] it turned out uh the open ssh implement there was a shortcut in open ssh implementation they don't validate
[2177.24 → 2186.60] the algorithm sent from the client with one received so they just validate the type and uh it was a
[2187.80 → 2197.16] a bug we had for a lot of time there are at least uh four or five open issue about this
[2197.16 → 2205.72] and because initially this bug was noticeable only with the proprietary server only recently a user
[2205.72 → 2215.48] reported as a reproducer using a node.js based ssh implementation so we can really understand what
[2215.48 → 2224.04] is going on uh compare with open ssh code which was working of course and apply the same workaround
[2224.68 → 2233.40] that violates the specification of course that's strange you have to love the uh archaeology aspect of this
[2233.40 → 2240.84] because what happened is that the spec was changed then open ssh implemented the spec correctly
[2240.84 → 2247.16] on one side but on the other side to make their job easier they made it more lenient, but you know
[2247.16 → 2253.88] that just means that they supported more things so, so far so good right but since open ssh supported that
[2253.88 → 2260.28] other implementations started making the mistake and open ssh would not catch them so nobody would notice
[2260.28 → 2267.32] and then they would use go against that which does the right thing and that would end up in a bug for
[2267.32 → 2275.24] us like there's just a whole history of protocol evolution uh that that led us to this moment
[2276.60 → 2279.56] let's hope we have fixed all the bugs now
[2282.20 → 2287.56] this mismatch between the type and the algorithm type I hope it's the last one
[2287.56 → 2293.72] we've been waiting to write up the triumphant announcement that you can finally turn off
[2293.72 → 2299.72] sha1 and that the sha2.56 is completely supported, and we've had this endless tale of
[2302.60 → 2309.56] bugs speaking of protocol bugs something I'm very excited about and that I was supposed to do years ago
[2309.56 → 2319.16] and I haven't done yet is for TLS instead setting up our tests to run the boring SSL test suite against
[2319.16 → 2326.12] our implementation the test suite is called BOGO and uh Roland you were just working on that yeah it's
[2326.12 → 2334.20] it's fascinating I think you know TLS is a really complicated specification, and it's kind of
[2334.20 → 2340.76] additionally complicated by the fact that it while it over specifies a lot of things is also under
[2340.76 → 2347.64] specifies some things, so there are a lot of corner cases where you kind of get weird interoperability
[2347.64 → 2356.60] bugs and boring SSL is kind of the de facto TLS implementation now basically because it is what
[2356.60 → 2363.56] chrome runs so it you know it has gotten probably you know handled more TLS handshakes than arguably any
[2363.56 → 2370.12] other software I don't know if someone will probably argue with me about that but um and so that it's
[2370.12 → 2376.36] kind of the golden implementation for TLS, and they have this giant test suite that you know was originally
[2376.36 → 2382.04] just for boring SSL, and it would test you know every single protocol behaviour that they could think of and
[2382.04 → 2389.40] had kind of regression cases for tons of bugs that they had seen and at some point um David Benjamin one
[2389.40 → 2395.48] one of the engineers worked on it to make it in you know to make the test suite applicable to other TLS
[2395.48 → 2406.20] stacks so you can, you know wire up this complicated system to run a go TLS client or a go TLS server
[2406.76 → 2415.24] against a kind of modified version of what it turns out is the go TLS stack which is written in a way to
[2415.24 → 2423.88] kind of introduce bugs and cause strange behaviours so that you can kind of see is your TLS stack actually
[2423.88 → 2430.52] doing the right thing we've had this long-running plan to kind of make the know integrate this
[2430.52 → 2438.04] to test the act the real go TLS stack because it is it's really hard to test you know it turns out that
[2438.04 → 2444.92] there are so many different things in TLS that you could do either correctly or incorrectly and trying
[2444.92 → 2451.40] to manually write unit tests for every single possible behaviour across you know three or four
[2451.40 → 2457.80] different versions of TLS and with you know three or four different types of keys or certificates or
[2458.84 → 2465.40] all of this is just you know too it's impossible for a single person to do so BOGO is hopefully going
[2465.40 → 2472.76] to eventually replace a lot of our TLS tests and instead of kind of writing individual unit tests
[2472.76 → 2479.40] ourselves we can then go and contribute tests to the BOGO test suite which is also you know the test
[2479.40 → 2487.24] boring SSL, but it is also used for rust TLS which is one of the largest rust TLS stacks and I think one
[2487.24 → 2493.00] of the python ones also uses it there's a handful of people who are using it so it lets us kind of not
[2493.00 → 2499.24] only you know test ourselves better but it also kind of allows for the TLS ecosystem to slowly converge
[2499.24 → 2503.88] on like what is the right answer for some of these things you know there is when I first ran the BOGO
[2503.88 → 2510.12] test suite one of you know there were a number of real bugs which we fixed uh but the vast
[2510.12 → 2515.72] majority were you know when uh when you encounter an error in TLS you send what's called an alert
[2515.72 → 2522.60] which is like a small you know it's a single I think u in eight or u in 16 that indicates what it
[2522.60 → 2527.56] was that went wrong during your TLS handshake and a lot of in the TLS specifications a lot of these are
[2527.56 → 2532.36] underspecified it's like oh you abort the error you abort the connection, but you don't know one ever
[2532.36 → 2538.52] says what alert do you send so when we ran these tests we got like 100 or 200 errors that say you're
[2538.52 → 2544.28] sending the wrong alert when this thing happens and i I went and I talked to David Benjamin who
[2544.28 → 2552.36] wrote a lot of these tests I said well why did you pick this alert and his response was just it's just
[2552.36 → 2559.32] what made sense and you know i could probably sit down and argue for a good hour or so
[2559.32 → 2564.44] about why some of the alerts we picked were better than the alerts that he picked but in reality it
[2564.44 → 2570.04] matters this is not important to anyone it's probably more important that we do the same thing that boring
[2570.04 → 2577.16] SSL does than you know being semantically correct about which alert you're sending in general I'm a very
[2577.16 → 2583.48] big fan of this sort of test sharing because I really think that things that have specifications
[2583.48 → 2589.00] which cryptography a lot of things have specifications should share test vectors because there's no good
[2589.00 → 2596.28] reason what we do is not useful to others uh especially in cryptography there is no a good reason the
[2596.28 → 2605.00] what we test is not useful to others and what others are testing is not useful to us so we have there been a
[2605.00 → 2611.56] couple projects like that one is uh white proof uh which is the named after the smallest mountain in
[2611.56 → 2620.04] the US uh in the spirit of setting achievable goals which was a project that was started at Google by
[2620.04 → 2626.68] Daniel blackenbacher and others and has now moved into a community project that I'm part of called
[2626.68 → 2634.52] CSP, and we're going to try to make that into a repository to share test vectors across implementations
[2635.00 → 2641.40] and bogus I think a very good example of that working out I'll have to correct you
[2642.20 → 2650.04] very quickly not America Australia wait really yeah mount white proof is in Australia yeah it's in
[2650.04 → 2659.24] Victoria oh, oh very important I think I've been saying this for a while now I've been spreading fake news
[2659.24 → 2666.04] news I think it's I think it's also witched witch proof but then you can choke up to my Italian
[2666.04 → 2671.80] accent whatever yeah if you showed that to an American that's probably what they would say as well so
[2672.52 → 2676.76] fair enough fair enough but yeah huh I placed it completely on the wrong side of the world
[2676.76 → 2685.56] cool uh I'm trying to think what other uh go 123 things are there and I think there's the crypto
[2685.56 → 2693.32] rand changes and I can't think of anything else and crypto rand is the package that you use to get
[2693.32 → 2700.76] random bytes out of, and it's mostly fine like it's not really one of the things that makes me think oh
[2700.76 → 2706.68] no I wish I could change things in the standard library so much, but it also has a few things we
[2706.68 → 2713.00] can make a little better and I'm thinking of doing just a single pass in this release and just clean
[2713.00 → 2719.00] up all the things and the first one is that was actually an idea that came from Rask which was
[2719.00 → 2724.04] very entertaining because I was like hey Rask can I make a new API in crypto run that doesn't return
[2724.04 → 2729.40] an error and just panics if it gets an error because it would be much more usable and I'll tell you all
[2729.40 → 2735.88] what API was, but usually he's the one that argues for being more conservative right, and so I expected
[2735.88 → 2741.16] him to be like well I don't know like how often is that going to panic, and instead he was like
[2741.16 → 2748.44] hmm really why does crypto rand ever return an error and like well yeah that's that's a good point you
[2748.44 → 2755.96] know we're using the system calls on modern Linux and well I guess iOS could be a problem and he
[2755.96 → 2762.52] basically told me look if you can fix it so that it almost never fails we could just make it throw
[2762.52 → 2767.48] and if you've never heard about what a throw is in go, and you're about to say wait go doesn't have
[2767.48 → 2773.64] exceptions there's no throwing in go no, no there is a function called throw it's an internal runtime
[2773.64 → 2778.44] function that just crashes your program and there's nothing you can do about it
[2778.44 → 2786.84] because that's to make sure that nobody tries to set up recover around it because there's nothing to
[2786.84 → 2794.68] recover and I went in there and I changed how we get a random bites on macOS because I texted you know
[2794.68 → 2800.68] friends at fruit companies that shall go unnamed and I asked okay so what should we use on your
[2800.68 → 2806.44] platform, and they're like yeah you know that that one is much faster and never turns an error would you look
[2806.44 → 2811.64] at that and so now we have random bites that basically never return an error if you're curious
[2811.64 → 2817.24] that there's this long proposal that spells it all out, and so we're just going to make a throw and
[2817.24 → 2823.16] crash the program if you're in a very weird corner case in which you misconfigured your system so much
[2823.16 → 2829.00] that even with all of that we can't get random bites and that makes me deeply happy
[2829.00 → 2839.64] so that's going to be fun then I want to make it a little more efficient by not causing it to escape the
[2839.64 → 2846.76] bytes slice you pass it into the heap so that you can avoid allocations I want to make it not import math
[2846.76 → 2852.36] big or at least I want to make an internal version of crypto run that doesn't import math big so that I can
[2852.36 → 2859.24] stop some packages that in the standard library that need random bytes and don't need math big which
[2859.24 → 2865.32] we talked about in the other episode I can make sure that they don't import it at all and yeah you
[2865.32 → 2870.20] know a few little changes like that I feel like there was at least another one oh yes and there's the
[2870.20 → 2877.40] new the new API which is going to be something you give it char set and can give you a random string
[2877.40 → 2883.80] made of those characters so you can generate things like passwords and tokens and stuff like that
[2884.36 → 2889.08] and I want to make it an API that you don't configure at all you just give it the char set
[2889.08 → 2895.88] and it gives you back a string using those characters that's long enough to be secure and then if you know
[2895.88 → 2900.60] what you're doing you can slice it down and make it shorter because it doesn't return an error so you can
[2900.60 → 2908.68] just put the slice operant right after and yeah so fun stuff with uh crypto randomness
[2908.68 → 2913.16] exactly I'm thinking of all the weird password requirements that I've seen on websites it's
[2913.16 → 2922.52] like it can only have one digit uh oh wow yeah if it can only have one of something oh actually you
[2922.52 → 2927.64] know my position on those is that the answer is that it's a bad idea I mean it's a bad idea but also
[2927.64 → 2934.28] you solve that by just generating a password that's just alpha uh like letters and at the end
[2934.28 → 2942.12] you put exclamation point a one and uh capital a and if anybody gives you grief for it, you can
[2942.12 → 2949.24] you can tell them Filippo said it's okay they can be pissed at me this is okay yeah I'm i can
[2949.24 → 2954.52] get behind that yeah speaking of how arcane those rules are I ran across a very fun I forget where this
[2954.52 → 2961.40] was browser game that somebody wrote where it was the goal of the game was to input a syntactically
[2961.40 → 2967.80] valid password and each time you got it right it would introduce a new even more arcane rule that you
[2967.80 → 2974.28] had to follow it's like all the numbers in your password must add up to a prime larger than
[2976.28 → 2983.48] something it got really hard I don't think I ever finished it, but you know I have seen some pretty
[2983.48 → 2991.80] crazy rules on passwords so it's good training yeah there's also that game of prompt hacking
[2992.28 → 2996.04] that you have to convince it to tell you that yeah oh god
[2998.20 → 3004.28] many things are included in 123 wow we covered a lot yeah now when we started this I was thinking oh
[3004.28 → 3010.28] we don't actually have that much this is a pretty boring release cycle, but we've managed to fill in
[3010.28 → 3014.12] an hour so that's a good yeah that's a good indication that maybe there's actually more than
[3014.12 → 3020.44] I thought there was I I do this every time too i I learned that we actually did a bunch of stuff as
[3020.44 → 3026.92] I prepare either these episodes or the cryptography State of the Union talks uh which by the way i just
[3026.92 → 3033.08] got the email yesterday that it's part of the going to be part of the program at gophercon us so if you
[3033.08 → 3040.12] if you want to hear basically all of this stuff but again with slides and I don't know just me being
[3040.12 → 3047.16] very excited on stage that that's an option Felipe wearing a suit yes also that uh with an um with a
[3047.16 → 3055.16] gopher uh enamel pin on the lapel it's the most important draw it you know it's the small to go first
[3055.16 → 3063.08] um also uh we're still waiting to hear about lining talks but Nicola you've submitted a lining talk right
[3063.08 → 3073.88] yes uh writing talks to speak about the state of crypto ssh but I still haven't uh a replay from
[3073.88 → 3082.52] gophercon I hope it will be accepted so I can uh speak also there about the crypto ssh and the improvement
[3082.52 → 3092.68] we are doing in um in this year and the new API for the uh with the new version that will
[3092.68 → 3099.72] hopefully include in the standard library let's hope let's try fingers crossed yeah there will be
[3099.72 → 3108.20] also a talk by economic on the analysis that were done around go vulnerabilities also the lots of
[3108.20 → 3112.28] security this year I think it's perfect all the conferences are going to be putting this
[3112.28 → 3116.84] important focus on things that talk in particular will be fascinating we've we've been putting
[3116.84 → 3123.00] a lot of work into vulnerability analysis and I think you know not not to toot our own
[3123.00 → 3129.80] horn but I think go currently has probably the most advanced vulnerability analysis tooling out there and
[3129.80 → 3135.88] it's still you know essentially in beta so I think there is you know there will be a lot of value there for
[3135.88 → 3144.76] for developers people are often worried about vulnerability not real vulnerability for example I remember some
[3144.76 → 3157.40] people asking us to update net http in x crypto repository, but it was basically unused so even if that
[3157.40 → 3164.84] package was vulnerable that vulnerability is not exploitable in crypto ssh it was used
[3164.84 → 3173.40] only marginally in the package this is very, very hard to explain to people because they run a
[3173.40 → 3182.36] an automatic scanner and the automatic scanner triggers the vulnerability, and they are uh alarmed they want
[3182.36 → 3189.72] all the vulnerability fixes very quickly but by doing so there is the risk that we introduce
[3189.72 → 3198.28] the untested features because we are always on the plaguing gauge, or we always use a new package that
[3198.28 → 3208.04] people haven't enough time to test and to about regression and so on and such things yeah this is
[3208.04 → 3215.56] basically an ad for goon check I think I can do it in like radio style um do you have issues with a lot of
[3215.56 → 3221.40] vulnerability reports clogging your uh pipeline do you wish your signal-to-noise ratio was better call
[3221.40 → 3231.24] goon check that is goon check anyway uh and uh coming to the go tool chain at some unspecified point in
[3231.24 → 3236.68] the future ask your engineer if uh beta software is right for you
[3236.68 → 3242.52] uh do test the release candidate anyway yes please
[3245.16 → 3250.12] yeah especially if you do strange things if you have the stranger your code is the more you should test
[3250.12 → 3255.32] the release candidate and tell us when you break things were you harmed by a release candidate there
[3255.32 → 3261.88] might be compensation for you in the form of backfires this the compensation might not be available after
[3261.88 → 3268.92] the date of the release i have to stop now an interesting thing i discovered
[3268.92 → 3276.76] recently is for example on Debian there are fixable vulnerability and unfixable vulnerability because
[3277.32 → 3286.36] Debian developer choose to not backport some vulnerability fix initially was really surprised because
[3286.36 → 3293.88] the vulnerability scanner for my docker image for my of open source project they posted
[3293.88 → 3304.44] vulnerability but i I checked and i I found that I was I all uh update were applied were already applied
[3304.44 → 3312.60] so I was so surprised to see this vulnerability then i I discovered these things about Debian so
[3312.60 → 3320.76] basically everyone publishing a docker image or the things like this is forced to use something like
[3320.76 → 3329.56] this or less because this way you only ship your go application with no dependencies and so you avoid
[3330.12 → 3335.56] this false positive or this fake vulnerability warning
[3342.60 → 3353.16] if you're anything like me, you have a certain tendency to put things off until the very last
[3353.16 → 3360.68] minute seeing the dentist going to the doctor home improvements that never ending chore list of yours
[3360.68 → 3365.64] and while most of the time it works out just fine the one thing in life that you really could not afford to
[3365.64 → 3372.12] wait on is setting up term coverage life insurance you've probably seen life insurance commercials on TV and
[3372.12 → 3378.20] thought yeah I'll look into that later no later doesn't come this really isn't something you can wait on
[3378.36 → 3384.92] choose life insurance through a ladder today here's what we love about ladder and why we allow them as a sponsor
[3384.92 → 3392.52] they are 100 digital no doctors no needles no paperwork when you apply for three million dollars in coverage or less
[3392.52 → 3399.92] just answer a few questions about your health in an application ladders customers rate them 4.8 out of 5 stars on trust pilot
[3399.92 → 3406.24] and they made forbs best life insurance 2021 list you just need a few minutes and a phone or laptop to apply
[3406.24 → 3412.16] ladder's smart algorithm works in real time so you'll find out if you're instantly approved no hidden fees
[3412.16 → 3419.44] you can cancel anytime get a full refund if you change your mind in the first 30 days ladder policies are
[3419.44 → 3427.92] issued by insurers with long proven histories of paying claims they're rated a and a plus by am best
[3427.92 → 3434.56] finally since life insurance costs more as you age now yeah right now's the time to cross it off
[3434.56 → 3442.24] your list so go to ladder life.com slash changelog right now to see if you're instantly approved that's
[3442.24 → 3448.24] l-a-d-d-d-e-r life.com slash changelog
[3448.24 → 3458.48] I actually think
[3458.48 → 3478.88] so who has an unpopular opinion okay my unpopular opinion is that you should pay for open source software you rely on
[3478.88 → 3485.68] of course you can use open source software for free but maintaining and evolving it is not free
[3485.68 → 3491.52] it requires a lot of time and effort, and you should learn to recognize the value of this work
[3492.32 → 3498.64] if you use an open source software at your company then it would make business sense to sponsor that
[3498.64 → 3506.00] project to ensure it is healthy and well maintained you should not think I will use it for free and
[3506.00 → 3515.68] someone else will pay for me too let's look at recent CWE what do you see maybe the oz backdoor
[3516.40 → 3522.80] now you understand what can happen if an open source software is not maintained or poorly maintained
[3522.80 → 3528.88] open source maintainers are generally passionate developers when joining sharing their work with
[3528.88 → 3535.76] the community but if they can't pay their bills their problem could be passed on to you and your
[3535.76 → 3542.72] company, and you can lose money a lot of money what do you do if you find a critical problem in
[3542.72 → 3550.48] open source software you are using do you open a github is where why don't you start
[3550.48 → 3558.88] supporting their work instead and establish a channel of mutual access and trust this way you will make your
[3558.88 → 3566.72] business interest because the open source project will be long sustainable in the long run and what
[3566.72 → 3574.64] will happen the developer will work on it full-time, and therefore you'll get an even better software this
[3574.64 → 3583.44] is a win-win, but this is something really easy to understand, but many people in company miss it
[3583.44 → 3593.36] and another thing maybe my real unpopular opinion is that often I get as open source maintainer and I think
[3593.36 → 3601.28] I'm not alone email like this we would like to pay for this feature to be added depending on the price
[3601.28 → 3609.92] obviously, but this is really annoying you should pay for ongoing maintenance not to add a nice feature that is
[3609.92 → 3618.00] only useful to you and maybe only work for your specific use case and at the same time you try to
[3618.00 → 3625.04] negotiate the lowest possible price and after this feature is added what happened that the
[3625.04 → 3634.40] open source maintainer have to maintain it forever this is most people in company are unable to understand
[3634.40 → 3640.96] this field I'm sorry if I was too passionate but as open source maintainer this is something
[3640.96 → 3649.12] that I deal with every day and what I feel inside all right since we're going on open source maintenance
[3649.12 → 3655.52] I'll pick one that is not about elliptic curves and I'll do the tail on that I agree with Nicola the other
[3655.52 → 3663.52] thing that often annoys me which I think lots of people who are very well-meaning a step into it is when
[3663.52 → 3671.60] people say oh we want to help the project so we always contribute our patches up and I can see
[3671.60 → 3680.64] Roland going like yes that's the thing that does not make the project more sustainable that sometimes
[3680.64 → 3685.68] makes the project less sustainable because now the maintainer has to review the patch and if it's a
[3685.68 → 3691.20] feature like Nicola was saying has to review the feature and maintain the feature forever now it's a good
[3691.20 → 3696.64] thing about open source like you're contributing to the general open source community and ecosystem
[3696.64 → 3704.48] it's a good thing and I think we all here are drawn to open source as this collective activity, but it's
[3704.48 → 3713.12] not helping the project itself it's not helping the project maintainers because they will still have to
[3713.12 → 3719.44] review it will still have to do a bunch of work later on so it's a good thing, but it does not solve the
[3719.44 → 3724.64] same problem and this comes up often because I say you know things that sound like what Nicola said and
[3724.64 → 3730.16] then people are like oh yeah we agree we care a lot we always contribute our patches and I'm like
[3731.60 → 3736.40] which is not to say that you only have to send money like there's a lot of things you can do to help the
[3736.40 → 3742.72] maintainers like you can go through issues and do the initial triage you can figure out what is the
[3742.72 → 3748.40] correct behaviour for an issue you can find out what the spec sometimes says i just you know look
[3748.40 → 3753.36] at an issue and decide that I am not looking into that today because it's way too complex and then i
[3753.36 → 3757.68] come back a week later and somebody went like oh yeah that happens because of this code over here does
[3757.68 → 3763.84] this thing and then the spec says that but actually open ssh before that version and after that version or
[3763.84 → 3768.96] like I don't know open SSL does that with TLS and that's what's happening and that's great when that
[3768.96 → 3776.00] happens that actually does make the load on me as a maintainer much, much lighter wow I feel like
[3776.00 → 3782.32] we've had two incredibly important and philosophical opinions here and I'm gonna just be incredibly silly
[3782.32 → 3789.92] now I have a very basic unpopular opinion which is I feel like becoming more and more unpopular as time
[3789.92 → 3797.04] goes on which is that I think for 90 of time I spend on the computer I would prefer to use a desktop pc
[3797.04 → 3804.88] or mac or whatever than a laptop i kind of like I part of what I hate about laptops is that
[3804.88 → 3810.56] they're portable and that you can take them anywhere and use them at any time I really like just having
[3810.56 → 3816.32] my computer in one place and heavy enough that I cannot pick it up and put it in my bag and be forced
[3816.32 → 3825.52] to do work you know down the street when I go to do something else less less time on the computer perhaps is
[3825.52 → 3837.52] better than there's the GitHub app yes I like it put the computer in a box close the box is a
[3837.52 → 3843.92] room we do not go into that room we do not speak of that room there was a period where I was strongly
[3843.92 → 3850.96] considering buying one of those time activated safes that I could, you know put a computer into but
[3852.96 → 3860.72] unfortunately I do still get sometimes paged, so this could be dangerous open that safe only with a code
[3860.72 → 3869.36] from the pager yeah then it's only when you really have to that's a product that you can use a safe with
[3869.36 → 3874.00] pager duty integration I would be surprised there's not already something like that
[3876.40 → 3881.84] my unpopular opinion is around pigeons I recently read a tweet that changed my entire perspective on
[3881.84 → 3888.24] them because for a while for the longest time I was looking at pigeons as like it's not nice to say but
[3888.24 → 3895.12] flying rats but then that tweet was very long and was describing how humans used pigeons for hundreds
[3895.12 → 3900.40] of years and breathed them exactly to be like our mail carriers until one day we got technology to fix
[3900.40 → 3905.04] that, and now they're just like depend on us, but we didn't do any proper off-boarding let's say
[3906.48 → 3912.80] so actually it's not their fault pigeons are okay I'm with you on that one I'm team pigeon but also
[3912.80 → 3919.92] rats are nice what's what's the yeah what's wrong with rats it's a rat pet of yours that's cool but if it's a
[3919.92 → 3926.96] rat that like it's into the foundation of your house or just lives in the inner garden of your
[3926.96 → 3932.80] building then it's too much hygiene questions unfortunately but yeah if it's a pet rat that's
[3932.80 → 3940.24] cool uh living in New York i I still remember mike the rat that used to live at the 59th street station
[3940.24 → 3947.36] it was actually reassuring like most of the time I would go to uh at war
[3948.80 → 3954.64] japan has the loyal dog that stays at the station New York has the loyal rat
[3957.44 → 3964.00] yes cool okay that was a very interesting episode the third one in our series six months after the
[3964.00 → 3968.48] first one and I hope the next one will be in like two or three months when we can discuss cool stuff
[3968.48 → 3977.44] again I'm sure there will be more it never stops no, no we must align with the go release cycle
[3979.60 → 3981.12] yeah I think we essentially already have
[3983.44 → 3990.16] yeah Roland and I are not uh admitting to it, but really we're doing this instead of uh release planning
[3991.44 → 3994.24] can just say like release notes linked to this episode you're good
[3994.24 → 3999.60] yeah we get into the episode, and we talk about stuff, and then we look at the notes and that's
[3999.60 → 4003.76] what we're gonna work on if you have questions meet me at gophercon yeah
[4006.00 → 4010.64] well thanks everyone, and thank you three for joining us thank you thank you
[4012.32 → 4018.40] all right that's our show thanks for hanging with us subscribe now if you haven't yet headed to
[4018.40 → 4025.20] go time dot FM for all the ways or search for go time wherever you get your podcasts you'll find
[4025.20 → 4029.84] us if you're a fan of go time and get value from the pod share the show with your friends and
[4029.84 → 4035.92] colleagues and if you really dig it hook us up with a five-star review we appreciate it thanks once
[4035.92 → 4041.92] again to our partners at fly.io to our beat freaking residents break master cylinder and to our friends at
[4041.92 → 4048.72] sentry save 100 bucks off their team plan when you use code changelog during signup that's all for now
[4048.72 → 4052.72] but we'll talk to you again next time on go time
[4052.72 → 4070.80] guys
[4070.80 → 4075.44] shame
